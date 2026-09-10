# -*- coding: utf-8 -*-
"""Chapter 28 — Using a financial institution.

Transcribed from the photos of pp. 148-151.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, FIGURE, LABELS, VERSE,
               TABLE, CELL, GLOSSARY)

CHAPTER = dict(
    number=28, slug="28-banking",
    unit="경제", title="금융기관 이용하기",
    titleEn="Using a financial institution",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 {은행}에서 볼 수 있는 모습입니다."),
        LABELS("{예금}", "{대출}", "{송금}", "{환전}"),
        HEADING(4, "01 각각의 {장면}은 무엇을 하는 모습입니까? 이 중 자신이 한국에서 해 본 것은 "
                   "무엇입니까?"),
        HEADING(4, "02 자신의 고향 나라와 한국에서 은행 관련 일을 할 때의 {공통점}과 {차이점}은 "
                   "무엇입니까?"),

        SECTION("goals", "학습목표"),
        BULLET("{금융기관}의 종류와 특징을 설명할 수 있다.", ordered=True),
        BULLET("{금융 거래} 하는 방법을 알고 이를 활용할 수 있다.", ordered=True),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"],
              [["심화", "경제", "14. 금융과 자산관리", "금융기관 활용, 자산관리"]]),

        SECTION("part", "01 금융기관에는 어떤 것이 있을까?"),
        HEADING(2, "은행에서 하는 일"),
        GLOSSARY(("금융", "돈이 돌고 도는 것", "금융"),
                 ("공과금", "국가나 지방자치단체가 국민에게 내도록 하는 것으로 각종 세금, "
                            "전기요금, 수도요금 등이 있음", "공과금"),
                 ("납부", "공과금 등을 내는 것", "납부")),
        PARAGRAPH("한국의 은행에서는 사람들의 돈을 {맡아|맡다} 주거나 돈을 필요로 하는 사람 또는 "
                  "기업에게 {빌려주기|빌려주다}도 한다. 또한 다른 사람에게 돈을 보내 주기도 "
                  "하며, 한국 돈과 외국 돈을 서로 {바꿔|바꾸다} 주기도 한다. {공과금}, 아파트 "
                  "{관리비}, 대학 {등록금} 등도 은행을 통해 {납부}할 수 있고 신용카드, 체크카드 "
                  "등을 만드는 것도 가능하다. 은행 {업무} 시간은 일반적으로 {평일} 오전 9시부터 "
                  "오후 4시까지이다."),

        HEADING(2, "은행의 종류"),
        GLOSSARY(("금융기관", "개인이나 기업의 돈을 맡아 주고 다른 개인이나 기업에게 빌려주는 "
                              "일 등을 하는 기관", "금융기관"),
                 ("금리", "맡긴 돈이나 빌린 돈에 붙는 이자", "금리"),
                 ("수수료", "어떤 일을 맡아서 처리해 준 대가로 받는 요금", "수수료")),
        PARAGRAPH("한국에는 다양한 은행이 있다. 우선, 화폐를 발행하는 {한국은행}이 있다. 그리고 "
                  "사람들이 많이 이용하는 은행으로는 {시중은행}과 {지방은행}이 있다. 시중은행은 "
                  "개인이 돈을 맡기거나 {빌리는|빌리다} 대표적인 {금융기관}으로, 전국 곳곳에 "
                  "{지점}이 많이 설치되어 있어서 이용하기 편리하다. 신한은행, 국민은행, 하나은행, "
                  "우리은행, 기업은행, 농협은행 등이 여기에 해당한다."),
        PARAGRAPH("지방은행은 특히 지역 경제의 발전에 필요한 돈을 {공급}하는 것을 {주된|주되다} "
                  "목적으로 광역시나 도에 {설립}된 은행이다. 경남은행, 광주은행, 대구은행, "
                  "부산은행, 전북은행, 제주은행 등이 여기에 해당한다. 이 외에도 {단위농협}, "
                  "{우체국}, 새마을금고 등도 전국에 많은 지점이 있고 {안전성}이 높기 때문에 "
                  "{안심}하고 편리하게 이용할 수 있다. 지금까지 소개한 금융기관은 모두 {대체로} "
                  "안전성이 높은 {반면} {금리}는 낮은 편이다."),
        PARAGRAPH("시중은행, 지방은행, 농협 등이 제공하는 낮은 금리에 만족하지 못한다면 "
                  "{상호저축은행}을 이용할 수 있다. 상호저축은행은 시중은행 등에 비해 금리가 높은 "
                  "{장점}이 있지만, 대체로 규모가 작고 지점 수가 많지 않다."),
        PARAGRAPH("최근에는 지점을 따로 만들지 않고 온라인 네트워크를 통해 금융 서비스를 "
                  "제공하는 {인터넷 전문 은행}도 {등장}하였다. {케이뱅크}, {카카오뱅크} 등이 그 "
                  "예이다. 인터넷 전문 은행은 기존의 은행에 비해 사용 {절차}가 간단하고 "
                  "{수수료}가 낮으며 언제 어느 때나 이용할 수 있다는 점에서 인기가 높다."),
        FIGURE("한국은행"),
        FIGURE("인터넷 전문 은행 — 카카오뱅크와 케이뱅크"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "저축 상품에는 어떤 것이 있을까?", translation=
          "What kinds of savings account are there?" "\n\n"
          "To build up money, it matters to save part of one’s income each "
          "month. Among savings products there is the ordinary deposit "
          "account, which one can pay into and take out of freely; the "
          "fixed deposit, where a set sum is left for a set period; and the "
          "instalment savings account, where an amount to save over a set "
          "period is decided and paid in bit by bit. The ordinary deposit "
          "pays a far lower rate than the fixed deposit or instalment "
          "savings."),
        PARAGRAPH("돈을 모으기 위해서는 매달 {소득} 중 일부를 저축하는 것이 중요하다. 저축 "
                  "{상품}에는 {입금}, {출금}이 자유로운 {보통 예금}, 일정 금액을 일정 기간 동안 "
                  "맡겨 두는 {정기 예금}, 일정 기간 동안 저축할 금액을 정해 놓고 그만큼씩 내는 "
                  "{정기 적금} 등이 있다. 보통 예금은 정기 적금이나 정기 예금에 비해 금리가 매우 "
                  "낮다."),
        BULLET("[정기 예금의 예] 100만원을 일정 기간 동안 은행에 맡겨두는 것",
          translation="[Example of a fixed deposit] Leaving a million won "
                      "with the bank for a set period."),
        BULLET("[정기 적금의 예] 10만원씩 매달 같은 날에 저축하는 것",
          translation="[Example of instalment savings] Saving 100,000 won "
                      "on the same day every month."),
        FIGURE("저금통에 돈을 모으는 두 사람 — ‘적금’과 ‘예금’의 깃발"),

        SECTION("part", "02 금융 거래는 어떻게 하면 될까?"),
        HEADING(2, "은행 계좌 만들기"),
        GLOSSARY(("금융실명제", "가짜 이름이나 다른 사람이 아닌, 오직 본인의 이름으로만 금융 "
                                "거래를 할 수 있도록 한 제도", "금융실명제")),
        PARAGRAPH("은행 {계좌}를 만들기 위해서는 반드시 본인이 신분증을 가지고 직접 은행을 "
                  "{방문}해야 한다. 한국에서는 모든 금융 거래를 본인 자신의 이름으로만 하도록 "
                  "하는 {금융실명제}가 실시되고 있기 때문이다. 자신의 이름을 다른 사람에게 "
                  "빌려주거나 다른 사람의 이름을 빌려서 계좌를 만들면 처벌을 받게 된다."),
        PARAGRAPH("외국인이 은행에서 계좌를 만들 때도 신분증(여권, {외국인등록증}, "
                  "{외국국적동포} {국내 거소 신고증} 등)이 필요하며, 경우에 따라 {재직증명서}나 "
                  "{재학증명서} 등의 {서류}를 요청하기도 한다. 이때 {인터넷 뱅킹}, {현금 인출 "
                  "카드} 등도 함께 신청할 수 있다. 계좌 비밀번호와 현금 인출 카드 비밀번호는 "
                  "본인만 알 수 있는 번호로 {신중}하게 정해야 한다. 신용카드를 신청한 경우에는 "
                  "며칠 후에 집이나 직장으로 {배송}된다."),

        HEADING(2, "금융 거래 하기"),
        GLOSSARY(("거래", "돈이나 물건을 주고 받는 것", "거래"),
                 ("ATM(현금자동입출금기)", "현금을 넣고 뽑을 수 있는 기계", "ATM")),
        PARAGRAPH("은행에 계좌를 만든 후에는 {ATM}(현금자동입출금기), 인터넷 뱅킹, 스마트폰 "
                  "뱅킹 등 자신이 편리한 방법을 자유롭게 선택하여 {금융 거래}를 할 수 있다."),
        PARAGRAPH("ATM에서는 출금, 입금, {이체}(송금), {계좌조회} 등을 할 수 있다. 주의해야 할 "
                  "점은 자신의 계좌가 있는 은행이 아닌 ATM {기기}를 사용할 때나 은행업무시간 "
                  "외에 출금을 하거나 이체를 할 때 수수료가 붙는다는 점이다."),
        PARAGRAPH("인터넷 뱅킹이나 스마트폰 뱅킹은 컴퓨터나 스마트폰을 통해 어디에서든 자유롭게 "
                  "은행 관련 업무를 볼 수 있다. 이를 활용하려면 먼저 신분증을 가지고 은행에서 "
                  "{신청서}를 {작성}한 후 제출해야 한다. 그리고 안전한 이용을 위해 "
                  "{공동인증서}를 발급받고, {OTP}를 통해 {1회용} 비밀번호를 입력한다."),
        PARAGRAPH("한편, 입금과 출금을 알려주는 {문자} 서비스를 신청하면 자신의 {통장}에 돈이 "
                  "들어오고 나가는 것을 스마트폰을 통해 {곧바로} 확인할 수 있다. 만약 자신이 "
                  "모르는 돈이 들어오거나 {빠져나갔을|빠져나가다} 경우에는 반드시 은행이나 "
                  "경찰서에 신고해야 한다."),
        FIGURE("ATM(현금자동입출금기)을 이용하는 모습"),
        FIGURE("OTP (토큰형, 카드형)"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "예금자 보호 제도란 무엇일까?", translation=
          "What is deposit protection?" "\n\n"
          "Korea operates a ‘deposit protection scheme’ so that people can "
          "save with confidence. Under it, the principal — the money "
          "originally deposited — and the interest on it are protected "
          "together up to 50 million won per person at each financial "
          "institution. So where a deposit comes to more than 50 million "
          "won, it is safer to divide it among several institutions."),
        PARAGRAPH("한국에서는 사람들이 안심하고 {예금}할 수 있도록 ‘{예금자 보호 제도}’를 "
                  "{시행}하고 있다. 이 제도에 {의해} {원금}(원래 맡긴 돈)과 {이자}(원금에 붙는 "
                  "돈)를 합쳐 금융기관별로 1인당 최고 5천만 원까지 보호 받을 수 있다. 그러므로 "
                  "{예금액}이 5천만 원을 넘을 경우에는 여러 금융기관에 나누어 맡기는 것이 더 "
                  "안전하다."),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 금융기관에는 어떤 것이 있을까?"),
        BULLET("한국의 은행 업무 시간은 일반적으로 평일 오전 (      )부터 오후 (      )까지이다."),
        BULLET("시중은행이나 지방은행은 대체로 안정성은 높은 반면 (        )가 낮은 편이다."),
        BULLET("최근에는 지점을 따로 만들지 않고 온라인 네트워크를 통해 금융서비스를 제공하는 "
               "(              )이 인기를 끌고 있다."),
        HEADING(3, "02 금융 거래는 어떻게 하면 될까?"),
        BULLET("은행 계좌를 만들기 위해서는 반드시 본인이 (          )을 가지고 직접 은행을 "
               "방문해야 한다."),
        BULLET("한국에서는 모든 금융 거래를 본인 자신의 이름으로만 하도록 하는 (            )가 "
               "실시되고 있다."),
        BULLET("인터넷 뱅킹이나 스마트폰 뱅킹은 (        )나 스마트폰을 통해 어디에서든 자유롭게 "
               "은행 관련 업무를 볼 수 있다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "인터넷과 스마트폰을 이용한 금융 사기를 조심해요!", translation=
          "Beware of financial fraud that uses the internet and the "
          "smartphone!" "\n\n"
          "Messenger phishing is a crime in which someone logs in secretly "
          "to a social media account such as KakaoTalk or Facebook and then "
          "sends messages to the friends and family registered there to take "
          "money from them. The method used is to say that someone is ill or "
          "has been in a traffic accident and money is urgently needed, and "
          "to ask for money to be sent, having it paid into another person’s "
          "account."),
        PARAGRAPH("{메신저 피싱}이란 카카오톡, 페이스북 등과 같은 {소셜 미디어}의 {계정}에 "
                  "{몰래} 로그인한 뒤 거기에 등록된 친구나 가족에게 메시지를 보내 돈을 "
                  "{빼가는|빼가다} 범죄이다. 누가 아프다거나 교통사고를 당해서 {급히} 돈이 "
                  "필요하니 돈을 보내 달라고 해서 다른 사람 계좌로 입금하도록 하는 {방식}을 "
                  "사용한다."),
        VERSE("[실제 사례] K씨는 스마트폰으로 메신저를 확인하던 중 친구로부터 “갑자기 아이가 많이 "
              "아파서 급하게 병원에 가야 하는 데 돈이 필요하니 100만 원을 빌려줘”라는 메시지를 "
              "받고 친구가 알려준 계좌번호로 100만 원을 송금했습니다.",
              "K씨는 나중에 친구에게 {안부} 전화를 하는 과정에서 메신저 피싱(Phishing)을 당했다는 "
              "사실을 {뒤늦게} 깨달았습니다.",
              translation=
              "[A real case] While checking his messenger app on his "
              "smartphone, K received a message from a friend saying “my "
              "child has suddenly become very ill and has to go to hospital "
              "urgently, I need money, so lend me a million won”, and "
              "transferred a million won to the account number the friend "
              "gave." "\n\n"
              "Only later, in the course of ringing the friend to ask how "
              "they were, did K realise that he had been the victim of "
              "messenger phishing."),
        PARAGRAPH("메신저 피싱을 {예방}하기 위해서는 다음을 반드시 지키도록 한다.",
          "To guard against messenger phishing, be sure to keep to the "
          "following."),
        BULLET("메신저로 돈을 {요구}하는 경우 반드시 전화를 걸어 본인인지 아닌지 확인해야 합니다.",
               ordered=True,
               translation="If money is asked for over a messenger app, "
                           "always ring and check whether it is really "
                           "that person."),
        BULLET("메신저를 통해서는 절대 개인 정보를 주고받아서는 안 됩니다.", ordered=True,
               translation="Never exchange personal information over a "
                           "messenger app."),
        BULLET("메신저 비밀번호를 자주 바꿔 줍니다.", ordered=True,
               translation="Change your messenger password often."),
        BULLET("메신저에 {출처}가 {분명}하지 않은 {첨부 파일}이나 링크가 있을 때는 클릭하지 "
               "않습니다.", ordered=True,
               translation="When there is an attachment or a link of "
                           "unclear origin in a message, do not click it."),
        BULLET("{공공장소}에 설치되어 있는 컴퓨터로는 금융 거래를 하지 않습니다.", ordered=True,
               translation="Do not carry out financial transactions on a "
                           "computer installed in a public place."),
        PARAGRAPH("★ 안전한 금융 거래를 위해 주의해야 할 점에 대해 이야기를 나눠 봅시다.",
          "Talk together about what to watch out for in order to bank "
          "safely."),
    ],

    english={
        "은행에서 하는 일": dict(
            title="What a bank does",
            paragraphs=[
                "A Korean bank will hold people's money for them, and lend to "
                "a person or a company that needs it. It will also send money "
                "to someone else, and exchange Korean money for foreign. "
                "Utility charges, apartment maintenance fees and university "
                "fees can be paid through a bank as well, and credit and debit "
                "cards obtained there. Banking hours are ordinarily nine in "
                "the morning to four in the afternoon on weekdays.",
            ],
        ),
        "은행의 종류": dict(
            title="Kinds of bank",
            paragraphs=[
                "Korea has banks of many kinds. First there is the Bank of "
                "Korea, which issues the currency. Then there are the "
                "commercial banks and the local banks, which people use most. "
                "A commercial bank is the typical institution for an "
                "individual to deposit with or borrow from, and convenient to "
                "use, with branches set up all over the country. Shinhan, "
                "KB Kookmin, Hana, Woori, IBK and NH Nonghyup are of this "
                "kind.",

                "A local bank is one established in a metropolitan city or a "
                "province with the chief purpose of supplying the money the "
                "local economy needs to develop. Kyongnam, Gwangju, Daegu, "
                "Busan, Jeonbuk and Jeju bank are of this kind. Besides "
                "these, the local Nonghyup branches, the post office and the "
                "Saemaul cooperatives have many branches nationwide and are "
                "very safe, so they can be used with confidence. All the "
                "institutions named so far are on the whole safe, but their "
                "interest rates are low.",

                "Anyone not satisfied with the low rates the commercial "
                "banks, the local banks and Nonghyup offer may use a mutual "
                "savings bank. Its rates are higher, but it is generally "
                "small and has few branches.",

                "Lately internet-only banks have appeared, providing "
                "financial services over an online network rather than "
                "building branches of their own. K bank and KakaoBank are "
                "examples. They are popular because the process is simpler "
                "than at an established bank, the fees are lower, and they "
                "can be used at any hour.",
            ],
        ),
        "은행 계좌 만들기": dict(
            title="Opening a bank account",
            paragraphs=[
                "To open an account you must go to the bank in person with "
                "your identification. This is because Korea operates a "
                "real-name system, under which all financial dealing must be "
                "done in one's own name. Lending your name to someone else, "
                "or opening an account in another's name, is punishable.",

                "A foreigner opening an account also needs identification — a "
                "passport, an alien registration card, a domestic residence "
                "report for a foreign-national Korean — and may be asked for "
                "papers such as proof of employment or of enrolment at a "
                "school. Internet banking and a cash card may be applied for "
                "at the same time. The account password and the cash card's "
                "should be chosen carefully, so that only you can know them. "
                "A credit card applied for is delivered to your home or "
                "workplace a few days later.",
            ],
        ),
        "금융 거래 하기": dict(
            title="Doing your banking",
            paragraphs=[
                "Once the account is open, you may bank as you find "
                "convenient: at an ATM, by internet banking, by smartphone "
                "banking.",

                "An ATM will let you withdraw, deposit, transfer and check "
                "the account. Bear in mind that a fee applies when you use "
                "the machine of a bank other than your own, or withdraw or "
                "transfer outside banking hours.",

                "Internet and smartphone banking let you do your banking "
                "freely from anywhere, by computer or telephone. To use them "
                "you must first fill in an application at the bank, with your "
                "identification, and submit it. For safety you are then "
                "issued a joint certificate, and enter a one-time password "
                "through an OTP device.",

                "If you sign up for the text service that reports deposits "
                "and withdrawals, you can see money entering and leaving your "
                "account on your telephone at once. Should money you know "
                "nothing about come in or go out, report it to the bank or the "
                "police without fail.",
            ],
        ),
    },

    extraAnnotations={
        "은행": dict(
            hanja="銀行", meaning="a bank",
            characters=[("銀", "은", "silver — as in 은메달"),
                        ("行", "행", "to go, a business — as in 행정, 여행")],
        ),
        "예금": dict(
            hanja="預金", meaning="a deposit; savings",
            characters=[("預", "예", "to entrust, beforehand — as in 예산"),
                        ("金", "금", "money — as in 현금, 세금")],
        ),
        "대출": dict(
            hanja="貸出", meaning="a loan",
            characters=[("貸", "대", "to lend — as in 임대 “letting”"),
                        ("出", "출", "to go out — as in 출금, 수출")],
        ),
        "송금": dict(
            hanja="送金", meaning="a remittance, sending money",
            characters=[("送", "송", "to send — as in 방송, 배송")],
        ),
        "환전": dict(
            hanja="換錢", meaning="changing money",
            characters=[("換", "환", "to exchange — as in 교환, 외환"),
                        ("錢", "전", "coin, money — as in 동전")],
        ),
        "장면": dict(hanja="場面", meaning="a scene"),
        "공통점": dict(
            hanja="共通點", meaning="a point in common",
            characters=[("共", "공", "together — as in 공유, 공동"),
                        ("通", "통", "to pass — as in 통과, 소통")],
        ),
        "차이점": dict(hanja="差異點", meaning="a point of difference"),
        "금융": dict(
            hanja="金融", meaning="finance, banking",
            characters=[("融", "융", "to melt, to circulate")],
            notes=["Literally money melting and flowing — hence the margin's "
                   "돈이 돌고 도는 것."],
        ),
        "금융기관": dict(hanja="金融機關", meaning="a financial institution"),
        "금융 거래": dict(hanja="金融去來", meaning="a financial transaction"),
        "맡다": dict(meaning="to take charge of, to hold for someone"),
        "빌려주다": dict(meaning="to lend"),
        "바꾸다": dict(meaning="to change, to exchange"),
        "공과금": dict(
            hanja="公課金", meaning="utility and public charges",
            characters=[("課", "과", "to impose, a lesson — as in 과제, 과목")],
        ),
        "관리비": dict(
            hanja="管理費", meaning="maintenance fees",
            notes=["The monthly charge on a Korean flat, covering the "
                   "building's shared costs."],
        ),
        "등록금": dict(
            hanja="登錄金", meaning="tuition fees",
            characters=[("登", "등", "to register — as in 등록, 등산")],
        ),
        "납부": dict(
            hanja="納付", meaning="payment (of a charge)",
            characters=[("納", "납", "to pay in — as in 납세"),
                        ("付", "부", "to hand over — as in 배부, 첨부")],
        ),
        "업무": dict(
            hanja="業務", meaning="business, work",
            characters=[("業", "업", "trade — as in 직업, 산업"),
                        ("務", "무", "duty — as in 의무, 국무총리")],
        ),
        "평일": dict(hanja="平日", meaning="a weekday"),
        "한국은행": dict(
            hanja="韓國銀行", meaning="the Bank of Korea",
            notes=["The central bank: it issues the currency and sets the "
                   "policy rate. Not a bank one holds an account with."],
        ),
        "시중은행": dict(
            hanja="市中銀行", meaning="a commercial bank",
            notes=["시중 is “in the market, about town” — a bank open to the "
                   "public, as against the central bank."],
        ),
        "지방은행": dict(hanja="地方銀行", meaning="a local bank"),
        "빌리다": dict(meaning="to borrow"),
        "지점": dict(
            hanja="支店", meaning="a branch",
            characters=[("支", "지", "branch, to support — as in 지출, 지원"),
                        ("店", "점", "shop — as in 상점, 백화점")],
        ),
        "공급": dict(
            hanja="供給", meaning="supply",
            characters=[("供", "공", "to offer — as in 제공"),
                        ("給", "급", "to give — as in 월급, 발급")],
            notes=["Its counterpart is 수요, demand."],
        ),
        "주되다": dict(hanja="主되다", meaning="to be the main one"),
        "설립": dict(
            hanja="設立", meaning="establishment, founding",
            characters=[("設", "설", "to establish — as in 시설, 설치"),
                        ("立", "립", "to stand — as in 입장, 독립")],
        ),
        "단위농협": dict(
            hanja="單位農協", meaning="a local Nonghyup branch",
            notes=["The village-level agricultural cooperative, which takes "
                   "deposits like a bank."],
        ),
        "우체국": dict(
            hanja="郵遞局", meaning="a post office",
            characters=[("郵", "우", "post — as in 우편, 우표"),
                        ("遞", "체", "to deliver in turn"),
                        ("局", "국", "bureau — as in 방송국, 약국")],
            notes=["Korean post offices take deposits and sell insurance as "
                   "well as carrying letters."],
        ),
        "안전성": dict(hanja="安全性", meaning="safety, security"),
        "안심": dict(
            hanja="安心", meaning="peace of mind",
            characters=[("安", "안", "peace — as in 안전, 치안"),
                        ("心", "심", "heart — as in 관심, 중심")],
        ),
        "대체로": dict(hanja="大體로", meaning="on the whole, generally"),
        "반면": dict(hanja="反面", meaning="whereas, on the other hand"),
        "금리": dict(
            hanja="金利", meaning="an interest rate",
            characters=[("利", "리", "profit, interest — as in 이익, 이자")],
        ),
        "상호저축은행": dict(
            hanja="相互貯蓄銀行", meaning="a mutual savings bank",
            characters=[("互", "호", "mutual — as in 상호"),
                        ("貯", "저", "to store up — as in 저축")],
            notes=["Higher rates, smaller and less safe than a commercial "
                   "bank — the trade-off the article is making."],
        ),
        "장점": dict(
            hanja="長點", meaning="an advantage, a strong point",
            notes=["Its opposite is 단점, which chapter 26's warm-up pairs it "
                   "with."],
        ),
        "인터넷 전문 은행": dict(
            hanja="인터넷專門銀行", meaning="an internet-only bank",
        ),
        "등장": dict(
            hanja="登場", meaning="appearance, coming on the scene",
            characters=[("登", "등", "to climb, to appear — as in 등록"),
                        ("場", "장", "place, stage — as in 장면, 시장")],
        ),
        "케이뱅크": dict(meaning="K bank"),
        "카카오뱅크": dict(
            meaning="KakaoBank",
            notes=["Opened 2017 and now one of Korea's largest banks by "
                   "customers, with no branches at all."],
        ),
        "절차": dict(
            hanja="節次", meaning="a procedure, formalities",
            characters=[("節", "절", "a joint, a season — as in 명절, 절기"),
                        ("次", "차", "order, next — as in 차례, 제25차")],
        ),
        "수수료": dict(
            hanja="手數料", meaning="a fee, a commission",
            characters=[("手", "수", "hand — as in 수표, 수단"),
                        ("數", "수", "number — as in 횟수, 과반수")],
        ),
        "소득": dict(hanja="所得", meaning="income"),
        "상품": dict(
            hanja="商品", meaning="a product",
            notes=["A bank's 상품 is an account or a plan, not a thing on a "
                   "shelf."],
        ),
        "입금": dict(hanja="入金", meaning="a deposit, paying in"),
        "출금": dict(hanja="出金", meaning="a withdrawal"),
        "보통 예금": dict(
            hanja="普通預金", meaning="an ordinary deposit account",
            notes=["Money in and out as you please, at almost no interest."],
        ),
        "정기 예금": dict(
            hanja="定期預金", meaning="a time deposit",
            notes=["A lump sum left for a fixed term."],
        ),
        "정기 적금": dict(
            hanja="定期積金", meaning="a regular savings plan",
            characters=[("積", "적", "to pile up — as in 면적, 적극")],
            notes=["A set amount paid in every month for a fixed term — the "
                   "commonest way Koreans save."],
        ),
        "계좌": dict(
            hanja="計座", meaning="an account",
            characters=[("計", "계", "to reckon — as in 계획, 통계"),
                        ("座", "좌", "seat — as in 좌석, 강좌")],
        ),
        "방문": dict(hanja="訪問", meaning="a visit"),
        "금융실명제": dict(
            hanja="金融實名制", meaning="the real-name financial system",
            characters=[("實", "실", "real — as in 사실, 실제"),
                        ("名", "명", "name — as in 성명, 유명")],
            notes=["Introduced by emergency decree in 1993 to stop money "
                   "moving under borrowed names."],
        ),
        "외국인등록증": dict(
            hanja="外國人登錄證", meaning="an alien registration card",
            notes=["The residence card the 출입국·외국인정책본부 issues — chapter "
                   "22's office."],
        ),
        "외국국적동포": dict(
            hanja="外國國籍同胞",
            meaning="an ethnic Korean of foreign nationality",
            characters=[("同", "동", "same — as in 동일, 동의"),
                        ("胞", "포", "womb, sibling — as in 세포 “a cell”")],
        ),
        "국내 거소 신고증": dict(
            hanja="國內居所申告證",
            meaning="a domestic residence report certificate",
            notes=["What an 외국국적동포 carries in place of the alien "
                   "registration card."],
        ),
        "재직증명서": dict(
            hanja="在職證明書", meaning="proof of employment",
            characters=[("在", "재", "to be at — as in 재적, 현재"),
                        ("職", "직", "post — as in 직업, 고위 공직자")],
        ),
        "재학증명서": dict(
            hanja="在學證明書", meaning="proof of enrolment at a school",
        ),
        "서류": dict(
            hanja="書類", meaning="papers, documents",
            characters=[("書", "서", "writing — as in 도서, 서명"),
                        ("類", "류", "kind, sort — as in 종류, 인류")],
        ),
        "인터넷 뱅킹": dict(meaning="internet banking"),
        "현금 인출 카드": dict(
            hanja="現金引出카드", meaning="a cash card",
            characters=[("引", "인", "to pull — as in 할인, 인상"),
                        ("出", "출", "to take out — as in 출금, 지출")],
        ),
        "신중": dict(
            hanja="愼重", meaning="care, prudence",
            characters=[("愼", "신", "to be cautious"),
                        ("重", "중", "heavy, weighty — as in 중요, 비중")],
        ),
        "배송": dict(hanja="配送", meaning="delivery"),
        "거래": dict(
            hanja="去來", meaning="a transaction, dealing",
            characters=[("去", "거", "to go — as in 과거, 제거"),
                        ("來", "래", "to come — as in 미래, 원래")],
            notes=["Literally going and coming — money or goods passing both "
                   "ways."],
        ),
        "ATM": dict(
            hanja="現金自動入出金機", meaning="a cash machine",
            notes=["Korean names it 현금자동입출금기 in full — the machine that "
                   "takes cash in and pays it out automatically."],
        ),
        "이체": dict(
            hanja="移替", meaning="a transfer between accounts",
            characters=[("移", "이", "to move — as in 이민, 이사"),
                        ("替", "체", "to replace, to substitute")],
        ),
        "계좌조회": dict(
            hanja="計座照會", meaning="checking an account",
            characters=[("照", "조", "to shine, to consult — as in 조명"),
                        ("會", "회", "to meet — as in 회의, 국회")],
        ),
        "기기": dict(hanja="機器", meaning="a device, a machine"),
        "신청서": dict(hanja="申請書", meaning="an application form"),
        "작성": dict(
            hanja="作成", meaning="filling in, drawing up",
            characters=[("作", "작", "to make — as in 제작, 작품"),
                        ("成", "성", "to complete — as in 성장, 구성")],
        ),
        "공동인증서": dict(
            hanja="共同認證書", meaning="a joint certificate",
            notes=["Renamed from 공인인증서 in 2020. The digital certificate "
                   "Korean banking has long run on."],
        ),
        "OTP": dict(
            meaning="a one-time password device",
            notes=["A token or card that shows a number good for one use."],
        ),
        "1회용": dict(
            hanja="一回用", meaning="single-use, one-time",
            characters=[("回", "회", "a time, to turn — as in 횟수, 회기")],
        ),
        "문자": dict(
            hanja="文字", meaning="a text message; a letter of an alphabet",
            notes=["문자를 보내다 “to send a text”, and 문자 “characters” as in "
                   "한글이라는 문자."],
        ),
        "통장": dict(
            hanja="通帳", meaning="a bankbook",
            characters=[("帳", "장", "a ledger, an account book")],
        ),
        "곧바로": dict(meaning="straight away, directly"),
        "빠져나가다": dict(meaning="to slip out, to go out (of money)"),
        "예금자 보호 제도": dict(
            hanja="預金者保護制度", meaning="deposit insurance",
            notes=["Up to 50 million won per person per institution — raised "
                   "to 100 million in 2025, after this printing."],
        ),
        "시행": dict(
            hanja="施行", meaning="enforcement, being in operation",
            characters=[("施", "시", "to carry out — as in 실시, 시설")],
        ),
        "의해": dict(hanja="依해", meaning="by, under (a rule)"),
        "원금": dict(
            hanja="元金", meaning="the principal",
            characters=[("元", "원", "origin — as in 원래, 원인")],
        ),
        "이자": dict(
            hanja="利子", meaning="interest",
            characters=[("利", "리", "profit — as in 금리, 이익"),
                        ("子", "자", "child, thing — as in 의자, 원자재")],
        ),
        "예금액": dict(hanja="預金額", meaning="the amount deposited"),
        "메신저 피싱": dict(
            meaning="messenger phishing",
            notes=["Taking over a messaging account and asking the victim's "
                   "friends for money — the commonest fraud of its kind in "
                   "Korea."],
        ),
        "소셜 미디어": dict(meaning="social media"),
        "계정": dict(
            hanja="計定", meaning="an account (online)",
            notes=["An online account is a 계정; a bank account a 계좌."],
        ),
        "몰래": dict(meaning="secretly, without being noticed"),
        "빼가다": dict(meaning="to take away, to siphon off"),
        "급히": dict(hanja="急히", meaning="urgently, in a hurry"),
        "방식": dict(hanja="方式", meaning="a method, a way"),
        "안부": dict(
            hanja="安否", meaning="asking after someone",
            characters=[("否", "부", "not, whether — as in 여부, 거부")],
            notes=["안부 전화 “a call to see how someone is”, 안부를 묻다 “to ask "
                   "after”."],
        ),
        "뒤늦게": dict(meaning="belatedly, too late"),
        "예방": dict(hanja="豫防", meaning="prevention"),
        "요구": dict(hanja="要求", meaning="a demand, asking for"),
        "출처": dict(
            hanja="出處", meaning="a source, where something comes from",
            notes=["The word at the foot of every quoted passage in this "
                   "book."],
        ),
        "분명": dict(
            hanja="分明", meaning="being clear, evident",
            characters=[("分", "분", "to divide — as in 부분, 신분"),
                        ("明", "명", "bright — as in 설명, 투명")],
        ),
        "첨부 파일": dict(
            hanja="添附파일", meaning="an attached file",
            characters=[("添", "첨", "to add — as in 첨가"),
                        ("附", "부", "to attach — as in 부록")],
        ),
        "공공장소": dict(hanja="公共場所", meaning="a public place"),
    },

    extraNotes=[
        "The margin gloss for ATM is my own wording: the book heads the entry "
        "ATM(현금자동입출금기) and leaves the definition to the article.",
        "The five rules against messenger phishing are printed numbered in "
        "their own box, and set here as a numbered list; the case study is "
        "set as a quoted passage.",
        "The review gaps on p. 151 are blank in the book and left blank here.",
    ],
)
