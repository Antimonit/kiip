# -*- coding: utf-8 -*-
"""Chapter 23 — The judiciary.

Transcribed from the photos of pp. 122-125; there is no Google Doc for it.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, TABLE,
               CELL, GLOSSARY)

CHAPTER = dict(
    number=23, slug="23-judiciary",
    unit="정치", title="사법부", titleEn="The judiciary",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음 그림은 {법원}에서 {재판}하는 모습입니다."),
        FIGURE("법정에서 재판이 열리는 모습 — 판사석에 세 사람, 옆에 검사와 변호인, 앞에 앉은 "
            "피고인"),
        HEADING(4, "01 재판에서 누가 어떤 일을 할까요?"),
        HEADING(4, "02 사람들 사이에 {다툼}이 있을 때, 어디에 도움을 구할 수 있을까요?"),

        SECTION("goals", "학습목표"),
        BULLET("사법부의 의미와 구성에 대해 설명할 수 있다.", ordered=True),
        BULLET("법원의 역할과 {공정}한 재판을 위한 노력을 설명할 수 있다.", ordered=True),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", 2), "제목", "관련 내용"],
              [["기본", "정치", "20. 한국의 민주 정치", "권력 분립"],
               ["심화", "정치", "9. 정치 과정과 시민 참여", "정치 과정"]]),

        SECTION("part", "01 재판은 누가 할까?"),
        HEADING(2, "법원이라고 불리는 사법부"),
        GLOSSARY(("분쟁", "말썽을 일으켜 다툼", "분쟁"),
              ("처벌", "벌을 줌", "처벌")),
        PARAGRAPH("국회에서 만든 법을 모든 사람이나 기관이 다 잘 지키면 좋겠지만 누군가 {어기는|어기다} "
          "경우가 생긴다. 또한, 일상생활을 하다 보면 서로 {다툼}이 생기기도 한다. 이때 누군가가 "
          "정말 법을 어겼는지, 법을 어겼다면 어떤 {대가}를 {치러야|치르다} 하는지, 다툼을 "
          "해결하기 위해서는 어떻게 해야 하는지 등에 대해 정확한 {판단}을 내려야 한다."),
        PARAGRAPH("{재판}을 통해 그러한 판단을 내려주는 기관이 {사법부}이다. 사법부는 법을 {해석}하고 "
          "{적용}하여 사람들 사이의 {분쟁}을 해결하고, 법을 어긴 사람이 있으면 그 잘못에 대해 법에 "
          "따라 {처벌}하기도 한다. 사법부는 {법원}이라고도 불린다."),

        HEADING(2, "법원의 구성"),
        GLOSSARY(("판결", "법원이 소송 사건에 대하여 판단하고 결정을 내림", "판결")),
        PARAGRAPH("법원의 종류에는 {대법원}, {고등법원}, {지방법원}, {가정법원} 등이 있다. 지방법원은 "
          "18개로 전국의 {주요} 지방에 {설치}되어 있다. 일반적으로 {해당} 지역에서 발생한 "
          "{사건}이나 분쟁에 관한 재판을 {진행}한다. 가정법원은 가족이나 {친척} 관계, {소년} 문제 "
          "등에 관한 재판을 {전문적}으로 담당한다."),
        PARAGRAPH("지방법원이나 가정법원의 {판결}을 받아들일 수 없는 경우에는 고등법원에서 다시 재판을 "
          "받을 수 있다. 고등법원은 모두 6개로 서울, 부산, 대구, 광주, 대전, 수원에 각각 설치되어 "
          "있다. 고등법원의 판결도 받아들일 수 없는 경우에는 대법원으로 사건을 가져갈 수 있다. "
          "대법원은 사법부에서 가장 높은 기관으로 {대법원장} 1명과 그 외 {대법관} 13명으로 "
          "구성되어 있다. 대법원에서 판결한 내용은 법원의 {최종적}인 판단으로 {인정받으며|인정받다} "
          "{변경}할 수 없다."),
        FIGURE("서울특별시 서초구 대법원 청사"),
        FIGURE("대법원장 임명장 수여 모습 (사진출처: 〈연합뉴스〉)"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "소송 구조 제도 안내책, 이젠 16개국 언어로 읽자!"),
        PARAGRAPH("{법원행정처}가 다문화 가족, 이주민 근로자 등의 권리 보호를 위한 {소송 구조} 제도 안내 "
          "책자를 영어, 러시아어, 중국어, 베트남어 등 16개 언어로 {번역}해 {발간}했다. 소송 구조 "
          "제도는 재판 {과정}에 필요한 돈을 내기 어려운 사람들을 {대상}으로 {변호사} 비용 등을 "
          "면제해 주거나 {납부} 기간을 {연장}해 주는 제도다. 법원행정처는 “번역된 소송 구조 제도 "
          "안내 책자를 통해 {내국인}은 물론 다문화 가족과 {국내} {거주} 외국인 근로자 등에 대한 "
          "소송 구조 제도가 {활성화}되고 권리 {구제} 기회가 늘어날 것으로 {기대}된다.”라고 "
          "{밝혔다|밝히다}."),
        SOURCE("[출처] 법률신문뉴스(2019.08.28)"),

        SECTION("part", "02 법원은 어떤 일을 할까?"),
        HEADING(2, "재판을 통한 권리 보호와 질서 유지"),
        PARAGRAPH("일상생활에서 사람들 사이의 크고 작은 다툼이 생기기도 하고 국가나 {지방자치단체}의 "
          "잘못으로 개인이나 {기업}이 피해를 입기도 한다. 또한, 자신의 {욕심} 때문에 법을 어기고 "
          "사회에 피해를 {끼치는|끼치다} 일도 발생한다. 이러한 경우에 법원은 법에 따른 재판을 "
          "통해 다툼을 해결하고 잘못을 바로잡는다. 이는 국민의 권리와 이익을 보호하고 사회 "
          "{질서}를 {유지}하기 위한 것이다."),
        FIGURE("공개 재판 방청 모습 (사진 출처: 〈연합뉴스〉)"),

        HEADING(2, "공정한 재판을 위한 제도"),
        GLOSSARY(("공정", "공평하고 올바름", "공정"),
              ("양심", "착하고 나쁨을 구별하는 도덕적 의식이나 마음씨", "양심"),
              ("재판부", "재판을 담당하고 이끌어가는 판사(들)", "재판부")),
        PARAGRAPH("재판이 {공정}하게 이루어져야 국민의 권리를 보호하고 질서를 유지할 수 있다. 이를 위해 "
          "한국에서는 몇 가지 제도를 실시하고 있다."),
        PARAGRAPH("첫째, 사법부의 {독립}을 헌법에서 {보장}하고 있다. 재판을 담당하는 {판사}({법관})에게 "
          "그 누구도 {간섭}할 수 없고 판사는 {오직} 헌법과 법률과 {양심}에 따라 재판해야 한다."),
        PARAGRAPH("둘째, 같은 사건에 대해 재판을 세 번까지 받을 수 있다. 일반적인 사건이라면 "
          "지방법원(1심), 고등법원(2심)을 {거쳐|거치다} 대법원(3심)의 판결까지 받을 수 있다. 이를 "
          "{삼심제}라고 한다."),
        PARAGRAPH("셋째, 재판 과정은 특별한 이유가 없다면 공개한다. {재판부}의 {허가}가 있으면 재판 "
          "{장면}의 일부를 {촬영}하거나 {중계방송}을 할 수도 있다."),

        HEADING(2, "재판의 종류"),
        GLOSSARY(("가사", "가정과 관계된 일", "가사"),
              ("상속", "물려주고 이어받는 것", "상속")),
        PARAGRAPH("재판에는 {민사 재판}, {형사 재판}, {가사} 재판 등이 있다. 민사 재판은 사람들 간의 "
          "다툼을 해결하기 위한 재판이다. 예를 들어 아파트 {층간 소음}으로 {인해} 누군가 피해를 "
          "입고 그와 관련해 다툼이 일어났다면 민사 재판을 통해 피해의 {정도}를 결정할 수 있다. "
          "형사 재판은 범죄와 형벌을 결정하기 위한 재판이다. 예를 들어, 다른 사람의 물건을 "
          "{훔쳐|훔치다} 간 사람이 있다면 형사 재판을 통해 그 사람에게 어떤 {죄}를 "
          "{묻고|죄를 묻다} 벌을 얼마나 줘야 하는지 결정할 수 있다. 가사 재판은 결혼, 이혼, 재산 "
          "{상속}, 자녀 {양육} 등과 관련된 분쟁을 해결하기 위한 재판이다."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "대법원의 결정이 우리 생활에 영향을 준다"),
        PARAGRAPH("‘환경 {오염} {우려}’를 이유로 {폐기물} 시설 {허락}하지 않은 결정은 {정당}하다!"),
        PARAGRAPH("거주 지역과 가까운 곳에 폐기물 {재활용} 시설을 설치하지 못하도록 한 지방자치단체의 "
          "결정이 정당하다는 대법원의 판결이 나왔다. A사는 ○○군에 폐기물 재활용 시설 설치를 "
          "허가해 달라는 사업 계획서를 제출했으나, ○○군은 이를 거부했다. 대법원은 “환경은 한 번 "
          "오염되면 {원래대로} {회복}하는 것이 거의 {불가능}하므로 오염되지 않도록 {예방}하는 "
          "것이 중요하다. ○○군 주민의 건강이나 주변 환경에 {미칠|미치다} 수 있는 {부정적}인 "
          "영향을 이유로 {부적합} {통보}를 한 것은 {위법}이 아니다.”라고 하였다."),
        SOURCE("[출처] 연합뉴스(2020.01.20)"),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 재판은 누가 할까?"),
        BULLET("(          )는 법을 해석하고 적용하여 문제를 해결하고 사회 질서를 유지한다."),
        BULLET("(          )은 가족이나 친척 관계, 소년 문제 등에 관한 재판을 전문적으로 담당한다."),
        BULLET("사법부에서 가장 높은 기관은 (        )으로 여기서는 최종적인 판결을 내린다."),
        HEADING(3, "02 법원은 어떤 일을 할까?"),
        BULLET("법원은 법에 따른 재판을 통해 다툼을 해결하고 잘못을 바로잡는다. 이는 국민의 "
          "(      )와 이익을 보호하고 사회 질서 유지를 위한 것이다."),
        BULLET("공정한 재판을 위해 같은 사건에 대해 일반적으로 (  )번까지 재판을 받을 수 있다."),
        BULLET("(      ) 재판은 사람들 간의 다툼을 해결하기 위한 재판이고, (      ) 재판은 범죄와 "
          "형벌에 관한 재판이다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "피의자(범죄를 저질렀을 것으로 의심받는 사람)의 인권도 보호해요!", translation=
          "The human rights of a suspect — someone suspected of having "
          "committed a crime — are protected too!"),
        BULLET("{영장주의}: 사람을 체포하거나 {구속}할 때, 누군가의 물건을 {압수}하거나 어떤 장소를 "
          "{수색}(찾아서 조사)할 때는 반드시 법원이 {발행}한 {영장}(명령을 담은 문서)을 "
          "{제시}해야 해요.",
          translation="The warrant principle: to arrest or detain someone, "
                      "to seize someone’s property or to search a place, a "
                      "warrant — a document carrying the order — issued by "
                      "a court must always be produced."),
        BULLET("{미란다원칙}: 사람을 체포할 때는 다음과 같은 내용을 말해 주어야 한다. “당신은 "
          "{변호인}을 {선임}할 권리가 있고 {변명}의 기회가 있다. 이 체포가 부당하다고 생각하면 "
          "법원에 {심사}를 {요청}할 권리가 있다.”",
          translation="The Miranda rule: when arresting someone the "
                      "following must be said to them. “You have the right "
                      "to appoint a lawyer and the chance to speak in your "
                      "defence. If you think this arrest is unjust, you "
                      "have the right to ask a court to review it.”"),
        BULLET("{무죄추정의 원칙}: 재판을 통해 최종적으로 {유죄} 판결이 확정되기 전까지는 {무죄}인 "
          "것으로 {추측}하여 판단한다.",
          translation="The presumption of innocence: until a verdict of "
                      "guilt is finally settled through a trial, one is "
                      "taken to be innocent."),
        FIGURE("미란다 원칙 고지 — “당신은 묵비권을 행사할 권리가 있고…”"),
        PARAGRAPH("★ {피의자}의 인권을 보호해야 하는 이유는 무엇일까요? 자신의 고향 나라에서는 피의자의 "
          "인권을 어떻게 보호하는지 이야기해 봅시다.",
          "Why must a suspect’s human rights be protected? Talk about how "
          "your home country protects the human rights of a suspect."),
    ],

    english={
        "법원이라고 불리는 사법부": dict(
            title="The judiciary, called the courts",
            paragraphs=[
                "It would be well if every person and every institution kept "
                "the laws the Assembly makes, but cases arise where someone "
                "breaks them. Quarrels between people arise too in the "
                "ordinary course of life. In such a case an accurate judgment "
                "has to be reached: whether someone really did break the law, "
                "what price they must pay if they did, and what should be "
                "done to settle the quarrel.",

                "The body that reaches such judgments, by trial, is the "
                "judiciary. The judiciary interprets and applies the law to "
                "settle disputes between people, and where someone has broken "
                "the law it may also punish them for the wrong according to "
                "law. The judiciary is also called the courts.",
            ],
        ),
        "법원의 구성": dict(
            title="How the courts are made up",
            paragraphs=[
                "The kinds of court include the Supreme Court, the high "
                "courts, the district courts and the family courts. There are "
                "eighteen district courts, set up in the main localities "
                "across the country. Ordinarily they hear cases and disputes "
                "that have arisen in their own area. The family courts deal "
                "specially with cases about family or kinship and about "
                "juveniles.",

                "Where the judgment of a district or family court cannot be "
                "accepted, the case may be heard again in a high court. There "
                "are six high courts in all, in Seoul, Busan, Daegu, Gwangju, "
                "Daejeon and Suwon. Where a high court's judgment cannot be "
                "accepted either, the case may be taken to the Supreme Court. "
                "The Supreme Court is the highest body in the judiciary, made "
                "up of the Chief Justice and thirteen other justices. What it "
                "decides is recognised as the courts' final judgment and "
                "cannot be altered.",
            ],
        ),
        "재판을 통한 권리 보호와 질서 유지": dict(
            title="Protecting rights and keeping order through trial",
            paragraphs=[
                "Quarrels great and small arise between people in the "
                "ordinary course of life, and an individual or a company may "
                "suffer harm through the fault of the state or a local "
                "authority. It happens too that someone breaks the law out of "
                "their own greed and does the community harm. In such cases "
                "the courts settle the quarrel and put the wrong right "
                "through a trial according to law. This is to protect the "
                "people's rights and interests and to keep order in society.",
            ],
        ),
        "공정한 재판을 위한 제도": dict(
            title="The arrangements for a fair trial",
            paragraphs=[
                "Only if a trial is conducted fairly can the people's rights "
                "be protected and order kept. Korea has several arrangements "
                "to that end.",

                "First, the independence of the judiciary is guaranteed by "
                "the constitution. No one may interfere with the judge who "
                "hears a case, and a judge must try it according to the "
                "constitution, the law and their conscience alone.",

                "Second, the same case may be tried up to three times. An "
                "ordinary case may go from the district court at first "
                "instance through a high court at second instance to a "
                "judgment of the Supreme Court at third. This is called the "
                "three-instance system.",

                "Third, the course of a trial is open unless there is a "
                "particular reason otherwise. With the court's permission "
                "part of the proceedings may be filmed or broadcast.",
            ],
        ),
        "재판의 종류": dict(
            title="Kinds of trial",
            paragraphs=[
                "Trials are civil, criminal, or in family matters. A civil "
                "trial is for settling a quarrel between people. If someone "
                "has suffered from noise between the floors of a block of "
                "flats and a quarrel has arisen over it, a civil trial can "
                "settle the extent of the harm. A criminal trial is for "
                "settling the offence and the punishment. If someone has "
                "stolen another's property, a criminal trial can settle what "
                "offence they are to answer for and how much punishment they "
                "should receive. A trial in family matters is for settling "
                "disputes to do with marriage, divorce, the inheritance of "
                "property, the raising of children and the like.",
            ],
        ),
    },

    extraAnnotations={
        "사법부": dict(
            hanja="司法部", meaning="the judiciary",
            characters=[("司", "사", "to take charge of — as in 사회자"),
                        ("法", "법", "law — as in 법원, 입법부"),
                        ("部", "부", "branch — as in 행정부, 입법부")],
        ),
        "법원": dict(
            hanja="法院", meaning="a court of law",
            characters=[("院", "원", "institution, house — as in 병원, 학원")],
        ),
        "재판": dict(
            hanja="裁判", meaning="a trial",
            characters=[("裁", "재", "to judge, to cut out — as in 재량"),
                        ("判", "판", "to judge — as in 판단, 판결")],
        ),
        "다툼": dict(
            meaning="a quarrel, a dispute",
            notes=["From 다투다 “to quarrel”. The plain Korean the book uses "
                   "beside 분쟁."],
        ),
        "어기다": dict(meaning="to break, to violate (a law, a promise)"),
        "대가": dict(
            hanja="代價", meaning="a price to pay",
            characters=[("代", "대", "to substitute — as in 대표, 시대"),
                        ("價", "가", "price, value — as in 물가, 평가")],
        ),
        "치르다": dict(
            meaning="to pay, to go through (an ordeal)",
            notes=["대가를 치르다 “to pay the price”. Not 치다."],
        ),
        "판단": dict(
            hanja="判斷", meaning="a judgment, a decision",
            characters=[("判", "판", "to judge — as in 판사, 판결"),
                        ("斷", "단", "to cut off, to decide — as in 단절")],
        ),
        "해석": dict(
            hanja="解釋", meaning="interpretation",
            characters=[("解", "해", "to loosen, to solve — as in 해결, 이해"),
                        ("釋", "석", "to explain, to release")],
        ),
        "적용": dict(
            hanja="適用", meaning="application (of a rule)",
            characters=[("適", "적", "suitable — as in 적절, 적합"),
                        ("用", "용", "to use — as in 사용, 활용")],
        ),
        "분쟁": dict(
            hanja="紛爭", meaning="a dispute",
            characters=[("紛", "분", "confused, tangled"),
                        ("爭", "쟁", "to contend — as in 경쟁, 전쟁")],
        ),
        "처벌": dict(
            hanja="處罰", meaning="punishment",
            characters=[("處", "처", "to deal with — as in 처리, 대처"),
                        ("罰", "벌", "penalty — as in 형벌, 벌금")],
        ),
        "대법원": dict(
            hanja="大法院", meaning="the Supreme Court",
            notes=["The top of the ordinary courts. Separate from the "
                   "헌법재판소, the Constitutional Court, which chapter 20 "
                   "names."],
        ),
        "고등법원": dict(hanja="高等法院", meaning="a high court"),
        "지방법원": dict(hanja="地方法院", meaning="a district court"),
        "가정법원": dict(hanja="家庭法院", meaning="a family court"),
        "주요": dict(hanja="主要", meaning="main, principal"),
        "설치": dict(
            hanja="設置", meaning="installation, establishment",
            characters=[("設", "설", "to establish — as in 시설, 건설"),
                        ("置", "치", "to place — as in 위치")],
        ),
        "해당": dict(
            hanja="該當", meaning="the relevant one, the one in question",
            characters=[("該", "해", "that, the said"),
                        ("當", "당", "to be the case — as in 담당, 당선")],
        ),
        "사건": dict(
            hanja="事件", meaning="a case, an incident",
            characters=[("事", "사", "affair — as in 사고, 인사"),
                        ("件", "건", "item, case — as in 조건, 물건")],
        ),
        "진행": dict(
            hanja="進行", meaning="to conduct, to proceed with",
            characters=[("進", "진", "to advance — as in 진출, 진학"),
                        ("行", "행", "to go, to do — as in 행정, 실행")],
        ),
        "친척": dict(
            hanja="親戚", meaning="relatives, kin",
            characters=[("親", "친", "close, parent — as in 친구, 부모님"),
                        ("戚", "척", "relative by marriage")],
        ),
        "소년": dict(
            hanja="少年", meaning="a juvenile, a boy",
            notes=["In law the word covers anyone under nineteen, of either "
                   "sex — 소년 재판 is a juvenile hearing."],
        ),
        "전문적": dict(
            hanja="專門的", meaning="specialised, professional",
            characters=[("專", "전", "exclusive — as in 전공, 전용"),
                        ("門", "문", "gate — as in 대문, 전문가")],
        ),
        "판결": dict(
            hanja="判決", meaning="a judgment, a verdict",
            characters=[("決", "결", "to decide — as in 결정, 해결")],
        ),
        "대법원장": dict(hanja="大法院長", meaning="the Chief Justice"),
        "대법관": dict(
            hanja="大法官", meaning="a Supreme Court justice",
            notes=["Thirteen besides the Chief Justice, fourteen in all."],
        ),
        "최종적": dict(
            hanja="最終的", meaning="final",
            characters=[("最", "최", "most — as in 최고, 최근"),
                        ("終", "종", "end — as in 종료, 최종")],
        ),
        "인정받다": dict(hanja="認定받다", meaning="to be recognised as"),
        "변경": dict(
            hanja="變更", meaning="alteration, change",
            characters=[("變", "변", "to change — as in 변화, 변호"),
                        ("更", "경", "again, to renew — as in 갱신")],
        ),
        "법원행정처": dict(
            hanja="法院行政處",
            meaning="the National Court Administration",
            notes=["The courts' own administrative arm, under the Supreme "
                   "Court."],
        ),
        "소송 구조": dict(
            hanja="訴訟救助", meaning="legal aid",
            characters=[("訴", "소", "to sue, to appeal — as in 소송, 고소"),
                        ("訟", "송", "to litigate"),
                        ("救", "구", "to rescue — as in 구조, 구제"),
                        ("助", "조", "to help — as in 도움's 조력, 보조")],
            notes=["Not 구조 “structure” (構造) — this 구조 is rescue. The court "
                   "waives or defers the fees for someone who cannot pay."],
        ),
        "번역": dict(
            hanja="翻譯", meaning="translation (written)",
            characters=[("翻", "번", "to turn over, to translate"),
                        ("譯", "역", "to translate — as in 통역")],
        ),
        "발간": dict(
            hanja="發刊", meaning="publication",
            characters=[("刊", "간", "to print, to publish — as in 주간지")],
        ),
        "과정": dict(hanja="過程", meaning="a process, a course"),
        "대상": dict(
            hanja="對象", meaning="a target, those covered",
            characters=[("對", "대", "against, towards — as in 대비, 반대"),
                        ("象", "상", "form — as in 상징, 현상")],
        ),
        "변호사": dict(
            hanja="辯護士", meaning="a lawyer",
            characters=[("辯", "변", "to plead — as in 답변, 변명"),
                        ("護", "호", "to protect — as in 보호, 간호"),
                        ("士", "사", "a qualified person — as in 기사, 박사")],
        ),
        "납부": dict(
            hanja="納付", meaning="payment (of a fee or tax)",
            characters=[("納", "납", "to pay in — as in 납세"),
                        ("付", "부", "to hand over — as in 배부, 첨부")],
        ),
        "연장": dict(
            hanja="延長", meaning="extension (of time)",
            characters=[("延", "연", "to prolong — as in 연기 “postponement”"),
                        ("長", "장", "long — as in 장기, 성장")],
        ),
        "내국인": dict(
            hanja="內國人", meaning="a national, a citizen of the country",
            notes=["Set against 외국인, and against 재외국민 abroad."],
        ),
        "국내": dict(hanja="國內", meaning="domestic, within the country"),
        "거주": dict(
            hanja="居住", meaning="residence",
            characters=[("居", "거", "to dwell — as in 거실"),
                        ("住", "주", "to live — as in 주택, 주민")],
        ),
        "활성화": dict(hanja="活性化", meaning="revitalisation, take-up"),
        "구제": dict(
            hanja="救濟", meaning="relief, redress",
            characters=[("救", "구", "to rescue — as in 구조, 구급"),
                        ("濟", "제", "to relieve, to cross — as in 경제")],
            notes=["권리 구제 is a remedy for a right that has been infringed."],
        ),
        "기대": dict(hanja="期待", meaning="expectation"),
        "밝히다": dict(meaning="to state, to make known; to light up"),
        "지방자치단체": dict(
            hanja="地方自治團體", meaning="a local authority",
            notes=["시, 군, 구 and their councils — chapter 24's subject."],
        ),
        "기업": dict(
            hanja="企業", meaning="a company, an enterprise",
            characters=[("企", "기", "to plan, to undertake — as in 기획"),
                        ("業", "업", "business — as in 직업, 사업")],
        ),
        "욕심": dict(
            hanja="慾心", meaning="greed",
            characters=[("慾", "욕", "desire — as in 욕망, 식욕"),
                        ("心", "심", "heart — as in 관심, 중심")],
        ),
        "끼치다": dict(
            meaning="to cause, to inflict (harm)",
            notes=["피해를 끼치다, 영향을 끼치다 — of something one does to "
                   "another."],
        ),
        "질서": dict(
            hanja="秩序", meaning="order",
            characters=[("秩", "질", "order, sequence"),
                        ("序", "서", "order, preface — as in 순서")],
        ),
        "유지": dict(
            hanja="維持", meaning="maintenance, keeping up",
            characters=[("維", "유", "to hold together, to tie"),
                        ("持", "지", "to hold — as in 지속, 지지")],
        ),
        "공정": dict(
            hanja="公正", meaning="fairness, impartiality",
            characters=[("公", "공", "public, impartial — as in 공익, 공개"),
                        ("正", "정", "correct — as in 정확, 부정")],
        ),
        "독립": dict(
            hanja="獨立", meaning="independence",
            characters=[("獨", "독", "alone — as in 단독, 독자"),
                        ("立", "립", "to stand — as in 입법, 설립")],
        ),
        "보장": dict(
            hanja="保障", meaning="guarantee",
            characters=[("保", "보", "to protect — as in 보호, 보험"),
                        ("障", "장", "barrier, to block — as in 장애")],
        ),
        "판사": dict(
            hanja="判事", meaning="a judge",
            notes=["법관 is the formal word for the office; 판사 is the person "
                   "who sits."],
        ),
        "법관": dict(hanja="法官", meaning="a judge (formal)"),
        "간섭": dict(
            hanja="干涉", meaning="interference",
            characters=[("干", "간", "to interfere, dry — as in 간여"),
                        ("涉", "섭", "to wade, to be involved — as in 교섭")],
        ),
        "오직": dict(meaning="only, solely"),
        "양심": dict(
            hanja="良心", meaning="conscience",
            characters=[("良", "량", "good — as in 양호하다, 개량"),
                        ("心", "심", "heart, mind — as in 중심, 욕심")],
        ),
        "거치다": dict(meaning="to go through, to pass by way of"),
        "삼심제": dict(
            hanja="三審制", meaning="the three-instance system",
            characters=[("審", "심", "to examine, to try — as in 심사, 심의"),
                        ("制", "제", "system — as in 제도, 단원제")],
            notes=["1심 district court, 2심 high court, 3심 Supreme Court — "
                   "three chances to be heard on the same case."],
        ),
        "재판부": dict(
            hanja="裁判部", meaning="the bench, the court hearing a case",
        ),
        "허가": dict(
            hanja="許可", meaning="permission, a licence",
            characters=[("許", "허", "to allow — as in 허락, 특허"),
                        ("可", "가", "possible — as in 가능, 불가능")],
        ),
        "장면": dict(
            hanja="場面", meaning="a scene",
            characters=[("場", "장", "place — as in 시장, 직장"),
                        ("面", "면", "face, side — as in 측면, 표면")],
        ),
        "촬영": dict(
            hanja="撮影", meaning="filming, photographing",
            characters=[("撮", "촬", "to take (a picture)"),
                        ("影", "영", "shadow, image — as in 그림자")],
        ),
        "중계방송": dict(
            hanja="中繼放送", meaning="a live broadcast, a relay",
            characters=[("繼", "계", "to succeed, to continue — as in 계속")],
        ),
        "민사 재판": dict(
            hanja="民事裁判", meaning="a civil trial",
            notes=["민사 소송 is the suit itself — the word your pencil note "
                   "adds."],
        ),
        "형사 재판": dict(
            hanja="刑事裁判", meaning="a criminal trial",
            characters=[("刑", "형", "punishment — as in 형벌, 사형")],
        ),
        "가사": dict(
            hanja="家事", meaning="family matters; housework",
            notes=["Same word as the 가사 “housework” of chapter 2, read here "
                   "in its legal sense."],
        ),
        "층간 소음": dict(
            hanja="層間騷音", meaning="noise between floors",
            characters=[("層", "층", "floor, layer — as in 계층, 고층"),
                        ("騷", "소", "noisy, disturbance"),
                        ("音", "음", "sound — as in 발음, 음악")],
            notes=["A standing grievance in Korean apartment life, and a "
                   "common civil claim."],
        ),
        "인해": dict(hanja="因해", meaning="owing to, because of"),
        "정도": dict(hanja="程度", meaning="extent, degree"),
        "훔치다": dict(meaning="to steal"),
        "죄": dict(
            hanja="罪", meaning="an offence, guilt",
            characters=[("罪", "죄", "sin, crime — as in 범죄, 무죄")],
        ),
        "죄를 묻다": dict(
            meaning="to hold someone to account for an offence",
            notes=["묻다 here is “to ask of, to call to account”, not “to "
                   "bury”."],
        ),
        "상속": dict(
            hanja="相續", meaning="inheritance",
            characters=[("相", "상", "mutual — as in 서로's 상호, 수상"),
                        ("續", "속", "to continue — as in 계속, 지속")],
        ),
        "양육": dict(
            hanja="養育", meaning="the raising of a child",
            characters=[("養", "양", "to nurture — as in 영양, 입양"),
                        ("育", "육", "to bring up — as in 교육, 보육")],
        ),
        "오염": dict(
            hanja="汚染", meaning="pollution",
            characters=[("汚", "오", "dirty, to stain"),
                        ("染", "염", "to stain, to dye — as in 전염병")],
        ),
        "우려": dict(
            hanja="憂慮", meaning="concern, apprehension",
            characters=[("憂", "우", "to worry, grief"),
                        ("慮", "려", "to consider — as in 배려, 고려")],
        ),
        "폐기물": dict(
            hanja="廢棄物", meaning="waste",
            characters=[("廢", "폐", "to discard — as in 폐지, 폐교"),
                        ("棄", "기", "to abandon — as in 포기 “giving up”")],
        ),
        "허락": dict(hanja="許諾", meaning="consent, permission"),
        "정당": dict(
            hanja="正當", meaning="being justified, proper",
            notes=["Not the 정당 “political party” (政黨) of chapter 21 — same "
                   "sound, different characters."],
        ),
        "재활용": dict(
            hanja="再活用", meaning="recycling",
            characters=[("再", "재", "again — as in 재적, 재판")],
        ),
        "원래대로": dict(hanja="元來대로", meaning="back to how it was"),
        "회복": dict(
            hanja="回復", meaning="recovery, restoration",
            characters=[("回", "회", "to turn, a time — as in 회의, 횟수"),
                        ("復", "복", "to return — as in 복구, 반복")],
        ),
        "불가능": dict(hanja="不可能", meaning="impossibility"),
        "예방": dict(
            hanja="豫防", meaning="prevention",
            characters=[("豫", "예", "beforehand — as in 예산, 예상"),
                        ("防", "방", "to defend — as in 방지, 국방")],
        ),
        "미치다": dict(
            meaning="to reach, to have an effect on; to go mad",
            notes=["영향을 미치다 “to have an influence on”."],
        ),
        "부정적": dict(hanja="否定的", meaning="negative"),
        "부적합": dict(hanja="不適合", meaning="unsuitability, non-conformity"),
        "통보": dict(
            hanja="通報", meaning="notification",
            characters=[("報", "보", "to report — as in 보고, 정보")],
        ),
        "위법": dict(
            hanja="違法", meaning="illegality, being against the law",
            characters=[("違", "위", "to violate — as in 위반")],
        ),
        "피의자": dict(
            hanja="被疑者", meaning="a suspect",
            characters=[("被", "피", "to suffer, passive — as in 피해"),
                        ("疑", "의", "to doubt — as in 의심, 의문")],
            notes=["피의자 while under investigation, 피고인 once charged and on "
                   "trial."],
        ),
        "영장주의": dict(
            hanja="令狀主義", meaning="the warrant requirement",
            characters=[("令", "령", "command — as in 명령, 대통령"),
                        ("狀", "장", "document, condition — as in 상태")],
        ),
        "구속": dict(
            hanja="拘束", meaning="detention, being held in custody",
            characters=[("拘", "구", "to seize, to restrain"),
                        ("束", "속", "to bind — as in 약속, 단속")],
        ),
        "압수": dict(
            hanja="押收", meaning="seizure, confiscation",
            characters=[("押", "압", "to press, to seize — as in 압력"),
                        ("收", "수", "to collect — as in 수입, 수령")],
        ),
        "수색": dict(
            hanja="搜索", meaning="a search",
            characters=[("搜", "수", "to search — as in 수사"),
                        ("索", "색", "to seek — as in 검색")],
        ),
        "발행": dict(hanja="發行", meaning="issuance (of a document)"),
        "영장": dict(hanja="令狀", meaning="a warrant"),
        "제시": dict(
            hanja="提示", meaning="presentation, showing",
            characters=[("提", "제", "to present — as in 제출, 제공"),
                        ("示", "시", "to show — as in 표시, 지시")],
        ),
        "미란다원칙": dict(
            meaning="the Miranda rule",
            notes=["From Miranda v. Arizona, 1966. Korean police must state "
                   "the right to counsel and to challenge the arrest at the "
                   "moment of arrest."],
        ),
        "변호인": dict(hanja="辯護人", meaning="defence counsel"),
        "선임": dict(
            hanja="選任", meaning="appointment, retaining (counsel)",
            characters=[("選", "선", "to choose — as in 선거, 선출"),
                        ("任", "임", "to entrust — as in 임명, 임기")],
        ),
        "변명": dict(
            hanja="辨明", meaning="an explanation in one's own defence",
        ),
        "심사": dict(
            hanja="審査", meaning="review, examination",
            characters=[("審", "심", "to examine — as in 삼심제, 심의"),
                        ("査", "사", "to investigate — as in 조사, 수사")],
            notes=["구속적부심사 is the review of whether detention is lawful — "
                   "what the caution offers."],
        ),
        "요청": dict(hanja="要請", meaning="a request"),
        "무죄추정의 원칙": dict(
            hanja="無罪推定의原則",
            meaning="the presumption of innocence",
        ),
        "유죄": dict(hanja="有罪", meaning="guilt, being guilty"),
        "무죄": dict(hanja="無罪", meaning="innocence, not guilty"),
        "추측": dict(
            hanja="推測", meaning="supposition, presuming",
            characters=[("推", "추", "to push, to infer — as in 추진"),
                        ("測", "측", "to measure — as in 측정")],
        ),
    },

    extraNotes=[
        "The three principles of 이야기 나누기 are printed as a two-column "
        "table with no header; they are set here as a list, each principle "
        "naming itself.",
        "The review gaps on p. 125 are blank in the book and left blank here.",
    ],
)
