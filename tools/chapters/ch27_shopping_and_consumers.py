# -*- coding: utf-8 -*-
"""Chapter 27 — Shopping and consumer protection.

Transcribed from the photos of pp. 144-147.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, FIGURE, LABELS, TABLE,
               GLOSSARY, CELL)

CHAPTER = dict(
    number=27, slug="27-shopping-and-consumers",
    unit="경제", title="장보기와 소비자 보호",
    titleEn="Shopping and consumer protection",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 한국에서 볼 수 있는 여러 가지 {시장}의 모습입니다."),
        LABELS("전통 시장", "대형 마트", "텔레비전 홈쇼핑", "온라인 쇼핑"),
        HEADING(4, "01 사진 중에서 자신이 한국에서 이용해 본 시장은 어디입니까?"),
        HEADING(4, "02 자신이 가장 자주 이용하는 시장과 그 이유는 무엇입니까?"),

        SECTION("goals", "학습목표"),
        BULLET("다양한 {장보기} 방법을 알고, 이를 일상생활에서 활용할 수 있다.", ordered=True),
        BULLET("{소비자}의 권리와 책임에 대해 설명할 수 있다.", ordered=True),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"],
              [["기본", "경제", "25. 일상생활과 경제 활동", "경제 활동의 의미, 결제 방법"]]),

        SECTION("part", "01 어디에서 장을 보면 될까?"),
        HEADING(2, "다양한 종류의 시장"),
        GLOSSARY(("흥정", "물건 값이나 양에 대해 의논하는 것. 사는 사람은 값을 깎아 달라고 하거나 "
                          "더 많은 양을 달라고 하고, 파는 사람은 그렇게 안 하려고 함", "흥정")),
        PARAGRAPH("한국에는 다양한 종류의 시장이 있다. 날마다 열리는 시장을 {상설} "
                  "시장이라고 하는데 {전통 시장}, {대형 마트}, {백화점}, 슈퍼마켓, {편의점} 등이 "
                  "여기에 {해당}한다. 먼저, 전통 시장은 작은 {상점}들이 모여 있는 곳으로 상점 "
                  "주인이 물건을 직접 파는 경우가 많아 가격 {흥정}을 하는 모습도 {흔히} 볼 수 "
                  "있다. 이러한 점 때문에 {국내외} {관광객}들이 많이 찾기도 한다."),
        PARAGRAPH("다음으로 대형 마트와 백화점은 {농수산물}부터 {공산품}에 이르기까지 다양한 "
                  "종류의 물건을 팔고 있는 {현대식} 시장이다. {주차장}이 넓고 물건 종류가 많아 "
                  "{한꺼번에} 많은 물건을 사려는 소비자에게 인기가 있다. 백화점은 대형 마트에 "
                  "비해 좀 더 비싸고 {고급스러운|고급스럽다} 물건을 많이 판다."),
        PARAGRAPH("그리고 슈퍼마켓과 편의점에서는 주로 {식료품}과 간단한 {생활용품}을 판다. "
                  "슈퍼마켓과 편의점은 사람들이 많이 모여 살거나 {이동}이 많은 곳에서 주로 볼 수 "
                  "있다. 특히 편의점은 {판매}하는 품목의 종류가 2,000개에 {달하고|달하다}, "
                  "24시간 이용할 수 있어서 젊은 {층}이 많이 찾는 곳이다. 한편, 3일에 한 번씩 "
                  "열리는 {3일장}, 5일에 한 번씩 열리는 {5일장}과 같은 {정기 시장}도 아직 남아 "
                  "있다. 정기 시장에서는 그 지역의 {특산품}이나 {상인}이 직접 키운 농산물 등을 "
                  "사고 팔 수 있다."),
        FIGURE("백화점"),
        FIGURE("편의점"),

        HEADING(2, "텔레비전 홈쇼핑과 온라인 쇼핑"),
        PARAGRAPH("{정보 통신} 기술이 {발달}하면서 텔레비전 {홈쇼핑}과 {온라인 쇼핑} 비중이 늘고 "
                  "있다. 홈쇼핑은 텔레비전을 통해 {소개}되는 상품을 직접 보면서 전화로 {주문}할 "
                  "수 있어 편리하다. 인터넷이나 쇼핑 {앱}을 이용하는 온라인 쇼핑의 인기도 매우 "
                  "높다. 특히, 코로나19 이후에는 사람들의 이동이 줄어들면서 온라인 쇼핑을 통해 "
                  "식료품, {생활물품}을 주문하는 사람들이 많아졌다. 홈쇼핑이나 온라인 쇼핑을 "
                  "이용할 때는 {물품}을 직접 볼 수 없으므로 먼저 {구매}한 사람들의 {상품평} 등을 "
                  "{참고}하는 것이 좋다."),
        FIGURE("모바일쇼핑 거래액 (통계청, 온라인 쇼핑 동향(2020.7)) — 2019년 7월 7조 2,146억 "
               "원에서 2020년 7월 8조 7,833억 원으로 21.7% 늘었다"),
        FIGURE("오프라인·온라인 쇼핑 현황 (통계청, 2019)"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "지역사랑 상품권을 아시나요?"),
        PARAGRAPH("{지역사랑 상품권}은 각 지역의 지방자치단체에서 {발행}하는 {상품권}으로 그 "
                  "지역에 있는 {가맹점}(사용하기로 약속을 맺은 상점)에서만 사용할 수 있고 {농협}, "
                  "{신협}, {새마을금고} 등에서 {구입}할 수 있다. 이 상품권을 이용하면 "
                  "기본적으로 0.5~10% 정도 {할인}을 받을 수 있고 명절에는 {추가} 할인도 받을 수 "
                  "있다. 전통 시장뿐만 아니라 {주유소}, 식당, {서점}, {학원} 등 가맹점 {스티커}가 "
                  "붙어 있는 곳이라면 어디에서든 {현금}처럼 사용이 가능하다."),
        FIGURE("지역사랑상품권 홍보물 — ‘마음은 ⊕, 부담은 ⊖, 지역경제는 ⊕, 상생의 가치를 ⊗’"),

        SECTION("part", "02 소비자의 권리와 책임에는 어떤 것이 있을까?"),
        HEADING(2, "소비자가 보호 받을 권리"),
        GLOSSARY(("수리", "고장나거나 잘못된 곳을 고침", "수리"),
                 ("환불", "이미 낸 돈을 돌려 받음", "환불"),
                 ("소비자기본법", "소비자의 권리와 책임을 정해 놓고 있는 법으로 안정적인 소비 "
                                  "생활과 경제 발전을 목적으로 함", "소비자기본법")),
        PARAGRAPH("{소비자}가 제품을 {구입}하거나 서비스를 이용할 때 피해를 입거나 {불만}을 "
                  "느끼는 경우가 발생한다. 이러한 경우에 소비자는 {수리}, {교환}, {환불}, 피해 "
                  "{보상} 등과 같은 보호를 받을 수 있다."),
        PARAGRAPH("한국에서는 소비자가 제품을 구입하고 사용할 때 {누릴|누리다} 수 있는 권리를 "
                  "{소비자기본법}으로 정해 놓고 있다. 구입한 제품에서 문제가 발생한 경우에는 먼저 "
                  "그 물건을 구입한 상점이나 그것을 만든 기업과의 {상담}을 통해 피해 보상을 받을 "
                  "수 있다. 만약 여기에서 문제가 해결되지 않고 {전문가}의 {협조}가 필요한 "
                  "경우에는 {한국소비자원}, {소비자 단체} 등 소비자를 지원해 주는 {전문 기관}의 "
                  "도움을 받을 수 있다. 이들 기관은 {생산자}와 소비자 중 누구에게 책임이 있는지 "
                  "{밝혀|밝히다} 주고 생산자의 잘못일 경우 적절한 보상이 이루어지도록 소비자를 "
                  "도와준다."),
        FIGURE("한국소비자원 누리집 (http://www.kca.go.kr)"),

        HEADING(2, "소비자의 책임"),
        GLOSSARY(("유통기한", "상품이 사람들 사이에 안전하게 거래될 수 있는 기한", "유통기한"),
                 ("영수증", "상품을 구입했음을 증명하는 문서", "영수증")),
        PARAGRAPH("소비자는 자신의 안전과 권리 보호를 위해 {책임감}있는 소비자로서 행동해야 "
                  "한다. 예를 들어, 소비자는 상품을 구입할 때 가격과 {품질}을 비교하고, 음식물의 "
                  "경우 {유통기한}을 반드시 확인해야 한다. 그리고 물건 구입 후에는 {영수증}을 "
                  "통해 정확한 {금액}을 {지불}했는지 확인하며, 교환이나 환불할 일이 생길 경우에는 "
                  "영수증을 제시해야 한다."),
        PARAGRAPH("또한 제품의 사용 {설명서} 및 {주의 사항}을 반드시 읽어 보고 상품을 안전하게 "
                  "사용해야 한다. {소비}에 필요한 {지식}과 정보를 얻기 위해 노력해야 하며, 자원을 "
                  "{절약}하고 환경을 보호하는 {현명}한 소비 생활을 해야 한다."),
        FIGURE("소비자의 책임"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "소비 과정에서 피해를 입었을 때는?"),
        HEADING(4, "1372 소비자 상담센터에 연락하기"),
        BULLET("한국말을 잘하는 사람"),
        BULLET("전화: 1372 + 통화버튼 누르고 안내에 따라 상담", level=2),
        BULLET("인터넷: 1372소비자상담센터(www.1372.go.kr) 접속하여 인터넷상담 클릭", level=2),
        BULLET("한국말을 잘 못하는 사람"),
        BULLET("{다누리콜센터}(1577-1366)로 전화 → 상담원의 통역 → 1372 소비자 상담센터에 연락",
               level=2),
        FIGURE("한국소비자원, 소비자상담 절차 — 소비자가 1372 소비자상담센터(한국소비자원, 10개 "
               "소비자단체, 17개 광역시도 지방자치단체)에 상담을 신청하고, 피해구제는 "
               "한국소비자원으로 이관된다"),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 어디에서 장을 보면 될까?"),
        BULLET("(            )은 작은 상점들이 모여 있는 곳으로 상점 주인과 가격 흥정을 하는 "
               "모습도 흔히 볼 수 있고 국내외 관광객들이 많이 찾기도 한다."),
        BULLET("(        )은 24시간 문을 여는 상점으로 특히 젊은 층이 많이 찾는 곳이다."),
        BULLET("(        )이나 (            )을 이용할 때는 물품을 직접 볼 수 없으므로 먼저 "
               "구매한 사람들의 상품평 등을 참고하여 신중하게 결정할 필요가 있다."),
        HEADING(3, "02 소비자의 권리와 책임에는 어떤 것이 있을까?"),
        BULLET("구입한 상품에서 문제가 발생해 전문가의 협조가 필요한 경우에는 (            )과 "
               "소비자 단체 등 소비자를 지원하는 전문기관의 도움을 받을 수 있다."),
        BULLET("한국에서는 소비자가 상품을 구입하고 사용할 때 누릴 수 있는 권리를 "
               "(            )으로 정해 놓고 있다."),
        BULLET("소비자는 상품을 구입할 때 가격과 품질을 비교하고, 음식물의 경우 (          )을 "
               "반드시 확인해야 한다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "소비자 스스로 안전과 권리 지키기"),
        PARAGRAPH("소비자는 스스로 자신의 안전과 권리를 지키기 위해 상품을 구매하기 전에 가격과 "
                  "품질을 {꼼꼼하게|꼼꼼하다} 살펴야 한다. 그리고 상품의 생산자와 {판매자}는 "
                  "품질과 안전에 대해 책임을 {져야|지다} 한다. 한국에서는 소비자의 권리와 이익을 "
                  "위해 다음과 같이 여러 가지 제도를 마련해 놓고 있다."),
        TABLE(["제조물 책임법", "리콜 제도", "의무표시제"],
              [["상품에 대한 책임을 제조업체가 지게 하는 법",
                "생산자가 소비자에게 상품의 문제를 알려주고, 그 상품을 수리·교환해 주는 제도",
                "원산지 표시, 유통 기한, 영양 성분 표시 등 소비자 안전 등에 중요한 표시를 반드시 "
                "하게 하는 제도"]]),
        PARAGRAPH("★ 자신의 고향 나라에서는 소비자를 보호하는 제도가 무엇이 있는지 이야기해 "
                  "봅시다."),
    ],

    english={
        "다양한 종류의 시장": dict(
            title="Markets of every kind",
            paragraphs=[
                "Korea has markets of many kinds. One that opens every day is "
                "a permanent market: the traditional market, the hypermarket, "
                "the department store, the supermarket and the convenience "
                "store all count as such. The traditional market is a "
                "gathering of small shops, and because the shopkeeper often "
                "sells the goods themselves you will commonly see haggling "
                "over the price. That is part of why visitors from home and "
                "abroad seek them out.",

                "The hypermarket and the department store are modern markets "
                "selling everything from farm and fish produce to "
                "manufactured goods. Their car parks are large and their range "
                "wide, which makes them popular with shoppers buying a great "
                "deal at once. The department store sells rather dearer and "
                "finer goods than the hypermarket.",

                "Supermarkets and convenience stores sell mainly groceries "
                "and simple household goods. They are found chiefly where "
                "many people live close together or pass through. The "
                "convenience store in particular carries as many as two "
                "thousand lines and is open around the clock, which is why "
                "the young go there so much. Periodic markets survive as well "
                "— the 3일장 that opens every third day, the 5일장 every "
                "fifth. At one of those, local specialities and produce the "
                "trader has grown themselves can be bought and sold.",
            ],
        ),
        "텔레비전 홈쇼핑과 온라인 쇼핑": dict(
            title="Television home shopping and online shopping",
            paragraphs=[
                "As information technology has advanced, television home "
                "shopping and online shopping have taken a larger share. Home "
                "shopping is convenient: you see the goods presented on "
                "television and can order by telephone. Online shopping, over "
                "the internet or through a shopping app, is very popular too. "
                "Since COVID-19 in particular, with people moving about less, "
                "many more order groceries and household goods online. "
                "Because you cannot see the goods yourself when shopping "
                "either way, it is worth consulting the reviews of people who "
                "bought before you.",
            ],
        ),
        "소비자가 보호 받을 권리": dict(
            title="The consumer's right to protection",
            paragraphs=[
                "It happens that a consumer suffers harm, or has cause for "
                "complaint, in buying a product or using a service. In such a "
                "case the consumer may claim protection: repair, exchange, a "
                "refund, compensation for the harm done.",

                "Korea sets out the rights a consumer enjoys in buying and "
                "using a product in the Framework Act on Consumers. Where "
                "something goes wrong with a product, compensation may first "
                "be sought by taking it up with the shop it was bought from or "
                "the company that made it. If that does not settle the matter "
                "and expert help is needed, bodies that support consumers — "
                "the Korea Consumer Agency, the consumer organisations — can "
                "be turned to. They establish whether the maker or the "
                "consumer is at fault and, where the maker is, help the "
                "consumer to proper compensation.",
            ],
        ),
        "소비자의 책임": dict(
            title="The consumer's responsibilities",
            paragraphs=[
                "For the sake of their own safety and rights a consumer "
                "should act responsibly. They should compare price against "
                "quality when buying, and always check the use-by date on "
                "food. After buying they should check from the receipt that "
                "the sum paid was right, and keep it to produce should an "
                "exchange or refund be needed.",

                "They should also read the instructions and the cautions "
                "before using a product, and use it safely. They should make "
                "the effort to gain the knowledge and information that "
                "consumption calls for, and consume wisely — sparing "
                "resources and protecting the environment.",
            ],
        ),
    },

    extraAnnotations={
        "시장": dict(
            hanja="市場", meaning="a market",
            characters=[("市", "시", "city, market — as in 도시, 시청"),
                        ("場", "장", "place — as in 장소, 직장")],
        ),
        "장보기": dict(
            meaning="doing the shopping",
            notes=["장을 보다 “to do the shopping”, from 장 “market”. Nothing to "
                   "do with 보다 “to see” in the usual sense."],
        ),
        "소비자": dict(
            hanja="消費者", meaning="a consumer",
            characters=[("消", "소", "to consume, to extinguish — as in 해소"),
                        ("費", "비", "to spend — as in 비용, 학비")],
        ),
        "상설": dict(
            hanja="常設", meaning="permanent, standing",
            characters=[("常", "상", "always, usual — as in 일상, 정상"),
                        ("設", "설", "to establish — as in 시설, 설치")],
            notes=["상설 시장 opens daily, against 정기 시장 which opens on set "
                   "days."],
        ),
        "전통 시장": dict(hanja="傳統市場", meaning="a traditional market"),
        "대형 마트": dict(
            hanja="大型마트", meaning="a hypermarket",
            characters=[("型", "형", "form, type — as in 유형, 모형")],
            notes=["Emart, Homeplus, Lotte Mart and the like."],
        ),
        "백화점": dict(
            hanja="百貨店", meaning="a department store",
            characters=[("百", "백", "hundred — as in 백성"),
                        ("貨", "화", "goods — as in 화폐, 재화"),
                        ("店", "점", "shop — as in 상점, 편의점")],
            notes=["Literally “hundred-goods store”."],
        ),
        "편의점": dict(
            hanja="便宜店", meaning="a convenience store",
            characters=[("便", "편", "convenient — as in 편리, 간편"),
                        ("宜", "의", "suitable")],
        ),
        "해당": dict(hanja="該當", meaning="to count as, to fall under"),
        "상점": dict(hanja="商店", meaning="a shop"),
        "흥정": dict(meaning="haggling, bargaining"),
        "흔히": dict(meaning="commonly, often"),
        "국내외": dict(hanja="國內外", meaning="at home and abroad"),
        "관광객": dict(
            hanja="觀光客", meaning="a tourist",
            characters=[("觀", "관", "to observe — as in 관람, 관심"),
                        ("光", "광", "light — as in 광부's 鑛 is separate"),
                        ("客", "객", "guest — as in 고객, 여객")],
        ),
        "농수산물": dict(
            hanja="農水産物", meaning="farm and fishery produce",
            characters=[("水", "수", "water — as in 수도, 수해")],
        ),
        "공산품": dict(
            hanja="工産品", meaning="manufactured goods",
            characters=[("工", "공", "craft, industry — as in 공업, 공구")],
        ),
        "현대식": dict(
            hanja="現代式", meaning="modern in style",
            characters=[("式", "식", "style, ceremony — as in 방식, 결혼식")],
        ),
        "주차장": dict(
            hanja="駐車場", meaning="a car park",
            characters=[("駐", "주", "to park, to station — as in 주차")],
        ),
        "한꺼번에": dict(meaning="all at once, in one go"),
        "고급스럽다": dict(
            hanja="高級스럽다", meaning="to look or feel upmarket",
            characters=[("級", "급", "grade, class — as in 학급, 등급")],
        ),
        "식료품": dict(
            hanja="食料品", meaning="groceries, foodstuffs",
            characters=[("料", "료", "material, fee — as in 재료, 요금")],
        ),
        "생활용품": dict(hanja="生活用品", meaning="household goods"),
        "이동": dict(hanja="移動", meaning="movement, getting about"),
        "판매": dict(
            hanja="販賣", meaning="sale, selling",
            characters=[("販", "판", "to sell, to trade"),
                        ("賣", "매", "to sell — as in 매장, 판매자")],
        ),
        "달하다": dict(hanja="達하다", meaning="to reach, to amount to"),
        "층": dict(
            hanja="層", meaning="a stratum, an age group; a floor",
            notes=["젊은 층 “the young”, 계층 “a social stratum”, 고층 “a high "
                   "floor” — the same 層."],
        ),
        "3일장": dict(
            hanja="三日場", meaning="a market held every third day",
        ),
        "5일장": dict(
            hanja="五日場", meaning="a market held every fifth day",
            notes=["Still the shape of market life in the countryside; "
                   "정선 5일장 and 모란 5일장 are known nationally."],
        ),
        "정기 시장": dict(
            hanja="定期市場", meaning="a periodic market",
            notes=["Set against 상설 시장: it opens on fixed days rather than "
                   "every day."],
        ),
        "특산품": dict(
            hanja="特産品", meaning="a local speciality",
            characters=[("特", "특", "special — as in 특별, 특권")],
        ),
        "상인": dict(
            hanja="商人", meaning="a trader, a merchant",
            characters=[("商", "상", "commerce — as in 상품, 상점")],
        ),
        "정보 통신": dict(hanja="情報通信", meaning="information and communications"),
        "발달": dict(hanja="發達", meaning="development, advance"),
        "홈쇼핑": dict(meaning="home shopping (by television)"),
        "온라인 쇼핑": dict(meaning="online shopping"),
        "소개": dict(
            hanja="紹介", meaning="introduction, presentation",
            characters=[("紹", "소", "to introduce, to continue"),
                        ("介", "개", "to mediate — as in 중개, 소개")],
        ),
        "주문": dict(
            hanja="注文", meaning="an order",
            characters=[("注", "주", "to pour, to focus — as in 주목, 주의"),
                        ("文", "문", "writing — as in 문서, 문화")],
        ),
        "앱": dict(meaning="an app"),
        "생활물품": dict(hanja="生活物品", meaning="household items"),
        "물품": dict(hanja="物品", meaning="goods, an article"),
        "구매": dict(
            hanja="購買", meaning="purchase",
            characters=[("購", "구", "to purchase"),
                        ("買", "매", "to buy — set against 賣 “to sell”")],
            notes=["買 buys and 賣 sells: the two characters differ by a "
                   "stroke, which Korean solves by reading them 매 alike and "
                   "pairing them as 구매 and 판매."],
        ),
        "상품평": dict(
            hanja="商品評", meaning="a product review",
            characters=[("評", "평", "to judge — as in 평가, 비평")],
        ),
        "참고": dict(
            hanja="參考", meaning="reference, consulting",
            characters=[("參", "참", "to take part — as in 참여, 참석"),
                        ("考", "고", "to consider — as in 사고, 참고인")],
        ),
        "지역사랑 상품권": dict(
            hanja="地域사랑商品券",
            meaning="a local-love gift certificate",
            notes=["Issued by a district and spendable only within it, at a "
                   "discount — a way of keeping money in the local economy."],
        ),
        "발행": dict(hanja="發行", meaning="issuance"),
        "상품권": dict(
            hanja="商品券", meaning="a gift certificate",
            characters=[("券", "권", "ticket, certificate — as in 여권, 승차권")],
        ),
        "가맹점": dict(
            hanja="加盟店", meaning="an affiliated shop, a franchise",
            characters=[("加", "가", "to join — as in 가입, 참가"),
                        ("盟", "맹", "an alliance, an oath")],
        ),
        "농협": dict(
            hanja="農協", meaning="Nonghyup, the agricultural cooperative",
            notes=["Short for 농업협동조합, and one of Korea's largest banks."],
        ),
        "신협": dict(
            hanja="信協", meaning="a credit union",
            notes=["Short for 신용협동조합."],
        ),
        "새마을금고": dict(
            meaning="a Saemaul community finance cooperative",
            notes=["The neighbourhood savings-and-loan society, named after "
                   "the 새마을 movement of the 1970s."],
        ),
        "구입": dict(
            hanja="購入", meaning="purchase, buying in",
            characters=[("入", "입", "to enter — as in 수입, 입력")],
        ),
        "할인": dict(
            hanja="割引", meaning="a discount",
            characters=[("割", "할", "to divide, to cut — as in 분할"),
                        ("引", "인", "to pull — as in 인상, 인용")],
        ),
        "추가": dict(hanja="追加", meaning="addition, further"),
        "주유소": dict(
            hanja="注油所", meaning="a petrol station",
            characters=[("油", "유", "oil — as in 석유, 원유")],
        ),
        "서점": dict(hanja="書店", meaning="a bookshop"),
        "학원": dict(
            hanja="學院", meaning="a private academy",
            notes=["Chapter 10's 학원 — the after-school cram school."],
        ),
        "스티커": dict(meaning="a sticker"),
        "현금": dict(hanja="現金", meaning="cash"),
        "불만": dict(
            hanja="不滿", meaning="dissatisfaction, a complaint",
            characters=[("不", "불", "not — as in 부동산, 불가능"),
                        ("滿", "만", "full — as in 만족, 만원")],
            notes=["Literally “not full” — the opposite of 만족."],
        ),
        "수리": dict(
            hanja="修理", meaning="repair",
            characters=[("修", "수", "to mend, to cultivate — as in 수정"),
                        ("理", "리", "to order — as in 관리, 처리")],
        ),
        "교환": dict(
            hanja="交換", meaning="exchange",
            characters=[("交", "교", "to exchange — as in 교류, 교통"),
                        ("換", "환", "to change — as in 환불, 외환")],
        ),
        "환불": dict(
            hanja="還拂", meaning="a refund",
            characters=[("還", "환", "to return — as in 반환, 귀환"),
                        ("拂", "불", "to pay out — as in 지불")],
        ),
        "보상": dict(
            hanja="補償", meaning="compensation",
            characters=[("補", "보", "to supplement — as in 보충, 후보자"),
                        ("償", "상", "to repay — as in 배상")],
        ),
        "소비자기본법": dict(
            hanja="消費者基本法",
            meaning="the Framework Act on Consumers",
        ),
        "누리다": dict(meaning="to enjoy, to have the benefit of"),
        "상담": dict(
            hanja="相談", meaning="consultation, taking advice",
            characters=[("談", "담", "to talk — as in 덕담, 회담")],
        ),
        "전문가": dict(hanja="專門家", meaning="an expert"),
        "협조": dict(
            hanja="協助", meaning="cooperation, assistance",
            characters=[("協", "협", "to cooperate — as in 협력, 협의"),
                        ("助", "조", "to help — as in 원조, 보조")],
        ),
        "한국소비자원": dict(
            hanja="韓國消費者院", meaning="the Korea Consumer Agency",
            notes=["The state body that mediates consumer disputes; 1372 is "
                   "its counselling line."],
        ),
        "소비자 단체": dict(hanja="消費者團體", meaning="a consumer organisation"),
        "전문 기관": dict(hanja="專門機關", meaning="a specialist body"),
        "생산자": dict(hanja="生産者", meaning="a producer, a maker"),
        "밝히다": dict(meaning="to establish, to make clear"),
        "책임감": dict(
            hanja="責任感", meaning="a sense of responsibility",
            characters=[("感", "감", "to feel — as in 감사, 소감")],
        ),
        "품질": dict(
            hanja="品質", meaning="quality",
            characters=[("品", "품", "article — as in 상품, 품목"),
                        ("質", "질", "quality, substance — as in 질문, 질서")],
        ),
        "유통기한": dict(
            hanja="流通期限", meaning="a sell-by date",
            characters=[("流", "류", "to flow — as in 교류, 유행"),
                        ("通", "통", "to pass — as in 통과, 교통"),
                        ("限", "한", "limit — as in 제한, 권한")],
            notes=["The date up to which a shop may sell it, not the date it "
                   "goes off — 소비기한 is that, and replaced 유통기한 on Korean "
                   "labels in 2023."],
        ),
        "영수증": dict(
            hanja="領收證", meaning="a receipt",
            characters=[("領", "령", "to receive — as in 수령, 대통령"),
                        ("收", "수", "to collect — as in 수입, 압수")],
        ),
        "금액": dict(hanja="金額", meaning="a sum of money"),
        "지불": dict(
            hanja="支拂", meaning="payment",
            characters=[("支", "지", "to pay out — as in 지원, 지출"),
                        ("拂", "불", "to pay — the same 拂 as in 환불")],
        ),
        "설명서": dict(hanja="說明書", meaning="an instruction manual"),
        "주의 사항": dict(
            hanja="注意事項", meaning="points to note, cautions",
            characters=[("項", "항", "item — as in 조항, 항목")],
        ),
        "소비": dict(hanja="消費", meaning="consumption"),
        "지식": dict(
            hanja="知識", meaning="knowledge",
            characters=[("知", "지", "to know — as in 지혜, 인지"),
                        ("識", "식", "to recognise — as in 의식, 상식")],
        ),
        "절약": dict(
            hanja="節約", meaning="thrift, sparing",
            characters=[("節", "절", "to moderate, a season — as in 명절, 절기"),
                        ("約", "약", "promise, to economise — as in 약속")],
        ),
        "현명": dict(
            hanja="賢明", meaning="being wise",
            characters=[("賢", "현", "wise, virtuous"),
                        ("明", "명", "bright, clear — as in 설명, 투명")],
        ),
        "다누리콜센터": dict(
            meaning="the Danuri call centre",
            notes=["1577-1366, the multilingual line for migrants and "
                   "multicultural families, staffed in thirteen languages."],
        ),
        "꼼꼼하다": dict(meaning="to be meticulous, thorough"),
        "판매자": dict(hanja="販賣者", meaning="a seller"),
        "지다": dict(
            meaning="to bear (a responsibility); to lose; to set",
            notes=["책임을 지다 “to bear responsibility”."],
        ),
    },

    extraNotes=[
        "Chapter 27 has no Google Doc: the Korean is my reading of the photos "
        "of pp. 144-147, so it is worth checking against the pages.",
        "Two figures on p. 145 are not reproduced: the 모바일쇼핑 거래액 graphic, "
        "whose two totals are in its caption instead, and the "
        "오프라인·온라인 쇼핑 현황 line chart, whose series are too small to read "
        "off the photograph.",
        "The three consumer-protection arrangements of 이야기 나누기 are printed "
        "as a table with the names as its header, which is how they are set "
        "here.",
        "The review gaps on p. 147 are blank in the book and left blank here.",
    ],
)
