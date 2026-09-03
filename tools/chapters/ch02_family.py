# -*- coding: utf-8 -*-
"""Chapter 2 — Family.

Source: 2.html (Google Docs HTML export)
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, LABELS,
               MARGIN, TABLE, CELL, CHART, GLOSSARY)

CHAPTER = dict(
    number=2, slug="02-family",
    unit="사회", title="가족", titleEn="Family",

    blocks=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 한국의 다양한 가족의 모습입니다."),
        HEADING(4, "01 한국에서많이본가족은어떤모습입니까?"),
        HEADING(4, "02 현재 본인의 가족은 어떤 가족의 모습과 가장 비슷합니까? (본인의 고향에 있는 가족, 한국에 있는 " "가족)"),
        SECTION("goals", "학습목표"),
        BULLET("한국 가족 형태의 변화와 가족 문화의 특징을 설명할 수 있다.", ordered=True),
        BULLET("한국 사회의 가족 및 친척 관계와 호칭을 설명할 수 있다.", ordered=True),
        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"], [["기본", "법", "33. 가족과법",
              "부부로 인정받기 위한 절차, 부부의 권리와 의무"],
              ["심화", "역사", "8. 사회변동", "저출산 현상, 고령화사회"],
              ["심화", "법", "17. 가족문제와 법", "가족과친족, 이혼"]]),
        SECTION("part", "01 한국의가족은어떤특징을가지고있을까?"),
        CHART("가구 유형별 비율(통계청, 2018) — 핵가족과 1인 가구의 비율이 높다.", "%", [["1인 가구",
              29.3],
              ["2인 가구", 27.3],
              ["3인 가구", 21.0],
              ["4인 가구", 17.0],
              ["5인 이상 가구", 5.4]]),
        FIGURE("가구 유형별 비율(통계청, 2018) 핵가족과 1인 가구의 비율이 높다."),
        GLOSSARY(("연령", "나이", "연령"),
              ("산업화",
              "생산 활동의 분업화(일을 나누어서 함)와 기계화(기계사용)로 제조(제품 생산)와 서비스 산업의 비율이 "
              "높아지는 현상", "산업화")),
        HEADING(4, "가족 형태의 변화"),
        PARAGRAPH("한국에서 결혼은 보통 30세 {전후}에 많이 하는 편인데, 최근 들어 30대 {중후반} 정도에 하는 "
          "경우가 늘어나 결혼하는 연령이 점점 높아지고 있다. 과거에는 결혼 후에도 부모와 같이 사는 {자녀}가 "
          "많아 {조부모}, 부모, 자녀 등 여러 세대의 가족이 같이 모여 사는 {확대가족|확대 가족} 형태가 " "일반적이었다."),
        PARAGRAPH("그러나 산업화와 함께 큰 도시에 학교와 회사 등이 많이 생기면서 공부나 취업을 위해 부모와 떨어져 "
          "생활하는 자녀들이 증가하였다. 이와 함께 결혼한 자녀가 부모와 함께 사는 경우가 크게 줄면서, 부모와 "
          "미혼 자녀가 함께 사는 핵가족의 모습을 주로 볼 수 있다. 또한 공부나 일 등을 하는 과정에서 결혼을 "
          "하지 않거나, 결혼을 하더라도 자녀를 낳지 않고 살겠다는 사람들이 늘어나면서 1인 가구나 부부만 사는 "
          "비율이 증가하고 있다."),
        GLOSSARY(("유대관계", "둘 이상을 서로 연결하거나 결합하는 관계", "유대관계"),
              ("제삿날", "조상이 돌아가신 날을 기억 하며 음식을 차려 조상에게 드리는 날", "제삿날"),
              ("유교", "공자에게서 비롯된 중국의 사상으로 중국 • 한국 • 일본 등에 많은 영향을 미침", "유교"),
              ("효 사상", "자식이 부모를 잘 섬기는 것을 중요하게 생각하는 것", "효 사상")),
        HEADING(4, "가족 문화의 특징"),
        PARAGRAPH("한국인은 개인의 행복뿐만 아니라 가족 {간}의 유대관계를 중요하게 생각한다. 그래서 명절, 조상의 "
          "제삿날, 가족(부모)의 생일, 어버이날 등이 되면 멀리 떨어져 있던 가족들도 한자리에 모이는 경우가 " "많다."),
        PARAGRAPH("전통적인 한국의 가족은 유교, 효 사상 등의 영향으로 가족 구성원 간의 서열이나 역할을 명확하게 "
          "나누었다. 그러나 사회 변동과 함께 가족 형태와 가치관이 달라지면서 가족 구성원의 역할과 가족 문화에도 "
          "변화가 생겼다. 예를 들어, 가족의 중요한 일을 남자 어른 혼자 결정하지 않고 가족 구성원이 함께 "
          "의논하여 결정하거나, 집안일이나 육아에 부부가 함께 참여하는 모습 등이 늘어나고 있다. 또한, 명절이나 "
          "생일에 가족이 한 집에 모이는 대신 가족 여행을 가는 경우도 많아지고 있다."),
        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "1인 가구 증가로 어떤 변화가 나타나고 있을까?"),
        PARAGRAPH("요즘 '1인분' 반찬, '한 끼' 같은 소포장 상품, 소형가전 등 1인 가구를 겨냥한 제품이 계속 "
          "등장하고 있다. 결혼 시기가 늦춰지고 이혼율 증가, 고령화 현상 등이 나타나면서 1인 가구의 비중이 "
          "30%에 가까워졌는데 이로 인해 주택, 식품, 가전제품 등 산업 전반에 큰 변화가 일어나고 있다. 작은 "
          "크기의 집을 찾는 사람이 늘고 있고 대형마트나 편의점에서는 혼자서 간단히 먹을 수 있는 간편식 매출이 "
          "급증하였다. 작은 크기의 가전제품도 많아졌을 뿐 아니라, 가전제품 사는 것 자체를 번거로워 하는 1인 "
          "가구를 위해 가전제품을 빌려주는 서비스도 늘어나고 있다."),
        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 한국의 가족은 어떤 특징을 가지고 있을까?"),
        BULLET("과거에는 결혼 후에도 부모와 같이 사는 경우가 많아 여러 세대의 가족이 같이 모여 사는 (   ) 형태가 " "많았다."),
        BULLET("( 산업화 ) 이후로 ( 공부 )나 ( 취업 )을 위해 부모와 떨어져 생활하는 자녀들이 많아졌으며, "
          "결혼한 이후에 부모와 함께 사는 경우도 크게 줄어 요즘은 대부분 ( 핵가족 )형태가 많다."),
        HEADING(3, "02 한국의 가족과 친척은 서로를 어떻게 부를까?"),
        BULLET("한국에서는 가족과 친척을 ( 호칭  )로 표시한다."),
        BULLET("남편과 아내는 촌수를 (   )."),
        BULLET("부모와 자녀 관계는 (   ), 형제·자매 관계는 (   ) 이다."),
        BULLET("형제자매의 자녀와 내 자녀의 관계는 (   ) 이다."),
        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "한국의 가족에서 ‘우리’와 ‘식구’의 의미는?"),
        PARAGRAPH("‘우리’는 ‘나와 당신’을 함께 가리키는 표현으로 나와 이야기를 나누는 상대방을 그만큼 가깝게 생각한다는 "
          "의미가 들어 있다."),
        PARAGRAPH("그래서 한국 사람들은 자신의 가족을 다른 사람에게 이야기할 때 ‘우리 엄마’, ‘우리 남편’, ‘우리 "
          "애들’과 같이 ‘우리’라는 표현을 많이 사용한다."),
        PARAGRAPH("또한 가족 대신에 {식구}라는 표현을 사용하기도 하는데 식구는 한 상에서 같이 밥을 먹는 사이라는 "
          "뜻이다. 그래서 한국 사람들은 종종 “언제 밥 한번 같이 먹자.”라는 말을 하는데, 이는 가족처럼 "
          "{친밀하게|친밀하다} 지내고 싶다는 표현 이기도 하다."),
        MARGIN("{집단주의} / {개인주의}"),
        PARAGRAPH("★ 위의 {사례}처럼 {자신}의 고향에서 가족과 관련된 {특색} 있는 표현과 그 의미를 소개해 봅시다."),
        SECTION("part", "02 한국의 가족과 친척은 서로를 어떻게 부를까?"),
        GLOSSARY(("호칭", "서로 부름", "호칭"),
              ("지칭", "어떤 대상을 가리켜 말함", "지칭"),
              ("양성평등", "여성과 남성을 차별하지 않고 동등하게 대우함", "양성평등")),
        HEADING(2, "가족 관계 호칭"),
        PARAGRAPH("한국에서는 가족 관계에서 서로를 부르는 호칭이 있다. 부부 간에는 주로 ‘여보’, ‘당신’이라고 부르거나 "
          "아이가 있을 경우 아이의 이름을 사용하여 ‘OO아빠’, ‘OO엄마’라고 부르기도 한다. 배우자의 부모님은 "
          "‘아버님’, ‘어머님’이라고 부르는데, 다른 사람 앞에서 배우자의 부모님을 지칭할 때는 아내는 남편의 "
          "부모님을 ‘시아버지’, ‘시어머니’라고 하고 남편은 아내의 부모님을 ‘장인어른’, ‘장모님’이라고 "
          "부른다. 남편의 부모는 아직 아이를 낳지 않은 며느리를 보통 ‘(새)아가’라고 부른다. 아이를 낳고 나면 "
          "며느리를 ‘어멈아’, 아들을 ‘애비야’ 라고도 부른다. 아내의 부모는 사위를 부를 때 사위의 성을 앞에 "
          "붙여서 ‘O서방’이라고 부른다. 예를 들어, 사위가 박 씨이면, ‘박서방’이라고 한다. 최근에는 "
          "양성평등의 정신을 더욱 잘 실현하기 위해 아내의 가족과 남편의 가족에 대한 호칭 구분을 없애자는 제안이 " "나오고 있다."),
        HEADING(2, "친척 관계 촌수"),
        PARAGRAPH("한국에서는 가족과 친척 관계를 ‘{촌수}’로 표시한다. 남편과 아내는 동일한 위치에 있다고 보기 때문에 "
          "촌수를 따지지 않는다. 부모와 자녀는 1촌, 형제자매는 2촌이다. 내가 결혼을 해서 자녀를 낳았다면, "
          "나의 남동생과 내 자녀는 3촌이 된다. 나의 남동생의 자녀와 내 자녀는 4촌이 된다. 일반적으로 남편이나 "
          "아내의 형제자매에게서 태어난 자녀와 내 자녀의 관계를 '사촌' 이라고 부른다. 남편의 남자 형제 자녀와는 "
          "'친사촌', 남편의 여자 형제 자녀와는 '고종사촌', 아내의 남자 형제 자녀와는 '외사촌', 아내의 여자 "
          "형제 자녀와는 '이종사촌'이라고 부른다."),
        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "남편의 가족을 부를 때와 아내의 가족을 부를 때 호칭이 달라요"),
        HEADING(3, "남편이 아내의 가족을 부를 때"),
        TABLE(["가족", "호칭"], [["아버지", "장인어른, 아버님"],
              ["어머니", "장모님, 어머님"],
              ["오빠", "형님, 처남(어릴 때)"],
              ["오빠의 아내", "아주머니"],
              ["언니", "처형"],
              ["언니의 남편", "형님, 동서(어릴 때)"],
              ["남동생", "처남"],
              ["남동생의 아내", "처남댁"],
              ["여동생", "처제"],
              ["여동생의 남편", "동서, O서방"]]),
        HEADING(3, "아내가 남편의 가족을 부를 때"),
        TABLE(["가족", "호칭"], [["아버지", "아버님"],
              ["어머니", "어머님"],
              ["형", "아주버님"],
              ["형의 아내", "형님"],
              ["누나", "형님"],
              ["누나의 남편", "시매부 또는 고모부"],
              ["남동생", "도련님"],
              ["남동생의 아내", "동서"],
              ["여동생", "아가씨"],
              ["여동생의 남편", "시매부 또는 고모부"]]),
    ],
    annotations={
        "연령": dict(
            hanja="年齡",
            meaning="\"age\" (formal/written word, more formal than 나이)",
        ),
        "산업화": dict(
            hanja="産業化",
            meaning="\"industrialization\"",
        ),
        "전후": dict(
            meaning="literally \"before-after\" — \"around/approximately\"",
            notes=["30대 중후반 — \"mid-to-late 30s\" (roughly 35–39)"],
        ),
        "중후반": dict(
            meaning="literally \"middle-later half\"",
        ),
        "자녀": dict(
            hanja="子女",
            meaning="literally \"son-daughter\" — \"children/one's offspring\"",
        ),
        "조부모": dict(
            hanja="祖父母",
            meaning="literally \"ancestor-father-mother\" — \"grandparents\"",
        ),
        "확대 가족": dict(
            headword="확대가족",
            hanja="擴大家族",
            meaning="\"extended family\"",
            characters=[("擴", "확", "to expand/enlarge"), ("大", "대", "big/large"
                )],
            surfaces=["확대가족"],
        ),
        "유대관계": dict(
            hanja="紐帶關係",
            meaning="\"bond/tie\" — a relationship connecting or uniting two or "
                "more things/people.",
        ),
        "제삿날": dict(
            hanja="祭祀날",
            meaning="\"ancestral memorial day\" — a day when descendants "
                "remember the day an ancestor passed away and prepare food "
                "to offer to that ancestor.",
        ),
        "유교": dict(
            hanja="儒敎",
            meaning="\"Confucianism\" — a Chinese school of thought originating "
                "from Confucius, which greatly influenced China, Korea, "
                "Japan, etc.",
        ),
        "효 사상": dict(
            hanja="孝思想",
            meaning="\"filial piety\" — the belief that it's important for "
                "children to serve/care for their parents well.",
        ),
        "간": dict(
            meaning="between / amongst",
        ),
        "식구": dict(
            hanja="食口",
            meaning="literally \"eating mouths\"",
            notes=["食 (sik) — to eat/food", "口 (gu) — mouth"],
        ),
        "친밀하다": dict(
            hanja="親密하다",
            meaning="to be intimate / close",
            surfaces=["친밀하게"],
        ),
        "집단주의": dict(
            meaning="groupism",
        ),
        "개인주의": dict(
            meaning="individualism",
        ),
        "사례": dict(
            hanja="事例",
            meaning="case / example / instance",
            characters=[("事", "사", "matter/affair (same 事 as in 사건)"), ("例",
                "례", "example (same 例 as in 해례본)")],
        ),
        "자신": dict(
            meaning="oneself",
        ),
        "특색": dict(
            hanja="特色",
            meaning="distinctive feature / characteristic / distinguishing "
                "trait",
        ),
        "호칭": dict(
            hanja="呼稱",
            meaning="\"a term/title used to address someone directly\"",
            characters=[("呼", None, "to call/shout"), ("稱", None,
                "to name/call/title")],
            notes=["Literally \"calling-name\" → the word or title you use "
                "when speaking directly to someone (in front of them)."],
        ),
        "지칭": dict(
            hanja="指稱",
            meaning="\"referring to / indicating a certain target when speaking "
                "about them\"",
            characters=[("指", None, "to point/indicate"), ("稱", None,
                "to name/call")],
            notes=["Literally \"pointing-name\" → the word you use when "
                "talking about someone to a third person, rather than "
                "speaking directly to them."],
        ),
        "양성평등": dict(
            hanja="兩性平等",
            meaning="\"gender equality\"",
            characters=[("兩", None, "both/two"), ("性", None, "sex/gender"), (
                "平", None, "equal/flat"), ("等", None, "rank/grade")],
            notes=["Hanja breakdown:"],
        ),
        "촌수": dict(
            hanja="寸數",
            meaning="\"degree of kinship\" — a numerical system for measuring "
                "how closely related two people are.",
            notes=["Literally \"distance-number\" → a number expressing how "
                "many relational \"steps\" separate two people."],
        ),
    },
    fixes=[
        ("한국에서많이본가족은어떤모습입니까?", "한국에서 많이 본 가족은 어떤 모습입니까?", "word spacing lost in the doc"),
        ("한국의가족은어떤특징을가지고있을까?", "한국의 가족은 어떤 특징을 가지고 있을까?", "word spacing lost in the doc"),
        ("가족과법", "가족과 법", "spacing"),
        ("가족과친족", "가족과 친족", "spacing"),
        ("고령화사회", "고령화 사회", "spacing"),
        ("기억 하며", "기억하며", "spacing"),
        ("중국 • 한국 • 일본", "중국·한국·일본", "bullets used for middle dots"),
        ("표현 이기도", "표현이기도", "spacing"),
        ("'사촌' 이라고", "‘사촌’이라고", "spacing and mismatched quote"),
    ],
    # read against the page and accepted, so they no longer report themselves.
    # 사회변동 and 가족문제와 법 were rejected and their corrections removed:
    # the 관련 단원 table prints both closed up.
    approved={
        "한국에서많이본가족은어떤모습입니까?", "한국의가족은어떤특징을가지고있을까?",
        "가족과법", "가족과친족", "고령화사회", "기억 하며", "중국 • 한국 • 일본",
        "표현 이기도", "'사촌' 이라고",
    },
    headwords={"친밀하게": "친밀하다", "확대가족": "확대 가족"},
    # left open again for now
    clearGaps={"호칭"},
    english={
        "가족 형태의 변화": dict(
            title="How the shape of the family changed",
            paragraphs=[
                "In Korea marriage is usually around the age of thirty, though lately "
                "more people marry in their mid to late thirties, so the age at "
                "marriage is climbing. In the past many children went on living with "
                "their parents after marrying, and the usual form was the extended "
                "family, several generations — grandparents, parents, children — "
                "gathered under one roof.",

                "With industrialisation, however, schools and companies gathered in "
                "the large cities, and more children came to live apart from their "
                "parents in order to study or to find work. Along with this the cases "
                "of married children living with their parents fell sharply, and what "
                "one mainly sees now is the nuclear family, parents living with their "
                "unmarried children. More people also decide, in the course of "
                "studying or working, not to marry, or to marry but not have "
                "children, so the proportion of single-person households and of "
                "couples living on their own is rising.",
            ],
        ),
        "가족 문화의 특징": dict(
            title="What marks the culture of the family",
            paragraphs=[
                "Koreans hold the bonds between family members to be important, not "
                "only the happiness of the individual. So at the seasonal holidays, "
                "an ancestor's memorial day, a parent's birthday or Parents' Day, "
                "families who live far apart will often gather in one place.",

                "In the traditional Korean family, under the influence of "
                "Confucianism and of filial piety, rank and role among family members "
                "were clearly divided. But as society has changed, and family forms "
                "and values with it, the roles of family members and the culture of "
                "the family have changed too. Important family matters, for instance, "
                "are increasingly decided by the family talking them over together "
                "rather than by the eldest man alone, and husband and wife "
                "increasingly share the housework and the raising of the children. It "
                "is also becoming common for a family to travel together at a holiday "
                "or a birthday instead of gathering at one house.",
            ],
        ),
        "가족 관계 호칭": dict(
            title="What family members call one another",
            paragraphs=[
                "In Korea there are set terms by which family members address one "
                "another. Between husband and wife the usual terms are ‘여보’ and "
                "‘당신’, or, where there are children, the child's name as in "
                "‘OO아빠’ and ‘OO엄마’. A spouse's parents are addressed as ‘아버님’ "
                "and ‘어머님’; when speaking of them to someone else, a wife calls "
                "her husband's parents ‘시아버지’ and ‘시어머니’, and a husband calls "
                "his wife's parents ‘장인어른’ and ‘장모님’. A husband's parents "
                "usually call a daughter-in-law who has not yet had a child "
                "‘(새)아가’. Once she has had a child they may call her ‘어멈아’ and "
                "their son ‘애비야’. A wife's parents address a son-in-law by putting "
                "his surname in front, as ‘O서방’. If the son-in-law is a 박, for "
                "instance, he is ‘박서방’. Lately it has been proposed that the "
                "distinction between the terms for the wife's family and those for "
                "the husband's family be done away with, the better to realise gender "
                "equality.",
            ],
        ),
        "친척 관계 촌수": dict(
            title="Counting kinship in degrees",
            paragraphs=[
                "In Korea family and kin relations are marked in ‘촌수’, degrees. "
                "Husband and wife are held to stand in the same place, so no degree "
                "is counted between them. Parent and child are one degree, brothers "
                "and sisters two. If I marry and have a child, my younger brother and "
                "my child are three degrees apart. My younger brother's child and my "
                "child are four. In general the children born to a husband's or a "
                "wife's siblings are called ‘사촌’ in relation to one's own children. "
                "The children of a husband's brother are ‘친사촌’, of a husband's "
                "sister ‘고종사촌’, of a wife's brother ‘외사촌’, and of a wife's "
                "sister ‘이종사촌’.",
            ],
        ),
    },
    # Both checked and accepted, so neither is reported on the page:
    #   - the two 호칭 tables below lost their structure in the export and were
    #     rebuilt by pairing each relative with the term that follows it
    #   - 시애부 is not a word; it is set as 시매부 (husband's sister's husband)
)
