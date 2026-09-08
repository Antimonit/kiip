# -*- coding: utf-8 -*-
"""Chapter 3 — The workplace.

Source: 3.html (Google Docs HTML export)
Page photos: pages 24-27.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, LABELS,
               MARGIN, TABLE, CELL, CHART, GLOSSARY)

CHAPTER = dict(
    number=3, slug="03-workplace",
    unit="사회", title="일터", titleEn="The workplace",

    blocks=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 한국의 일터와 관련된 다양한 모습입니다."),
        LABELS("{택배}", "{야근}", "{회식}"),
        HEADING(4, "01 한국 일터와 관련된 여러 가지 모습 중에서 본인의 고향과 비슷한 점, 다른 점은 무엇입니까?"),
        HEADING(4, "02 본인은 한국의 어떤 직장에서 일을 해 보고 싶습니까? 그 이유는 무엇입니까?"),
        SECTION("goals", "학습목표"),
        BULLET("한국 사회의 직장 생활 특징을 설명할 수 있다.", ordered=True),
        BULLET("한국 사회의 직장 문화를 이해하고 직장 관련 어려움에 대한 해결 방안을 탐색할 수 있다.", ordered=True),
        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"], [["기본", "경제", "29. 취업하기",
              "한국의 일자리 현황, 취업하기 위한 방법"],
              ["심화", "경제", "15. 기업과 근로자", "대한민국의 여러 기업들, 대한민국의 근로 조건, 근로자의 권리"]
              ]),
        SECTION("part", "01 한국인은 어떤 일터에서 일할까?"),
        GLOSSARY(("취업난", "일자리를 구하기 어려움", "취업난"),
              ("은퇴", "맡은 일에서 물러남", "은퇴"),
              ("자아실현", "개인의 능력을 발휘하고 가치 를 이루어 냄", "자아실현"),
              ("사회공헌", "사회의 발전에 도움을 중 국가기업", "사회공헌", "seciety contribution"),
              ("공기업", "국가나 지방자치단체가 사회 공공의 복리를 증진하기 위하 여 경영하는 기업", "공기업",
              "state-owned company"),
              ("임금", "어떤 직장에서 계속 일하는 사람이 일의 대가로 받는 돈", "임금", "wage/pay")),
        HEADING(2, "한국인들이 선호하는 일터", translation=
          "한국인들이 선호하는 일터 (Workplaces Koreans prefer)" "\n\n"
          "\"In Korea, it's possible to work from age 15 and up. "
          "However, generally, people tend to start working in their "
          "early 20s after high school graduation, or in their "
          "mid-to-late 20s after university graduation. Recently, due "
          "to job-market difficulties (취업난), the age at which people "
          "start working has often become even later. After getting "
          "employed, people generally work until around age 60. These "
          "days, as average life expectancy has lengthened, more "
          "people take on new jobs or prepare to start businesses "
          "even after retirement, for economic reasons or for "
          "self-realization (자아실현) or social contribution (사회공헌)." "\n\n"
          "Among those preparing to find jobs in Korea, many prefer "
          "stable employment and hope to become civil servants or "
          "work at state-owned enterprises (공기업). Compared to other "
          "workplaces, these jobs have stable employment terms and "
          "working conditions, but since the number of positions is "
          "small, competition rates are high. Some people want to "
          "work at large corporations (대기업). Large corporations are "
          "popular because wages are high and there are many welfare "
          "benefits for employees." "\n\n"
          "Besides these, there are also people who take jobs at "
          "somewhat smaller mid-sized companies, people who work "
          "freelance without a fixed affiliation, and people who "
          "start their own companies or shops directly.\""),
        PARAGRAPH("한국에서는 만 15세 이상부터 일을 하는 것이 가능하다. 그러나 일반적으로는 고등학교 졸업 후 20대 "
          "{초반}이나, 대학교 졸업 후 20대 중후반쯤에 일을 시작하는 편이다. 최근에는 취업난으로 인해 일을 "
          "시작하는 나이가 더 늦어지는 경우도 많다. 취업 후에는 대체로 60세 전후까지 직장 생활을 한다. 요즘은 "
          "평균 {수명이} 길어져서 은퇴 이후에도 경제적 이유나 자아실현, 사회 공헌 등을 위해 새로운 직업을 "
          "갖거나 창업을 준비하는 사람들이 많아졌다."),
        PARAGRAPH("한국에서 취업을 준비하는 사람들 중에는 안정적인 직업을 선호해 공무원이 되거나 공기업에서 일하는 것을 "
          "희망하는 경우가 많다. 이러한 직장은 다른 곳에 비해 근무 기간이나 근무 환경이 안정적이지만 뽑는 "
          "인원수가 많지 않아 경쟁률이 높은 편이다. 대기업에서 일하기를 원하는 사람도 있다. 대기업은 임금이 높고 "
          "직원에 대한 복지 혜택도 많아서 인기가 높다."),
        PARAGRAPH("그 외에 다소규모가 작은 중소기업에 취직하거나 일정한 소속이 없이 자유 계약으로 일하는 사람들, 직접 "
          "회사나 가게를 만들어 사업을 하는 사람들도 있다."),
        GLOSSARY(("기혼", "이미 결혼함", "기혼", "married"),
              ("경력 단절", "공부나 직장을 그만두고 나서 새로운 직장에 들어가기까지 경력이 비어있는 상태", None,
              "career interrupted"),
              ("정책", "공공문체를 해결하기 위해 정부 가 결정한 일의 계획", None, "policy")),
        HEADING(2, "여성의 경제 활동", translation="여성의 경제 활동 (Women's Economic Activity)"
          "\n\n" "\"In the past, most working people were men. However, as "
          "university enrollment rates for men and women gradually "
          "became similar, and women's advancement into society "
          "became more active, the gap in the ratio of working men "
          "and women has greatly narrowed. As more women engage in "
          "economic activity, the gender imbalance by occupation is "
          "also gradually easing." "\n\n"
          "Dual-income couples, where both husband and wife work, are "
          "also increasing (dual-income household rate: 46.3%, "
          "Statistics Korea, 2019), but a significant number of "
          "married women quit their jobs due to childbirth and "
          "childcare issues, which causes career interruptions (경력 "
          "단절). For women who want to return to work after raising "
          "their children to some extent, education and policies (정책) "
          "supporting reemployment and entrepreneurship are being "
          "implemented.\""),
        PARAGRAPH("과거에는 직장인 대부분이 남성이었다. 그러나 {점차} 남녀의 대학 진학률이 비슷해지고 여성의 사회 "
          "{진출}이 {활발해|활발하다}지면서 일하는 남녀의 비율 차이가 크게 줄어들었다. 경제 활동을 하는 여성이 "
          "많아지면서 직업별 남녀 간 불균형도 조금씩 {완화|완화하다}되고 있다."),
        PARAGRAPH("남편과 아내 모두가 일을 하는 맞벌이 부부도 증가하고 있으나(맞벌이 가구 비율 46.3%, 통계청, "
          "2019) 기혼 여성 중 {상당수}는 출산과 {양육} 문제로 직장을 그만두기도 하며, 이로 인해 경력 "
          "{단절}이 발생한다. 자녀를 어느 정도 키운 후에 다시 일하기 원하는 여성들을 위해 재취업과 창업을 "
          "지원하는 교육 및 정책이 {시행|시행하다}되고 있다."),
        CHART("남녀의 경제 활동 참가율(통계청, 2019)(단위: %) — 남자와 여자의 경제 활동 비율 격차가 "
              "줄어들고 있다. 막대는 각 해의 남녀 격차를 나타낸다.", "%p", [["1985년", 45.8],
              ["1995년", 41.2],
              ["2005년", 34.8],
              ["2011년", 33.5],
              ["2012년", 33.3],
              ["2019년", 20.7]]),
        MARGIN("실시하다/시행하다"),
        SECTION("aside", "알아두면 좋아요"),
        HEADING(4, "한국에서 특별히 많이 볼 수 있는 직업은?"),
        PARAGRAPH("차의 주인이 일정 금액을 내고 요청하면 차를 대신 운전해주는 사람을 {대리운전기사}라고 하는데 한국 "
          "특유의 회식문화로 인해 대리 운전 전문 회사가 생겨나기 시작했다. 주로 밤 시간에 일하고, 운전면허가 "
          "있으면 일할 수 있어 본인의 직업 외에 {겸업|겸업하다}하는 사람들도 많다. 한편, 1인 가구와 맞벌이 "
          "가구가 증가하면서 인터넷으로 물건을 주문하면 새벽에 배송해주는 산업도 크게 성장하고 있다. 이에 따라 "
          "새벽배송 일에 종사하는 사람들의 수도 많아졌다."),
        SECTION("part", "02 한국인의 직장 생활은 어떤 모습일까?"),
        GLOSSARY(("관공서", "국가 또는 지방자치단체의 사무를 처리하는 기관", "관공서"),
              ("탄력적", "상황에 따라 알맞게 대처하는 것", "탄력적", "Flexible"),
              ("교대", "어떤 일을 여럿이 나누어서 차례에 따라 맡아 함", "교대")),
        HEADING(2, "직장 근무 시간과 근무 유형"),
        PARAGRAPH("한국의 관공서나 회사는 일반적으로 오전 9시부터 오후 6시까지 일한다. 낮 12시 전후로 1시간 정도의 "
          "점심시간이 있으므로 하루에 8시간 정도 근무한다. 보통 오후 6시가 되면 퇴근을 하는데, 해야 할 일이 "
          "남았을 경우에는 직장에 남아 시간 외 근무를 하기도 한다. 그래도 일주일 동안의 총 근무 시간은 52시간 "
          "이내여야 한다(2020년 기준). 근무 시작 시간과 종료 시간이 {명확하게|명확하다} 정해진 정규 근무 "
          "외에 일정한 기간 동안 근로해야 할 총 근로 시간만 정하고 시간을 효율적으로 활용하도록 하는 탄력적 근로 "
          "{시간제}를 운영하는 회사도 있다."),
        PARAGRAPH("대부분의 직장에서는 월요일에서 금요일까지 5일을 일하는 ‘주 5일제’가 적용되지만 일터의 특성상 주말에 "
          "일을 해야 하는 경우는 평일에 쉬기도 한다. 24시간 운영하는 찜질방, 편의점, PC방이나 경찰서, "
          "소방서, 병원, 항만, 공항 등 24시간 내내 서비스가 제공되어야 하는 곳에서 일하는 경우는 직원들이 "
          "서로 차례를 바꾸어 교대 근무를 한다."),
        GLOSSARY(("추구", "목적을 이룰 때까지 뒤좇아 구함", None, "pursuit/chase"),
              ("경향", "현상이나 행동이 어떤 방향으로 기울어짐", None, "trend/tendency"),
              ("워라밸", "일과 삶의 균형이라는 뜻으로 “Work and Life Balance”의 준말")),
        HEADING(2, "직장 문화"),
        PARAGRAPH("한국에서는 근무를 마친 후에 종종 회사 진원 들끼리 회식을 한다. 회사 직원들끼리 친밀한 관계를 형성하기 "
          "위해서 또는 축하나 위로를 받아야 할 직장 동료가 있을 때 회식을 하는 경우가 많다. 회식하는 날은 "
          "식사와 이야기가 밤늦게까지 이어지기도 한다."),
        PARAGRAPH("최근에는 일과 삶의 균형을 추구하는 문화, 개인의 의사를 존중하는 문화가 확산되면서 회식의 빈도가 "
          "줄어드는 경향이 있다. 그리고 회식을 하더라도 술이나 식사 대신 직장 동료들과 함께 영화나 공연, "
          "스포츠를 즐기는 등 모두가 참여해서 즐길 수 있는 방식이 늘어나고 있다."),
        FIGURE("직장 동료들과 함께 차를 마시거나 영화를 보며 회식을 하는 문화가 많아지고 있다."),
        SECTION("aside", "알아두면 좋아요"),
        HEADING(4, "한국 직장인들은 일 년에 휴가를 며칠 정도 사용할까?"),
        PARAGRAPH("한국 직장인은 2018년 한 해 평균 15일의 유급 휴가(쉬면서도 임금을 받는 휴가)를 받아 이 중 "
          "14일을 사용한 것으로 조사되었다. 평균 사용 일수가 8일이던 2016년 보다 6일, 평균 10일이던 "
          "2017년보다 4일이 늘어났다. 이에 따라 조사 대상 국가 가운데 한국이 가장 높은 증가율을 보였다. "
          "이러한 결과는 일과 삶의 균형을 추구 하는 워라밸 문화 확산, 주 52시간 근로제 시행, 그리고 정부와 "
          "기업의 휴가 권장 분위기가 더해지면서 나타난 것으로 보인다."),
        SOURCE("(익스피디아, 2018, 국가별 유급 휴가 사용 현황, 한국경제 2018.11.25. 기사)"),
    ],
    annotations={
        "일터": dict(
            meaning="직장 / workplace",
        ),
        "취업난": dict(
            hanja="就業難",
            meaning="difficulty in finding employment / job market difficulty",
            characters=[("就業", None,
                "to get employed/take up a job (就 = to take up/assume, 業 = "
                "work/occupation)"), ("難", None,
                "difficulty/hardship (same 難 as in 어려움's hanja equivalent, "
                "곤란하다, 재난 \"disaster\")")],
        ),
        "은퇴": dict(
            hanja="隱退",
            meaning="retirement",
            characters=[("隱", None, "to hide/retreat/withdraw"), ("退", None,
                "to retreat/step back")],
        ),
        "자아실현": dict(
            hanja="自我實現",
            meaning="self-realization / self-actualization",
            characters=[("自我", None,
                "\"self/ego\" (自 = self, 我 = I/self — a doubled emphasis on "
                "\"self\")"), ("實現", None,
                "\"realization/actualization\" (實 = actual/real, 現 = "
                "appear/manifest) — \"to make something real/manifest\"")],
        ),
        "사회공헌": dict(
            hanja="社會貢獻",
            meaning="social contribution",
            characters=[("社會", None, "society"), ("貢獻", None,
                "contribution (貢 = tribute/offering, 獻 = to offer/present) "
                "— \"to offer something valuable\"")],
        ),
        "공기업": dict(
            hanja="公企業",
            meaning="state-owned/public enterprise",
            characters=[("公", None, "public"), ("企業", None,
                "enterprise/company (企 = to plan/undertake, 業 = "
                "business/work)")],
        ),
        "임금": dict(
            hanja="賃金",
            meaning="wage/pay",
            characters=[("賃", None,
                "to rent/hire (the same root idea as \"paying for labor,\" "
                "like renting someone's time/effort)"), ("金", None,
                "money/gold")],
        ),
        "초반": dict(
            meaning="early phase",
        ),
        "수명이": dict(
            headword="수명",
            hanja="壽命",
            meaning="lifespan / life expectancy",
            characters=[("壽", None,
                "long life/longevity (an old, somewhat literary character "
                "specifically about long life — appears in 장수 "
                "\"longevity,\" 만수무강 \"long life\" wishes)"), ("命", None,
                "life/fate/destiny (same 命 as in 생명 \"life,\" 운명 "
                "\"destiny\")")],
        ),
        "기혼": dict(
            hanja="旣婚",
            meaning="married",
            characters=[("旣", None, "already"), ("婚", None, "marriage")],
            notes=["(Opposite: 미혼 — 未婚, \"unmarried,\" 未 = not yet.)"],
        ),
        "점차": dict(
            hanja="漸次",
            meaning="gradually",
            characters=[("漸", None, "gradually/step-by-step"), ("次", None,
                "order/sequence")],
        ),
        "진출": dict(
            hanja="進出",
            meaning="advance into / entry into (a field/market/society)",
            characters=[("進", None, "to advance/enter"), ("出", None,
                "to go out/emerge")],
        ),
        "활발하다": dict(
            hanja="活潑하다",
            meaning="to be lively/active",
            characters=[("活", None,
                "alive/active (same 活 as in 생활 \"life/living,\" 활동 "
                "\"activity\")"), ("潑", None, "lively/vigorous")],
            surfaces=["활발해"],
        ),
        "완화하다": dict(
            hanja="緩和하다",
            meaning="to ease/alleviate/relax [something]",
            characters=[("緩", None, "slow/relaxed/loose"), ("和", None,
                "harmony/moderation")],
            surfaces=["완화"],
        ),
        "상당수": dict(
            hanja="相當數",
            meaning="a considerable/significant number",
            characters=[("相當", None, "considerable/quite a lot"), ("數", None,
                "number")],
        ),
        "양육": dict(
            hanja="養育",
            meaning="raising/rearing (a child) / childcare/upbringing",
            characters=[("養", None,
                "to nurture/raise/feed (same 養 as in 영양 \"nutrition,\" 양성 "
                "\"cultivation/training\")"), ("育", None,
                "to raise/educate/nurture (same 育 as in 교육 \"education,\" "
                "체육 \"physical education\")")],
            notes=["출산과 양육 문제로 직장을 그만두기도 하며 = \"[women] also quit their jobs "
                "due to issues of childbirth and childcare (양육)\"",
                "육아 — \"childcare/childrearing\" (育 = raise, 兒 = "
                "child/infant) — very commonly used interchangeably with 양육 "
                "in everyday speech, especially for the day-to-day, "
                "hands-on care of young children (기저귀 갈기, 젖 먹이기 등 — diaper "
                "changing, feeding, etc.)",
                "양육 — slightly more formal/broad, often used in legal, "
                "policy, or academic contexts (양육권 = custody rights, 양육비 = "
                "child support payments) — covers the whole process of "
                "raising a child to adulthood, not just the early hands-on "
                "years"],
        ),
        "단절": dict(
            hanja="斷絶",
            meaning="cutoff/severance/discontinuity",
            characters=[("斷", None, "to cut off"), ("絶", None,
                "to sever/terminate")],
        ),
        "시행하다": dict(
            hanja="施行하다",
            meaning="to implement/carry out/to enforce",
            characters=[("施", None, "to carry out/execute"), ("行", None,
                "to act/go")],
            notes=["교육 및 정책이 시행되고 있다 = \"education and policies are being "
                "implemented.\""],
            surfaces=["시행"],
        ),
        "대리운전기사": dict(
            meaning="\"designated/substitute driver\" (a driver you call to "
                "drive your car for you, typically when you've been "
                "drinking)",
            notes=["대리 — on behalf of / substitute / proxy", "운전 — driving",
                "기사 — technician/driver/engineer"],
        ),
        "겸업하다": dict(
            hanja="兼業하다",
            meaning="to hold a side job/do work on the side",
            characters=[("兼", None, "to combine/concurrently hold"), ("業", None
                , "work/occupation/business (same 業 you've seen in 산업 "
                "\"industry,\" 취업 \"employment,\" 기업 \"enterprise\")")],
            surfaces=["겸업"],
        ),
        "관공서": dict(
            hanja="官公署",
            meaning="government office / public agency",
            characters=[("官", None, "government official/office"), ("公", None,
                "public"), ("署", None, "office/bureau/department")],
        ),
        "탄력적": dict(
            hanja="彈力的",
            meaning="flexible/elastic",
        ),
        "교대": dict(
            hanja="交代",
            meaning="shift / taking turns / alternation",
        ),
        "명확하다": dict(
            hanja="明確하다",
            meaning="to be clear/definite/unambiguous",
            characters=[("明", None,
                "bright/clear (same 明 as in 설명 \"explanation,\" 분명하다 "
                "\"obvious/clear\")"), ("確", None,
                "certain/definite/firm (same 確 as in 확인 \"confirmation,\" "
                "확실하다 \"certain/sure\")")],
            surfaces=["명확하게"],
        ),
        "시간제": dict(
            meaning="time-based system / by-the-hour system",
        ),
    },
    chapterGlossary=["일터"],
    fixes=[
        ("회사 진원 들끼리", "회사 직원들끼리", "typo — 진원 for 직원, plus spacing"),
        ("도움을 중 국가기업", "도움을 줌", "typo — 중 for 줌; 국가기업 was a handwritten note "
                                    "beside 공기업 in the margin, not part of this definition (p. 25)"),
        ("사회공헌", "사회 공헌", "the margin glossary prints it as two words (p. 25)"),
        ("공공문체를", "공공문제를", "typo — 문체 for 문제 (p. 25)"),
        ("seciety", "society", "typo"),
        ("가치 를", "가치를", "spacing"),
        ("증진하기 위하 여", "증진하기 위하여", "spacing"),
        ("다소규모가", "다소 규모가", "spacing"),
        ("정부 가", "정부가", "spacing"),
        ("추구 하는", "추구하는", "spacing"),
        ("2016년 보다", "2016년보다", "the page itself is inconsistent here — 2016년 보다 "
                                 "beside 2017년보다 (p. 26); normalised to the closed form"),
    ],
    headwords={"활발해": "활발하다", "완화": "완화하다", "시행": "시행하다",
               "겸업": "겸업하다", "명확하게": "명확하다", "점차": "점차"},
    english={
        "직장 근무 시간과 근무 유형": dict(
            title="Working hours and kinds of work",
            paragraphs=[
                "Government offices and companies in Korea generally work from nine "
                "in the morning to six in the evening. There is about an hour for "
                "lunch around noon, so the working day comes to about eight hours. "
                "People usually leave at six, though where work is left over they may "
                "stay on and work outside hours. Even so, the total across the week "
                "has to be within 52 hours (as of 2020). Besides regular hours, with "
                "a fixed start and finish, some companies run flexible working time, "
                "where only the total to be worked over a set period is fixed and the "
                "time is left to be used efficiently.",

                "Most workplaces are on a five-day week, Monday to Friday, though "
                "where the nature of the work calls for weekends the days off fall on "
                "weekdays instead. Where service has to be provided around the clock "
                "— 찜질방, convenience stores and PC방 that never close, or police "
                "stations, fire stations, hospitals, harbours and airports — the staff "
                "take turns and work shifts.",
            ],
        ),
        "직장 문화": dict(
            title="The culture of the workplace",
            paragraphs=[
                "In Korea the staff of a company often eat together once work is "
                "done. Such a 회식 is usually held to build a close relationship among "
                "colleagues, or when a colleague has something to be congratulated or "
                "consoled for. On the day of a 회식 the eating and the talking can run "
                "late into the night.",

                "Lately, as a culture of seeking balance between work and life and of "
                "respecting what the individual wants has spread, 회식 have tended to "
                "become less frequent. And even where one is held, ways that everyone "
                "can join in are on the increase — a film, a performance or sport "
                "with colleagues in place of drink and a meal.",
            ],
        ),
    },
    append=[
        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 한국인은 어떤 일터에서 일할까?"),
        BULLET("취업을 준비하는 사람들 중에 안정적인 직업을 희망하는 사람은 (        )이 되거나 "
          "(        )에서 일하는 것을 선호하고, 임금이 높고 복지 혜택이 많은 (        )에 "
          "취직하기를 원하는 사람도 많다."),
        BULLET("(      )의 사회 진출이 활발해지면서 직업별 남녀 간 불균형도 조금씩 완화되고 있다."),
        BULLET("출산과 양육 등의 문제로 직장을 그만 두었다가 다시 일하기 원하는 여성들의 "
          "(        )과 창업을 지원하는 교육과 정책이 시행되고 있다."),
        HEADING(3, "02 한국인의 직장 생활은 어떤 모습일까?"),
        BULLET("일반적으로 한국의 직장에서는 월요일부터 금요일까지 하루에 8시간씩 주 (    )일 "
          "근무를 하고 필요한 경우에 한하여 일주일에 최대 (    )시간까지 일할 수 있다"
          "(2020년 기준)."),
        BULLET("서비스가 24시간 제공되어야 하는 곳에서 일하는 경우는 직원들이 서로 차례를 바꾸어 "
          "(        ) 근무를 한다."),
        BULLET("동료들끼리 친밀한 관계를 형성하기 위해서 또는 축하나 위로를 받아야 할 직장 동료가 "
          "있을 때 근무를 마친 후 회사 직원들끼리 (        )을 한다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "직장인 80% 이상 “회사생활에서는 ‘일’보다 ‘사람’이 더 중요”", translation=
          "Over 80% of employees: “at work, ‘people’ matter more than "
          "‘the job’”" "\n\n"
          "In a survey of office workers about ‘work and relationships "
          "within the workplace’, 81% of respondents answered that of ‘the "
          "job and the people’ it is ‘the people’ that weigh more heavily on "
          "leaving a company. Relationship stress (71.8%) was also found to "
          "be far worse than work-related stress (28.2%)." "\n\n"
          "As a way of resolving conflict, the commonest answer was ‘avoid "
          "it so that conflict does not arise if at all possible’ (59.6%, "
          "multiple answers allowed). Passive responses made up most of the "
          "rest — ‘bear it alone, inwardly’ (42.2%), ‘prepare to change jobs "
          "or resign’ (35.5%) — which appeared to be because the other party "
          "to the conflict is usually in a position senior to their own."),
        PARAGRAPH("직장인 대상으로 ‘일과 직장 내 인간관계’에 대해 조사를 실시한 결과 응답자의 81%는 "
          "‘일과 사람’ 중 {퇴사}(회사를 그만두는 것)에 더 영향을 끼치는 것은 ‘사람’이라고 "
          "답했다. 또 업무 관련 스트레스(28.2%)보다 인간관계 스트레스(71.8%)가 훨씬 심한 "
          "것으로 조사됐다."),
        PARAGRAPH("{갈등}을 해결하는 방법으로는 ‘가급적 갈등이 생기지 않도록 피한다’(59.6%, "
          "{복수응답})는 답변이 가장 많았다. 또한 ‘혼자 속으로만 참는다’(42.2%), "
          "‘{이직}이나 퇴사를 준비한다’(35.5%) 등의 {소극적}인 대응이 주를 이루었는데, "
          "이는 갈등의 대상이 주로 자신들보다 높은 {지위}에 있기 때문인 것으로 나타났다."),
        SOURCE("[출처] 사람인, 일과 직장 내 인간관계조사(2019); 동아경제(2019.03.02)"),
        PARAGRAPH("★ 한국에서 직장 생활을 하며 겪었던 인간관계 중 도움을 받았거나 힘들었던 경험을 "
          "이야기해 봅시다.",
          "Talk about a relationship at work in Korea that helped you, or "
          "that you found hard."),
    ],
    extraAnnotations={
        "경력 단절": dict(
            hanja="經歷斷絶", meaning="a career interrupted",
            characters=[("經", "경", "to pass through, undergo — as in 경험 “experience”, 경제"),
                         ("歷", "력", "to pass, history — as in 역사 “history”, 이력서 “résumé”"),
                         ("斷", "단", "to cut off"),
                         ("絶", "절", "to sever, terminate")],
            notes=["경력 is a working record; 단절 is its being cut. The page glosses it as the "
                   "state of having a gap between leaving one job and entering the next. "
                   "경력단절여성 is the standard policy term for women in that position."],
        ),
        "정책": dict(
            hanja="政策", meaning="policy",
            characters=[("政", "정", "government, rule — as in 정부 “government”, 정치 “politics”"),
                         ("策", "책", "plan, scheme — as in 대책 “countermeasure”, 방책")],
            notes=["A plan a government settles on to solve a public problem, which is how the "
                   "page glosses it: 공공문제를 해결하기 위해 정부가 결정한 일의 계획."],
        ),
        "추구": dict(
            hanja="追求", meaning="pursuit, the chasing after something",
            characters=[("追", "추", "to chase, follow — as in 추격 “chase”, 추적 “tracking”"),
                         ("求", "구", "to seek, ask for — as in 요구 “demand”, 구하다 “to seek”")],
            notes=["일과 삶의 균형을 추구하는 문화 = “a culture that pursues work–life balance”. "
                   "Takes 을/를 for what is pursued."],
        ),
        "경향": dict(
            hanja="傾向", meaning="a tendency, a trend",
            characters=[("傾", "경", "to lean, tilt — as in 경사 “slope”"),
                         ("向", "향", "direction, to face — as in 방향 “direction”, 향하다 “to face”")],
            notes=["Literally a leaning in some direction, which is the page's gloss: "
                   "현상이나 행동이 어떤 방향으로 기울어짐. Usually ~는 경향이 있다, “there is a "
                   "tendency to ~”."],
        ),
        "택배": dict(
            hanja="宅配", meaning="parcel delivery, courier service",
            characters=[("宅", "택", "house, home — as in 주택 “housing”, 자택"),
                        ("配", "배", "to distribute, deliver — as in 배송, 배달")],
            notes=["Literally “home delivery”. 택배 is the parcel or the service; "
                   "택배 기사 is the driver."],
        ),
        "야근": dict(
            hanja="夜勤", meaning="working late, night duty",
            characters=[("夜", "야", "night — as in 야식 “late-night snack”, 심야"),
                        ("勤", "근", "to work, duty — as in 근무, 출근, 퇴근")],
            notes=["Staying past normal hours, which the passage on p. 26 describes as "
                   "시간 외 근무를 하기도 한다."],
        ),
        "회식": dict(
            hanja="會食", meaning="a company dinner, eating together as a team",
            characters=[("會", "회", "to gather, meeting — as in 회사, 회의"),
                        ("食", "식", "to eat, food — the same 食 as in 식구 “household”")],
            notes=["A workplace institution rather than just a meal out; 직장 문화 on "
                   "p. 26 is largely about it."],
        ),
        "퇴사": dict(
            hanja="退社", meaning="leaving a company, resigning",
            characters=[("退", "퇴", "to retreat, withdraw — the same 退 as in 은퇴 “retirement”"),
                        ("社", "사", "company, society — as in 회사, 입사")],
            notes=["The page glosses it in line: 퇴사(회사를 그만두는 것). "
                   "입사하다 is the opposite — to join a company."],
        ),
        "갈등": dict(
            hanja="葛藤", meaning="conflict, discord",
            characters=[("葛", "갈", "arrowroot vine"),
                        ("藤", "등", "wisteria vine")],
            notes=["Literally two climbing vines tangled around each other — the image "
                   "behind the word is knotted growth that cannot be pulled apart.",
                   "갈등을 해결하는 방법으로는 = “as for ways of resolving conflict”."],
        ),
        "복수응답": dict(
            hanja="複數應答", meaning="multiple answers permitted",
            characters=[("複", "복", "double, multiple — as in 복사 “copy”, 복잡하다 “complicated”"),
                        ("數", "수", "number — as in 촌수, 상당수"),
                        ("應", "응", "to respond — as in 응답, 반응"),
                        ("答", "답", "answer — as in 대답, 정답")],
            notes=["Survey shorthand: respondents could choose more than one option, "
                   "which is why the percentages in this paragraph add up to well over 100."],
        ),
        "이직": dict(
            hanja="移職", meaning="changing jobs, moving to another employer",
            characters=[("移", "이", "to move, shift — as in 이사 “moving house”, 이민 “emigration”"),
                        ("職", "직", "post, occupation — as in 직장, 직업, 취직")],
            notes=["Distinct from 퇴사, which is only about leaving; 이직 implies moving on "
                   "to somewhere else."],
        ),
        "소극적": dict(
            hanja="消極的", meaning="passive, unassertive",
            characters=[("消", "소", "to extinguish, dissipate — as in 소비 “consumption”"),
                        ("極", "극", "pole, extreme — as in 태극, 극단적"),
                        ("的", "적", "-ic, -al: makes an adjective — as in 탄력적, 안정적")],
            notes=["The opposite is 적극적 (積極的), “active, proactive”. Here the survey "
                   "calls avoiding and enduring conflict 소극적인 대응 — a passive response."],
        ),
        "지위": dict(
            hanja="地位", meaning="position, standing, status",
            characters=[("地", "지", "ground, place — as in 지역, 지방"),
                        ("位", "위", "place, rank — as in 순위 “ranking”, 1위")],
            notes=["Social or organisational standing rather than physical position: "
                   "자신들보다 높은 지위에 있다 = “to be in a position above one's own”."],
        ),
    },
    # every correction below has been read against the photos of pp. 24-27
    approved={
        "가치 를", "사회공헌", "seciety", "도움을 중 국가기업", "증진하기 위하 여",
        "다소규모가", "공공문체를", "정부 가", "회사 진원 들끼리", "추구 하는",
        "2016년 보다",
    },
    # Checked and accepted, so not reported: 주요 내용정리 and 이야기 나누기 are
    # missing from the Google Doc, which stops after the 휴가 box on p. 26, and
    # both were transcribed from the photos of p. 27.
    extraNotes=[
        "The 남녀 경제 활동 참가율 figure needs better formatting: the page has a line chart "
        "of two series over time, and drawing it as one bar per year does not reflect the "
        "original well.",
    ],
)
