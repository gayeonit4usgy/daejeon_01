# 가상 인물 프리미엄 모드 — 무대사 브랜드 뮤즈 영상

**발동 조건**: 산출물에 영상 포함 + 브리프(기획안)에 인물 앵커 없음 + 0단계 가상 인물 질문에 사용자가 "예".

이 모드의 목적은 **프리미엄 TV 스팟급의 고급스러운 인상**이다. 대사와 자막 없이, 가상 모델의 존재감·제품의 아름다움·질감·빛만으로 브랜드를 말한다. `video.md`의 순서(셧리스트 → 스토리보드 승인 → 생성)와 `seedance-grammar.md`의 프롬프트 구조는 그대로 유지하고, 이 문서는 그 위에 얹히는 **차이점만** 적는다 — 오버라이드 범위는 문법 문서 상단의 오버라이드 표에 선언돼 있다.

## 1. 가상 모델 설계 — 픽셔널 브랜드 뮤즈

브리프의 타깃 서술·브랜드 무드·카테고리에서 캐스팅을 도출한다. 사용자에게 외모 취향을 묻지 않는다 — 전문 캐스팅 디렉터로서 이 스킬이 직접 잡는다.

- **외형 서술 블록(영문)을 한 번 확정하면, 이후 모든 프롬프트(키 이미지·스토리보드·영상 Part 1/2)에 단어 단위로 동일하게 복붙한다.** 기존 인물 앵커 원칙과 같다 — 한 단어 다르면 다른 사람이 나온다.
- 서술에 반드시 포함할 것: 성별·연령대·전체 인상, 헤어·의상 방향(브랜드 무드 승계 — 예: K-뷰티면 natural elegance, refined Korean mood; 의상은 카테고리에 맞게), calm/confident 등 기본 표정, 그리고 **natural skin texture** 지시.
- **피부 질감 원칙**: `natural skin texture, visible pores, no plastic over-smoothed beauty filter look`. 과도한 보정 룩은 프리미엄이 아니라 저가 광고 룩이다.
- **실존 인물 금지**: 실존 인물의 이름·닮은꼴 지정 금지. 결과 전달 시에도 모델을 실존 인물처럼 특정하지 않는다 — 이 모델은 픽셔널 브랜드 뮤즈다. 이 원칙 덕에 초상권 이슈가 없다는 점을 전달 노트에 한 줄 남긴다.

## 2. 키 이미지 → element 잠금 — 별도 승인 절차 없음

1. 스토리보드 **전에** 가상 모델 키 이미지 1장을 생성한다 — 인물 표현에 강한 모델(seedream 계열 등, models_explore로 확인), 정면 계열 상반신, 확정한 외형 서술 블록 + 브랜드 무드 조명.
2. 키 이미지를 element로 잠근다(`higgsfield.md`). 이후 스토리보드 시트와 모든 영상 프롬프트에 **제품 element와 가상 모델 element를 함께 결합**한다.
3. **별도의 모델 승인 질문을 추가하지 않는다.** 가상 모델은 스토리보드 시트에 등장하므로, 사용자는 스토리보드 승인 게이트에서 모델의 룩까지 한 번에 승인하게 된다. 사용자가 스토리보드에서 인물을 바꾸자고 하면 키 이미지부터 재생성하고 element를 갈아끼운 뒤 시트를 다시 만든다.

## 3. 무대사 프리미엄 문법 — `seedance-grammar.md`와의 차이

셧리스트는 `seedance-grammar.md` 3절 구조(Style Prefix → Commercial Objective → Characters → Brand/Product Anchors → Scene → timed CUTs, 정확히 15초)를 유지하되, **Dialogue & Lip Sync 블록을 무대사 선언으로 대체한다**:

```
No dialogue. The model does not speak. No lip-sync.
No subtitles, no captions, no on-screen text, no floating typography, no slogan text.
No background music description.
```

컷 설계 규칙:

- **15초 안에 3~5컷.** (문법 문서 기본값 1~4컷을 이 모드가 오버라이드한다.) 과밀한 장면 전환 금지 — 컷이 많아질수록 프리미엄 인상이 깨진다. 30초(2편 체이닝)면 편당 3~5컷.
- **우아한 슬로우 카메라 무브먼트** 기본: slow push-in, gentle orbit, graceful pan. 급한 whip pan·과한 슬로모션 남발 지양.
- shallow depth of field, cinematic clarity, realistic product photography 지향.
- 감정과 메시지는 대사가 아니라 **시선·손끝의 움직임·제품 질감·빛의 변화**로 말한다. 각 컷의 Scene 서술에 이 중 무엇으로 말하는지가 드러나야 한다.
- 조명 기본값은 soft natural light. 팔레트는 브리프의 브랜드 무드에서 가져오고, 무드 서술이 없으면 카테고리 기본을 쓴다 — 뷰티·스킨케어: warm cream, ivory, beige, muted gold, soft green / 그 외 카테고리: `posters.md` "룩의 출처" 표의 톤을 영상 언어로 승계.
- 비율·길이는 1단계 확정값을 따른다. 프리미엄 TV 스팟 지향이므로 기본 추천은 16:9지만, 사용자가 쇼츠(9:16)를 확정했으면 같은 문법을 세로 프레이밍으로 적용한다(`video.md` 비율 프레이밍 규칙).

## 4. 네거티브 프롬프트 — 프롬프트마다 별도 블록

영상 프롬프트마다 네거티브 프롬프트를 함께 작성한다. models_explore로 Seedance가 negative prompt 파라미터를 지원하는지 확인하고, 지원하면 파라미터로, 지원하지 않으면 프롬프트 본문 끝에 `Do not include:` 절로 삽입한다.

기본 네거티브 (항상 포함):

```
text, subtitles, captions, watermark, logo overlay, typography,
talking, mouth movement, lip-sync, singing,
plastic skin, over-smoothed face, beauty filter look, distorted hands, extra fingers,
distorted product, wrong product shape, crowded rapid scene changes, chaotic editing
```

여기에 **사용자·브리프가 밝힌 제외 요소를 승계해 추가한다** — 예: 과한 미소 금지 → exaggerated smile / 판타지 금지 → fantasy elements, surreal effects / 과한 슬로모션 금지 → excessive slow motion. 브리프의 표시광고법 3칸에서 "쓰면 안 되는" 연출(성분 침투 CG 등)도 네거티브에 반영한다.

## 5. 레퍼런스 광고 영상이 있으면 — 무드만 가져온다

사용자가 참고 광고 영상(파일·링크)이나 스타일 서술을 제공하면:

- 가져오는 것: **무드, 페이싱, 조명, 구도, 렌즈 언어, 컬러 팔레트, 감정 리듬**. 이를 분석해 영문 프롬프트 언어로 번역해 반영한다.
- 가져오지 않는 것: **구조 복제, 직접 모방.** 레퍼런스의 컷 구성·시나리오를 그대로 따라 만들지 않는다. 타사 로고·브랜드 요소는 절대 재현하지 않는다.
- 영상 파일은 힉스필드 element로 결합할 수 없으므로 분석→프롬프트 번역 방식만 쓴다. 레퍼런스가 없으면 되묻지 않는다 — 학습된 프리미엄 광고 문법으로 스스로 설계한다.

## 6. USP가 비어 있어도 진행한다

핵심 혜택(USP)은 브리프에서 승계하는 것이 정상 경로다. 브리프 없이 최소 3요소로 진행 중인데 혜택 서술이 약하면, 되묻지 말고 **비주얼 무드·제품의 아름다움·모델의 존재감·질감·조명·프리미엄 브랜드 인상**에 집중해 설계한다. 이 경우 셧리스트의 Commercial Objective를 "premium brand impression" 중심으로 잡고, 추정 기반임을 기획 제시 화면에 명시한다.

## 7. 제품·모델 보존 — 지어내지 않는다

- **제품**: 실물 사진 element에 잡힌 디자인(용기 형태·색·라벨·캡 등)을 프롬프트 서술로도 한 번 더 고정한다 — element와 서술이 이중 안전장치다. 사진에 없는 면을 상상으로 정밀 묘사하지 않는다(SKILL.md 0단계 원칙 그대로).
- **모델**: 1절에서 확정한 외형 서술 블록 + element 결합. 30초 체이닝이면 Part 1/2의 Characters 블록을 단어 단위로 복붙한다(`video.md` CONTINUITY 규칙).

## 하지 않는 것

- 대사·립싱크·자막·화면 텍스트·플로팅 타이포·음악 장르/트랙 서술을 프롬프트에 넣는 것
- 15초에 6컷 이상 욱여넣는 것
- 실존 인물 특정·닮은꼴 캐스팅, 과도한 보정 필터 룩
- 레퍼런스 광고의 구조·시나리오를 그대로 복제하는 것
- 키 이미지·element 없이 가상 모델 등장 컷을 생성하는 것 — 컷마다 다른 얼굴이 나온다
