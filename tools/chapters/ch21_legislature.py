# -*- coding: utf-8 -*-
"""Chapter 21 — The legislature.

No Google Doc: yours stop at chapter 12. Transcribed from the photos of
pp. 114-117, so the Korean here is my reading of the page rather than yours,
and any error in it is mine.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, TABLE,
               CELL, GLOSSARY)

CHAPTER = dict(
    number=21, slug="21-legislature",
    unit="정치", title="입법부", titleEn="The legislature",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 한국에서 생활하는 외국인에 대한 {대우}를 {규정}해 놓은 "
          "‘{재한외국인 처우 기본법}’의 일부 내용을 쉽게 풀어쓴 것입니다."),
        HEADING(3, "재한외국인 처우 기본법"),
        BULLET("제1조 (목적) 이 법은 한국에서 생활하는 외국인이 받게 되는 대우 등에 관한 내용을 정해 "
          "놓았다. 이를 통해 외국인이 한국 사회에 적응하여 자신의 능력을 충분히 {발휘}할 수 "
          "있도록 하고, 한국 국민과 외국인이 서로를 이해하고 존중하는 환경을 만들어 한국의 발전과 "
          "사회 통합에 {이바지하는|이바지하다} 것을 목적으로 한다."),
        BULLET("제10조 (한국에서 생활하는 외국인의 {인권} 보호) 국가와 지방자치단체는 한국에서 "
          "생활하는 외국인 또는 그 자녀에 대한 {불합리한|불합리하다} 차별을 막고 인권 보호를 "
          "위한 교육 등을 위해 노력해야 한다."),
        BULLET("제11조 (한국에서 생활하는 외국인의 {사회적응} 지원) 국가와 지방자치단체는 외국인이 "
          "한국에서 생활하는 데 필요한 기본적인 지식에 관한 교육, 정보 제공, 상담 등을 지원할 수 "
          "있다."),
        HEADING(4, "01 이 법은 한국에서 생활하는 외국인에게 어떤 도움을 줄 수 있는지 왼쪽에 제시된 법 "
             "{조항}에서 그 {구체적}인 내용을 찾아볼까요?"),
        HEADING(4, "02 왼쪽과 같은 내용을 법으로 만들어 놓은 이유는 무엇입니까?"),

        SECTION("goals", "학습목표"),
        BULLET("입법부의 의미와 국회의 구성을 설명할 수 있다.", ordered=True),
        BULLET("국회가 하는 일을 설명할 수 있다.", ordered=True),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", 2), "제목", "관련 내용"],
              [["기본", "정치", "20. 한국의 민주 정치", "권력 분립"],
               ["심화", "정치", "9. 정치 과정과 시민 참여", "정치 과정"]]),

        SECTION("part", "01 법은 누가, 어디서 만들까?"),
        HEADING(2, "국회라고 불리는 입법부"),
        GLOSSARY(("득표율", "전체 투표수에서 찬성표를 얻은 비율", "득표율"),
              ("출마", "선거에 후보로 나섬", "출마"),
              ("당선", "선거에서 뽑힘", "당선")),
        PARAGRAPH("민주주의 국가에서는 국민이 선거를 통해 뽑은 대표를 중심으로 국가의 일을 결정하고 있다. "
          "국민의 대표가 모여서 나라의 중요한 일을 {논의}하고 그와 관련한 법을 만들거나 고치는 "
          "{기관}을 {입법부}라고 한다. ‘{입법}’은 ‘법을 세운다.’, ‘법을 만든다.’는 의미이다. "
          "한국에서는 입법부를 {국회}라고 부른다."),

        HEADING(2, "국회의 구성"),
        GLOSSARY(("단원제", "입법부가 한 개만 존재하는 방식. 상원과 하원 두 개가 있으면 양원제라고 "
                        "부름", "단원제")),
        PARAGRAPH("국회는 4년에 한 번씩 실시되는 {국회의원} {총선거}(총선)를 통해 {선출}된 국회의원으로 "
          "{구성}된다. 국회의원은 각 지역의 대표인 {지역구} 의원과 각 {정당}의 {득표율}에 따라 "
          "선출되는 {비례대표} 의원이 있다. 각 지역구에서는 {출마}한 {후보자} 중 가장 많은 표를 "
          "얻은 사람 1명이 {당선}되고, 비례대표는 정당 투표를 통해 얻은 득표율에 따라 "
          "{당선자}가 {가려진다|가려지다}. 국회의원 수는 헌법과 {법률}에 따라 결정되는데 2020년 "
          "기준으로는 300명이다. 한국 국회는 {상원}, {하원}의 구분이 없는 {단원제} 방식을 "
          "선택하고 있다."),
        FIGURE("국회의사당 회의 모습"),
        FIGURE("국회의사당 전경"),

        HEADING(2, "국회의원의 특권과 의무"),
        GLOSSARY(("특권", "특별히 주어지는 권리", "특권"),
              ("회기", "국회가 활동할 수 있는 일정한 기간", "회기"),
              ("고위 공직자", "국가의 일을 맡은 사람들 중에 중요하고 높은 관직에 있는 사람",
               "고위 공직자"),
              ("청렴", "성품과 행실이 바르고, 뇌물을 받지 않는 등 재물 욕심이 없음", "청렴")),
        PARAGRAPH("국회의원이 국가의 중요한 법을 만들거나 행정부, 사법부 등 다른 국가 기관을 견제하는 "
          "과정에서 {부당한|부당하다} {압력}을 받아서는 안 된다. 이를 위해 국회의원에게는 "
          "{특권}이 주어지기도 한다. 예를 들어 국회의원은 국회가 열리고 있는 {회기} 중에는 "
          "국회의 {동의} 없이 {체포}되지 않는다. 이를 {불체포 특권}이라고 한다."),
        PARAGRAPH("국회의원이 이러한 특권을 {누리는|누리다} 만큼 따라야 할 의무도 있다. 국회의원은 "
          "{고위 공직자}로서 {청렴}해야 하고 개인보다 나라의 이익을 먼저 생각해야 한다. 또한, "
          "자신의 높은 지위를 이용해서 {부정한|부정하다} 방법으로 재산을 모으지 않도록 재산을 "
          "{공개}해야 한다."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "총선에는 투표 용지가 2장!"),
        PARAGRAPH("국회의원을 뽑는 선거를 {총선}이라고 한다. 총선에 참여하는 {유권자}는 {투표소}에 가서 "
          "두 번 투표하게 된다. 한 장은 자신이 살고 있는 지역의 대표 후보자에게, 다른 한 장은 "
          "본인이 {지지}하는 정당에 투표한다."),
        TABLE(["정당", "지역구", "비례대표", "계"],
              [["더불어민주당", "161", "13", "174"],
               ["국민의힘", "84", "19", "103"],
               ["정의당", "1", "5", "6"],
               ["국민의당", "0", "3", "3"],
               ["열린민주당", "0", "3", "3"],
               ["기본소득당", "0", "1", "1"],
               ["시대전환", "0", "1", "1"],
               ["무소속", "7", "2", "9"],
               ["계", "253", "47", "300"]]),
        FIGURE("정당별 국회의원 의석수(2020년 11월)"),

        SECTION("part", "02 국회는 어떤 일을 할까?"),
        HEADING(2, "입법에 관한 일"),
        GLOSSARY(("법안", "법률로 만들어지기 전 단계의 초안", "법안"),
              ("재적", "어떤 조직이나 단체에 소속되어 있는 상태", "재적"),
              ("과반수", "전체의 절반이 넘는 수", "과반수"),
              ("법안 통과", "법안이 의회(국회)에서 승인되는 것", "법안 통과")),
        PARAGRAPH("법을 만드는 것(입법)은 국회의 가장 기본적인 일이다. 국회의원 10명 이상이 함께 "
          "{법안}을 {제출}하면 새로운 법을 만들거나 고치는 일이 시작된다. 국회 {재적}의원의 "
          "{과반수}가 {출석}하고 그중 과반수가 {찬성}하면 법안이 {통과}되어 법이 만들어진다. "
          "국회 재적 의원의 수가 300명이라면 151명 이상이 국회에 출석해야 법안 통과를 위한 "
          "투표를 실시할 수 있다. 만약 국회의원 200명이 국회에 출석해서 투표했다면 101명 이상이 "
          "법안에 찬성해야 법안이 통과된다."),
        FIGURE("국회 법안 제출 모습"),

        HEADING(2, "국가 재정(살림)에 관한 일"),
        GLOSSARY(("재정", "경제적 활동이나 상태", "재정"),
              ("예산", "예상되는 수입과 비용", "예산"),
              ("검토", "사실이나 내용을 따져봄", "검토")),
        PARAGRAPH("국회는 나라의 {살림}에 필요한 {예산}을 {확정}하는 일을 한다. 정부가 1년 동안 나라를 "
          "이끌어 가는 데 쓸 돈에 대한 계획({예산안})을 {짜서|짜다} 국회에 제출하면 국회는 "
          "그것이 {적절한지|적절하다} 살펴본다. 만약 {건설} 분야에 너무 많은 예산이 "
          "{배정}되었다고 판단되면 그와 관련한 예산을 줄이기도 하고, 교육 분야에 더 많은 돈이 "
          "필요하다고 판단되면 교육 예산을 늘리기도 한다. 정부의 예산은 국민이 낸 {세금}으로 "
          "{마련}되기 때문에 국민의 대표인 국회의원이 이를 {검토}하고 확정하는 것이다."),

        HEADING(2, "국정에 관한 일"),
        PARAGRAPH("국회는 정부가 법에 따라 일을 잘하고 있는지 확인하기 위해 {국정 감사}를 실시한다. 국정 "
          "감사는 매년 9월~11월 사이에 기간을 정해 약 20일 정도 실시된다. 국회의원은 "
          "{나랏일}을 맡은 사람들에게 궁금한 점을 질문하고, 잘못한 일이 있으면 "
          "{바로잡도록|바로잡다} 요구한다. 국정 감사는 국회가 정부를 견제하고 {감시}할 수 있는 "
          "중요한 역할을 한다."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "나라의 중요한 일을 맡으려면 먼저 국회 인사청문회부터!"),
        PARAGRAPH("{청문회}는 나라의 중요한 일과 관련하여 국회가 {당사자}(직접 관련된 사람)나 {증인}, "
          "{참고인} 등에게 질문하고 사실이나 의견을 듣는 제도이다. {인사청문회}는 {대법원장}, "
          "{국무총리}, {장관} 등과 같은 고위 공직자가 되고자 하는 사람들({후보자})에 대해 "
          "실시하는 것이다. 국회는 후보자가 그 자리에 적합한 능력과 {도덕성}을 갖추고 있는지에 "
          "관한 질문하고 {답변}을 듣는다. 인사청문회가 끝난 뒤, 국회는 후보자 {임명}에 대해 동의 "
          "또는 반대투표를 하거나 {적격} 혹은 {부적격} 의견을 정부에 제출한다."),
        FIGURE("인사 청문회 모습"),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 법은 누가, 어디서 만들까?"),
        BULLET("국민의 대표가 모여서 나라의 중요한 일을 논의하고 관련된 법을 만드는 곳을 "
          "( 입법부 )라고 한다."),
        BULLET("국민의 대표인 (        )은 지역구 의원과 비례대표 의원으로 구성된다."),
        BULLET("2020년 기준으로 한국 국회의원의 수는 ( 300 )명이다."),
        HEADING(3, "02 국회는 어떤 일을 할까?"),
        BULLET("( 법 )을 만드는 것은 국회의 가장 기본적인 일이다."),
        BULLET("국회는 나라의 살림에 필요한 ( 예산 )을 확정하는 일을 한다."),
        BULLET("국회에서는 정부가 법에 따라 일을 잘하고 있는지 확인하기 위해 ( 감사 )를 실시한다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "나의 의견도 법에 반영될 수 있다", translation=
          "My opinion too can be reflected in the law" "\n\n"
          "“Abolish the ‘payment after departure’ rule for migrant workers’ "
          "severance pay”" "\n\n"
          "It has been pointed out that because of the ‘severance pay on "
          "departure’ rule, migrant workers often have difficulty receiving "
          "their severance pay. The Joint Committee with Migrants in Korea, "
          "the Joint Action for Abolishing Discrimination against Migrant "
          "Workers and Realising Human and Labour Rights, and the Solidarity "
          "for Migrants’ Human Rights made this case at a briefing on their "
          "survey of how the post-departure severance pay system works in "
          "practice."),
        PARAGRAPH("“이주민 근로자 {퇴직금} ‘{출국} 후 {수령제}’ {폐지}를”"),
        PARAGRAPH("‘퇴직금 출국 후 수령제’ 때문에 이주민 근로자들이 퇴직금을 받는 데 어려움을 겪는 일이 "
          "많다는 {지적}이 나왔다. ‘외국인 이주·노동운동협의회’, ‘이주노동자 {차별철폐}와 "
          "인권·{노동권} 실현을 위한 {공동행동}’, ‘이주인권연대’는 ‘이주노동자 출국 후 퇴직금 "
          "수령제도 {실태조사} {발표회}’를 열어 이런 {주장}을 {폈다|펴다}."),
        FIGURE("국가인권위원회에서 열린 ‘이주민 근로자 출국 후 퇴직금 수령제도 실태조사 발표회’ "
            "(사진 출처: 〈연합뉴스〉)"),
        SOURCE("[출처] 한겨레(2019.08.12)"),
        PARAGRAPH("★ 자신의 생활, 일, 공부 등과 관련하여 제안하고 싶은 법이 있다면 그 내용을 이야기해 "
          "봅시다.",
          "If there is a law you would like to propose to do with your life, "
          "your work or your studies, talk about what it would say."),
    ],

    english={
        "국회라고 불리는 입법부": dict(
            title="The legislature, called the National Assembly",
            paragraphs=[
                "In a democracy the affairs of state are decided around the "
                "representatives the people have elected. The body in which "
                "those representatives gather to debate the important affairs "
                "of the country, and to make or amend the laws that go with "
                "them, is the legislature. 입법 means to set up a law, to make "
                "a law. In Korea the legislature is called the 국회.",
            ],
        ),
        "국회의 구성": dict(
            title="How the Assembly is made up",
            paragraphs=[
                "The Assembly is made up of members elected in a general "
                "election held once every four years. Its members are of two "
                "kinds: constituency members, who represent a particular "
                "area, and proportional members, elected according to each "
                "party's share of the vote. In each constituency the one "
                "candidate who stood and won the most votes is elected; the "
                "proportional members are settled by each party's share in "
                "the party vote. The number of members is fixed by the "
                "constitution and by statute, and stood at 300 as of 2020. "
                "The Korean Assembly has chosen a single chamber, with no "
                "division into upper and lower houses.",
            ],
        ),
        "국회의원의 특권과 의무": dict(
            title="A member's privileges and duties",
            paragraphs=[
                "A member of the Assembly must not come under improper "
                "pressure while making the important laws of the state or "
                "checking the other organs of state, the executive and the "
                "judiciary. Certain privileges are granted for that reason. "
                "A member may not be arrested without the Assembly's consent "
                "while it is in session, for instance. This is called the "
                "privilege of freedom from arrest.",

                "For as much as a member enjoys such privileges, there are "
                "duties to follow as well. As a senior public official a "
                "member must be of clean hands, and must put the country's "
                "interest before their own. They must also declare their "
                "assets, so as not to gather wealth by improper means through "
                "the high position they hold.",
            ],
        ),
        "입법에 관한 일": dict(
            title="Its work on legislation",
            paragraphs=[
                "Making law is the most basic of the Assembly's work. Ten or "
                "more members submitting a bill together begins the making or "
                "amending of a law. If a majority of the members on the roll "
                "attend and a majority of those present are in favour, the "
                "bill passes and becomes law. Where the Assembly has 300 "
                "members on its roll, 151 or more must attend before a vote "
                "on passing a bill may be held. If 200 members attended and "
                "voted, 101 or more must be in favour for the bill to pass.",
            ],
        ),
        "국가 재정(살림)에 관한 일": dict(
            title="Its work on the national finances",
            paragraphs=[
                "The Assembly settles the budget the country's housekeeping "
                "needs. The government draws up a plan for the money it will "
                "spend on running the country over the year and submits it to "
                "the Assembly, which considers whether it is appropriate. If "
                "it judges too much to have been allocated to construction it "
                "may cut the relevant sum; if it judges education to need "
                "more it may raise the education budget. Because the "
                "government's budget is found from the taxes the people pay, "
                "it is the members, as the people's representatives, who "
                "examine and settle it.",
            ],
        ),
        "국정에 관한 일": dict(
            title="Its work on the affairs of state",
            paragraphs=[
                "The Assembly holds a state audit to check that the "
                "government is doing its work according to law. The audit "
                "runs for about twenty days in a period set between September "
                "and November each year. Members put their questions to those "
                "charged with the affairs of the country, and where something "
                "has gone wrong they demand that it be put right. The state "
                "audit serves an important part in letting the Assembly check "
                "the government and keep watch over it.",
            ],
        ),
    },

    extraAnnotations={
        "입법부": dict(
            hanja="立法部", meaning="the legislature",
            characters=[("立", "립", "to establish — as in 설립, 독립"),
                        ("法", "법", "law — as in 헌법, 법원"),
                        ("部", "부", "branch, ministry — as in 행정부, 법무부")],
        ),
        "입법": dict(hanja="立法", meaning="legislation, law-making"),
        "국회": dict(
            hanja="國會", meaning="the National Assembly",
            characters=[("國", "국", "country — as in 국가, 국민"),
                        ("會", "회", "assembly — as in 회의, 사회")],
        ),
        "대우": dict(
            hanja="待遇", meaning="treatment, how one is dealt with",
            characters=[("待", "대", "to wait, to treat — as in 기대, 초대"),
                        ("遇", "우", "to meet, to encounter")],
        ),
        "규정": dict(
            hanja="規定", meaning="to lay down, to stipulate",
            characters=[("規", "규", "rule — as in 규칙, 규제"),
                        ("定", "정", "to fix — as in 지정, 확정")],
        ),
        "재한외국인 처우 기본법": dict(
            hanja="在韓外國人處遇基本法",
            meaning="the Framework Act on the Treatment of Foreigners Residing in Korea",
            characters=[("在", "재", "to reside at — as in 재외국민, 현재"),
                        ("處", "처", "to deal with — as in 처리, 부처"),
                        ("遇", "우", "to treat — the same 遇 as in 대우")],
            notes=["Enacted 2007. The law the KIIP itself rests on: article "
                   "11 is what funds the social adaptation support this "
                   "course is part of."],
        ),
        "발휘": dict(
            hanja="發揮", meaning="to display, to bring out (an ability)",
            characters=[("發", "발", "to issue forth — as in 발달, 발견"),
                        ("揮", "휘", "to wield, to brandish")],
        ),
        "이바지하다": dict(meaning="to contribute to"),
        "인권": dict(
            hanja="人權", meaning="human rights",
            characters=[("人", "인", "person — as in 인구, 개인"),
                        ("權", "권", "right — as in 권리, 권익")],
        ),
        "불합리하다": dict(
            hanja="不合理하다", meaning="to be unreasonable",
            characters=[("合", "합", "to fit — as in 적합하다, 통합"),
                        ("理", "리", "reason — as in 원리, 관리")],
            notes=["Its opposite is 합리적, chapter 25's word."],
        ),
        "사회적응": dict(hanja="社會適應", meaning="social adaptation"),
        "조항": dict(
            hanja="條項", meaning="an article, a clause",
            characters=[("條", "조", "article, item — as in 제1조's 조"),
                        ("項", "항", "item, term — as in 항목")],
        ),
        "구체적": dict(
            hanja="具體的", meaning="concrete, specific",
            characters=[("具", "구", "tool, to be equipped — as in 도구, 구비"),
                        ("體", "체", "body — as in 단체, 전체")],
            notes=["Its opposite is 추상적, abstract."],
        ),
        "논의": dict(
            hanja="論議", meaning="discussion",
            characters=[("論", "론", "to argue — as in 토론, 의논"),
                        ("議", "의", "to deliberate — as in 회의, 의견")],
        ),
        "기관": dict(
            hanja="機關", meaning="an organ, an institution",
            characters=[("機", "기", "machine, workings — as in 기능, 계기"),
                        ("關", "관", "to relate — as in 관계, 관련")],
        ),
        "국회의원": dict(
            hanja="國會議員", meaning="a member of the National Assembly",
            characters=[("員", "원", "member — as in 공무원, 구성원")],
        ),
        "총선거": dict(
            hanja="總選擧", meaning="a general election",
            characters=[("總", "총", "whole, general — as in 총리, 총인구")],
            notes=["Shortened to 총선. Held every four years for the whole "
                   "Assembly at once."],
        ),
        "총선": dict(hanja="總選", meaning="the general election"),
        "선출": dict(
            hanja="選出", meaning="to elect",
            characters=[("選", "선", "to choose — as in 선거, 선발"),
                        ("出", "출", "to come out — as in 출석, 제출")],
        ),
        "구성": dict(
            hanja="構成", meaning="composition, to be made up of",
            characters=[("構", "구", "to construct — as in 구조, 구성원")],
        ),
        "지역구": dict(
            hanja="地域區", meaning="an electoral constituency",
            characters=[("區", "구", "district, ward — as in 구청, 지구")],
            notes=["253 of the 300 seats. The other 47 are 비례대표."],
        ),
        "정당": dict(
            hanja="政黨", meaning="a political party",
            characters=[("政", "정", "government — as in 정치, 정부"),
                        ("黨", "당", "party, faction — as in 여당, 야당")],
        ),
        "득표율": dict(
            hanja="得票率", meaning="share of the vote",
            characters=[("得", "득", "to obtain — as in 소득, 취득"),
                        ("票", "표", "a vote, a ticket — as in 투표, 개표"),
                        ("率", "률", "rate — as in 비율, 진학률")],
        ),
        "비례대표": dict(
            hanja="比例代表", meaning="a proportional representative",
            characters=[("比", "비", "to compare — as in 비율, 비중"),
                        ("例", "례", "example, precedent — as in 사례, 예를 들어"),
                        ("代", "대", "to represent, generation — as in 대표, 시대")],
            notes=["Elected from a party list in proportion to the party "
                   "vote, rather than for a place."],
        ),
        "출마": dict(
            hanja="出馬", meaning="to stand for election",
            characters=[("出", "출", "to go out — as in 출석, 진출"),
                        ("馬", "마", "horse — as in 경마 “horse racing”")],
            notes=["Literally “to ride out” — an old military figure for "
                   "entering the field."],
        ),
        "후보자": dict(
            hanja="候補者", meaning="a candidate",
            characters=[("候", "후", "season, to await — as in 기후"),
                        ("補", "보", "to supplement — as in 보완, 보충")],
        ),
        "당선": dict(
            hanja="當選", meaning="to be elected",
            characters=[("當", "당", "to hit, to be the case — as in 해당, 담당"),
                        ("選", "선", "to choose — as in 선거, 선출")],
            notes=["낙선 is the opposite — to lose an election."],
        ),
        "당선자": dict(hanja="當選者", meaning="the person elected"),
        "가려지다": dict(
            meaning="to be decided between, to be sorted out",
            notes=["From 가리다 “to distinguish, to pick out”. 승자가 가려지다 "
                   "“the winner is decided”."],
        ),
        "법률": dict(
            hanja="法律", meaning="a statute, law",
            characters=[("律", "률", "law, rule — as in 규율, 자율")],
        ),
        "상원": dict(hanja="上院", meaning="an upper house"),
        "하원": dict(hanja="下院", meaning="a lower house"),
        "단원제": dict(
            hanja="單院制", meaning="a unicameral system",
            characters=[("單", "단", "single — as in 단독, 단체"),
                        ("院", "원", "house, institution — as in 법원, 병원"),
                        ("制", "제", "system — as in 제도, 직선제")],
            notes=["Korea has one chamber. 양원제 is the two-chamber system."],
        ),
        "부당하다": dict(
            hanja="不當하다", meaning="to be improper, unjust",
            characters=[("當", "당", "fitting — as in 해당, 당선")],
        ),
        "압력": dict(
            hanja="壓力", meaning="pressure",
            characters=[("壓", "압", "to press — as in 억압당하다"),
                        ("力", "력", "force — as in 권력, 능력")],
        ),
        "특권": dict(
            hanja="特權", meaning="a privilege",
            characters=[("特", "특", "special — as in 특정, 특징"),
                        ("權", "권", "right — as in 권리, 인권")],
        ),
        "회기": dict(
            hanja="會期", meaning="a session",
            characters=[("會", "회", "assembly — as in 국회, 회의"),
                        ("期", "기", "period — as in 기간, 학기")],
        ),
        "동의": dict(
            hanja="同意", meaning="consent",
            characters=[("同", "동", "same — as in 동일, 동문회"),
                        ("意", "의", "intention — as in 의견, 의미")],
        ),
        "체포": dict(
            hanja="逮捕", meaning="arrest",
            characters=[("逮", "체", "to seize, to reach"),
                        ("捕", "포", "to catch — as in 포착 “to capture”")],
        ),
        "불체포 특권": dict(
            hanja="不逮捕特權", meaning="the privilege of freedom from arrest",
            notes=["A member may not be arrested while the Assembly sits, "
                   "unless the Assembly consents. Meant to stop the executive "
                   "silencing the legislature."],
        ),
        "누리다": dict(meaning="to enjoy, to have the benefit of"),
        "고위 공직자": dict(
            hanja="高位公職者", meaning="a senior public official",
            characters=[("職", "직", "office, post — as in 직업, 대통령직")],
        ),
        "청렴": dict(
            hanja="淸廉", meaning="integrity, clean hands",
            characters=[("淸", "청", "clear, pure — as in 청소 “cleaning”"),
                        ("廉", "렴", "upright, frugal")],
        ),
        "부정하다": dict(
            hanja="不正하다", meaning="to be corrupt, improper",
            characters=[("正", "정", "correct — as in 정식, 부정 선거")],
        ),
        "공개": dict(
            hanja="公開", meaning="disclosure, to make public",
            characters=[("公", "공", "public — as in 공적, 공무원"),
                        ("開", "개", "to open — as in 개방, 개봉")],
        ),
        "유권자": dict(
            hanja="有權者", meaning="an eligible voter",
            characters=[("有", "유", "to have — as in 고유, 유일하다"),
                        ("權", "권", "right — as in 권리, 특권")],
            notes=["Literally “one who has the right” — the right to vote."],
        ),
        "투표소": dict(
            hanja="投票所", meaning="a polling station",
            characters=[("投", "투", "to throw, to cast — as in 투자 “investment”"),
                        ("所", "소", "place — as in 장소, 산소")],
        ),
        "지지": dict(
            hanja="支持", meaning="support, backing",
            characters=[("支", "지", "to support, a branch — as in 지원, 지출"),
                        ("持", "지", "to hold — as in 유지, 지속적")],
        ),
        "법안": dict(
            hanja="法案", meaning="a bill",
            characters=[("案", "안", "a plan, a draft — as in 예산안, 방안")],
        ),
        "제출": dict(
            hanja="提出", meaning="to submit",
            characters=[("提", "제", "to raise, to present — as in 제시, 제공"),
                        ("出", "출", "to put out — as in 출석, 수출")],
        ),
        "재적": dict(
            hanja="在籍", meaning="being on the roll",
            characters=[("在", "재", "to be at — as in 현재, 재한외국인"),
                        ("籍", "적", "register — as in 국적, 호적")],
            notes=["재적 의원 means every member on the books, whether present "
                   "or not — the number a quorum is measured against."],
        ),
        "과반수": dict(
            hanja="過半數", meaning="a majority, more than half",
            characters=[("過", "과", "to pass, excess — as in 과거, 통과"),
                        ("半", "반", "half — as in 반달, 후반"),
                        ("數", "수", "number — as in 횟수, 수십")],
        ),
        "출석": dict(
            hanja="出席", meaning="attendance",
            characters=[("席", "석", "seat — as in 좌석, 결석")],
            notes=["Its opposite is 결석, chapter 10's word."],
        ),
        "찬성": dict(
            hanja="贊成", meaning="assent, being in favour",
            characters=[("贊", "찬", "to approve, to assist"),
                        ("成", "성", "to accomplish — as in 성장, 구성")],
            notes=["Its opposite is 반대. 찬반 토론 “a for-and-against debate” "
                   "opens chapter 20."],
        ),
        "통과": dict(
            hanja="通過", meaning="passage, to pass",
            characters=[("通", "통", "to pass through — as in 교통, 통신"),
                        ("過", "과", "to pass — as in 과반수, 과정")],
        ),
        "법안 통과": dict(hanja="法案通過", meaning="the passing of a bill"),
        "살림": dict(
            meaning="housekeeping, running a household",
            notes=["The book glosses 재정 with it: the state's finances "
                   "thought of as the country's housekeeping."],
        ),
        "재정": dict(
            hanja="財政", meaning="finances",
            characters=[("財", "재", "wealth — as in 재산, 문화재"),
                        ("政", "정", "government — as in 정치, 행정")],
        ),
        "예산": dict(
            hanja="豫算", meaning="a budget",
            characters=[("豫", "예", "beforehand — as in 예상, 예방"),
                        ("算", "산", "to reckon — as in 계산 “calculation”")],
        ),
        "예산안": dict(hanja="豫算案", meaning="a budget bill, a draft budget"),
        "확정": dict(
            hanja="確定", meaning="to settle, to finalise",
            characters=[("確", "확", "certain — as in 확인, 확실"),
                        ("定", "정", "to fix — as in 지정, 규정")],
        ),
        "짜다": dict(
            meaning="to draw up, to put together (a plan); to be salty",
            notes=["계획을 짜다, 예산을 짜다 — of assembling something out of "
                   "parts. A separate 짜다 means salty."],
        ),
        "적절하다": dict(
            hanja="適切하다", meaning="to be appropriate",
            characters=[("適", "적", "suitable — as in 적합하다, 적용"),
                        ("切", "절", "to cut, earnest — as in 친절 “kindness”")],
        ),
        "건설": dict(
            hanja="建設", meaning="construction",
            characters=[("建", "건", "to build — as in 건물 “building”, 건의"),
                        ("設", "설", "to establish — as in 시설, 설립")],
        ),
        "배정": dict(
            hanja="配定", meaning="allocation",
            characters=[("配", "배", "to distribute — as in 배려, 배달")],
            notes=["Chapter 10's 배정 — being assigned to a school — is the "
                   "same word."],
        ),
        "세금": dict(
            hanja="稅金", meaning="tax",
            characters=[("稅", "세", "tax — as in 세무 “tax affairs”"),
                        ("金", "금", "money, gold — as in 요금, 축의금")],
        ),
        "마련": dict(meaning="to arrange, to provide for"),
        "검토": dict(
            hanja="檢討", meaning="examination, review",
            characters=[("檢", "검", "to inspect — as in 검사, 검색"),
                        ("討", "토", "to discuss, to attack — as in 토론")],
        ),
        "국정 감사": dict(
            hanja="國政監査", meaning="the state audit",
            characters=[("監", "감", "to oversee — as in 감독, 감시"),
                        ("査", "사", "to investigate — as in 조사, 검사")],
            notes=["Twenty days each autumn in which the Assembly questions "
                   "the government on how it has run the country."],
        ),
        "나랏일": dict(
            meaning="the affairs of the country",
            notes=["나라 + 일, with the ㅅ of the compound. The plain Korean "
                   "for 국정."],
        ),
        "바로잡다": dict(meaning="to put right, to correct"),
        "감시": dict(
            hanja="監視", meaning="surveillance, keeping watch",
            characters=[("監", "감", "to oversee — as in 감사, 감독"),
                        ("視", "시", "to see — as in 시청, 중시")],
        ),
        "청문회": dict(
            hanja="聽聞會", meaning="a hearing",
            characters=[("聽", "청", "to listen — as in 시청자"),
                        ("聞", "문", "to hear — as in 신문 “newspaper”")],
        ),
        "인사청문회": dict(
            hanja="人事聽聞會", meaning="a confirmation hearing",
            notes=["인사 here is appointments, not greetings. Held for a "
                   "nominee to high office before the Assembly gives or "
                   "withholds its view."],
        ),
        "당사자": dict(
            hanja="當事者", meaning="the party directly concerned",
            characters=[("當", "당", "to be the case — as in 해당, 담당"),
                        ("事", "사", "affair — as in 사건, 사례")],
        ),
        "증인": dict(
            hanja="證人", meaning="a witness",
            characters=[("證", "증", "to prove — as in 신분증, 증명")],
        ),
        "참고인": dict(hanja="參考人", meaning="a person called to give information"),
        "대법원장": dict(
            hanja="大法院長", meaning="the Chief Justice",
            notes=["Head of the 대법원, the Supreme Court — chapter 23's "
                   "subject."],
        ),
        "국무총리": dict(
            hanja="國務總理", meaning="the Prime Minister",
            characters=[("務", "무", "duty — as in 의무, 업무"),
                        ("總", "총", "general — as in 총선, 총인구"),
                        ("理", "리", "to manage — as in 관리, 처리")],
            notes=["Appointed by the president with the Assembly's consent, "
                   "and second to the president in the executive."],
        ),
        "장관": dict(
            hanja="長官", meaning="a minister",
            characters=[("長", "장", "head, long — as in 사장, 대법원장"),
                        ("官", "관", "official — as in 관공서, 외교관")],
        ),
        "도덕성": dict(
            hanja="道德性", meaning="moral character",
            characters=[("道", "도", "way — as in 도로, 효도"),
                        ("德", "덕", "virtue — as in 덕담")],
        ),
        "답변": dict(
            hanja="答辯", meaning="a reply, an answer",
            characters=[("答", "답", "to answer — as in 응답, 정답"),
                        ("辯", "변", "to argue, to plead — as in 변호사")],
        ),
        "임명": dict(
            hanja="任命", meaning="appointment to office",
            characters=[("任", "임", "to entrust, duty — as in 담임, 책임"),
                        ("命", "명", "command, life — as in 생명, 운명")],
        ),
        "적격": dict(
            hanja="適格", meaning="being qualified",
            characters=[("格", "격", "standard, rank — as in 격차, 성격")],
        ),
        "부적격": dict(hanja="不適格", meaning="being unqualified"),
        "퇴직금": dict(
            hanja="退職金", meaning="severance pay",
            characters=[("退", "퇴", "to withdraw — as in 퇴근, 은퇴"),
                        ("職", "직", "post — as in 직업, 직장")],
            notes=["Korean law owes a worker a lump sum on leaving a job "
                   "after a year — the money this article is about."],
        ),
        "출국": dict(
            hanja="出國", meaning="departure from the country",
            characters=[("出", "출", "to go out — as in 출석, 수출")],
            notes=["Its opposite is 입국. 출입국 covers both, chapter 7's "
                   "word."],
        ),
        "수령제": dict(
            hanja="受領制", meaning="the collection system",
            characters=[("受", "수", "to receive — as in 수강, 접수"),
                        ("領", "령", "to receive, to lead — as in 대통령")],
            notes=["The rule that a migrant worker may collect severance pay "
                   "only after leaving Korea — which is what the campaign "
                   "wanted repealed."],
        ),
        "폐지": dict(
            hanja="廢止", meaning="abolition, repeal",
            characters=[("廢", "폐", "to abolish — as in 폐교 “closed school”"),
                        ("止", "지", "to stop — as in 정지, 금지")],
        ),
        "지적": dict(
            hanja="指摘", meaning="pointing out, criticism",
            characters=[("指", "지", "to point — as in 지정, 지시"),
                        ("摘", "적", "to pick, to pluck")],
        ),
        "차별철폐": dict(
            hanja="差別撤廢", meaning="the abolition of discrimination",
            characters=[("撤", "철", "to withdraw, to remove"),
                        ("廢", "폐", "to abolish — as in 폐지")],
        ),
        "노동권": dict(hanja="勞動權", meaning="labour rights"),
        "공동행동": dict(hanja="共同行動", meaning="joint action"),
        "실태조사": dict(
            hanja="實態調査", meaning="a survey of actual conditions",
            characters=[("實", "실", "real — as in 사실, 실천"),
                        ("態", "태", "condition — as in 태도, 상태")],
        ),
        "발표회": dict(
            hanja="發表會", meaning="a presentation, a public meeting",
            characters=[("表", "표", "to show — as in 표현, 표출")],
        ),
        "주장": dict(
            hanja="主張", meaning="an assertion, a claim",
            characters=[("主", "주", "main — as in 주인, 주권"),
                        ("張", "장", "to stretch, to spread")],
        ),
        "펴다": dict(
            meaning="to spread out; to put forward (an argument)",
            notes=["주장을 펴다 “to press a claim” — the same verb as unfolding "
                   "something."],
        ),
    },

    extraNotes=[
        "Chapter 21 has no Google Doc: the Korean is transcribed from the "
        "photos of pp. 114-117 rather than from a transcription of yours, so "
        "mistakes in it are mine and it is worth reading against the pages.",
        "The review gaps on p. 117 carry your own answers, written in by "
        "hand — 입법부, 300, 법, 예산, 감사. Those are set as the covered "
        "answers; the one you left blank, 국회의원, is left blank here too.",
        "The 국정 감사 article prints 궁금한, which is how the book spells it "
        "in chapter 8 as well. Set as printed.",
    ],
)
