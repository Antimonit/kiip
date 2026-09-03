# -*- coding: utf-8 -*-
"""Chapter 29 — Finding work.

The last chapter of 제5편 경제, transcribed from the photos of pp. 152-155.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, VERSE,
               TABLE, CELL, GLOSSARY)

CHAPTER = dict(
    number=29, slug="29-finding-work",
    unit="경제", title="취업하기", titleEn="Finding work",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 외국인 {근로자} {지원 사업}에 신청한 {지원자}의 {면접} 모습입니다."),
        FIGURE("사무실 소파에 마주 앉아 면접을 보는 사람들"),
        HEADING(4, "01 {취업}을 위해 면접을 해 본 경험이 있습니까? 취업과 관련된 면접에서 "
                   "지원자에게 필요한 것은 무엇입니까?"),
        HEADING(4, "02 한국에서 취업을 하게 된다면 어떤 일을 하고 싶습니까?"),

        SECTION("goals", "학습목표"),
        BULLET("한국의 {일자리} 상황을 설명할 수 있다.", ordered=True),
        BULLET("한국에서 취업을 하기 위한 방법을 이해하고 활용할 수 있다.", ordered=True),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"],
              [["기본", "사회", "11. 고등 교육과 입시", "대학 입학 방법, 고등 교육 기관"],
               ["심화", "경제", "15. 기업과 근로자", "한국의 기업, 한국 근로 조건"]]),

        SECTION("part", "01 한국의 일자리 상황은 어떠할까?"),
        HEADING(2, "일자리 찾기가 쉽지 않네요"),
        GLOSSARY(("생계", "살림을 꾸려나가는 것, 살아가는 형편", "생계"),
                 ("실업률", "일할 의지와 능력을 가진 사람들 중에서 취업하지 못하는 사람이 "
                            "차지하는 비율", "실업률"),
                 ("자영업", "자신이 스스로 경영하는 사업", "자영업"),
                 ("치열", "어떤 일의 정도가 맹렬하고 뜨거움", "치열"),
                 ("비정규직", "정규직으로서 보장받지 못하는 계약직, 임시직, 일용직 등",
                  "비정규직")),
        PARAGRAPH("사람들은 {직업}을 통해 기본적인 {생계}를 유지하고 자신의 꿈을 이룰 수 있다. "
                  "또한 많은 사람들이 직장에서 안정적으로 일을 하면 나라의 경제 발전에도 "
                  "{기여}할 수 있다. 일하기를 원하는 사람은 많지만 모든 사람이 다 일을 할 수 "
                  "있는 것은 아니다."),
        PARAGRAPH("한국의 {실업률}은 미국이나 유럽의 여러 나라에 비해서는 낮은 편이다. 그러나 "
                  "한국은 미국, 유럽 등에 비해 {자영업}을 하는 사람들이 많고 여성이 경제 활동에 "
                  "참가하는 비율이 낮기 때문에 실업률이 낮게 나타나는 {측면}이 있다. 최근 "
                  "한국에서도 직업을 구하기 위한 {경쟁}이 매우 {치열}하다. 또한, 전체 근로자 "
                  "중에서 {비정규직} 근로자가 차지하는 비중이 높아지면서 {임금}이나 {근로 조건} "
                  "등에서 상대적으로 {불리함}을 겪는 경우도 나타나고 있다."),
        TABLE(["국가", "2018년", "2019년", "2020년"],
              [["한국", "10.4", "11.0", "11.9"],
               ["독일", "6.2", "5.4", "5.3"],
               ["일본", "3.6", "3.7", "4.0"],
               ["미국", "8.5", "8.5", "8.9"],
               ["프랑스", "20.7", "19.1", "19.5"],
               ["스페인", "34.4", "32.9", "31.1"],
               ["이탈리아", "32.2", "29.3", "29.7"]]),
        FIGURE("주요국 청년 실업률 비교 — OECD 국가별 15~24세 실업률 추이 (단위: %) "
               "(통계청, KOSIS 국가통계 포털(2020))"),

        HEADING(2, "일자리 지원을 위한 정부의 노력"),
        GLOSSARY(("시간선택제", "근로자가 필요에 따라 자신의 일할 시간을 선택해 일반적인 "
                                "근무시간보다 짧게 일하는 방식임", "시간선택제")),
        PARAGRAPH("일자리를 {둘러싼|둘러싸다} 어려움을 극복하기 위해 한국 정부는 많은 노력을 "
                  "기울이고 있다. {실업자}가 다시 {취직}할 수 있도록 돕기 위해 여러 가지 교육 "
                  "프로그램을 제공하거나 실업자와 근로자의 기본적인 생활을 보장하기 위한 "
                  "{사회보장제도}를 확대하는 것 등이 그 예이다."),
        PARAGRAPH("한국 정부는 대상에 따른 {맞춤형} 일자리 정책을 제공하고 있다. 예를 들어 "
                  "직장을 구하는 {청년}에게는 {구직} 활동 {지원금}을 제공하거나 {개인별}로 취업 "
                  "계획을 세우고 {단계적}으로 이를 {실천}하도록 지원하는 {취업성공패키지} 제도가 "
                  "실시되고 있다."),
        PARAGRAPH("또한 일과 육아를 함께 할 수 있는 환경을 만들기 위해 여성과 남성 모두에게 "
                  "{출산} 및 {육아 휴직제도}를 {권장}하고 있다. 그리고 여성의 {시간선택제} "
                  "{근무}가 가능한 일자리가 {증가}하고 있다. 한편, 최근에는 {은퇴} 후에도 "
                  "일하고자 하는 사람들이 많기 때문에 60세 이상 인구의 {고용} {안정}과 "
                  "{재취업}을 위한 지원도 이루어지고 있다."),
        FIGURE("취업성공패키지 누리집 (www.work.go.kr/pkg)"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "한국 일자리 정보의 모든 것, 워크넷"),
        PARAGRAPH("{워크넷}은 고용노동부와 {한국고용정보원}이 {운영}하는 구직(직장을 구하는 것) "
                  "및 {구인}(일할 사람을 구하는 것) 정보와 직업·{진로정보}를 제공하는 "
                  "{누리집}(www.work.go.kr)이다. 워크넷의 {통합} 일자리 서비스를 통해 "
                  "지방자치단체나 기업이 제공하는 일자리 정보를 쉽고 빠르게 {검색}할 수 있다. "
                  "여기서는 온라인 구직 신청, 이메일 {입사}(회사에 들어가는 것) 지원, {맞춤} "
                  "정보 서비스, 구직 활동 사항 {조회}/{출력} 등의 서비스를 이용할 수 있다."),
        FIGURE("워크넷 누리집"),

        SECTION("part", "02 취업하기 위해서는 무엇을 준비해야 할까?"),
        HEADING(2, "외국인이 한국에서 취업하려면"),
        GLOSSARY(("구인 광고", "어떤 일자리에 사람을 구하는 광고", "구인 광고"),
                 ("한국산업인력공단", "근로자들의 능력을 개발하는 프로그램을 통해 산업에 필요한 "
                                      "인력을 길러내는 국가기관", "한국산업인력공단"),
                 ("이력서", "그동안 쌓은 학력이나 직업 관련 경험을 적은 것", "이력서")),
        PARAGRAPH("한국에서는 {체류자격}(사증)이 허용되는 {범위} 내에서 직업을 선택할 수 있다. "
                  "한국에서 오랜 기간 거주할 수 있는 자격이 주어진다면 취업할 수 있는 범위는 "
                  "{넓어진다|넓어지다}. 직업을 갖고자 하는 사람은 적극적으로 자신이 원하는 직업을 "
                  "탐색하고, 그 직업에 필요한 능력을 갖추기 위해 준비해야 한다."),
        PARAGRAPH("먼저 취업 관련 정보에 관심을 가지고 누리집이나 {모집 공고문} 등에 올라온 "
                  "{구인 광고}를 자세히 살펴보면서 그 일자리가 자신의 상황이나 능력에 맞는지 "
                  "확인해 보아야 한다. 일자리를 구할 때 가장 중요한 것은 해당 분야에 필요한 "
                  "능력을 갖추는 것이다. 특히 외국인의 경우 한국어 능력과 한국 사회 이해 수준을 "
                  "높이면 취업에 더 {유리}할 수 있다. 또한, 각종 {직업 학교}나 평생 교육 기관, "
                  "{한국산업인력공단} 등에서는 여러 가지 전문적인 직업 교육 프로그램을 운영하고 "
                  "있는데 이를 통해 자신의 능력을 더욱 높이는 노력이 필요하다. 한편, 자신이 어떤 "
                  "분야에 {전문성}을 가지고 있다는 것을 보여주는 {자격증}을 {따거나|따다} 관련 "
                  "분야의 {현장}에서 일한 경험을 {증명}하면 취업에도 도움이 되고 나중에 더 좋은 "
                  "대우를 받을 수도 있다. 그러므로 자신이 가지고 있는 자격증이나 {경력} 등을 "
                  "{이력서}에 꼼꼼히 기록해야 하며, 취업을 위한 면접을 할 때는 자신이 일할 능력이 "
                  "있고 의지가 높다는 점을 적극적으로 {표현}하는 것이 좋다."),
        FIGURE("한국산업인력공단 누리집 (http://www.hrdkorea.or.kr/)"),

        HEADING(2, "취업할 때 반드시 챙겨야 할 점"),
        GLOSSARY(("고용노동부", "일자리와 관련된 도움을 주기 위한 정부 부처", "고용노동부")),
        PARAGRAPH("취업할 때에는 자신이 취업하려고 하는 {업체}가 하는 일은 무엇이며, {정식}으로 "
                  "등록되어 있는지 확인해야 한다. 취업을 하게 되면 {근로 계약서}를 반드시 "
                  "작성하고, 취업 이후에도 임금이나 근로 조건 등에서 부당한 대우를 받지 않도록 "
                  "근로자가 누릴 수 있는 기본적인 권리에 관해 살펴볼 필요가 있다. {이민자}나 "
                  "외국인의 경우 일자리와 관련된 문제가 발생했을 경우에 {고용노동부}나 "
                  "한국산업인력공단, 각 지역의 {외국인 근로자 지원센터} 등에 {문의}하여 도움을 "
                  "받는 것이 좋다."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "외국인 취업 박람회, 나에게 맞는 한국의 직장은?"),
        PARAGRAPH("2014년부터 해마다 서울에서 개최되는 ‘외국인 {취업 박람회}’는 한국의 기업과 "
                  "외국인 우수 인재들이 만나 취업 관련 정보를 나누고 실제로 취업의 기회를 "
                  "제공하기도 하는 자리이다. 여기서는 외국인 {구직자}에게 {적합}한 한국 기업이 "
                  "어디인지 {추천}해 주고 이력서 잘 쓰는 방법, 면접 잘 보는 방법, 한국에서 유학 "
                  "생활 잘하는 방법 등을 알려준다. 또한, 외국인의 취업을 지원하는 기관 정보, "
                  "한국어 교육 정보, 한국 {행정 기관} 이용 정보 등도 제공한다."),
        FIGURE("외국인 취업 박람회 (사진 출처: 〈연합뉴스〉)"),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 한국의 일자리 상황은 어떠할까?"),
        BULLET("한국은 미국, 유럽의 여러 나라에 비해 자영업자의 비율이 높고 여성의 경제 활동 참가 "
               "비율이 낮아 (        )이 낮게 나타나는 편이다."),
        BULLET("최근에는 전체 근로자 중에서 (          ) 근로자의 비중이 높아져 임금이나 근로 "
               "조건 등에서 상대적으로 불리함을 겪는 사례도 많아지고 있다."),
        HEADING(3, "02 취업하기 위해서는 무엇을 준비해야 할까?"),
        BULLET("일자리를 구할 때 자신이 어떤 분야에 전문성을 가지고 있다는 것을 보여주는 "
               "(        )을 따면 큰 도움이 된다."),
        BULLET("자신이 가지고 있는 자격증이나 경력 등을 (        )에 꼼꼼히 기록해 두는 것이 "
               "취업에 유리하다."),
        BULLET("취업을 하게 되면 (            )를 반드시 작성하여 임금이나 근로 조건 등과 관련한 "
               "근로자의 권리를 보호 받을 수 있도록 한다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "외국인 인력 지원센터에 고마움을 나눕니다."),
        VERSE("“빈은 현재 직장에서 4년 10개월을 일하고 나서 베트남으로 {귀국}했다가 {성실} "
              "근로자로 다시 한국에 들어왔습니다. {어느덧} 9년이라는 시간 동안 같은 직장에서 "
              "일했습니다.",
              "하지만 빈에게도 처음에는 한국 생활이 쉽지 않았습니다. 특히, 빈은 한국어에 어려움을 "
              "많이 느꼈는데 직장 {동료}들은 빈을 도와주기 위해 저희 외국인 인력 지원센터를 "
              "찾아왔습니다.",
              "빈은 저와 함께 매주 일요일마다 외국인 인력 지원센터에서 진행되는 한국어 공부와 "
              "베트남 {커뮤니티} 활동에 참여하였고 한국 생활에도 점점 잘 적응했습니다.",
              "빈은 자신이 그랬던 것처럼, 자신이 했던 고민을 하고 있는 외국인 친구들을 위해 "
              "이제는 먼저 {다가가|다가가다} 돕고 있습니다. 베트남에서 온 빈은 그렇게 외국인 "
              "인력 지원센터에서 고마움을 나누고 있습니다.”"),
        SOURCE("[출처] 한국산업인력공단(2015). HRDKOREA Newsletter 3호."),
        PARAGRAPH("★ 자신이 한국에 잘 적응할 수 있도록 도움을 주었던 사람이나 기관에 대해 "
                  "이야기해 봅시다."),
    ],

    english={
        "일자리 찾기가 쉽지 않네요": dict(
            title="Work is not easy to find",
            paragraphs=[
                "Through an occupation a person keeps themselves and may "
                "fulfil their hopes. Many people working steadily at their "
                "jobs also contributes to the country's economic development. "
                "But though many want to work, not everyone can.",

                "Korea's unemployment rate is low next to the United States "
                "and the countries of Europe. Part of the reason it shows low, "
                "though, is that more people are self-employed than in "
                "America or Europe and fewer women take part in economic "
                "activity. Competition for a job has lately become fierce in "
                "Korea too. And as irregular workers take a larger share of "
                "the workforce, cases of relative disadvantage in wages and "
                "working conditions have appeared.",
            ],
        ),
        "일자리 지원을 위한 정부의 노력": dict(
            title="What the government does for jobs",
            paragraphs=[
                "The Korean government puts much effort into overcoming the "
                "difficulties around work. Providing training programmes to "
                "help the unemployed back into a job, and widening the social "
                "security that guarantees the unemployed and the employed a "
                "basic living, are examples.",

                "It provides job policies tailored to whom they are for. A "
                "young person looking for work, for instance, may be given a "
                "job-seeking allowance, or supported through the "
                "취업성공패키지 scheme, which helps them draw up a personal "
                "plan for finding work and carry it out step by step.",

                "To make it possible to work and raise children at once, "
                "childbirth and childcare leave are encouraged for women and "
                "men alike. Jobs open to women on selected hours are "
                "increasing. And because many now wish to work after "
                "retirement, there is support for the employment and "
                "re-employment of people over sixty.",
            ],
        ),
        "외국인이 한국에서 취업하려면": dict(
            title="A foreigner looking for work in Korea",
            paragraphs=[
                "In Korea you may choose an occupation within what your "
                "residence status — your visa — allows. Given a status that "
                "lets you live here a long while, the range of work open to "
                "you widens. Anyone wanting a job should search out the work "
                "they want and prepare themselves for what it calls for.",

                "Start by taking an interest in the information: read the job "
                "advertisements on websites and notice boards closely, and "
                "check whether the work suits your circumstances and your "
                "abilities. What matters most in finding work is having what "
                "the field requires. For a foreigner in particular, raising "
                "your Korean and your understanding of Korean society can "
                "help. Vocational schools, lifelong learning institutions and "
                "the Human Resources Development Service of Korea run "
                "specialist training programmes, and it is worth using them to "
                "raise your abilities further. Taking a certificate that shows "
                "your expertise in a field, or proving experience on the job "
                "in it, both helps in finding work and may bring better terms "
                "later. So record your certificates and your experience "
                "carefully on your résumé, and at an interview make a point of "
                "showing that you are able and willing to work.",
            ],
        ),
        "취업할 때 반드시 챙겨야 할 점": dict(
            title="What to see to when you take a job",
            paragraphs=[
                "Check what the company you are applying to does, and whether "
                "it is properly registered. Once you have the job, always draw "
                "up a contract of employment, and afterwards look into the "
                "basic rights a worker holds, so as not to be treated "
                "improperly over wages or conditions. A migrant or a foreigner "
                "who runs into a problem over work would do well to ask the "
                "Ministry of Employment and Labour, the Human Resources "
                "Development Service of Korea, or the local support centre for "
                "foreign workers.",
            ],
        ),
    },

    extraAnnotations={
        "취업": dict(
            hanja="就業", meaning="taking up employment",
            characters=[("就", "취", "to take up, to proceed — as in 취직, 취학"),
                        ("業", "업", "work, trade — as in 직업, 산업")],
        ),
        "근로자": dict(
            hanja="勤勞者", meaning="a worker",
            characters=[("勤", "근", "diligent — as in 근무, 출근"),
                        ("勞", "로", "toil — as in 노동, 피로")],
            notes=["The word Korean law uses, where everyday speech says "
                   "노동자 — and the choice between them is itself political."],
        ),
        "지원 사업": dict(hanja="支援事業", meaning="a support programme"),
        "지원자": dict(
            hanja="志願者", meaning="an applicant",
            notes=["This 지원 is 志願, volunteering or applying; the 지원 of "
                   "지원 사업 is 支援, support. Same sound, opposite "
                   "direction."],
        ),
        "면접": dict(
            hanja="面接", meaning="an interview",
            characters=[("面", "면", "face — as in 장면, 반면"),
                        ("接", "접", "to meet, to touch — as in 접수, 직접")],
        ),
        "일자리": dict(meaning="a job, a position"),
        "직업": dict(
            hanja="職業", meaning="an occupation",
            characters=[("職", "직", "post — as in 직장, 재직증명서")],
        ),
        "생계": dict(
            hanja="生計", meaning="a living, livelihood",
            characters=[("計", "계", "to reckon — as in 계획, 통계")],
        ),
        "기여": dict(hanja="寄與", meaning="contribution"),
        "실업률": dict(
            hanja="失業率", meaning="the unemployment rate",
            characters=[("失", "실", "to lose — as in 실패, 실수"),
                        ("率", "률", "rate — as in 비율, 점유율")],
        ),
        "자영업": dict(
            hanja="自營業", meaning="self-employment",
            characters=[("營", "영", "to manage — as in 운영, 경영")],
            notes=["A quarter of Korean workers are 자영업자 — one of the "
                   "highest shares in the OECD, which is the article's "
                   "point."],
        ),
        "측면": dict(
            hanja="側面", meaning="an aspect, a side",
            characters=[("側", "측", "side — as in 측근")],
        ),
        "경쟁": dict(hanja="競爭", meaning="competition"),
        "치열": dict(
            hanja="熾烈", meaning="being fierce, intense",
            characters=[("熾", "치", "blazing"),
                        ("烈", "렬", "violent, ardent — as in 열렬하다")],
        ),
        "비정규직": dict(
            hanja="非正規職", meaning="irregular employment",
            characters=[("非", "비", "non-, not — as in 비공식, 비무장"),
                        ("規", "규", "rule — as in 규정, 규모")],
            notes=["Contract, temporary and daily work, set against 정규직 — "
                   "the central division in the Korean labour market."],
        ),
        "임금": dict(
            hanja="賃金", meaning="wages",
            characters=[("賃", "임", "to hire, to rent — as in 임대"),
                        ("金", "금", "money — as in 요금, 현금")],
            notes=["Not the 임금 “king” of old stories, which is native "
                   "Korean."],
        ),
        "근로 조건": dict(hanja="勤勞條件", meaning="working conditions"),
        "불리함": dict(
            headword="불리하다", hanja="不利하다",
            meaning="to be disadvantageous",
            notes=["Its opposite is 유리하다, which the next article uses."],
        ),
        "둘러싸다": dict(meaning="to surround, to be bound up with"),
        "실업자": dict(hanja="失業者", meaning="an unemployed person"),
        "취직": dict(hanja="就職", meaning="getting a job"),
        "사회보장제도": dict(
            hanja="社會保障制度", meaning="the social security system",
            notes=["Chapter 7's subject: 사회 보험, 공공 부조, 사회 서비스."],
        ),
        "맞춤형": dict(
            hanja="맞춤型", meaning="tailored, made to measure",
            notes=["From 맞추다. 맞춤옷 is a tailored suit; 맞춤형 정책 a policy "
                   "cut to fit."],
        ),
        "청년": dict(
            hanja="靑年", meaning="a young person, youth",
            characters=[("靑", "청", "blue-green, young — as in 청소년, 청와대")],
        ),
        "구직": dict(
            hanja="求職", meaning="job-seeking",
            notes=["구직 is looking for a job, 구인 looking for a worker — the "
                   "two sides of 워크넷."],
        ),
        "지원금": dict(hanja="支援金", meaning="an allowance, a grant"),
        "개인별": dict(hanja="個人別", meaning="individual, person by person"),
        "단계적": dict(hanja="段階的", meaning="step by step"),
        "실천": dict(
            hanja="實踐", meaning="putting into practice",
            characters=[("實", "실", "real — as in 사실, 실제"),
                        ("踐", "천", "to tread, to carry out")],
        ),
        "취업성공패키지": dict(
            meaning="the Employment Success Package",
            notes=["A staged programme of counselling, training and "
                   "job-placement with an allowance attached. Folded into "
                   "국민취업지원제도 in 2021, after this printing."],
        ),
        "출산": dict(hanja="出産", meaning="childbirth"),
        "육아 휴직제도": dict(
            hanja="育兒休職制度", meaning="parental leave",
            characters=[("休", "휴", "rest — as in 휴가, 휴일"),
                        ("職", "직", "post — as in 직업, 재직")],
        ),
        "권장": dict(
            hanja="勸奬", meaning="encouragement, recommending",
            characters=[("勸", "권", "to urge — as in 권유"),
                        ("奬", "장", "to encourage — as in 장려, 장학금")],
        ),
        "시간선택제": dict(
            hanja="時間選擇制", meaning="selected-hours working",
            notes=["Shorter hours of the worker's own choosing — Korea's name "
                   "for part-time work on regular terms."],
        ),
        "근무": dict(
            hanja="勤務", meaning="service, working at a job",
            characters=[("勤", "근", "diligent — as in 근로자, 출근"),
                        ("務", "무", "duty — as in 업무, 의무")],
        ),
        "증가": dict(hanja="增加", meaning="increase"),
        "은퇴": dict(
            hanja="隱退", meaning="retirement",
            characters=[("隱", "은", "to hide — as in 은둔"),
                        ("退", "퇴", "to withdraw — as in 퇴직금, 퇴근")],
        ),
        "고용": dict(
            hanja="雇傭", meaning="employment",
            characters=[("雇", "고", "to hire"),
                        ("傭", "용", "to employ")],
        ),
        "안정": dict(hanja="安定", meaning="stability"),
        "재취업": dict(hanja="再就業", meaning="re-employment"),
        "워크넷": dict(
            meaning="Work-Net",
            notes=["www.work.go.kr — the state's own job board, and where a "
                   "구직 신청 is filed."],
        ),
        "한국고용정보원": dict(
            hanja="韓國雇傭情報院",
            meaning="the Korea Employment Information Service",
        ),
        "운영": dict(hanja="運營", meaning="operation, running"),
        "구인": dict(hanja="求人", meaning="seeking a worker, recruitment"),
        "진로정보": dict(
            hanja="進路情報", meaning="career information",
            characters=[("進", "진", "to advance — as in 진행, 추진"),
                        ("路", "로", "road — as in 도로, 통로")],
            notes=["진로 is the path ahead — a school's careers guidance is "
                   "진로 상담."],
        ),
        "누리집": dict(
            meaning="a website",
            notes=["The native-Korean coinage for 홈페이지: 누리 “world” plus "
                   "집 “house”. Government sites use it by policy."],
        ),
        "통합": dict(hanja="統合", meaning="integration, unified"),
        "검색": dict(
            hanja="檢索", meaning="a search",
            characters=[("檢", "검", "to inspect — as in 검사, 검토"),
                        ("索", "색", "to seek — as in 탐색, 수색")],
        ),
        "입사": dict(
            hanja="入社", meaning="joining a company",
            notes=["Its opposite is 퇴사, leaving one."],
        ),
        "맞춤": dict(meaning="tailored to fit"),
        "조회": dict(hanja="照會", meaning="an enquiry, a look-up"),
        "출력": dict(hanja="出力", meaning="printing out, output"),
        "체류자격": dict(
            hanja="滯留資格", meaning="residence status",
            characters=[("滯", "체", "to stay — as in 체류, 정체"),
                        ("資", "자", "qualification, funds — as in 자원"),
                        ("格", "격", "standard — as in 적격, 성격")],
            notes=["The visa class — E-9, F-2, F-5 and so on — which decides "
                   "what work is open to you."],
        ),
        "범위": dict(
            hanja="範圍", meaning="a scope, a range",
            characters=[("範", "범", "model, limit — as in 모범, 규범"),
                        ("圍", "위", "to enclose — as in 주위, 포위")],
        ),
        "넓어지다": dict(meaning="to widen, to broaden"),
        "모집 공고문": dict(
            hanja="募集公告文", meaning="a recruitment notice",
            characters=[("募", "모", "to recruit — as in 공모"),
                        ("集", "집", "to gather — as in 집중, 수집"),
                        ("告", "고", "to notify — as in 광고, 신고")],
        ),
        "구인 광고": dict(hanja="求人廣告", meaning="a job advertisement"),
        "유리": dict(
            hanja="有利", meaning="being advantageous",
            characters=[("有", "유", "to have — as in 소유, 유용"),
                        ("利", "리", "profit — as in 이익, 금리")],
        ),
        "직업 학교": dict(hanja="職業學校", meaning="a vocational school"),
        "한국산업인력공단": dict(
            hanja="韓國産業人力公團",
            meaning="the Human Resources Development Service of Korea",
            notes=["HRD Korea: it runs the national skills certificates and "
                   "the EPS test that brings E-9 workers to Korea."],
        ),
        "전문성": dict(hanja="專門性", meaning="expertise"),
        "자격증": dict(
            hanja="資格證", meaning="a certificate of qualification",
            notes=["Korea runs some 500 national 자격증, from welding to "
                   "hairdressing; holding one is what 전문성 is proved by."],
        ),
        "따다": dict(
            meaning="to pick; to obtain (a certificate)",
            notes=["자격증을 따다 “to get a certificate” — the same verb as "
                   "picking fruit."],
        ),
        "현장": dict(
            hanja="現場", meaning="the site, the field",
            characters=[("現", "현", "present — as in 현재, 현금")],
        ),
        "증명": dict(hanja="證明", meaning="proof, certification"),
        "경력": dict(
            hanja="經歷", meaning="experience, a career record",
            characters=[("經", "경", "to pass through — as in 경제, 경험"),
                        ("歷", "력", "history — as in 역사, 학력")],
        ),
        "이력서": dict(
            hanja="履歷書", meaning="a résumé, a CV",
            characters=[("履", "리", "to tread, to carry out — as in 이행"),
                        ("歷", "력", "record — the same 歷 as in 경력")],
        ),
        "표현": dict(hanja="表現", meaning="expression"),
        "업체": dict(
            hanja="業體", meaning="a firm, a business",
            characters=[("體", "체", "body — as in 단체, 자치단체")],
        ),
        "정식": dict(
            hanja="正式", meaning="formal, official",
            characters=[("正", "정", "correct — as in 정확, 공정"),
                        ("式", "식", "form — as in 방식, 현대식")],
        ),
        "근로 계약서": dict(
            hanja="勤勞契約書", meaning="a contract of employment",
            characters=[("契", "계", "to contract, to pledge"),
                        ("約", "약", "promise — as in 약속, 조약")],
            notes=["Korean law requires it in writing, and a copy given to "
                   "the worker."],
        ),
        "이민자": dict(hanja="移民者", meaning="a migrant"),
        "고용노동부": dict(
            hanja="雇傭勞動部",
            meaning="the Ministry of Employment and Labour",
        ),
        "외국인 근로자 지원센터": dict(
            hanja="外國人勤勞者支援센터",
            meaning="a support centre for foreign workers",
            notes=["Regional centres offering counselling, interpreting and "
                   "Korean classes, usually at weekends. The one in the "
                   "closing story is such a centre."],
        ),
        "문의": dict(
            hanja="問議", meaning="an enquiry",
            characters=[("問", "문", "to ask — as in 질문, 방문"),
                        ("議", "의", "to discuss — as in 회의, 논의")],
        ),
        "취업 박람회": dict(
            hanja="就業博覽會", meaning="a job fair",
            characters=[("博", "박", "broad, extensive — as in 박사"),
                        ("覽", "람", "to view — as in 관람")],
        ),
        "구직자": dict(hanja="求職者", meaning="a job-seeker"),
        "적합": dict(
            hanja="適合", meaning="being suitable",
            characters=[("適", "적", "fitting — as in 적절, 적용"),
                        ("合", "합", "to match — as in 합의, 결합")],
        ),
        "추천": dict(
            hanja="推薦", meaning="a recommendation",
            characters=[("推", "추", "to push, to infer — as in 추진, 추측"),
                        ("薦", "천", "to recommend")],
        ),
        "행정 기관": dict(hanja="行政機關", meaning="an administrative body"),
        "귀국": dict(
            hanja="歸國", meaning="returning to one's country",
            characters=[("歸", "귀", "to return — as in 귀가, 복귀")],
        ),
        "성실": dict(
            hanja="誠實", meaning="being sincere, diligent",
            characters=[("誠", "성", "sincerity — as in 성의"),
                        ("實", "실", "real, faithful — as in 사실, 실천")],
            notes=["성실 근로자 is a formal category: a worker who completed "
                   "their term without incident may re-enter Korea on a new "
                   "E-9 permit."],
        ),
        "어느덧": dict(meaning="before one knows it, already"),
        "동료": dict(
            hanja="同僚", meaning="a colleague",
            characters=[("同", "동", "same — as in 동일, 공동"),
                        ("僚", "료", "an official, a companion")],
        ),
        "커뮤니티": dict(meaning="a community"),
        "다가가다": dict(meaning="to go up to someone, to approach"),
    },

    extraNotes=[
        "Chapter 29 has no Google Doc: the Korean is my reading of the photos "
        "of pp. 152-155, so it is worth checking against the pages.",
        "The OECD youth unemployment figures on p. 153 are set as a table, as "
        "the book prints them, with the caption kept as a figure beneath.",
        "The closing story is set as a quoted passage, paragraph by "
        "paragraph, which is how the book boxes it.",
        "The review gaps on p. 155 are blank in the book and left blank here.",
    ],
)
