# -*- coding: utf-8 -*-
"""Chapter 25 — Everyday life and economic activity.

The first chapter of 제5편 경제, transcribed from the photos of pp. 136-139.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, FIGURE, LABELS, TABLE,
               CELL, CHART, GLOSSARY)

CHAPTER = dict(
    number=25, slug="25-daily-economic-life",
    unit="경제", title="일상생활과 경제 활동",
    titleEn="Everyday life and economic activity",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 일상생활에서 경제 활동과 관련된 {선택} 상황입니다."),
        LABELS("버스 — 비용: 1,200원, 소요시간: 30분",
               "택시 — 비용: 5,000원, 소요시간: 10분"),
        FIGURE("책상에 앉아 버스와 택시를 나란히 떠올리는 사람"),
        HEADING(4, "01 이와 같은 상황에서 나라면 어떤 방법을 선택할까요? 그 이유는 무엇입니까?"),
        HEADING(4, "02 자신의 고향 나라와 한국에서 생활하면서 이처럼 {경제적} 선택을 해야 했던 "
                   "경험을 이야기해 볼까요?"),

        SECTION("goals", "학습목표"),
        BULLET("일상생활 경제 활동의 의미와 {물가}의 개념에 대해 설명할 수 있다.", ordered=True),
        BULLET("한국의 {화폐}와 {결제} {수단}에 대해 이해하고, {합리적}인 경제 활동에 대해 "
               "설명할 수 있다.", ordered=True),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"],
              [["기본", "경제", "27. 장보기와 소비자 보호", "시장의 유형, 장보는 방법"]]),

        SECTION("part", "01 경제 활동이란 무엇일까?"),
        HEADING(2, "경제 활동의 의미"),
        GLOSSARY(("의식주", "입고 먹고 집에서 사는 것", "의식주")),
        PARAGRAPH("사람이 살아가기 위해서는 기본적인 {의식주}와 함께, 다양한 {욕구}와 필요를 "
                  "{채울|채우다} 수 있는 {재화}와 서비스가 {갖추어져|갖추어지다} 있어야 한다. "
                  "한국어 교재, 스마트폰, 화장품 등과 같은 {상품}을 재화라고 하고, 한국어 수업, "
                  "물건 {배달}, 의사의 {진료} 등을 서비스라고 한다."),
        PARAGRAPH("이처럼 사람이 살아가는 데 필요한 재화와 서비스를 만들어 사고 팔며 사용하는 "
                  "모든 활동을 {경제 활동}이라고 말한다. 한국은 개인들의 자유로운 경제 활동을 "
                  "보장하는 {시장경제체제}를 {채택}하고 있어서 경제 활동이 매우 {활발}하게 "
                  "일어난다."),

        HEADING(2, "한국의 물가"),
        GLOSSARY(("공공 요금", "공적인 이익을 목적하는 하는 사업에 대한 요금", "공공 요금")),
        PARAGRAPH("{물가}란 여러 가지 재화나 서비스의 {가치}를 {종합}하여 계산한 {평균적}인 "
                  "가격을 뜻한다. 물가는 사람들의 경제 활동에 큰 영향을 {미친다|미치다}."),
        PARAGRAPH("한국의 물가는 전 세계적으로 어떤 {수준}일까? 한국은 버스나 지하철과 같은 "
                  "대중교통 {요금}, {수도} 요금, {전기} 요금과 같은 {공공 요금}은 {상당히} 싼 "
                  "편이다. 한국의 공공 요금이 싼 이유는 교통, 수도, 전기 등 {공공 서비스}를 "
                  "제공할 때 한국 정부나 정부 관련 기관이 {관여}하기 때문이다."),
        PARAGRAPH("{반면}, 쌀, 고기, 채소, 과일 등과 같은 {식재료} 가격은 상당히 비싸다는 "
                  "{평가}를 받는다. 넓은 지역에서 {농산물}이나 {가축}을 {대규모}로 키우는 외국에 "
                  "비해 한국의 {농지}나 {목장}이 {상대적}으로 좁다는 점도 이와 관련이 있다. "
                  "{한편}, 서울과 그 주변 지역, 그리고 지방 대도시의 경우에는 {부동산} 가격이 "
                  "매우 높다. 서울을 {비롯한|비롯하다} 대도시에는 직장, 학교, 문화 시설 등이 "
                  "많고 그에 따라 인구가 {집중}되어 있기 때문이다."),
        FIGURE("소비자물가동향(통계청, 2020) — 2019년 10월부터 2020년 10월까지의 소비자물가 "
               "추이를 그린 꺾은선 그래프"),
        CHART("주요국 소비자물가 상승률 (2019년 6월 기준 세계 53개국 통계 전년 동기 대비) "
              "(출처: 국제결제은행, 연합뉴스, 2019)", "%",
              [["멕시코", 3.9],
               ["홍콩", 3.2],
               ["중국", 2.9],
               ["영국", 2.0],
               ["평균", 1.9],
               ["미국", 1.6],
               ["독일", 1.6],
               ["호주", 1.6],
               ["프랑스", 1.2],
               ["한국", 0.7],
               ["스위스", 0.6],
               ["스페인", 0.4],
               ["포르투갈", 0.4],
               ["그리스", -0.3]]),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "내 것, 남의 것에서 ‘우리’의 것으로, 공유경제"),
        PARAGRAPH("21세기 세상을 바꿀 수 있는 아이디어 중 하나인 ‘{공유경제}’가 한국에서도 "
                  "{활성화}되고 있다. 공유경제란 {일방적}인 {소유}의 개념이 아닌 빌려 쓰고, 나눠 "
                  "쓰는 경제 활동을 의미한다. 서울의 {따릉이}와 같은 공공 자전거 서비스는 "
                  "{전국적}으로 활성화되어 있으며, 자동차나 주택 {공유} 서비스도 많은 사람들이 "
                  "{유용}하게 활용하고 있다. 그 밖에 지방 자치단체를 중심으로 장난감, 우산, "
                  "가정용 {공구}, {도서} 등을 {저렴}한 가격에 빌려주기도 한다."),
        FIGURE("공공 자전거를 스마트폰으로 빌리는 모습"),

        SECTION("part", "02 경제 활동에서 합리적인 선택은 왜 필요할까?"),
        HEADING(2, "경제 활동에 사용되는 한국의 화폐와 그 변화"),
        GLOSSARY(("신분증", "개인의 정보를 나타내는 증명서(주민등록증, 외국인등록증, "
                            "운전면허증, 여권 등)", "신분증"),
                 ("수표", "십만원권 수표", "수표")),
        PARAGRAPH("재화나 서비스를 {사고파는|사고팔다} 경제 활동을 하는 과정에서 {화폐}가 "
                  "사용된다. 한국의 화폐는 {동전}과 {지폐}로 {나뉜다|나뉘다}. 동전은 1원, 5원, "
                  "10원, 50원, 100원, 500원이 있고, 지폐는 1,000원, 5,000원, 10,000원, "
                  "50,000원이 있다. 일상생활에서 1원, 5원짜리 동전은 거의 사용되지 않는다. 그 "
                  "밖에 100,000원 이상의 {수표}를 사용할 수도 있다. 수표를 사용할 경우에는 "
                  "본인의 {신분증}을 {제시}하고, 일반적으로 수표 {뒷면}에 이름이나 {서명}, "
                  "{연락처}를 적는다."),
        PARAGRAPH("최근에는 동전이나 지폐와 같은 화폐 사용이 {줄어들고|줄어들다} {신용카드}나 "
                  "{체크카드} 사용 {비중}이 늘고 있다. 또한, 스마트폰이 널리 활성화되면서 모바일 "
                  "{간편 결제} 서비스를 활용하는 사람도 크게 늘어나고 있다. 모바일 간편 결제 "
                  "서비스는 주로 ‘○○ 페이’라는 이름을 가지고 있다."),
        FIGURE("모바일 간편 결제 서비스 이용현황(2019)"),
        FIGURE("신용카드 결제 모습"),
        FIGURE("○○페이 결제 모습"),

        HEADING(2, "한국에서 합리적인 경제 활동하기"),
        GLOSSARY(("능동적", "다른 것의 영향을 받지 않고, 스스로 움직이는 것", "능동적")),
        PARAGRAPH("빠르게 변화하는 한국의 경제 상황에서 {능동적}으로 생활하려면 {합리적}으로 "
                  "선택하는 능력을 {길러야|기르다} 한다. 예를 들어, {월급}을 받으면 옷을 살까, "
                  "영화를 볼까, {저축}을 한다면 얼마를 할까 등과 같이 어디에 어떻게 사용하는 "
                  "것이 좋을지 결정해야 한다. 돈이나 시간이 {충분}하다면 이와 같은 {고민}을 할 "
                  "필요가 없을 것이다. 그러나 {현실적}으로는 {제한}된 {비용}과 시간으로 모든 "
                  "것을 다 할 수는 없기 때문에 다양한 {기준}과 {대안}을 살펴보면서 더 가치 있고 "
                  "필요한 것을 선택해야 한다. 경제 활동을 잘 하기 위해서는 이러한 합리적 선택이 "
                  "필요하다."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "‘○○페이 됩니다’ 간편 결제 서비스란?"),
        PARAGRAPH("간편 결제 서비스란 지갑에서 플라스틱 카드를 {꺼내지|꺼내다} 않고도 "
                  "온·오프라인에서 스마트폰으로 결제할 수 있는 서비스를 말한다. {기존} 모바일 "
                  "결제는 액티브X, 키보드 {보안프로그램} 등 각종 {플러그인}을 {설치}하고 매번 "
                  "카드 정보나 개인정보를 {입력}해야 하는 {번거로움}이 있었다."),
        PARAGRAPH("간편 결제는 이런 {복잡}한 {단계}를 {없앴기|없애다} 때문에 카드 정보를 한 번만 "
                  "입력해 놓으면 이후에는 아이디와 비밀번호, 휴대 전화 번호, SMS 등을 이용한 "
                  "간단한 {인증}만으로 빠르고 {간편}하게 결제할 수 있다."),
        FIGURE("가게에서 스마트폰으로 결제하는 모습"),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 경제 활동이란 무엇일까?"),
        BULLET("사람이 살아가는 데 필요한 재화와 서비스를 만들어 사고 팔며 사용하는 모든 활동을 "
               "( 경제 활동 )이라고 한다."),
        BULLET("여러 가지 재화나 서비스의 가치를 종합하여 계산한 평균적인 가격을 ( 물가 )라고 "
               "한다."),
        BULLET("한국의 공공 요금은 다른 나라와 비교하여 대체로 ( 싼 ) 편이고, 식재료 가격은 "
               "상대적으로 ( 비싼 ) 편이다. ( 해당되는 단어에 ○표 하기 )"),
        HEADING(3, "02 경제 활동에서 합리적인 선택은 왜 필요할까?"),
        BULLET("( 화폐 )는 사람들 간에 재화나 서비스를 사고 팔 때 사용하는 수단이다."),
        BULLET("한국의 지폐 중 가장 높은 가치를 가지고 있는 것은 ( 오만 원 )권이고, 십만 원 "
               "이상은 ( 수표 )를 사용할 수도 있다."),
        BULLET("한국에서 경제 활동을 잘 하기 위해서는 다양한 기준과 대안을 살펴보면서 더 가치 "
               "있고 필요한 것을 선택해야 한다. 이를 ( 합리적 ) 선택이라고 한다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "이 돈으로 무엇을 할 수 있을까?"),
        PARAGRAPH("경제 활동에서 여러 가지 중에 하나를 결정해야 하는 상황, 즉 합리적인 선택을 "
                  "하기 위해서는 다음과 같은 과정이 필요하다."),
        BULLET("자신이 사용할 수 있는 돈을 확인한다.", ordered=True),
        BULLET("사려고 하는 재화나 서비스의 종류를 {탐색}한다.", ordered=True),
        BULLET("재화나 서비스의 비용을 살펴본다.", ordered=True),
        BULLET("비용 {대비} 나에게 가장 이익이 되고 필요한 것을 선택한다.", ordered=True),
        BULLET("재화나 서비스 선택의 결과를 평가한다.", ordered=True),
        PARAGRAPH("★ 위의 과정을 참고하여 본인에게 50,000원이 생겼다면, 이번 주말에 이 돈을 "
                  "어떻게 사용하고 싶은지 이야기해 봅시다."),
    ],

    english={
        "경제 활동의 의미": dict(
            title="What economic activity is",
            paragraphs=[
                "To live, a person needs the basics of clothing, food and "
                "shelter, and also goods and services that can meet all "
                "manner of wants and needs. Wares such as a Korean textbook, "
                "a smartphone or cosmetics are goods; a Korean lesson, a "
                "delivery, a doctor's consultation are services.",

                "Every activity of making, buying, selling and using the "
                "goods and services a person needs in order to live is "
                "economic activity. Korea has adopted a market economy, which "
                "guarantees individuals their freedom of economic activity, "
                "and economic activity there is accordingly very lively.",
            ],
        ),
        "한국의 물가": dict(
            title="Prices in Korea",
            paragraphs=[
                "물가 means the average price arrived at by taking the value "
                "of many goods and services together. It bears heavily on how "
                "people go about their economic lives.",

                "Where do Korea's prices stand in the world? Public charges — "
                "public-transport fares for the bus or the underground, water, "
                "electricity — are on the cheap side. They are cheap because "
                "the Korean government, or a body connected with it, has a "
                "hand in providing transport, water and power.",

                "Food, on the other hand — rice, meat, vegetables, fruit — is "
                "reckoned dear. That has something to do with Korea's fields "
                "and pastures being small next to countries that raise crops "
                "and livestock on a large scale over wide areas. Property, "
                "meanwhile, is very expensive in Seoul and around it and in "
                "the provincial cities. That is because Seoul and the other "
                "cities hold so many workplaces, schools and cultural "
                "facilities, and the population has gathered where they are.",
            ],
        ),
        "경제 활동에 사용되는 한국의 화폐와 그 변화": dict(
            title="The money Korea uses, and how it is changing",
            paragraphs=[
                "Money is used in the course of the buying and selling that "
                "makes up economic activity. Korean money divides into coins "
                "and notes. The coins are 1, 5, 10, 50, 100 and 500 won; the "
                "notes 1,000, 5,000, 10,000 and 50,000 won. The 1 and 5 won "
                "coins are hardly ever used in daily life. Beyond that, a "
                "cheque may be used for 100,000 won or more. The payer shows "
                "identification and ordinarily writes a name, a signature and "
                "a telephone number on the back of it.",

                "Lately cash — coins and notes — has been used less, and the "
                "share taken by credit and debit cards has grown. As "
                "smartphones have spread, the number of people using mobile "
                "payment services has risen sharply too. Those services "
                "mostly go by the name of “○○ Pay”.",
            ],
        ),
        "한국에서 합리적인 경제 활동하기": dict(
            title="Making sound economic choices in Korea",
            paragraphs=[
                "Living on your own terms in Korea's fast-changing economy "
                "means cultivating the ability to choose sensibly. When your "
                "salary comes in you must decide where and how to spend it: "
                "clothes or a film, and how much to put by. Were money and "
                "time unlimited there would be no need to weigh any of it. "
                "In practice, though, limited money and time will not stretch to "
                "everything, so you have to weigh various standards against "
                "various alternatives and choose what is worth more and "
                "needed more. Doing well economically calls for choices made "
                "that way.",
            ],
        ),
    },

    extraAnnotations={
        "경제 활동": dict(
            hanja="經濟活動", meaning="economic activity",
            characters=[("經", "경", "to manage, a classic — as in 경영, 경력"),
                        ("濟", "제", "to relieve, to cross — as in 구제"),
                        ("活", "활", "living — as in 생활, 활동"),
                        ("動", "동", "to move — as in 운동, 역동성")],
        ),
        "선택": dict(
            hanja="選擇", meaning="a choice",
            characters=[("選", "선", "to choose — as in 선거, 선출"),
                        ("擇", "택", "to pick — as in 채택")],
        ),
        "경제적": dict(hanja="經濟的", meaning="economic, financial"),
        "의식주": dict(
            hanja="衣食住", meaning="clothing, food and shelter",
            characters=[("衣", "의", "clothing — as in 의류, 의복"),
                        ("食", "식", "food — as in 식사, 식재료"),
                        ("住", "주", "dwelling — as in 주거, 주택")],
            notes=["The three necessities, in the order Korean always names "
                   "them. Chapter 14 is 전통 의식주."],
        ),
        "욕구": dict(
            hanja="慾求", meaning="a want, a desire",
            characters=[("慾", "욕", "desire — as in 욕심, 식욕"),
                        ("求", "구", "to seek — as in 요구, 추구")],
        ),
        "채우다": dict(meaning="to fill, to satisfy (a need)"),
        "재화": dict(
            hanja="財貨", meaning="goods",
            characters=[("財", "재", "wealth — as in 재산, 재정"),
                        ("貨", "화", "goods, money — as in 화폐, 백화점")],
            notes=["Set against 서비스: a good is a thing, a service is work "
                   "done."],
        ),
        "갖추어지다": dict(meaning="to be in place, to be provided for"),
        "상품": dict(
            hanja="商品", meaning="a ware, an item for sale",
            characters=[("商", "상", "commerce — as in 상인, 상업"),
                        ("品", "품", "article — as in 제품, 작품")],
        ),
        "배달": dict(
            hanja="配達", meaning="delivery",
            characters=[("配", "배", "to distribute — as in 배정, 배려"),
                        ("達", "달", "to reach — as in 발달, 전달")],
        ),
        "진료": dict(
            hanja="診療", meaning="medical treatment, a consultation",
            characters=[("診", "진", "to examine (a patient) — as in 진찰"),
                        ("療", "료", "to cure — as in 치료, 의료")],
        ),
        "시장경제체제": dict(
            hanja="市場經濟體制", meaning="a market economy",
            characters=[("體", "체", "body — as in 단체, 구체적"),
                        ("制", "제", "system — as in 제도, 단원제")],
            notes=["Set against 계획경제, the planned economy — which is the "
                   "note in your margin."],
        ),
        "채택": dict(hanja="採擇", meaning="adoption, to adopt"),
        "활발": dict(
            hanja="活潑", meaning="being lively, brisk",
            characters=[("活", "활", "living — as in 활동, 활성화"),
                        ("潑", "발", "to splash, spirited")],
        ),
        "물가": dict(
            hanja="物價", meaning="prices, the price level",
            characters=[("物", "물", "thing — as in 물건, 건축물"),
                        ("價", "가", "price — as in 가격, 평가")],
            notes=["Not one price but the general level of them — 물가가 "
                   "오르다 “prices are rising”."],
        ),
        "가치": dict(
            hanja="價値", meaning="value",
            characters=[("値", "치", "worth — as in 수치 “a figure”")],
        ),
        "종합": dict(
            hanja="綜合", meaning="taking together, aggregating",
            characters=[("綜", "종", "to gather, to compile"),
                        ("合", "합", "to join — as in 합의, 통합")],
        ),
        "평균적": dict(hanja="平均的", meaning="average"),
        "미치다": dict(
            meaning="to reach, to bear on",
            notes=["영향을 미치다 “to have an influence on”."],
        ),
        "수준": dict(
            hanja="水準", meaning="a level, a standard",
            characters=[("水", "수", "water — as in 수도, 수해"),
                        ("準", "준", "standard — as in 기준, 준비")],
        ),
        "요금": dict(
            hanja="料金", meaning="a charge, a fare",
            characters=[("料", "료", "fee, material — as in 재료, 자료"),
                        ("金", "금", "money — as in 세금, 요금")],
        ),
        "수도": dict(
            hanja="水道", meaning="the water supply",
            notes=["Not the 수도 “capital city” (首都), which is the 수도권 of "
                   "chapter 6."],
        ),
        "전기": dict(hanja="電氣", meaning="electricity"),
        "공공 요금": dict(
            hanja="公共料金", meaning="public charges, utility charges",
            notes=["The margin gloss reads 공적인 이익을 목적하는 하는, with 하는 "
                   "twice over. That is the book's own slip; it stands as "
                   "printed."],
        ),
        "상당히": dict(
            hanja="相當히", meaning="considerably, quite",
        ),
        "공공 서비스": dict(hanja="公共서비스", meaning="a public service"),
        "관여": dict(hanja="關與", meaning="involvement, having a hand in"),
        "반면": dict(
            hanja="反面", meaning="on the other hand",
            characters=[("反", "반", "opposite — as in 반대, 반영"),
                        ("面", "면", "side, face — as in 측면, 장면")],
        ),
        "식재료": dict(
            hanja="食材料", meaning="foodstuffs, ingredients",
            characters=[("材", "재", "material — as in 재료, 인재")],
        ),
        "평가": dict(hanja="評價", meaning="an assessment, being reckoned"),
        "농산물": dict(
            hanja="農産物", meaning="farm produce",
            characters=[("農", "농", "farming — as in 농업, 농촌"),
                        ("産", "산", "to produce — as in 생산, 출산")],
        ),
        "가축": dict(
            hanja="家畜", meaning="livestock",
            characters=[("家", "가", "house — as in 가족, 농가"),
                        ("畜", "축", "to raise (animals) — as in 축산업")],
        ),
        "대규모": dict(
            hanja="大規模", meaning="large scale",
            characters=[("規", "규", "rule, scale — as in 규정, 규칙"),
                        ("模", "모", "pattern, model — as in 모범")],
        ),
        "농지": dict(hanja="農地", meaning="farmland"),
        "목장": dict(
            hanja="牧場", meaning="a pasture, a ranch",
            characters=[("牧", "목", "to herd — as in 목축"),
                        ("場", "장", "place — as in 시장, 직장")],
        ),
        "상대적": dict(hanja="相對的", meaning="relative, comparatively"),
        "한편": dict(meaning="meanwhile, for that matter"),
        "부동산": dict(
            hanja="不動産", meaning="property, real estate",
            characters=[("動", "동", "to move — as in 운동, 활동"),
                        ("産", "산", "property, produce — as in 재산, 생산")],
            notes=["Literally “immovable property”. 부동산 중개 업소 is the estate "
                   "agent of chapter 5."],
        ),
        "비롯하다": dict(meaning="to include, starting with"),
        "집중": dict(
            hanja="集中", meaning="concentration",
            characters=[("集", "집", "to gather — as in 집회, 집단"),
                        ("中", "중", "middle — as in 중심, 집중적")],
        ),
        "공유경제": dict(
            hanja="共有經濟", meaning="the sharing economy",
            characters=[("共", "공", "together — as in 공동, 공공"),
                        ("有", "유", "to have — as in 소유, 유권자")],
        ),
        "활성화": dict(hanja="活性化", meaning="taking hold, being invigorated"),
        "일방적": dict(
            hanja="一方的", meaning="one-sided",
            notes=["The book contrasts 일방적인 소유 with borrowing and sharing."],
        ),
        "소유": dict(
            hanja="所有", meaning="ownership",
            characters=[("所", "소", "that which — as in 장소, 소감")],
        ),
        "따릉이": dict(
            meaning="Ttareungi, Seoul's public bicycles",
            notes=["따르릉, a bicycle bell, plus the diminutive 이. Busan's is "
                   "따부기, Daejeon's 타슈."],
        ),
        "전국적": dict(hanja="全國的", meaning="nationwide"),
        "공유": dict(hanja="共有", meaning="sharing, holding in common"),
        "유용": dict(
            hanja="有用", meaning="being useful",
            characters=[("用", "용", "to use — as in 사용, 활용")],
        ),
        "공구": dict(
            hanja="工具", meaning="a tool",
            characters=[("工", "공", "work, craft — as in 공업, 공사"),
                        ("具", "구", "implement — as in 도구, 구체적")],
        ),
        "도서": dict(
            hanja="圖書", meaning="books",
            characters=[("圖", "도", "picture, plan — as in 지도, 의도"),
                        ("書", "서", "writing, book — as in 서명, 문서")],
            notes=["The formal word — 도서관 is the library."],
        ),
        "저렴": dict(
            hanja="低廉", meaning="being inexpensive",
            characters=[("低", "저", "low — as in 저출산, 저축's 貯 is separate"),
                        ("廉", "렴", "cheap, upright — as in 청렴")],
        ),
        "사고팔다": dict(meaning="to buy and sell"),
        "화폐": dict(
            hanja="貨幣", meaning="money, currency",
            characters=[("貨", "화", "goods, money — as in 재화, 화물"),
                        ("幣", "폐", "currency, silk offering")],
        ),
        "동전": dict(
            hanja="銅錢", meaning="a coin",
            characters=[("銅", "동", "copper — as in 동상 “a bronze statue”"),
                        ("錢", "전", "coin, money")],
        ),
        "지폐": dict(
            hanja="紙幣", meaning="a banknote",
            characters=[("紙", "지", "paper — as in 편지, 신문지"),
                        ("幣", "폐", "currency — the same 幣 as in 화폐")],
        ),
        "나뉘다": dict(meaning="to be divided into"),
        "수표": dict(
            hanja="手票", meaning="a cheque",
            characters=[("手", "수", "hand — as in 수술, 선수"),
                        ("票", "표", "ticket, slip — as in 투표, 득표율")],
        ),
        "신분증": dict(
            hanja="身分證", meaning="an identity card",
            characters=[("身", "신", "body, self — as in 자신, 신체"),
                        ("分", "분", "part, station — as in 부분, 신분"),
                        ("證", "증", "proof — as in 증인, 증명")],
        ),
        "제시": dict(hanja="提示", meaning="presenting, showing"),
        "뒷면": dict(meaning="the reverse, the back"),
        "서명": dict(
            hanja="署名", meaning="a signature",
            characters=[("署", "서", "office, to sign — as in 관공서"),
                        ("名", "명", "name — as in 성명, 유명")],
        ),
        "연락처": dict(
            hanja="連絡處", meaning="contact details",
            characters=[("連", "연", "to connect — as in 연결, 연속"),
                        ("絡", "락", "to entwine, to contact")],
        ),
        "줄어들다": dict(meaning="to decrease, to dwindle"),
        "신용카드": dict(
            hanja="信用카드", meaning="a credit card",
            characters=[("信", "신", "trust — as in 신뢰, 통신"),
                        ("用", "용", "to use — as in 사용, 이용")],
        ),
        "체크카드": dict(
            meaning="a debit card",
            notes=["Draws straight from the account, unlike 신용카드."],
        ),
        "비중": dict(
            hanja="比重", meaning="a share, relative weight",
            characters=[("比", "비", "to compare — as in 비율, 비교"),
                        ("重", "중", "heavy — as in 중요, 중임")],
        ),
        "간편 결제": dict(
            hanja="簡便決濟", meaning="simple payment, one-tap payment",
            characters=[("簡", "간", "simple, brief — as in 간단"),
                        ("便", "편", "convenient — as in 편리, 불편")],
        ),
        "결제": dict(
            hanja="決濟", meaning="payment, settlement",
            characters=[("決", "결", "to settle — as in 결정, 해결"),
                        ("濟", "제", "to settle, to relieve — as in 경제")],
            notes=["결제 is paying for something; 결재 does not exist, though "
                   "결재(決裁) “approval” is a different word people confuse it "
                   "with."],
        ),
        "수단": dict(
            hanja="手段", meaning="a means",
            characters=[("手", "수", "hand — as in 수표, 선수"),
                        ("段", "단", "step, grade — as in 단계, 계단")],
        ),
        "능동적": dict(
            hanja="能動的", meaning="active, self-directed",
            characters=[("能", "능", "ability — as in 능력, 가능"),
                        ("動", "동", "to move — as in 활동, 운동")],
            notes=["Its opposite is 수동적, passive."],
        ),
        "합리적": dict(
            hanja="合理的", meaning="rational, sound",
            characters=[("合", "합", "to fit — as in 합의, 적합"),
                        ("理", "리", "reason — as in 원리, 관리")],
            notes=["Literally “fitting reason”. Its opposite 불합리하다 is "
                   "chapter 21's word."],
        ),
        "기르다": dict(meaning="to cultivate, to bring up"),
        "월급": dict(
            hanja="月給", meaning="a monthly salary",
            characters=[("給", "급", "to give, to pay — as in 발급, 공급")],
        ),
        "저축": dict(
            hanja="貯蓄", meaning="saving",
            characters=[("貯", "저", "to store up"),
                        ("蓄", "축", "to accumulate — as in 축적")],
        ),
        "충분": dict(
            hanja="充分", meaning="being enough",
            characters=[("充", "충", "to fill — as in 확충, 보충"),
                        ("分", "분", "part — as in 부분, 분산")],
        ),
        "고민": dict(
            hanja="苦悶", meaning="worrying over something, a dilemma",
            characters=[("苦", "고", "bitter, hardship — as in 고생"),
                        ("悶", "민", "to be distressed")],
        ),
        "현실적": dict(hanja="現實的", meaning="realistic, in practice"),
        "제한": dict(
            hanja="制限", meaning="a limit, restriction",
            characters=[("制", "제", "to control — as in 제도, 규제"),
                        ("限", "한", "limit — as in 권한, 기한")],
        ),
        "비용": dict(
            hanja="費用", meaning="cost, expense",
            characters=[("費", "비", "to spend — as in 학비, 회비")],
        ),
        "기준": dict(hanja="基準", meaning="a standard, a criterion"),
        "대안": dict(
            hanja="代案", meaning="an alternative",
            characters=[("代", "대", "to substitute — as in 대표, 대신"),
                        ("案", "안", "plan, draft — as in 법안, 예산안")],
        ),
        "꺼내다": dict(meaning="to take out, to pull out"),
        "기존": dict(
            hanja="旣存", meaning="existing, the older kind",
            characters=[("旣", "기", "already"),
                        ("存", "존", "to exist — as in 존재, 보존")],
        ),
        "보안프로그램": dict(
            hanja="保安프로그램", meaning="a security program",
            notes=["The keyboard-security plug-ins Korean banking sites used "
                   "to require, alongside ActiveX."],
        ),
        "플러그인": dict(meaning="a plug-in"),
        "설치": dict(hanja="設置", meaning="installation"),
        "입력": dict(
            hanja="入力", meaning="input, entering",
            characters=[("入", "입", "to enter — as in 입국, 수입"),
                        ("力", "력", "force — as in 능력, 압력")],
        ),
        "번거로움": dict(
            meaning="the bother of something",
            notes=["From 번거롭다 “to be troublesome, fussy”."],
        ),
        "복잡": dict(
            hanja="複雜", meaning="being complicated, crowded",
            characters=[("複", "복", "double, repeated — as in 복수"),
                        ("雜", "잡", "mixed, miscellaneous — as in 혼잡")],
        ),
        "단계": dict(
            hanja="段階", meaning="a step, a stage",
            characters=[("段", "단", "step — as in 수단, 단락"),
                        ("階", "계", "grade, floor — as in 계층, 계단")],
        ),
        "없애다": dict(
            meaning="to do away with, to get rid of",
            notes=["없다's causative — to make something not be. Spelled with "
                   "ㅐ, not the 없에다 people often write."],
        ),
        "인증": dict(
            hanja="認證", meaning="authentication",
            characters=[("認", "인", "to recognise — as in 인정, 확인"),
                        ("證", "증", "proof — as in 신분증, 증명")],
        ),
        "간편": dict(hanja="簡便", meaning="being simple and convenient"),
        "탐색": dict(
            hanja="探索", meaning="searching out, exploring",
            characters=[("探", "탐", "to search — as in 탐구, 탐험"),
                        ("索", "색", "to seek — as in 검색, 수색")],
        ),
        "대비": dict(
            hanja="對比", meaning="comparison, against",
            notes=["비용 대비 “against the cost”. Not the 대비 “preparation” "
                   "(對備) of chapter 22's 검역."],
        ),
    },

    extraNotes=[
        "Chapter 25 has no Google Doc: the Korean is my reading of the photos "
        "of pp. 136-139, so it is worth checking against the pages.",
        "The 공공 요금 gloss on p. 137 prints 목적하는 하는, with 하는 twice. "
        "That is the book's own slip and stands as printed.",
        "The 소비자물가 추이 line chart on p. 137 and the 모바일 간편 결제 chart "
        "on p. 138 are not reproduced — their figures are too small to read "
        "off the photograph with any confidence. The 주요국 소비자물가 상승률 "
        "bars are.",
        "그리스 stands at -0.3% in that chart, and a negative bar draws as no "
        "bar at all; the figure is printed beside it either way.",
        "The five steps of 이야기 나누기 are printed as boxes joined by arrows; "
        "they are set here as a numbered list.",
        "The review gaps on p. 139 carry your own pencilled answers — 경제 "
        "활동, 물가, 싼/비싼, 화폐, 오만 원, 수표, 합리적.",
    ],
)
