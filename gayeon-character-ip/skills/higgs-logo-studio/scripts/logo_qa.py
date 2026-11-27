#!/usr/bin/env python3
"""
로고 검수 + 파생본 생성. 크레딧을 쓰지 않는다.

    python logo_qa.py <이미지> --outdir <폴더> --name <브랜드명>

만드는 것:
    <name>_transparent.png   투명 배경
    <name>_mono.png          흑백 (도장·자수·단색 인쇄)
    <name>_square.png        정사각형 (SNS·앱 아이콘)
    <name>_qa_sheet.png      검수 시트 (흰 배경 / 어두운 배경 / 흑백 / 32px)

판정하는 것 (stdout에 경고로):
    1. 32px에서 형태가 남는가
    2. 흑백으로 만들면 요소가 구분되는가
    3. 어두운 배경에서 보이는가
    4. 배경 투명화가 됐는가

의존성: pillow, numpy, scipy
"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage

DARK_BG = (17, 24, 39)
LIGHT_BG = (255, 255, 255)


def cutout(im, tol_core=10, tol_edge=70, dilate=3):
    """배경을 투명하게. 흰색을 지우는 게 아니라 '테두리와 연결된 영역'만 지운다.

    이 구분이 핵심이다. 단순히 흰 픽셀을 지우면 로고 안의 흰 삼각형·흰 글자에
    구멍이 뚫린다. 배경은 테두리에서 이어져 들어오는 연결 영역이므로,
    거기서 flood fill 하듯 판정하면 내부 흰색은 살아남는다.
    """
    a = np.asarray(im.convert("RGB")).astype(np.float64)
    h, w, _ = a.shape

    # 배경색을 묻지 않고 테두리에서 읽는다 (흰색이 아닐 수도 있으므로)
    border = np.concatenate([a[0], a[-1], a[:, 0], a[:, -1]])
    bg = np.median(border, axis=0)
    dist = np.abs(a - bg).max(axis=2)

    core = dist <= tol_core
    lab, _ = ndimage.label(core)
    edge_labels = set(lab[0]) | set(lab[-1]) | set(lab[:, 0]) | set(lab[:, -1])
    edge_labels.discard(0)
    if not edge_labels:
        return None, 0.0  # 테두리가 배경이 아님 → 투명화 포기
    bg_region = np.isin(lab, list(edge_labels))

    # 안티에일리어싱 경계에만 부드러운 알파를 준다
    fringe = ndimage.binary_dilation(bg_region, iterations=dilate) & ~bg_region
    alpha = np.full((h, w), 255.0)
    alpha[bg_region] = 0
    alpha[fringe] = np.clip(dist[fringe] / tol_edge, 0, 1) * 255

    # 경계색 복원: 관측색 C = α·F + (1-α)·B  →  F = (C - (1-α)·B) / α
    # 이걸 빼먹으면 경계가 배경색을 머금은 채 남아서, 어두운 배경에 얹었을 때
    # 흰 테두리(할로)가 뜬다.
    rgb = a.copy()
    af = (alpha / 255.0)[..., None]
    m = fringe & (alpha > 8)
    with np.errstate(divide="ignore", invalid="ignore"):
        F = (a - (1 - af) * bg) / np.maximum(af, 1e-6)
    rgb[m] = np.clip(F[m], 0, 255)

    out = Image.fromarray(
        np.dstack([rgb.astype(np.uint8), alpha.astype(np.uint8)]), "RGBA"
    )
    return out, float(bg_region.mean())


def trim_and_square(im, pad_ratio=0.08):
    """로고를 잘라내 정사각 캔버스 가운데 놓는다 (여백 균등)."""
    bbox = im.split()[3].getbbox()
    if not bbox:
        return im
    logo = im.crop(bbox)
    side = int(max(logo.size) * (1 + pad_ratio * 2))
    canvas = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    canvas.alpha_composite(logo, ((side - logo.width) // 2, (side - logo.height) // 2))
    return canvas


def to_mono(im):
    """알파는 유지한 채 명도만. 도장·자수·단색 인쇄용."""
    g = Image.merge(
        "RGBA",
        (*(im.convert("L").convert("RGB").split()), im.split()[3]),
    )
    return g


def on_bg(im, bg, size):
    c = Image.new("RGBA", (size, size), (*bg, 255))
    c.alpha_composite(im.resize((size, size), Image.LANCZOS))
    return c.convert("RGB")


def dominant_grays(im, k=5):
    """로고의 주요 색들을 흑백으로 바꿨을 때의 명도. 두 색이 같은 명도가 되면
    흑백 인쇄에서 경계가 사라진다 — 그걸 잡기 위한 값."""
    a = np.asarray(im)
    ink = a[:, :, 3] > 200
    if ink.sum() < 50:
        return []
    px = a[ink][:, :3].astype(int)
    # 색을 32단계로 뭉뚱그려 대표색을 센다 (k-means 없이 충분하다)
    q = (px // 32 * 32)
    uniq, cnt = np.unique(q, axis=0, return_counts=True)
    order = np.argsort(-cnt)[:k]
    tot = cnt.sum()
    out = []
    for i in order:
        if cnt[i] / tot < 0.03:  # 3% 미만은 잡티
            continue
        r, g, b = uniq[i]
        out.append((0.299 * r + 0.587 * g + 0.114 * b, cnt[i] / tot))
    return out


def judge(im):
    """자동 판정 3종.

    판정은 '요소 단위'로 한다. 면적 가중 평균을 쓰면 큰 심볼이 작은 글자를 덮어서,
    이름이 통째로 사라지는 로고가 '통과'로 나온다. 실패는 대개 국소적이고,
    로고에서 국소적 실패는 전체 실패다 — 이름이 안 보이는 로고는 못 쓴다.
    """
    warns, info = [], {}
    a = np.asarray(im)
    ink = a[:, :, 3] > 200
    if ink.sum() < 50:
        return ["로고 픽셀을 거의 찾지 못했습니다. 입력 이미지를 확인하세요."], {}

    lum = 0.299 * a[:, :, 0] + 0.587 * a[:, :, 1] + 0.114 * a[:, :, 2]
    total = ink.sum()
    scale = 32 / max(im.size)

    # 요소를 먼저 '묶는다'. 워드마크는 글자 6개로 쪼개져 있지만 사람 눈에는
    # 하나의 덩어리다. 글자 간격만큼 닫아주면 단어 하나로 묶이고, 멀리 떨어진
    # 심볼은 따로 남는다. 묶지 않으면 글자 하나하나가 2% 미만이라 잡티로
    # 걸러져서, 정작 이름이 사라지는 로고를 통과시킨다.
    r = max(3, int(max(im.size) * 0.015))
    grouped = ndimage.binary_closing(ink, structure=np.ones((r, r)))
    parts, n = ndimage.label(grouped)
    major = [
        i for i in range(1, n + 1)
        if (ink & (parts == i)).sum() / total >= 0.02
    ]
    info["elements"] = len(major)

    thin_fail, dark_lost, lost_share = [], [], 0.0
    dark_lum = 0.299 * DARK_BG[0] + 0.587 * DARK_BG[1] + 0.114 * DARK_BG[2]

    # 판정은 요소마다 따로 한다. 전체 평균을 내면 큰 심볼이 작은 글자를 덮어서,
    # 이름이 통째로 사라지는 로고가 '통과'로 나온다.
    for i in major:
        m = ink & (parts == i)
        share = m.sum() / total
        # 획 절반 두께 → 32px에서의 굵기. 면적이 아니라 굵기를 보는 이유는,
        # 글자가 덩어리로 뭉개져도 잉크 면적은 그대로이기 때문이다.
        half = ndimage.distance_transform_edt(m)[m]
        w32 = float(np.median(half)) * 2 * scale
        if w32 < 1.2:
            thin_fail.append((share, w32))
        if np.abs(lum[m] - dark_lum).mean() <= 60:
            dark_lost.append(share)
            lost_share += share

    info["thinnest_element_at_32px"] = (
        round(min(w for _, w in thin_fail), 2) if thin_fail else None
    )
    info["elements_lost_on_dark"] = len(dark_lost)

    # 1) 32px 파비콘
    if thin_fail:
        w = min(x for _, x in thin_fail)
        warns.append(
            f"32px(파비콘·앱 아이콘)에서 요소 {len(thin_fail)}개의 획이 {w:.1f}픽셀까지 "
            "얇아져 뭉개집니다. 작은 크기에서는 심볼만 쓰는 단순 버전이 따로 필요합니다."
        )

    # 2) 어두운 배경
    if dark_lost:
        warns.append(
            f"어두운 배경(다크모드·밤 배너)에서 요소 {len(dark_lost)}개(로고의 "
            f"{lost_share:.0%})가 묻혀서 안 보입니다. 밝은색 버전이 따로 필요합니다 — "
            "특히 글자가 사라지면 이름 없는 로고가 됩니다."
        )

    # 3) 흑백 — 서로 다른 색이 같은 명도로 뭉치는가
    grays = dominant_grays(im)
    info["dominant_grays"] = [round(g, 1) for g, _ in grays]
    if len(grays) >= 2:
        gs = sorted(g for g, _ in grays)
        if any(gs[i + 1] - gs[i] < 20 for i in range(len(gs) - 1)):
            warns.append(
                "흑백으로 만들면 서로 다른 색이 같은 밝기가 되어 경계가 사라집니다. "
                "한쪽 색의 명도를 낮추거나, 흑백 전용 버전이 필요합니다."
            )

    return warns, info


def build_sheet(im, out_path):
    size, gap, top = 280, 40, 74
    panels = [
        (on_bg(im, LIGHT_BG, size), "흰 배경"),
        (on_bg(im, DARK_BG, size), "어두운 배경"),
        (on_bg(to_mono(im), LIGHT_BG, size), "흑백"),
        (
            on_bg(
                im.resize((32, 32), Image.LANCZOS).resize((size, size), Image.NEAREST),
                LIGHT_BG,
                size,
            ),
            "32px 파비콘",
        ),
    ]
    W = gap + len(panels) * (size + gap)
    sheet = Image.new("RGB", (W, top + size + gap), (244, 244, 245))
    d = ImageDraw.Draw(sheet)
    try:
        f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except Exception:
        f = ImageFont.load_default()
    for i, (p, label) in enumerate(panels):
        x = gap + i * (size + gap)
        d.rectangle([x - 1, top - 1, x + size, top + size], outline=(220, 220, 224))
        sheet.paste(p, (x, top))
        d.text((x, top - 34), label, fill=(17, 24, 39), font=f)
    sheet.save(out_path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("image")
    ap.add_argument("--outdir", default=".")
    ap.add_argument("--name", default="logo")
    ap.add_argument("--tol-core", type=int, default=10, help="배경 판정 허용오차")
    args = ap.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    src = Image.open(args.image)

    # 이미 투명한 입력이면 그대로 쓰고, 아니면 배경을 뚫는다
    if src.mode == "RGBA" and np.asarray(src)[:, :, 3].min() < 250:
        im, bg_ratio, cut_ok = src.convert("RGBA"), None, True
    else:
        im, bg_ratio = cutout(src, tol_core=args.tol_core)
        cut_ok = im is not None
        if not cut_ok:
            print("[!] 배경을 투명하게 만들지 못했습니다 (배경이 단색·플랫이 아닙니다).")
            print("    → 흰 배경 그대로 확정하거나, 힉스필드 remove_background로 폴백하세요.")
            im = src.convert("RGBA")
        elif bg_ratio < 0.03:
            print(f"[!] 배경으로 인식된 영역이 {bg_ratio:.1%}뿐입니다. 로고가 캔버스에 꽉 찼거나")
            print("    배경이 플랫하지 않습니다. 결과를 눈으로 확인하세요.")

    im = trim_and_square(im)

    p = {k: outdir / f"{args.name}_{k}.png" for k in ("transparent", "mono", "square", "qa_sheet")}
    im.save(p["transparent"])
    to_mono(im).save(p["mono"])
    im.save(p["square"])  # trim_and_square 결과가 곧 정사각형이다
    build_sheet(im, p["qa_sheet"])

    warns, info = judge(im)
    print(f"\n[검수] {args.name}")
    print(json.dumps(info, ensure_ascii=False, indent=2))
    if warns:
        print("\n[경고] 사용자에게 반드시 알릴 것:")
        for w in warns:
            print(f"  · {w}")
    else:
        print("\n[통과] 32px·흑백·어두운 배경 모두 문제없습니다.")
    print(f"\n[출력] {outdir.resolve()}")
    for k, v in p.items():
        print(f"  {k:12s} {v.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
