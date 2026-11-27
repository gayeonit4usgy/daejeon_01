# 로고 문법 — 사용자가 못 채우는 빈칸을 채우는 법

이 문서는 Q2~Q4의 답만으로 **로고 타입·색·폰트·프롬프트**를 확정하기 위한 판단 근거다. 생성 전에 읽는다.

## 1. 로고 타입 5종 — 스킬의 어휘

사용자에게는 이 단어를 쓰지 않는다. 괄호 안이 사용자에게 말할 때의 표현이다.

| 타입 | 정체 | 강점 | 약점 |
|---|---|---|---|
| **워드마크** (글자만 있는 형태) | 브랜드명 자체를 디자인 | 이름을 각인시킨다. 신생 브랜드에 유리 | 이름이 길면 작아지고, 정사각형에 안 들어간다 |
| **모노그램** (앞글자를 딴 형태) | 이니셜 1~3자를 결합 | 정사각형·앱 아이콘에 강하다 | 이름을 못 알려준다. 워드마크 병기 필요 |
| **심볼/아이콘** (그림 표시) | 형상 하나 | 언어를 넘고, 작아져도 살아남는다 | 의미 학습에 시간이 든다 |
| **조합형** (그림+글자) | 심볼 + 워드마크 | **가장 안전한 기본값.** 상황별로 떼어 쓸 수 있다 | 배치 규칙이 필요 |
| **엠블럼** (배지·도장 형태) | 글자를 형태 안에 가둠 | 전통·수제·클래식 톤에 강하다 | 작아지면 죽는다. 디테일이 많다 |

**의심스러우면 조합형이다.** 심볼과 워드마크를 함께 만들면 사용자가 나중에 상황에 맞춰 떼어 쓸 수 있다. 초보자에게는 이 유연성이 크다.

## 2. 도출 규칙 — Q2·Q3가 타입을 정한다

순서대로 적용한다. 위쪽이 강한 제약이다.

1. **앱 아이콘·프로필이 용도에 있다** → 워드마크 단독 탈락. 정사각형 안에서 읽히려면 심볼 또는 모노그램이 필요하다. 조합형으로 만들되 **심볼이 단독으로 서게** 설계한다.
2. **이름이 길다** (영문 4단어 이상 / 한글 6자 이상) → 워드마크 부적합. 모노그램 또는 조합형.
3. **간판·인쇄가 용도** → 원경 판독이 기준이다. 굵은 획, 획 대비가 큰 세리프·얇은 선·잔 디테일 탈락.
4. **포장·스티커·자수** → 단색 1도 인쇄를 가정한다. 그라데이션·그림자·투명도 겹침·3D 탈락. 실루엣만으로 읽혀야 한다.
5. **이름이 짧고 강하다** (영문 1~2단어 / 한글 2~4자) + 온라인 위주 → 워드마크가 가장 세다.
6. **다 해당 없음** → 조합형.

**용도가 여러 개면 가장 좁은 제약을 따른다.** 앱 아이콘 + 간판이면 둘 다 만족해야 하므로 심볼이 강한 조합형이다. 제약은 합집합이 아니라 교집합에서 산다.

## 3. Q4 느낌 → 디자인 속성 번역표

**이 표가 참조 브랜드를 프롬프트 언어로 바꾸는 장치다.** 프롬프트에는 오른쪽 열만 들어간다. 브랜드명은 절대 들어가지 않는다.

| 사용자가 고른 것 | 프롬프트에 들어갈 속성 | 색 성향 | 폰트 성향 |
|---|---|---|---|
| **깔끔·정돈** | geometric simplicity, generous negative space, single weight, no ornament, flat, precise alignment | 무채색 + 포인트 1색. 저채도 | 기하학적 산세리프, 중간 굵기 |
| **따뜻·손맛** | hand-drawn quality, slightly irregular strokes, organic curves, warm and tactile, imperfect by intent | 흙색·크림·테라코타·머스터드 | 라운드 산세리프 또는 부드러운 세리프 |
| **고급·클래식** | refined thin strokes, high contrast serif, wide letter spacing, restrained, timeless, ample margin | 검정·아이보리·딥네이비 + 금속 포인트 | 하이컨트라스트 세리프, 넓은 자간 |
| **재미·개성** | bold heavy weight, playful proportion, unexpected shape, high contrast, confident | 고채도 원색 대비 | 굵은 산세리프, 커스텀 느낌 |

**"고급·클래식"과 "간판" 용도가 충돌하면 용도가 이긴다.** 얇은 획은 멀리서 사라진다. 이때는 "고급"을 획 굵기가 아니라 **여백과 자간과 절제된 색**으로 구현한다. 충돌을 사용자에게 되묻지 말고 이렇게 푼다.

## 4. 색 — 3개를 넘기지 않는다

- **주색 1 + 보조 1 + 무채색 1.** 초보자 로고가 촌스러워지는 1번 원인이 색이 많은 것이다.
- Recraft를 쓸 때는 `colors` 파라미터에 HEX를 넣어 **팔레트를 잠근다.** 프롬프트로 색을 부탁하는 것보다 훨씬 정확하다.
- **업종 상투구는 피한다**: 카페=갈색, 병원=파랑, 친환경=초록. 틀린 건 아니지만 그 업종 전체와 똑같아진다. 상투색을 쓸 거면 톤을 비틀어서(예: 초록 대신 딥 제이드) 쓴다.
- **흑백에서 무너지는 색 조합을 경계한다.** 명도가 비슷한 두 색은 흑백 변환하면 한 덩어리가 된다. `scripts/logo_qa.py`의 흑백 패널이 이걸 잡아준다.

## 5. 폰트

로고의 글자는 이미지로 생성되지만, **사용자에게 넘길 "추천 폰트 이름"은 별개**다. 나중에 명함·PPT·자막에서 톤을 맞추는 데 쓴다.

- 한글 → `references/korean-type.md` (무료 상업용만 추천한다. 유료 폰트를 모르고 쓰면 사용자가 나중에 라이선스 사고를 겪는다)
- 영문 → Inter, Montserrat, Poppins (산세리프) / Playfair Display, Cormorant (세리프) — 모두 무료

## 6. 프롬프트 문법

로고 프롬프트는 **7개 슬롯**으로 쓴다. 빠뜨리면 모델이 알아서 채우는데, 대개 원하지 않는 방향으로 채운다.

```
[1 로고 타입] [2 심볼 아이디어] [3 스타일 속성] [4 타이포그래피] 
[5 색] [6 배경] [7 피해야 할 것]
```

**7번(negative)이 로고에서 특히 중요하다.** 이미지 모델은 로고를 그리라고 하면 자꾸 "로고가 인쇄된 명함 사진"이나 "로고를 든 사람"을 그린다. 명시적으로 막아야 한다.

기본 negative (거의 항상 붙인다):
```
no mockup, no business card, no photograph of a logo, no 3D render, no drop shadow, 
no gradient mesh, no watermark, no additional text, no tagline, no border frame, 
flat vector artwork on plain background
```

**배경은 순백(#FFFFFF) 플랫으로 고정한다.** 이유가 둘이다: ① 로고를 판단할 때 배경이 개입하면 안 된다 ② `logo_qa.py`의 투명화가 안정적으로 작동한다. Recraft는 `background_color: "#FFFFFF"`로 명시 지정할 수 있다.

**작성 예 (깔끔·정돈 / 조합형 / 앱 아이콘 포함):**
```
A minimal combination logo for a brand named "OPPADU": a geometric symbol above a 
wordmark. Symbol: an abstract mark built from two overlapping rounded squares 
suggesting a spreadsheet cell and a door. Style: geometric simplicity, generous 
negative space, single stroke weight, flat, precise alignment, no ornament. 
Typography: clean geometric sans-serif, medium weight, wide tracking, all caps. 
Color: deep jade (#059669) with charcoal (#111827). Background: flat pure white. 
Negative: no mockup, no business card, no photograph, no 3D, no shadow, no gradient, 
no watermark, no extra text, no frame. Flat vector artwork, centered, ample margin.
```

**심볼 아이디어(슬롯 2)를 "적절한 아이콘"처럼 비워두지 않는다.** 그러면 모델이 업종 상투 아이콘(카페=컵, 교육=학사모)을 꺼낸다. Q2의 한 줄에서 **구체적 형상을 스킬이 만들어낸다.** 4장이 서로 다른 시안이 되려면 심볼 아이디어 4개가 서로 달라야 한다.

## 7. 검수 6기준

확정 전에 스킬이 스스로 통과시킨다. 사용자에게 묻지 않는다. (초보자는 이 기준을 모르기 때문에 물어도 답이 안 나온다.)

1. **작은 크기** — 32px에서 형태가 남는가 → `logo_qa.py`가 자동 판정
2. **흑백** — 색을 빼도 구분되는가 → `logo_qa.py`가 자동 판정
3. **어두운 배경** — 밤 배너·다크모드에서 보이는가 → `logo_qa.py`가 자동 판정
4. **기억성** — 5초 보고 대충 그릴 수 있는가. 요소가 3개를 넘으면 대개 실패다
5. **독창성** — 업종 상투 아이콘 그대로인가. 카페=컵, 엑셀=초록 격자면 다시 뽑는다
6. **글자** — 한글 자모 분리·오탈자·유령 글자 (한글이면 매번, 영문이면 스펠링만)

1~3은 스크립트가, 4~6은 스킬이 눈으로 본다. **미달이면 사용자에게 보이기 전에 재생성한다.** 초보자에게 "이거 작게 하면 안 보이는데 괜찮으세요?"라고 묻는 건 판단을 떠넘기는 것이다.
