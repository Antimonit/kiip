# -*- coding: utf-8 -*-
"""Chapter 33 — The family and the law.

Transcribed from the photos of pp. 174-177. Your English glosses on pp. 174,
175 and 176 are carried as the entries for the words they sit over.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, LABELS,
               MARGIN, TABLE, CELL, GLOSSARY)

CHAPTER = dict(
    number=33, slug="33-family-and-law",
    unit="법", title="가족과 법", titleEn="The family and the law",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 ‘결혼’과 관련된 물건입니다.",
                  "Below are things to do with getting married."),
        LABELS("반지", "{청첩장}", "웨딩드레스", "부케"),
        FIGURE("결혼 관련 사진 넷 — 반지, 청첩장, 웨딩드레스, 부케"),
        HEADING(4, "01 각 사진에 나타난 물건들이 결혼에서 어떤 역할을 하는지 말해 봅시다.",
                translation="Say what part each of the things in the "
                            "photographs plays in a wedding."),
        HEADING(4, "02 자신의 고향 나라에서 결혼을 할 때 꼭 준비하는 물건이나 절차에는 무엇이 있습니까?",
                translation="What things or steps are always prepared for a "
                            "wedding in your home country?"),

        SECTION("goals", "학습목표"),
        BULLET("{부부}의 권리와 의무에 관한 법의 기본 내용을 설명할 수 있다.", ordered=True,
               translation="Explain the basics of the law on a married "
                           "couple’s rights and duties."),
        BULLET("{가정 폭력} 및 {이혼}에 적용되는 법의 기본 내용을 설명할 수 있다.", ordered=True,
               translation="Explain the basics of the law that applies to "
                           "domestic violence and divorce."),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"],
              [["심화", "법", "17. 가족 문제와 법",
                "가족과 친족, 법률혼·사실혼·동거, 이혼의 종류, 이혼의 절차와 방법"]]),

        SECTION("part", "01 법은 결혼생활에 어떤 영향을 줄까?"),
        GLOSSARY(("혼인 신고", "결혼한 사실을 행정 기관에 공식적으로 신고하는 일", "혼인 신고",
                  "marriage registration")),
        HEADING(2, "부부로 인정받기 위한 절차", translation=
                "The steps to being recognised as a married couple" "\n\n"
                "Marriage is two people who love each other meeting and "
                "becoming husband and wife. For the two to be recognised as "
                "a married couple in law, the marriage must be registered at "
                "a city, district or county office. Even a couple who have "
                "held no wedding are recognised as married and can receive "
                "the protection of the law once they register. A couple who "
                "have not registered may be unable to enjoy legal rights "
                "over property, the raising of children and so on."),
        PARAGRAPH("결혼은 사랑하는 두 사람이 만나 {부부}가 되는 것이다. 두 사람이 법적인 부부로 "
                  "{인정받기|인정받다} 위해서는 시청, 구청, 군청 등에 {혼인 신고}를 해야 한다. 결혼식을 "
                  "올리지 않은 부부라도 혼인 신고를 하면 부부로 인정되고 법의 보호를 받을 수 있다. 혼인 "
                  "신고를 하지 않은 부부는 {재산}, 자녀 {양육} 등과 관련하여 법적인 권리를 누리지 못할 수 "
                  "있다."),
        FIGURE("○○시청에 있는 혼인 신고 기념 포토존"),

        GLOSSARY(("처분", "일정한 대상을 어떻게 처리할 것인가에 대해 결정함", "처분"),
                 ("부부 별산제",
                  "부부가 혼인하기 전부터 각자 가졌던 재산 또는 혼인생활 중 자기 이름으로 얻은 재산을 "
                  "각자의 것으로 인정하는 제도", "부부 별산제",
                  "the separate property system"),
                 ("가사노동", "청소, 빨래, 요리 등 가정을 유지하고 살림을 꾸려나가기 위해 하는 노동",
                  "가사노동", "domestic chores")),
        HEADING(2, "부부의 권리와 의무", translation=
                "A married couple’s rights and duties" "\n\n"
                "In Korea each of a married couple may hold property of "
                "their own and has the right to dispose of it as they see "
                "fit. This is called the separate property system. Even so, "
                "property in the name of one of them is regarded as joint "
                "property where the couple obtained it by working together "
                "after marrying. The couple may also act for one another in "
                "dealing with everyday goods or money, buying things or "
                "borrowing money on the other’s behalf." "\n\n"
                "There are also duties they owe each other. A married couple "
                "should basically live together. And since theirs is a "
                "relationship of helping and depending on each other "
                "mentally and financially, they must bear the cost of living "
                "jointly. Where one of them earns money at work and the "
                "other does the domestic work, both are held in law to have "
                "earned the living. That is because if neither of them did "
                "the domestic work themselves, someone else would have to be "
                "employed to take it on, and that cost too would count as "
                "the cost of living."),
        PARAGRAPH("한국에서는 부부가 각자 자신의 {재산}을 가질 수 있고 자신의 뜻에 따라 그 재산을 "
                  "{처분}할 수 있는 권리가 있다. 이를 {부부 별산제}라고 한다. 그런데 부부 중 어느 한쪽의 "
                  "이름으로 되어 있는 재산이라고 해도 부부가 결혼 후에 함께 노력하여 얻은 것은 {공동} "
                  "재산으로 본다. 부부는 {일상적}인 물건이나 돈을 {거래할|거래하다} 때 서로를 "
                  "{대신하여|대신하다} 물건을 {구입하거나|구입하다} 돈을 빌릴 수도 있다."),
        PARAGRAPH("부부 간에는 서로 지켜야 할 의무도 있다. 부부는 기본적으로 함께 살아야 한다. 또한 부부는 "
                  "{정신적}, 경제적으로도 서로 돕고 {의지하는|의지하다} 관계이므로 생활에 필요한 비용을 "
                  "공동으로 {부담해야|부담하다} 한다. 부부 중 한 사람은 직장에서 돈을 벌고 다른 사람은 "
                  "{가사노동}을 하는 경우에도 법적으로는 두 사람 모두 {생활비}를 번 것으로 인정한다. 만약 "
                  "부부 중 누군가가 가사노동을 직접 하지 않는다면 그 가사노동을 {맡아줄|맡다} 다른 사람을 "
                  "{고용해야|고용하다} 하는데 그 비용도 생활비에 {해당하기|해당하다} 때문이다."),
        FIGURE("부부는 함께 살아야 하지만, 일시적으로 따로 살 수밖에 없는 경우도 있다."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "결혼을 하면 혼인 신고! 아이를 낳으면 출생 신고!", translation=
                "Marry and register the marriage! Have a child and register "
                "the birth!" "\n\n"
                "Just as a couple who marry without registering the marriage "
                "are not recognised as married in law, a child’s rights may "
                "not be protected in law if the birth is not registered when "
                "the child is born. When a child is born the hospital "
                "generally issues a birth certificate. It records the "
                "parents’ names and address, the place of birth (a hospital, "
                "a home and so on), the date and time of birth, and the "
                "child’s sex, height, weight, state of health, the hospital "
                "and the doctor. Once the child’s mother or father takes the "
                "birth certificate to the community service centre for the "
                "area where they live and registers the birth, the child is "
                "recognised as a member of Korean society. The birth must be "
                "registered within a month of the child being born. Past a "
                "month, a fine of up to 50,000 won is payable. Lately it has "
                "become possible to register a birth online as well."),
        PARAGRAPH("결혼을 하고 혼인 신고를 하지 않으면 법적인 부부로 인정받지 못하듯이 아이가 태어났을 때 "
                  "{출생 신고}를 하지 않으면 그 아이의 권리를 법적으로 보호받지 못할 수 있다. 아이가 "
                  "태어나면 일반적으로 병원에서 {출생증명서}를 {발급해준다|발급하다}. 출생증명서에는 부모의 "
                  "이름과 주소, 출생한 장소(병원, 집 등), 출생한 날짜와 시간, 아이의 {성별}, 키, 몸무게, "
                  "건강 상태, 병원 이름, 의사 이름 등이 기록되어 있다. 아이의 엄마나 아빠가 출생증명서를 "
                  "가지고 본인이 살고 있는 지역의 행정복지센터에 가서 출생신고를 하면 그 아이는 한국 사회의 "
                  "{구성원}으로 인정받는다. 출생신고는 아이가 태어난 후 1개월 내에 해야 한다. 1개월을 "
                  "{넘기면|넘기다} 최대 5만원의 {과태료}를 내야 한다. 최근에는 인터넷으로도 출생 신고를 할 "
                  "수 있게 되었다."),

        SECTION("part", "02 가족관계에서 생기는 문제를 법으로 어떻게 해결할 수 있을까?"),
        GLOSSARY(("인격", "사람으로서의 품위와 자격", "인격", "personality, character")),
        HEADING(2, "가정 폭력의 해결", translation=
                "Dealing with domestic violence" "\n\n"
                "A family is the closest and most intimate relationship "
                "there is, but that is no reason to treat one another "
                "carelessly. A family should respect each other and protect "
                "each other’s dignity and rights. Where a member of a family "
                "acts so as to cause physical, mental or financial harm to "
                "another, that is regarded as domestic violence and is "
                "punished." "\n\n"
                "Korean law defines all of the following as domestic "
                "violence: striking a family member or throwing things at "
                "them, swearing at them or threatening them, failing to look "
                "after a child or an elderly person properly or tormenting "
                "them, and not providing the money needed to live. Where "
                "domestic violence occurs one can report it to the police or "
                "ask a counselling centre for help."),
        PARAGRAPH("가족은 가장 가깝고 {친밀한|친밀하다} 관계를 맺고 있지만 그렇다고 해서 {함부로} "
                  "{대하면|대하다} 안 된다. 가족은 서로 {존중하고|존중하다} 각자의 {인격}과 권리를 "
                  "지켜주어야 한다. 만약 가족 {구성원} 사이에 {신체적}, 정신적, {재산적} 피해를 주는 "
                  "행동을 한다면 그것은 {가정 폭력}으로 {간주되어|간주되다} {처벌}을 받게 된다."),
        PARAGRAPH("한국의 법에서는 가족을 때리거나 가족에게 물건을 던지는 것, 가족에게 {욕설}을 하거나 "
                  "{협박하는|협박하다} 것, 어린이나 노인을 제대로 {돌보지|돌보다} 않거나 "
                  "{괴롭히는|괴롭히다} 것, 필요한 생활비를 주지 않는 것 등을 모두 가정 폭력으로 "
                  "{규정하고|규정하다} 있다. 가정 폭력이 발생하면 경찰에 신고하거나 상담센터 등에 "
                  "{요청하여|요청하다} 도움을 받을 수 있다."),
        FIGURE("‘가정폭력 현행범 즉시 체포, 접근금지 어기면 징역’ 경찰 홍보물"),
        MARGIN("▶ 가정폭력 발생 시 상담센터",
               "여성긴급전화 1366",
               "한국여성의전화 (02) 2263-6464",
               "안전Dream 아동 여성 장애인 경찰지원센터 117",
               "한국남성의전화 (02) 2653-1366",
               "건강가정지원센터 1577-9337",
               "한국가정법률상담소 1644-7077",
               "다누리 콜센터 1577-1366"),

        GLOSSARY(("위자료", "다른 사람의 불법적인 행위로 인해 생긴 정신적 고통이나 피해에 대해 물어주는 돈",
                  "위자료", "alimony, damages")),
        HEADING(2, "이혼의 종류와 방법", translation=
                "The kinds of divorce, and how it is done" "\n\n"
                "Where a couple think they can no longer keep their married "
                "life going, they can divorce by agreement or through a "
                "court. Divorce by agreement is the couple agreeing between "
                "themselves to divorce; judicial divorce is divorce decided "
                "by a court’s ruling when one of them wants a divorce and "
                "the other does not consent. For instance, where one of them "
                "has been unfaithful, or has otherwise failed to carry out "
                "the duties of a spouse and caused the other suffering, the "
                "court can order a divorce by its ruling." "\n\n"
                "The spouse responsible for the divorce must pay the other "
                "damages. Even if a couple divorce, the relationship between "
                "parent and child remains as it was. Who will raise the "
                "children is decided by agreement between the two divorcing. "
                "If no agreement is reached, it follows the ruling of the "
                "family court. The side that comes to raise the children can "
                "ask the other for part of the cost of doing so. The side "
                "that does not raise them is allowed to see them within "
                "limits."),
        PARAGRAPH("부부가 더 이상 결혼 생활을 유지하기 어렵다고 생각하면 {합의}나 재판을 통해 {이혼}을 할 "
                  "수 있다. {협의 이혼}은 부부가 서로 합의하여 이혼을 하는 것이고, {재판상 이혼}은 부부 중 "
                  "한쪽은 이혼을 원하는데 다른 한쪽이 {동의하지|동의하다} 않을 때 법원의 {판결}에 따라 "
                  "이혼을 결정하는 것이다. 예를 들어 부부 중 한쪽이 {부정한|부정하다} {행위}를 하는 등 "
                  "배우자로서의 의무를 제대로 {이행하지|이행하다} 않고 상대방을 고통스럽게 한 경우에는 "
                  "법원에서 판결로 이혼을 {명령할|명령하다} 수 있다."),
        PARAGRAPH("이혼에 책임이 있는 배우자는 상대방에게 {위자료}를 줘야 한다. 부부가 이혼을 하더라도 "
                  "부모와 자녀의 관계는 그대로 유지된다. 누가 자녀를 키울 것인가의 문제는 이혼을 하는 두 "
                  "사람의 합의로 결정한다. 만약 합의가 이뤄지지 않으면 {가정법원}의 판결에 따른다. 자녀를 "
                  "키우게 된 쪽은 상대방에게 자녀 양육에 필요한 비용의 일부를 {요구할|요구하다} 수 있다. "
                  "자녀를 키우지 않게 된 쪽은 {제한된|제한되다} 범위 내에서 자녀와 만나는 것이 "
                  "{허용된다|허용되다}."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "이혼한 상대방이 위자료나 양육비를 주지 않는다면?", translation=
                "What if a divorced spouse does not pay the damages or the "
                "child support?" "\n\n"
                "The spouse responsible for the divorce must pay the other "
                "damages. The side that does not raise the children must also "
                "pay the other child support. Where the damages or the child "
                "support are not paid despite the family court’s ruling, one "
                "can apply to the family court for an enforcement order — an "
                "order to pay the child support. Where the order is made and "
                "still not complied with up to three times, a fine becomes "
                "payable. In some cases the person may even be held in prison "
                "until they pay."),
        PARAGRAPH("이혼의 책임이 있는 배우자는 상대방에게 위자료를 {지급해야|지급하다} 한다. 또한 자녀를 "
                  "양육하지 않는 측에서는 상대방에게 자녀 {양육비}를 지급해야 한다. 하지만 가정법원의 "
                  "판결에도 {불구하고|불구하다} 위자료나 자녀 양육비를 지급하지 않는다면 가정법원에 "
                  "{이행 명령}(양육비를 지급하라는 명령)을 신청하면 된다. 가정법원이 이행 명령을 "
                  "{내렸는데도|내리다} 3회까지 이행하지 않을 때는 과태료를 내게 된다. 경우에 따라서는 "
                  "지급할 때까지 {교도소}에 {갇힐|갇히다} 수도 있다."),
        FIGURE("가정의 문제를 해결하는 가정법원 (서울)"),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 법은 결혼생활에 어떤 영향을 줄까?"),
        BULLET("결혼한 두 사람이 법적인 부부로 인정받기 위해서는 시청, 구청, 군청 등에 (            )를 "
               "해야 한다."),
        BULLET("한국에서는 남편과 아내가 각자 자기 재산을 가질 수 있고 자신의 뜻에 따라 그 재산을 처분할 "
               "수 있다. 그러나 결혼 후 부부가 함께 노력하여 얻은 재산은 (        ) 재산으로 본다."),
        BULLET("부부는 기본적으로 함께 살아야 하며 생활 비용을 공동으로 부담해야 한다. 부부 중 한 사람은 "
               "직장 생활을 하고 다른 사람은 (            )을 하는 경우라도 둘이 함께 생활비를 번 것으로 "
               "인정된다."),
        HEADING(3, "02 가족관계에서 생기는 문제를 법으로 어떻게 해결할 수 있을까?"),
        BULLET("가족에게 신체적, 정신적, 재산적 피해를 주는 것은 (            )으로 간주되어 법에 따라 "
               "처벌을 받는다."),
        BULLET("두 사람이 합의하여 이혼하는 것을 (        ) 이혼이라고 하고, 부부 중 한쪽이 이혼에 "
               "동의하지 않을 때 법원의 판결을 통해 이혼하는 것을 (        ) 이혼이라고 한다."),
        BULLET("이혼에 책임이 있는 배우자는 상대방에게 (        )를 줘야 한다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "이혼의 책임이 주로 한국인 배우자에게 있다면?", translation=
                "What if the responsibility for a divorce lies mainly with "
                "the Korean spouse?" "\n\n"
                "One of the things an immigrant in an international marriage "
                "worries about most, should it come to divorce, is whether "
                "they will lose their residence status in Korea. In the past "
                "a marriage immigrant’s residence status was extended only "
                "where the responsibility for the divorce lay ‘entirely’ "
                "with the Korean spouse. Recently, however, the Supreme "
                "Court has ruled that residence status should be granted to "
                "a marriage immigrant where the responsibility lies ‘mainly’ "
                "with the Korean spouse. Limiting the condition for keeping "
                "residence status to cases where the marriage immigrant "
                "bears ‘no’ responsibility at all for the divorce, it held, "
                "may leave their rights inadequately protected. The ruling "
                "is regarded as one that raises the level of marriage "
                "immigrants’ human rights around divorce and may help "
                "towards a better married life as well."),
        PARAGRAPH("{국제결혼}을 한 이민자가 이혼을 하게 될 경우 가장 걱정하는 부분 중 하나가 한국에서의 "
                  "체류 자격을 잃지 않을까 하는 것이다. 과거에는 이혼의 책임이 ‘{전적}으로’ 한국인 "
                  "배우자에게 있어야만 결혼 이민자의 체류 자격을 {연장해주었다|연장하다}. 그러나 최근 "
                  "{대법원}은 한국인 배우자에게 ‘주로’ 책임이 있다면 결혼 이민자에게 체류 자격을 주어야 "
                  "한다고 {판결하였다|판결하다}. 이혼에 {이르기까지|이르다} 결혼이민자에게는 ‘{전혀}’ "
                  "책임이 없는 경우로만 체류 자격 유지 조건을 {제한한다면|제한하다} 결혼 이민자의 권리가 "
                  "제대로 보장되지 않을 수 있다는 것이다. 이것은 이혼과 관련하여 결혼 이민자의 인권 수준을 "
                  "높이고 보다 나은 결혼생활에도 도움을 줄 수 있는 판결로 {평가된다|평가되다}."),
        FIGURE("‘이주여성 인권 사각지대 해결방안 모색’ 홍보물"),
        PARAGRAPH("★ 국제결혼을 한 이민자의 어려움을 줄이고 권리를 보호하기 위해서는 어떤 노력과 정책이 "
                  "필요한지 이야기해 봅시다.",
                  "Talk about what efforts and policies are needed to lessen "
                  "the difficulties of immigrants in international marriages "
                  "and to protect their rights."),
    ],

    extraAnnotations={
        "청첩장": dict(
            hanja="請牒狀", meaning="a wedding invitation",
            characters=[("請", "청", "to invite, ask — as in 신청, 요청"),
                        ("牒", "첩", "a note, a document"),
                        ("狀", "장", "a letter, a form — as in 상장, 영장")],
        ),
        "부부": dict(
            hanja="夫婦", meaning="a married couple, husband and wife",
            characters=[("夫", "부", "husband, man — as in 남편의 夫, 부인"),
                        ("婦", "부", "wife, woman — as in 주부, 임산부")],
        ),
        "가정 폭력": dict(
            hanja="家庭暴力", meaning="domestic violence",
            characters=[("家庭", None, "the home, the household"),
                        ("暴力", None, "violence — 暴 violent, 力 force")],
        ),
        "이혼": dict(
            hanja="離婚", meaning="divorce",
            characters=[("離", "리", "to part, separate — as in 격리, 분리"),
                        ("婚", "혼", "marriage — as in 결혼, 혼인")],
        ),
        "인정받다": dict(
            hanja="認定받다", meaning="to be recognised (as)",
            characters=[("認", "인", "to acknowledge — as in 인식, 승인"),
                        ("定", "정", "to fix, settle — as in 결정, 지정")],
            surfaces=["인정받기"],
        ),
        "혼인 신고": dict(
            hanja="婚姻申告", meaning="registering a marriage",
            characters=[("婚姻", None, "marriage (the legal act)"),
                        ("申告", None, "a report to the authorities — chapter 31")],
        ),
        "재산": dict(
            hanja="財産", meaning="property, assets",
            characters=[("財", "재", "wealth — as in 재정, 재물"),
                        ("産", "산", "to produce, property — as in 생산, 부동산")],
            notes=["Chapter 34’s subject: property and the law."],
        ),
        "양육": dict(
            hanja="養育", meaning="raising a child, upbringing",
            characters=[("養", "양", "to nurture — as in 양성, 영양"),
                        ("育", "육", "to raise — as in 교육, 보육")],
        ),
        "처분": dict(
            hanja="處分", meaning="disposal; deciding what to do with something",
            characters=[("處", "처", "to handle — as in 처리, 처우"),
                        ("分", "분", "to divide — as in 분리, 신분")],
        ),
        "부부 별산제": dict(
            hanja="夫婦別産制", meaning="the separate property system",
            characters=[("別", "별", "separate — as in 구별, 특별"),
                        ("産", "산", "property"),
                        ("制", "제", "a system — as in 제도, 직선제")],
            notes=["What each of a couple owned before marrying, and what "
                   "each obtains in their own name during it, is theirs."],
        ),
        "공동": dict(
            hanja="共同", meaning="joint, shared",
            characters=[("共", "공", "together — as in 공공, 공유"),
                        ("同", "동", "same — as in 동등, 동일")],
        ),
        "일상적": dict(
            hanja="日常的", meaning="everyday, ordinary",
            characters=[("日常", None, "daily life — 日 day, 常 usual")],
        ),
        "거래하다": dict(
            hanja="去來하다", meaning="to deal, to transact",
            characters=[("去", "거", "to go — as in 강제퇴거, 과거"),
                        ("來", "래", "to come — as in 미래, 내년")],
            surfaces=["거래할"],
        ),
        "대신하다": dict(
            hanja="代身하다", meaning="to act in place of, to substitute for",
            characters=[("代", "대", "to replace, a generation — as in 대리, 대신"),
                        ("身", "신", "body, self — as in 신분, 자신")],
            surfaces=["대신하여"],
        ),
        "구입하다": dict(
            hanja="購入하다", meaning="to purchase",
            characters=[("購", "구", "to buy — as in 구매, 구입"),
                        ("入", "입", "to enter, take in — as in 수입, 입원")],
            surfaces=["구입하거나"],
        ),
        "정신적": dict(
            hanja="精神的", meaning="mental, of the mind",
            characters=[("精神", None, "spirit, mind — as in 준법 정신")],
        ),
        "의지하다": dict(
            hanja="依支하다", meaning="to depend on, to lean on",
            characters=[("依", "의", "to rely on — as in 의존"),
                        ("支", "지", "to support — as in 지원, 지지")],
            surfaces=["의지하는"],
        ),
        "부담하다": dict(
            hanja="負擔하다", meaning="to bear (a cost), to shoulder",
            characters=[("負", "부", "to carry, to lose — as in 부담, 승부"),
                        ("擔", "담", "to bear — as in 담당, 부담")],
            surfaces=["부담해야"],
        ),
        "가사노동": dict(
            hanja="家事勞動", meaning="domestic work, housework",
            characters=[("家事", None, "household affairs — 家 house, 事 matter"),
                        ("勞動", None, "labour")],
        ),
        "생활비": dict(
            hanja="生活費", meaning="the cost of living, living expenses",
            characters=[("生活", None, "living, life"),
                        ("費", "비", "expense — as in 학비, 진료비")],
        ),
        "맡다": dict(meaning="to take on, to be charged with", surfaces=["맡아줄"]),
        "고용하다": dict(
            hanja="雇傭하다", meaning="to employ",
            characters=[("雇", "고", "to hire — as in 고용, 해고"),
                        ("傭", "용", "to hire, wages")],
            surfaces=["고용해야"],
        ),
        "해당하다": dict(
            hanja="該當하다", meaning="to count as, to correspond to",
            characters=[("該", "해", "that, the said"),
                        ("當", "당", "to be due — as in 정당, 상당")],
            surfaces=["해당하기"],
        ),
        "출생 신고": dict(
            hanja="出生申告", meaning="registering a birth",
            characters=[("出生", None, "birth — 出 to come out, 生 life"),
                        ("申告", None, "a report to the authorities")],
        ),
        "출생증명서": dict(
            hanja="出生證明書", meaning="a birth certificate",
            characters=[("證明書", None, "a certificate — 證 evidence, "
                                         "明 clear, 書 document")],
        ),
        "발급하다": dict(
            hanja="發給하다", meaning="to issue (a document)",
            characters=[("發", "발", "to send out — as in 발행, 발생"),
                        ("給", "급", "to give, supply — as in 지급, 공급")],
            surfaces=["발급해준다"],
        ),
        "성별": dict(
            hanja="性別", meaning="sex, gender",
            characters=[("性", "성", "nature, sex — as in 성격, 양성평등"),
                        ("別", "별", "to distinguish — as in 구별, 차별")],
        ),
        "구성원": dict(
            hanja="構成員", meaning="a member (of a body)",
            characters=[("構成", None, "to make up, compose"),
                        ("員", "원", "member — as in 회원, 직원")],
        ),
        "넘기다": dict(
            meaning="to pass (a limit), to let go by",
            surfaces=["넘기면"],
        ),
        "과태료": dict(
            hanja="過怠料", meaning="a fine (an administrative penalty)",
            characters=[("過", "과", "fault, excess — as in 과실, 초과"),
                        ("怠", "태", "idleness, neglect"),
                        ("料", "료", "a fee — as in 수수료, 위자료")],
            notes=["Distinct from 벌금, which is a criminal fine — chapter 36."],
        ),
        "인격": dict(
            hanja="人格", meaning="dignity as a person, character",
            characters=[("人", "인", "person"),
                        ("格", "격", "standing, rank — as in 자격, 성격")],
        ),
        "친밀하다": dict(
            hanja="親密하다", meaning="to be close, intimate",
            characters=[("親", "친", "close, kin — as in 친척, 친구"),
                        ("密", "밀", "dense, close — as in 밀집, 비밀")],
            surfaces=["친밀한"],
        ),
        "함부로": dict(
            meaning="carelessly, thoughtlessly, however one likes",
            notes=["함부로 대하다 “to treat someone carelessly”; 함부로 말하다 "
                   "“to speak out of turn”."],
        ),
        "대하다": dict(
            hanja="對하다", meaning="to treat, to face",
            characters=[("對", "대", "facing, toward — as in 대상, 대응")],
            surfaces=["대하면"],
        ),
        "존중하다": dict(
            hanja="尊重하다", meaning="to respect",
            characters=[("尊", "존", "to revere — as in 존귀, 존엄"),
                        ("重", "중", "heavy, important — as in 중요, 중시")],
            surfaces=["존중하고"],
        ),
        "신체적": dict(
            hanja="身體的", meaning="physical, of the body",
            characters=[("身體", None, "the body — 身 body, 體 body, form")],
        ),
        "재산적": dict(
            hanja="財産的", meaning="financial, in terms of property",
        ),
        "간주되다": dict(
            hanja="看做되다", meaning="to be regarded as, to be deemed",
            characters=[("看", "간", "to look at — as in 간호사, 간판"),
                        ("做", "주", "to make, to do")],
            surfaces=["간주되어"],
        ),
        "처벌": dict(
            hanja="處罰", meaning="punishment",
            characters=[("處", "처", "to handle — as in 처분, 처우"),
                        ("罰", "벌", "penalty — as in 벌금, 형벌")],
        ),
        "욕설": dict(
            hanja="辱說", meaning="abuse, swearing at someone",
            characters=[("辱", "욕", "to insult, disgrace"),
                        ("說", "설", "to say — as in 설명, 소설")],
        ),
        "협박하다": dict(
            hanja="脅迫하다", meaning="to threaten, to intimidate",
            characters=[("脅", "협", "to threaten — as in 위협"),
                        ("迫", "박", "to press, force — as in 압박, 촉박")],
            surfaces=["협박하는"],
        ),
        "돌보다": dict(meaning="to look after, to care for", surfaces=["돌보지"]),
        "괴롭히다": dict(
            meaning="to torment, to harass",
            notes=["종교적 괴롭힘 “religious persecution” is chapter 31’s "
                   "phrase for what makes a refugee."],
            surfaces=["괴롭히는"],
        ),
        "규정하다": dict(
            hanja="規定하다", meaning="to define, to lay down",
            characters=[("規", "규", "rule — as in 규범, 규칙"),
                        ("定", "정", "to fix — as in 지정, 제정")],
            surfaces=["규정하고"],
        ),
        "요청하다": dict(
            hanja="要請하다", meaning="to request, to ask for",
            characters=[("要", "요", "to require — as in 요건, 요구"),
                        ("請", "청", "to ask — as in 신청, 청첩장")],
            surfaces=["요청하여"],
        ),
        "위자료": dict(
            hanja="慰藉料", meaning="damages for mental suffering, alimony",
            characters=[("慰", "위", "to comfort — as in 위로, 위문"),
                        ("藉", "자", "to rely on, to spread"),
                        ("料", "료", "a fee — as in 과태료, 수수료")],
        ),
        "합의": dict(
            hanja="合意", meaning="agreement, consent",
            characters=[("合", "합", "to join, agree — as in 합격, 결합"),
                        ("意", "의", "intention — as in 의견, 의지")],
        ),
        "협의 이혼": dict(
            hanja="協議離婚", meaning="divorce by agreement",
            characters=[("協議", None, "consultation, mutual agreement — "
                                       "協 to co-operate, 議 to deliberate")],
        ),
        "재판상 이혼": dict(
            hanja="裁判上離婚", meaning="judicial divorce, divorce by trial",
            characters=[("裁判", None, "a trial — chapter 23")],
        ),
        "동의하다": dict(
            hanja="同意하다", meaning="to consent, to agree",
            characters=[("同", "동", "same — as in 동등, 공동"),
                        ("意", "의", "intention — the same 意 as in 합의")],
            surfaces=["동의하지"],
        ),
        "판결": dict(
            hanja="判決", meaning="a ruling, a judgment",
            characters=[("判", "판", "to judge — as in 판단, 재판"),
                        ("決", "결", "to decide — as in 결정, 해결")],
        ),
        "부정하다": dict(
            hanja="不貞하다", meaning="to be unfaithful",
            characters=[("不", "부", "not — as in 부당, 부적합"),
                        ("貞", "정", "chastity, fidelity")],
            notes=["부정한 행위 is the legal term for adultery. Not the 부정 of "
                   "부정 선거, which is 不正 “irregular”."],
            surfaces=["부정한"],
        ),
        "행위": dict(
            hanja="行爲", meaning="an act, conduct",
            characters=[("行", "행", "to act — as in 행동, 시행"),
                        ("爲", "위", "to do, for the sake of — as in 위하다")],
        ),
        "이행하다": dict(
            hanja="履行하다", meaning="to carry out, to perform (a duty)",
            characters=[("履", "리", "to tread, to fulfil"),
                        ("行", "행", "to act — the same 行 as in 행위")],
            surfaces=["이행하지"],
        ),
        "명령하다": dict(
            hanja="命令하다", meaning="to order, to command",
            characters=[("命", "명", "life, an order — as in 생명, 수명"),
                        ("令", "령", "a command — as in 법령, 영장")],
            surfaces=["명령할"],
        ),
        "가정법원": dict(
            hanja="家庭法院", meaning="the family court",
            characters=[("家庭", None, "the home, the family"),
                        ("法院", None, "a court — chapter 23")],
        ),
        "요구하다": dict(
            hanja="要求하다", meaning="to demand, to ask for",
            characters=[("要", "요", "to require — as in 요건, 요청"),
                        ("求", "구", "to seek — as in 추구, 구직")],
            surfaces=["요구할"],
        ),
        "제한되다": dict(
            hanja="制限되다", meaning="to be limited, restricted",
            characters=[("制", "제", "to control — as in 제도, 규제"),
                        ("限", "한", "a limit — as in 기한, 한계")],
            surfaces=["제한된"],
        ),
        "허용되다": dict(
            hanja="許容되다", meaning="to be allowed, permitted",
            characters=[("許", "허", "to allow — as in 허가, 허락"),
                        ("容", "용", "to contain, accept — as in 내용, 수용")],
            surfaces=["허용된다"],
        ),
        "지급하다": dict(
            hanja="支給하다", meaning="to pay, to disburse",
            characters=[("支", "지", "to pay out, support — as in 지원, 지출"),
                        ("給", "급", "to give — as in 발급, 공급")],
            surfaces=["지급해야"],
        ),
        "양육비": dict(
            hanja="養育費", meaning="child support",
            characters=[("養育", None, "raising a child"),
                        ("費", "비", "expense — as in 생활비, 학비")],
        ),
        "불구하다": dict(
            hanja="不拘하다", meaning="notwithstanding, despite",
            notes=["Always as ~에도 불구하고 “in spite of”."],
            surfaces=["불구하고"],
        ),
        "이행 명령": dict(
            hanja="履行命令", meaning="an enforcement order",
            notes=["An order from the family court to pay what the ruling "
                   "requires; ignoring it three times brings a fine."],
        ),
        "내리다": dict(
            meaning="to hand down (a ruling, an order)",
            surfaces=["내렸는데도"],
        ),
        "교도소": dict(
            hanja="矯導所", meaning="a prison",
            characters=[("矯", "교", "to correct, straighten"),
                        ("導", "도", "to guide — as in 지도, 인도적"),
                        ("所", "소", "a place — as in 사무소, 주소")],
        ),
        "갇히다": dict(meaning="to be shut in, to be held", surfaces=["갇힐"]),
        "국제결혼": dict(
            hanja="國際結婚", meaning="an international marriage",
            characters=[("國際", None, "international — as in 국제법"),
                        ("結婚", None, "marriage")],
        ),
        "전적": dict(
            hanja="全的", meaning="entire, wholly",
            characters=[("全", "전", "whole — as in 전국, 안전"),
                        ("的", "적", "the adjective suffix")],
        ),
        "연장하다": dict(
            hanja="延長하다", meaning="to extend, to prolong",
            characters=[("延", "연", "to stretch, delay — as in 연기"),
                        ("長", "장", "long — as in 장기, 장관")],
            surfaces=["연장해주었다"],
        ),
        "대법원": dict(
            hanja="大法院", meaning="the Supreme Court",
            characters=[("大", "대", "great — as in 대통령, 대학"),
                        ("法院", None, "a court")],
            notes=["Chapter 23’s subject: the courts and what they do."],
        ),
        "판결하다": dict(
            hanja="判決하다", meaning="to rule, to give judgment",
            surfaces=["판결하였다"],
        ),
        "이르다": dict(
            meaning="to reach, to come to",
            notes=["이혼에 이르기까지 “up to reaching divorce”."],
            surfaces=["이르기까지"],
        ),
        "전혀": dict(meaning="not at all, entirely (with a negative)"),
        "제한하다": dict(
            hanja="制限하다", meaning="to limit, to restrict",
            surfaces=["제한한다면"],
        ),
        "평가되다": dict(
            hanja="評價되다", meaning="to be judged, to be rated",
            characters=[("評", "평", "to appraise — as in 평가, 상품평"),
                        ("價", "가", "value, price — as in 가격, 물가")],
            surfaces=["평가된다"],
        ),
    },

    extraNotes=[
        "The four 생각해 봅시다 photographs on p. 174 (a ring, an invitation, a "
        "wedding dress, a bouquet) are set as labels with a caption; the "
        "photographs themselves are not reproduced.",
        "The photo-zone picture on p. 175, the couple illustration, the "
        "police poster on p. 176, the family court on p. 176 and the "
        "이주여성 인권 poster on p. 177 are not reproduced; their captions are.",
        "The review gaps on p. 177 are blank in the book and left blank here.",
    ],
)
