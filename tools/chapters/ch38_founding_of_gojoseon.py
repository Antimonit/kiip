# -*- coding: utf-8 -*-
"""Chapter 38 — The founding of 고조선.

Transcribed from the photos of pp. 200-203. The pages carry no handwriting.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, VERSE,
               TABLE, CELL, GLOSSARY)

CHAPTER = dict(
    number=38, slug="38-founding-of-gojoseon",
    unit="역사", title="고조선의 건국", titleEn="The founding of 고조선",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 {비파형 동검}과 {고인돌}의 모습입니다.",
                  "Below are a 비파형 동검 (lute-shaped bronze dagger) and a "
                  "고인돌 (dolmen)."),
        FIGURE("비파형 동검 다섯 자루의 사진 · 받침돌 두 개 위에 덮개돌을 얹은 고인돌의 사진"),
        HEADING(4, "01 비파형 동검과 고인돌은 각각 어떤 {용도}로 사용되었을까요?",
                translation="What were the 비파형 동검 and the 고인돌 each "
                            "used for?"),
        HEADING(4, "02 이들 {유물}을 {남긴|남기다} 사람들은 어느 시대 사람들이었을까요?",
                translation="Which age did the people who left these relics "
                            "belong to?"),

        SECTION("goals", "학습목표"),
        BULLET("한국 역사의 {흐름}을 세계 역사와의 {관련} 속에서 설명할 수 있다.", ordered=True,
               translation="Explain the course of Korean history in relation "
                           "to world history."),
        BULLET("{고조선}의 생활 모습에 대해 설명할 수 있다.", ordered=True,
               translation="Explain what life was like in 고조선."),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"],
              [["기본", "사회", "1. 한국의 상징", "한국의 국기와 국가"]]),

        SECTION("part", "01 한국 역사는 어떻게 변해 왔을까?"),
        HEADING(2, "한국 역사를 배우는 이유", translation=
                "Why Korean history is studied" "\n\n"
                "As Park Eun-sik, a Korean historian and independence "
                "activist, said, where history stands upright the country "
                "can stand upright too. The reason for studying not only "
                "what Korea is like today but its history as well is to "
                "understand Korea’s yesterday and today accurately and to "
                "lead Korea in the right direction. Korea’s today lies "
                "within its history, and Korea’s past is held within the "
                "shape of Korean society today."),
        VERSE("나라의 교육과 역사가 없어지지 {아니하면|아니하다} 그 나라는 {망하지|망하다} 않는다.",
              translation="If a country’s education and history do not "
                          "disappear, that country does not fall."),
        SOURCE("-박은식-"),
        PARAGRAPH("한국의 {역사학자}이자 {독립운동가}였던 {박은식}의 말처럼 역사가 {바로} 서 있으면 "
                  "나라도 바로 설 수 있다. {현대} 한국의 모습뿐만 아니라 한국의 역사를 공부하는 이유는 "
                  "한국의 어제와 오늘을 정확하게 이해하고 한국을 {올바른|올바르다} {방향}으로 "
                  "{이끌어|이끌다} 가기 위해서이다. 한국의 역사 속에 한국의 오늘이 들어 있고, 현대 한국 "
                  "사회의 모습 속에 한국의 {과거}가 {담겨|담기다} 있다."),

        HEADING(2, "한국사의 흐름", translation=
                "The course of Korean history" "\n\n"
                "What history has been carried on in the Korean peninsula, "
                "where Korea lies? Let us look at the chronology and see how "
                "the history of Korea and the history of other countries "
                "have changed."),
        PARAGRAPH("한국이 {자리 잡고|자리 잡다} 있는 {한반도}에서는 어떤 역사가 {이어져|이어지다} 오고 "
                  "있을까? {연표}를 보면서 한국의 역사와 다른 나라의 역사가 어떻게 변화해 왔는지 "
                  "{살펴보자|살펴보다}."),
        TABLE(["유럽, 미국 지역", "한국", "아시아 지역"],
              [["{기원전} 3500년경 메소포타미아 {문명} 시작", "",
                "기원전 2500년경 중국 문명, 인도 문명 시작"],
               ["기원전 3000년경 이집트 문명 시작", "기원전 2333년 고조선 {건국}", ""],
               ["기원전 27년 로마, {제정} {수립}", "기원전 57년 신라 건국",
                "기원전 7세기 베트남, 반랑국 건국"],
               ["", "기원전 37년 고구려 건국", ""],
               ["476년 서로마 제국 {멸망}", "기원전 18년 백제 건국",
                "기원전 221년 진(秦), 중국 통일"],
               ["", "676년 신라, 삼국 {통일}", ""],
               ["1096년 십자군 전쟁 시작", "698년 대조영, 발해 건국",
                "610년경 이슬람교 {성립}"],
               ["", "918년 왕건, 고려 건국", "890년 캄보디아, 앙코르 {왕조} 성립"],
               ["1337년 영국·프랑스, 백년 전쟁 시작", "1392년 이성계, 조선 건국",
                "1206년 칭기즈 칸, 몽골 통일"],
               ["1517년 루터의 {종교 개혁}", "1592년 {임진왜란}",
                "1590년 도요토미 히데요시, 일본 통일"],
               ["1600년 영국, 동인도 회사 설립", "1636년 {병자호란}",
                "1868년 일본, 메이지 유신"],
               ["1789년 프랑스 {혁명}", "1897년 대한 제국 수립", "1912년 쑨원, 중화민국 수립"],
               ["", "1910년 대한 제국, {국권} {빼앗김|빼앗기다}", ""],
               ["1914년 제1차 세계 대전(~1918)",
                "1919년 3·1 운동, 대한민국 {임시 정부} 수립", "1919년 중국, 5·4 운동"],
               ["1939년 제2차 세계 대전(~1945)", "1945년 8·15 {광복}",
                "1937년 중·일 전쟁 {발발}"],
               ["", "1948년 대한민국 정부 수립", ""],
               ["1945년 국제 연합(UN) {창설}", "1950년 6·25 전쟁(~1953)",
                "1949년 중국, 중화 인민 공화국 수립"],
               ["1948년 세계 인권 선언", "1960년 4·19 혁명",
                "1976년 베트남 사회주의 공화국 수립"],
               ["", "1980년 5·18 민주화 운동", ""],
               ["1990년 독일 통일", "1987년 6월 민주 {항쟁}",
                "1992년 중국과 베트남, 한국과 {수교}"],
               ["1991년 소련 {해체}", "2000년 최초의 남북 {정상회담}", ""]]),

        SECTION("part", "02 고조선의 생활 모습은 어떠했을까?"),
        GLOSSARY(("삼국유사",
                  "고려 시대의 스님 일연이 고구려·백제·신라 3국의 유사(전해 내려오는 이야기)를 모아 "
                  "만든 역사책", "삼국유사",
                  dict(en="a history book made by 일연, a monk of the 고려 period, who gathered the 유사 (stories handed down) of the three kingdoms 고구려, 백제 and 신라")),
                 ("숭배", "우러러 보며 공경함", "숭배",
                  dict(en="looking up to and revering")),
                 ("신석기", "돌을 갈아 만든 도구", "신석기",
                  dict(en="a tool made by grinding stone")),
                 ("청동기", "구리와 주석 등으로 만든 도구", "청동기",
                  dict(en="a tool made of copper, tin and the like"))),
        HEADING(2, "고조선의 건국", translation=
                "The founding of 고조선" "\n\n"
                "Did a bear really become a person, as the passage above "
                "has it? Is the ancestor of the Korean people a bear? The "
                "story of the founding of 고조선, the beginning of Korean "
                "history, is interpreted as follows." "\n\n"
                "In Manchuria and the Korean peninsula there lived a tribe "
                "that worshipped the bear and a tribe that worshipped the "
                "tiger. Around the time the Neolithic age was drawing to a "
                "close, the 환웅 tribe, who claimed to be descendants of "
                "heaven, moved into the Korean peninsula. The 환웅 tribe, "
                "who had superior weapons made of bronze, joined forces with "
                "the tribe that worshipped the bear and drove off the tribe "
                "that worshipped the tiger. The 환웅 tribe and the tribe "
                "that worshipped the bear became one through marriage, and "
                "made a new tribe with 단군왕검 as its ruler. 단군왕검 "
                "afterwards founded a country, and that country is 고조선, "
                "the first state the Korean people founded."),
        VERSE("하늘에서 내려 온 {환웅}이 인간 세상을 {다스리고|다스리다} 있었는데, 어느 날 곰과 "
              "호랑이가 찾아와 인간이 되게 해 달라고 {빌었다|빌다}. 환웅은 100일 동안 {쑥}과 "
              "{마늘}만 먹으며 {햇빛}을 보지 않으면 인간이 될 수 있다고 했다. 호랑이와 달리, 환웅의 "
              "말대로 한 곰은 여자가 되었고, 환웅과 결혼하였다. 둘 사이에서 태어난 {단군왕검}이 "
              "고조선을 {세웠다|세우다}.",
              translation="환웅, who had come down from heaven, was governing "
                          "the human world when one day a bear and a tiger "
                          "came to him and begged to be made human. 환웅 said "
                          "that they could become human if they ate only "
                          "mugwort and garlic for a hundred days and did not "
                          "see the sunlight. Unlike the tiger, the bear did "
                          "as 환웅 said, became a woman and married 환웅. "
                          "단군왕검, who was born to the two, founded 고조선."),
        SOURCE("- 〈삼국유사〉 -"),
        PARAGRAPH("위의 글처럼 곰이 정말 사람이 된 것일까? 한국인의 {조상}은 곰일까? 한국 역사의 시작인 "
                  "고조선 건국 이야기는 다음과 같이 {해석되고|해석되다} 있다."),
        PARAGRAPH("{만주} 및 한반도에 곰을 {숭배}하는 {부족}과 호랑이를 숭배하는 부족이 살고 있었다. "
                  "{신석기} 시대가 끝나갈 {무렵}, 하늘의 {자손}이라고 주장하는 환웅 부족이 한반도로 "
                  "{이동하여|이동하다} 들어왔다. {청동기}로 만든 {우수한|우수하다} {무기}를 갖고 있던 "
                  "환웅 부족은 곰을 숭배하는 부족과 힘을 {합쳐|합치다} 호랑이를 숭배하는 부족을 "
                  "{물리쳤다|물리치다}. 환웅 부족과 곰을 숭배하는 부족은 결혼을 통해 하나가 되었고, "
                  "단군왕검을 {지배자}로 하는 새로운 부족을 만들었다. 이후 단군왕검은 나라를 세웠는데, "
                  "그 나라가 바로 한국인이 세운 첫 번째 국가인 고조선이다."),
        FIGURE("고조선의 문화 범위 — 만주와 한반도 지도. 범례: 고조선 관련 문화 범위, 비파형 동검 분포 "
               "지역, 탁자식 고인돌 분포 지역"),

        GLOSSARY(("노비", "사회적으로 가장 신분이 낮은 남자 종(노)과 여자 종(비)을 가리킴", "노비",
                  dict(en="refers to the male servant (노) and the female servant (비), of the lowest standing in society"))),
        HEADING(2, "고조선의 생활 모습", translation=
                "Life in 고조선" "\n\n"
                "To keep order in society, 고조선 made a law of eight "
                "provisions (the 8조법). Three of them have come down to the "
                "present."),
        PARAGRAPH("고조선은 사회 {질서}를 {유지하기|유지하다} 위해 여덟 가지 내용의 법({8조법})을 "
                  "만들었다. 이 중 세 가지 내용이 현재까지 {전해지고|전해지다} 있다."),
        BULLET("사람을 죽인 {자}는 {사형}에 {처한다|처하다}.", ordered=True,
               translation="One who kills a person is put to death."),
        BULLET("남을 다치게 한 자는 {곡식}으로 {갚는다|갚다}.", ordered=True,
               translation="One who injures another repays it in grain."),
        BULLET("{도둑질한|도둑질하다} 자는 {도둑맞은|도둑맞다} 집의 {노비}로 {삼는데|삼다}, {죄}를 "
               "{용서} 받으려면 50만 {전}의 돈을 내야 한다.", ordered=True,
               translation="One who steals is made a servant of the house "
                           "that was robbed, and to be pardoned for the "
                           "offence must pay 500,000 전 in money."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "강화 참성단과 개천절", translation=
                "참성단 on Ganghwa and 개천절" "\n\n"
                "참성단, on Mani-san on Ganghwa-do in Incheon, is the place "
                "where, the story goes, 단군왕검 held rites to heaven. On "
                "the basis of the record that 고조선 was founded on 3 October "
                "2333 BC, Korea has made 3 October a national holiday called "
                "개천절 (meaning ‘the day heaven opened’). And when 개천절 "
                "comes, rites are held to 단군왕검 at 참성단. The flame (the "
                "sacred torch) used at the athletics meeting held in Korea "
                "every year (the National Sports Festival) is also lit "
                "here."),
        PARAGRAPH("인천의 강화도 {마니산}에 있는 {참성단}은 단군왕검이 하늘에 {제사}를 지냈다는 이야기가 "
                  "전해 오는 곳이다. 기원전 2333년 10월 3일에 고조선이 세워졌다는 {기록}을 {바탕}으로 "
                  "한국에서는 10월 3일을 {개천절}(‘하늘이 열린 날’이라는 뜻)이라는 {국경일}로 정했다. "
                  "그리고 개천절이 되면 참성단에서 단군왕검에게 제사를 지낸다. 또한, 한국에서 매년 열리는 "
                  "체육대회({전국체전})에 사용되는 불({성화})도 이곳에서 만들고 있다."),
        FIGURE("강화 참성단"),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 한국 역사는 어떻게 변해 왔을까?"),
        BULLET("한국의 역사학자이자 독립운동가였던 (        )은 “나라의 교육과 역사가 없어지지 "
               "아니하면 그 나라는 망하지 않는다.”라는 말을 통해 역사의 중요성을 강조하였다."),
        BULLET("현대 한국의 모습뿐 아니라 한국의 (        )를 공부하는 이유는 한국의 어제와 오늘을 "
               "정확하게 이해하고 한국을 올바른 방향으로 이끌어가기 위해서이다."),
        HEADING(3, "02 고조선의 생활 모습은 어떠했을까?"),
        BULLET("한국인이 세운 첫 번째 국가는 (        )이다."),
        BULLET("고조선을 세운 사람은 (        )이다."),
        BULLET("고조선의 사회 질서를 유지하기 위해 (        )을 만들었는데, 현재는 그중 3가지만 "
               "전해지고 있다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "[『{삼국유사}』에 기록된 단군의 고조선 건국 이야기]"),
        PARAGRAPH("하늘을 다스리는 {환인}에게는 환웅이라는 아들이 있었다. 환웅은 늘 땅을 "
                  "{굽어보며|굽어보다} 인간 세상을 다스리고 싶어 했다. {마침내} 환웅은 비, 구름, 바람을 "
                  "각각 {맡은|맡다} 신들을 이끌고 한반도의 {태백산}에 내려왔다. 이후 환웅은 ‘{널리} "
                  "인간을 {이롭게|이롭다} 한다.’라는 {홍익인간}의 뜻을 {펼치며|펼치다} 인간 세상을 "
                  "다스렸다. 그러던 어느 날 인간 세계를 다스리던 환웅에게 곰과 호랑이가 찾아와서 말했다."),
        PARAGRAPH("“저희는 사람이 되고 싶습니다. 사람이 되게 해 주세요.”"),
        PARAGRAPH("그러자 환웅이 곰과 호랑이에게 쑥과 마늘을 주며 대답하였다."),
        PARAGRAPH("“100일 동안 {동굴}에서 이것을 먹고 지내라. 그러면 사람이 될 수 있을 것이다.”"),
        PARAGRAPH("곰과 호랑이는 환웅의 말대로 동굴에 들어가서 쑥과 마늘을 먹으며 지냈다. 하지만 호랑이는 "
                  "그것을 {견디지|견디다} 못하고 {도중}에 동굴을 나와 {도망치고|도망치다} 말았다. 끝까지 "
                  "잘 견뎌 낸 곰은 여자로 {변하여|변하다} 환웅과 결혼하였다. 둘 사이에 건강한 아이가 "
                  "태어났는데 그 아이가 바로 단군왕검이다. {무럭무럭} 자란 단군왕검은 청동기 문화를 "
                  "바탕으로 나라(고조선)을 세웠다."),
        PARAGRAPH("★ 자신의 고향 나라에 전해지는 건국 {신화}나 건국 이야기를 말해 봅시다. 단군의 고조선 "
                  "건국 이야기와 어떤 {차이점}과 {공통점}이 있는지 이야기를 나눠 봅시다.",
                  "Tell the founding myth or founding story handed down in "
                  "your home country. Talk about how it differs from the "
                  "story of 단군’s founding of 고조선 and what the two have "
                  "in common."),
    ],

    english={
        "[『삼국유사』에 기록된 단군의 고조선 건국 이야기]": dict(
            title="The story of 단군’s founding of 고조선 as recorded in "
                  "the 삼국유사",
            paragraphs=[
                "환인, who governed heaven, had a son called 환웅. 환웅 was "
                "always looking down on the earth and wished to govern the "
                "human world. At last 환웅 came down to Taebaek-san on the "
                "Korean peninsula, leading the gods who had charge of the "
                "rain, the clouds and the wind. Thereafter 환웅 governed the "
                "human world, spreading the ideal of 홍익인간, ‘to benefit "
                "humankind widely’. Then one day a bear and a tiger came to "
                "환웅, who was governing the human world, and spoke.",
                "“We wish to become human. Please make us human.”",
                "At that 환웅 gave the bear and the tiger mugwort and garlic "
                "and answered.",
                "“Live in a cave for a hundred days eating this. Then you "
                "will be able to become human.”",
                "The bear and the tiger went into a cave as 환웅 had said "
                "and lived on mugwort and garlic. But the tiger could not "
                "bear it, and part-way through came out of the cave and ran "
                "away. The bear, who bore it well to the end, turned into a "
                "woman and married 환웅. A healthy child was born to the "
                "two, and that child is 단군왕검. 단군왕검, who grew up "
                "strong, founded a country (고조선) on the basis of Bronze "
                "Age culture.",
            ],
        ),
    },

    extraAnnotations={
        "비파형 동검": dict(
            hanja="琵琶形銅劍", meaning="a lute-shaped bronze dagger",
            characters=[("琵琶", None, "the 비파, a pear-shaped lute — 琵 and "
                                      "琶 both name the instrument"),
                        ("形", "형", "a shape — as in 형태, 삼각형"),
                        ("銅", "동", "copper, bronze — as in 청동, 동메달"),
                        ("劍", "검", "a sword — as in 검도")],
            notes=["The dagger typical of the 고조선 culture area; the blade "
                   "swells out like the body of a 비파."],
        ),
        "고인돌": dict(
            meaning="a dolmen",
            notes=["A native word: 고이다 “to prop up” + 돌 “stone” — a stone "
                   "that is propped up. A Bronze Age tomb."],
        ),
        "용도": dict(
            hanja="用途", meaning="a use, a purpose",
            characters=[("用", "용", "to use — as in 사용, 이용"),
                        ("途", "도", "a road, a way — as in 도중")],
        ),
        "유물": dict(
            hanja="遺物", meaning="a relic, an artefact",
            characters=[("遺", "유", "to leave behind — as in 유산, 유적"),
                        ("物", "물", "a thing — as in 물건, 박물관")],
        ),
        "남기다": dict(meaning="to leave behind", surfaces=["남긴"]),
        "흐름": dict(
            meaning="a flow, a course",
            notes=["The noun of 흐르다 “to flow”. 역사의 흐름 is the course "
                   "of history."],
        ),
        "관련": dict(
            hanja="關聯", meaning="relation, connection",
            characters=[("關", "관", "a gate, to concern — as in 관계, 관심"),
                        ("聯", "련", "to link — as in 연합, 연결")],
        ),
        "고조선": dict(
            hanja="古朝鮮", meaning="고조선, the first Korean state",
            characters=[("古", "고", "old — as in 고대, 고전"),
                        ("朝", "조", "morning, a dynasty — as in 조선, 왕조"),
                        ("鮮", "선", "fresh, bright — as in 신선하다")],
            notes=["The state was called 조선; 古 was added later to tell it "
                   "from the 조선 founded in 1392."],
        ),
        "아니하다": dict(
            meaning="not to (the full form of 않다)",
            notes=["없어지지 아니하면 = 없어지지 않으면. The uncontracted form "
                   "reads as old or formal."],
            surfaces=["아니하면"],
        ),
        "망하다": dict(
            hanja="亡하다", meaning="to fall, to be ruined",
            characters=[("亡", "망", "to perish — as in 멸망, 사망")],
            surfaces=["망하지"],
        ),
        "역사학자": dict(
            hanja="歷史學者", meaning="a historian",
            characters=[("歷", "역", "to pass through — as in 경력, 이력서"),
                        ("史", "사", "history — as in 한국사"),
                        ("學", "학", "learning — as in 학교, 과학"),
                        ("者", "자", "person")],
        ),
        "독립운동가": dict(
            hanja="獨立運動家", meaning="an independence activist",
            characters=[("獨", "독", "alone — as in 독학, 단독"),
                        ("立", "립", "to stand — as in 설립, 수립"),
                        ("運", "운", "to move — as in 운전, 운영"),
                        ("動", "동", "to move — as in 이동, 활동"),
                        ("家", "가", "a person of a calling — as in 작가, "
                                    "전문가")],
        ),
        "박은식": dict(
            hanja="朴殷植",
            meaning="Park Eun-sik (1859-1925), historian and independence "
                    "activist",
            notes=["The second president of the provisional government in "
                   "Shanghai."],
        ),
        "바로": dict(
            meaning="upright, straight; (elsewhere) precisely, right away",
            notes=["바로 서다 “to stand upright”. Further down, 그 나라가 바로 "
                   "… 고조선이다 uses it as “none other than”."],
        ),
        "현대": dict(
            hanja="現代", meaning="the present age, modern times",
            characters=[("現", "현", "to appear, present — as in 현재, 표현"),
                        ("代", "대", "an age, a generation — as in 시대, "
                                    "세대")],
        ),
        "올바르다": dict(meaning="to be right, proper",
                       surfaces=["올바른"]),
        "방향": dict(
            hanja="方向", meaning="a direction",
            characters=[("方", "방", "a side, a way — as in 방법, 지방"),
                        ("向", "향", "to face — as in 향하다, 성향")],
        ),
        "이끌다": dict(meaning="to lead", surfaces=["이끌어", "이끌고"]),
        "과거": dict(
            hanja="過去", meaning="the past",
            characters=[("過", "과", "to pass — as in 통과, 과정"),
                        ("去", "거", "to go, gone — as in 제거")],
        ),
        "담기다": dict(
            meaning="to be held in, to be contained",
            notes=["The passive of 담다 “to put in”."],
            surfaces=["담겨"],
        ),
        "자리 잡다": dict(
            meaning="to be situated, to settle",
            surfaces=["자리 잡고"],
        ),
        "한반도": dict(
            hanja="韓半島", meaning="the Korean peninsula",
            characters=[("韓", "한", "Korea — as in 한국, 대한민국"),
                        ("半", "반", "half — as in 절반, 반년"),
                        ("島", "도", "an island — as in 제주도, 독도")],
            notes=["半島 “half-island” is a peninsula."],
        ),
        "이어지다": dict(
            meaning="to continue, to be carried on",
            surfaces=["이어져"],
        ),
        "연표": dict(
            hanja="年表", meaning="a chronological table",
            characters=[("年", "연", "a year — as in 연도, 매년"),
                        ("表", "표", "a table, a surface — as in 발표, 표현")],
        ),
        "살펴보다": dict(meaning="to look into, to examine",
                       surfaces=["살펴보자"]),
        "기원전": dict(
            hanja="紀元前", meaning="BC, before the common era",
            characters=[("紀", "기", "a record, an era — as in 세기, 기념"),
                        ("元", "원", "the origin, the first — as in 원래"),
                        ("前", "전", "before — as in 이전, 오전")],
        ),
        "문명": dict(
            hanja="文明", meaning="civilisation",
            characters=[("文", "문", "writing, culture — as in 문화, 문자"),
                        ("明", "명", "bright — as in 설명, 분명")],
        ),
        "건국": dict(
            hanja="建國", meaning="the founding of a state",
            characters=[("建", "건", "to build — as in 건물, 건설"),
                        ("國", "국", "a country — as in 국가, 한국")],
        ),
        "제정": dict(
            hanja="帝政", meaning="imperial rule, an empire",
            characters=[("帝", "제", "an emperor — as in 황제, 제국"),
                        ("政", "정", "government — as in 정치, 정부")],
            notes=["Not 제정 (制定), enacting a law, which chapter 21 has."],
        ),
        "수립": dict(
            hanja="樹立", meaning="establishment (of a government, a state)",
            characters=[("樹", "수", "a tree, to plant — as in 가로수"),
                        ("立", "립", "to stand — as in 독립, 설립")],
        ),
        "멸망": dict(
            hanja="滅亡", meaning="downfall, destruction",
            characters=[("滅", "멸", "to extinguish — as in 소멸, 멸종"),
                        ("亡", "망", "to perish — as in 망하다, 사망")],
        ),
        "통일": dict(
            hanja="統一", meaning="unification",
            characters=[("統", "통", "to govern, to gather — as in 대통령, "
                                    "전통"),
                        ("一", "일", "one")],
        ),
        "성립": dict(
            hanja="成立", meaning="coming into being, formation",
            characters=[("成", "성", "to become, to achieve — as in 성공, "
                                    "완성"),
                        ("立", "립", "to stand — as in 수립, 독립")],
        ),
        "왕조": dict(
            hanja="王朝", meaning="a dynasty",
            characters=[("王", "왕", "a king"),
                        ("朝", "조", "a court, a dynasty — as in 조선")],
        ),
        "종교 개혁": dict(
            hanja="宗敎改革", meaning="the Reformation",
            characters=[("宗", "종", "a sect, an ancestor — as in 종교"),
                        ("敎", "교", "to teach — as in 교육, 불교"),
                        ("改", "개", "to change — as in 개선, 개정"),
                        ("革", "혁", "to reform, hide — as in 혁명, 혁신")],
        ),
        "임진왜란": dict(
            hanja="壬辰倭亂",
            meaning="the Japanese invasion of 1592 (the Imjin War)",
            characters=[("壬辰", None, "the year 임진 of the sixty-year "
                                      "cycle, here 1592"),
                        ("倭", "왜", "Japan (an old name)"),
                        ("亂", "란", "a disturbance, a war — as in 혼란, "
                                    "반란")],
        ),
        "병자호란": dict(
            hanja="丙子胡亂",
            meaning="the Manchu (Qing) invasion of 1636",
            characters=[("丙子", None, "the year 병자 of the sixty-year "
                                      "cycle, here 1636"),
                        ("胡", "호", "the northern peoples, here the Manchu"),
                        ("亂", "란", "a disturbance, a war")],
        ),
        "혁명": dict(
            hanja="革命", meaning="a revolution",
            characters=[("革", "혁", "to reform — as in 개혁, 혁신"),
                        ("命", "명", "a mandate, life — as in 생명, 운명")],
        ),
        "국권": dict(
            hanja="國權", meaning="national sovereignty",
            characters=[("國", "국", "a country"),
                        ("權", "권", "a right, power — as in 권리, 주권")],
        ),
        "빼앗기다": dict(
            meaning="to be robbed of, to have taken away",
            notes=["The passive of 빼앗다. 국권 빼앗김 is Japan’s annexation "
                   "of 1910; 빼앗김 is the noun form the chronology ends "
                   "its lines on."],
            surfaces=["빼앗김"],
        ),
        "임시 정부": dict(
            hanja="臨時政府", meaning="a provisional government",
            characters=[("臨", "임", "to face, for the occasion — as in "
                                    "임박"),
                        ("時", "시", "time — as in 시간, 시대"),
                        ("政", "정", "government — as in 정치"),
                        ("府", "부", "an office — as in 정부")],
        ),
        "광복": dict(
            hanja="光復", meaning="liberation (of 15 August 1945)",
            characters=[("光", "광", "light — as in 관광, 영광"),
                        ("復", "복", "to return, to restore — as in 회복, "
                                    "복습")],
            notes=["“Light restored”. 광복절 is 15 August."],
        ),
        "발발": dict(
            hanja="勃發", meaning="an outbreak (of war)",
            characters=[("勃", "발", "sudden"),
                        ("發", "발", "to break out, to send out — as in "
                                    "발생, 출발")],
        ),
        "창설": dict(
            hanja="創設", meaning="founding, establishment",
            characters=[("創", "창", "to begin, to create — as in 창조, 창업"),
                        ("設", "설", "to set up — as in 설립, 시설")],
        ),
        "항쟁": dict(
            hanja="抗爭", meaning="a struggle, resistance",
            characters=[("抗", "항", "to resist — as in 저항, 반항"),
                        ("爭", "쟁", "to contend — as in 전쟁, 경쟁")],
        ),
        "수교": dict(
            hanja="修交", meaning="establishing diplomatic relations",
            characters=[("修", "수", "to cultivate, to mend — as in 수리, "
                                    "연수"),
                        ("交", "교", "to exchange — as in 외교, 교류")],
        ),
        "해체": dict(
            hanja="解體", meaning="dissolution, break-up",
            characters=[("解", "해", "to undo — as in 해결, 이해"),
                        ("體", "체", "a body — as in 단체, 신체")],
        ),
        "정상회담": dict(
            hanja="頂上會談", meaning="a summit meeting",
            characters=[("頂", "정", "the top — as in 정상, 절정"),
                        ("上", "상", "above"),
                        ("會", "회", "to meet — as in 회의, 사회"),
                        ("談", "담", "to talk — as in 상담, 대담")],
        ),
        "삼국유사": dict(
            hanja="三國遺事",
            meaning="the 삼국유사, “Memorabilia of the Three Kingdoms”",
            characters=[("三", "삼", "three"),
                        ("國", "국", "a country"),
                        ("遺", "유", "to leave behind — as in 유물, 유산"),
                        ("事", "사", "a matter, an affair — as in 사건")],
            notes=["Compiled by the monk 일연 in the 고려 period (thirteenth "
                   "century); the oldest surviving record of the 단군 "
                   "story."],
        ),
        "숭배": dict(
            hanja="崇拜", meaning="worship, reverence",
            characters=[("崇", "숭", "lofty, to esteem — as in 숭고하다"),
                        ("拜", "배", "to bow — as in 세배, 예배")],
        ),
        "신석기": dict(
            hanja="新石器", meaning="a Neolithic (polished stone) tool",
            characters=[("新", "신", "new — as in 신문, 신입"),
                        ("石", "석", "stone — as in 석유, 보석"),
                        ("器", "기", "a tool, a vessel — as in 악기, 기구")],
            notes=["신석기 시대 is the Neolithic, the New Stone Age."],
        ),
        "청동기": dict(
            hanja="靑銅器", meaning="a bronze tool",
            characters=[("靑", "청", "blue-green — as in 청년, 청와대"),
                        ("銅", "동", "copper — as in 동검"),
                        ("器", "기", "a tool, a vessel — as in 신석기")],
            notes=["청동기 시대 is the Bronze Age."],
        ),
        "환웅": dict(
            hanja="桓雄", meaning="환웅, the son of heaven in the 단군 story",
            characters=[("桓", "환", "a name character (a kind of tree; "
                                    "bright)"),
                        ("雄", "웅", "male, heroic — as in 영웅")],
        ),
        "다스리다": dict(
            meaning="to govern, to rule",
            surfaces=["다스리고", "다스리는", "다스렸다", "다스리던"],
        ),
        "빌다": dict(meaning="to beg, to pray", surfaces=["빌었다"]),
        "쑥": dict(meaning="mugwort"),
        "마늘": dict(meaning="garlic"),
        "햇빛": dict(meaning="sunlight"),
        "단군왕검": dict(
            hanja="檀君王儉", meaning="단군왕검, the founder of 고조선",
            characters=[("檀", "단", "the sandalwood (birch) tree"),
                        ("君", "군", "a lord — as in 군주"),
                        ("王", "왕", "a king"),
                        ("儉", "검", "thrifty — as in 검소하다; here part of "
                                    "the title")],
            notes=["단군 is read as a priestly title and 왕검 as a ruler’s, "
                   "so the name is taken to show a ruler who was also the "
                   "chief priest. Often shortened to 단군."],
        ),
        "세우다": dict(
            meaning="to found, to set up",
            surfaces=["세웠다", "세웠는데", "세운"],
        ),
        "조상": dict(
            hanja="祖上", meaning="an ancestor",
            characters=[("祖", "조", "a forefather — as in 조부모, 시조"),
                        ("上", "상", "above, earlier")],
        ),
        "해석되다": dict(
            hanja="解釋되다", meaning="to be interpreted",
            characters=[("解", "해", "to undo, to explain — as in 이해, 해결"),
                        ("釋", "석", "to explain, to release — as in 석방")],
            surfaces=["해석되고"],
        ),
        "만주": dict(
            hanja="滿洲", meaning="Manchuria",
            characters=[("滿", "만", "full — as in 만족"),
                        ("洲", "주", "a continent, a land — as in 아시아주")],
        ),
        "부족": dict(
            hanja="部族", meaning="a tribe",
            characters=[("部", "부", "a part, a group — as in 부분, 일부"),
                        ("族", "족", "a clan — as in 가족, 민족")],
            notes=["Not 부족 (不足), a shortage."],
        ),
        "무렵": dict(
            meaning="around the time (of)",
            notes=["끝나갈 무렵 “around the time it was drawing to a "
                   "close”."],
        ),
        "자손": dict(
            hanja="子孫", meaning="descendants",
            characters=[("子", "자", "a child — as in 자녀"),
                        ("孫", "손", "a grandchild — as in 손자, 후손")],
        ),
        "이동하다": dict(
            hanja="移動하다", meaning="to move, to migrate",
            characters=[("移", "이", "to move — as in 이민, 이사"),
                        ("動", "동", "to move — as in 운동, 활동")],
            surfaces=["이동하여"],
        ),
        "우수하다": dict(
            hanja="優秀하다", meaning="to be superior, excellent",
            characters=[("優", "우", "superior — as in 우대, 우승"),
                        ("秀", "수", "outstanding — as in 수재")],
            surfaces=["우수한"],
        ),
        "무기": dict(
            hanja="武器", meaning="a weapon",
            characters=[("武", "무", "martial — as in 무술, 무력"),
                        ("器", "기", "a tool — as in 청동기")],
        ),
        "합치다": dict(
            hanja="合치다", meaning="to join, to combine",
            characters=[("合", "합", "to join — as in 통합, 결합")],
            notes=["힘을 합치다 “to join forces”."],
            surfaces=["합쳐"],
        ),
        "물리치다": dict(meaning="to drive off, to defeat",
                       surfaces=["물리쳤다"]),
        "지배자": dict(
            hanja="支配者", meaning="a ruler",
            characters=[("支", "지", "to support, to hold — as in 지원, 지지"),
                        ("配", "배", "to allot — as in 배달, 분배"),
                        ("者", "자", "person")],
        ),
        "노비": dict(
            hanja="奴婢", meaning="a servant, a slave (male and female)",
            characters=[("奴", "노", "a male servant — as in 노예"),
                        ("婢", "비", "a female servant")],
        ),
        "질서": dict(
            hanja="秩序", meaning="order",
            characters=[("秩", "질", "rank, order"),
                        ("序", "서", "sequence — as in 순서")],
        ),
        "유지하다": dict(
            hanja="維持하다", meaning="to maintain, to keep",
            characters=[("維", "유", "to tie, to hold together"),
                        ("持", "지", "to hold — as in 지속, 소지")],
            surfaces=["유지하기"],
        ),
        "8조법": dict(
            hanja="八條法", meaning="the Eight Provisions, the law of 고조선",
            characters=[("八", "팔", "eight"),
                        ("條", "조", "an article, a clause — as in 조건, "
                                    "제1조"),
                        ("法", "법", "law")],
            notes=["Read 팔조법. Only three of the eight survive."],
        ),
        "전해지다": dict(
            hanja="傳해지다", meaning="to be handed down",
            characters=[("傳", "전", "to pass on — as in 전통, 전달")],
            surfaces=["전해지고", "전해지는"],
        ),
        "자": dict(
            hanja="者", meaning="a person, one who (written, legal)",
            characters=[("者", "자", "person — as in 지배자, 역사학자")],
            notes=["죽인 자 “one who has killed”. As a word on its own it "
                   "belongs to laws and old texts."],
        ),
        "사형": dict(
            hanja="死刑", meaning="the death penalty",
            characters=[("死", "사", "to die — as in 사망"),
                        ("刑", "형", "punishment — as in 형법, 처벌")],
        ),
        "처하다": dict(
            hanja="處하다", meaning="to sentence to, to punish with",
            characters=[("處", "처", "to deal with, a place — as in 처벌, "
                                    "처리")],
            notes=["사형에 처하다 “to put to death”."],
            surfaces=["처한다"],
        ),
        "곡식": dict(
            hanja="穀食", meaning="grain",
            characters=[("穀", "곡", "grain — as in 곡물, 잡곡"),
                        ("食", "식", "food — as in 음식, 식사")],
        ),
        "갚다": dict(meaning="to repay", surfaces=["갚는다"]),
        "도둑질하다": dict(
            meaning="to steal",
            notes=["도둑 “a thief” + -질, the doing of it."],
            surfaces=["도둑질한"],
        ),
        "도둑맞다": dict(meaning="to be robbed, to have stolen",
                       surfaces=["도둑맞은"]),
        "삼다": dict(
            meaning="to make (someone) into, to take as",
            notes=["노비로 삼다 “to make a servant of”."],
            surfaces=["삼는데"],
        ),
        "죄": dict(
            hanja="罪", meaning="a crime, an offence",
            characters=[("罪", "죄", "a crime — as in 범죄, 무죄")],
        ),
        "용서": dict(
            hanja="容恕", meaning="forgiveness, pardon",
            characters=[("容", "용", "to admit, to hold — as in 내용, 허용"),
                        ("恕", "서", "to forgive")],
        ),
        "전": dict(
            hanja="錢", meaning="전, an old unit of money",
            characters=[("錢", "전", "money, a coin — as in 동전, 금전")],
        ),
        "마니산": dict(
            hanja="摩尼山", meaning="Mani-san, a mountain on Ganghwa-do",
            characters=[("摩尼", None, "마니, a Buddhist word for a jewel"),
                        ("山", "산", "a mountain")],
        ),
        "참성단": dict(
            hanja="塹星壇", meaning="참성단, the altar on Mani-san",
            characters=[("塹", "참", "a moat, a trench"),
                        ("星", "성", "a star"),
                        ("壇", "단", "an altar, a platform — as in 제단, "
                                    "강단")],
        ),
        "제사": dict(
            hanja="祭祀", meaning="a sacrificial rite",
            characters=[("祭", "제", "a rite — as in 축제"),
                        ("祀", "사", "to sacrifice")],
            notes=["제사를 지내다 “to hold the rite”."],
        ),
        "기록": dict(
            hanja="記錄", meaning="a record",
            characters=[("記", "기", "to write down — as in 기억, 일기"),
                        ("錄", "록", "to record — as in 등록, 녹음")],
        ),
        "바탕": dict(
            meaning="a basis, a foundation",
            notes=["…을 바탕으로 “on the basis of …”."],
        ),
        "개천절": dict(
            hanja="開天節", meaning="개천절, National Foundation Day "
                                   "(3 October)",
            characters=[("開", "개", "to open — as in 개방, 공개"),
                        ("天", "천", "heaven — as in 천국, 천재"),
                        ("節", "절", "a festival day — as in 광복절, 명절")],
        ),
        "국경일": dict(
            hanja="國慶日", meaning="a national holiday",
            characters=[("國", "국", "a country"),
                        ("慶", "경", "a happy occasion — as in 경사, 경축"),
                        ("日", "일", "a day")],
            notes=["Chapter 1 lists the five 국경일."],
        ),
        "전국체전": dict(
            hanja="全國體典", meaning="the National Sports Festival",
            characters=[("全", "전", "whole — as in 전체, 안전"),
                        ("國", "국", "a country"),
                        ("體", "체", "the body — as in 체육"),
                        ("典", "전", "a ceremony — as in 제전, 사전")],
            notes=["Short for 전국체육대회."],
        ),
        "성화": dict(
            hanja="聖火", meaning="the sacred torch (of a games)",
            characters=[("聖", "성", "holy — as in 성당, 성경"),
                        ("火", "화", "fire — as in 화재, 화요일")],
        ),
        "환인": dict(
            hanja="桓因", meaning="환인, the lord of heaven, 환웅’s father",
            characters=[("桓", "환", "a name character — the same 桓 as in "
                                    "환웅"),
                        ("因", "인", "a cause — as in 원인")],
        ),
        "굽어보다": dict(meaning="to look down on (from above)",
                       surfaces=["굽어보며"]),
        "마침내": dict(meaning="at last, finally"),
        "맡다": dict(meaning="to take charge of", surfaces=["맡은"]),
        "태백산": dict(
            hanja="太白山", meaning="Taebaek-san",
            characters=[("太", "태", "great — as in 태양, 태극기"),
                        ("白", "백", "white"),
                        ("山", "산", "a mountain")],
        ),
        "널리": dict(meaning="widely"),
        "이롭다": dict(
            hanja="利롭다", meaning="to be of benefit",
            characters=[("利", "이", "benefit — as in 이익, 편리")],
            surfaces=["이롭게"],
        ),
        "홍익인간": dict(
            hanja="弘益人間", meaning="“to benefit humankind widely”",
            characters=[("弘", "홍", "wide, great"),
                        ("益", "익", "benefit — as in 이익, 권익"),
                        ("人", "인", "a person"),
                        ("間", "간", "between — 人間 is humankind")],
            notes=["The founding ideal of 고조선, and the stated ideal of "
                   "Korean education today."],
        ),
        "펼치다": dict(meaning="to spread, to unfold", surfaces=["펼치며"]),
        "동굴": dict(
            hanja="洞窟", meaning="a cave",
            characters=[("洞", "동", "a hollow, a village — as in 동네"),
                        ("窟", "굴", "a cave, a hole")],
        ),
        "견디다": dict(meaning="to bear, to endure",
                      surfaces=["견디지", "견뎌"]),
        "도중": dict(
            hanja="途中", meaning="part-way, in the middle of",
            characters=[("途", "도", "a road — as in 용도"),
                        ("中", "중", "the middle")],
        ),
        "도망치다": dict(
            hanja="逃亡치다", meaning="to run away",
            characters=[("逃", "도", "to flee — as in 도피"),
                        ("亡", "망", "to flee, to perish — as in 망하다")],
            surfaces=["도망치고"],
        ),
        "변하다": dict(
            hanja="變하다", meaning="to change, to turn into",
            characters=[("變", "변", "to change — as in 변화, 변경")],
            surfaces=["변하여"],
        ),
        "무럭무럭": dict(
            meaning="(growing) fast and strong",
            notes=["A mimetic word used of children and plants: 무럭무럭 "
                   "자라다."],
        ),
        "신화": dict(
            hanja="神話", meaning="a myth",
            characters=[("神", "신", "a god — as in 정신, 신"),
                        ("話", "화", "a story, talk — as in 대화, 전화")],
        ),
        "차이점": dict(
            hanja="差異點", meaning="a point of difference",
            characters=[("差", "차", "a difference — as in 차별, 격차"),
                        ("異", "이", "different — as in 이상, 특이"),
                        ("點", "점", "a point — as in 장점, 공통점")],
        ),
        "공통점": dict(
            hanja="共通點", meaning="something in common",
            characters=[("共", "공", "together — as in 공동, 공공"),
                        ("通", "통", "to pass through — as in 교통, 소통"),
                        ("點", "점", "a point — as in 차이점")],
        ),
    },

    extraNotes=[
        "The photographs of the daggers and the dolmen on p. 200, the map "
        "on p. 202 and the photograph of 참성단 are not reproduced; the "
        "map’s caption and legend are.",
        "The chronology on p. 201 is three lists side by side, not a table "
        "of rows. It is set here as a table with each entry on the line it "
        "is printed on, so a row is the three columns read across at one "
        "height and an empty cell is a gap in that column. An entry the "
        "book breaks over two lines — 중국 문명, 인도 문명 시작 and 3·1 "
        "운동, 대한민국 임시 정부 수립 — is one cell.",
        "The two shaded passages on p. 202 — the 삼국유사 story and the "
        "three surviving provisions of the 8조법 — are set as a quotation "
        "and a numbered list.",
        "The review gaps on p. 203 are blank in the book and left blank "
        "here.",
    ],
)
