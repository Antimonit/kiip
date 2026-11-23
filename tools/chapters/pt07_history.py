# -*- coding: utf-8 -*-
"""제7편 역사 — the spread that closes the part, pp. 228-231.

Not a chapter: every 편 ends with four pages of its own. This one has no
crossword — 대단원 정리 is a ladder game over the old kingdoms and three
tables by century — then 단원 종합 평가, then two pages of pictures: 한국의
대표적인 문화유산 and 지도로 살펴보는 한국 역사. Transcribed from the photos.

The answers to the 종합 평가 are mine, worked out from the chapters. The book
keeps its own in 정답보기, which is not photographed, so if one of mine is
wrong the book is not to blame. The ladder's boxes (가)-(마) are left open,
as the page leaves them.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, FIGURE, TABLE, CELL,
               LABELS)

PART = dict(
    number=7, slug="part-7", part=True,
    unit="역사", title="대단원 마무리", titleEn="Closing the part",

    append=[
        SECTION("summary", "대단원 정리"),
        PARAGRAPH("1. 고조선 : 기원전 2333년에 단군왕검이 건국(한국 최초의 국가), 8조법으로 사회 질서 "
                  "유지"),
        HEADING(4, "2. 사다리 타기 놀이를 하면서 (가)~(마)에 들어갈 나라 이름을 써 보세요."),
        TABLE([["(가)", "(나)", "(다)", "통일 신라", "발해"]]),
        FIGURE("사다리 — 위의 다섯 칸에서 내려오는 세로줄 다섯 개와 그 사이를 잇는 가로줄들. 줄을 따라 "
               "내려가면 아래의 다섯 칸 가운데 하나에 닿는다."),
        TABLE([["신라에 침입한 왜를 물리침 / 5세기에 한반도 중부 지역까지 차지",
                "대조영에 의해 나라가 세워짐 / (라) 문화를 바탕으로 주변 나라의 문화도 받아들임",
                "온조에 의해 나라가 세워짐 / 4세기에 전성기를 맞이함",
                "화랑도를 육성함 / 삼국 통일을 이룩함",
                "(마)와 함께 남북국이라 불림 / 석굴암, 불국사를 만들었음"]]),
        HEADING(4, "3. 고려 시대"),
        TABLE(["10세기", "11세기", "12세기", "13세기", "14세기"],
              [["후삼국 통일 / 불교 강조 / 서희의 외교 담판",
                "거란의 침입 / 귀주대첩",
                "무신정변",
                "몽골의 침략 / 직지심체요절 발행",
                "홍건적과 왜구의 침입 / 위화도 회군"]]),
        HEADING(4, "4. 조선 시대"),
        TABLE(["14세기 말 ~15세기", "16세기", "17세기", "18세기", "19세기"],
              [["조선 건국 / 훈민정음 창제 / 경국대전 완성",
                "서원 건립 / 임진왜란(일본의 침입) / 이순신의 활약",
                "병자호란(청나라의 침입)",
                "수원 화성 건립(정조)",
                "흥선 대원군의 개혁 정치 / 독립 협회 활동"]]),
        HEADING(4, "5. 일제 강점기"),
        TABLE([["일제의 식민 통치 (1910~1945)",
                "강압 통치 실시 / 중 · 일 전쟁, 태평양 전쟁 때 한국인들을 강제 동원함"],
               ["한국인의 독립운동",
                "유관순, 김구, 이봉창, 윤봉길 등 / 대한민국 임시 정부 수립하여 독립운동 전개"]]),

        SECTION("exam", "단원 종합 평가"),
        HEADING(4, "01 (가)에 해당하는 국가로 옳은 것은?"),
        FIGURE("우표 두 장 (대한민국 KOREA 2008, 250) — 왼쪽은 곰과 호랑이 앞에 선 사람, 오른쪽은 "
               "꽃 사이에 아이를 가운데 두고 선 남녀"),
        PARAGRAPH("이 우표에는 곰에서 인간이 된 웅녀가 환웅과 결혼하여 단군왕검을 낳은 이야기가 그려져 "
                  "있습니다. 단군왕검이 세웠다고 전해지는 (가)은/는 한국인이 세운 최초의 나라입니다."),
        BULLET("① 신라"),
        BULLET("② 백제"),
        BULLET("③ 고조선"),
        BULLET("④ 고구려"),
        PARAGRAPH("정답 ( ③ )"),

        HEADING(4, "02 다음 중 고려 태조 왕건에 대한 설명으로 옳은 것은?"),
        BULLET("① 후삼국을 통일하였다."),
        BULLET("② 과거 제도를 실시하였다."),
        BULLET("③ 일본 군대와 싸워 이겼다."),
        BULLET("④ 남한산성에서 청나라에 맞서 싸웠다."),
        PARAGRAPH("정답 ( ① )"),

        HEADING(4, "03 다음 기구를 처음으로 만든 조선 시대의 왕에 대한 설명으로 옳은 것은?"),
        FIGURE("앙부일구(해시계) — 다리가 달린 오목한 솥 모양의 기구"),
        FIGURE("측우기(비의 양을 재는 기구) — 測雨臺라고 새긴 돌 받침 위에 놓인 원통"),
        BULLET("① 조선을 건국하였다."),
        BULLET("② 수원 화성을 만들었다."),
        BULLET("③ 경국대전을 완성하였다."),
        BULLET("④ 훈민정음을 창제하였다."),
        PARAGRAPH("정답 ( ④ )"),

        HEADING(4, "04 다음 중 한국의 독립을 위해 노력한 인물의 활동으로 옳지 않은 것은?"),
        BULLET("① 흥선 대원군이 {척화비}를 세웠다."),
        BULLET("② 김구가 대한민국 임시 정부를 이끌었다."),
        BULLET("③ 윤봉길이 홍커우 공원에서 {의거}를 일으켰다."),
        BULLET("④ 유관순이 3·1 운동에 참여하여 만세 {시위}를 벌였다."),
        PARAGRAPH("정답 ( ① )"),

        SECTION("feature", "한국의 대표적인 문화유산"),
        HEADING(4, "고조선"),
        FIGURE("비파형 동검 — 날이 비파 모양으로 불룩한 청동 검 두 자루"),
        HEADING(4, "고구려"),
        FIGURE("금동 연가 7년명 여래 입상 — 큰 광배를 등지고 선 금빛 불상"),
        HEADING(4, "백제"),
        FIGURE("부여 정림사지 5층 석탑 — 절터에 선 다섯 층 돌탑"),
        HEADING(4, "신라"),
        FIGURE("첨성대 — 돌을 병 모양으로 쌓아 올린 탑"),
        HEADING(4, "통일 신라"),
        FIGURE("불국사 — 돌계단과 석축 위에 선 절 건물"),
        HEADING(4, "발해"),
        FIGURE("영광탑 — 다섯 층 벽돌탑"),
        HEADING(4, "고려"),
        FIGURE("영주 부석사 무량수전 — 기와지붕을 얹은 나무 건물"),
        FIGURE("팔만대장경판 — 글자를 빽빽이 새긴 나무판"),
        HEADING(4, "조선"),
        FIGURE("삼강행실도 — 그림과 글이 실린 책장과 三綱行實이라 쓴 표지"),
        FIGURE("자격루 — 전시실에 복원해 놓은 물시계"),

        SECTION("feature", "지도로 살펴보는 한국 역사"),
        FIGURE("고조선의 문화 범위 — 만주와 한반도 북부를 칠한 지도. 비파형 동검과 탁자식 고인돌이 "
               "나온 곳을 기호로 표시함"),
        LABELS("고조선 관련 문화 범위", "비파형 동검 분포 지역", "탁자식 고인돌 분포 지역",
               "농안", "창춘", "옌지", "백두산", "묘향산", "산하이관", "평양", "구월산", "마니산"),
        FIGURE("4세기 삼국의 상황 — 백제가 한반도 중서부와 남서부를 넓게 차지한 지도"),
        LABELS("고구려", "백제", "신라", "가야", "탐라", "동해", "황해"),
        FIGURE("5세기 삼국의 상황 — 고구려가 한반도 중부까지 내려온 지도"),
        LABELS("고구려", "백제", "신라", "가야", "탐라", "동해", "황해"),
        FIGURE("6세기 삼국의 상황 — 신라가 동해안을 따라 북쪽으로, 또 한반도 중부로 넓어진 지도"),
        LABELS("고구려", "신라", "백제", "탐라", "동해", "황해"),
        FIGURE("후삼국 시대 — 한반도를 셋으로 나눈 지도"),
        LABELS("고려", "후백제", "신라", "동해", "황해"),
        FIGURE("통일 신라와 발해 — 북쪽의 발해와 남쪽의 신라를 나누어 칠한 지도"),
        LABELS("발해", "신라", "일본", "동해", "황해"),
        FIGURE("고려 시대 — 고려와 그 둘레의 나라, 바다 건너의 항구를 표시한 지도"),
        LABELS("거란(요)", "여진", "고려", "서경", "개경", "벽란도", "동경", "합포", "탐라",
               "우산", "덩저우", "밍저우", "일본", "동해", "황해"),
        FIGURE("조선 시대 — 여덟 도를 나누어 칠한 지도"),
        LABELS("함길도(함경도)", "평안도", "황해도", "한성", "강원도", "경기도", "충청도",
               "경상도", "전라도"),
        FIGURE("현대 — 한반도의 도를 나누어 칠한 지도"),
        LABELS("함경북도", "함경남도", "평안북도", "평안남도", "황해도", "경기도", "강원도",
               "충청북도", "충청남도", "경상북도", "경상남도", "전라북도", "전라남도", "제주도",
               "울릉도", "독도", "서해", "동해", "남해"),
    ],

    extraAnnotations={
        "척화비": dict(
            hanja="斥和碑", meaning="a stele rejecting peace with the West",
            characters=[("斥", "척", "to repel, to reject — as in 배척"),
                        ("和", "화", "peace, harmony — as in 평화, 화해"),
                        ("碑", "비", "a stone monument — as in 비석")],
            notes=["Set up across the country by 흥선 대원군 in 1871, to say "
                   "that making terms with the Western powers was selling the "
                   "country."],
        ),
        "의거": dict(
            hanja="義擧", meaning="a righteous deed, an act of resistance",
            characters=[("義", "의", "righteousness — as in 정의, 의무"),
                        ("擧", "거", "to raise, to carry out — as in 선거")],
            notes=["The word for an attack made in the cause of "
                   "independence: 윤봉길 의거, 이봉창 의거."],
        ),
        "시위": dict(
            hanja="示威", meaning="a demonstration",
            characters=[("示", "시", "to show — as in 표시, 제시"),
                        ("威", "위", "might, force — as in 위협, 권위")],
        ),
    },

    extraNotes=[
        "제7편's closing spread runs pp. 228-231. It has no crossword.",
        "The ladder game of 대단원 정리 is not reproduced. Its five boxes "
        "above and five boxes below are set as two rows, in the order the "
        "page prints them from left to right; which lower box each upper one "
        "leads to is what the ladder decides, so a box does not belong to "
        "the one set over it here. The boxes (가) to (마) are left open, as "
        "on the page.",
        "The tables of 대단원 정리 print each cell's points as bullets; they "
        "are joined here with a slash, as a cell holds one run of text.",
        "The answers to the 종합 평가 are mine — worked out from the chapters, "
        "since 정답보기 is not photographed.",
        "The photographs on p. 230 and the maps on p. 231 are not "
        "reproduced. Each is set as its printed caption with a description "
        "of mine after the dash, and a map is followed by the names printed "
        "on it. The river names on the 고조선 map and the city names on the "
        "현대 map are too small in the photographs to read and are left out.",
    ],
)
