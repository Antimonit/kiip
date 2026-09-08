# -*- coding: utf-8 -*-
"""Chapter 24 — Elections and local self-government.

Transcribed from the photos of pp. 126-129; there is no Google Doc for it.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, TABLE,
               CELL, GLOSSARY)

CHAPTER = dict(
    number=24, slug="24-elections-and-local-government",
    unit="정치", title="선거와 지방자치",
    titleEn="Elections and local self-government",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 A도시의 지역 사회 문제와 관련된 사진입니다."),
        FIGURE("길가에 쌓인 쓰레기 봉투와 버려진 물건들"),
        HEADING(4, "01 사진 속에 나타난 A도시의 문제는 무엇이고, 누가 해결해야 합니까?"),
        HEADING(4, "02 자신이 살고 있는 지역 사회의 문제에는 어떤 것이 있습니까? 어떤 해결 방법이 "
             "있을까요?"),

        SECTION("goals", "학습목표"),
        BULLET("선거의 {원칙}과 종류를 설명할 수 있다.", ordered=True),
        BULLET("{지방자치제}도와 주민 생활을 설명할 수 있다.", ordered=True),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", 2), "제목", "관련 내용"],
              [["기본", "정치", "20. 한국의 민주정치", "선거"],
               ["심화", "정치", "10. 선거와 정당", "선거"]]),

        SECTION("part", "01 선거는 어떻게 이루어지고 있을까?"),
        HEADING(2, "선거의 의미"),
        GLOSSARY(("선거권연령", "선거권연령은 2019년 12월 공직선거법 개정안 통과로 기존 만 19세에서 "
                             "만 18세로 하향 조정됨", "선거권연령")),
        PARAGRAPH("선거는 국민이 자신을 대표할 사람을 직접 뽑는 것으로, 민주주의 국가에서 국민이 정치에 "
          "참여하는 기본적인 방법이다. 한국에서는 {만 18세} 이상의 국민이면 선거에 참여할 수 "
          "있다."),

        HEADING(2, "선거의 4대 원칙"),
        PARAGRAPH("공정한 선거를 위해 한국 헌법에서는 보통·평등·직접·비밀선거라는 선거의 4대 {원칙}을 "
          "규정하고 있다."),
        BULLET("{보통 선거}: 선거에 참여할 수 있는 나이인 만 18세가 되면 한국 국민 누구나 참여할 수 "
          "있다."),
        BULLET("{평등 선거}: 성별·재산·{학력}·권력 등의 {조건}에 관계없이 {공평}하게 1인 1표씩 "
          "투표한다."),
        BULLET("{직접 선거}: {투표권}을 가진 사람이 다른 사람을 거치지 않고 직접 투표하여 자신의 "
          "대표를 뽑는다."),
        BULLET("{비밀 선거}: 어떤 후보나 정당에 투표했는지 다른 사람이 알지 못하게 한다."),
        HEADING(4, "민주선거 원칙의 반의어"),
        BULLET("보통선거 ↔ {제한선거}"),
        BULLET("평등선거 ↔ {차등선거}"),
        BULLET("직접선거 ↔ {간접선거}"),
        BULLET("비밀선거 ↔ {공개선거}"),

        HEADING(2, "선거의 종류"),
        PARAGRAPH("한국에서 실시되는 주요 선거의 종류는 다음과 같다."),
        TABLE(["선거", "실시 간격", "실시 시기", "당선되는 사람", "외국인의 참여 여부"],
              [["대통령 선거 (대선)", "5년", "3월", "대통령 1명", "허용 안 됨"],
               ["국회의원 총선거 (총선)", "4년", "4월", "국회의원 300명", "허용 안 됨"],
               ["지방 선거", "4년", "6월",
                "각 지역의 지방자치단체장, 지방의회의원, 교육감",
                "영주권을 얻은 지 3년이 지난 만 18세 이상의 외국인 중 지방자치단체의 외국인 "
                "등록 대장에 올라 있는 사람은 참여 가능"]]),
        FIGURE("투표하는 모습"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "투표일에 투표할 수 없다면? 사전 투표를 이용하세요!"),
        PARAGRAPH("각 선거의 투표일은 {임시 공휴일}로 정해져 있다. 그런데 그날 회사에 중요한 일이 있거나 "
          "개인적으로 {사정}이 생겨서 투표하지 못하는 상황이 생길 수도 있다. 이러한 경우에도 "
          "투표할 수 있도록 하기 위해 한국에서는 {사전 투표}를 실시한다. 사전 투표는 선거가 "
          "실시되기 {전주} 금요일과 토요일 아침 6시부터 저녁 6시까지 이루어진다. 사전 투표 "
          "기간에는 본인의 {주소지}와 상관없이 전국 어디든 본인이 가기 편한 곳에서 투표할 수 "
          "있다. 사전 투표는 국민의 정치 참여를 높이기 위한 제도이다."),

        SECTION("part", "02 우리 지역을 위한 정치는 어떻게 할까?"),
        HEADING(2, "지방자치제의 의미"),
        GLOSSARY(("지방자치제", "‘국가의 주인은 국민이고 국가와 그 권력은 국민으로부터 나온다.’라는 "
                             "민주주의의 가장 근본적이고 일반적인 원리로부터 나온 제도",
               "지방자치제")),
        PARAGRAPH("지역 주민이 스스로 자기 지역의 {대표자}를 뽑아서 지역의 정치를 담당하도록 하는 것을 "
          "{지방자치제}라 한다. 각 지역마다 {처한|처하다} 상황이나 {문제점}이 다르기 때문에 "
          "정부에서 각 지역의 {요구}를 모두 {처리}하기가 어렵다. 그래서 각 지역의 {자치단체}와 "
          "주민이 지역의 일에 스스로 참여하고 해결하는 지방자치제가 필요하다."),
        PARAGRAPH("지방자치제는 {중앙 정부}가 권력을 {함부로} 사용하는 것을 막을 수 있고 지역 주민이 "
          "{일상적}으로 정치에 참여할 수 있다는 점에서 민주주의를 잘 실현할 수 있는 제도이다. "
          "지방자치제는 지역 주민의 삶에 가까이 {붙어|붙다} 있다는 의미에서 ‘{풀뿌리 민주주의}’"
          "라고도 불린다."),
        FIGURE("지방 선거 홍보 포스터 — 6.13. 아름다운 선거, 행복한 우리 동네"),

        HEADING(2, "지방자치의 모습"),
        GLOSSARY(("광역", "큰 도시와 그 근처의 작은 시와 군을 포함하는 하나의 넓은 행정 단위",
               "광역")),
        PARAGRAPH("{지방자치}는 각 지역의 {지방자치단체}와 지역 주민의 {협력}과 참여를 통해 이루어진다. "
          "지방자치단체는 {광역}자치단체와 {기초}자치단체로 구분된다. 각 지방자치단체는 "
          "{지방의회}와 {지방자치단체장}을 두고 있다. 4년에 한 번씩 열리는 지방 선거를 통해 "
          "{지방의회의원}과 지방자치단체장을 뽑는다."),
        TABLE(["", "지방의회", "지방자치단체장"],
              [[CELL("광역자치단체", down=2), "특별(광역)시의회, 도의회",
                "특별(광역)시장, 도지사"],
               ["예) 서울특별시의회, 대전광역시의회, 경상북도의회",
                "예) 광주광역시장, 경기도지사, 제주도지사"],
               [CELL("기초자치단체", down=2), "시의회, 군의회, 구의회",
                "시장, 군수, 구청장"],
               ["예) 춘천시의회, 순창군의회, 수성구의회",
                "예) 충주시장, 포천군수, 해운대구청장"],
               ["기능", "지방의원으로 구성 / 지역의 실정에 맞는 정책 결정",
                "지방자치단체를 대표 / 지방의회가 결정한 정책 집행"]]),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "외국인 주민 회의도 개최해요"),
        HEADING(4, "서울시외국인주민대표자회의"),
        PARAGRAPH("서울에 사는 외국인이 {자국}의 대표가 되어 {시정}에 참여하는 {협의체}로 정책을 "
          "{제안}함."),
        HEADING(4, "부산외국인주민대표자회의"),
        PARAGRAPH("부산에 거주하는 외국인 주민들이 부산시민과 함께 {구성원}으로서 {조화}를 이루며 잘 "
          "정착할 수 있도록 {실효성}있는 정책을 마련하고자 {힘씀|힘쓰다}."),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 선거는 어떻게 이루어지고 있을까?"),
        BULLET("한국에서는 만 (      )세 이상의 국민이면 선거에 참여할 수 있다."),
        BULLET("성별, 재산, 학력, 권력 등의 조건에 관계없이 공평하게 1인 1표씩 투표하는 원칙은 "
          "(      ) 선거이다."),
        BULLET("영주권을 얻은 지 (    )년이 지난 만 18세 이상의 외국인 중 지방자치단체의 외국인 등록 "
          "대장에 올라 있는 사람은 (      ) 선거에 참여할 수 있다."),
        HEADING(3, "02 우리 지역을 위한 정치는 어떻게 할까?"),
        BULLET("(            )는 지역 주민이 스스로 자기 지역의 대표자를 뽑아서 지역의 정치를 "
          "담당하도록 하는 것이다."),
        BULLET("지방자치제는 지역 주민의 삶에 매우 가까이 붙어 있다는 점에서 (        ) 민주주의라고도 "
          "불린다."),
        BULLET("지방자치단체는 (            )와 (            )로 구분한다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "‘우리동네 시민경찰’로 임명된 외국인 자율방범대!", translation=
          "A foreign neighbourhood watch appointed ‘our neighbourhood’s "
          "citizen police’!" "\n\n"
          "○○ police station has chosen the foreign neighbourhood watch as "
          "‘our neighbourhood’s citizen police’. This is the first time in "
          "the country that a foreign neighbourhood watch has been appointed "
          "our neighbourhood’s citizen police. The foreign neighbourhood "
          "watch at ○○ police station is a body made up of fifty foreigners "
          "of Chinese, Filipino, Vietnamese, Nepalese and other "
          "nationalities. A watch member of Chinese nationality gave his "
          "thoughts: “I am glad to be able to work, beyond nationality and "
          "all together, to make our neighbourhood safe and good to live "
          "in.”"),
        PARAGRAPH("○○경찰서는 외국인 {자율방범대}를 ‘우리동네 {시민경찰}’로 {선정}했다. 외국인 "
          "자율방범대가 우리동네 시민경찰로 임명된 것은 전국에서 이번이 처음이다. ○○경찰서 "
          "외국인 자율방범대는 중국, 필리핀, 베트남, 네팔 등 {국적}의 외국인 50명으로 구성된 "
          "{단체}이다. 중국 국적 자율방법대원은 “국적을 {초월}해서 다 같이 안전하고 살기 좋은 "
          "우리 동네를 만들기 위해 노력할 수 있어 기쁘다.”고 {소감}을 밝혔다."),
        FIGURE("외국인 자율방범대 발대식(사진 출처: 〈연합뉴스〉)"),
        SOURCE("[출처] 경기일보 (2019.08.28)"),
        PARAGRAPH("★ 지역 주민으로서 자신이 살고 있는 지역을 위해 할 수 있는 일이 무엇인지 이야기해 "
          "봅시다.",
          "Talk about what you can do, as a resident, for the area where you "
          "live."),
    ],

    english={
        "선거의 의미": dict(
            title="What an election is",
            paragraphs=[
                "An election is the people choosing directly those who are to "
                "represent them, and it is the basic way in which the people "
                "of a democracy take part in politics. In Korea any national "
                "of eighteen years or over may take part.",
            ],
        ),
        "선거의 4대 원칙": dict(
            title="The four principles of an election",
            paragraphs=[
                "For the sake of fair elections the Korean constitution lays "
                "down four principles: that the vote be universal, equal, "
                "direct and secret.",
            ],
        ),
        "선거의 종류": dict(
            title="Kinds of election",
            paragraphs=[
                "The main elections held in Korea are as follows.",
            ],
        ),
        "지방자치제의 의미": dict(
            title="What local self-government is",
            paragraphs=[
                "Local self-government is the people of a locality choosing "
                "their own representatives for themselves and having them "
                "conduct the politics of the place. Because the circumstances "
                "and the problems each locality faces differ, it is hard for "
                "the central government to attend to every demand of every "
                "area. Local self-government, in which each locality's own "
                "authority and its residents take part in and settle its "
                "affairs themselves, is needed for that reason.",

                "Local self-government keeps the central government from "
                "using its power as it pleases, and lets the people of a "
                "locality take part in politics as a matter of daily life; in "
                "that it is an arrangement well suited to realising "
                "democracy. Because it sits so close to the lives of the "
                "people of a place, it is also called grassroots democracy.",
            ],
        ),
        "지방자치의 모습": dict(
            title="How local self-government works",
            paragraphs=[
                "Local self-government comes about through the cooperation "
                "and participation of each locality's authority and its "
                "residents. Local authorities are divided into the wide-area "
                "authorities and the basic ones. Each has a council and a "
                "head. The councillors and the head are chosen at the local "
                "elections held once every four years.",
            ],
        ),
    },

    extraAnnotations={
        "선거": dict(
            hanja="選擧", meaning="an election",
            characters=[("選", "선", "to choose — as in 선출, 선택"),
                        ("擧", "거", "to raise, to conduct — as in 거행")],
        ),
        "원칙": dict(
            hanja="原則", meaning="a principle",
            characters=[("原", "원", "origin — as in 원래, 원인"),
                        ("則", "칙", "rule — as in 규칙, 법칙")],
        ),
        "선거권연령": dict(
            hanja="選擧權年齡", meaning="the voting age",
            notes=["Lowered from nineteen to eighteen by the amendment to the "
                   "공직선거법 passed in December 2019 — in time for the 2020 "
                   "general election whose seat count chapter 21 prints."],
        ),
        "만 18세": dict(
            meaning="eighteen years of age (full count)",
            notes=["만 marks age counted as elsewhere in the world, from the "
                   "birthday, against the Korean count that adds a year at "
                   "birth and another at new year."],
        ),
        "보통 선거": dict(
            hanja="普通選擧", meaning="universal suffrage",
            characters=[("普", "보", "universal, general — as in 보급"),
                        ("通", "통", "to pass through — as in 통과, 교통")],
        ),
        "평등 선거": dict(
            hanja="平等選擧", meaning="equal suffrage",
            notes=["One person, one vote, of equal weight."],
        ),
        "직접 선거": dict(hanja="直接選擧", meaning="direct suffrage"),
        "비밀 선거": dict(hanja="秘密選擧", meaning="the secret ballot"),
        "제한선거": dict(
            hanja="制限選擧", meaning="restricted suffrage",
            notes=["The vote limited by property, sex or education — the "
                   "opposite of 보통선거, and how most countries began."],
        ),
        "차등선거": dict(hanja="差等選擧", meaning="weighted suffrage"),
        "간접선거": dict(
            hanja="間接選擧", meaning="indirect suffrage",
            notes=["Electors chosen by the people vote in their place. Korea "
                   "elected its presidents this way until 1987."],
        ),
        "공개선거": dict(hanja="公開選擧", meaning="open voting"),
        "학력": dict(
            hanja="學歷", meaning="educational attainment",
            characters=[("歷", "력", "history, record — as in 역사, 경력")],
        ),
        "조건": dict(
            hanja="條件", meaning="a condition",
            characters=[("條", "조", "article, item — as in 조항, 조약"),
                        ("件", "건", "case, item — as in 사건, 물건")],
        ),
        "공평": dict(
            hanja="公平", meaning="fairness, impartiality",
            characters=[("平", "평", "level, even — as in 평등, 평화")],
        ),
        "투표권": dict(hanja="投票權", meaning="the right to vote"),
        "임시 공휴일": dict(
            hanja="臨時公休日", meaning="a temporary public holiday",
            characters=[("臨", "임", "to face, temporary — as in 임시직"),
                        ("休", "휴", "rest — as in 휴가, 휴일")],
            notes=["Election day is a holiday in Korea, so that working "
                   "people can vote."],
        ),
        "사정": dict(
            hanja="事情", meaning="circumstances, a reason",
            characters=[("事", "사", "affair — as in 사건, 가사"),
                        ("情", "정", "feeling, state — as in 정보, 애정")],
        ),
        "사전 투표": dict(
            hanja="事前投票", meaning="early voting",
            notes=["The Friday and Saturday of the week before, 6 a.m. to "
                   "6 p.m., at any station in the country — no reason needed."],
        ),
        "전주": dict(hanja="前週", meaning="the previous week"),
        "주소지": dict(
            hanja="住所地", meaning="the place of one's registered address",
        ),
        "지방자치제": dict(
            hanja="地方自治制", meaning="local self-government",
            characters=[("自", "자", "self — as in 자신, 자유"),
                        ("治", "치", "to govern — as in 정치, 치안")],
            notes=["Written into the constitution in 1948, suspended in 1961, "
                   "and restored in full only in 1995."],
        ),
        "지방자치": dict(hanja="地方自治", meaning="local self-government"),
        "대표자": dict(hanja="代表者", meaning="a representative"),
        "처하다": dict(
            hanja="處하다", meaning="to be placed in, to face (a situation)",
        ),
        "문제점": dict(hanja="問題點", meaning="a problem, a difficulty"),
        "요구": dict(
            hanja="要求", meaning="a demand, a request",
            characters=[("要", "요", "necessary — as in 중요, 필요"),
                        ("求", "구", "to seek — as in 요청's 구, 추구")],
        ),
        "처리": dict(
            hanja="處理", meaning="handling, disposal",
            characters=[("處", "처", "to deal with — as in 처벌, 대처"),
                        ("理", "리", "to manage — as in 관리, 원리")],
        ),
        "자치단체": dict(hanja="自治團體", meaning="a self-governing authority"),
        "중앙 정부": dict(
            hanja="中央政府", meaning="the central government",
            characters=[("央", "앙", "centre — as in 중앙")],
        ),
        "함부로": dict(
            meaning="carelessly, as one pleases",
            notes=["Close to 마구 and 마음대로, but always with a note of "
                   "reproach — of power used without care."],
        ),
        "일상적": dict(hanja="日常的", meaning="everyday, routine"),
        "붙다": dict(meaning="to be attached to, to stick to"),
        "풀뿌리 민주주의": dict(
            meaning="grassroots democracy",
            notes=["풀뿌리 is “grass root” — a calque of the English figure."],
        ),
        "지방자치단체": dict(hanja="地方自治團體", meaning="a local authority"),
        "협력": dict(
            hanja="協力", meaning="cooperation",
            characters=[("協", "협", "to cooperate — as in 협의, 협회"),
                        ("力", "력", "force — as in 능력, 압력")],
        ),
        "광역": dict(
            hanja="廣域", meaning="a wide area, a metropolitan region",
            characters=[("廣", "광", "wide — as in 광고, 광장"),
                        ("域", "역", "region — as in 지역, 영역")],
            notes=["The 광역자치단체 are the 17 시·도; the 기초자치단체 the 시, 군 "
                   "and 구 beneath them."],
        ),
        "기초": dict(
            hanja="基礎", meaning="basic, foundational",
            characters=[("基", "기", "base — as in 기본, 기반"),
                        ("礎", "초", "cornerstone")],
        ),
        "지방의회": dict(hanja="地方議會", meaning="a local council"),
        "지방자치단체장": dict(
            hanja="地方自治團體長",
            meaning="the head of a local authority",
            notes=["A 시장, 군수, 구청장 or 도지사 — the executive side, against "
                   "the council."],
        ),
        "지방의회의원": dict(hanja="地方議會議員", meaning="a local councillor"),
        "자국": dict(hanja="自國", meaning="one's own country"),
        "시정": dict(
            hanja="市政", meaning="city administration",
            characters=[("市", "시", "city — as in 시장, 도시")],
        ),
        "협의체": dict(
            hanja="協議體", meaning="a consultative body",
            characters=[("議", "의", "to deliberate — as in 회의, 의논")],
        ),
        "제안": dict(
            hanja="提案", meaning="a proposal",
            characters=[("提", "제", "to present — as in 제출, 제시"),
                        ("案", "안", "plan, draft — as in 법안, 예산안")],
        ),
        "구성원": dict(hanja="構成員", meaning="a member of a body"),
        "조화": dict(
            hanja="調和", meaning="harmony",
            characters=[("調", "조", "to tune, to adjust — as in 조정, 조사"),
                        ("和", "화", "harmony, peace — as in 화합, 평화")],
        ),
        "실효성": dict(
            hanja="實效性", meaning="effectiveness in practice",
            characters=[("效", "효", "effect — as in 효과, 효력")],
        ),
        "힘쓰다": dict(meaning="to strive, to put effort into"),
        "자율방범대": dict(
            hanja="自律防犯隊", meaning="a volunteer crime-prevention patrol",
            characters=[("律", "률", "rule — as in 법률, 규율"),
                        ("防", "방", "to defend — as in 예방, 방지"),
                        ("犯", "범", "to offend — as in 범죄, 범인"),
                        ("隊", "대", "a troop, a corps — as in 군대")],
            notes=["Neighbourhood volunteers who patrol with the local police "
                   "station — 자율 “self-regulating”, i.e. unpaid and "
                   "voluntary."],
        ),
        "시민경찰": dict(hanja="市民警察", meaning="a citizen police volunteer"),
        "선정": dict(
            hanja="選定", meaning="selection, designation",
            characters=[("選", "선", "to choose — as in 선거, 선출"),
                        ("定", "정", "to fix — as in 확정, 규정")],
        ),
        "국적": dict(
            hanja="國籍", meaning="nationality",
            characters=[("籍", "적", "register — as in 재적, 호적")],
        ),
        "단체": dict(hanja="團體", meaning="a group, an organisation"),
        "초월": dict(
            hanja="超越", meaning="transcending, going beyond",
            characters=[("超", "초", "to exceed — as in 초과, 초고속"),
                        ("越", "월", "to cross over — as in 월경")],
        ),
        "소감": dict(
            hanja="所感", meaning="one's impressions, what one felt",
            characters=[("所", "소", "place, that which — as in 장소, 소득"),
                        ("感", "감", "to feel — as in 감사, 감정")],
        ),
    },

    extraNotes=[
        "The 4대 원칙 table on p. 127 is printed with no header, so it is set "
        "as a list, each principle naming itself, and the 반의어 box beside "
        "it likewise.",
        "The 지방자치 table on p. 128 prints 예 in a column of its own; here "
        "the examples are folded into the row below each kind, prefixed 예).",
        "The review gaps on p. 129 are blank in the book and left blank here.",
    ],
)
