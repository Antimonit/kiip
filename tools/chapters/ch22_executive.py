# -*- coding: utf-8 -*-
"""Chapter 22 — The executive.

Transcribed from the photos of pp. 118-121; there is no Google Doc for it.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, LABELS,
               TABLE, CELL, GLOSSARY)

CHAPTER = dict(
    number=22, slug="22-executive",
    unit="정치", title="행정부", titleEn="The executive",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 한국에서 생활하면서 경험할 수 있는 여러 가지 상황입니다."),
        LABELS("병원비를 걱정하는 사람", "{수해}를 입은 집",
               "아이의 교육을 걱정하는 사람", "여러 나라의 돈을 들고 있는 사람"),
        HEADING(4, "01 각각의 상황에 놓여 있는 사람이라면 한국의 어떤 정부 기관으로부터 도움을 받을 수 "
             "있습니까?"),
        HEADING(4, "02 자신의 고향 나라와 한국에서 각각 {행정 기관}을 이용해 본 경험을 이야기해 "
             "볼까요?"),

        SECTION("goals", "학습목표"),
        BULLET("행정부의 의미와 정부의 구성을 설명할 수 있다.", ordered=True),
        BULLET("대통령의 {권한}과 정부의 역할을 설명할 수 있다.", ordered=True),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", 2), "제목", "관련 내용"],
              [["기본", "정치", "20. 한국의 민주 정치", "권력 분립"],
               ["심화", "역사", "7. 민주주의의 발전", "한국 민주주의의 발전 과정"]]),

        SECTION("part", "01 법은 누가 집행할까?"),
        HEADING(2, "정부라 불리는 행정부"),
        GLOSSARY(("공익", "사회 전체의 이익", "공익"),
              ("집행", "실제로 시행함", "집행"),
              ("대통령제", "대통령을 중심으로 국정이 운영되는 정부 형태", "대통령제")),
        PARAGRAPH("국회가 만든 법을 {기반}으로 하여 {공익}을 {실현}할 목적으로 여러 {정책}을 만들고 "
          "실시하는 일을 {행정}이라고 한다. 출·{입국관리}, {여권} {발급}, 도로 건설, 초등학교 "
          "{배정} 등이 행정의 예이다. {행정부}는 이처럼 국민에게 필요한 정책을 직접 {집행}하면서 "
          "나라의 살림을 하는 곳이다. 행정부를 줄여서 {정부}라고도 부른다. 한국은 대통령을 "
          "중심으로 행정을 이끌어 가는 {대통령제}를 {채택}하고 있다."),

        HEADING(2, "정부의 구성"),
        GLOSSARY(("선출", "여럿 가운데서 뽑힘", "선출"),
              ("중임", "어떤 일을 다시 맡음", "중임"),
              ("임명", "일정한 지위나 임무를 남에게 맡김", "임명")),
        PARAGRAPH("한국 정부는 {대통령}을 중심으로 {국무총리}와 여러 개의 {부}, {처}, {청}, {위원회} "
          "등으로 구성된다. 대통령은 정부의 최고 {책임자}로 나라의 중요한 일을 결정하며 외국에 "
          "대해 나라를 대표한다. 대통령은 국민의 {직접 선거}를 통해 {선출}된다. 대통령의 "
          "{임기}는 5년이며 {중임}은 할 수 없다."),
        PARAGRAPH("국무총리는 대통령을 도와 행정부의 여러 정책을 {관리}하는 역할을 맡는다. 국무총리는 "
          "국회의 동의를 받아 대통령이 {임명}한다."),
        PARAGRAPH("각 부의 책임자는 {장관}이라고 부른다. 2020년 기준으로 한국 정부에는 18개의 부가 있다. "
          "이 외에도 {식품의약품안전처}, {검찰청}, {국가인권위원회} 등과 같은 다양한 기관이 "
          "있다."),
        FIGURE("국무총리 임명식(사진 출처: 청와대)"),
        FIGURE("정부 청사 소개 — 서울 청사, 과천 청사, 대전 청사, 세종 청사"),

        HEADING(2, "국무회의"),
        PARAGRAPH("정부가 국가의 중요한 정책에 대해 {의논}하고 결정할 때는 {국무회의}를 연다. 국무회의는 "
          "정부의 최고 {의사 결정} {기구}이다. 대통령, 국무총리, 장관 등이 참여하며 {의장}은 "
          "대통령, {부의장}은 국무총리이다."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "대통령이 있는 청와대에 가 보고 싶다면..."),
        PARAGRAPH("서울시 종로구에 {위치}한 {청와대}는 푸른색 지붕을 가진 집이라는 뜻이다. 대통령이 일을 "
          "하는 곳인 청와대 {본관}에만 {청기와}가 15만 장이 사용되었다. 청와대는 조선시대 왕들이 "
          "{머물렀던|머물다} {경복궁}과 가까이 있으며 한국의 대통령이 나랏일을 하는 장소로 "
          "사용되고 있다. 청와대는 옛날 {궁궐}의 모습과 {현대적}인 {건축} 기술이 {결합}된 아름다운 "
          "{건축물}로 {평가받고|평가받다} 있다. 청와대 홈페이지에서 미리 {신청}하면 청와대 일부 "
          "{시설}을 {관람}할 수 있다."),
        FIGURE("청와대"),

        SECTION("part", "02 정부는 어떤 일을 할까?"),
        HEADING(2, "대통령의 권한"),
        GLOSSARY(("권한", "어떤 사람이나 기관의 힘이 미치는 범위", "권한"),
              ("조약", "외국과 맺은 약속으로 법과 같은 효력을 가짐", "조약")),
        PARAGRAPH("한국은 대통령제 국가이다. 대통령은 국가 {운영}에 관한 많은 {권한}을 {행사}할 수 있다. "
          "주요 권한으로는 {국군}을 {지휘}하는 권한, 국무총리와 각 부의 장관 등 {공무원}을 "
          "임명하는 권한이 있다. 또 국회가 만든 법안을 {거부}할 수 있는 권한, {범죄}를 "
          "{저지른|저지르다} 사람의 {형벌}을 줄여주거나 {면제}해 줄 수 있는 권한, 외국과 {조약}을 "
          "맺을 수 있는 권한 등도 가지고 있다."),
        TABLE(["대통령", "재임"],
              [["이승만(1~3대)", "1948~1960"],
               ["윤보선(4대)", "1960~1962"],
               ["박정희(5~9대)", "1963~1979"],
               ["최규하(10대)", "1979~1980"],
               ["전두환(11~12대)", "1980~1988"],
               ["노태우(13대)", "1988~1993"],
               ["김영삼(14대)", "1993~1998"],
               ["김대중(15대)", "1998~2003"],
               ["노무현(16대)", "2003~2008"],
               ["이명박(17대)", "2008~2013"],
               ["박근혜(18대)", "2013~2017"],
               ["문재인(19대)", "2017~"]]),
        FIGURE("한국의 역대 대통령"),

        HEADING(2, "정부의 역할"),
        GLOSSARY(("남북통일", "남한과 북한으로 갈려 있는 우리 국토와 우리 겨레가 하나로 되는 일",
               "남북통일"),
              ("검역", "해외에서 전염병이나 해충 등이 들어오는 것을 막기 위해 공항이나 항구에서 "
                       "검사하는 것", "검역"),
              ("치안", "나라를 안전하게 하는 일", "치안")),
        PARAGRAPH("정부는 국민의 자유와 권리 보호, {외교}와 경제 발전, {남북통일} 등의 목적을 실현하기 "
          "위해 노력한다. 그래서 각 부의 장관을 {비롯한|비롯하다} 정부 공무원들은 국민의 삶에 "
          "도움을 주는 정책을 만들고 집행한다."),
        PARAGRAPH("예를 들어, {법무부}에서는 {법질서}와 {이민} 정책 등에 관한 일을, {고용노동부}에서는 "
          "취업과 노동 등에 관한 일을, {여성가족부}는 여성과 청소년 및 가족 관련 일을, {교육부}는 "
          "초·중·고, 대학 및 평생 교육 등에 관한 일을 {담당}한다."),
        PARAGRAPH("또한, 법무부에 {속하는|속하다} {출입국·외국인정책본부}에서는 한국에 {체류}하는 외국인 "
          "{등록}과 사회 {정착}을 도와주는 일을, {보건복지부}에 속하는 {질병관리청}에서는 각종 "
          "{전염병}에 {대비}한 {검역} 관련 일을, {환경부}에 속하는 {기상청}은 날씨에 관한 정보를 "
          "제공하는 일을, {행정안전부}에 속하는 {경찰청}은 범죄 {수사} 및 {치안} 등에 관한 일을 "
          "담당한다."),
        SOURCE("▶ 정부24 http://www.gov.kr/"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "대통령이 없는 국가에서는 정부를 누가 이끌까?"),
        PARAGRAPH("영국, 태국, 일본 등의 국가에서는 {의회}에서 정부 책임자를 뽑는데, 이를 {총리} 또는 "
          "{수상}이라고 한다. 이 나라에서는 총리 또는 수상이 국가를 대표하고 나라의 살림을 "
          "이끌어간다. {국왕}이 있지만, 국왕은 국가의 {상징적}인 {존재}일 뿐 행정이나 정치에 직접 "
          "{관여}하지 않는다. 이처럼 정부 형태는 국가마다 다르지만, 정부의 최고 책임자가 국민을 "
          "위해 국가의 일을 맡는 것은 {동일}하다."),
        FIGURE("영국 총리와 엘리자베스 2세 영국 여왕 (사진 출처: 〈연합뉴스〉)"),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 법은 누가 집행할까?"),
        BULLET("행정부의 최고 책임자는 (          )으로 나라의 중요한 일을 결정하며 국가를 대표한다."),
        BULLET("대통령의 임기는 (    )년이며, 중임은 할 수 없다."),
        BULLET("정부가 국가의 중요한 정책에 대해 의논하고 결정할 때 (          )를 연다. "
          "(          )의 의장은 대통령이고 부의장은 국무총리이다."),
        HEADING(3, "02 정부는 어떤 일을 할까?"),
        BULLET("대통령이 가진 권한에는 (        )을 지휘하는 권한, 주요 공무원을 임명하는 권한, "
          "외국과 조약을 맺을 수 있는 권한 등이 있다."),
        BULLET("정부의 여러 부처 중 (          )에서는 법질서와 이민 정책 등에 관한 일을, "
          "고용노동부에서는 취업과 노동 등에 관한 일을 담당한다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "외국인을 위한 정부 정책에는 어떤 것이 있을까?",
          translation="What government policies are there for foreigners?"),
        HEADING(4, "★★ 경찰 ‘외국인 보호를 위한 종합 안내서’ 배부", translation=
          "Police hand out a ‘comprehensive guide to protecting "
          "foreigners’" "\n\n"
          "The provincial police agency has produced and handed out a "
          "‘comprehensive police guide to protecting foreigners’, to lessen "
          "the difficulty of communicating when a foreigner reports a crime. "
          "The guide covers what counts as violence, what to do when one has "
          "been harmed, and the exemption from the duty to give a "
          "foreigner’s personal details when one has been harmed."),
        PARAGRAPH("지방경찰청은 외국인이 범죄를 {신고}했을 때 {의사소통}의 어려움을 줄여주기 위해 "
          "‘외국인 보호를 위한 경찰 종합 안내서’를 만들어 나누어 주었다. 이 안내서에는 {폭력}의 "
          "{개념}, {피해}를 입었을 때 {대처}하는 방법, 피해를 입었을 때 외국인의 개인 정보를 "
          "알려야 하는 의무 {면제} 등에 대한 내용을 담았다."),
        SOURCE("[출처] 대구신문(2019.09.19)"),
        HEADING(4, "○○시, 다문화 가족을 위한 보건소 이용 안내서 배부", translation=
          "○○ City hands out a guide to using the health centre for "
          "multicultural families" "\n\n"
          "○○ City has produced and is handing out a comprehensive health "
          "guide in five foreign languages — English, Vietnamese, Chinese "
          "and Cambodian among them. A foreigner who visited the health "
          "centre and received the guide in several languages said, “I am so "
          "glad to see a booklet made in my mother tongue, and I feel "
          "grateful for ○○ City’s warm consideration.”"),
        PARAGRAPH("○○시는 영어, 베트남어, 중국어, 캄보디아어 등 5개 외국어로 된 건강 종합 안내서를 "
          "만들어 나누어 주고 있다. {보건소}를 방문해 여러 나라 언어로 된 안내서를 받아 본 "
          "외국인은 “{모국어}로 {제작}된 안내 {책자}를 보니 너무 반갑고, ○○시의 따뜻한 {배려}에 "
          "고마움을 느낀다”고 말했다."),
        SOURCE("[출처] 포천일보(2017.08.01)"),
        HEADING(4, "◇◇시, 외국인 주민에게 ‘동행 통역 서비스’ 실시", translation=
          "◇◇ City starts an ‘accompanied interpreting service’ for foreign "
          "residents" "\n\n"
          "◇◇ City has started an interpreting service for foreign residents "
          "so that they can be helped in their mother tongue when they visit "
          "the civil affairs office. An official of ◇◇ City said, “With this "
          "service, using government offices will become far easier for "
          "foreign residents who have had difficulty because of the "
          "language.”"),
        PARAGRAPH("◇◇시는 외국인 주민이 {민원실}을 방문했을 때 모국어로 안내를 받을 수 있도록 외국인 "
          "주민을 위한 {통역} 서비스를 시작했다. ◇◇시 {관계자}는 “이 서비스를 {활용}하면 언어 "
          "문제로 어려움을 겪었던 외국인 주민의 {관공서} 이용이 훨씬 쉬워질 것”이라고 말했다."),
        SOURCE("[출처] 중부매일(2019.08.07)"),
        PARAGRAPH("★ 자신이 사는 지역에는 외국인을 위한 어떤 정책이 있는지 이야기해 봅시다.",
          "Talk about what policies for foreigners there are in the area "
          "where you live."),
    ],

    english={
        "정부라 불리는 행정부": dict(
            title="The executive, called the government",
            paragraphs=[
                "Making and carrying out policies on the basis of the laws "
                "the Assembly has made, with the public interest as their "
                "end, is administration. Immigration control, issuing "
                "passports, building roads, assigning children to primary "
                "schools are all examples of it. The executive is where the "
                "policies the people need are carried out directly like this, "
                "and where the country's housekeeping is done. 행정부 "
                "shortened is 정부. Korea has adopted a presidential system, "
                "in which the administration is led around the president.",
            ],
        ),
        "정부의 구성": dict(
            title="How the government is made up",
            paragraphs=[
                "The Korean government is made up, around the president, of "
                "the prime minister and a number of ministries, agencies, "
                "offices and commissions. As the government's highest officer "
                "the president decides the important affairs of the country "
                "and represents it abroad. The president is elected by direct "
                "vote of the people. The term is five years, and no one may "
                "serve twice.",

                "The prime minister's part is to assist the president and "
                "manage the executive's various policies. The prime minister "
                "is appointed by the president with the Assembly's consent.",

                "The officer in charge of each ministry is called its "
                "minister. As of 2020 the Korean government has eighteen "
                "ministries. Besides these there are various other bodies, "
                "such as the Ministry of Food and Drug Safety, the "
                "Prosecution Service and the National Human Rights "
                "Commission.",
            ],
        ),
        "국무회의": dict(
            title="The State Council",
            paragraphs=[
                "When the government discusses and decides the important "
                "policies of the state it holds a meeting of the State "
                "Council. The Council is the government's highest "
                "decision-making body. The president, the prime minister "
                "and the ministers take part; "
                "the president chairs it and the prime minister is its "
                "vice-chair.",
            ],
        ),
        "대통령의 권한": dict(
            title="The president's powers",
            paragraphs=[
                "Korea is a presidential state. The president may "
                "exercise many powers over the running of the country. Chief "
                "among them are the power to command the armed forces and the "
                "power to appoint public officials, including the prime "
                "minister and the ministers of each department. The president "
                "also holds the power to veto a bill the Assembly has passed, "
                "the power to reduce or remit the punishment of someone who "
                "has committed a crime, and the power to conclude treaties "
                "with foreign countries.",
            ],
        ),
        "정부의 역할": dict(
            title="What the government does",
            paragraphs=[
                "The government works towards ends such as protecting the "
                "people's freedom and rights, diplomacy, economic "
                "development, and the unification of North and South. Its "
                "officials, the ministers of each department among them, "
                "therefore make and carry out policies that help the people "
                "in their lives.",

                "The Ministry of Justice, for instance, handles matters of "
                "legal order and immigration policy; the Ministry of "
                "Employment and Labour, employment and work; the Ministry of "
                "Gender Equality and Family, matters to do with women, young "
                "people and families; the Ministry of Education, primary, "
                "middle and high schools, universities and lifelong "
                "learning.",

                "The Korea Immigration Service under the Ministry of Justice "
                "handles the registration of foreigners staying in Korea and "
                "helps them settle; the Korea Disease Control and Prevention "
                "Agency under the Ministry of Health and Welfare handles "
                "quarantine against infectious disease of every sort; the "
                "Korea Meteorological Administration under the Ministry of "
                "Environment provides information on the weather; and the "
                "National Police Agency under the Ministry of the Interior "
                "and Safety handles criminal investigation and public order.",
            ],
        ),
    },

    extraAnnotations={
        "행정부": dict(
            hanja="行政部", meaning="the executive branch",
            characters=[("行", "행", "to go, to do — as in 행동, 유행"),
                        ("政", "정", "government — as in 정치, 정부"),
                        ("部", "부", "branch, ministry — as in 입법부, 법무부")],
        ),
        "행정": dict(
            hanja="行政", meaning="administration",
            notes=["The work itself; 행정부 is the branch that does it."],
        ),
        "정부": dict(
            hanja="政府", meaning="the government",
            characters=[("府", "부", "office, seat of government")],
        ),
        "행정 기관": dict(hanja="行政機關", meaning="an administrative body"),
        "수해": dict(
            hanja="水害", meaning="flood damage",
            characters=[("水", "수", "water — as in 수돗물, 홍수"),
                        ("害", "해", "harm — as in 피해, 해충")],
        ),
        "기반": dict(
            hanja="基盤", meaning="a foundation, a base",
            characters=[("基", "기", "base — as in 기본, 기준"),
                        ("盤", "반", "a plate, a board")],
        ),
        "공익": dict(
            hanja="公益", meaning="the public interest",
            characters=[("公", "공", "public — as in 공개, 공무원"),
                        ("益", "익", "benefit — as in 이익, 유익하다")],
            notes=["Its opposite is 사익, private interest."],
        ),
        "실현": dict(
            hanja="實現", meaning="realisation, bringing about",
            characters=[("實", "실", "real — as in 사실, 실제"),
                        ("現", "현", "to appear, present — as in 현재, 표현")],
        ),
        "정책": dict(
            hanja="政策", meaning="a policy",
            characters=[("政", "정", "government — as in 정치, 행정"),
                        ("策", "책", "plan, scheme — as in 대책 “countermeasure”")],
        ),
        "입국관리": dict(
            hanja="入國管理", meaning="immigration control",
            notes=["The book writes 출·입국관리 for both directions at once."],
        ),
        "여권": dict(
            hanja="旅券", meaning="a passport",
            characters=[("旅", "여", "travel — as in 여행, 여객"),
                        ("券", "권", "a ticket, a certificate — as in 상품권")],
            notes=["Not 여권 as in 女權 “women's rights”, nor 여당's 與."],
        ),
        "발급": dict(
            hanja="發給", meaning="issuance (of a document)",
            characters=[("發", "발", "to issue — as in 발표, 발전"),
                        ("給", "급", "to supply — as in 공급, 급여")],
        ),
        "배정": dict(hanja="配定", meaning="assignment, allocation"),
        "집행": dict(
            hanja="執行", meaning="execution, enforcement",
            characters=[("執", "집", "to hold, to grasp — as in 집권"),
                        ("行", "행", "to carry out — as in 행정, 실행")],
        ),
        "대통령제": dict(
            hanja="大統領制", meaning="a presidential system",
            notes=["Set against 의원내각제, the parliamentary system the aside "
                   "on p. 120 describes."],
        ),
        "채택": dict(
            hanja="採擇", meaning="adoption, to adopt",
            characters=[("採", "채", "to pick, to gather — as in 채용 “hiring”"),
                        ("擇", "택", "to choose — as in 선택")],
        ),
        "대통령": dict(
            hanja="大統領", meaning="the president",
            characters=[("統", "통", "to unify, to command — as in 통일, 통합"),
                        ("領", "령", "to lead — as in 영토, 수령")],
        ),
        "국무총리": dict(hanja="國務總理", meaning="the prime minister"),
        "부": dict(
            hanja="部", meaning="a ministry",
            notes=["The three ranks the page names go 부 › 처 › 청: ministry, "
                   "then agency under the prime minister, then agency under a "
                   "ministry."],
        ),
        "처": dict(hanja="處", meaning="an agency (under the prime minister)"),
        "청": dict(hanja="廳", meaning="an agency (under a ministry)"),
        "위원회": dict(
            hanja="委員會", meaning="a commission, a committee",
            characters=[("委", "위", "to entrust — as in 위임"),
                        ("員", "원", "member — as in 국회의원, 공무원")],
        ),
        "책임자": dict(
            hanja="責任者", meaning="the person in charge",
            characters=[("責", "책", "responsibility — as in 책임감"),
                        ("任", "임", "duty, to entrust — as in 임명, 임기")],
        ),
        "직접 선거": dict(
            hanja="直接選擧", meaning="direct election",
            notes=["The people vote for the president themselves, not through "
                   "electors — what the 1987 movement won."],
        ),
        "선출": dict(hanja="選出", meaning="to be elected"),
        "임기": dict(
            hanja="任期", meaning="a term of office",
            characters=[("任", "임", "duty — as in 임명, 책임"),
                        ("期", "기", "period — as in 회기, 기간")],
        ),
        "중임": dict(
            hanja="重任", meaning="serving a second term",
            characters=[("重", "중", "heavy, again — as in 중요, 중시")],
            notes=["Korea's president serves one five-year term and no more, a "
                   "deliberate guard against a long-serving strongman."],
        ),
        "관리": dict(
            hanja="管理", meaning="management, administration",
            characters=[("管", "관", "to manage, a pipe — as in 보관"),
                        ("理", "리", "reason, to order — as in 처리, 원리")],
        ),
        "임명": dict(
            hanja="任命", meaning="appointment to office",
            characters=[("命", "명", "command — as in 생명, 운명")],
        ),
        "장관": dict(hanja="長官", meaning="a minister"),
        "식품의약품안전처": dict(
            hanja="食品醫藥品安全處",
            meaning="the Ministry of Food and Drug Safety",
            notes=["식약처 for short."],
        ),
        "검찰청": dict(
            hanja="檢察廳", meaning="the Prosecution Service",
            characters=[("檢", "검", "to inspect — as in 검사, 검역"),
                        ("察", "찰", "to examine — as in 경찰, 관찰")],
        ),
        "국가인권위원회": dict(
            hanja="國家人權委員會",
            meaning="the National Human Rights Commission of Korea",
            notes=["The body that held the hearing chapter 21's news story "
                   "reports."],
        ),
        "의논": dict(
            hanja="議論", meaning="discussion, talking over",
            notes=["The same 議論 as 논의, read the other way round; 의논 is the "
                   "everyday word, 논의 the formal one."],
        ),
        "국무회의": dict(
            hanja="國務會議", meaning="the State Council",
            characters=[("務", "무", "duty, affairs — as in 의무, 업무")],
        ),
        "의사 결정": dict(hanja="意思決定", meaning="decision-making"),
        "기구": dict(
            hanja="機構", meaning="an organ, a body",
            characters=[("機", "기", "workings — as in 기관, 기능"),
                        ("構", "구", "to construct — as in 구성, 구조")],
        ),
        "의장": dict(
            hanja="議長", meaning="a chair",
            characters=[("議", "의", "to deliberate — as in 회의, 국회의원"),
                        ("長", "장", "head — as in 사장, 대법원장")],
        ),
        "부의장": dict(hanja="副議長", meaning="a vice-chair"),
        "위치": dict(
            hanja="位置", meaning="position, to be situated",
            characters=[("位", "위", "place, rank — as in 지위, 순위"),
                        ("置", "치", "to place — as in 설치")],
        ),
        "청와대": dict(
            hanja="靑瓦臺", meaning="the Blue House",
            characters=[("靑", "청", "blue-green — as in 청년, 청소년"),
                        ("瓦", "와", "roof tile — as in 기와"),
                        ("臺", "대", "platform, terrace — as in 무대")],
            notes=["Literally “blue-tiled terrace”, for the roof. The "
                   "president's office moved out to 용산 in 2022, after this "
                   "book was printed, and the grounds are open to visitors."],
        ),
        "본관": dict(hanja="本館", meaning="the main building"),
        "청기와": dict(meaning="a blue-glazed roof tile"),
        "머물다": dict(meaning="to stay, to remain"),
        "경복궁": dict(
            hanja="景福宮", meaning="Gyeongbokgung palace",
            notes=["The Joseon dynasty's chief palace, just south of the Blue "
                   "House."],
        ),
        "궁궐": dict(
            hanja="宮闕", meaning="a palace",
            characters=[("宮", "궁", "palace — as in 경복궁, 궁전"),
                        ("闕", "궐", "a palace gate")],
        ),
        "현대적": dict(hanja="現代的", meaning="modern"),
        "건축": dict(
            hanja="建築", meaning="architecture, building",
            characters=[("建", "건", "to build — as in 건설, 건물"),
                        ("築", "축", "to construct — as in 축조")],
        ),
        "건축물": dict(hanja="建築物", meaning="a building, a structure"),
        "결합": dict(
            hanja="結合", meaning="combination, joining",
            characters=[("結", "결", "to tie — as in 결혼, 결과"),
                        ("合", "합", "to join — as in 통합, 적합하다")],
        ),
        "평가받다": dict(
            hanja="評價받다", meaning="to be regarded as, to be rated",
            characters=[("評", "평", "to criticise, to judge — as in 비평"),
                        ("價", "가", "value, price — as in 물가, 가치")],
        ),
        "신청": dict(hanja="申請", meaning="an application, to apply"),
        "시설": dict(
            hanja="施設", meaning="a facility",
            characters=[("施", "시", "to carry out — as in 실시"),
                        ("設", "설", "to establish — as in 건설, 설립")],
        ),
        "관람": dict(
            hanja="觀覽", meaning="viewing, going to see",
            characters=[("觀", "관", "to observe — as in 관광, 관심"),
                        ("覽", "람", "to look over — as in 열람 “perusal”")],
        ),
        "운영": dict(
            hanja="運營", meaning="operation, running",
            characters=[("運", "운", "to move, luck — as in 운동, 운전"),
                        ("營", "영", "to manage — as in 경영, 영업")],
        ),
        "권한": dict(
            hanja="權限", meaning="authority, a power",
            characters=[("權", "권", "right, power — as in 권력, 인권"),
                        ("限", "한", "limit — as in 제한, 기한")],
            notes=["Literally the limit within which a power reaches, which is "
                   "just how the margin glosses it."],
        ),
        "행사": dict(
            hanja="行使", meaning="exercise (of a power)",
            characters=[("使", "사", "to use, to send — as in 사용, 대사관")],
            notes=["Not the 행사 “event” of 문화 행사, which is 行事."],
        ),
        "국군": dict(
            hanja="國軍", meaning="the national armed forces",
            characters=[("軍", "군", "army — as in 군대, 군인")],
        ),
        "지휘": dict(
            hanja="指揮", meaning="command",
            characters=[("指", "지", "to point — as in 지적, 지시"),
                        ("揮", "휘", "to wield — as in 발휘")],
            notes=["Also the word for conducting an orchestra: 지휘자."],
        ),
        "공무원": dict(hanja="公務員", meaning="a public official"),
        "거부": dict(
            hanja="拒否", meaning="refusal, veto",
            characters=[("拒", "거", "to refuse, to resist"),
                        ("否", "부", "not, to deny — as in 부정, 여부")],
            notes=["거부권 is the veto power itself."],
        ),
        "범죄": dict(
            hanja="犯罪", meaning="a crime",
            characters=[("犯", "범", "to offend — as in 범인 “culprit”"),
                        ("罪", "죄", "sin, guilt — as in 죄송하다")],
        ),
        "저지르다": dict(meaning="to commit (an offence)"),
        "형벌": dict(
            hanja="刑罰", meaning="punishment, a penalty",
            characters=[("刑", "형", "punishment — as in 형법, 사형"),
                        ("罰", "벌", "penalty — as in 벌금 “a fine”")],
        ),
        "면제": dict(
            hanja="免除", meaning="exemption, remission",
            characters=[("免", "면", "to excuse, to avoid — as in 면세"),
                        ("除", "제", "to remove — as in 제외, 삭제")],
        ),
        "조약": dict(
            hanja="條約", meaning="a treaty",
            characters=[("條", "조", "article — as in 조항, 제1조"),
                        ("約", "약", "promise — as in 약속, 계약")],
        ),
        "외교": dict(
            hanja="外交", meaning="diplomacy",
            characters=[("外", "외", "outside — as in 외국, 해외"),
                        ("交", "교", "to exchange — as in 교통, 교류")],
        ),
        "남북통일": dict(
            hanja="南北統一", meaning="the unification of North and South",
            characters=[("統", "통", "to unify — as in 통합, 대통령"),
                        ("一", "일", "one — as in 동일, 제일")],
        ),
        "비롯하다": dict(
            meaning="to include, starting with",
            notes=["A를 비롯한 B “B, A among them” — a set phrase for naming the "
                   "leading example first."],
        ),
        "법무부": dict(hanja="法務部", meaning="the Ministry of Justice"),
        "법질서": dict(hanja="法秩序", meaning="legal order"),
        "이민": dict(
            hanja="移民", meaning="migration, immigration",
            characters=[("移", "이", "to move — as in 이사, 이주"),
                        ("民", "민", "people — as in 국민, 주민")],
        ),
        "고용노동부": dict(
            hanja="雇傭勞動部", meaning="the Ministry of Employment and Labour",
        ),
        "여성가족부": dict(
            hanja="女性家族部",
            meaning="the Ministry of Gender Equality and Family",
        ),
        "교육부": dict(hanja="敎育部", meaning="the Ministry of Education"),
        "담당": dict(
            hanja="擔當", meaning="to be in charge of",
            characters=[("擔", "담", "to bear — as in 부담, 담임"),
                        ("當", "당", "to be the case — as in 해당, 당선")],
        ),
        "속하다": dict(hanja="屬하다", meaning="to belong to, to come under"),
        "출입국·외국인정책본부": dict(
            hanja="出入國外國人政策本部",
            meaning="the Korea Immigration Service",
            notes=["The office that runs the KIIP and issues residence cards "
                   "— the part of government most of this book's readers deal "
                   "with directly."],
        ),
        "체류": dict(
            hanja="滯留", meaning="stay, residence",
            characters=[("滯", "체", "to stagnate, to be delayed — as in 정체"),
                        ("留", "류", "to remain — as in 유학, 보류")],
            notes=["체류 자격 is the visa status; 체류 기간 the period of stay."],
        ),
        "등록": dict(
            hanja="登錄", meaning="registration",
            characters=[("登", "등", "to climb, to register — as in 등산"),
                        ("錄", "록", "to record — as in 기록, 목록")],
        ),
        "정착": dict(
            hanja="定着", meaning="settling, taking root",
            characters=[("定", "정", "to fix — as in 확정, 규정"),
                        ("着", "착", "to arrive, to attach — as in 도착, 애착")],
        ),
        "보건복지부": dict(
            hanja="保健福祉部",
            meaning="the Ministry of Health and Welfare",
        ),
        "질병관리청": dict(
            hanja="疾病管理廳",
            meaning="the Korea Disease Control and Prevention Agency",
            notes=["Raised from a 본부 to a 청 in September 2020, on the "
                   "strength of its part in the COVID response — which is why "
                   "this printing has the newer name."],
        ),
        "전염병": dict(
            hanja="傳染病", meaning="an infectious disease",
            characters=[("傳", "전", "to transmit — as in 전통, 전달"),
                        ("染", "염", "to dye, to stain — as in 염색"),
                        ("病", "병", "illness — as in 질병, 병원")],
        ),
        "대비": dict(
            hanja="對備", meaning="preparation against",
            characters=[("備", "비", "to prepare — as in 준비, 설비")],
        ),
        "검역": dict(
            hanja="檢疫", meaning="quarantine",
            characters=[("檢", "검", "to inspect — as in 검사, 검토"),
                        ("疫", "역", "epidemic — as in 방역, 면역")],
        ),
        "환경부": dict(hanja="環境部", meaning="the Ministry of Environment"),
        "기상청": dict(
            hanja="氣象廳",
            meaning="the Korea Meteorological Administration",
            characters=[("氣", "기", "air, spirit — as in 날씨's 기후, 기분"),
                        ("象", "상", "form, elephant — as in 상징, 현상")],
        ),
        "행정안전부": dict(
            hanja="行政安全部",
            meaning="the Ministry of the Interior and Safety",
        ),
        "경찰청": dict(hanja="警察廳", meaning="the National Police Agency"),
        "수사": dict(
            hanja="搜査", meaning="a criminal investigation",
            characters=[("搜", "수", "to search — as in 수색"),
                        ("査", "사", "to investigate — as in 조사, 감사")],
        ),
        "치안": dict(
            hanja="治安", meaning="public order, public safety",
            characters=[("治", "치", "to govern, to cure — as in 정치, 치료"),
                        ("安", "안", "peace — as in 안전, 불안")],
        ),
        "의회": dict(
            hanja="議會", meaning="a parliament, an assembly",
            notes=["The general word; 국회 is Korea's own."],
        ),
        "총리": dict(hanja="總理", meaning="a premier, a prime minister"),
        "수상": dict(
            hanja="首相", meaning="a prime minister",
            characters=[("首", "수", "head — as in 수도 “capital”"),
                        ("相", "상", "minister, mutual — as in 상대, 서로")],
            notes=["Used of Britain's and Japan's; 총리 of Korea's own."],
        ),
        "국왕": dict(hanja="國王", meaning="a monarch, a king"),
        "상징적": dict(hanja="象徵的", meaning="symbolic"),
        "존재": dict(
            hanja="存在", meaning="existence, a presence",
            characters=[("存", "존", "to exist — as in 보존"),
                        ("在", "재", "to be at — as in 현재, 재적")],
        ),
        "관여": dict(
            hanja="關與", meaning="involvement, taking part in",
            characters=[("關", "관", "to relate — as in 관계, 관련"),
                        ("與", "여", "to give, to take part — as in 참여, 여당")],
        ),
        "동일": dict(
            hanja="同一", meaning="being the same, identical",
            characters=[("同", "동", "same — as in 동의, 공동")],
        ),
        "신고": dict(
            hanja="申告", meaning="a report to the authorities",
            characters=[("申", "신", "to state — as in 신청"),
                        ("告", "고", "to tell — as in 광고, 보고")],
        ),
        "의사소통": dict(
            hanja="意思疏通", meaning="communication",
            characters=[("疏", "소", "to be sparse, to clear"),
                        ("通", "통", "to pass through — as in 통신, 교통")],
        ),
        "폭력": dict(
            hanja="暴力", meaning="violence",
            characters=[("暴", "폭", "violent, sudden — as in 폭우 “downpour”"),
                        ("力", "력", "force — as in 능력, 압력")],
        ),
        "개념": dict(
            hanja="槪念", meaning="a concept",
            characters=[("槪", "개", "general, outline — as in 대개"),
                        ("念", "념", "thought — as in 이념, 기념")],
        ),
        "피해": dict(
            hanja="被害", meaning="damage, harm suffered",
            characters=[("被", "피", "to receive, passive — as in 피고"),
                        ("害", "해", "harm — as in 수해, 해충")],
            notes=["피해자 is the victim, 가해자 the one who did it."],
        ),
        "대처": dict(
            hanja="對處", meaning="coping, dealing with",
            characters=[("處", "처", "to deal with — as in 처리, 처우")],
        ),
        "보건소": dict(
            hanja="保健所", meaning="a public health centre",
            notes=["The local clinic run by the district office — where "
                   "vaccinations and health checks are done cheaply."],
        ),
        "모국어": dict(
            hanja="母國語", meaning="one's mother tongue",
            characters=[("母", "모", "mother — as in 모유, 부모"),
                        ("語", "어", "language — as in 언어, 한국어")],
        ),
        "제작": dict(
            hanja="製作", meaning="production, making",
            characters=[("製", "제", "to manufacture — as in 제품, 제조"),
                        ("作", "작", "to make — as in 작품, 작업")],
        ),
        "책자": dict(hanja="冊子", meaning="a booklet, a pamphlet"),
        "배려": dict(
            hanja="配慮", meaning="consideration, thoughtfulness",
            characters=[("配", "배", "to distribute — as in 배정, 배달"),
                        ("慮", "려", "to consider — as in 고려")],
        ),
        "민원실": dict(
            hanja="民願室", meaning="the civil service counter",
            notes=["민원 is a citizen's request or complaint to an office; the "
                   "민원실 is the room where you file it."],
        ),
        "통역": dict(
            hanja="通譯", meaning="interpreting (spoken)",
            characters=[("譯", "역", "to translate — as in 번역 “translation”")],
            notes=["통역 is spoken, 번역 written."],
        ),
        "관계자": dict(hanja="關係者", meaning="an official, a person concerned"),
        "활용": dict(
            hanja="活用", meaning="making use of",
            characters=[("活", "활", "living — as in 생활, 활성화"),
                        ("用", "용", "to use — as in 사용, 이용")],
        ),
        "관공서": dict(
            hanja="官公署", meaning="a government office",
            characters=[("官", "관", "official — as in 장관, 외교관"),
                        ("署", "서", "office — as in 경찰서, 세무서")],
        ),
    },

    extraNotes=[
        "Chapter 22 has no Google Doc: the Korean is my reading of the photos "
        "of pp. 118-121, so it is worth checking against the pages.",
        "The twelve portraits on p. 120 are set as a table of names and terms "
        "— the photographs themselves are not reproduced.",
        "The review gaps on p. 121 are blank in the book and left blank here.",
        "청와대 has since ceased to be the president's office: it opened to "
        "the public in May 2022, two years after this printing. The aside is "
        "left as the book has it.",
    ],
)
