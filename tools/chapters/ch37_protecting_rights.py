# -*- coding: utf-8 -*-
"""Chapter 37 — Protecting rights, and the law.

Transcribed from the photos of pp. 190-193. Your English glosses on pp. 190
and 191 are carried as the entries for the words they sit over.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, LABELS,
               TABLE, CELL, CHART, GLOSSARY)

CHAPTER = dict(
    number=37, slug="37-protecting-rights",
    unit="법", title="권리 보호와 법", titleEn="Protecting rights and the law",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 2019년 {국가인권위원회}가 ‘세계 이주민의 날’을 맞아 발표한 이주민 정책 10대 "
                  "가이드 라인입니다.",
                  "Below are the ten guidelines on policy for migrants that "
                  "the National Human Rights Commission published in 2019 to "
                  "mark International Migrants Day."),
        LABELS("1. 평등과 존중", "2. 권리구제 접근", "3. 난민 인권", "4. 노동할 권리",
               "5. 취약노동자 보호", "6. 의료 서비스", "7. 사회보장보호", "8. 아동 최우선",
               "9. 이주여성 인권", "10. 구금 최소화"),
        FIGURE("10대 인권가이드라인 그림 열 칸"),
        HEADING(4, "01 각 그림에서 이주민에게 {보장하려는|보장하다} 권리는 무엇입니까?",
                translation="What right does each picture set out to "
                            "guarantee migrants?"),
        HEADING(4, "02 이주민의 권리 보호를 위한 한국의 정책 중에서 가장 잘되는 부분과 그렇지 않은 부분은 "
                   "무엇입니까?",
                translation="Of Korea’s policies for protecting migrants’ "
                            "rights, which parts work best and which do not?"),

        SECTION("goals", "학습목표"),
        BULLET("{재판}을 통한 {분쟁} 해결 과정을 설명할 수 있다.", ordered=True,
               translation="Explain how a dispute is resolved through a "
                           "trial."),
        BULLET("재판 외에 분쟁을 해결하고 권리를 보장하는 다양한 {제도}를 설명할 수 있다.", ordered=True,
               translation="Explain the various arrangements, other than a "
                           "trial, that resolve disputes and secure rights."),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"],
              [["기본", "법", "33. 가족과 법", "가정법원을 통한 가족 문제 해결"],
               [CELL("심화", down=2), "법", "36. 범죄와 법", "법집행기관을 통한 범죄 예방 및 권리 보호"],
               ["법", "19. 직장생활과 법", "국가인권위원회를 통한 근로자 보호"]]),

        SECTION("part", "01 재판은 분쟁 해결에 어떤 도움을 줄까?"),
        GLOSSARY(("분쟁", "사람이나 집단들 간에 문제가 일어나서 다투는 것", "분쟁",
                  "a dispute, a conflict"),
                 ("당사자", "어떤 일에 직접 관계된 사람이나 기관", "당사자",
                  "the person directly involved")),
        HEADING(2, "재판을 통한 분쟁 해결", translation=
                "Resolving a dispute through a trial" "\n\n"
                "A foreigner living in Korea may come into dispute with "
                "someone. It is well if that is settled amicably, but where "
                "it is not one can have the help of the law." "\n\n"
                "The chief way of resolving a dispute and protecting one’s "
                "rights through the law is a lawsuit. A lawsuit means asking "
                "a court for a ruling. Where a dispute has arisen between "
                "individuals over property or family matters, the parties can "
                "ask the court to try it. And where an individual has been "
                "harmed by an act of the state, or judges that they have been "
                "made to pay excessive taxes, the party harmed can bring a "
                "suit even against the state. In such a case the judge of the "
                "court hears the parties’ arguments and resolves the dispute "
                "by giving a ruling according to the law."),
        PARAGRAPH("외국인이 한국에서 살면서 다른 사람과 {분쟁}을 겪을 수도 있다. 그것이 "
                  "{원만하게|원만하다} 잘 해결되면 좋지만 그렇지 않을 경우에는 법의 도움을 받을 수 있다."),
        PARAGRAPH("법을 통해 분쟁을 해결하고 권리를 보호하는 대표적인 방법은 {소송}이다. 소송은 {법원}에 "
                  "{판결}을 요구하는 것을 가리킨다. 개인 간의 재산 문제나 가족 문제로 분쟁이 발생한 경우 "
                  "{당사자}는 법원에 {재판}해 달라고 요청할 수 있다. 또한, 국가의 {행위}로 인해 개인이 "
                  "피해를 입거나 세금 등을 지나치게 많이 내게 되었다고 판단되면 피해 당사자가 국가를 "
                  "{상대로}도 소송을 {제기할|제기하다} 수 있다. 이 경우 법원의 {판사}는 당사자들의 "
                  "{주장}을 듣고 법에 따라 판결을 {내려|내리다} 분쟁을 해결한다."),
        FIGURE("법원의 모습(scourt.go.kr)"),

        GLOSSARY(("중위소득",
                  "전체 가구의 소득액을 순서대로 늘어놓았을 때 중간에 위치한 소득액을 말함. 중위소득은 가족 "
                  "구성원 수에 따라 달라지는데 2020년 4인 가구의 기준 중위소득은 4,749,174원임",
                  "중위소득", "the median income")),
        HEADING(2, "약자들을 위한 법률 지원: 대한법률구조공단", translation=
                "Legal support for the weaker party: the Korea Legal Aid "
                "Corporation" "\n\n"
                "It is generally not easy for an individual to prepare for a "
                "trial alone, so people rely a great deal on the help of a "
                "legal expert such as a lawyer. The cost of that can be a "
                "heavy burden, and it is then worth having the help of the "
                "Korea Legal Aid Corporation. The Corporation provides every "
                "kind of legal service for those in financial difficulty or "
                "who do not know the law well. Anyone can receive legal "
                "advice, advice on a trial and representation in a suit there "
                "free of charge. A foreigner living in Korea can have the "
                "Corporation’s help too. For that, one obtains proof of alien "
                "registration through the immigration office, a city, county "
                "or district office, or a community service centre. And where "
                "one’s income is below a certain level (125% of the median "
                "income), a civil or criminal case can be supported free of "
                "charge, or at a minimum cost of about a fifth of the "
                "lawyers’ fee scale the Supreme Court sets. To prove one’s "
                "income, papers such as a health insurance certificate or a "
                "receipt for earned income tax withholding will do."),
        PARAGRAPH("일반적으로 개인이 혼자서 재판을 준비하기는 쉽지 않으므로 {변호사}와 같은 "
                  "{법률전문가}의 도움을 많이 받는다. 그런데 이 경우 비용이 큰 {부담}이 될 수 있는데 이때 "
                  "{대한법률구조공단}의 도움을 받으면 좋다. 대한법률구조공단은 경제적으로 어렵거나 법을 잘 "
                  "모르는 사람들을 위해 {각종} 법률 서비스를 제공한다. 이곳에서는 누구나 무료로 법률 상담, "
                  "재판 상담, 소송 {대리} 등의 지원을 받을 수 있다. 특히 한국에 거주하는 외국인도 "
                  "대한법률구조공단의 도움을 받을 수 있다. 이를 위해서는 출입국·외국인청 또는 각 지역의 "
                  "시·군·구청 또는 행정복지센터를 통해 외국인등록 {사실증명}을 받으면 된다. 또한 소득이 일정 "
                  "{수준}({중위소득} 125%) 이하인 경우에는 {민형사} 사건의 경우 무료 또는 대법원이 정한 "
                  "변호사 {보수} 규칙의 약 5분의 2 정도에 {해당하는|해당하다} 최소 비용으로 소송을 지원받을 "
                  "수 있다. 소득 증명을 위해서는 건강보험증이나 {근로소득원천징수영수증} 등의 서류를 "
                  "{챙기면|챙기다} 된다."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "외국인의 공정한 재판을 위한 통번역 지원", translation=
                "Interpreting and translation support for a fair trial for "
                "foreigners" "\n\n"
                "A foreigner may not receive a proper ruling because "
                "communication in the language does not go smoothly during "
                "the trial. It sometimes happens that the outcome of a trial "
                "is voided after a criminal trial on the ground that the "
                "interpreting and translation support was inadequate. The "
                "National Court Administration is therefore working with the "
                "Hankuk University of Foreign Studies to run a certification "
                "assessment for court interpreters, so as to provide "
                "foreigners with interpreting and translation of a high "
                "standard. Through good interpreting and translation, "
                "foreigners’ right to a fair trial is expected to be better "
                "secured. Further details can be found on the Korean courts’ "
                "website (www.scourt.go.kr)."),
        PARAGRAPH("외국인의 경우 재판 과정에서 언어 소통이 {원활하지|원활하다} 않아 제대로 된 판결을 받지 못할 "
                  "수 있다. {형사 재판} 이후에 {통번역} 인력 지원이 제대로 되지 않았다는 이유로 재판 결과가 "
                  "{무효}가 되는 일이 종종 벌어지기도 한다. 이에 {법원행정처}에서는 한국외국어대학교와 "
                  "{협력하여|협력하다} 외국인에게 높은 수준의 통번역 서비스를 제공하기 위해 {법정 통역인} "
                  "{인증평가}를 실시하고 있다. 수준 높은 통번역 서비스를 통해 외국인이 {공정한|공정하다} "
                  "재판을 받을 권리도 더욱 잘 보장될 것으로 {기대된다|기대되다}. 관련 내용은 대한민국 법원 "
                  "누리집(www.scourt.go.kr)을 통해 확인할 수 있다."),
        CHART("늘어나는 외국인 피고인(단위: 명) — 1심 접수기준", "명",
              [["2012년", 3243],
               ["2013년", 3563],
               ["2014년", 3789],
               ["2015년", 4729],
               ["2016년", 4786],
               ["2017년", 4489]]),
        SOURCE("[자료] 대법원"),

        SECTION("part", "02 재판 외에 분쟁을 해결하는 방법에는 어떤 것이 있을까?"),
        GLOSSARY(("제3자", "해당 문제의 직접적인 당사자 외의 사람", "제3자"),
                 ("자문", "전문가에게 어떤 일을 더 잘 처리하는 방법을 물어보는 것", "자문")),
        HEADING(2, "대안적 분쟁 해결 제도", translation=
                "Alternative dispute resolution" "\n\n"
                "Not every dispute has to be resolved through a trial. That "
                "is because a trial takes a great deal of time and money, so "
                "that the process itself can be a great hardship for the "
                "parties. Korea has arrangements in place for resolving a "
                "dispute without going as far as a trial. They include "
                "negotiation, where the parties agree voluntarily and settle "
                "by talking; mediation, where a third party takes part and "
                "offers advice or counsel; and arbitration, where a third "
                "party is given full authority and settles the matter "
                "bindingly."),
        PARAGRAPH("모든 분쟁을 재판을 통해 해결할 필요는 없다. 왜냐하면 재판에는 많은 시간과 비용이 들기 "
                  "때문에 재판 과정 자체가 당사자들에게 큰 고통이 될 수도 있기 때문이다. 한국에서는 재판까지 "
                  "가지 않고도 분쟁을 해결할 수 있는 제도를 마련해 두고 있다. 여기에는 당사자들이 "
                  "{자발적}으로 합의하고 대화로 해결하는 {협상}, {제3자}가 참여하여 {조언}이나 {자문}을 "
                  "제공하는 {조정}, 그리고 제3자가 모든 권한을 {부여받아|부여받다} 강제로 해결하는 {중재}가 "
                  "있다."),

        GLOSSARY(("구제", "부당하게 피해를 입은 사람의 권리나 이익을 회복하도록 하는 일", "구제"),
                 ("권고", "어떤 행위를 하도록 권하는 것", "권고"),
                 ("부패", "지위에 따른 권한과 영향력을 부당하게 사용하여 사회질서에 반하여 자신의 이익을 "
                          "취하는 것", "부패")),
        HEADING(2, "권리를 보호해 주는 다양한 기관", translation=
                "The bodies that protect rights" "\n\n"
                "Korea runs a number of bodies for the protection of people’s "
                "rights besides the courts." "\n\n"
                "The National Human Rights Commission is an independent state "
                "body for protecting everyone’s basic human rights. Someone "
                "whose human rights have been violated can ask the Commission "
                "for advice, an investigation, a remedy and so on. Where the "
                "Commission judges that a violation has occurred, it "
                "recommends that the party who violated the rights put the "
                "matter right." "\n\n"
                "The Anti-Corruption and Civil Rights Commission is a body "
                "whose purpose is preventing corruption, protecting people’s "
                "rights and interests, and providing remedies. Someone harmed "
                "by a state body can raise the matter with the Commission and "
                "ask for a remedy for the harm they have suffered." "\n\n"
                "There are also bodies that protect the rights of immigrants "
                "and foreigners. The foreigner support centres in each area "
                "help immigrants and foreigners adapt to Korean society and "
                "give advice on harm or disadvantage met with in life in "
                "Korea, and help with bringing a suit. Beyond those, asking "
                "at a public body such as the local community service centre, "
                "or at a civic organisation, will get one basic help."),
        PARAGRAPH("한국에서는 법원 외에도 국민의 권리 보호를 위해 여러 기관을 운영하고 있다."),
        PARAGRAPH("{국가인권위원회}는 모든 사람들의 기본적인 {인권}을 보호하기 위한 {독립된|독립되다} "
                  "국가기관이다. {인권침해}를 당한 사람은 국가인권위원회에 상담이나 {조사}, {구제} 등을 "
                  "요청할 수 있다. 국가인권위원회는 인권침해 사실이 있다고 판단하면 인권을 "
                  "{침해한|침해하다} 당사자에게 문제를 {개선하도록|개선하다} {권고}한다."),
        PARAGRAPH("{국민권익위원회}는 {부패} {방지}와 국민의 {권익} 보호, 권리 구제를 목적으로 하는 "
                  "기관이다. 국가기관에 의해 피해를 입은 국민은 국민권익위원회에 문제를 {제기할|제기하다} 수 "
                  "있으며 자신이 입은 피해를 구제해 달라고 요청할 수 있다."),
        PARAGRAPH("{이민자}나 외국인의 권리를 보호해 주는 기관들도 있다. 각 지역에 있는 {외국인 지원센터}에서는 "
                  "이민자나 외국인의 한국 사회 적응을 돕고, 한국 생활 중 겪은 피해나 {불이익}에 대한 상담, "
                  "소송 {진행}에 도움을 준다. 그 외에도 각 지역에 있는 행정복지센터와 같은 공공 기관이나 "
                  "{시민단체} 등에 {문의하면|문의하다} 기본적인 도움을 받을 수 있다."),
        FIGURE("국민권익위원회 블로그 — ‘정부, 생활 속 반칙과 특권 근절을 위한 9개 중점과제 이행점검’"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "외국인을 위한 마을 변호사 제도를 이용해 보세요", translation=
                "Try the village lawyer scheme for foreigners" "\n\n"
                "Korea runs a village lawyer scheme to resolve local "
                "residents’ legal difficulties and protect their rights. The "
                "village lawyer scheme for foreigners in particular began in "
                "2015, and since 2017 it has been extended to every foreigner "
                "staying in the country. Ringing the 1345 call centre lets a "
                "foreigner take legal advice free of charge. Interpreting is "
                "provided in more than twenty languages, so a foreigner can "
                "get help easily."),
        PARAGRAPH("한국에서는 지역 주민들의 법적 어려움 해결과 권리 보호를 위해 {마을 변호사} 제도를 운영하고 "
                  "있다. 특히 2015년부터는 외국인을 위한 마을 변호사 제도가 {시행되었고|시행되다}, "
                  "2017년부터는 국내에 체류하고 있는 모든 외국인을 대상으로 {확대} 운영되고 있다. 1345 "
                  "콜센터로 전화하면 외국인이 무료로 법률 상담을 받을 수 있다. 20여 개 언어로 {통역} 서비스를 "
                  "제공하고 있기 때문에 외국인도 쉽게 도움을 받을 수 있다."),
        FIGURE("‘외국인을 위한 마을변호사를 만나보세요 1345’ 홍보물"),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 재판은 분쟁 해결에 어떤 도움을 줄까?"),
        BULLET("법을 통해 분쟁을 해결하고 권리를 보호하는 대표적인 방법은 소송이다. 소송은 (        )에 "
               "분쟁에 대한 판결을 요구하는 것을 가리킨다."),
        BULLET("일반적으로 개인이 혼자서 재판을 준비하기는 어려우므로 (        )와 같은 법률전문가의 도움을 "
               "받는 것이 좋다."),
        BULLET("재판과 관련한 비용이 많이 들기 때문에 경제적 형편이 어려운 경우 (                )을 통해 "
               "무료로 도움을 받을 수 있다."),
        HEADING(3, "02 재판 외에 분쟁을 해결하는 방법에는 어떤 것이 있을까?"),
        BULLET("한국에서는 재판까지 가지 않고 분쟁을 해결하도록 돕는 대안적 분쟁 해결 제도를 마련해 두고 "
               "있다. 예를 들면 당사자들이 합의하고 대화로 해결하는 (        ), 제3자가 조언하는 조정, "
               "제3자가 강제로 해결하는 중재가 있다."),
        BULLET("(            )는 모든 사람들의 기본적인 인권을 보호하기 위한 독립된 국가기관이다."),
        BULLET("(            )는 부패 방지와 국민의 권익 보호, 권리 구제를 위한 활동을 수행한다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "한국말이 서툴러도 119 도움을 받을 수 있어요", translation=
                "You can have the help of 119 even if your Korean is halting" "\n\n"
                "In January 2019 A, a migrant worker from Bangladesh working "
                "in an area of Gyeonggi-do, suddenly collapsed with a heart "
                "problem. But their colleagues, whose Korean was halting, "
                "could not call 119 for emergency rescue, and A died in the "
                "end." "\n\n"
                "For people who find reporting by voice difficult, foreigners "
                "among them, 119 reports can now be made by video, text, app "
                "and the web as well. One can make a video call to 119, for "
                "instance, or send a text message to report. One can also "
                "download the 119 reporting app to a smartphone, or go to "
                "119.go.kr and enter the details of the report."),
        PARAGRAPH("2019년 1월 경기 한 지역에서 일하던 방글라데시 출신 {이주노동자} A씨가 심장에 문제가 생겨 "
                  "갑자기 {쓰러졌다|쓰러지다}. 하지만 한국말이 {서툴렀던|서투르다} {동료}들은 119 "
                  "{응급 구조}를 요청하지 못했고 결국 A씨는 끝내 {숨지고|숨지다} 말았다."),
        PARAGRAPH("이처럼 외국인을 비롯하여 {음성}으로 신고하는 것이 어려운 사람들을 위해 최근에는 119 신고 "
                  "{접수} 처리를 {영상}, 문자, 앱, 웹을 통해서도 할 수 있도록 했다. 예를 들어 119로 "
                  "{영상통화}를 하거나 문자 메시지를 보내서 신고할 수 있게 된 것이다. 또한 스마트폰으로 119 "
                  "{신고앱}을 {다운받을|다운받다} 수도 있으며, 119.go.kr에 {접속한|접속하다} 후 신고 내용을 "
                  "{입력하는|입력하다} 것도 가능하다."),
        FIGURE("‘119 신고 이렇게도 가능합니다!’ 홍보물"),
        PARAGRAPH("★ 외국인으로서 어려움을 당했을 때 도움을 받을 수 있는 한국의 기관이나 제도에 대해 말해 "
                  "봅시다. 어떤 부분이 더 필요하거나 개선되어야 하는지 말해 봅시다.",
                  "Talk about the Korean bodies and arrangements one can turn "
                  "to for help when a foreigner meets difficulty. Say what "
                  "more is needed, or what should be put right."),
    ],

    extraAnnotations={
        "국가인권위원회": dict(
            hanja="國家人權委員會",
            meaning="the National Human Rights Commission",
            characters=[("人權", None, "human rights"),
                        ("委員會", None, "a commission, a committee")],
            notes=["An independent state body. Chapter 21’s 이야기 나누기 has a "
                   "briefing held there."],
        ),
        "보장하다": dict(
            hanja="保障하다", meaning="to guarantee, to secure",
            characters=[("保", "보", "to protect — as in 보호, 보험"),
                        ("障", "장", "a barrier, to shield")],
            surfaces=["보장하려는"],
        ),
        "재판": dict(
            hanja="裁判", meaning="a trial",
            characters=[("裁", "재", "to judge, to cut — as in 중재, 제재"),
                        ("判", "판", "to judge — as in 판결, 판사")],
        ),
        "분쟁": dict(
            hanja="紛爭", meaning="a dispute, a conflict",
            characters=[("紛", "분", "confused, tangled"),
                        ("爭", "쟁", "to contend — as in 경쟁, 논쟁")],
        ),
        "제도": dict(
            hanja="制度", meaning="a system, an arrangement",
            characters=[("制", "제", "to control — as in 제재, 규제"),
                        ("度", "도", "a degree, a measure — as in 한도, 정도")],
        ),
        "원만하다": dict(
            hanja="圓滿하다", meaning="to be amicable, smooth",
            characters=[("圓", "원", "round — as in 원형"),
                        ("滿", "만", "full — as in 만족, 충만")],
            notes=["The page prints 원만하게; 원만히 is the more usual adverb."],
            surfaces=["원만하게"],
        ),
        "소송": dict(
            hanja="訴訟", meaning="a lawsuit",
            characters=[("訴", "소", "to sue — as in 기소, 고소"),
                        ("訟", "송", "to litigate")],
        ),
        "법원": dict(
            hanja="法院", meaning="a court",
            characters=[("法", "법", "law"),
                        ("院", "원", "an institution — as in 병원, 대법원")],
        ),
        "판결": dict(
            hanja="判決", meaning="a ruling, a judgment",
            characters=[("判", "판", "to judge — as in 판사, 재판"),
                        ("決", "결", "to decide — as in 결정, 해결")],
        ),
        "당사자": dict(
            hanja="當事者", meaning="the party directly involved",
            characters=[("當", "당", "the said — as in 해당, 정당"),
                        ("事", "사", "a matter — as in 사건, 검사"),
                        ("者", "자", "person")],
        ),
        "행위": dict(
            hanja="行爲", meaning="an act, conduct",
            characters=[("行", "행", "to act — as in 행동, 시행"),
                        ("爲", "위", "to do, for")],
        ),
        "상대로": dict(
            hanja="相對로", meaning="against (someone), vis-à-vis",
            characters=[("相對", None, "the other side — 相 mutual, 對 facing")],
            notes=["국가를 상대로 소송을 제기하다 “to bring a suit against the "
                   "state”."],
        ),
        "제기하다": dict(
            hanja="提起하다", meaning="to bring (a suit), to raise (an issue)",
            characters=[("提", "제", "to put forward — as in 제출, 제안"),
                        ("起", "기", "to raise — as in 기소, 기상")],
            surfaces=["제기할"],
        ),
        "판사": dict(
            hanja="判事", meaning="a judge",
            characters=[("判", "판", "to judge"),
                        ("事", "사", "a matter — as in 검사, 사건")],
        ),
        "주장": dict(
            hanja="主張", meaning="an argument, a contention",
            characters=[("主", "주", "main — as in 주인, 주체"),
                        ("張", "장", "to stretch — as in 확장, 긴장")],
        ),
        "내리다": dict(
            meaning="to hand down (a ruling)",
            surfaces=["내려"],
        ),
        "변호사": dict(
            hanja="辯護士", meaning="a lawyer, an advocate",
            characters=[("辯", "변", "to argue, to plead — as in 변명, 변론"),
                        ("護", "호", "to protect — as in 보호, 간호"),
                        ("士", "사", "a qualified person — as in 공인중개사")],
        ),
        "법률전문가": dict(
            hanja="法律專門家", meaning="a legal expert",
            characters=[("法律", None, "law"),
                        ("專門家", None, "an expert")],
        ),
        "부담": dict(
            hanja="負擔", meaning="a burden",
            characters=[("負", "부", "to carry — as in 부담, 승부"),
                        ("擔", "담", "to bear — as in 담당, 담임")],
        ),
        "대한법률구조공단": dict(
            hanja="大韓法律救助公團",
            meaning="the Korea Legal Aid Corporation",
            characters=[("救助", None, "rescue, aid — 救 to save, 助 to help"),
                        ("公團", None, "a public corporation")],
        ),
        "각종": dict(
            hanja="各種", meaning="every kind of",
            characters=[("各", "각", "each — as in 각자, 각국"),
                        ("種", "종", "a kind — as in 종류, 품종")],
        ),
        "대리": dict(
            hanja="代理", meaning="acting for another, representation",
            characters=[("代", "대", "to replace — as in 대신, 대리운전"),
                        ("理", "리", "to manage — as in 관리, 처리")],
            notes=["소송 대리 is being represented in a suit by a lawyer."],
        ),
        "사실증명": dict(
            hanja="事實證明", meaning="proof of a fact (a certificate)",
            notes=["외국인등록 사실증명 is the certificate showing one is "
                   "registered as a foreigner."],
        ),
        "수준": dict(
            hanja="水準", meaning="a level, a standard",
            characters=[("水", "수", "water — as in 수영, 수도"),
                        ("準", "준", "a level — as in 기준, 표준")],
        ),
        "중위소득": dict(
            hanja="中位所得", meaning="the median income",
            characters=[("中位", None, "the middle position"),
                        ("所得", None, "income — as in 소득세")],
        ),
        "민형사": dict(
            hanja="民刑事", meaning="civil and criminal (cases)",
            characters=[("民", "민", "civil, the people — as in 민법, 국민"),
                        ("刑事", None, "criminal — as in 형사 재판")],
        ),
        "보수": dict(
            hanja="報酬", meaning="remuneration, a fee",
            characters=[("報", "보", "to repay, to report — as in 보고, 정보"),
                        ("酬", "수", "to reward")],
        ),
        "해당하다": dict(
            hanja="該當하다", meaning="to amount to, to correspond to",
            surfaces=["해당하는"],
        ),
        "근로소득원천징수영수증": dict(
            hanja="勤勞所得源泉徵收領收證",
            meaning="a receipt for earned income tax withholding",
            characters=[("勤勞所得", None, "earned income"),
                        ("源泉徵收", None, "withholding at source — 源泉 the "
                                          "source, 徵收 collection"),
                        ("領收證", None, "a receipt")],
        ),
        "챙기다": dict(
            meaning="to get together, to see to (papers)",
            surfaces=["챙기면"],
        ),
        "원활하다": dict(
            hanja="圓滑하다", meaning="to go smoothly, without a hitch",
            characters=[("圓", "원", "round — the same 圓 as in 원만하다"),
                        ("滑", "활", "slippery, smooth")],
            surfaces=["원활하지"],
        ),
        "형사 재판": dict(
            hanja="刑事裁判", meaning="a criminal trial",
        ),
        "통번역": dict(
            hanja="通飜譯", meaning="interpreting and translation",
            characters=[("通譯", None, "interpreting"),
                        ("飜譯", None, "translation")],
        ),
        "무효": dict(
            hanja="無效", meaning="void, of no effect",
            characters=[("無", "무", "without — as in 무국적, 무단"),
                        ("效", "효", "effect — as in 유효 기간")],
        ),
        "법원행정처": dict(
            hanja="法院行政處",
            meaning="the National Court Administration",
            notes=["Chapter 23’s 알아두면 좋아요 has it publishing the legal aid "
                   "guide in sixteen languages."],
        ),
        "협력하다": dict(
            hanja="協力하다", meaning="to co-operate, to work with",
            characters=[("協", "협", "to join in — as in 협의, 협정"),
                        ("力", "력", "strength — as in 노력, 능력")],
            surfaces=["협력하여"],
        ),
        "법정 통역인": dict(
            hanja="法廷通譯人", meaning="a court interpreter",
            characters=[("法廷", None, "a courtroom — 廷 a court, a hall")],
        ),
        "인증평가": dict(
            hanja="認證評價", meaning="a certification assessment",
            characters=[("認證", None, "certification — 認 to recognise, "
                                       "證 evidence"),
                        ("評價", None, "assessment")],
        ),
        "공정하다": dict(
            hanja="公正하다", meaning="to be fair, impartial",
            characters=[("公", "공", "public, impartial — as in 공공, 공인"),
                        ("正", "정", "right — as in 정의, 정당")],
            surfaces=["공정한"],
        ),
        "기대되다": dict(
            hanja="期待되다", meaning="to be expected, hoped for",
            characters=[("期", "기", "a period, to expect — as in 기간, 기대"),
                        ("待", "대", "to wait — as in 우대, 대기")],
            surfaces=["기대된다"],
        ),
        "자발적": dict(
            hanja="自發的", meaning="voluntary, of one’s own accord",
            characters=[("自", "자", "self — as in 자율, 자국"),
                        ("發", "발", "to send out — as in 발생, 발휘")],
        ),
        "협상": dict(
            hanja="協商", meaning="negotiation",
            characters=[("協", "협", "to co-operate — as in 협력, 협의"),
                        ("商", "상", "commerce, to discuss — as in 상가, 상업")],
        ),
        "제3자": dict(
            hanja="第三者", meaning="a third party",
            characters=[("第", "제", "the ordinal prefix — as in 제1편"),
                        ("者", "자", "person")],
        ),
        "조언": dict(
            hanja="助言", meaning="advice",
            characters=[("助", "조", "to help — as in 조수석, 원조"),
                        ("言", "언", "words — as in 언어, 발언")],
        ),
        "자문": dict(
            hanja="諮問", meaning="counsel sought from an expert",
            characters=[("諮", "자", "to consult"),
                        ("問", "문", "to ask — as in 질문, 문의")],
        ),
        "조정": dict(
            hanja="調停", meaning="mediation",
            characters=[("調", "조", "to adjust — as in 조사, 조정"),
                        ("停", "정", "to halt — as in 정지, 정류장")],
            notes=["Chapter 20 has 조정 (調整) for reconciling interests; this "
                   "is the legal 조정, mediation by a third party."],
        ),
        "부여받다": dict(
            hanja="附與받다", meaning="to be given (authority)",
            characters=[("附", "부", "to attach — as in 부착, 부과"),
                        ("與", "여", "to give — as in 수여, 참여")],
            surfaces=["부여받아"],
        ),
        "중재": dict(
            hanja="仲裁", meaning="arbitration",
            characters=[("仲", "중", "to mediate — as in 중개, 중간"),
                        ("裁", "재", "to judge — as in 재판, 제재")],
        ),
        "인권": dict(
            hanja="人權", meaning="human rights",
        ),
        "독립되다": dict(
            hanja="獨立되다", meaning="to be independent",
            characters=[("獨", "독", "alone — as in 독재, 독학"),
                        ("立", "립", "to stand — as in 설립, 확립")],
            surfaces=["독립된"],
        ),
        "인권침해": dict(
            hanja="人權侵害", meaning="a violation of human rights",
        ),
        "조사": dict(
            hanja="調査", meaning="an investigation, a survey",
        ),
        "구제": dict(
            hanja="救濟", meaning="a remedy, relief",
            characters=[("救", "구", "to save — as in 구조, 구급"),
                        ("濟", "제", "to relieve, to cross — as in 경제")],
        ),
        "침해하다": dict(
            hanja="侵害하다", meaning="to violate, to infringe",
            surfaces=["침해한"],
        ),
        "개선하다": dict(
            hanja="改善하다", meaning="to put right, to improve",
            characters=[("改", "개", "to change — as in 개정, 개혁"),
                        ("善", "선", "good — as in 최선")],
            surfaces=["개선하도록"],
        ),
        "권고": dict(
            hanja="勸告", meaning="a recommendation, urging",
            characters=[("勸", "권", "to urge — as in 권장, 권유"),
                        ("告", "고", "to tell — as in 신고, 보고")],
        ),
        "국민권익위원회": dict(
            hanja="國民權益委員會",
            meaning="the Anti-Corruption and Civil Rights Commission",
            characters=[("權益", None, "rights and interests")],
        ),
        "부패": dict(
            hanja="腐敗", meaning="corruption",
            characters=[("腐", "부", "to rot"),
                        ("敗", "패", "to be defeated, to spoil — as in 실패")],
        ),
        "방지": dict(
            hanja="防止", meaning="prevention",
            characters=[("防", "방", "to guard against — as in 예방, 방역"),
                        ("止", "지", "to stop — as in 금지, 정지")],
        ),
        "권익": dict(
            hanja="權益", meaning="rights and interests",
            characters=[("權", "권", "right — as in 권리, 인권"),
                        ("益", "익", "benefit — as in 이익, 국익")],
        ),
        "이민자": dict(
            hanja="移民者", meaning="an immigrant",
            characters=[("移民", None, "migration — 移 to move, 民 people"),
                        ("者", "자", "person")],
        ),
        "외국인 지원센터": dict(
            meaning="a foreigner support centre",
        ),
        "불이익": dict(
            hanja="不利益", meaning="disadvantage, detriment",
            characters=[("不利", None, "unfavourable — 不 not, 利 benefit"),
                        ("益", "익", "benefit")],
        ),
        "진행": dict(
            hanja="進行", meaning="going forward, conducting",
            characters=[("進", "진", "to advance — as in 진학, 진출"),
                        ("行", "행", "to go — as in 행위, 시행")],
        ),
        "시민단체": dict(
            hanja="市民團體", meaning="a civic organisation, an NGO",
            characters=[("市民", None, "citizens"),
                        ("團體", None, "an organisation")],
        ),
        "문의하다": dict(
            hanja="問議하다", meaning="to enquire, to ask",
            characters=[("問", "문", "to ask — as in 질문, 자문"),
                        ("議", "의", "to deliberate — as in 회의, 협의")],
            surfaces=["문의하면"],
        ),
        "마을 변호사": dict(
            meaning="the village lawyer (a free legal advice scheme)",
            notes=["Chapter 7 has a case settled through the 마을변호사 service "
                   "on the 1345 line."],
        ),
        "시행되다": dict(
            hanja="施行되다", meaning="to come into force, to be run",
            surfaces=["시행되었고"],
        ),
        "확대": dict(
            hanja="擴大", meaning="expansion, extension",
            characters=[("擴", "확", "to expand — as in 확산, 확장"),
                        ("大", "대", "great")],
        ),
        "통역": dict(
            hanja="通譯", meaning="interpreting",
            characters=[("通", "통", "to pass, communicate — as in 통과, 소통"),
                        ("譯", "역", "to translate — as in 번역, 통번역")],
        ),
        "이주노동자": dict(
            hanja="移住勞動者", meaning="a migrant worker",
            characters=[("移住", None, "migration — as in 이주민"),
                        ("勞動者", None, "a worker")],
        ),
        "쓰러지다": dict(meaning="to collapse, to fall down",
                       surfaces=["쓰러졌다"]),
        "서투르다": dict(
            meaning="to be poor at, halting",
            notes=["Chapter 7 has 한국말이 서툴러 of migrant workers who cannot "
                   "say what they mean."],
            surfaces=["서툴렀던"],
        ),
        "동료": dict(
            hanja="同僚", meaning="a colleague",
            characters=[("同", "동", "same — as in 동등, 공동"),
                        ("僚", "료", "an official, a colleague")],
        ),
        "응급 구조": dict(
            hanja="應急救助", meaning="emergency rescue",
            characters=[("應急", None, "emergency — 應 to respond, 急 urgent"),
                        ("救助", None, "rescue")],
        ),
        "숨지다": dict(meaning="to die, to pass away", surfaces=["숨지고"]),
        "음성": dict(
            hanja="音聲", meaning="voice, speech",
            characters=[("音", "음", "sound — as in 음악, 발음"),
                        ("聲", "성", "voice — as in 성악, 함성")],
        ),
        "접수": dict(
            hanja="接受", meaning="receipt (of an application or a report)",
            characters=[("接", "접", "to receive, to touch — as in 접속, 접근"),
                        ("受", "수", "to receive — as in 수강, 수여")],
        ),
        "영상": dict(
            hanja="映像", meaning="video, an image",
            characters=[("映", "영", "to project — as in 영화, 상영"),
                        ("像", "상", "an image — as in 초상, 인상")],
        ),
        "영상통화": dict(
            hanja="映像通話", meaning="a video call",
        ),
        "신고앱": dict(meaning="the reporting app"),
        "다운받다": dict(meaning="to download", surfaces=["다운받을"]),
        "접속하다": dict(
            hanja="接續하다", meaning="to connect, to go to (a site)",
            characters=[("接", "접", "to touch — the same 接 as in 접수"),
                        ("續", "속", "to continue — as in 계속, 지속")],
            surfaces=["접속한"],
        ),
        "입력하다": dict(
            hanja="入力하다", meaning="to enter, to input",
            characters=[("入", "입", "to enter — as in 입국, 입원"),
                        ("力", "력", "force — as in 노력, 능력")],
            surfaces=["입력하는"],
        ),
    },

    extraNotes=[
        "The ten guideline pictures on p. 190 are set as labels with their "
        "numbers, as the book prints them; the pictures themselves are not "
        "reproduced.",
        "The courtroom photograph on p. 191, the 국민권익위원회 blog card on "
        "p. 192, the 마을변호사 poster and the 119 poster on p. 193 are not "
        "reproduced; their captions are.",
        "The 외국인 피고인 figure on p. 191 is set as a chart; the book counts "
        "cases received at first instance.",
        "The review gaps on p. 193 are blank in the book and left blank here.",
    ],
)
