# -*- coding: utf-8 -*-
"""Chapter 34 — Property and the law.

Transcribed from the photos of pp. 178-181. Your English glosses on pp. 178,
179 and 180 are carried as the entries for the words they sit over.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, TABLE,
               CELL, GLOSSARY)

CHAPTER = dict(
    number=34, slug="34-property-and-law",
    unit="법", title="재산과 법", titleEn="Property and the law",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 돈 {거래}를 할 때 나타날 수 있는 상황입니다.",
                  "Below is a situation that can arise when money changes "
                  "hands."),
        FIGURE("친한 친구가 급하게 돈을 빌려 달라고 하는 그림"),
        SOURCE("▲ 친한 친구가 급하게 돈을 빌려 달라고 합니다. 친한 친구지만 돈 거래를 하는 것이 "
               "부담스럽기도 합니다."),
        HEADING(4, "01 그림과 같은 일을 직접 경험하거나 주변에서 본 적이 있습니까? 이런 부탁을 받는다면 "
                   "어떤 점을 주의해야 합니까?",
                translation="Have you been through something like the picture "
                            "yourself, or seen it happen around you? If you "
                            "were asked this, what would you have to be "
                            "careful about?"),
        HEADING(4, "02 자신의 고향나라에서는 다른 사람과 돈을 주고받은 사실을 증명하기 위해 어떤 방법을 "
                   "사용하나요?",
                translation="In your home country, what is used to prove that "
                            "money has passed between people?"),

        SECTION("goals", "학습목표"),
        BULLET("{금전} 거래와 관련된 법적 내용을 설명할 수 있다.", ordered=True,
               translation="Explain the law to do with lending and borrowing "
                           "money."),
        BULLET("{부동산} 거래와 관련된 법적 내용을 설명할 수 있다.", ordered=True,
               translation="Explain the law to do with dealing in property."),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"],
              [["심화", "법", "18. 재산 문제와 법",
                "죽음과 유언, 상속, 법을 통한 금전 분쟁 해결, 내용증명"]]),

        SECTION("part", "01 금전 거래를 할 때 무엇을 알아 두어야 할까?"),
        GLOSSARY(("계약", "두 명 이상의 사람이 말이나 글로 일정한 약속을 하는 것", "계약",
                  "a contract"),
                 ("의사", "무엇을 하고자 하는 생각이나 뜻", "의사", "intention, intent"),
                 ("무효", "법률 행위의 효과가 생기지 않는 것", "무효", "invalid, null")),
        HEADING(2, "계약의 의미", translation=
                "What a contract means" "\n\n"
                "금전 means money. A money transaction means people lending "
                "and borrowing money between them. When money changes hands "
                "a contract is generally made." "\n\n"
                "A contract must be entered into according to the free "
                "intention of those making it. A contract may also be void "
                "where what it contains runs against public order. That is, "
                "a contract that would violate an individual’s rights or "
                "amount to a crime is not allowed."),
        PARAGRAPH("{금전}은 돈을 가리킨다. {금전 거래}란 사람들끼리 돈을 빌리고 빌려주는 것을 가리킨다. "
                  "금전 거래를 할 때는 일반적으로 {계약}을 하게 된다."),
        PARAGRAPH("계약은 사람들의 자유로운 {의사}에 따라 {맺어야|맺다} 한다. 또한 계약 내용이 "
                  "{사회질서}에 {어긋나는|어긋나다} 내용이면 {무효}가 될 수 있다. 즉, 개인의 권리를 "
                  "{침해하거나|침해하다} {범죄}가 될 수 있는 계약은 {허용되지|허용되다} 않는다."),
        FIGURE("계약은 두 사람의 의사가 일치하면 바로 성립한다."),

        GLOSSARY(("계약서", "계약이 성립되었음을 증명하기 위해 작성하는 서류", "계약서",
                  "a written contract"),
                 ("차용증", "남의 돈이나 물건을 빌린 것을 증명하는 문서", "차용증",
                  "a promissory note (IOU)"),
                 ("영수증", "돈이나 물품 등을 받았음을 증명하는 문서", "영수증", "a receipt"),
                 ("배상", "손해를 물어줌", "배상", "compensation")),
        HEADING(2, "금전 거래를 증명하는 서류", translation=
                "The papers that prove a money transaction" "\n\n"
                "A contract can be made by word of mouth between the parties, "
                "but it can become hard to prove what was agreed if trouble "
                "arises later. So when money changes hands, one’s rights are "
                "protected by drawing up a written contract that confirms the "
                "terms and having each party sign it or press their seal on "
                "it." "\n\n"
                "When one has lent money, it is well to take a promissory "
                "note from the borrower as evidence. And when repaying "
                "borrowed money one should take a receipt proving that the "
                "money has been repaid. A promissory note or a receipt should "
                "include the names, addresses and contact details of those "
                "involved, the amount (the principal and the interest), the "
                "date and their signatures." "\n\n"
                "If the borrower does not repay by the time they promised, "
                "the lender asks them directly to repay. If they still do "
                "not, the lender can seek the help of a court or another such "
                "body and be compensated for the loss suffered."),
        PARAGRAPH("계약은 {당사자}의 말을 통해서도 이루어질 수 있지만 나중에 혹시 문제가 생겼을 때 계약 "
                  "내용을 {증명하기|증명하다}가 어려워질 수 있다. 그러므로 금전 거래를 할 때는 계약 내용을 "
                  "확인해 주는 {계약서}를 {작성하고|작성하다} 각자 {서명}을 하거나 {도장}을 찍어야 권리를 "
                  "보호받을 수 있다."),
        PARAGRAPH("돈을 빌려주었을 때는 돈을 빌려준 사람에게 {증거}로 {차용증}을 받는 것이 좋다. 또한 빌린 "
                  "돈을 {갚을|갚다} 때는 돈을 갚은 내용을 증명해 주는 {영수증}을 받아야 한다. 차용증이나 "
                  "영수증에는 돈을 거래한 사람의 이름, 주소, {연락처}, 거래한 {금액}({원금}, {이자}), "
                  "거래한 날짜, 서명 등이 포함되어야 한다."),
        PARAGRAPH("만약 돈을 빌려간 사람이 돈을 갚기로 약속한 {시점}까지 돈을 갚지 않을 경우 돈을 빌려준 "
                  "사람은 돈을 갚으라고 직접 요청한다. 그래도 돈을 갚지 않는다면 법원 등 관련 기관의 도움을 "
                  "받아 자신의 입은 {손해}를 {배상}받을 수 있다."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "이자를 무조건 많이 받을 수는 없어요", translation=
                "There is a limit to the interest that may be charged" "\n\n"
                "Someone who needs money urgently may want to borrow even at "
                "high interest. In Korea, though, the law sets a limit so "
                "that a lender may not charge more than 24% interest a year. "
                "A bank or a moneylender — a company that lends money — that "
                "charges more than 24% a year is regarded as acting "
                "unlawfully and can be punished under the law. The same "
                "applies to money lent between individuals where the sum is "
                "100,000 won or more."),
        PARAGRAPH("누군가 돈이 급하게 필요하다면 높은 이자를 내고서라도 돈을 빌리고 싶어 한다. 그런데 "
                  "한국에서는 돈을 빌려주는 사람이 {지나치게|지나치다} 높은 이자를 받지 못하도록 법으로 정해 "
                  "두고 있다. 은행이나 {대부업체}(돈을 빌려주는 기업)가 돈을 빌려줄 때 1년에 24%를 넘는 "
                  "이자를 받으면 {불법}으로 {간주되어|간주되다} 법에 따라 처벌을 받을 수 있다. 개인 간에 "
                  "10만원 이상의 돈을 거래할 때도 마찬가지다."),
        FIGURE("‘24% 넘는 이자? 불법입니다’ 안내 포스터"),

        SECTION("part", "02 부동산 거래를 할 때 무엇을 알아 두어야 할까?"),
        GLOSSARY(("등기부 등본", "부동산에 관한 권리 관계를 적어둔 증명서", "등기부 등본",
                  "a certified copy of the register")),
        HEADING(2, "부동산과 등기부 등본", translation=
                "Property and the certified copy of the register" "\n\n"
                "부동산 means property that cannot be carried about — a home, "
                "land, a building. The first thing to do in dealing in "
                "property is to check the certified copy of the register. It "
                "records who holds the rights over the land or the building "
                "being dealt in, and how it has been dealt in until now. From "
                "it one can learn, for instance, who the actual owner is and "
                "how much is owed to a bank. The certified copy can also be "
                "checked on the court’s internet registry site."),
        PARAGRAPH("{부동산}이란 집이나 땅, 건물 등 직접 가지고 다닐 수 없는 재산을 말한다. 부동산을 거래할 "
                  "때 가장 {우선적}으로 할 일은 {등기부 등본}을 확인하는 일이다. 등기부 등본에는 거래하는 "
                  "{토지}나 건물에 대한 권리가 누구에게 있는지, 그동안 어떻게 거래되어 왔는지 등이 "
                  "{기록되어|기록되다} 있다. 예를 들어 실제 {소유자}가 누구인지, 은행에 {빚}이 얼마나 "
                  "있는지 등을 등기부 등본을 통해 알 수 있다. 등기부 등본은 법원의 인터넷 {등기소} "
                  "사이트에서도 확인할 수 있다."),

        GLOSSARY(("부동산 소유권 이전 등기", "부동산을 소유한 사람이 바뀌었다는 것을 등기소에 신고하는 것",
                  "부동산 소유권 이전 등기"),
                 ("전입신고",
                  "거주지를 옮기는 경우 새로운 거주지의 행정복지센터에 그 사실을 신고하는 일. 전입한 날부터 "
                  "14일 이내에 해야 함", "전입신고"),
                 ("확정일자", "집을 계약한 날짜에 대해 법원이나 행정복지센터 등이 사실임을 증명해 준 날짜",
                  "확정일자"),
                 ("경매", "물건을 사려는 사람이 여럿일 때 값을 가장 높이 부르는 사람에게 파는 일", "경매")),
        HEADING(2, "부동산 거래 과정", translation=
                "How a property transaction goes" "\n\n"
                "In buying and selling property, a deposit of about 10% of "
                "the price is generally handed over first. The money paid in "
                "between is called the 중도금, and the last payment the 잔금. "
                "Before paying the balance one should check the certified "
                "copy of the register from time to time to make sure there "
                "has been no change in the important rights, and once the "
                "balance is paid the transfer of ownership must be "
                "registered." "\n\n"
                "It is also possible to borrow someone else’s property "
                "rather than own it. Letting property out is called 임대, and "
                "renting it 임차. In renting a flat or a shop unit, 전세 or "
                "monthly rent are the arrangements mostly used." "\n\n"
                "In Korea the person renting property — the tenant — is "
                "regarded as the weaker party and specially protected by "
                "law. For a tenant to have that protection in full they must "
                "register their move in and obtain a fixed date. In that "
                "case the tenant can live there for at least two years "
                "whether or not the owner changes. And even if the home they "
                "were living in comes to be sold at auction, they can have "
                "the deposit they left returned to them ahead of others."),
        PARAGRAPH("부동산을 사고팔 때는 일반적으로 거래 가격의 10% 정도의 {계약금}을 먼저 주고받는다. "
                  "계약금에 이어 중간에 내는 돈을 {중도금}, 마지막에 내는 돈을 {잔금}이라고 한다. 잔금을 "
                  "내기 전에도 {틈틈이} 등기부 등본을 통해 중요한 권리에 {변동}이 없는지 확인하고, 잔금을 "
                  "{치른|치르다} 이후에는 {부동산 소유권 이전 등기}를 해야 한다."),
        PARAGRAPH("부동산을 {소유하지|소유하다} 않고 다른 사람의 부동산을 빌려 쓰는 것도 가능하다. 이때 "
                  "부동산을 빌려주는 것을 {임대}, 빌려 쓰는 것을 {임차}라고 한다. 아파트나 {상가}를 빌려 "
                  "쓸 때는 주로 {전세}나 {월세} 방식을 많이 사용한다."),
        PARAGRAPH("한국에서는 부동산을 빌려 쓰는 사람({임차인})을 {약자}로 간주하여 법으로 특별히 보호한다. "
                  "이때 임차인이 법적 보호를 {충분히} 받기 위해서는 반드시 {전입신고}를 하고 {확정일자}를 "
                  "받아야 한다. 이 경우 임차인은 {집주인}이 바뀌는 것과 상관없이 최소한 2년 동안 거주할 수 "
                  "있다. 또한 거주하던 집이 {경매} 등으로 팔리는 경우가 생기더라도 원래 {맡겼던|맡기다} "
                  "{보증금}을 다른 사람보다 먼저 {돌려받을|돌려받다} 수 있다."),
        FIGURE("‘부동산 전자계약은 이렇게!’ 안내 그림"),
        SOURCE("▲ 2017년부터 부동산 거래에서 온라인 계약서 작성이 가능하다."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "부동산 거래를 도와주는 전문가: 공인중개사(부동산 중개업자)", translation=
                "The expert who helps with property transactions: the "
                "licensed estate agent" "\n\n"
                "In making a property contract one can deal more easily and "
                "safely through a licensed estate agent. A commission is then "
                "paid to the agent according to the value of the transaction "
                "— money paid for having handled the business between the two "
                "sides. For a purchase of under 900 million won, or a tenancy "
                "(전세 or monthly rent) of under 600 million won, the "
                "commission is between 0.3% and 0.6%. Above those amounts it "
                "can be settled by agreement, within 0.9% of the value for a "
                "purchase and within 0.8% for a tenancy."),
        PARAGRAPH("부동산 관련 계약을 할 때는 {공인중개사}를 통해 보다 쉽고 안전하게 거래할 수 있다. 이때 "
                  "거래 금액에 따라 공인중개사에게 {중개수수료}(양쪽의 중간에서 일을 맡아 처리해 준 대가로 "
                  "주는 돈)를 낸다. 부동산 {매매}(사고파는 것)의 경우 9억원 미만, {임대차}(전세나 월세)의 "
                  "경우 6억원 미만인 경우는 0.3~0.6% 사이에서 중개수수료를 낸다. 거래 금액이 그 이상일 "
                  "때는 매매의 경우 거래금액의 0.9%, 임대차의 경우 거래금액의 0.8% 내에서 {협의}를 통해 "
                  "정할 수 있다."),
        FIGURE("공인중개사 자격증"),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 금전 거래를 할 때 무엇을 알아 두어야 할까?"),
        BULLET("사람과 사람 사이에서 거래를 할 때 맺는 약속을 계약이라고 하는데, 이 내용이 사회질서에 "
               "어긋나는 내용이면 (        )가 될 수 있다."),
        BULLET("금전 거래를 할 때는 계약 내용을 확인해 주는 (        )를 작성해야 권리를 보호받을 수 "
               "있다."),
        BULLET("돈을 빌려주었을 때는 (        ), 빌린 돈을 갚을 때는 (        )을 받아 놓아야 한다."),
        HEADING(3, "02 부동산 거래를 할 때 무엇을 알아 두어야 할까?"),
        BULLET("집이나 땅, 건물 등 직접 가지고 다닐 수 없는 재산을 (        )이라고 하며, 이것을 "
               "거래할 때는 반드시 (            )을 확인해야 한다."),
        BULLET("부동산 계약을 할 때는 일반적으로 거래 가격의 10% 내외에서 (        )을 먼저 주고받으며, "
               "이후 중도금과 잔금을 모두 지급하면 부동산 거래가 마무리된다."),
        BULLET("다른 사람이 소유한 부동산을 빌려 쓰는 것을 (        )라고 하며, 한국에서는 부동산을 빌려 "
               "쓰는 사람들을 법을 통해 특별히 보호하고 있다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "해외로 보낼 수 있는 돈에는 한도가 있어요", translation=
                "There is a limit on the money that can be sent abroad" "\n\n"
                "Even for money one has earned oneself in Korea, there is a "
                "limit on the amount when sending it abroad. With the 2019 "
                "amendment of the Foreign Exchange Transactions Act, the "
                "amount that can now be sent abroad without proving the "
                "reason for the transaction is, in US dollars, up to 5,000 "
                "dollars per remittance and 50,000 dollars a year. With the "
                "amendment, in particular, sending money abroad became "
                "possible not only through the commercial banks, card "
                "companies and savings banks but through internet banks and "
                "authorised apps. So that foreign workers in farming and "
                "fishing areas and multicultural families can deal in foreign "
                "currency conveniently, the post office also carries out "
                "overseas remittance for foreigners." "\n\n"
                "A fee has to be paid on sending money abroad, of the order "
                "of 5,000 to 10,000 won depending on the bank, and internet "
                "banks tend to charge less than the commercial banks. Older "
                "people and foreigners are often given favourable terms, so "
                "it is worth looking into it before sending."),
        PARAGRAPH("한국 내에서 본인이 번 돈이라고 하더라도 해외로 {송금할|송금하다} 때는 금액에 {한도}가 "
                  "있다. 2019년 {외국환거래법} {개정}으로 현재 거래 {사유}를 증명하지 않고도 해외로 보낼 수 "
                  "있는 금액은 미국 달러 기준으로 송금 건당 5천 달러, 연간 5만 달러 이내이다. 특히 "
                  "{법개정}과 함께 {시중은행}, 카드사, {저축은행}은 물론이고 인터넷 은행이나 {공인된|공인} "
                  "앱 등을 통해서도 해외 송금이 가능하다. {농어촌} 외국인 근로자, 다문화 가정 등이 편리하게 "
                  "{외환} 거래를 할 수 있도록 {우체국}에서도 외국인을 대상으로 해외 송금 {업무}를 실시하고 "
                  "있다."),
        PARAGRAPH("해외 송금을 할 때는 {수수료}를 내야 하는데 은행에 따라 대략 5천 원~1만 원 정도 선이며 "
                  "인터넷 은행 등은 시중은행보다 수수료가 낮은 편이다. 노인이나 외국인 등을 "
                  "{우대하는|우대하다} 경우도 많으니 미리 알아보고 송금하는 것이 좋다."),
        FIGURE("‘우체국 해외송금’ 안내 포스터"),
        PARAGRAPH("★ 자신의 고향 나라에 송금할 때 주로 사용하는 방법은 무엇이며, 어떤 점이 편리하고 "
                  "불편한지 말해 봅시다.",
                  "What do you mostly use to send money to your home country, "
                  "and what is convenient or inconvenient about it?"),
    ],

    extraAnnotations={
        "거래": dict(
            hanja="去來", meaning="a transaction, dealing",
            characters=[("去", "거", "to go — as in 과거, 퇴거"),
                        ("來", "래", "to come — as in 미래, 내년")],
        ),
        "금전": dict(
            hanja="金錢", meaning="money",
            characters=[("金", "금", "gold, money — as in 금액, 벌금"),
                        ("錢", "전", "a coin, money — as in 소전, 동전")],
        ),
        "금전 거래": dict(
            hanja="金錢去來", meaning="lending and borrowing money",
        ),
        "부동산": dict(
            hanja="不動産", meaning="property, real estate",
            characters=[("不動", None, "immovable — 不 not, 動 to move"),
                        ("産", "산", "property — as in 재산, 생산")],
            notes=["Chapter 5 has 부동산 as the estate agent’s office; here it "
                   "is the property itself."],
        ),
        "계약": dict(
            hanja="契約", meaning="a contract",
            characters=[("契", "계", "a bond, a pledge"),
                        ("約", "약", "a promise — as in 약속, 협약")],
        ),
        "의사": dict(
            hanja="意思", meaning="intention, what one means to do",
            characters=[("意", "의", "intention — as in 의견, 합의"),
                        ("思", "사", "to think — as in 사상, 사고")],
            notes=["Not the 의사 “doctor”, which is 醫師."],
        ),
        "맺다": dict(
            meaning="to tie, to enter into (a contract, a relationship)",
            surfaces=["맺어야"],
        ),
        "사회질서": dict(
            hanja="社會秩序", meaning="social order, public order",
            characters=[("社會", None, "society"),
                        ("秩序", None, "order — chapter 30’s 질서")],
        ),
        "어긋나다": dict(
            meaning="to run counter to, to go against",
            surfaces=["어긋나는"],
        ),
        "무효": dict(
            hanja="無效", meaning="void, of no effect",
            characters=[("無", "무", "without — as in 무국적, 무료"),
                        ("效", "효", "effect — as in 유효 기간")],
        ),
        "침해하다": dict(
            hanja="侵害하다", meaning="to violate, to infringe",
            characters=[("侵", "침", "to invade — as in 침입, 침략"),
                        ("害", "해", "harm — as in 피해, 해치다")],
            surfaces=["침해하거나"],
        ),
        "범죄": dict(
            hanja="犯罪", meaning="a crime",
            characters=[("犯", "범", "to violate — as in 범인, 범칙금"),
                        ("罪", "죄", "guilt — as in 유죄, 무죄")],
            notes=["Chapter 36’s subject: crime and the law."],
        ),
        "허용되다": dict(
            hanja="許容되다", meaning="to be allowed, permitted",
            characters=[("許", "허", "to allow — as in 허가, 허락"),
                        ("容", "용", "to accept — as in 수용, 내용")],
            surfaces=["허용되지"],
        ),
        "당사자": dict(
            hanja="當事者", meaning="the party concerned, the person involved",
            characters=[("當", "당", "the said, due — as in 당연, 해당"),
                        ("事", "사", "a matter — as in 사건, 사업"),
                        ("者", "자", "person")],
            notes=["Chapter 21’s 청문회 hears the 당사자, the person directly "
                   "concerned."],
        ),
        "증명하다": dict(
            hanja="證明하다", meaning="to prove, to certify",
            characters=[("證", "증", "evidence — as in 증거, 영수증"),
                        ("明", "명", "clear — as in 분명, 설명")],
            surfaces=["증명하기"],
        ),
        "계약서": dict(
            hanja="契約書", meaning="a written contract",
            characters=[("契約", None, "a contract"),
                        ("書", "서", "a document — as in 증명서, 서명")],
        ),
        "작성하다": dict(
            hanja="作成하다", meaning="to draw up, to write out",
            characters=[("作", "작", "to make — as in 제작, 작업"),
                        ("成", "성", "to complete — as in 완성, 구성")],
            surfaces=["작성하고"],
        ),
        "서명": dict(
            hanja="署名", meaning="a signature",
            characters=[("署", "서", "to sign, an office — as in 경찰서, 부서"),
                        ("名", "명", "a name — as in 성명, 유명")],
        ),
        "도장": dict(
            hanja="圖章", meaning="a seal, a stamp",
            characters=[("圖", "도", "a drawing, a plan — as in 지도, 도서"),
                        ("章", "장", "a chapter, a badge — as in 훈장, 문장")],
            notes=["Pressing one’s 도장 does the work a signature does."],
        ),
        "증거": dict(
            hanja="證據", meaning="evidence",
            characters=[("證", "증", "evidence — the same 證 as in 증명"),
                        ("據", "거", "to rely on — as in 근거, 의거")],
        ),
        "차용증": dict(
            hanja="借用證", meaning="a promissory note, an IOU",
            characters=[("借", "차", "to borrow — as in 임차, 차용"),
                        ("用", "용", "to use — as in 사용, 이용"),
                        ("證", "증", "certificate")],
        ),
        "갚다": dict(meaning="to repay, to pay back", surfaces=["갚을"]),
        "영수증": dict(
            hanja="領收證", meaning="a receipt",
            characters=[("領", "령", "to receive, to lead — as in 대통령, 영토"),
                        ("收", "수", "to collect — as in 수입, 수거"),
                        ("證", "증", "certificate")],
        ),
        "연락처": dict(
            hanja="連絡處", meaning="contact details",
            characters=[("連絡", None, "contact, getting in touch"),
                        ("處", "처", "a place — as in 처소, 부처")],
        ),
        "금액": dict(
            hanja="金額", meaning="an amount of money",
            characters=[("金", "금", "money — as in 금전, 벌금"),
                        ("額", "액", "a sum, a forehead — as in 예금액, 총액")],
        ),
        "원금": dict(
            hanja="元金", meaning="the principal (the sum originally lent)",
            characters=[("元", "원", "origin, principal — as in 원래, 원인"),
                        ("金", "금", "money")],
        ),
        "이자": dict(
            hanja="利子", meaning="interest",
            characters=[("利", "리", "benefit, gain — as in 이익, 권리"),
                        ("子", "자", "a child, a small thing — as in 자녀")],
            notes=["Chapter 28 has 이자 on savings; here it is interest on a "
                   "loan, capped at 24% a year."],
        ),
        "시점": dict(
            hanja="時點", meaning="a point in time",
            characters=[("時", "시", "time — as in 시간, 시대"),
                        ("點", "점", "a point — as in 지점, 관점")],
        ),
        "손해": dict(
            hanja="損害", meaning="loss, damage",
            characters=[("損", "손", "to lose — as in 손실, 손상"),
                        ("害", "해", "harm — as in 피해, 침해")],
        ),
        "배상": dict(
            hanja="賠償", meaning="compensation, making good a loss",
            characters=[("賠", "배", "to compensate, to pay for"),
                        ("償", "상", "to compensate — as in 보상, 배상")],
            notes=["배상 is making good a loss one caused; 보상 is compensation "
                   "more broadly — chapter 7’s 산업재해보상보험."],
        ),
        "지나치다": dict(
            meaning="to be excessive, to go too far",
            surfaces=["지나치게"],
        ),
        "대부업체": dict(
            hanja="貸付業體", meaning="a moneylender, a lending company",
            characters=[("貸付", None, "lending — 貸 to lend, 付 to give"),
                        ("業體", None, "a business, a firm — as in 산업체")],
        ),
        "불법": dict(
            hanja="不法", meaning="unlawful, illegal",
            characters=[("不", "불", "not — as in 부당, 부정"),
                        ("法", "법", "law")],
        ),
        "간주되다": dict(
            hanja="看做되다", meaning="to be regarded as, to be deemed",
            characters=[("看", "간", "to look at — as in 간호사"),
                        ("做", "주", "to make, to do")],
            surfaces=["간주되어"],
        ),
        "등기부 등본": dict(
            hanja="登記簿謄本", meaning="a certified copy of the property register",
            characters=[("登記", None, "registration — 登 to record, 記 to write"),
                        ("簿", "부", "a ledger — as in 가족관계등록부"),
                        ("謄本", None, "a certified copy — 謄 to transcribe, "
                                       "本 the original")],
        ),
        "우선적": dict(
            hanja="優先的", meaning="taking priority, first of all",
            characters=[("優先", None, "priority — 優 superior, 先 first")],
        ),
        "토지": dict(
            hanja="土地", meaning="land",
            characters=[("土", "토", "earth, soil — as in 국토, 토양"),
                        ("地", "지", "ground, place — as in 지역, 체류지")],
        ),
        "기록되다": dict(
            hanja="記錄되다", meaning="to be recorded",
            characters=[("記", "기", "to write down — as in 기사, 일기"),
                        ("錄", "록", "to record — as in 등록, 목록")],
            surfaces=["기록되어"],
        ),
        "소유자": dict(
            hanja="所有者", meaning="the owner",
            characters=[("所有", None, "ownership — 所 place, 有 to have"),
                        ("者", "자", "person")],
        ),
        "빚": dict(meaning="a debt"),
        "등기소": dict(
            hanja="登記所", meaning="the registry office",
            characters=[("登記", None, "registration"),
                        ("所", "소", "a place — as in 사무소, 주소")],
        ),
        "계약금": dict(
            hanja="契約金", meaning="the deposit paid on signing",
            notes=["About 10% of the price in a property deal."],
        ),
        "중도금": dict(
            hanja="中途金", meaning="the interim payment",
            characters=[("中途", None, "midway — 中 middle, 途 road")],
        ),
        "잔금": dict(
            hanja="殘金", meaning="the balance, the final payment",
            characters=[("殘", "잔", "remaining — as in 잔여"),
                        ("金", "금", "money")],
        ),
        "틈틈이": dict(meaning="in spare moments, from time to time"),
        "변동": dict(
            hanja="變動", meaning="a change, a fluctuation",
            characters=[("變", "변", "to change — as in 변화, 변경"),
                        ("動", "동", "to move — as in 이동, 활동")],
        ),
        "치르다": dict(
            meaning="to pay (a sum), to go through (an event)",
            surfaces=["치른"],
        ),
        "부동산 소유권 이전 등기": dict(
            hanja="不動産所有權移轉登記",
            meaning="registration of the transfer of ownership",
            characters=[("所有權", None, "ownership"),
                        ("移轉", None, "transfer — 移 to move, 轉 to turn")],
        ),
        "소유하다": dict(
            hanja="所有하다", meaning="to own",
            surfaces=["소유하지"],
        ),
        "임대": dict(
            hanja="賃貸", meaning="letting out, leasing (to someone)",
            characters=[("賃", "임", "to hire, rent — as in 임금, 임차"),
                        ("貸", "대", "to lend — as in 대여, 대출")],
            notes=["Chapter 5 has 공공 임대 주택, housing let by the state."],
        ),
        "임차": dict(
            hanja="賃借", meaning="renting, taking on lease",
            characters=[("賃", "임", "to hire, rent"),
                        ("借", "차", "to borrow — as in 차용증")],
        ),
        "상가": dict(
            hanja="商街", meaning="a shop unit, a parade of shops",
            characters=[("商", "상", "commerce — as in 상품, 상인"),
                        ("街", "가", "a street — as in 시가지")],
        ),
        "전세": dict(
            hanja="傳貰", meaning="jeonse, a large deposit in place of rent",
            notes=["Chapter 5 explains it: a sum left with the landlord and "
                   "returned at the end of the term, mostly Korean."],
        ),
        "월세": dict(
            hanja="月貰", meaning="monthly rent",
            characters=[("月", "월", "month — as in 월급, 월별"),
                        ("貰", "세", "rent — chapter 5’s 세")],
        ),
        "임차인": dict(
            hanja="賃借人", meaning="the tenant",
            characters=[("賃借", None, "renting"),
                        ("人", "인", "person")],
        ),
        "약자": dict(
            hanja="弱者", meaning="the weaker party",
            characters=[("弱", "약", "weak — as in 약점, 허약"),
                        ("者", "자", "person")],
        ),
        "충분히": dict(
            hanja="充分히", meaning="fully, sufficiently",
            characters=[("充", "충", "to fill — as in 충족, 보충"),
                        ("分", "분", "a part — as in 부분, 분리")],
        ),
        "전입신고": dict(
            hanja="轉入申告", meaning="registering a move in",
            characters=[("轉入", None, "moving in — chapter 31’s 전입하다"),
                        ("申告", None, "a report to the authorities")],
            notes=["To be done within 14 days of moving in."],
        ),
        "확정일자": dict(
            hanja="確定日字", meaning="the fixed date (certified date of a lease)",
            characters=[("確定", None, "settled, confirmed — 確 certain, "
                                       "定 to fix"),
                        ("日字", None, "a date")],
            notes=["Chapter 5 says to get it at the community service centre "
                   "so the deposit can be recovered safely."],
        ),
        "집주인": dict(meaning="the landlord, the owner of the house"),
        "경매": dict(
            hanja="競賣", meaning="an auction",
            characters=[("競", "경", "to compete — as in 경쟁, 경기"),
                        ("賣", "매", "to sell — as in 매매, 판매")],
        ),
        "맡기다": dict(
            meaning="to leave (something) with someone, to entrust",
            surfaces=["맡겼던"],
        ),
        "보증금": dict(
            hanja="保證金", meaning="a deposit (security)",
            characters=[("保證", None, "a guarantee — 保 to protect, 證 evidence"),
                        ("金", "금", "money")],
        ),
        "돌려받다": dict(meaning="to get back, to have returned",
                       surfaces=["돌려받을"]),
        "공인중개사": dict(
            hanja="公認仲介士", meaning="a licensed estate agent",
            characters=[("公認", None, "officially recognised, licensed"),
                        ("仲介", None, "brokerage — chapter 5’s 중개"),
                        ("士", "사", "a qualified person — as in 변호사, 기사")],
        ),
        "중개수수료": dict(
            hanja="仲介手數料", meaning="the agent’s commission",
            characters=[("手數料", None, "a fee — 手 hand, 數 number, 料 charge")],
        ),
        "매매": dict(
            hanja="賣買", meaning="buying and selling, a sale",
            characters=[("賣", "매", "to sell — as in 판매, 경매"),
                        ("買", "매", "to buy — as in 구매")],
        ),
        "임대차": dict(
            hanja="賃貸借", meaning="a tenancy (letting and renting)",
            notes=["The two sides together: 임대 by the owner, 임차 by the "
                   "tenant."],
        ),
        "협의": dict(
            hanja="協議", meaning="consultation, settling by agreement",
            characters=[("協", "협", "to co-operate — as in 협력, 협정"),
                        ("議", "의", "to deliberate — as in 회의, 논의")],
        ),
        "송금하다": dict(
            hanja="送金하다", meaning="to remit, to send money",
            characters=[("送", "송", "to send — as in 송달, 방송"),
                        ("金", "금", "money")],
            surfaces=["송금할"],
        ),
        "한도": dict(
            hanja="限度", meaning="a limit, a ceiling",
            characters=[("限", "한", "a limit — as in 제한, 기한"),
                        ("度", "도", "a degree — as in 제도, 정도")],
        ),
        "외국환거래법": dict(
            hanja="外國換去來法",
            meaning="the Foreign Exchange Transactions Act",
            characters=[("外國換", None, "foreign exchange"),
                        ("去來", None, "transactions")],
        ),
        "개정": dict(
            hanja="改正", meaning="amendment (of a law)",
            characters=[("改", "개", "to change — as in 개선, 개혁"),
                        ("正", "정", "right, correct")],
        ),
        "사유": dict(
            hanja="事由", meaning="a reason, grounds",
            characters=[("事", "사", "a matter — as in 사건, 당사자"),
                        ("由", "유", "a cause — as in 이유, 자유")],
        ),
        "법개정": dict(hanja="法改正", meaning="amendment of the law"),
        "시중은행": dict(
            hanja="市中銀行", meaning="a commercial bank",
            characters=[("市中", None, "in the market, on the high street")],
        ),
        "저축은행": dict(
            hanja="貯蓄銀行", meaning="a savings bank",
            characters=[("貯蓄", None, "saving — chapter 28")],
        ),
        "공인": dict(
            hanja="公認", meaning="official recognition, authorised",
            characters=[("公", "공", "public — as in 공공, 공기업"),
                        ("認", "인", "to recognise — as in 인정, 승인")],
            surfaces=["공인된"],
        ),
        "농어촌": dict(
            hanja="農漁村", meaning="farming and fishing villages",
            characters=[("農", "농", "farming — as in 농촌, 농민"),
                        ("漁", "어", "fishing — as in 어선, 어업"),
                        ("村", "촌", "a village — as in 촌수, 농촌")],
        ),
        "외환": dict(
            hanja="外換", meaning="foreign exchange",
            characters=[("外", "외", "outside, foreign — as in 외국, 해외"),
                        ("換", "환", "to exchange — as in 교환, 환불")],
        ),
        "우체국": dict(
            hanja="郵遞局", meaning="the post office",
            characters=[("郵", "우", "post, mail — as in 우편"),
                        ("遞", "체", "to deliver in turn"),
                        ("局", "국", "a bureau — as in 방송국, 약국")],
        ),
        "업무": dict(
            hanja="業務", meaning="work, business, duties",
            characters=[("業", "업", "business — as in 취업, 기업"),
                        ("務", "무", "duty — as in 의무, 공무원")],
        ),
        "수수료": dict(
            hanja="手數料", meaning="a fee, a charge",
        ),
        "우대하다": dict(
            hanja="優待하다", meaning="to give favourable terms to",
            characters=[("優", "우", "superior, preferential — as in 우선, 우수"),
                        ("待", "대", "to wait, to treat — as in 기대, 대우")],
            surfaces=["우대하는"],
        ),
    },

    extraNotes=[
        "The 생각해 봅시다 illustration on p. 178, the handshake photograph on "
        "p. 179, the interest poster on p. 179, the electronic-contract "
        "graphic on p. 180, the estate agent’s licence on p. 180 and the post "
        "office remittance poster on p. 181 are not reproduced; their "
        "captions are.",
        "The review gaps on p. 181 are blank in the book and left blank here.",
    ],
)
