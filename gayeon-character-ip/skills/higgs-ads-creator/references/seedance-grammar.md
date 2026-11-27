# Seedance 2.0 연출 문법 — 15초 광고 프롬프트의 단일 출처

너는 최고 수준의 한국 광고 감독이자 촬영감독, 연기 디렉터, 제품 비주얼 전문가다. 이 문서는 **15초 한 편의 프롬프트를 어떻게 쓰는가**만 다룬다. 감독된(directed) 광고를 만드는 것이지, 브리프를 예쁜 클립으로 토막 내는 게 아니다.

## 이 문서의 자리

```
SKILL.md          산출물·스토리·영상 스타일 확정, 승인 게이트, 크레딧  (파이프라인)
video.md          셧리스트 → 스토리보드 → 생성 순서, 30초 체이닝        (순서)
higgsfield.md     모델·element·업로드·get_cost                          (실행)
seedance-grammar.md  ← 이 문서. 프롬프트 안에 무엇을 어떻게 쓰는가      (문법·연출)
virtual-model.md  무대사 프리미엄 모드 오버라이드                        (모드별 차이)
```

**이 문서는 파이프라인을 정하지 않는다.** 모드는 SKILL.md 2단계에서 스토리와 함께 이미 정해졌고, 포맷·길이·비율은 1단계에서 확정됐으며, 승인·비용·생성은 SKILL.md와 higgsfield.md의 일이다. 여기서 다시 고르거나 다시 묻지 않는다.

**모든 프롬프트 단위는 정확히 15초다.** 30초는 15초 2편이다(`video.md` 2절). 이건 문법 상수다.

## 오버라이드 — 이 문서의 법칙이 바뀌는 유일한 경우

| 조건 | 문서 | 바뀌는 것 |
|---|---|---|
| 가상 인물 프리미엄 모드 (0단계 질문 "예") | `virtual-model.md` | ① Dialogue & Lip Sync 블록 → 무대사 선언으로 대체 ② 컷 수 상한 4 → **3~5컷** ③ 네거티브 프롬프트 블록 추가 |

이 경우를 빼면 아래 법칙은 그대로다. 반대로 **위 세 가지 외에는 가상 인물 모드에서도 이 문서를 따른다** — 구조, 연속성, 클레임 규율, 후반작업 경계 전부.

---

## 1. 커머셜 모드 8종 — 정의 (선택은 이미 끝났다)

SKILL.md 2단계에서 선택된 스토리에 모드가 표기돼 있다. 그 모드를 Style Prefix에 넣고, 아래 정의대로 페이싱·연기 강도·조명 광택·카메라 에너지·제품 강조·컷 밀도를 통제한다.

| 모드 | 성격 |
|---|---|
| **Premium TVC** | 정제되고 통제된, 동경을 부르는 화면. 시각적으로 경제적이고 즉각 읽힌다 |
| **Emotional Brand Film** | 절제된 감정, 인간 관계, 살아 있는 한국적 디테일. 반응이 착지할 여백을 준다 |
| **Beauty / Fashion** | 피부·모발·원단·제스처·실루엣·화장품 질감의 정밀함, 우아한 카메라 통제 |
| **Food & Beverage** | 식욕 소구 — 김, 결로, 액체의 거동, 질감, 온도, 만족스러운 제품 인터랙션 |
| **Technology / Finance** | 확신과 명료함, 정밀한 손-기기 인터랙션, 깨끗한 공간. 근거 없는 주장 없이 혜택을 보여준다 |
| **Lifestyle** | 동시대 한국의 일상, 온기, 사용성, 사회적 맥락, 자연스러운 제품 통합 |
| **Witty Digital Commercial** | 즉각적인 훅, 날카로운 반응 타이밍, 시각적 코미디, 통제된 과장, 빠른 편집 리듬 |
| **Product Demonstration** | 명확한 인과, 읽히는 작동, 제품 핸들링, 기능 가시성, 물리적으로 납득되는 결과 |

주 모드 하나가 원칙이다. 컨셉이 정말 필요로 할 때만 보조 모드 하나를 겹치되, 무관한 스타일의 혼합은 만들지 않는다.

**"한국 광고 스타일"을 일반적인 럭셔리 이미지, 아이돌 미학, 막연한 동아시아 프로덕션 디자인으로 환원하지 않는다.**

---

## 2. Global Style Prefix

**대화를 먼저 확인한다.** 사용자가 커스텀 스타일 프리픽스를 올렸거나 붙여넣었으면 **그 프리픽스를 원문 그대로** 쓴다. 고쳐 쓰거나 번역하거나 줄이거나 "개선"하지 않는다.

커스텀 프리픽스는 비주얼 룩을 덮어쓰지만, 아래 비-스타일 규칙은 덮지 못한다:

- 모든 프롬프트는 정확히 15초
- 한국어 대사는 한글로
- 보이는 발화에는 명시적 한글 립싱크 지시
- 인물·제품 연속성
- 자막·광고 카피·그래픽 로고·엔드카드 제외
- 근거 없는 광고 주장 금지

커스텀 프리픽스가 없으면 아래 기본값을 쓴다. `[SELECTED COMMERCIAL MODE]`는 선택된 모드로, `[FORMAT LINE]`은 `16:9 horizontal commercial framing` 또는 `9:16 vertical Shorts framing — compose for a mobile feed`로 치환한다. 3단계에서 실사가 아닌 영상 스타일(3D·2D 애니메이션 등)이 선택됐으면 첫 줄의 룩 서술을 그 스타일로 교체하되 나머지 줄은 유지한다(`video.md` 1절).

```text
Style: Premium contemporary Korean commercial realism. Photorealistic, polished, culturally specific, and category-appropriate — no generic pan-Asian styling, no 3D-render or game-engine look unless explicitly requested.
Commercial Mode: [SELECTED COMMERCIAL MODE]. Let this mode control pacing, performance intensity, lighting polish, camera energy, product emphasis, and cut density.
Format: [FORMAT LINE].
Market & Art Direction: Contemporary South Korea. Use culturally accurate Korean casting, locations, wardrobe, grooming, props, spatial behavior, and production design. Never mix in Japanese, Chinese, or vague "East Asian" visual cues. Use non-Korean casting only when the brief calls for it.
Lighting: Motivated premium commercial lighting. Combine believable daylight, practicals, bounce, diffusion, negative fill, and controlled studio augmentation when the category requires it. Preserve natural contact shadows and realistic response on skin, food, glass, metal, fabric, liquid, and packaging.
Color: Brand- and product-led palette with a clear dominant / secondary / accent hierarchy. Keep skin tones natural and keep product colors stable across every cut.
Camera: Physical cinema lenses. Select controlled dolly, gimbal, handheld, macro, probe, tabletop, or locked-off camera work according to the commercial objective. Use 180° shutter motion blur unless a deliberate product-detail beat requires crisper motion.
Skin & Materials: Natural pore-level skin, realistic hair, believable grooming, and physically accurate fabric. Product surfaces, food textures, liquids, steam, condensation, foam, reflections, translucency, and packaging materials must remain convincing and consistent.
Acting: Natural contemporary Korean commercial performance — precise eye-lines, micro-pauses, grounded breathing, restrained premium emotion, warm relational chemistry, and clearer reaction beats only when the selected mode calls for comedy or digital energy. Every gesture must serve the product, relationship, or commercial idea.
Dialogue & Lip Sync: Spoken dialogue is written in Korean Hangul exactly as performed. Match visible mouth shapes, syllable timing, breath, pauses, jaw movement, and emotional cadence to the Korean line. Never translate the spoken line into English inside the dialogue.
Physics: Gravity, inertia, liquid behavior, food behavior, fabric movement, hand-object contact, and contact shadows are realistic. No floating props, impossible product handling, or continuity-breaking object motion.
Composition: Clear commercial hierarchy. Faces, product, and primary action remain immediately legible. Do not allocate shot time to subtitles, copy, graphic logos, or end cards.
Continuity: Character identity, facial features, hair, wardrobe, makeup, emotional state, hand dominance, props, product shape, scale, color, material, orientation, fill level, opened or unopened state, damage, condensation, and environment remain identical across every cut. No identity drift or product drift.
Technical: Exactly 15 seconds per prompt. 24fps smooth motion. High detail. No jitter, temporal warping, duplicated fingers, unstable product geometry, mouth drift, or identity drift.
Audio: Korean dialogue when scripted, synchronized production sound, environmental SFX, and product foley. No subtitles or captions. No music unless the user explicitly requests music.
Post-Production Boundary: Do not design or render subtitles, advertising copy, legal text, promotional graphics, standalone logos, logo animation, or end cards. These are added after video generation. Do not create separate prompt blocks for them.
```

Style Prefix는 모든 유닛의 프롬프트 맨 앞에 **원문 그대로** 붙는다. 각 유닛의 프롬프트는 재조립 없이 Seedance에서 단독으로 작동해야 한다.

---

## 3. 프롬프트 구조 — 이것이 법칙이다

15초 유닛 하나의 프롬프트는 위에서 아래로 이 순서를 그대로 따른다.

```text
[STYLE PREFIX — full block, verbatim]

Commercial Objective:
[One concise sentence stating what this 15-second unit must make the audience notice, feel, or understand. Do not invent claims, slogans, prices, rankings, or guarantees.]

Characters:
[Short, specific, vivid anchors for only the people visible in this unit. Korean age range, facial and hair features, wardrobe, grooming, emotional state, relevant props. Carry forward their exact condition from the prior unit unless a change happened visibly on screen.]

Brand / Product Anchors:
[Define every visible product or branded physical object by stable visual facts: product type, silhouette, proportions, material, surface finish, color, package structure, cap or opening mechanism, orientation, fill level, temperature cues, condensation, damage, hand contact. Pull these directly from the ad brief's 제품 시각 앵커 when one exists. Do not request readable brand typography, subtitles, slogans, logos, or graphic overlays. If no product is visible, write "No physical product visible in this prompt."]

Scene:
[One or two sentences: what is happening, where, when. Be geo-spatial — where every character and product is positioned relative to the location, camera, light, and each other. Culturally accurate contemporary Korean detail.]

Dialogue & Lip Sync:
[The exact spoken Korean line in Hangul, the speaker, delivery, breath, pause structure, approximate delivery duration. Explicitly require phoneme-accurate Korean lip sync whenever the speaker's mouth is visible. If nobody speaks, write "No spoken dialogue."]

CUT 1 — [time range within 0.0–15.0s] — [shot type, lens feel, height, movement]:
[What happens: acting beat, product interaction, hand position, eye-line, breath, Korean lip sync when visible, camera behavior, lighting behavior, product physics, diegetic sound.]

CUT 2 — [time range] — [shot type, lens feel, height, movement]:
[The next beat at the same precision.]

CUT 3 — [time range] — [shot type, lens feel, height, movement]:
[The final beat of this 15-second unit.]
```

- **컷은 1~4개.** 선택된 모드에 따른다. 연기나 제품 액션이 15초를 끌고 갈 수 있으면 지속 단일 숏도 유효하다. 템플릿에 3개가 보인다고 3컷을 억지로 만들지 않는다. (가상 인물 프리미엄 모드는 3~5컷 — `virtual-model.md`)
- **컷 타임코드는 `0.0s`부터 `15.0s`까지 빈틈도 겹침도 없이 덮는다.**
- 마지막 프레임은 의도적으로 설계한다. 30초 1편의 마지막 프레임은 2편으로의 이음새다(`video.md` 2절). 다만 **마지막 초를 로고·카피·엔드카드로 쓰지 않는다.**
- 제품 element는 Brand / Product Anchors 서술 안에 결합한다(`higgsfield.md`). element 플레이스홀더 문법을 사용자에게 노출하지 않는다.

---

## 4. 한국 광고를 연출하는 법

위 구조는 그릇이다. 그 안에 들어가는 게 실제 연출 작업이다.

### 커머셜 오브젝티브에서 출발한다

각 유닛의 가장 중요한 시각적·감정적 임무 하나를 특정한다. 예: 음료가 즉시 차갑고 회복시켜 준다고 느끼게 하기 / 스킨케어 질감이 가볍게 스며든다고 느끼게 하되 의학적 주장은 만들지 않기 / 금융 서비스가 침착하다고 느끼게 하되 근거 없는 인터페이스 텍스트가 아니라 행동으로 / 기능 하나를 명확한 인과 액션 하나로 읽히게 하기. 오브젝티브는 화면과 연기를 지휘한다 — **화면에 박히는 슬로건이 아니다.**

### 한국적 구체성

동시대 한국의 공간·행동·물질문화를 정확히 쓴다: 아파트, 빌라, 오피스텔, 사무실, 카페, 편의점, 동네 거리, 대중교통, 리테일. 의상·그루밍·식기·포장 거동·집 정리 상태·직장 예절·나이 위계·대인 거리가 장면과 맞아야 한다. **한국을 신호하려고 한복·네온사인·서울 랜드마크·아이돌 스타일링·"K-컬처" 기호를 얹지 않는다.** 일본·중국·범아시아 단서를 한국 장면에 섞지 않는다. 문화적 정확성은 관찰된 것처럼 느껴져야지, 선언되면 안 된다.

### 미장센과 블로킹

모든 장면을 블로킹한다. 각 인물이 어디에 서고 앉고 들어오고 돌아서고 손을 뻗고 바라보는지 적는다. 제품이 인터랙션 전·중·후에 어디 있는지 적는다. 사람과 사물을 가르는 것을 서술한다 — 아일랜드 식탁, 편의점 냉장고 문, 책상 모서리. 손은 제품에 자연스럽게 접근해야 한다. 시선이 맞아야 한다. **제품 정면이 카메라 쪽으로 순간이동하지 않는다** — 패키지가 회전하면 누가 왜 돌리는지 서술한다.

### 페이싱과 리듬

훅·전개·제품 순간·감정 전환·반응·마지막 실사 페이오프가 각각 어디에 놓일지 정한다. 모드가 리듬을 지배한다 — Premium TVC는 통제된 1~3컷과 확신에 찬 홀드, Emotional Brand Film은 긴 반응·침묵·감정의 잔상, Beauty/Fashion은 제스처 안무·매크로 질감·우아한 전환, Food & Beverage는 빠른 식욕 신호 + 만족스러운 히어로 비트 하나, Technology/Finance는 명확한 손-기기 인과와 침착한 확신, Lifestyle은 자연스러운 일상 리듬과 억지 없는 통합, Witty Digital은 첫 비트의 훅과 또렷한 셋업-페이오프 타이밍, Product Demonstration은 순차적 인과와 건너뛴 단계 없음. **강한 제품 순간 하나가 불명확한 다섯 개를 이긴다.**

### 연기 지시

기본값은 자연스러운 동시대 한국 광고 연기다. 감정 라벨을 보이는 행동으로 번역한다 — "그녀는 안도한다"가 아니라 **"첫 모금 뒤 어깨가 풀리고, 반 박자 눈을 감았다가, 코로 조용히 숨을 내쉰다."** 프리미엄·감성 작업은 절제된 연기, 디지털 코미디는 더 읽히는 반응 — 컨셉이 요구하지 않는 한 과장된 연극적 제스처는 쓰지 않는다. 프레임 안의 모든 사람은 호흡·눈의 움직임·자세 변화·반응하는 주의로 살아 있어야 한다.

### 한글 대사와 립싱크

모든 대사는 **들려야 하는 그대로 한글로** 쓴다 — 프롬프트 안에 영어 번역을 넣지 않는다. 보이는 화자마다: 누가 말하는지 특정한다; 딜리버리를 지정한다(속삭이듯, 대화체, 건조하게, 밝게, 숨차게, 절제하며, 코믹하게, 감정을 누르며); 대사 앞뒤 포즈를 지정한다; 자연스러운 딜리버리 길이를 추정해 컷 타이밍이 그것을 받치게 한다; **음소 단위로 정확한 한글 입 모양**을 요구한다 — 음절 타이밍, 자음 폐쇄, 모음 형태, 턱 열림, 입술 둥글기, 호흡, 마지막 입 정돈. 핵심 대사에서는 화자의 머리 각도와 입이 보이게 유지한다. 의도적으로 오프스크린으로 잇는 게 아니면 음절 중간에 컷하지 않는다. 대사 중 다른 인물의 입이 움직이지 않게 한다.

**15초에 카피 같은 발화를 욱여넣지 않는다.** 브리프의 대사 후보는 말할 수 있게 쓰인 것이므로, 새 카피를 지어내기보다 그것을 쓴다.

### 인물 연속성

모든 컷과 유닛에 걸쳐 내부적으로 추적한다: 정체성과 얼굴 구조 / 나이와 신체 비율 / 모발 길이·가르마·질감·젖음·움직임 / 의상·주름·여밈·소매·장신구·신발·가방 / 메이크업·피부 마감·땀·눈물·음식 잔여물·작은 자국 / 손잡이 방향과 어느 손이 제품을 쥐는지 / 감정 상태와 호흡 / 직전 컷 끝의 위치와 이동 방향.

**연속성 판단은 Characters, Brand / Product Anchors, Scene, CUT 서술 안에 구체적 문장으로 나타나야 한다 — 별도의 보이는 트래커로 만들지 않는다.**

### 제품·패키지 연속성

**광고는 제품이 흔들릴 때 실패한다. 주연 배우의 엄격함으로 제품을 추적한다:** 정확한 실루엣·비율·크기·캡/뚜껑/펌프/힌지/손잡이/버튼/이음매 / 재질·광택·거칠기·투명도·반사·엣지 거동 / 색과 색온도 / 방향과 어느 면이 카메라를 향하는지 / 잔량·개봉 여부·씰 상태·따른 양·베어 문 자국·부스러기·녹음·거품·김·성에·결로 / 손가락 위치·쥐는 압력·접촉 그림자·손과 제품의 스케일 / 다음 컷으로 넘어가는 손상·흘림·물방울·지문·잔여물.

**Seedance에게 읽히는 패키지 문구, 광고 카피, 깨끗한 그래픽 로고를 만들어 달라고 하지 않는다.** 사용자가 제품 사진을 주면 `higgsfield.md`의 경로로 element를 만들어 실물 패키지 디자인을 최대한 보존하되, 정확한 타이포그래피와 브랜드 마크는 후반작업의 문제로 다룬다.

### 제품 액션과 감각적 사실성

카테고리별로 제품 거동을 연출한다. **음료**: 캡 저항, 결로의 이동, 점도, 기포, 따르는 궤적, 삼킴, 온도 반응. **음식**: 김의 방향, 크러스트, 소스 부착, 기름 광택, 늘어남, 베어 물 때의 변형, 식기 접촉. **뷰티**: 제품 양, 펌프 액션, 손끝 압력, 발림, 흡수, 광택, 거울 시선. **패션**: 원단 무게, 드레이프, 봉제선 장력, 걸을 때 실루엣 반응, 장신구 관성. **테크**: 화면 방향, 버튼/제스처 인과, 그립, 반사, 읽히는 텍스트 없이 일관된 인터페이스 상태. **가전**: 문·뚜껑·힌지·트레이, 기류, 김, 진동, 전후 사물 상태.

**불가능한 "뷰티 매직", 떠다니는 성분, 유사과학적 입자, 근거 없는 전후 결과를 쓰지 않는다** — 사용자가 거짓 사실 주장을 함의하지 않는 양식화된 은유를 명시적으로 요청한 경우가 아니면.

### 카메라 언어

렌즈·높이·거리·움직임·동기를 구체적으로: "Eye-level 40mm two-shot, slow 30-centimeter dolly-in as the mother notices the daughter's reaction." / "100mm macro tabletop slide across condensation beads, parallel to the bottle shoulder." / "Static 65mm close-up, camera on the shadow side, holding through the full Korean line for clean lip sync."

**모든 무브는 드러내거나, 명확히 하거나, 강화하거나, 연결해야 한다** — 시네마틱하게 들리려고 카메라를 움직이지 않는다.

### 조명과 색

모드가 광택을 통제하지만 모든 빛은 동기화되고 물리적으로 일관되어야 한다. 방향, 부드러움, 광원 동기, 그리고 키·필·네거티브 필·프랙티컬·림·배경 분리의 관계를 적는다. 뷰티는 정제된 소프트 커머셜 라이트를 쓰되 납득 가능한 피부 질감을 유지하고, 푸드는 김·투과·기름·결로를 위한 통제된 하이라이트와 백라이트를, 라이프스타일은 자연광과 프랙티컬을, 프리미엄 TVC는 여전히 그럴듯한 조각된 스튜디오 통제를, 위티 디지털은 더 밝고 그래픽하게 — 그러나 **제품 색과 피부톤은 안정적으로 유지된다.** 하나의 자연광 백라이트 룩을 모든 카테고리에 강요하지 않는다.

### 클레임 규율

성능·건강·안전·순위·가격·환경 영향·속도·수익·효능·우월성에 대해 **근거 없는 주장을 만들거나 시각적으로 함의하지 않는다.** "1위" 지위, 의학적 효과, 보장된 결과, 정확한 퍼센트, 경쟁사 비교, 인증, 수상, 가격, 할인, 사용자가 제공하지 않은 전후 결과를 지어내지 않는다.

**브리프의 표시광고법 3칸이 구속력을 갖는다**(SKILL.md 0단계에서 승계됨): "쓰면 안 되는" 칸의 표현은 프롬프트에 절대 들어가지 않고, "근거가 있어야" 칸의 표현은 사용자가 근거 존재를 확인해 준 경우에만 들어간다. 브리프가 불완전하면 **주장을 조작하는 대신 정직한 제품 경험을 연출한다.**

### 후반작업 경계

자막·캡션·광고 카피·법적 고지·프로모션 그래픽·단독 로고·로고 애니메이션·엔드카드는 이 프롬프트가 만드는 영상 바깥이다. **On-Screen Copy / Logo / CTA / Legal / End Card 블록을 만들지 않는다.** 마지막 초를 빈 팩샷 카드로 쓰지 않는다. 모델에게 정확한 한글 타이포그래피를 렌더링해 달라고 하지 않는다. **각 15초 유닛은 의미 있는 실사·제품·연기·환경 비트에서 끝난다.** (전달 노트는 `video.md` 5절)

---

## 5. 세로 쇼츠 연출

세로는 가로를 잘라낸 게 아니다. 네이티브로 연출한다.

- **구도:** 중앙 가중, 더 타이트한 프레이밍. 얼굴과 제품이 프레임에서 눈에 띄게 큰 비중을 차지한다. 깊이를 수직으로 쌓는다 — 좌우 블로킹 대신 전경/배경 스태킹. 플랫폼 UI가 겹치는 프레임 최상단·최하단에 핵심 액션을 두지 않는다.
- **훅 규율:** 첫 **1.5~2초**가 멈춤을 벌어야 한다 — 반응하는 얼굴, 액션 중인 제품, 또는 컨셉이 딛고 선 이상 신호. **절대 설정 와이드로 열지 않는다.**
- **리듬:** 가로보다 대체로 빠르다 — 2~4컷. 단, 연속된 실연이나 연기 하나면 지속 단일 세로 숏도 유효하다.
- **하나의 아이디어:** 쇼츠 유닛 하나는 훅 하나와 페이오프 하나만 나른다. 셋업 막과 페이오프 막이 필요하면 그게 2편 케이스다(`video.md` 2절).
- **대사:** 짧게, 그리고 일찍. **쇼츠 13초에 착지하는 한국어 대사는 대부분의 시청자가 듣지 못한다.**

---

## 6. 워크드 예시

입력(브리프 경유 또는 직접): *"퇴근한 직장인이 냉장고에서 차가운 보리차를 꺼내 마시고 '아, 이제 좀 살겠다'라고 말하는 일상적인 음료 광고. 제품 사진 있음."*

확정값(SKILL.md 1~3단계에서 옴): 모드 **Lifestyle + Food & Beverage** / 포맷 **가로 15초 1편** / 영상 스타일 **실사**. 제품 사진 → element 잠금(`higgsfield.md`).

```text
[Style Prefix verbatim, Commercial Mode: Lifestyle + Food & Beverage, Format: 16:9 horizontal commercial framing]

Commercial Objective:
Make the first cold sip feel immediately restorative and recognizably part of an ordinary Korean evening, without advertising copy or an end card.

Characters:
MINJUN — Korean man, early 30s, slightly tired eyes, short black hair flattened at the crown from a full workday, white office shirt with the collar open and sleeves rolled evenly to the forearms, charcoal trousers, black socks, watch on left wrist, restrained fatigue in his shoulders. Same person, wardrobe, grooming, and emotional state across every cut.

Brand / Product Anchors:
One slim clear PET bottle of amber barley tea, matte beige cap, subtle vertical ribbing at the lower third, cold surface with fine condensation beads, approximately three-quarters full at first appearance. No readable label, advertising copy, or graphic logo. The bottle stays in Minjun's right hand after he removes it from the refrigerator; cap transfers to his left hand after opening.

Scene:
A compact contemporary Seoul apartment kitchen at 10:40 p.m. The refrigerator stands camera-left beside a pale oak cabinet run. Minjun enters from a narrow hallway camera-right. Warm under-cabinet practical light contrasts with cool refrigerator light.

Dialogue & Lip Sync:
MINJUN says in natural, low-volume Korean after swallowing: "아, 이제 좀 살겠다." Short recovery breath before "아," brief pause after the comma, completed in approximately 2.1 seconds with a soft exhale. Hold his face at a three-quarter angle, mouth unobstructed. Phoneme-accurate Korean lip sync, natural jaw opening, rounded vowels, clear consonant closure, no mouth movement from any other person.

CUT 1 — 0.0–4.2s — Medium-wide 35mm, waist height, slow gimbal settle:
Minjun enters camera-right already loosening his shoulders, crosses to the refrigerator, opens the door with his left hand. Cool refrigerator light lifts the shadow side of his face. He scans the middle shelf, exhales through his nose, reaches with his right hand. Camera settles as his fingers wrap around the cold bottle. Low room tone, refrigerator hum, soft fabric movement.

CUT 2 — 4.2–9.6s — 100mm macro to 55mm close product-hand transition, controlled tabletop slide:
Condensation beads slide as Minjun lifts the bottle. His right-hand grip compresses the PET plastic slightly without deforming its silhouette. He closes the refrigerator with his left elbow, twists the cap open with believable resistance, brings the bottle to his lips. Precise cap crack, plastic creak, small liquid shift. Product shape, fill level, cap color, and hand placement remain stable.

CUT 3 — 9.6–15.0s — Static 65mm close-up, eye level, three-quarter profile:
One continuous sip, throat moving once as he swallows. He lowers the bottle to chest height, shoulders releasing visibly. Half-beat. He delivers "아, 이제 좀 살겠다." with exact Korean lip sync, eyes softening toward the quiet living room off-screen. The final second holds on his small relieved smile and the cold bottle still beading in the foreground. No subtitle, logo, copy, or end card.
```

이 프롬프트가 스토리보드 시트와 영상 생성으로 넘어가는 경로는 `video.md` 3~4절이다.

---

## 7. 프롬프트 체크리스트

프롬프트를 넘기기 전에 확인한다.

- [ ] Style Prefix가 맨 앞에 원문 그대로 붙었고, 모드·포맷 라인이 치환됐다
- [ ] 블록 순서가 법칙 그대로다 (Objective → Characters → Anchors → Scene → Dialogue & Lip Sync → CUTs)
- [ ] 컷 타임코드가 0.0s~15.0s를 빈틈·겹침 없이 덮는다. 컷 수 1~4 (가상 인물 모드 3~5)
- [ ] 프롬프트 지시는 영문, **대사는 한글 원문** — 프롬프트 안에 영어 번역이 없다
- [ ] 보이는 화자마다 음소 단위 립싱크 지시가 있다 (또는 "No spoken dialogue.")
- [ ] Characters와 Brand / Product Anchors가 구체적이고, 30초 2편이면 두 프롬프트에 단어 단위로 동일하다(`video.md` 2절)
- [ ] 제품 element가 Anchors 서술 안에 결합됐다
- [ ] 지어낸 클레임·가격·순위·인증·전후 결과가 없다. 브리프의 "쓰면 안 되는" 표현이 없다
- [ ] 자막·카피·로고·CTA·엔드카드 블록이 없고, 마지막 초가 카드가 아니다
- [ ] 프롬프트가 단독으로 완결된다 — 재조립 없이 그대로 Seedance에 들어간다
- [ ] 사용자에게 element 플레이스홀더 문법이나 내부 파라미터명을 노출하지 않는다
