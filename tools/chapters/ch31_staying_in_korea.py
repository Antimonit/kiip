# -*- coding: utf-8 -*-
"""Chapter 31 — Staying in Korea, and the law.

Transcribed from the photos of pp. 166-169. Your English glosses on pp. 167,
168 and 169 are carried as the entries for the words they sit over.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, MARGIN,
               TABLE, CELL, CHART, GLOSSARY)

CHAPTER = dict(
    number=31, slug="31-staying-in-korea",
    unit="법", title="한국 체류와 법", titleEn="Staying in Korea and the law",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 공항을 통해 한국에 들어올 때 입국심사를 하는 모습입니다.",
                  "Below is what immigration control looks like on entering "
                  "Korea through an airport."),
        FIGURE("공항 입국심사 줄 · 인천국제공항의 입국심사 창구"),
        HEADING(4, "01 한국 공항의 {입국심사}에서 본인이 받은 질문은 무엇이었습니까? 한국에서 입국심사를 "
                   "받을 때 어떤 {인상}을 받았습니까?",
                translation="What were you asked at immigration control at a "
                            "Korean airport? What impression did going "
                            "through it in Korea leave on you?"),
        HEADING(4, "02 다른 나라와 한국의 입국심사를 비교해 봤을 때 어떤 공통점이나 차이점이 있다고 "
                   "생각합니까?",
                translation="Comparing immigration control in Korea with "
                            "other countries, what do you think they have in "
                            "common and how do they differ?"),
        SOURCE("※ 입국심사: 다른 나라에 들어가기 전에 공항에서 받는 심사"),

        SECTION("goals", "학습목표"),
        BULLET("외국인의 한국 입국 및 {체류} 절차를 설명할 수 있다.", ordered=True,
               translation="Explain the procedure for a foreigner entering "
                           "and staying in Korea."),
        BULLET("외국인의 {정착}을 돕는 한국의 법과 제도를 설명할 수 있다.", ordered=True,
               translation="Explain the Korean laws and schemes that help "
                           "foreigners settle."),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"],
              [["기본", "법", "30. 외국인과 법", "외국인의 법적 권리와 의무"]]),

        SECTION("part", "01 외국인이 한국에 머무르려면 어떤 절차가 필요할까?"),
        GLOSSARY(("유효 기간", "어떤 물건을 정상적으로 사용할 수 있는 기간", "유효 기간"),
                 ("공중위생", "다수의 사람들에게 영향을 줄 수 있는 질병을 예방하고 건강을 유지하는 것",
                  "공중위생", "public health"),
                 ("방역", "전염병 등을 퍼지지 않도록 예방하는 것", "방역",
                  "prevention of epidemics")),
        HEADING(2, "외국인이 한국에 들어오는 과정", translation=
                "How a foreigner enters Korea" "\n\n"
                "A foreigner wishing to enter Korea must hold a passport "
                "within its period of validity and a visa. A passport is the "
                "document that certifies the nationality and the identity of "
                "someone travelling abroad. A visa, also called a 사증, means "
                "the certificate by which the Korean government permits a "
                "foreigner to enter." "\n\n"
                "Even holding a visa, one may not be able to enter if one "
                "does not pass immigration control. Permission to enter is "
                "refused, for instance, to someone suspected of having an "
                "infectious disease, to someone who might harm public health "
                "such as a drug addict, to someone carrying a dangerous "
                "object such as a gun, a knife or explosives, and to someone "
                "judged likely to harm the safety or the interests of others "
                "in Korea. And where an infectious disease is going round, "
                "as with COVID-19 in 2020, everyone entering must take a "
                "diagnostic test and follow Korea’s disease-control "
                "measures, such as isolating at home or at a facility."),
        PARAGRAPH("한국으로 들어오고자 하는 외국인은 {유효 기간}이 남아 있는 {여권}과 비자(VISA)를 "
                  "가지고 있어야 한다. 여권은 외국을 여행하는 사람의 {국적}이나 {신분}을 증명해 주는 "
                  "문서이다. 비자는 ‘{사증}’이라고도 하는데 한국 정부가 외국인의 입국을 "
                  "{허가하는|허가하다} 증명서를 의미한다."),
        PARAGRAPH("비자를 가지고 있더라도 {입국심사}를 {통과하지|통과하다} 못하면 입국하지 못할 수도 "
                  "있다. 예를 들어 {전염병}에 걸린 것으로 {의심되거나|의심되다} {마약} {중독자} 등과 "
                  "같이 {공중위생}을 {해칠|해치다} 수 있는 사람, 총이나 칼, {화약} 등과 같이 위험한 "
                  "물건을 가지고 있는 사람, 한국에서 여러 사람의 안전이나 {이익}을 해칠 가능성이 있다고 "
                  "판단되는 사람은 입국 허가를 받을 수 없다. 또한 모든 입국자는 2020년 코로나19와 같은 "
                  "{감염병} 유행 상황에서는 {진단} 검사를 받고 {자가격리}나 {시설격리} 등 한국의 "
                  "{방역} {조치}를 따라야 한다."),
        FIGURE("한국 입국자에 대한 코로나19 선별 진료소 검사 모습"),

        GLOSSARY(("체류", "어떤 지역에 오래 머물러 있는 상태", "체류"),
                 ("연수", "지식이나 기술을 연구하고 훈련함", "연수"),
                 ("투자", "사업을 하기 위해 돈을 댐", "투자")),
        HEADING(2, "외국인이 한국에 머무르는 과정", translation=
                "How a foreigner stays in Korea" "\n\n"
                "To stay in Korea a foreigner must hold a residence status. "
                "Residence status differs according to the length of stay. A "
                "short stay is one of up to 90 days for tourism, a family "
                "visit and the like; a long stay is one of more than 90 days "
                "for study, training, marriage, investment and so on." "\n\n"
                "For a long stay one must visit the immigration office with "
                "jurisdiction within 90 days of entering and register as a "
                "foreigner. Where the place of residence changes after "
                "registration, a change of residence must be reported to the "
                "immigration office or the community service centre within "
                "14 days of moving in."),
        PARAGRAPH("외국인이 한국에 머무르기 위해서는 {체류} {자격}을 갖추어야 한다. 체류 자격은 체류 "
                  "기간에 따라 다르다. {단기체류}는 관광이나 가족 방문 등을 목적으로 90일 이내로 "
                  "머무르는 것이고, {장기체류}는 유학, {연수}, 결혼, {투자} 등의 목적으로 90일을 "
                  "{초과하여|초과하다} 머무르는 것이다."),
        PARAGRAPH("장기체류를 위해서는 입국한 날로부터 90일 이내에 {관할} {출입국·외국인청}을 방문하여 "
                  "외국인으로 {등록해야|등록하다} 한다. 등록 이후에 {체류지}를 {변경한|변경하다} 경우에는 "
                  "{전입한|전입하다} 날로부터 14일 이내에 출입국·외국인청 또는 행정복지센터에 체류지 변경 "
                  "{신고}를 해야 한다."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "대한민국 비자에 대해 알아봅시다",
                translation="Let’s look at the Korean visa"),
        BULLET("비자번호: 비자발급 일련번호",
               translation="Visa number: the serial number of the visa "
                           "issued."),
        BULLET("체류자격: 외국인이 국내에 체류하면서 행할 수 있는 활동이나 신분 종류",
               translation="Residence status: the activities a foreigner may "
                           "carry out while in the country, or the kind of "
                           "status held."),
        BULLET("체류기간: 대한민국 입국일부터 체류할 수 있는 기간",
               translation="Period of stay: how long one may stay, from the "
                           "date of entry into Korea."),
        BULLET("종류: 비자의 종류(S: 단수비자, D: 더블비자, M: 복수비자)",
               translation="Type: the kind of visa (S: single entry, D: "
                           "double entry, M: multiple entry)."),
        BULLET("발급일: 비자 발급일자",
               translation="Date of issue: the date the visa was issued."),
        BULLET("입국만료일: 비자유효기간",
               translation="Final entry date: the end of the visa’s "
                           "validity."),
        BULLET("발급지: 비자를 발급한 재외공관에 대한 정보",
               translation="Issued at: which overseas mission issued the "
                           "visa."),
        FIGURE("대한민국 비자 견본 — 번호가 붙은 일곱 항목"),
        SOURCE("※ 참고: 2020년 7월부터 대한민국 비자 발급 시 여권에 부착하는 비자 스티커가 비자발급확인서로 "
               "대체되었다. 대한민국 비자포털 누리집(www.visa.go.kr)에 접속하여 여권번호, 성명, "
               "생년월일을 입력하면 즉시 확인 및 출력이 가능하다."),

        SECTION("part", "02 외국인의 정착을 돕는 법에는 어떤 것이 있을까?"),
        GLOSSARY(("재한 외국인", "한국에 있는 외국인", "재한 외국인",
                  "a foreigner residing in Korea"),
                 ("다문화", "한 사회 안에 다양한 인종, 민족, 집단, 문화 등이 어우러져 사는 현상",
                  "다문화", "multicultural"),
                 ("세계인의 날",
                  "한국 국민과 재한 외국인이 서로 존중하며 살아갈 수 있도록 2007년 한국에서 법으로 정한 "
                  "기념일", "세계인의 날")),
        HEADING(2, "재한 외국인을 지원하는 법", translation=
                "The law that supports foreigners in Korea" "\n\n"
                "Korea supports foreigners so that they can adapt to Korean "
                "society, use their abilities and live happily. The leading "
                "example is the Act on the Treatment of Foreigners Residing "
                "in Korea, made in 2007." "\n\n"
                "The Act lays down the prevention of discrimination against "
                "foreigners residing in Korea and their children, education "
                "in human rights, foreigners’ social adaptation, and the "
                "treatment of permanent residents and refugees. Under it the "
                "state and local authorities work to further understanding "
                "of a multicultural society, and 20 May each year has been "
                "set as Together Day, helping Koreans and foreigners "
                "residing here to respect each other’s culture and "
                "traditions."),
        PARAGRAPH("한국에서는 외국인이 한국 사회에 {적응하고|적응하다} 개인의 능력을 "
                  "{발휘하여|발휘하다} 행복한 생활을 할 수 있도록 지원하고 있다. 대표적인 예가 바로 "
                  "2007년에 만들어진 {재한외국인처우기본법}이다."),
        PARAGRAPH("이 법에서는 {재한 외국인}과 그 자녀에 대한 {차별} 방지 및 인권교육, 재한 외국인의 "
                  "사회 적응, {영주권자} 및 {난민}의 {처우} 등을 규정하고 있다. 이 법에 따라 국가 및 "
                  "지방자치단체에서는 {다문화}에 대한 이해를 {증진하기|증진하다} 위해 노력하고 있으며, "
                  "매년 5월 20일을 {세계인의 날}로 정하여 한국인과 재한 외국인이 서로의 문화와 전통을 "
                  "{존중하도록|존중하다} 돕고 있다."),
        FIGURE("외국인주민을 위한 시민교육 장면 (수원시 외국인복지센터)"),

        GLOSSARY(("다국어", "여러 나라의 말", "다국어", "multilingual"),
                 ("모국어", "자기 나라의 말", "모국어", "native language")),
        HEADING(2, "외국인의 편리한 생활을 돕기 위한 제도", translation=
                "The schemes that make life easier for foreigners" "\n\n"
                "Schemes that can help foreigners live more conveniently are "
                "run on the basis of the Act on the Treatment of Foreigners "
                "Residing in Korea and other laws. To solve foreigners’ "
                "difficulties in communicating, for instance, a multilingual "
                "telephone advice service is run, mainly by the Ministry of "
                "Justice, the Ministry of Gender Equality and Family and the "
                "Ministry of Employment and Labour. Someone who has not been "
                "in Korea long and cannot yet use Korean freely can be "
                "helped in their own language through this service. One can "
                "make a report or take legal advice when one’s human rights "
                "have been violated, and can also take advice on "
                "difficulties to do with work, school or family life. Korean "
                "lessons are provided as well, mainly through the foreign "
                "residents’ support centres in each area." "\n\n"
                "In Korea, where a foreign worker cannot receive medical "
                "benefits through Korean health insurance, treatment costs "
                "from admission to discharge can be supported up to five "
                "million won at a time (as of 2020). This is called the "
                "emergency medical support service, and a foreign worker can "
                "receive it by applying to a medical institution designated "
                "by one of the 17 cities and provinces."),
        PARAGRAPH("{재한외국인처우기본법} 등을 {근거}로 외국인이 보다 편리하게 생활하는 데 도움을 줄 수 "
                  "있는 제도가 실시되고 있다. 예를 들어, 외국인의 {언어소통} 문제를 해결하기 위해 "
                  "{법무부}, 여성가족부, 고용노동부 등을 중심으로 {다국어} 전화상담서비스를 실시하고 "
                  "있다. 한국에 온 지 오래되지 않아 아직 한국어를 자유롭게 하지 못하는 사람은 이 서비스를 "
                  "통해 자신의 {모국어}로 도움을 받을 수 있다. 인권을 {침해당했을|침해당하다} 때 신고나 "
                  "{법률} 상담을 받을 수도 있고 직장이나 학교, {가정}생활과 관련한 어려움에 대한 상담도 "
                  "받을 수 있다. 한편, 각 지역의 {외국인주민지원센터} 등을 중심으로 한국어 교육도 "
                  "제공하고 있다."),
        PARAGRAPH("한국에서는 외국인 근로자의 경우 한국의 건강보험 등을 통해 의료 혜택을 받을 수 없는 "
                  "상황에서도 1회 500만원 내에서 {입원}부터 {퇴원}까지 {진료비}를 지원받을 수 "
                  "있다(2020년 기준). 이를 {긴급의료지원} 서비스라고 하는데 외국인 근로자가 전국 17개 "
                  "시·도가 {지정한|지정하다} {의료기관}에 신청하여 받을 수 있다."),
        MARGIN("▶ 통역 서비스 제공 상담기관",
               "외국인종합안내센터 1345",
               "다누리콜센터 1577-1366",
               "외국인력상담센터 1577-0071"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "한국에 있는 외국인 마을을 찾아 떠나 볼까요?", translation=
                "Shall we go and find the foreigners’ quarters in Korea?" "\n\n"
                "As the number of foreigners living in Korea grows, the "
                "quarters where they live together are growing too. "
                "Well-known ones in Seoul are 한남동 (America, Europe), 이태원 "
                "(south-west Asia, Africa), 서래마을 (France), 이촌동 (Japan), "
                "광희동 (Mongolia), 창신동 (Nepal, Pakistan) and 혜화동 (the "
                "Philippines), and many people from China live in the "
                "‘Yeongdeungpo Chinatown’ that joins 대림동 and 신길동. In Ansan, "
                "Gyeonggi-do, a great many foreigners live around 원곡동, the "
                "‘village without borders’, Koryo-saram among them."),
        PARAGRAPH("한국에 거주하는 외국인이 늘어나면서 외국인이 모여 사는 외국인 마을도 증가하고 있다. "
                  "서울에서는 한남동(미국, 유럽), 이태원(서아시아, 아프리카), 서래마을(프랑스), "
                  "이촌동(일본), 광희동(몽골), 창신동(네팔, 파키스탄), 혜화동(필리핀) 등이 유명하며, "
                  "대림동과 신길동을 잇는 ‘영등포 차이나타운’에는 중국에서 온 사람들이 많이 살고 있다. "
                  "경기도 안산에는 원곡동 국경 없는 마을을 중심으로 {고려인}을 비롯한 많은 외국인이 "
                  "거주하고 있다."),
        FIGURE("여러 나라 방향과 거리를 적은 이정표"),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 외국인이 한국에 머무르려면 어떤 절차가 필요할까?"),
        BULLET("외국인이 한국에 들어오려면 여행자의 신분을 증명해 주는 문서인 (        )과 한국 "
               "정부에서 외국인의 입국을 허가하는 증명서인 (        )를 가지고 있어야 한다."),
        BULLET("관광이나 가족 방문 등을 목적으로 90일 이내로 머무르는 것은 (        )체류, 유학, "
               "결혼 등을 목적으로 90일을 초과하여 머무르는 것은 (        )체류라고 한다."),
        BULLET("장기체류를 위해서는 (        )일 이내에 관할 출입국·외국인청을 방문하여 외국인으로 "
               "등록해야 한다."),
        HEADING(3, "02 외국인의 정착을 돕는 법에는 어떤 것이 있을까?"),
        BULLET("한국에서는 외국인이 한국 사회에 잘 적응하고 행복한 생활을 할 수 있도록 지원하기 위해 "
               "(                )을 만들었다."),
        BULLET("한국어를 아직 자유롭게 하지 못하는 사람을 위해서는 그 사람의 모국어로 다양한 상담을 "
               "받을 수 있는 (                )를 제공하고 있다."),
        BULLET("건강보험 등의 혜택을 받을 수 없는 외국인이 긴급 의료 지원을 받아야 하는 경우에는 "
               "2019년 기준으로 1회 (        )원 내에서 진료비를 지원받을 수 있다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "한국에 난민이 더 많이 들어온다면?", translation=
                "What if more refugees came to Korea?" "\n\n"
                "In 2018 Yemenis came to Jeju in Korea, fleeing the war in "
                "their own country. Jeju is a place a foreigner can enter "
                "without a visa and stay for up to 30 days. When a large "
                "number of them applied to the Korean government for refugee "
                "status — a refugee being someone who has left their home "
                "country because of war, disaster, religious persecution and "
                "the like — a great deal of dispute arose within Korean "
                "society." "\n\n"
                "In the end, of the 561 who entered Jeju, as of December "
                "2019 two were recognised as refugees and 412 were given "
                "leave to stay on humanitarian grounds. Many of them worked "
                "on Jeju and tried to settle into Korean society. There have "
                "also been calls to make sure the visa-free entry Jeju set "
                "up for tourism is not misused, and the Korean government "
                "continues to work on measures for this."),
        PARAGRAPH("2018년 {예멘인}이 {자국} 내의 전쟁을 피해 한국의 제주도로 들어왔다. 제주도는 외국인이 "
                  "비자 없이 입국해서 30일까지 머물 수 있는 곳이기 때문이다. 당시 {다수}의 예멘인이 한국 "
                  "정부에 {난민}(전쟁이나 {재난}, 종교적 괴롭힘 등으로 자신의 고향 나라를 떠난 사람)을 "
                  "신청하자 이를 두고 한국 사회 내에서 수많은 {논쟁}이 벌어졌다."),
        PARAGRAPH("결국 2019년 12월 기준 제주도에 입국한 561명 중 2명이 난민으로 {인정받고|인정받다}, "
                  "412명이 {인도적} 체류허가를 받았다. 이들 중 많은 사람들이 제주도에서 일하면서 한국 "
                  "사회에 {정착하기|정착하다} 위해 노력하였다. 한편, 관광을 위해 만들어 놓은 제주도의 "
                  "{무비자} 입국 제도가 잘못 사용되지 않도록 해야 한다는 {주장}도 있어서 한국 정부가 이와 "
                  "관련한 {대책}을 계속 마련하고 있다."),
        CHART("2018년 제주에 입국한 예멘인 현황(단위: 명)", "명",
              [["인도적 체류 허가", 412],
               ["난민불인정 후 이의신청", 52],
               ["자진출국", 30],
               ["난민인정", 2]]),
        CHART("인도적 체류 중인 예멘인 취업 현황(단위: 명) — 미신고자는 미취업자, 육아, 환자, 미신고 "
              "근로자 등", "명",
              [["미신고자", 162],
               ["조선소", 145],
               ["농장", 62],
               ["양식장", 25],
               ["요식업", 17],
               ["어선", 1]]),
        SOURCE("[자료] 법무부"),
        PARAGRAPH("★ 한국 사회에 난민이 많아지면 어떤 변화가 생길까요? 한국 사회의 난민 수용에 대한 본인의 "
                  "생각을 말해 봅시다.",
                  "What changes would come if there were more refugees in "
                  "Korean society? Say what you yourself think about Korean "
                  "society taking in refugees."),
    ],

    extraAnnotations={
        "입국심사": dict(
            hanja="入國審査", meaning="immigration control, entry inspection",
            characters=[("入國", None, "entering a country"),
                        ("審査", None, "examination, screening — 審 to "
                                       "examine, 査 to investigate")],
            notes=["The page glosses it as 다른 나라에 들어가기 전에 공항에서 받는 심사."],
        ),
        "인상": dict(
            hanja="印象", meaning="an impression",
            characters=[("印", "인", "a seal, a mark — as in 인쇄 “printing”"),
                        ("象", "상", "an image — as in 상징 “symbol”, 현상")],
        ),
        "정착": dict(
            hanja="定着", meaning="settling, taking root",
            characters=[("定", "정", "to fix, settle — as in 지정, 결정"),
                        ("着", "착", "to arrive, attach — as in 도착, 착용")],
        ),
        "유효 기간": dict(
            hanja="有效期間", meaning="period of validity",
            characters=[("有效", None, "valid, in effect — 有 to have, 效 effect"),
                        ("期間", None, "a period of time")],
        ),
        "여권": dict(
            hanja="旅券", meaning="a passport",
            characters=[("旅", "려", "travel — as in 여행 “travel”, 여객"),
                        ("券", "권", "a ticket, a certificate — as in 상품권, 승차권")],
        ),
        "국적": dict(
            hanja="國籍", meaning="nationality",
            characters=[("國", "국", "country"),
                        ("籍", "적", "a register — as in 호적, 본적")],
            notes=["Chapter 32’s subject: what nationality means and who "
                   "counts as a Korean national."],
        ),
        "신분": dict(
            hanja="身分", meaning="identity; social standing",
            characters=[("身", "신", "body, self — as in 신체, 자신"),
                        ("分", "분", "a part, a share — as in 분리, 부분")],
        ),
        "사증": dict(
            hanja="査證", meaning="a visa (the formal Korean word)",
            characters=[("査", "사", "to investigate — the same 査 as in 입국심사"),
                        ("證", "증", "a certificate — as in 증명서, 영수증")],
        ),
        "허가하다": dict(
            hanja="許可하다", meaning="to permit, to grant leave",
            characters=[("許", "허", "to allow — as in 허락, 특허"),
                        ("可", "가", "possible, permissible — as in 가능")],
            surfaces=["허가하는"],
        ),
        "통과하다": dict(
            hanja="通過하다", meaning="to pass through, to get through",
            characters=[("通", "통", "to pass — as in 통행, 교통"),
                        ("過", "과", "to pass by, exceed — as in 과정, 초과")],
            surfaces=["통과하지"],
        ),
        "전염병": dict(
            hanja="傳染病", meaning="a contagious disease, a plague",
            characters=[("傳", "전", "to transmit — as in 전달, 전통"),
                        ("染", "염", "to dye, to be infected — as in 감염, 오염"),
                        ("病", "병", "illness")],
        ),
        "의심되다": dict(
            hanja="疑心되다", meaning="to be suspected",
            characters=[("疑", "의", "to doubt — as in 의문, 피의자"),
                        ("心", "심", "heart, mind — as in 심리, 관심")],
            surfaces=["의심되거나"],
        ),
        "마약": dict(
            hanja="痲藥", meaning="a narcotic drug",
            characters=[("痲", "마", "numbness, paralysis"),
                        ("藥", "약", "medicine — as in 약국, 화약")],
        ),
        "중독자": dict(
            hanja="中毒者", meaning="an addict",
            characters=[("中毒", None, "poisoning, addiction — 中 to be struck, "
                                       "毒 poison"),
                        ("者", "자", "person")],
        ),
        "공중위생": dict(
            hanja="公衆衛生", meaning="public health",
            characters=[("公衆", None, "the public, the general body of people"),
                        ("衛生", None, "hygiene — 衛 to guard, 生 life")],
        ),
        "감염병": dict(
            hanja="感染病", meaning="an infectious disease",
            characters=[("感染", None, "infection — 感 to feel, 染 to be dyed"),
                        ("病", "병", "illness — as in 전염병, 질병")],
        ),
        "해치다": dict(
            meaning="to harm, to damage",
            notes=["공중위생을 해치다 “to harm public health”; 안전을 해치다 is "
                   "chapter 8’s phrase."],
            surfaces=["해칠"],
        ),
        "화약": dict(
            hanja="火藥", meaning="gunpowder, explosives",
            characters=[("火", "화", "fire — as in 화재 “fire”, 화산"),
                        ("藥", "약", "medicine, chemical — the same 藥 as in 마약")],
        ),
        "이익": dict(
            hanja="利益", meaning="benefit, profit, interests",
            characters=[("利", "리", "benefit — as in 이해관계, 권리"),
                        ("益", "익", "gain — as in 유익하다 “beneficial”")],
        ),
        "진단": dict(
            hanja="診斷", meaning="a diagnosis",
            characters=[("診", "진", "to examine (medically) — as in 진료, 진찰"),
                        ("斷", "단", "to decide, cut off — as in 판단, 단절")],
        ),
        "자가격리": dict(
            hanja="自家隔離", meaning="self-isolation at home",
            characters=[("自家", None, "one’s own home"),
                        ("隔離", None, "isolation — 隔 to separate, 離 to part")],
        ),
        "시설격리": dict(
            hanja="施設隔離", meaning="isolation at a facility",
        ),
        "방역": dict(
            hanja="防疫", meaning="disease control, keeping an epidemic from "
                                 "spreading",
            characters=[("防", "방", "to guard against — as in 예방, 방지"),
                        ("疫", "역", "an epidemic — as in 면역 “immunity”")],
        ),
        "조치": dict(
            hanja="措置", meaning="a measure, a step taken",
            characters=[("措", "조", "to arrange, handle"),
                        ("置", "치", "to place — as in 설치, 위치")],
        ),
        "체류": dict(
            hanja="滯留", meaning="staying, sojourn",
            characters=[("滯", "체", "to stay, be delayed — as in 정체, 체증"),
                        ("留", "류", "to remain — as in 유학 “study abroad”")],
        ),
        "자격": dict(
            hanja="資格", meaning="status, qualification",
            characters=[("資", "자", "resources, means — as in 자원, 투자"),
                        ("格", "격", "standard, rank — as in 성격, 합격")],
            notes=["체류 자격 is the residence status a visa carries."],
        ),
        "단기체류": dict(
            hanja="短期滯留", meaning="a short stay (up to 90 days)",
            characters=[("短期", None, "short term — 短 short, 期 period")],
        ),
        "장기체류": dict(
            hanja="長期滯留", meaning="a long stay (more than 90 days)",
            characters=[("長期", None, "long term — 長 long, 期 period")],
        ),
        "연수": dict(
            hanja="硏修", meaning="training, a course of study",
            characters=[("硏", "연", "to study, grind — as in 연구 “research”"),
                        ("修", "수", "to cultivate, mend — as in 수리, 수업")],
        ),
        "투자": dict(
            hanja="投資", meaning="investment",
            characters=[("投", "투", "to throw, put in — as in 투표 “vote”"),
                        ("資", "자", "resources, capital — the same 資 as in 자격")],
        ),
        "초과하다": dict(
            hanja="超過하다", meaning="to exceed",
            characters=[("超", "초", "to exceed, super- — as in 초월, 초등"),
                        ("過", "과", "to pass, exceed — the same 過 as in 통과")],
            surfaces=["초과하여"],
        ),
        "관할": dict(
            hanja="管轄", meaning="jurisdiction; the office with jurisdiction",
            characters=[("管", "관", "to manage — as in 관리, 관공서"),
                        ("轄", "할", "to control, an axle pin")],
        ),
        "출입국·외국인청": dict(
            meaning="the immigration office",
            notes=["출입국 leaving and entering the country, 외국인청 the "
                   "foreigners’ office. Registration and changes of address "
                   "are done here."],
        ),
        "등록하다": dict(
            hanja="登錄하다", meaning="to register",
            characters=[("登", "등", "to climb, to record — as in 등산, 등기"),
                        ("錄", "록", "to record — as in 기록, 목록")],
            surfaces=["등록해야"],
        ),
        "체류지": dict(
            hanja="滯留地", meaning="the place where one is staying",
            characters=[("地", "지", "place — as in 지역, 주소지")],
        ),
        "변경하다": dict(
            hanja="變更하다", meaning="to change, to alter",
            characters=[("變", "변", "to change — as in 변화, 변동"),
                        ("更", "경", "again, to renew — as in 갱신")],
            surfaces=["변경한"],
        ),
        "전입하다": dict(
            hanja="轉入하다", meaning="to move in (to a new address)",
            characters=[("轉", "전", "to turn, transfer — as in 이전, 전학"),
                        ("入", "입", "to enter — as in 입국, 입원")],
            surfaces=["전입한"],
        ),
        "신고": dict(
            hanja="申告", meaning="a report, a notification (to authorities)",
            characters=[("申", "신", "to state, apply — as in 신청, 신고"),
                        ("告", "고", "to tell — as in 보고, 광고")],
        ),
        "재한 외국인": dict(
            hanja="在韓外國人", meaning="a foreigner residing in Korea",
            characters=[("在", "재", "to be at, reside — as in 재외국민, 현재"),
                        ("韓", "한", "Korea")],
        ),
        "적응하다": dict(
            hanja="適應하다", meaning="to adapt, to adjust",
            characters=[("適", "적", "suitable — as in 적합, 적용"),
                        ("應", "응", "to respond — as in 응답, 호응")],
            surfaces=["적응하고"],
        ),
        "발휘하다": dict(
            hanja="發揮하다", meaning="to display, to bring out (an ability)",
            characters=[("發", "발", "to send out — as in 발행, 발급"),
                        ("揮", "휘", "to wield, wave — as in 지휘 “command”")],
            surfaces=["발휘하여"],
        ),
        "재한외국인처우기본법": dict(
            hanja="在韓外國人處遇基本法",
            meaning="the Act on the Treatment of Foreigners Residing in Korea",
            characters=[("處遇", None, "treatment, how someone is dealt with"),
                        ("基本法", None, "a framework act")],
            notes=["Made in 2007. Chapter 21’s 이야기 나누기 has migrant groups "
                   "arguing about how it works in practice."],
        ),
        "차별": dict(
            hanja="差別", meaning="discrimination",
            characters=[("差", "차", "difference — as in 차이, 격차"),
                        ("別", "별", "to distinguish — as in 구별, 특별")],
        ),
        "영주권자": dict(
            hanja="永住權者", meaning="a permanent resident",
            characters=[("永住權", None, "permanent residence — chapter 30"),
                        ("者", "자", "person")],
        ),
        "난민": dict(
            hanja="難民", meaning="a refugee",
            characters=[("難", "난", "difficulty, hardship — as in 취업난, 재난"),
                        ("民", "민", "the people — as in 국민, 이주민")],
            notes=["The page glosses it as 전쟁이나 재난, 종교적 괴롭힘 등으로 자신의 "
                   "고향 나라를 떠난 사람."],
        ),
        "처우": dict(
            hanja="處遇", meaning="treatment, how someone is treated",
            characters=[("處", "처", "to handle, a place — as in 처리, 부처"),
                        ("遇", "우", "to meet, to treat — as in 대우")],
        ),
        "다문화": dict(
            hanja="多文化", meaning="multicultural",
            characters=[("多", "다", "many — as in 다수, 다국어"),
                        ("文化", None, "culture")],
        ),
        "증진하다": dict(
            hanja="增進하다", meaning="to further, to promote",
            characters=[("增", "증", "to increase — as in 증가, 증대"),
                        ("進", "진", "to advance — as in 진학, 진출")],
            surfaces=["증진하기"],
        ),
        "세계인의 날": dict(
            meaning="Together Day (20 May)",
            notes=["Set in law in 2007 so that Koreans and foreigners "
                   "residing here live in mutual respect."],
        ),
        "존중하다": dict(
            hanja="尊重하다", meaning="to respect",
            characters=[("尊", "존", "to revere — as in 존귀, 존엄"),
                        ("重", "중", "heavy, important — as in 중요, 중시")],
            surfaces=["존중하도록"],
        ),
        "근거": dict(
            hanja="根據", meaning="a basis, grounds",
            characters=[("根", "근", "a root — as in 근본, 근원"),
                        ("據", "거", "to rely on — as in 의거, 증거")],
        ),
        "언어소통": dict(
            hanja="言語疏通", meaning="communicating in a language",
            characters=[("言語", None, "language"),
                        ("疏通", None, "communication — 疏 to clear, 通 to pass")],
        ),
        "법무부": dict(
            hanja="法務部", meaning="the Ministry of Justice",
            characters=[("法務", None, "legal affairs"),
                        ("部", "부", "a ministry — as in 행정부, 교육부")],
        ),
        "다국어": dict(
            hanja="多國語", meaning="multilingual, in several languages",
            characters=[("多", "다", "many — the same 多 as in 다문화"),
                        ("國語", None, "a national language")],
        ),
        "모국어": dict(
            hanja="母國語", meaning="one’s mother tongue",
            characters=[("母", "모", "mother — as in 모유, 모녀"),
                        ("國語", None, "national language")],
        ),
        "침해당하다": dict(
            hanja="侵害당하다", meaning="to have one’s rights violated",
            characters=[("侵", "침", "to invade, encroach — as in 침입, 침략"),
                        ("害", "해", "harm — as in 피해, 해치다")],
            surfaces=["침해당했을"],
        ),
        "법률": dict(
            hanja="法律", meaning="a law, legislation",
            characters=[("法", "법", "law"),
                        ("律", "률", "a rule, a statute — as in 규율, 자율")],
        ),
        "가정": dict(
            hanja="家庭", meaning="the home, the household",
            characters=[("家", "가", "house, family — as in 가족, 국가"),
                        ("庭", "정", "a courtyard — as in 정원 “garden”")],
        ),
        "외국인주민지원센터": dict(
            meaning="a foreign residents’ support centre",
            notes=["Runs Korean lessons and advice services in each area."],
        ),
        "입원": dict(
            hanja="入院", meaning="admission to hospital",
            characters=[("入", "입", "to enter — the same 入 as in 입국"),
                        ("院", "원", "an institution — as in 병원, 법원")],
        ),
        "퇴원": dict(
            hanja="退院", meaning="discharge from hospital",
            characters=[("退", "퇴", "to withdraw — as in 은퇴, 퇴사"),
                        ("院", "원", "institution")],
        ),
        "진료비": dict(
            hanja="診療費", meaning="treatment costs, medical fees",
            characters=[("診療", None, "medical treatment — 診 to examine, "
                                       "療 to treat"),
                        ("費", "비", "expense — as in 학비, 생계비")],
        ),
        "긴급의료지원": dict(
            hanja="緊急醫療支援", meaning="emergency medical support",
            characters=[("緊急", None, "urgent, emergency — as in 긴급 신고"),
                        ("醫療", None, "medical care"),
                        ("支援", None, "support")],
        ),
        "지정하다": dict(
            hanja="指定하다", meaning="to designate",
            characters=[("指", "지", "to point — as in 지시, 지적"),
                        ("定", "정", "to fix — the same 定 as in 정착")],
            surfaces=["지정한"],
        ),
        "의료기관": dict(
            hanja="醫療機關", meaning="a medical institution",
            characters=[("醫療", None, "medical care"),
                        ("機關", None, "an institution, a body — as in 국가 기관")],
        ),
        "고려인": dict(
            hanja="高麗人", meaning="Koryo-saram, ethnic Koreans of the former "
                                  "Soviet Union",
            characters=[("高麗", None, "Goryeo, the old name of Korea"),
                        ("人", "인", "person")],
        ),
        "예멘인": dict(meaning="a Yemeni"),
        "자국": dict(
            hanja="自國", meaning="one’s own country",
            characters=[("自", "자", "self — as in 자신, 자율"),
                        ("國", "국", "country")],
        ),
        "다수": dict(
            hanja="多數", meaning="a large number, the majority",
            characters=[("多", "다", "many — the same 多 as in 다문화"),
                        ("數", "수", "number — as in 수명, 인원")],
            notes=["다수결의 원칙 “majority rule” is chapter 20’s phrase."],
        ),
        "재난": dict(
            hanja="災難", meaning="a disaster",
            characters=[("災", "재", "calamity — as in 재해, 화재"),
                        ("難", "난", "difficulty — the same 難 as in 난민")],
        ),
        "논쟁": dict(
            hanja="論爭", meaning="a dispute, controversy",
            characters=[("論", "론", "to argue, discuss — as in 논의, 이론"),
                        ("爭", "쟁", "to contend — as in 경쟁 “competition”")],
        ),
        "인정받다": dict(
            hanja="認定받다", meaning="to be recognised (as)",
            characters=[("認", "인", "to acknowledge — as in 인식, 승인"),
                        ("定", "정", "to fix, settle")],
            surfaces=["인정받고"],
        ),
        "인도적": dict(
            hanja="人道的", meaning="humanitarian",
            characters=[("人道", None, "humanity, the human way"),
                        ("的", "적", "the adjective suffix")],
            notes=["인도적 체류허가 is leave to stay on humanitarian grounds — "
                   "short of refugee status."],
        ),
        "정착하다": dict(
            hanja="定着하다", meaning="to settle, to put down roots",
            surfaces=["정착하기"],
        ),
        "무비자": dict(
            meaning="visa-free",
            notes=["Jeju lets a foreigner enter without a visa and stay up "
                   "to 30 days."],
        ),
        "주장": dict(
            hanja="主張", meaning="an assertion, a claim, a call for",
            characters=[("主", "주", "main, master — as in 주인, 민주주의"),
                        ("張", "장", "to stretch, spread — as in 긴장, 확장")],
        ),
        "대책": dict(
            hanja="對策", meaning="a countermeasure, a plan to deal with",
            characters=[("對", "대", "facing, against — as in 대응, 대비"),
                        ("策", "책", "a plan — as in 정책 “policy”")],
        ),
    },

    extraNotes=[
        "The two 생각해 봅시다 photographs on p. 166 (an immigration hall and "
        "the desks at Incheon airport), the visa specimen on p. 167 and the "
        "signpost photograph on p. 168 are not reproduced; their captions and "
        "the numbered visa fields are.",
        "The two figures on p. 169 are bar charts of the Yemeni arrivals on "
        "Jeju and of what those with humanitarian leave went on to do; both "
        "are set as charts.",
        "The review gaps on p. 169 are blank in the book and left blank here. "
        "The last of them says 2019년 기준 where the article on p. 168 says "
        "2020년 기준; both are set as printed.",
    ],
)
