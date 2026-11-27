# 스킬 모음 (Claude Skills)

CJ AX 부트캠프에서 직접 만든 Claude 스킬입니다. 폴더마다 `SKILL.md`가 스킬 본문이고, 일부는 `references/`·`scripts/`·`assets/` 보조 파일이 함께 있습니다.

## 조사·기획

| 스킬 | 설명 |
|---|---|
| [`mvp-research-design`](./mvp-research-design/SKILL.md) | "mvp 파일 만들어줘" — 매일 손으로 하던 경쟁사 조사를 AI 에이전트로 줄이는 MVP 조사 설계서(mvp.md + 한눈에 보는 HTML)를 직무·회사·채용공고에 맞춰 질문하며 만든다. |
| [`persona-cjm`](./persona-cjm/SKILL.md) | BRAND·ITEM·TARGET·SITUATION만 넣으면 퍼소나를 5-Whys로 분석하고 6단계 고객여정지도(CJM)·페인포인트 우선순위를 도출, 리뷰로 강화한 뒤 릴스/팝업/투어 모드로 HTML 기획서를 만든다. |
| [`persona-journey`](./persona-journey/SKILL.md) | 고객 페르소나(Before)·브랜드 페르소나(After)를 설계·진단하고 여정지도를 그린 뒤 리뷰·인터뷰·자체 데이터로 가설을 검증한다. |
| [`copy-team-painpoints`](./copy-team-painpoints/SKILL.md) | "카피팀" — 페인포인트·미해결과제를 100개 뽑은 뒤 단계별로 걸러 핵심 3개와 카피 앵글까지 정리한다. |

## 힉스필드 AI 에이전트 (광고·영상·로고 제작)

| 스킬 | 설명 |
|---|---|
| [`higgs-ads-scripter`](./higgs-ads-scripter/SKILL.md) | 쇼핑몰 상품 링크·상세페이지·사진을 분석해 타깃·핵심 혜택·훅·표시광고법 체크가 담긴 HTML 광고 제작 브리프를 만든다. |
| [`higgs-ads-creator`](./higgs-ads-creator/SKILL.md) | 광고 브리프를 힉스필드로 완성된 광고 소재(한글 카피 포스터 6장, Seedance 2.0 쇼츠·롱폼 영상)로 제작한다. |
| [`higgs-3d-shorts-creator`](./higgs-3d-shorts-creator/SKILL.md) | 화난 과일·채소·음식 캐릭터가 "그렇게 보관하면 안 돼!"라고 말하는 6초 픽사풍 3D 쇼츠를 만든다. |
| [`higgs-explainer-studio`](./higgs-explainer-studio/SKILL.md) | 주제·스크립트·링크로 한국어 내레이션이 들어간 페이스리스 설명 영상(최대 3분)을 끝까지 제작한다. |
| [`higgs-logo-studio`](./higgs-logo-studio/SKILL.md) | 질문 4개만 답하면 쓸 수 있는 로고 시안 4장 → 다듬기 → 투명 PNG·파비콘·HEX까지 세트로 만든다(기존 로고 진단·수정도 가능). |

## 사용 방법

1. 원하는 스킬 폴더를 통째로 내려받습니다.
2. Claude 앱의 스킬 설정에서 폴더(또는 zip)로 업로드하거나, Claude Code에서는 `~/.claude/skills/` 아래에 폴더째 넣습니다.
3. 각 `SKILL.md`의 description에 적힌 말(예: "mvp 파일 만들어줘", "카피팀")로 호출합니다.

## 실행 예시

- [`mvp-research-design`](./mvp-research-design/SKILL.md)로 만든 메디큐브 경쟁사 광고 소재 리서치 MVP: [폴더 보기](../mvp/medicube/) (설계서 `mvp.md`·`mvp.html`, 제안서, 아침회의 파일럿 결과)
