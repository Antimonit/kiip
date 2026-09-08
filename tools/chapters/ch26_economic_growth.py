# -*- coding: utf-8 -*-
"""Chapter 26 — Economic growth.

Transcribed from the photos of pp. 140-143.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, LABELS,
               TABLE, CELL, CHART, GLOSSARY)

CHAPTER = dict(
    number=26, slug="26-economic-growth",
    unit="경제", title="경제 성장", titleEn="Economic growth",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 세계 여러 나라로 {수출}하는 한국의 주요 {품목}입니다."),
        LABELS("TV 디스플레이", "스마트폰", "자동차", "김"),
        HEADING(4, "01 한국에서 {생산}한 물건 중 어떤 것을 사용해 봤습니까?"),
        HEADING(4, "02 사용해 본 한국 {제품}이나 {식품}의 특징(장·단점)은 무엇입니까?"),

        SECTION("goals", "학습목표"),
        BULLET("한국의 경제 성장 과정을 설명할 수 있다.", ordered=True),
        BULLET("한국과 다른 나라와의 {경제 교류}에 대해 설명할 수 있다.", ordered=True),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"],
              [["심화", "경제", "16. 국민경제와 국제거래", "한국의 경제 지표, 경제 교류"]]),

        SECTION("part", "01 한국 경제는 어떻게 성장해 왔을까?"),
        HEADING(2, "‘한강의 기적’을 이루다"),
        GLOSSARY(("폐허", "무너지고 부서져 못 쓰게 됨", "폐허"),
                 ("복구", "원래 상태로 돌아감", "복구"),
                 ("수출", "외국에 물건을 파는 것", "수출"),
                 ("신소재", "미래의 기술을 이끌어갈 새로운 재료", "신소재"),
                 ("외환 위기", "1997년 한국 정부가 가진 외환(외국 돈)이 부족해지면서 겪은 경제 "
                               "위기", "외환 위기"),
                 ("금융 위기", "2008년 미국에서 시작되어 한국을 비롯한 전 세계로 확산된 대규모의 "
                               "경제 위기", "금융 위기")),
        PARAGRAPH("한국은 1950년대에 6·25 전쟁을 겪으면서 {산업} {시설}이 대부분 "
                  "{파괴}되었고, {국토} 전체가 {폐허}가 되었다. 이후 한국은 전쟁으로 인한 피해를 "
                  "{복구}하고 잘 사는 나라를 만들기 위해 {힘썼다|힘쓰다}."),
        PARAGRAPH("한국은 경제 성장을 위해 특히 {수출}에 많은 노력을 {기울였다|기울이다}. "
                  "1950~60년대에는 옷, 신발, 가방, {가발} 등을 주로 수출하였고, 1970년대 기계, "
                  "배, {철강} 등에 이어 1980년대부터는 자동차, 전기, {전자 제품} 등의 수출이 "
                  "크게 늘었다. 1990~2010년대를 지나면서 {반도체}, 휴대폰, {신소재} 등으로 수출 "
                  "{품목}을 늘렸고, 더 {나아가|나아가다} 드라마나 노래와 같은 문화 {콘텐츠}, "
                  "{의료} 서비스 등의 분야에서도 수출을 많이 하고 있다."),
        PARAGRAPH("1997년 한국의 {외환 위기}, 2008년 세계적인 {금융 위기}로 한때 어려움을 겪기도 "
                  "했지만 결국 이를 {극복}하였다. 과거에 매우 가난했던 한국이 지금처럼 {눈부신} "
                  "성장을 한 것을 가리켜 사람들은 ‘{한강의 기적}’이라고 부른다. 1953년 "
                  "67달러였던 한국의 1인당 {국민 소득}은 2019년 31,400달러를 "
                  "{넘어섰다|넘어서다}."),

        HEADING(2, "경제 성장에서 사람이 중요한 역할을 하다"),
        GLOSSARY(("교육열", "교육에 대한 열정", "교육열")),
        PARAGRAPH("한국이 빠르게 경제 성장을 할 수 있었던 {요인}은 무엇일까? 그중 몇 가지를 "
                  "{제시}하면 다음과 같다. 첫째, {풍부}한 {노동력}이다. 한국은 {영토}가 좁고 "
                  "{자원}이나 기술, 돈이 많지 않았지만 인구는 많은 편이었다. 이를 경제 성장에 "
                  "{적극} 활용하였다. 둘째, 뜨거운 {교육열}이다. 단지 일할 사람이 많았다는 "
                  "사실보다는 그들이 적절하고 필요한 교육을 받아 {우수}한 노동력이 되었다는 점이 "
                  "중요하다. 셋째, 경제적 위기를 극복하겠다는 {의지}이다. 한국은 {지속적}인 경제 "
                  "성장을 위해 우수한 {인재}를 {확보}하고 {첨단} 기술을 {개발}하기 위한 노력을 "
                  "계속하고 있다."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "독일로 간 광부와 간호사"),
        PARAGRAPH("1963년 한국인 {광부} 247명이 처음 독일에 도착한 것을 시작으로 1977년까지 "
                  "8,395명의 광부가 독일의 {광산}(석탄을 캐는 곳)에서 일했다. 1965년부터는 "
                  "한국인 {간호사}의 독일 취업이 {허용}되어 1976년까지 모두 10,371명이 독일로 "
                  "떠났다."),
        PARAGRAPH("광부들은 지하 1,000m의 {탄광}(석탄이 묻혀 있는 광산)에서 힘든 노동을 "
                  "{견뎌야|견디다} 했으며, 간호사들도 처음에는 병원의 어려운 일을 "
                  "{도맡았다|도맡다}. 이들의 월급은 한국으로 보내져 가족의 {생계비}와 {학비}로 "
                  "쓰였고 국가의 경제 성장에도 큰 도움이 되었다."),
        SOURCE("[출처: 김육훈(2011). 살아있는 한국 근현대사 교과서.]"),
        FIGURE("독일로 떠나는 광부들"),
        FIGURE("독일 병원의 한국인 간호사들"),

        SECTION("part", "02 한국은 세계 여러 나라와 어떻게 교류하고 있을까?"),
        HEADING(2, "무역 강국이 된 한국"),
        GLOSSARY(("수입", "외국에서 물건을 사오는 것", "수입"),
                 ("첨단 제품", "높은 수준의 과학 기술로 만든 제품", "첨단 제품"),
                 ("자유무역협정(FTA)", "국가 간 상품이나 서비스의 자유로운 수출과 수입을 위한 "
                                       "약속", "자유무역협정"),
                 ("관세", "수출되거나 수입되는 물건에 매겨지는 세금", "관세")),
        PARAGRAPH("한국의 수출과 {수입}을 {합친|합치다} {무역} {규모}는 지난 2011년 세계 9번째로 "
                  "1조 달러를 넘어선 이후로 {꾸준히} {상위권}을 유지하고 있다. 2019년에도 "
                  "{수출액} 5,424억 달러, {수입액} 5,302억 달러를 {기록}하였다."),
        PARAGRAPH("한국은 {무역 강국}의 {지위}를 유지하기 위해 {첨단 제품}의 수출을 계속 "
                  "{확대}하고 있다. 또한, 한국 제품을 수출할 해외 {시장}을 {확보}하고 경제의 "
                  "{경쟁력}을 {강화}하기 위해 여러 나라와의 {자유무역협정}(FTA)을 {추진}해 왔다. "
                  "2004년 칠레와의 자유무역협정을 시작으로 중국, 베트남, 미국, 유럽연합 등 50개 "
                  "이상의 국가와 자유무역협정을 맺고 있다. 자유무역협정은 수출이나 수입을 할 때 "
                  "내는 {관세}를 줄이거나 없앨 수 있어서 무역을 활발하게 하는 데 크게 "
                  "{기여}할 수 있다."),
        TABLE(["수출상품", "수입상품"],
              [["반도체", "원유"],
               ["자동차", "천연가스"],
               ["석유제품", "석유제품"],
               ["선박", "석탄"],
               ["평판디스플레이 및 센서", "컴퓨터"]]),
        FIGURE("한국 주요 수출입품 (2019)"),

        HEADING(2, "한강의 기적, 이제는 나눔으로"),
        GLOSSARY(("경제협력기구(OECD)", "세계 경제의 발전과 인류의 복지 증진을 위한 경제 기구",
                  "경제협력개발기구"),
                 ("저개발 국가", "경제 성장이 정도가 낮은 나라", "저개발 국가"),
                 ("원조", "물건이나 돈 등으로 도와줌", "원조")),
        PARAGRAPH("6·25 전쟁이 끝날 무렵 세계에서 가장 가난한 나라 중 하나였던 한국은 국제 "
                  "사회의 {지원}과 스스로의 노력을 통해 경제 성장의 {기틀}을 마련하였다. 그러한 "
                  "{기반} 위에서 꾸준히 성장을 {거듭해|거듭하다} 온 결과, 이제 {경제 강국}이 된 "
                  "한국은 다른 나라의 경제 성장을 도와주는 역할에 참여하고 있다."),
        PARAGRAPH("한국은 2009년에 {경제협력개발기구}(OECD)의 {개발원조회의}(DAC)에 {가입}한 후 "
                  "{저개발 국가}의 경제 성장을 지원하고 있다. 또한, {한국국제협력단}(KOICA)과 "
                  "{대외경제협력기금}(EDCF)을 중심으로 경제 상황이 어려운 나라의 {보건}, 교육, "
                  "{위생}, 교통 환경을 {개선}하고, 물이나 에너지 {부족} 등과 관련된 문제가 "
                  "{해소}될 수 있도록 돕고 있다. 이러한 노력에 대해 해외에서는 한국이 과거에 "
                  "{원조}를 받다가 이제는 원조를 하게 된 {최초}의 나라라고 평가한다."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "전세계 코로나19 극복을 위한 한국의 지원"),
        PARAGRAPH("코로나19가 전세계로 {확산}되고 있을 때, 한국은 {신속}한 {진단검사}부터 "
                  "{치료}까지의 과정이 큰 {주목}을 받았다. 특히 이를 {K-방역}이란 이름으로 "
                  "시스템을 {구축}하고 경험을 공유하여 다른 나라에서도 코로나19 위기를 "
                  "극복하는데 큰 도움을 주었다. 또한 약 110개국(2020.6.3.기준/외교부)에서 "
                  "코로나19 관련 {인도적} 지원을 {요청}해 왔다. 이에 한국은 피해 상황이 "
                  "{심각}하고, 보건 {체계}가 어려운 나라 중심으로 생산된 {진단키트}와 마스크 등 "
                  "{방역물품}을 지원하기도 하였다."),
        FIGURE("에티오피아에 방역물품을 기증하는 모습"),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 한국 경제는 어떻게 성장해 왔을까?"),
        BULLET("한국은 6·25 전쟁 이후 경제 성장을 위해 특히 (        )에 많은 노력을 기울였다."),
        BULLET("한국이 가난을 극복하고 빠르게 경제 성장을 한 것을 가리켜 (            )이라고 "
               "부른다."),
        BULLET("한국이 빠르게 경제 성장을 할 수 있었던 요인으로는 풍부한 (        ), 뜨거운 "
               "(        ), 경제적 위기를 극복하겠다는 의지 등을 꼽을 수 있다."),
        HEADING(3, "02 한국은 세계 여러 나라와 어떻게 교류하고 있을까?"),
        BULLET("한국은 제품을 수출할 해외 시장을 확보하고 경제의 경쟁력을 강화하기 위해 여러 "
               "나라와 (            )을 적극 추진해 왔다."),
        BULLET("한국은 과거에 국제사회의 (      )를 받았다가 이제는 (      )를 하게 된 최초의 "
               "나라라는 평가를 받는다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "한국의 세계 수출시장 점유율 1위 제품에는 무엇이 있을까?", translation=
          "Which Korean products lead the world export market?" "\n\n"
          "As of 2018 Korea held first place in the world export market in "
          "63 product lines in all, which puts it thirteenth in the world. "
          "Among those first-place lines, chemical products (27), steel (12) "
          "and textile products (5) made up 69.8%. Representative products "
          "include memory semiconductors, ships, washing machines, "
          "motorcycle helmets, nail clippers, medicine capsules, ski gloves, "
          "tents, fishing rods, colour monitors, microwave ovens and butane "
          "gas." "\n\n"
          "Korean-grown laver in particular holds first place in the world, "
          "and ‘소전’, the raw material of coins, also holds 50% of the world "
          "market."),
        PARAGRAPH("한국의 세계 수출시장 {점유율} 1위 품목은 2018년 기준, 총 63개로 세계 13위를 "
                  "{차지}하고 있다. 1위 품목 중 {화학제품}(27개), 철강(12개), {섬유제품}(5개)이 "
                  "69.8%의 비중을 보였다. 대표적인 제품으로는 {메모리 반도체}, {선박}, 세탁기, "
                  "오토바이 헬멧, 손톱깎이, {의약} 캡슐, 스키 장갑, 텐트, 낚싯대, 컬러 모니터, "
                  "전자레인지, 부탄가스 등이 있다."),
        PARAGRAPH("특히, 한국산 김은 세계 점유율 1위를 차지하고 있으며, 동전의 {원자재}인 "
                  "‘{소전}’도 세계의 50%를 점유하고 있다."),
        CHART("우리나라 세계수출 1위 품목 수 (2018년 HS 6단위 기준) — 괄호 안은 세계 순위", "개",
              [["2015년 (14위)", 68],
               ["2016년 (12위)", 71],
               ["2017년 (12위)", 75],
               ["2018년 (13위)", 63]]),
        CHART("우리나라 세계수출 1위 주요 품목 (2018년)", "개",
              [["화학제품", 27],
               ["철강", 12],
               ["섬유제품", 5],
               ["가죽·고무·신발·여행용품", 4]]),
        SOURCE("[출처] 한국무역협회, 국제무역통상연구원(2020)"),
        PARAGRAPH("★ 자신의 고향 나라에서 한국으로 수출하거나 수입하는 제품에 대해 이야기해 "
                  "봅시다.",
          "Talk about the products your home country exports to Korea or "
          "imports from it."),
    ],

    english={
        "‘한강의 기적’을 이루다": dict(
            title="The miracle on the Han",
            paragraphs=[
                "Korea went through the Korean War in the 1950s, and most of "
                "its industrial plant was destroyed; the whole country was "
                "left in ruins. It then set about repairing the damage the war "
                "had done and making itself a country that lived well.",

                "Exports above all were where Korea put its effort for the "
                "sake of growth. In the 1950s and 60s it exported chiefly "
                "clothes, shoes, bags and wigs; machinery, ships and steel "
                "followed in the 1970s; and from the 1980s exports of cars, "
                "electrical goods and electronics rose sharply. Through the "
                "1990s and 2000s it added semiconductors, mobile telephones "
                "and new materials to the list, and further still it now "
                "exports a great deal in fields such as cultural content — "
                "drama and music — and medical services.",

                "Korea's foreign-exchange crisis of 1997 and the world "
                "financial crisis of 2008 brought hard times for a while, but "
                "it came through them in the end. People call the dazzling "
                "growth of a country once so poor the miracle on the Han. "
                "Korea's income per head, 67 dollars in 1953, passed 31,400 "
                "dollars in 2019.",
            ],
        ),
        "경제 성장에서 사람이 중요한 역할을 하다": dict(
            title="People played the important part in that growth",
            paragraphs=[
                "What lay behind Korea's rapid growth? A few of the causes "
                "are these. First, an abundant workforce. Korea's territory "
                "was small and it had little in the way of resources, "
                "technology or money, but it did have people. Those it put "
                "to work for growth. Second, a burning appetite for "
                "education. What matters is not simply that there were many "
                "hands to work, but that those hands received the right "
                "education and became a skilled workforce. Third, the will to "
                "come through economic crisis. Korea keeps working to secure "
                "able people and to develop advanced technology, for the sake "
                "of growth that lasts.",
            ],
        ),
        "무역 강국이 된 한국": dict(
            title="Korea as a trading power",
            paragraphs=[
                "Korea's trade — exports and imports together — passed a "
                "trillion dollars in 2011, ninth in the world, and has stayed "
                "near the top ever since. 2019 saw exports of 542.4 billion "
                "dollars and imports of 530.2 billion.",

                "To hold its standing as a trading power Korea keeps widening "
                "its exports of advanced products. It has also pursued free "
                "trade agreements with many countries, to secure the overseas "
                "markets its products need and to strengthen the economy's "
                "competitiveness. Beginning with Chile in 2004, it now holds "
                "agreements with more than fifty countries, China, Vietnam, "
                "the United States and the European Union among them. A free "
                "trade agreement can lower or remove the duty paid on exports "
                "and imports, and so does a great deal to make trade brisk.",
            ],
        ),
        "한강의 기적, 이제는 나눔으로": dict(
            title="The miracle on the Han, now shared out",
            paragraphs=[
                "Korea, one of the poorest countries in the world as the "
                "Korean War ended, laid the groundwork for growth through the "
                "support of the international community and its own effort. "
                "Having grown steadily on that foundation, it is now an "
                "economic power itself, and takes a part in helping other "
                "countries grow.",

                "Korea joined the OECD's Development Assistance Committee in "
                "2009 and supports the growth of less developed countries. "
                "Through KOICA and the Economic Development Cooperation Fund "
                "it helps improve health, education, sanitation and transport "
                "in countries in economic difficulty, and helps resolve "
                "problems such as shortages of water and energy. For that "
                "work Korea is reckoned abroad to be the first country ever to "
                "have gone from receiving aid to giving it.",
            ],
        ),
    },

    extraAnnotations={
        "수출": dict(
            hanja="輸出", meaning="export",
            characters=[("輸", "수", "to transport — as in 수송, 운수"),
                        ("出", "출", "to go out — as in 출국, 제출")],
        ),
        "수입": dict(
            hanja="輸入", meaning="import",
            notes=["Not the 수입 “income” (收入) — same sound, different "
                   "characters. Here it is goods coming in."],
        ),
        "품목": dict(
            hanja="品目", meaning="an item, a line of goods",
            characters=[("品", "품", "article — as in 상품, 제품"),
                        ("目", "목", "eye, item — as in 목표, 항목")],
        ),
        "생산": dict(
            hanja="生産", meaning="production",
            characters=[("生", "생", "to live, to bear — as in 생활, 학생"),
                        ("産", "산", "to produce — as in 농산물, 부동산")],
        ),
        "제품": dict(hanja="製品", meaning="a manufactured product"),
        "식품": dict(hanja="食品", meaning="foodstuffs, food products"),
        "경제 교류": dict(
            hanja="經濟交流", meaning="economic exchange",
            characters=[("交", "교", "to exchange — as in 외교, 교통"),
                        ("流", "류", "to flow — as in 유행, 물류")],
        ),
        "산업": dict(
            hanja="産業", meaning="industry",
            characters=[("業", "업", "trade, business — as in 직업, 농업")],
        ),
        "시설": dict(hanja="施設", meaning="a facility, plant"),
        "파괴": dict(
            hanja="破壞", meaning="destruction",
            characters=[("破", "파", "to break — as in 파산 “bankruptcy”"),
                        ("壞", "괴", "to collapse — as in 붕괴")],
        ),
        "국토": dict(
            hanja="國土", meaning="a country's territory",
            characters=[("土", "토", "earth, land — as in 토지, 영토")],
        ),
        "폐허": dict(
            hanja="廢墟", meaning="ruins",
            characters=[("廢", "폐", "to discard — as in 폐지, 폐기물"),
                        ("墟", "허", "ruins, a deserted place")],
        ),
        "복구": dict(
            hanja="復舊", meaning="restoration, repair",
            characters=[("復", "복", "to return — as in 회복, 반복"),
                        ("舊", "구", "old — as in 구식 “old-fashioned”")],
        ),
        "힘쓰다": dict(meaning="to strive, to put effort into"),
        "기울이다": dict(
            meaning="to tilt; to devote (effort)",
            notes=["노력을 기울이다 “to put effort in” — the set phrase."],
        ),
        "가발": dict(
            hanja="假髮", meaning="a wig",
            characters=[("假", "가", "false, temporary — as in 가정"),
                        ("髮", "발", "hair — as in 이발소 “barber's”")],
            notes=["One of Korea's chief exports in the 1960s, made from "
                   "Korean women's own hair."],
        ),
        "철강": dict(
            hanja="鐵鋼", meaning="steel",
            characters=[("鐵", "철", "iron — as in 지하철, 철도"),
                        ("鋼", "강", "steel")],
        ),
        "전자 제품": dict(hanja="電子製品", meaning="electronics"),
        "반도체": dict(
            hanja="半導體", meaning="a semiconductor",
            characters=[("半", "반", "half — as in 과반수, 절반"),
                        ("導", "도", "to lead, to conduct — as in 지도자"),
                        ("體", "체", "body — as in 단체, 체계")],
            notes=["Korea's largest export by value, by a wide margin."],
        ),
        "신소재": dict(
            hanja="新素材", meaning="a new material",
            characters=[("素", "소", "element, plain — as in 요소"),
                        ("材", "재", "material — as in 재료, 인재")],
        ),
        "나아가다": dict(
            meaning="to advance; and further",
            notes=["더 나아가 “going further still” as a connective."],
        ),
        "콘텐츠": dict(meaning="content (media)"),
        "의료": dict(hanja="醫療", meaning="medical care"),
        "외환 위기": dict(
            hanja="外換危機", meaning="a foreign-exchange crisis",
            characters=[("換", "환", "to exchange — as in 교환, 전환"),
                        ("危", "위", "danger — as in 위험, 위기"),
                        ("機", "기", "occasion, machine — as in 기관, 기회")],
            notes=["The IMF crisis of 1997, which Koreans call IMF 사태 as "
                   "often as 외환 위기."],
        ),
        "금융 위기": dict(
            hanja="金融危機", meaning="a financial crisis",
            characters=[("融", "융", "to melt, to circulate")],
            notes=["금융 is finance — chapter 28 is 금융기관 이용하기."],
        ),
        "극복": dict(
            hanja="克服", meaning="overcoming",
            characters=[("克", "극", "to conquer — as in 극기"),
                        ("服", "복", "clothes, to submit — as in 의복")],
        ),
        "눈부신": dict(
            headword="눈부시다", meaning="dazzling, brilliant",
            notes=["Literally “eye-blinding”. The book writes it closed."],
        ),
        "한강의 기적": dict(
            hanja="漢江의奇蹟", meaning="the miracle on the Han",
            characters=[("奇", "기", "strange, rare — as in 기이하다"),
                        ("蹟", "적", "trace, vestige")],
            notes=["After the Wirtschaftswunder's “miracle on the Rhine”. The "
                   "Han is the river through Seoul."],
        ),
        "국민 소득": dict(
            hanja="國民所得", meaning="national income",
            notes=["1인당 국민 소득 is income per head — the figure the page "
                   "quotes."],
        ),
        "넘어서다": dict(meaning="to pass, to exceed"),
        "요인": dict(
            hanja="要因", meaning="a factor, a cause",
            characters=[("要", "요", "necessary — as in 중요, 요소"),
                        ("因", "인", "cause — as in 원인, 인해")],
        ),
        "제시": dict(hanja="提示", meaning="to put forward, to present"),
        "풍부": dict(
            hanja="豊富", meaning="abundance",
            characters=[("豊", "풍", "plentiful — as in 풍년 “a good harvest”"),
                        ("富", "부", "rich — as in 부자, 부유하다")],
        ),
        "노동력": dict(
            hanja="勞動力", meaning="labour, a workforce",
            characters=[("勞", "로", "toil — as in 노동, 근로자"),
                        ("力", "력", "force — as in 능력, 압력")],
        ),
        "영토": dict(
            hanja="領土", meaning="territory",
            characters=[("領", "령", "to rule, to receive — as in 대통령")],
        ),
        "자원": dict(
            hanja="資源", meaning="resources",
            characters=[("資", "자", "capital, funds — as in 자본, 투자"),
                        ("源", "원", "source — as in 원인, 기원")],
        ),
        "적극": dict(
            hanja="積極", meaning="actively, positively",
            characters=[("積", "적", "to pile up — as in 면적, 축적"),
                        ("極", "극", "extreme, pole — as in 극복's 克 is separate")],
        ),
        "교육열": dict(
            hanja="敎育熱", meaning="zeal for education",
            characters=[("熱", "열", "heat, fever — as in 열정, 열심")],
        ),
        "우수": dict(
            hanja="優秀", meaning="being excellent",
            characters=[("優", "우", "superior, gentle — as in 우선, 배우"),
                        ("秀", "수", "outstanding")],
        ),
        "의지": dict(
            hanja="意志", meaning="will, resolve",
            characters=[("意", "의", "intention — as in 의견, 합의"),
                        ("志", "지", "aspiration — as in 지원자's 志")],
        ),
        "지속적": dict(hanja="持續的", meaning="sustained, continuing"),
        "인재": dict(
            hanja="人材", meaning="talented people",
            notes=["Literally “human material” — able people as a resource."],
        ),
        "확보": dict(
            hanja="確保", meaning="securing, obtaining",
            characters=[("確", "확", "certain — as in 확인, 확정"),
                        ("保", "보", "to keep — as in 보호, 보장")],
        ),
        "첨단": dict(hanja="尖端", meaning="the leading edge, high technology"),
        "개발": dict(
            hanja="開發", meaning="development",
            characters=[("開", "개", "to open — as in 개최, 공개"),
                        ("發", "발", "to issue — as in 발전, 발표")],
        ),
        "광부": dict(
            hanja="鑛夫", meaning="a miner",
            characters=[("鑛", "광", "ore, mine — as in 광산, 광물"),
                        ("夫", "부", "man, husband — as in 부부, 농부")],
        ),
        "광산": dict(hanja="鑛山", meaning="a mine"),
        "간호사": dict(
            hanja="看護師", meaning="a nurse",
            characters=[("看", "간", "to look after — as in 간병"),
                        ("護", "호", "to protect — as in 보호, 변호사")],
        ),
        "허용": dict(
            hanja="許容", meaning="permission, being allowed",
            characters=[("許", "허", "to allow — as in 허가, 허락"),
                        ("容", "용", "to allow, to contain — as in 포용")],
        ),
        "탄광": dict(
            hanja="炭鑛", meaning="a coal mine",
            characters=[("炭", "탄", "coal, charcoal — as in 석탄, 연탄")],
        ),
        "견디다": dict(meaning="to endure, to bear"),
        "도맡다": dict(meaning="to take on entirely, to be left with"),
        "생계비": dict(
            hanja="生計費", meaning="living costs",
            characters=[("計", "계", "to reckon — as in 계획, 통계"),
                        ("費", "비", "expense — as in 비용, 학비")],
        ),
        "학비": dict(hanja="學費", meaning="school fees"),
        "합치다": dict(meaning="to combine, to add together"),
        "무역": dict(
            hanja="貿易", meaning="trade",
            characters=[("貿", "무", "to trade"),
                        ("易", "역", "to exchange; easy — as in 교역")],
        ),
        "규모": dict(hanja="規模", meaning="scale, size"),
        "꾸준히": dict(meaning="steadily, without let-up"),
        "상위권": dict(
            hanja="上位圈", meaning="the upper ranks",
            characters=[("位", "위", "rank, place — as in 순위, 지위"),
                        ("圈", "권", "sphere, zone — as in 수도권, 역세권")],
        ),
        "수출액": dict(
            hanja="輸出額", meaning="the value of exports",
            characters=[("額", "액", "amount, forehead — as in 금액, 총액")],
        ),
        "수입액": dict(hanja="輸入額", meaning="the value of imports"),
        "기록": dict(
            hanja="記錄", meaning="a record, to record",
            characters=[("記", "기", "to write down — as in 일기, 기사"),
                        ("錄", "록", "to record — as in 등록, 목록")],
        ),
        "무역 강국": dict(
            hanja="貿易强國", meaning="a trading power",
            characters=[("强", "강", "strong — as in 강화, 강조")],
        ),
        "지위": dict(hanja="地位", meaning="standing, status"),
        "첨단 제품": dict(hanja="尖端製品", meaning="an advanced product"),
        "확대": dict(hanja="擴大", meaning="expansion, widening"),
        "시장": dict(
            hanja="市場", meaning="a market",
            notes=["Not the 시장 “mayor” (市長) of chapter 24 — same sound."],
        ),
        "경쟁력": dict(
            hanja="競爭力", meaning="competitiveness",
            characters=[("競", "경", "to compete — as in 경쟁, 경기"),
                        ("爭", "쟁", "to contend — as in 분쟁, 전쟁")],
        ),
        "강화": dict(
            hanja="强化", meaning="strengthening",
            characters=[("化", "화", "to become — as in 활성화, 도시화")],
        ),
        "자유무역협정": dict(
            hanja="自由貿易協定", meaning="a free trade agreement",
            notes=["FTA. The book's margin abbreviates it that way. Korea's "
                   "first was with Chile in 2004."],
        ),
        "추진": dict(
            hanja="推進", meaning="pursuing, driving forward",
            characters=[("推", "추", "to push — as in 추측, 추천"),
                        ("進", "진", "to advance — as in 진행, 증진")],
        ),
        "관세": dict(
            hanja="關稅", meaning="customs duty, a tariff",
            characters=[("關", "관", "gate, to relate — as in 관계, 관문"),
                        ("稅", "세", "tax — as in 세금, 면세")],
        ),
        "기여": dict(
            hanja="寄與", meaning="contribution",
            characters=[("寄", "기", "to entrust, to send — as in 기증, 기부"),
                        ("與", "여", "to give — as in 참여, 관여")],
        ),
        "지원": dict(hanja="支援", meaning="support, assistance"),
        "기틀": dict(meaning="the groundwork, the makings of something"),
        "기반": dict(hanja="基盤", meaning="a foundation"),
        "거듭하다": dict(meaning="to repeat, to do over and over"),
        "경제 강국": dict(hanja="經濟强國", meaning="an economic power"),
        "경제협력개발기구": dict(
            hanja="經濟協力開發機構", meaning="the OECD",
            notes=["Korea joined in 1996. The book's margin heads the entry "
                   "경제협력기구, one word short of the name."],
        ),
        "개발원조회의": dict(
            hanja="開發援助會議",
            meaning="the Development Assistance Committee (DAC)",
            characters=[("援", "원", "to aid — as in 지원, 응원"),
                        ("助", "조", "to help — as in 원조, 보조")],
        ),
        "가입": dict(
            hanja="加入", meaning="joining, enrolment",
            characters=[("加", "가", "to add — as in 참가, 증가"),
                        ("入", "입", "to enter — as in 입국, 입력")],
        ),
        "저개발 국가": dict(
            hanja="低開發國家", meaning="a less developed country",
            characters=[("低", "저", "low — as in 저렴, 저출산")],
        ),
        "한국국제협력단": dict(
            hanja="韓國國際協力團", meaning="KOICA",
            notes=["The agency that runs Korea's grant aid and its overseas "
                   "volunteers."],
        ),
        "대외경제협력기금": dict(
            hanja="對外經濟協力基金", meaning="the EDCF",
            notes=["Korea's concessional loan fund for developing countries."],
        ),
        "보건": dict(
            hanja="保健", meaning="public health",
            characters=[("健", "건", "healthy — as in 건강, 건전")],
        ),
        "위생": dict(
            hanja="衛生", meaning="hygiene, sanitation",
            characters=[("衛", "위", "to guard — as in 위성 “satellite”")],
        ),
        "개선": dict(
            hanja="改善", meaning="improvement",
            characters=[("改", "개", "to reform — as in 개정, 개혁"),
                        ("善", "선", "good — as in 선행, 최선")],
        ),
        "부족": dict(hanja="不足", meaning="shortage, being insufficient"),
        "해소": dict(
            hanja="解消", meaning="resolution, clearing up",
            characters=[("解", "해", "to loosen — as in 해결, 이해"),
                        ("消", "소", "to extinguish — as in 소비, 소화")],
        ),
        "원조": dict(
            hanja="援助", meaning="aid",
            notes=["Korea went from taking aid to giving it — the point the "
                   "article closes on."],
        ),
        "최초": dict(
            hanja="最初", meaning="the first, the earliest",
            characters=[("最", "최", "most — as in 최고, 최종"),
                        ("初", "초", "beginning — as in 초등학교, 초대")],
        ),
        "확산": dict(
            hanja="擴散", meaning="spread, diffusion",
            characters=[("擴", "확", "to expand — as in 확대, 확충"),
                        ("散", "산", "to scatter — as in 분산, 해산")],
        ),
        "신속": dict(
            hanja="迅速", meaning="promptness, speed",
            characters=[("迅", "신", "swift"),
                        ("速", "속", "fast — as in 속도, 고속")],
        ),
        "진단검사": dict(
            hanja="診斷檢査", meaning="diagnostic testing",
            characters=[("診", "진", "to diagnose — as in 진료, 진찰"),
                        ("斷", "단", "to cut, to decide — as in 판단")],
        ),
        "치료": dict(
            hanja="治療", meaning="treatment",
            characters=[("治", "치", "to cure, to govern — as in 정치, 치안"),
                        ("療", "료", "to heal — as in 의료, 진료")],
        ),
        "주목": dict(
            hanja="注目", meaning="attention, notice",
            characters=[("注", "주", "to pour, to focus — as in 주의, 주사"),
                        ("目", "목", "eye — as in 목표, 품목")],
        ),
        "K-방역": dict(
            meaning="K-quarantine, Korea's COVID-19 response",
            notes=["The government's own name for the test-trace-treat system "
                   "of 2020, marketed abroad on the K- pattern of K-pop."],
        ),
        "구축": dict(
            hanja="構築", meaning="building, putting in place (a system)",
            characters=[("構", "구", "to construct — as in 구성, 구조"),
                        ("築", "축", "to build — as in 건축")],
        ),
        "인도적": dict(
            hanja="人道的", meaning="humanitarian",
            characters=[("道", "도", "way — as in 도덕성, 도로")],
        ),
        "요청": dict(hanja="要請", meaning="a request"),
        "심각": dict(
            hanja="深刻", meaning="being serious, grave",
            characters=[("深", "심", "deep — as in 심화, 심야"),
                        ("刻", "각", "to carve — as in 조각, 시각")],
        ),
        "체계": dict(
            hanja="體系", meaning="a system",
            characters=[("系", "계", "lineage, system — as in 계열")],
        ),
        "진단키트": dict(meaning="a test kit"),
        "방역물품": dict(
            hanja="防疫物品", meaning="disease-control supplies",
        ),
        "점유율": dict(
            hanja="占有率", meaning="market share",
            characters=[("占", "점", "to occupy — as in 점령"),
                        ("有", "유", "to have — as in 소유, 공유"),
                        ("率", "률", "rate — as in 비율, 득표율")],
        ),
        "차지": dict(meaning="taking up, occupying (a place or rank)"),
        "화학제품": dict(
            hanja="化學製品", meaning="chemical products",
            characters=[("學", "학", "study — as in 학교, 학력")],
        ),
        "섬유제품": dict(
            hanja="纖維製品", meaning="textiles",
            characters=[("纖", "섬", "fine, slender"),
                        ("維", "유", "to tie — as in 유지")],
        ),
        "메모리 반도체": dict(
            meaning="memory semiconductors",
            notes=["DRAM and NAND flash — the part of the chip market Korea "
                   "leads."],
        ),
        "선박": dict(
            hanja="船舶", meaning="ships, vessels",
            characters=[("船", "선", "ship — as in 여객선, 조선업"),
                        ("舶", "박", "a large ship")],
        ),
        "의약": dict(hanja="醫藥", meaning="medicine, pharmaceuticals"),
        "원자재": dict(
            hanja="原資材", meaning="raw material",
            characters=[("原", "원", "origin — as in 원래, 원인"),
                        ("資", "자", "material, funds — as in 자원, 자본")],
        ),
        "소전": dict(
            hanja="素錢", meaning="a coin blank",
            notes=["The plain metal disc a coin is struck from. Korea's mint "
                   "supplies about half the world's."],
        ),
    },

    extraNotes=[
        "The margin on p. 142 heads its OECD entry 경제협력기구, one word short "
        "of 경제협력개발기구, which is how the article itself writes it. Both "
        "stand as printed, and the entry is filed under the full name.",
        "The review gaps on p. 143 are blank in the book and left blank here.",
        "The two charts of 이야기 나누기 are read off the page; the world rank "
        "printed inside each bar of the first is folded into its label.",
    ],
)
