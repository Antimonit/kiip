# -*- coding: utf-8 -*-
"""Chapter 44 — Korea's cultural heritage.

Transcribed from the photos of pp. 224-227. The pages carry no handwriting.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, FIGURE, LABELS, TABLE,
               CELL, GLOSSARY)

CHAPTER = dict(
    number=44, slug="44-cultural-heritage",
    unit="역사", title="한국의 문화유산", titleEn="Korea’s cultural heritage",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 {절}에서 {참선하는|참선하다} 모습과 가정에서 {제사} 지내는 모습입니다.",
                  "Below are people sitting in meditation at a temple and a "
                  "family holding an ancestral rite at home."),
        FIGURE("절에서 스님과 세 사람이 방석에 앉아 참선하는 그림"),
        HEADING(4, "01 각 그림은 무엇을 하는 모습입니까? 각각 어느 {종교}와 관련이 있을까요?",
                translation="What is being done in each picture? Which "
                            "religion does each have to do with?"),
        FIGURE("가정에서 두 사람이 제사상을 차리는 그림"),
        HEADING(4, "02 그림 속의 모습과 같은 것을 해 보았거나 본 적이 있습니까? 어떤 느낌이 들었습니까?",
                translation="Have you ever done, or seen, anything like what "
                            "is in the pictures? How did it feel?"),

        SECTION("goals", "학습목표"),
        BULLET("한국의 {불교}와 {유교} 관련 {문화유산}을 설명할 수 있다.", ordered=True,
               translation="Explain Korea’s cultural heritage connected with "
                           "Buddhism and Confucianism."),
        BULLET("한국 {과학기술}을 알 수 있는 문화유산을 설명할 수 있다.", ordered=True,
               translation="Explain the cultural heritage that shows Korea’s "
                           "science and technology."),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"],
              [["기본", "문화", "15. 의례", "결혼식, 성년식, 제사"]]),

        SECTION("part", "01 불교와 유교 관련 문화유산에는 어떤 것들이 있을까?"),
        HEADING(2, "불교 문화가 꽃피다", translation=
                "Buddhist culture comes into flower" "\n\n"
                "The three countries of 고구려, 백제 and 신라 developed while "
                "competing and co-operating with one another and exchanging "
                "with China, Japan and others. Buddhism in particular, which "
                "came into Korea in the Three Kingdoms period, went beyond "
                "religion and influenced many parts of culture: learning, "
                "music, crafts, architecture and so on. The cultural heritage "
                "connected with Buddhism includes pagodas, temples and "
                "statues of the Buddha. Buddhism flourished greatly not only "
                "in 통일 신라 and 발해, of course, but in the 고려 period too."),
        PARAGRAPH("고구려, 백제, 신라 세 나라는 서로 {경쟁하고|경쟁하다} {협력하는|협력하다} 가운데 중국, "
                  "일본 등과 {교류하면서|교류하다} 발전하였다. 특히 {삼국 시대}에 한국에 들어온 불교는 "
                  "종교를 {넘어서서|넘어서다} {학문}과 음악, {공예}, {건축} 등 여러 문화에 {영향}을 "
                  "주었다. 불교 관련 문화유산에는 {탑}, 절, {불상} 등이 있다. 불교는 {통일 신라}와 "
                  "{발해}는 {물론} 고려 시대에도 크게 {발달하였다|발달하다}."),
        FIGURE("통일 신라의 불국사 (경상북도 경주)"),
        FIGURE("고구려의 금동 연가 7년명 여래 입상 (국립 중앙 박물관)"),
        FIGURE("백제의 부여 정림사지 5층 석탑 (충청남도 부여)"),
        FIGURE("신라의 경주 분황사 모전석탑 (경상북도 경주)"),
        FIGURE("발해의 영광탑 (중국 지린성)"),
        FIGURE("고려의 부석사 무량수전 (경상북도 영주)"),

        HEADING(2, "유교 문화가 발전하다", translation=
                "Confucian culture develops" "\n\n"
                "In the 조선 period an effort was made to build a country in "
                "which social order and good manners stood upright, with "
                "Confucianism at the centre. Among the ideas of Confucianism, "
                "삼강오륜 and 관혼상제 (the coming-of-age ceremony, marriage, "
                "death and ancestral rites) in particular were held to be "
                "very important. 삼강오륜 was taught so that the people would "
                "be loyal to the country, respect their parents and elders, "
                "and keep to what is right between men and women; and they "
                "were made to follow Confucian etiquette when holding a "
                "coming-of-age ceremony, a wedding, a funeral or an ancestral "
                "rite."),
        GLOSSARY(("예법", "예의로 지켜야 할 규범", "예법",
                  dict(en="the norms to be kept as a matter of courtesy"))),
        PARAGRAPH("조선 시대에는 유교를 중심으로 사회 {질서}와 {예절}이 {바로 선|바로 서다} 나라를 만들기 "
                  "위해서 노력하였다. 유교의 {이념} 중에서도 특히 {삼강오륜}과 {관혼상제}({성인식}, "
                  "결혼, 죽음, 제사)가 매우 중요하게 {여겨졌다|여겨지다}. 삼강오륜을 가르쳐 {백성}은 "
                  "나라에 {충성하고|충성하다}, 부모와 {웃어른}을 {공경하며|공경하다}, 남녀 간에 {도리}를 "
                  "지키게 하였고, 성인식, 결혼식, {장례식}, 제사를 지낼 때 유교의 {예법}을 "
                  "{따르게|따르다} 하였다."),
        FIGURE("『삼강행실도』 — 조선 시대에 한국과 중국의 충신, 효자 등의 이야기를 모아 놓은 책"),
        FIGURE("성균관 — 조선 시대 유교(유학)를 가르치던 최고의 교육 기관"),

        SECTION("part", "02 과학기술을 알 수 있는 문화유산에는 어떤 것들이 있을까?"),
        HEADING(2, "삼국 시대와 고려 시대의 과학기술", translation=
                "Science and technology in the Three Kingdoms and 고려 "
                "periods" "\n\n"
                "In the Three Kingdoms period astronomy developed, to obtain "
                "the information farming needed and to tie the king’s "
                "authority to the heavens. As an instrument for observing the "
                "heavenly bodies (the sun, the moon, the stars), 신라’s 첨성대 "
                "is the famous example. In 통일 신라, too, woodblock printing "
                "developed, in which letters are carved into wood and printed "
                "on to paper." "\n\n"
                "The 팔만대장경판 made in the 고려 period are woodblocks made "
                "for printing the Buddhist scriptures. Not only are the "
                "letters even and beautiful in shape; their scale, running to "
                "no fewer than 81,352 blocks, and the skill with which they "
                "have been preserved are recognised as of world standing too. "
                "In the 고려 period weapons using gunpowder were also "
                "developed for the first time, through 최무선."),
        GLOSSARY(("관측", "관찰하고 측정함", "관측",
                  dict(en="observing and measuring"))),
        PARAGRAPH("삼국 시대에는 {농업}에 필요한 정보를 얻고 왕의 {권위}를 하늘과 연결하기 위해 {천문학}이 "
                  "발달하였다. 대표적인 {천체}(태양, 달, 별) {관측} {기구}로는 신라의 {첨성대}가 "
                  "유명하다. 또한 통일 신라에서는 나무에 글자를 {새겨|새기다} 종이로 {찍어 내는|찍어 내다} "
                  "{목판 인쇄술}이 발달하였다."),
        PARAGRAPH("고려 시대에 만든 {팔만대장경판}은 {불경}을 {인쇄하기|인쇄하다} 위해 만든 {목판}이다. "
                  "글자의 모양이 {고르고|고르다} 아름다울 뿐만 아니라 {무려} 8만 1352판에 "
                  "{이르는|이르다} {규모}와 {보존} 기술도 세계적인 것으로 {인정받고|인정받다} 있다. 고려 "
                  "시대에는 {최무선}을 통해 처음으로 {화약}을 사용한 {무기}도 "
                  "{개발되었다|개발되다}."),
        FIGURE("첨성대(경상북도 경주) — 현재까지 남아 있는 동양에서 가장 오래된 천문대"),
        FIGURE("무구정광대다라니경(불교 중앙 박물관) — 8세기 중반에 만든 것으로, 신라의 발달된 목판 "
               "인쇄술과 종이 만드는 기술을 보여 준다."),
        FIGURE("팔만대장경판 — 몽골의 침입을 부처님의 힘으로 물리치기 위해 만든 것으로, 유네스코 세계 "
               "기록유산의 하나이다."),

        HEADING(2, "조선 시대의 과학기술", translation=
                "Science and technology in the 조선 period" "\n\n"
                "In the 조선 period science and technology were thought very "
                "important, with the aim of building a rich and strong "
                "country and helping the people in their lives. In 세종’s time "
                "in particular many scientific instruments were made, such as "
                "the 앙부일구 (a sundial), the 자격루 (a water clock) and the "
                "혼천의 (an instrument for observing the heavenly bodies). The "
                "측우기, the world’s first instrument for measuring rainfall, "
                "was invented too, and was used to measure the amount of rain "
                "that fell in each region. With the invention of scientific "
                "instruments like these, people came to know accurately in "
                "everyday life not only the time but also the 절기 (the year "
                "divided into twenty-four to mark off the seasons) and the "
                "seasons. This was a great help in farming as well." "\n\n"
                "Meanwhile, in the later 조선 period 수원 화성 was built using "
                "the building techniques of East and West, and the use of the "
                "거중기 at that time made it possible to cut the construction "
                "period by a great deal."),
        PARAGRAPH("조선 시대에는 {부유하고|부유하다} 강한 나라를 만들고 백성의 생활에 도움을 주기 위한 "
                  "{목적}에서 과학기술을 매우 중요하게 생각하였다. 특히 {세종} 때 {앙부일구}({해시계}), "
                  "{자격루}({물시계}), {혼천의}(천체 관측 기구) 등과 같은 과학 기구가 많이 만들어졌다. "
                  "그리고 세계 {최초}의 {강우량} {측정} 기구인 {측우기}도 {발명되어|발명되다} 각 지역에서 "
                  "내린 비의 양을 {재는|재다} 데 사용되었다. 이와 같은 과학 기구의 {발명}으로 "
                  "{일상생활}에서 {시각}은 물론 {절기}(계절을 {구분하려고|구분하다} 한 해를 스물넷으로 나눈 "
                  "것)와 계절을 정확히 알 수 있게 되었다. 이는 {농사짓는|농사짓다} 데에도 큰 도움이 "
                  "되었다."),
        PARAGRAPH("한편, 조선 {후기}에는 {동서양}의 건축 기술을 사용하여 {수원 화성}을 "
                  "{건립하였는데|건립하다}, 이때 {거중기}를 사용해 {공사} 기간을 {훨씬} {줄일|줄이다} 수 "
                  "있었다."),
        FIGURE("측우기 — 원통형의 그릇에 빗물을 받아 강우량을 측정하는 기구로 세계 최초로 제작되었다."),
        FIGURE("앙부일구 — 눈금의 기울기와 가로, 세로 눈금의 간격을 보면 태양의 움직임을 알 수 있다."),
        FIGURE("자격루 — 물의 흐름을 이용하여 종, 북, 징을 쳐서 자동으로 시간을 알려 주었다."),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 불교와 유교 관련 문화유산에는 어떤 것들이 있을까?"),
        BULLET("삼국 시대에 들어온 (        )는 종교는 물론 학문과 음악, 공예, 건축 등 여러 문화에 영향을 "
               "주었다. 특히 탑, 절, 불상 등이 많이 만들어졌다."),
        BULLET("(        )에서 삼강오륜을 통해 백성은 나라에 충성하고, 부모와 웃어른을 공경하며, 남녀 간에 "
               "도리를 지켜야 한다고 가르쳤다."),
        HEADING(3, "02 과학기술을 알 수 있는 문화유산에는 어떤 것들이 있을까?"),
        BULLET("통일 신라와 고려 시대에는 나무에 글자를 새겨 종이로 찍어내는 목판 인쇄술이 발달하였다. "
               "신라의 무구정광대다라니경과 고려의 (                )이 대표적인 문화유산이다."),
        BULLET("조선 시대 (        ) 때에는 앙부일구, 자격루, 측우기 등과 같은 과학 기구가 많이 "
               "만들어졌다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "[한국의 유네스코 세계유산에는 어떤 것들이 있을까?]", translation=
                "What are Korea’s UNESCO World Heritage sites?" "\n\n"
                "The UNESCO World Heritage Committee is a body belonging to "
                "the United Nations (UN), set up to protect the world’s "
                "cultural heritage and natural heritage. It designates "
                "important cultural properties all over the world as World "
                "Heritage, and preserves and studies them. In 2019 Korea’s "
                "서원 were chosen as UNESCO World Heritage. A 서원 was a "
                "building put up in the 조선 period, a place where students "
                "were taught Confucian learning and rites were held for "
                "outstanding Confucian scholars. In 2022 the 삼국유사, a "
                "history of the Three Kingdoms period compiled in the 고려 "
                "period, and in 2023 the records connected with the 동학 "
                "Peasant Revolution, were also chosen as UNESCO Memory of the "
                "World, the latter recognised for their importance in world "
                "history, in that the people of 조선 took the lead and strove "
                "towards the universal values of freedom, equality and human "
                "rights. As of 2024 Korea has 16 UNESCO World Heritage sites "
                "and 18 entries in the Memory of the World."),
        PARAGRAPH("유네스코 {세계유산} 위원회는 {국제 연합}(UN)에 {속해|속하다} 있는 {기구|기구(機構)}로, "
                  "세계의 문화유산 및 {자연 유산}을 보호하기 위해 만든 것이다. 이 기구는 세계 {곳곳}의 "
                  "중요한 {문화재}를 세계 유산으로 정하여 {보존하고|보존하다} 연구한다. 2019년에는 한국의 "
                  "{서원}이 유네스코 세계유산에 {선정}이 되었다. 서원은 조선 시대에 만들어진 건물로, "
                  "학생들에게 {유학}을 가르치고 {뛰어난|뛰어나다} {유학자}들에게 제사를 지내는 곳이었다. "
                  "2022년에는 고려시대에 {편찬된|편찬되다} 삼국시대 {역사서}인 {삼국유사}, 2023년에는 "
                  "{동학농민혁명}과 관련한 {기록물}이 조선 백성들이 {주체}가 되어 자유, 평등, 인권의 "
                  "{보편적} {가치}를 {지향하기|지향하다} 위해 노력했던 {세계사적} {중요성}을 "
                  "{인정받아|인정받다} 유네스코 {세계기록유산}에 {선정되기도|선정되다} 하였다. 2024년 현재 "
                  "한국은 유네스코 세계유산 16개, 세계기록유산 18개를 가지고 있다."),
        FIGURE("2019년에 유네스코 세계유산에 등재된 서원 9곳 중 병산서원과 필암서원의 모습 — 서원의 위치를 "
               "표시한 지도와 사진 두 장"),
        LABELS("영주 소수서원", "안동 도산서원", "병산서원 경북 안동", "논산 돈암서원", "정읍 무성서원",
               "함양 남계서원", "달성 도동서원", "경주 옥산서원", "필암서원 전남 장성"),
        PARAGRAPH("★ 자신의 고향 나라에서 유네스코 세계유산이나 세계기록유산에 등재된 것이 있다면 소개하는 "
                  "시간을 가져 봅시다. 만약 없거나 잘 모른다면 추천하고 싶은 문화유산을 소개해 봅시다.",
                  "If anything in your home country is inscribed as UNESCO "
                  "World Heritage or in the Memory of the World, take some "
                  "time to introduce it. If there is nothing, or you are not "
                  "sure, introduce a piece of cultural heritage you would "
                  "like to recommend."),
    ],

    extraAnnotations={
        "절": dict(
            meaning="a Buddhist temple",
            notes=["The native word; 사 (寺) is the Sino-Korean one that "
                   "closes temple names, as in 불국사, 부석사."],
        ),
        "참선하다": dict(
            hanja="參禪하다", meaning="to practise Seon (Zen) meditation",
            characters=[("參", "참", "to take part — as in 참여, 참가"),
                        ("禪", "선", "Seon, Zen, meditation")],
            surfaces=["참선하는"],
        ),
        "제사": dict(
            hanja="祭祀", meaning="an ancestral rite",
            characters=[("祭", "제", "a rite, an offering — as in 축제, 관혼상제"),
                        ("祀", "사", "to offer to the spirits")],
            notes=["제사를 지내다 “to hold an ancestral rite”. Chapter 15 "
                   "sets the rite out."],
        ),
        "종교": dict(
            hanja="宗敎", meaning="religion",
            characters=[("宗", "종", "the ancestral line, the principal — as in 세종"),
                        ("敎", "교", "to teach, a teaching — as in 불교, 유교")],
        ),
        "불교": dict(
            hanja="佛敎", meaning="Buddhism",
            characters=[("佛", "불", "the Buddha — as in 불상, 불경"),
                        ("敎", "교", "a teaching — as in 종교, 유교")],
        ),
        "유교": dict(
            hanja="儒敎", meaning="Confucianism",
            characters=[("儒", "유", "a scholar, Confucian — as in 유학, 유학자"),
                        ("敎", "교", "a teaching — as in 종교, 불교")],
        ),
        "문화유산": dict(
            hanja="文化遺産", meaning="cultural heritage",
            characters=[("文化", None, "culture — 文 writing, 化 to become"),
                        ("遺産", None, "an inheritance, a legacy — 遺 to "
                                       "leave behind, 産 property")],
        ),
        "과학기술": dict(
            hanja="科學技術", meaning="science and technology",
            characters=[("科學", None, "science — 科 a branch, 學 learning"),
                        ("技術", None, "technology, skill — 技 a skill, "
                                       "術 an art")],
        ),
        "경쟁하다": dict(
            hanja="競爭하다", meaning="to compete",
            characters=[("競", "경", "to vie — as in 경기"),
                        ("爭", "쟁", "to contend — as in 전쟁, 분쟁")],
            surfaces=["경쟁하고"],
        ),
        "협력하다": dict(
            hanja="協力하다", meaning="to co-operate",
            characters=[("協", "협", "to join in — as in 협상, 협의"),
                        ("力", "력", "strength — as in 노력, 능력")],
            surfaces=["협력하는"],
        ),
        "교류하다": dict(
            hanja="交流하다", meaning="to exchange, to have dealings with",
            characters=[("交", "교", "to mix, to exchange — as in 교통, 외교"),
                        ("流", "류", "to flow — as in 유행, 한류")],
            surfaces=["교류하면서"],
        ),
        "삼국 시대": dict(
            hanja="三國時代", meaning="the Three Kingdoms period",
            characters=[("三", "삼", "three"),
                        ("國", "국", "a country — as in 한국, 국가"),
                        ("時代", None, "a period, an age — 時 time, "
                                       "代 a generation")],
            notes=["The age of 고구려, 백제 and 신라."],
        ),
        "넘어서다": dict(
            meaning="to go beyond, to get past",
            notes=["종교를 넘어서서 “going beyond religion”."],
            surfaces=["넘어서서"],
        ),
        "학문": dict(
            hanja="學問", meaning="learning, scholarship",
            characters=[("學", "학", "to learn — as in 학교, 과학"),
                        ("問", "문", "to ask — as in 질문, 문의")],
        ),
        "공예": dict(
            hanja="工藝", meaning="crafts, craftwork",
            characters=[("工", "공", "work, making — as in 공사, 공장"),
                        ("藝", "예", "an art — as in 예술")],
        ),
        "건축": dict(
            hanja="建築", meaning="architecture, building",
            characters=[("建", "건", "to build — as in 건립, 건물"),
                        ("築", "축", "to construct")],
        ),
        "영향": dict(
            hanja="影響", meaning="influence",
            characters=[("影", "영", "a shadow"),
                        ("響", "향", "an echo")],
            notes=["영향을 주다 “to influence”."],
        ),
        "탑": dict(
            hanja="塔", meaning="a pagoda, a tower",
            characters=[("塔", "탑", "a pagoda — as in 석탑")],
        ),
        "불상": dict(
            hanja="佛像", meaning="a statue of the Buddha",
            characters=[("佛", "불", "the Buddha — as in 불교, 불경"),
                        ("像", "상", "an image, a statue — as in 입상, 영상")],
        ),
        "통일 신라": dict(
            hanja="統一新羅", meaning="Unified Silla",
            characters=[("統一", None, "unification — 統 to gather into "
                                       "one, 一 one"),
                        ("新羅", None, "Silla")],
        ),
        "발해": dict(
            hanja="渤海", meaning="Balhae (698–926)",
            notes=["The kingdom north of 통일 신라; its 영광탑 stands in what "
                   "is now Jilin, China."],
        ),
        "물론": dict(
            hanja="勿論", meaning="of course; not only … (but)",
            characters=[("勿", "물", "do not"),
                        ("論", "론", "to discuss — as in 토론, 여론")],
            notes=["A는 물론 B도 “not only A, of course, but B too”."],
        ),
        "발달하다": dict(
            hanja="發達하다", meaning="to develop, to flourish",
            characters=[("發", "발", "to send out — as in 발명, 개발"),
                        ("達", "달", "to reach — as in 전달, 배달")],
            surfaces=["발달하였다"],
        ),
        "질서": dict(
            hanja="秩序", meaning="order",
            characters=[("秩", "질", "order, rank"),
                        ("序", "서", "sequence — as in 순서")],
        ),
        "예절": dict(
            hanja="禮節", meaning="manners, etiquette",
            characters=[("禮", "예", "courtesy, rites — as in 예법, 장례"),
                        ("節", "절", "a joint, moderation — as in 절기, 계절")],
        ),
        "바로 서다": dict(
            meaning="to stand upright, to be set right",
            notes=["질서와 예절이 바로 선 나라 “a country where order and "
                   "manners stand firm”."],
            surfaces=["바로 선"],
        ),
        "이념": dict(
            hanja="理念", meaning="an idea, an ideology",
            characters=[("理", "이", "reason, principle — as in 도리, 이유"),
                        ("念", "념", "a thought — as in 기념, 개념")],
        ),
        "삼강오륜": dict(
            hanja="三綱五倫",
            meaning="the three bonds and five relationships of Confucianism",
            characters=[("三", "삼", "three"),
                        ("綱", "강", "a guiding rope, a bond"),
                        ("五", "오", "five"),
                        ("倫", "륜", "human relationships — as in 윤리")],
            notes=["The three bonds are ruler and subject, parent and child, "
                   "husband and wife."],
        ),
        "관혼상제": dict(
            hanja="冠婚喪祭",
            meaning="the four rites: coming of age, marriage, funeral and "
                    "ancestral rites",
            characters=[("冠", "관", "a cap — the coming-of-age capping"),
                        ("婚", "혼", "marriage — as in 결혼"),
                        ("喪", "상", "mourning — as in 상주"),
                        ("祭", "제", "a rite — as in 제사")],
        ),
        "성인식": dict(
            hanja="成人式", meaning="a coming-of-age ceremony",
            characters=[("成", "성", "to become, to complete — as in 성년, 성공"),
                        ("人", "인", "a person"),
                        ("式", "식", "a ceremony — as in 결혼식, 장례식")],
        ),
        "여겨지다": dict(
            meaning="to be regarded as",
            notes=["The passive of 여기다 “to regard, to consider”."],
            surfaces=["여겨졌다"],
        ),
        "백성": dict(
            hanja="百姓", meaning="the common people (of a kingdom)",
            characters=[("百", "백", "a hundred"),
                        ("姓", "성", "a surname — as in 성씨")],
        ),
        "충성하다": dict(
            hanja="忠誠하다", meaning="to be loyal",
            characters=[("忠", "충", "loyalty — as in 충신"),
                        ("誠", "성", "sincerity — as in 정성, 성실")],
            surfaces=["충성하고"],
        ),
        "웃어른": dict(
            meaning="one’s elders",
            notes=["웃- “upper” and 어른 “an adult, an elder”."],
        ),
        "공경하다": dict(
            hanja="恭敬하다", meaning="to respect, to revere",
            characters=[("恭", "공", "respectful"),
                        ("敬", "경", "to respect — as in 존경, 경로")],
            surfaces=["공경하며"],
        ),
        "도리": dict(
            hanja="道理", meaning="what is right, one’s duty",
            characters=[("道", "도", "a way — as in 도로, 도덕"),
                        ("理", "리", "reason, principle — as in 이념, 이유")],
            notes=["도리를 지키다 “to keep to what is right”."],
        ),
        "장례식": dict(
            hanja="葬禮式", meaning="a funeral",
            characters=[("葬", "장", "to bury — as in 화장, 매장"),
                        ("禮", "례", "rites — as in 예절, 예법"),
                        ("式", "식", "a ceremony — as in 성인식, 결혼식")],
        ),
        "예법": dict(
            hanja="禮法", meaning="etiquette, the rules of propriety",
            characters=[("禮", "예", "courtesy, rites — as in 예절, 장례"),
                        ("法", "법", "law, a rule — as in 방법, 법률")],
        ),
        "따르다": dict(
            meaning="to follow, to observe",
            surfaces=["따르게"],
        ),
        "농업": dict(
            hanja="農業", meaning="agriculture, farming",
            characters=[("農", "농", "farming — as in 농사, 농민"),
                        ("業", "업", "work, an industry — as in 산업, 직업")],
        ),
        "권위": dict(
            hanja="權威", meaning="authority",
            characters=[("權", "권", "power, a right — as in 권리, 인권"),
                        ("威", "위", "majesty, might — as in 위협")],
        ),
        "천문학": dict(
            hanja="天文學", meaning="astronomy",
            characters=[("天", "천", "the heavens — as in 천체, 혼천의"),
                        ("文", "문", "patterns, writing — as in 문화"),
                        ("學", "학", "learning — as in 과학, 학문")],
        ),
        "천체": dict(
            hanja="天體", meaning="a heavenly body",
            characters=[("天", "천", "the heavens — as in 천문학"),
                        ("體", "체", "a body — as in 신체, 주체")],
        ),
        "관측": dict(
            hanja="觀測", meaning="observation (and measurement)",
            characters=[("觀", "관", "to look at — as in 관찰, 관광"),
                        ("測", "측", "to measure — as in 측정, 측우기")],
        ),
        "기구": dict(
            hanja="器具", meaning="an instrument, an implement",
            characters=[("器", "기", "a vessel, a device — as in 측우기, 무기"),
                        ("具", "구", "a tool — as in 도구, 가구")],
            notes=["The 기구 of 국제 연합 on p. 227 is another word, 機構 “a "
                   "body”."],
        ),
        "첨성대": dict(
            hanja="瞻星臺", meaning="Cheomseongdae, the observatory at 경주",
            characters=[("瞻", "첨", "to look up at"),
                        ("星", "성", "a star"),
                        ("臺", "대", "a platform, a tower — as in 천문대")],
        ),
        "새기다": dict(
            meaning="to carve, to engrave",
            surfaces=["새겨"],
        ),
        "찍어 내다": dict(
            meaning="to print off, to stamp out",
            notes=["찍다 “to stamp, to print” with 내다 “to turn out”. The "
                   "review on p. 227 prints it closed up, 찍어내는."],
            surfaces=["찍어 내는"],
        ),
        "목판 인쇄술": dict(
            hanja="木版印刷術", meaning="woodblock printing",
            characters=[("木版", None, "a woodblock — 木 wood, 版 a "
                                       "printing block"),
                        ("印刷", None, "printing — 印 to stamp, 刷 to brush"),
                        ("術", "술", "an art, a technique — as in 기술")],
        ),
        "팔만대장경판": dict(
            hanja="八萬大藏經板",
            meaning="the woodblocks of the Tripitaka Koreana",
            characters=[("八萬", None, "eighty thousand"),
                        ("大藏經", None, "the complete Buddhist canon — 大 "
                                         "great, 藏 a store, 經 scripture"),
                        ("板", "판", "a board, a block")],
            notes=["Kept at 해인사."],
        ),
        "불경": dict(
            hanja="佛經", meaning="the Buddhist scriptures",
            characters=[("佛", "불", "the Buddha — as in 불교, 불상"),
                        ("經", "경", "scripture — as in 성경")],
        ),
        "인쇄하다": dict(
            hanja="印刷하다", meaning="to print",
            characters=[("印", "인", "a seal, to stamp — as in 인감, 인상"),
                        ("刷", "쇄", "to brush, to print")],
            surfaces=["인쇄하기"],
        ),
        "목판": dict(
            hanja="木版", meaning="a woodblock (for printing)",
            characters=[("木", "목", "wood — as in 목재"),
                        ("版", "판", "a printing block — as in 출판")],
        ),
        "고르다": dict(
            meaning="to be even, regular",
            notes=["The adjective; 고르다 “to choose” is a different word."],
            surfaces=["고르고"],
        ),
        "무려": dict(
            hanja="無慮", meaning="as many as, no fewer than",
            characters=[("無", "무", "without — as in 무료, 무효"),
                        ("慮", "려", "to consider — as in 고려, 배려")],
        ),
        "이르다": dict(
            meaning="to reach, to amount to",
            notes=["8만 1352판에 이르는 “running to 81,352 blocks”."],
            surfaces=["이르는"],
        ),
        "규모": dict(
            hanja="規模", meaning="scale, size",
            characters=[("規", "규", "a rule — as in 규칙, 규범"),
                        ("模", "모", "a pattern — as in 모양, 모범")],
        ),
        "보존": dict(
            hanja="保存", meaning="preservation",
            characters=[("保", "보", "to keep, to protect — as in 보호, 보장"),
                        ("存", "존", "to exist — as in 존재")],
        ),
        "인정받다": dict(
            hanja="認定받다", meaning="to be recognised",
            characters=[("認", "인", "to recognise — as in 확인, 인증"),
                        ("定", "정", "to settle — as in 결정, 선정")],
            surfaces=["인정받고", "인정받아"],
        ),
        "최무선": dict(
            hanja="崔茂宣", meaning="Choe Museon (1325–1395)",
            notes=["The 고려 official who learnt to make gunpowder and had "
                   "firearms made."],
        ),
        "화약": dict(
            hanja="火藥", meaning="gunpowder",
            characters=[("火", "화", "fire — as in 화재"),
                        ("藥", "약", "a drug, a compound — as in 약국")],
        ),
        "무기": dict(
            hanja="武器", meaning="a weapon",
            characters=[("武", "무", "military — as in 무력"),
                        ("器", "기", "a vessel, a device — as in 기구, 측우기")],
        ),
        "개발되다": dict(
            hanja="開發되다", meaning="to be developed",
            characters=[("開", "개", "to open — as in 개방, 공개"),
                        ("發", "발", "to send out — as in 발명, 발달")],
            surfaces=["개발되었다"],
        ),
        "부유하다": dict(
            hanja="富裕하다", meaning="to be rich, wealthy",
            characters=[("富", "부", "wealth — as in 부자, 풍부"),
                        ("裕", "유", "plentiful — as in 여유")],
            surfaces=["부유하고"],
        ),
        "목적": dict(
            hanja="目的", meaning="a purpose, an aim",
            characters=[("目", "목", "the eye, an item — as in 목표, 과목"),
                        ("的", "적", "a target — as in 보편적")],
        ),
        "세종": dict(
            hanja="世宗", meaning="King Sejong (reigned 1418–1450)",
            characters=[("世", "세", "a generation, the world — as in 세계"),
                        ("宗", "종", "an ancestor — the 宗 of 종교, closing "
                                    "a king’s temple name")],
        ),
        "앙부일구": dict(
            hanja="仰釜日晷",
            meaning="the 앙부일구, a bowl-shaped sundial",
            characters=[("仰", "앙", "to look up"),
                        ("釜", "부", "a cauldron — as in 부산"),
                        ("日", "일", "the sun, a day"),
                        ("晷", "구", "a shadow cast by the sun")],
            notes=["“The upturned-cauldron sundial”."],
        ),
        "해시계": dict(
            hanja="해時計", meaning="a sundial",
            characters=[("時計", None, "a clock — 時 time, 計 to count")],
            notes=["해 “the sun” is the native word."],
        ),
        "자격루": dict(
            hanja="自擊漏",
            meaning="the 자격루, a water clock that strikes by itself",
            characters=[("自", "자", "self — as in 자동, 자유"),
                        ("擊", "격", "to strike — as in 공격"),
                        ("漏", "루", "to drip, a water clock")],
        ),
        "물시계": dict(
            hanja="물時計", meaning="a water clock",
            characters=[("時計", None, "a clock — 時 time, 計 to count")],
        ),
        "혼천의": dict(
            hanja="渾天儀", meaning="the 혼천의, an armillary sphere",
            characters=[("渾", "혼", "whole, round"),
                        ("天", "천", "the heavens — as in 천체, 천문학"),
                        ("儀", "의", "an instrument, a ceremony — as in 의례")],
        ),
        "최초": dict(
            hanja="最初", meaning="the first, the very beginning",
            characters=[("最", "최", "most — as in 최고, 최대"),
                        ("初", "초", "the beginning — as in 초기")],
        ),
        "강우량": dict(
            hanja="降雨量", meaning="rainfall",
            characters=[("降", "강", "to fall, to come down — as in 하강"),
                        ("雨", "우", "rain — as in 측우기"),
                        ("量", "량", "an amount — as in 수량")],
        ),
        "측정": dict(
            hanja="測定", meaning="measurement",
            characters=[("測", "측", "to measure — as in 관측, 측우기"),
                        ("定", "정", "to settle — as in 결정, 선정")],
        ),
        "측우기": dict(
            hanja="測雨器", meaning="the 측우기, a rain gauge",
            characters=[("測", "측", "to measure — as in 측정, 관측"),
                        ("雨", "우", "rain — as in 강우량"),
                        ("器", "기", "a vessel, a device — as in 기구, 무기")],
        ),
        "발명되다": dict(
            hanja="發明되다", meaning="to be invented",
            characters=[("發", "발", "to send out — as in 발달, 개발"),
                        ("明", "명", "bright, clear — as in 설명")],
            surfaces=["발명되어"],
        ),
        "재다": dict(
            meaning="to measure",
            notes=["비의 양을 재다 “to measure the amount of rain”."],
            surfaces=["재는"],
        ),
        "발명": dict(
            hanja="發明", meaning="an invention",
            characters=[("發", "발", "to send out — as in 발달, 개발"),
                        ("明", "명", "bright, clear — as in 설명")],
        ),
        "일상생활": dict(
            hanja="日常生活", meaning="everyday life",
            characters=[("日常", None, "the everyday — 日 a day, 常 usual"),
                        ("生活", None, "life, living — 生 to live, 活 lively")],
        ),
        "시각": dict(
            hanja="時刻", meaning="the time (a point on the clock)",
            characters=[("時", "시", "time — as in 시간, 시계"),
                        ("刻", "각", "to carve, a moment")],
        ),
        "절기": dict(
            hanja="節氣", meaning="the twenty-four solar terms",
            characters=[("節", "절", "a joint, a division — as in 계절, 예절"),
                        ("氣", "기", "air, weather — as in 기후, 공기")],
            notes=["Chapter 16’s 알아두면 좋아요 lists the twenty-four."],
        ),
        "구분하다": dict(
            hanja="區分하다", meaning="to divide, to tell apart",
            characters=[("區", "구", "a district, to divide — as in 구역"),
                        ("分", "분", "to divide — as in 부분, 분류")],
            surfaces=["구분하려고"],
        ),
        "농사짓다": dict(
            hanja="農事짓다", meaning="to farm",
            characters=[("農", "농", "farming — as in 농업, 농민"),
                        ("事", "사", "a matter, work — as in 공사, 행사")],
            surfaces=["농사짓는"],
        ),
        "후기": dict(
            hanja="後期", meaning="the later period",
            characters=[("後", "후", "after — as in 이후, 오후"),
                        ("期", "기", "a period — as in 기간, 초기")],
        ),
        "동서양": dict(
            hanja="東西洋", meaning="East and West",
            characters=[("東", "동", "east — as in 동양"),
                        ("西", "서", "west — as in 서양"),
                        ("洋", "양", "an ocean — as in 동양, 서양")],
        ),
        "수원 화성": dict(
            hanja="水原華城", meaning="Hwaseong Fortress at 수원",
            characters=[("水原", None, "Suwon — 水 water, 原 a plain"),
                        ("華", "화", "splendid — as in 화려"),
                        ("城", "성", "a fortress, a walled town")],
        ),
        "건립하다": dict(
            hanja="建立하다", meaning="to build, to put up",
            characters=[("建", "건", "to build — as in 건축, 건물"),
                        ("立", "립", "to stand, to set up — as in 설립, 독립")],
            surfaces=["건립하였는데"],
        ),
        "거중기": dict(
            hanja="擧重機", meaning="the 거중기, a pulley crane",
            characters=[("擧", "거", "to lift — as in 선거"),
                        ("重", "중", "heavy — as in 중요, 체중"),
                        ("機", "기", "a machine — as in 기계, 비행기")],
        ),
        "공사": dict(
            hanja="工事", meaning="construction work",
            characters=[("工", "공", "work, making — as in 공예, 공장"),
                        ("事", "사", "a matter, work — as in 농사, 행사")],
        ),
        "훨씬": dict(meaning="by far, much (more or less)"),
        "줄이다": dict(
            meaning="to cut down, to shorten",
            notes=["The causative of 줄다 “to shrink”."],
            surfaces=["줄일"],
        ),
        "세계유산": dict(
            hanja="世界遺産", meaning="World Heritage",
            characters=[("世界", None, "the world"),
                        ("遺産", None, "an inheritance, a legacy — 遺 to "
                                       "leave behind, 産 property")],
        ),
        "국제 연합": dict(
            hanja="國際聯合", meaning="the United Nations",
            characters=[("國際", None, "international — 國 a country, 際 "
                                       "between"),
                        ("聯合", None, "a union — 聯 to link, 合 to join")],
        ),
        "속하다": dict(
            hanja="屬하다", meaning="to belong to",
            characters=[("屬", "속", "to belong — as in 소속")],
            surfaces=["속해"],
        ),
        "기구(機構)": dict(
            hanja="機構", meaning="a body, an organisation",
            characters=[("機", "기", "a machine, a mechanism — as in 기관, 거중기"),
                        ("構", "구", "to frame, a structure — as in 구조, 구성")],
            notes=["Not the 기구 (器具) “instrument” of p. 226."],
        ),
        "자연 유산": dict(
            hanja="自然遺産", meaning="natural heritage",
            characters=[("自然", None, "nature — 自 self, 然 so"),
                        ("遺産", None, "an inheritance, a legacy")],
        ),
        "곳곳": dict(meaning="everywhere, place after place"),
        "문화재": dict(
            hanja="文化財", meaning="a cultural property",
            characters=[("文化", None, "culture"),
                        ("財", "재", "property, wealth — as in 재산")],
        ),
        "보존하다": dict(
            hanja="保存하다", meaning="to preserve",
            characters=[("保", "보", "to keep, to protect — as in 보호, 보장"),
                        ("存", "존", "to exist — as in 존재")],
            surfaces=["보존하고"],
        ),
        "서원": dict(
            hanja="書院", meaning="a 서원, a private Confucian academy",
            characters=[("書", "서", "a book, writing — as in 도서관, 역사서"),
                        ("院", "원", "an institution — as in 병원, 법원")],
        ),
        "선정": dict(
            hanja="選定", meaning="selection",
            characters=[("選", "선", "to choose — as in 선거, 선택"),
                        ("定", "정", "to settle — as in 결정, 인정")],
        ),
        "유학": dict(
            hanja="儒學", meaning="Confucian learning",
            characters=[("儒", "유", "a scholar, Confucian — as in 유교"),
                        ("學", "학", "learning — as in 학문, 과학")],
            notes=["Not 유학 (留學) “studying abroad”."],
        ),
        "뛰어나다": dict(
            meaning="to be outstanding",
            surfaces=["뛰어난"],
        ),
        "유학자": dict(
            hanja="儒學者", meaning="a Confucian scholar",
            characters=[("儒學", None, "Confucian learning"),
                        ("者", "자", "a person — as in 학자, 당사자")],
        ),
        "편찬되다": dict(
            hanja="編纂되다", meaning="to be compiled",
            characters=[("編", "편", "to weave, to edit — as in 편집"),
                        ("纂", "찬", "to gather, to compile")],
            surfaces=["편찬된"],
        ),
        "역사서": dict(
            hanja="歷史書", meaning="a history, a book of history",
            characters=[("歷史", None, "history — 歷 to pass through, 史 "
                                       "a chronicle"),
                        ("書", "서", "a book — as in 서원, 도서관")],
        ),
        "삼국유사": dict(
            hanja="三國遺事",
            meaning="the 삼국유사, “Memorabilia of the Three Kingdoms”",
            characters=[("三國", None, "the Three Kingdoms"),
                        ("遺", "유", "to leave behind — as in 유산"),
                        ("事", "사", "matters, events — as in 사건")],
            notes=["Compiled by the monk 일연 in the 고려 period."],
        ),
        "동학농민혁명": dict(
            hanja="東學農民革命",
            meaning="the 동학 Peasant Revolution (1894)",
            characters=[("東學", None, "동학, “Eastern Learning”"),
                        ("農民", None, "peasants, farmers"),
                        ("革命", None, "a revolution — 革 to change, 命 "
                                       "a mandate")],
        ),
        "기록물": dict(
            hanja="記錄物", meaning="records, documents",
            characters=[("記", "기", "to write down — as in 기억, 일기"),
                        ("錄", "록", "to record — as in 등록, 녹음"),
                        ("物", "물", "a thing — as in 건물, 박물관")],
        ),
        "주체": dict(
            hanja="主體", meaning="the main agent, the one who acts",
            characters=[("主", "주", "main, a master — as in 주인, 민주"),
                        ("體", "체", "a body — as in 천체, 단체")],
            notes=["주체가 되다 “to take the lead”."],
        ),
        "보편적": dict(
            hanja="普遍的", meaning="universal",
            characters=[("普", "보", "wide, general — as in 보통"),
                        ("遍", "편", "everywhere"),
                        ("的", "적", "the suffix “-al, -ic” — as in 세계사적")],
        ),
        "가치": dict(
            hanja="價値", meaning="value, worth",
            characters=[("價", "가", "a price — as in 가격, 물가"),
                        ("値", "치", "worth — as in 수치")],
        ),
        "지향하다": dict(
            hanja="志向하다", meaning="to aim at, to strive towards",
            characters=[("志", "지", "the will — as in 의지, 지원"),
                        ("向", "향", "to face towards — as in 방향")],
            surfaces=["지향하기"],
        ),
        "세계사적": dict(
            hanja="世界史的", meaning="of world history, world-historical",
            characters=[("世界", None, "the world"),
                        ("史", "사", "history — as in 역사"),
                        ("的", "적", "the suffix “-al, -ic” — as in 보편적")],
        ),
        "중요성": dict(
            hanja="重要性", meaning="importance",
            characters=[("重", "중", "heavy — as in 거중기, 체중"),
                        ("要", "요", "essential — as in 필요, 주요"),
                        ("性", "성", "a nature, “-ness” — as in 가능성")],
        ),
        "세계기록유산": dict(
            hanja="世界記錄遺産", meaning="UNESCO Memory of the World",
            characters=[("世界", None, "the world"),
                        ("記錄", None, "a record — 記 to write down, 錄 to "
                                       "record"),
                        ("遺産", None, "an inheritance, a legacy")],
            notes=["A caption on p. 226 spaces it 세계 기록유산."],
        ),
        "선정되다": dict(
            hanja="選定되다", meaning="to be chosen, selected",
            characters=[("選", "선", "to choose — as in 선거, 선택"),
                        ("定", "정", "to settle — as in 결정, 측정")],
            surfaces=["선정되기도"],
        ),
    },

    extraNotes=[
        "The photographs on pp. 225-226 are not reproduced; their captions "
        "are. Where a caption has a name in bold and a line of description "
        "under it, the two are joined here with a dash.",
        "The map of the nine 서원 on p. 227 is set as its caption and the "
        "nine names printed on it; the province names on the map (충남, 전북, "
        "전남, 경북, 경남, 제주도) are left out.",
        "The review gaps on p. 227 are blank in the book and left blank here.",
    ],
)
