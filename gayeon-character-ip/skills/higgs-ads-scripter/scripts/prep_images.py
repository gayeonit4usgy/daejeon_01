#!/usr/bin/env python3
"""상세페이지 이미지를 Claude가 읽을 수 있는 형태로 준비한다.

왜 필요한가:
  한국 커머스 상세페이지 이미지는 850 x 9,000px 같은 극단적 세로 비율이다.
  Claude의 비전 입력은 긴 변 기준 약 1,568px로 축소되므로, 850x9571을 그대로
  넣으면 139x1568이 되어 글자가 완전히 뭉개진다. 용량만 크고 정보량은 0이다.

  이 스크립트는 긴 이미지를 세로로 자른 뒤 2장씩 가로로 붙인다.
  1700x1900 (비율 1:1.1)이 되어 축소 후에도 조각당 폭이 ~700px로 남아 읽힌다.
  2-up으로 붙이는 이유는 view 호출 횟수를 절반으로 줄이기 위해서다.

사용법:
  python scripts/prep_images.py <zip|디렉토리|이미지...> [--out DIR] [--chunk N]

출력:
  hero.png        — 세로가 짧은 이미지(대표컷)들을 가로로 이어붙인 것
  detail_N_M.png  — 긴 이미지 N을 자른 뒤 2장씩 붙인 M번째 조각
  그리고 무엇이 무엇인지 알려주는 매니페스트를 stdout에 출력
"""

import argparse
import re
import sys
import zipfile
from pathlib import Path

try:
    import numpy as np
    from PIL import Image
except ImportError:
    sys.exit("의존성 필요: pip install pillow numpy --break-system-packages")

Image.MAX_IMAGE_PIXELS = None  # 상세페이지는 정상적으로 거대하다

EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp"}

# 세로/가로 비율이 이 값을 넘으면 축소 시 글자가 뭉개지므로 자른다.
# 1568 * (850/h) >= 600 을 만족하는 h의 상한이 약 2,200이므로 기준을 2.6으로 둔다.
TALL_RATIO = 2.6
DEFAULT_CHUNK = 1900
OVERLAP = 60  # 글줄이 잘리지 않도록 조각 사이를 겹친다


def natkey(p):
    """imgi_9 < imgi_10 이 되도록. 다운로드 확장이 붙이는 DOM 순서 번호가
    페이지 순서와 일치하는 경우가 많아, 자연 정렬이 곧 지면 순서가 된다."""
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", str(p))]


def gif_change_strip(im, path, cols=3, pad=60):
    """GIF에서 '무엇이 변하는가'만 잘라내 프레임을 나란히 붙인다.

    한국 상세페이지는 발색 전후 비교, 텍스처 시연, N종 순환 배너를 GIF로 만든다.
    첫 프레임만 읽으면 정작 광고에 필요한 변화를 통째로 놓친다 — 톤업 선크림의
    전후 비교가 129프레임 안에 들어 있는 식이다.

    그렇다고 프레임을 여러 장 펼치면 안 된다. 848x4003 배너를 6프레임으로 펼치면
    조각이 12장이 되는데, 정작 바뀌는 건 그중 좁은 띠 하나뿐이다.

    그래서 프레임 간 차이가 실제로 발생하는 세로 구간을 찾아 거기만 자르고,
    첫·중간·마지막 프레임을 좌→우로 붙인다. before/after는 그 셋이면 충분하고,
    셋이면 축소 후에도 프레임당 500px가 남아 읽힌다.

    변화가 없으면(사실상 정지 GIF) None을 반환한다.
    """
    total = getattr(im, "n_frames", 1)
    if total <= 1:
        return None

    # 변화 구간을 찾기 위해 넉넉히 훑고, 붙일 때는 cols장만 쓴다
    probe = [round(i * (total - 1) / 7) for i in range(8)]
    frames = []
    for i in probe:
        im.seek(i)
        frames.append(im.convert("RGB").copy())

    base = np.asarray(frames[0].convert("L"), dtype=np.int16)
    acc = np.zeros_like(base)
    for fr in frames[1:]:
        acc = np.maximum(acc, np.abs(base - np.asarray(fr.convert("L"), dtype=np.int16)))

    rows = np.where(acc.max(axis=1) > 12)[0]  # 12 미만은 디더링 잡음으로 본다
    if rows.size == 0:
        return None

    w, h = frames[0].size
    top, bot = max(0, int(rows.min()) - pad), min(h, int(rows.max()) + pad)
    if bot - top < 40:
        return None

    picks = [frames[0], frames[len(frames) // 2], frames[-1]][:cols]
    band = [f.crop((0, top, w, bot)) for f in picks]
    paste_row(band, path)
    pct = 100 * (bot - top) / h
    return f"{total}프레임 / 변화 구간 {top}~{bot}px (전체의 {pct:.0f}%) / 첫·중간·마지막 좌→우"


def collect(inputs, workdir):
    """zip / 디렉토리 / 개별 파일을 이미지 경로 리스트로 펼친다."""
    out = []
    for raw in inputs:
        p = Path(raw)
        if not p.exists():
            sys.exit(f"없는 경로: {p}")
        if p.suffix.lower() == ".zip":
            dest = workdir / f"_unzip_{p.stem}"
            dest.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(p) as z:
                for m in z.namelist():
                    # zip slip 방어: 압축 안의 경로를 신뢰하지 않는다
                    name = Path(m).name
                    if not name or Path(name).suffix.lower() not in EXTS:
                        continue
                    with z.open(m) as src, open(dest / name, "wb") as dst:
                        dst.write(src.read())
            out += [f for f in dest.iterdir() if f.suffix.lower() in EXTS]
        elif p.is_dir():
            out += [f for f in p.rglob("*") if f.suffix.lower() in EXTS]
        elif p.suffix.lower() in EXTS:
            out.append(p)
    return sorted(set(out), key=natkey)


def paste_row(images, path):
    """이미지들을 가로로 이어붙여 저장한다."""
    w = sum(i.size[0] for i in images)
    h = max(i.size[1] for i in images)
    canvas = Image.new("RGB", (w, h), "white")
    x = 0
    for im in images:
        canvas.paste(im.convert("RGB"), (x, 0))
        x += im.size[0]
    canvas.save(path)
    return w, h


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inputs", nargs="+", help="zip / 디렉토리 / 이미지 파일")
    ap.add_argument("--out", default="./prepped")
    ap.add_argument("--chunk", type=int, default=DEFAULT_CHUNK)
    a = ap.parse_args()

    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    if len([i for i in a.inputs if str(i).lower().endswith(".zip")]) > 1:
        print("주의: zip을 여러 개 넣었다. 다른 상품이 섞이면 브리프가 오염된다.\n", file=sys.stderr)

    files = collect(a.inputs, out)
    if not files:
        sys.exit("이미지를 찾지 못함")

    # (라벨, 이미지) 목록. GIF는 첫 프레임만 본문으로 쓰고, 변화는 별도 스트립으로 뽑는다.
    items, strips = [], []
    for f in files:
        try:
            im = Image.open(f)
        except Exception as e:
            print(f"  건너뜀 {f.name}: {e}", file=sys.stderr)
            continue
        if getattr(im, "n_frames", 1) > 1:
            sp = out / f"gifchange_{len(strips)+1}.png"
            note = gif_change_strip(im, sp)
            if note:
                strips.append((sp, note, f.name))
            im.seek(0)
            items.append((f"{f.name} (GIF 첫 프레임)", im.convert("RGB").copy()))
        else:
            items.append((f.name, im))

    short = [(l, im) for l, im in items if im.size[1] / im.size[0] <= TALL_RATIO]
    tall = [(l, im) for l, im in items if im.size[1] / im.size[0] > TALL_RATIO]

    print(f"입력 파일 {len(files)}개 → 이미지 {len(items)}장 (대표컷 {len(short)} / 긴 상세컷 {len(tall)})\n")
    made = []

    if short:
        # 대표컷은 제품 외형(시각 앵커)용. 글자를 읽을 게 아니라 형태를 보는 것이라
        # 한 장에 다 이어붙여도 충분하다. 다만 너무 많으면 조각당 폭이 줄어드니 4장씩 나눈다.
        for i in range(0, len(short), 4):
            grp = short[i : i + 4]
            p = out / (f"hero_{i//4+1}.png" if len(short) > 4 else "hero.png")
            w, h = paste_row([im for _, im in grp], p)
            made.append((p, f"{w}x{h}", "대표컷: " + ", ".join(l[:26] for l, _ in grp)))

    for idx, (label, im) in enumerate(tall, 1):
        w, h = im.size
        step = a.chunk - OVERLAP
        ys = list(range(0, h, step))
        # 자투리가 아주 작으면 조각 하나를 없애고 앞 조각이 끝까지 덮게 한다.
        # 기준을 넉넉히 잡으면 마지막 조각이 너무 길어져 다시 축소 문제가 생기므로 0.15로 둔다.
        if len(ys) > 1 and h - ys[-1] < a.chunk * 0.15:
            ys.pop()
        # 마지막 조각은 반드시 이미지 끝까지 간다. 상세페이지 하단에는 성분표와
        # 주의사항이 있어 규제 확인에 필요하므로 한 픽셀도 흘리면 안 된다.
        bounds = [
            (y, h if i == len(ys) - 1 else min(y + a.chunk, h))
            for i, y in enumerate(ys)
        ]
        chunks = [im.crop((0, t, w, b)) for t, b in bounds]
        for i in range(0, len(chunks), 2):
            pair = chunks[i : i + 2]
            p = out / f"detail_{idx}_{i//2+1}.png"
            cw, ch = paste_row(pair, p)
            span = f"{bounds[i][0]}~{bounds[i+len(pair)-1][1]}px"
            made.append((p, f"{cw}x{ch}", f"{label[:34]} 의 {span} / 전체 {h}px (좌→우)"))

    for sp, note, src in strips:
        from PIL import Image as _I
        w, h = _I.open(sp).size
        made.append((sp, f"{w}x{h}", f"[GIF 변화] {src[:30]} — {note}"))

    print(f"{'파일':<22} {'크기':<12} 내용")
    print("-" * 78)
    for p, size, desc in made:
        print(f"{p.name:<22} {size:<12} {desc}")
    print(f"\n{len(made)}장 생성 → {out.resolve()}")
    print("view 도구로 순서대로 열어 읽을 것. detail_N_M 안에서는 좌측이 먼저다.")


if __name__ == "__main__":
    main()
