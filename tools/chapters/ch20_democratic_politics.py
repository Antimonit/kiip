# -*- coding: utf-8 -*-
"""Chapter 20 — Democratic politics in Korea.

No Google Doc: yours stop at chapter 12. Transcribed from the photos of
pp. 110-113, so the Korean here is my reading of the page rather than yours,
and any error in it is mine.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, VERSE,
               TABLE, CELL, GLOSSARY)

CHAPTER = dict(
    number=20, slug="20-democratic-politics",
    unit="정치", title="한국의 민주 정치", titleEn="Democratic politics in Korea",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 사회통합프로그램 수업 교실 모습입니다. 학생들이 스마트폰 사용 규칙을 "
          "정하자는 {의견}이 나왔습니다."),
        FIGURE("교실에서 ‘교실 내 스마트폰 사용 찬반 토론’을 하는 모습"),
        HEADING(4, "01 교실에서 스마트폰 사용 관련 규칙은 어떻게 결정하는 것이 좋을까요?"),
        HEADING(4, "02 어떤 {조직}이나 {단체}에서 함께 생활하는 사람과 {갈등}이 생겼을 때, 이를 "
             "{민주적}으로 해결하기 위해서는 어떻게 해야 합니까?"),

        SECTION("goals", "학습목표"),
        BULLET("민주주의와 주권의 의미를 설명할 수 있다.", ordered=True),
        BULLET("권력 분립의 필요성과 방식을 설명할 수 있다.", ordered=True),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", 2), "제목", "관련 내용"],
              [["기본", "정치", "24. 선거와 지방자치", "선거"],
               ["심화", "역사", "7. 민주주의의 발전", "민주주의의 발전 과정"]]),

        SECTION("part", "01 한국의 주인은 누구일까?"),
        HEADING(2, "정치와 민주주의의 의미"),
        GLOSSARY(("선거", "어떤 단체의 대표를 뽑음", "선거"),
              ("통치", "나라나 지역을 다스림", "통치"),
              ("이해관계", "이익과 손해가 걸려 있는 관계", "이해관계"),
              ("민주주의(democracy)", "국민이 권력을 가지고 스스로를 다스린다는 것을 "
                                     "의미하며, 인간의 존엄성, 자유, 평등과 같은 가치를 추구함",
               "민주주의")),
        PARAGRAPH("‘{정치}’하면 무엇이 {떠오르는가|떠오르다}? 누군가는 {선거}를 떠올리고 누군가는 "
          "{대통령}을, 누군가는 법을 떠올릴 수도 있다. 정치는 좁게 보면 국가를 {통치}하는 것을 "
          "가리키므로 선거, 대통령, 법 등과도 {밀접한|밀접하다} 관계가 있다. 한편, 넓은 의미의 "
          "정치는 국가를 {다스리는|다스리다} 일은 물론 일상생활에서 사람들 사이의 서로 다른 "
          "{이해관계}를 {조정}하는 것을 가리킨다. 학교나 회사에서 어떤 규칙을 정하는 것, "
          "지역의 문제 해결을 위해 주민 {회의}를 여는 것 등도 일상생활 속 정치의 모습이다."),
        PARAGRAPH("이러한 정치는 {민주주의}에 맞게 이루어져야 국민을 {이롭게|이롭다} 할 수 있다. 다시 "
          "말해서 국민 사이의 다양한 {의견} 차이를 {민주적}인 방식으로 {좁히고|좁히다} 조정해서 "
          "서로에게 {이익}이 될 수 있도록 하는 것이다. 한국도 과거에는 왕이나 {귀족} 등이 국가의 "
          "일을 {의논}하고 결정했다. 하지만 오늘날은 민주주의의 {원리}에 따라 모든 국민이 "
          "{신분}이나 {재산}, {성별} 등과 관계없이 자유롭게 한국 사회에 대해 다양한 목소리를 "
          "{표출}하고 해결 과정에 참여할 수 있다."),

        HEADING(2, "한국의 주인은 국민"),
        GLOSSARY(("권리", "어떤 일을 하거나 다른 사람에 대하여 당연히 요구할 수 있는 힘이나 자격",
               "권리"),
              ("권력", "다른 사람을 복종시키거나 지배할 수 있는 공식적인 권리와 힘", "권력"),
              ("명시", "분명하게 보여줌", "명시"),
              ("주권", "주인으로서 권리", "주권")),
        PARAGRAPH("{헌법}은 한국의 최고 법으로 한국을 이끌어 가는 기본 {원리}와 국가 기관의 {구성}, "
          "그리고 한국 국민의 기본적인 {권리}와 {의무} 등을 담고 있다. 한국의 헌법 제1조에는 "
          "‘대한민국이 민주주의를 {기반}으로 한 {공화국}이며, 대한민국 국민은 국가의 "
          "{주인}으로서 모든 {권력}의 {뿌리}가 된다.’는 점을 {명시}하고 있다. 이는 한국에서는 "
          "{특정} 개인이나 {정치인}이 아니라 한국 국민이 {주권}을 가지고 있으며, 국민의 뜻에 "
          "따라 국민을 위한 민주 정치를 하고자 한다는 점을 분명히 한 것으로 볼 수 있다."),
        VERSE("대한민국헌법 제1장 제1조",
              "① 대한민국은 {민주공화국}이다.",
              "② 대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다."),
        FIGURE("한국의 헌법 제1조"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "한국 민주주의 발전에 큰 영향을 준 사건"),
        BULLET("{4·19혁명}(1960년): 3.15 {부정 선거}에 대한 {반발}로 일어난 학생과 시민들의 "
          "{시위}로 {이승만} 대통령이 대통령 자리에서 {물러남|물러나다}."),
        BULLET("{5·18 민주화 운동}(1980년): 군인 {세력} {집권} 반대와 민주주의 {회복}에 대한 광주 "
          "시민의 {민주화} 운동으로 시위 과정에서 수많은 광주 시민이 군인들에 의해 "
          "{희생됨|희생되다}."),
        BULLET("{6월 민주 항쟁}(1987년): 대통령 {직선제}, 헌법 {개정} 등을 요구하는 시위가 "
          "{전국적}으로 일어나 결국 대통령 직선제 등의 내용을 담은 헌법이 새로 만들어짐."),
        FIGURE("〈4.19 혁명 당시 남대문 앞의 시위 모습〉"),

        SECTION("part", "02 한국은 왜 국가 기관의 권력을 나누어 놓았을까?"),
        HEADING(2, "권력 분립의 필요성"),
        GLOSSARY(("궁극적", "어떤 일의 마지막", "궁극적"),
              ("기여", "도움이 되도록 함", "기여")),
        PARAGRAPH("국가의 모든 일을 한 사람이 결정한다면 국민의 자유와 권리는 {보장}되기 어렵다. 권력을 "
          "가진 사람이 자신이나 가족, 친구 등에게만 {유리한|유리하다} 결정을 내릴 수도 있다. "
          "따라서 오늘날 한국을 {비롯한|비롯하다} 대부분의 민주주의 국가는 국가 권력이 특정 "
          "개인이나 {집단}에 {집중}되지 않도록 몇 개로 나누어 각각을 {독립}시켜 놓고 있다."),
        PARAGRAPH("국가 권력을 여러 기관이 나누어 갖도록 하는 {원칙}을 ‘{권력 분립}의 원칙’이라고 한다. "
          "한국은 민주주의 {실현}을 위해 국가 권력을 {입법부}(국회), {행정부}(정부), "
          "{사법부}(법원)로 나누어 놓았다. 국가 권력을 세 개로 {분리}해 놓았다는 의미에서 이를 "
          "‘{삼권 분립}’이라고도 한다. 이처럼 권력을 몇 개로 분리해 놓으면 특정 개인이나 집단이 "
          "국가의 중요한 일을 마음대로 {처리}하기 어렵다. 권력 분립은 {궁극적}으로 국민의 권리와 "
          "이익을 보호하는데 {기여}할 수 있다."),

        HEADING(2, "삼권 분립을 통한 권력의 견제와 균형"),
        GLOSSARY(("견제", "상대편이 지나치게 많은 세력을 가지거나 마음대로 행동하지 못하도록 함",
               "견제")),
        PARAGRAPH("국민이 뽑은 대표들이 모인 입법부(국회)에서 만드는 법은 국가를 {운영}하는 기본적인 "
          "규칙이 된다."),
        PARAGRAPH("행정부(정부)는 입법부에서 {제정}한 법에 따라 국민을 위한 다양한 {정책}과 활동을 "
          "{펼친다|펼치다}."),
        PARAGRAPH("사법부(법원)는 입법부가 만든 법을 {해석}하고 {적용}하여 {재판}을 한다."),
        PARAGRAPH("이 세 기관은 각각 다른 두 기관을 {견제}한다. 입법부는 행정부와 사법부의 {고위} "
          "{공무원}이 헌법과 법을 {위반}했을 때 그를 {파면}하도록 {헌법재판소}에 요청할 수 있다. "
          "행정부의 대통령은 입법부가 만든 {법안}을 {거부}할 수 있다. 사법부는 국회에서 만든 "
          "법안이 헌법에 위반되는지 {여부}를 {판단}해 달라고 헌법재판소에 요청할 수 있다."),
        PARAGRAPH("이와 같은 방식으로 입법부, 행정부, 사법부는 어느 한쪽이 권력을 {함부로} 사용하지 못 "
          "하도록 견제하면서 {균형}을 이룰 수 있도록 하였다."),
        TABLE(["기관", "하는 일"],
              [["입법부(국회)", "법률 {제정}"],
               ["행정부(정부)", "법률 {집행}"],
               ["사법부(법원)", "법률 {적용}"]]),
        FIGURE("한국의 권력 분립 — 국민을 가운데 두고 입법부·행정부·사법부가 서로를 견제하는 그림"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "민주 정치의 반대말은 무엇일까?"),
        PARAGRAPH("{독재} 정치는 민주 정치의 반대말이다. 독재는 어떤 개인이나 단체 등이 모든 권력을 "
          "{차지}하고 일을 마음대로 처리하는 것이다. 한국에서도 독재 정치가 이루어진 시기가 "
          "있었다. 일부 대통령들은 {대통령직}을 오래 유지하기 위한 과정에서 또는 {정권}을 얻기 "
          "위한 과정에서 {불법}이나 {폭력}을 이용하기도 했다. 그로 인해 많은 사람이 "
          "{억압당하고|억압당하다} 희생되었다는 점에서 독재 정치는 {비판}을 받는다."),
        SOURCE("[출처] 천재학습백과 초등 사회 용어사전, 천재교육."),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 한국의 주인은 누구일까?"),
        BULLET("넓은 의미의 (        )는 일상생활에서 사람들 사이의 서로 다른 {이해관계}를 {조정}하는 "
          "것이다."),
        BULLET("오늘날 한국에서는 (        ) {원리}에 따라 모든 국민이 차별 없이 자유롭게 한국 사회에 "
          "대해 다양한 목소리를 {표출}하고 해결 과정에 참여할 수 있다."),
        BULLET("한국에서는 {특정} 개인이나 {정치인}이 아니라 한국 국민이 (        )을 가지고 있다."),
        HEADING(3, "02 한국은 왜 국가 기관의 권력을 나누어 놓았을까?"),
        BULLET("한국은 {민주주의} {실현}을 위해서 국가 {권력}을 (        ), (        ), (        )으로 "
          "나누어 놓았다."),
        BULLET("국가 권력을 여러 기관으로 나누는 것을 (        ) {원칙}이라고 한다. 한국은 국가 권력을 "
          "세 개로 {분리}해 놓았다는 점에서 (        )이라고도 한다."),
        BULLET("{입법부}는 국가 {운영}의 기본이 되는 법을 (        )하고 {행정부}는 법에 따라 {정책}을 "
          "(        )하며 {사법부}는 법을 {해석}하고 (        )하여 {재판}을 한다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "일상생활과 민주주의"),
        TABLE(["가정에서", "학교에서"],
              [["가정에서 중요한 결정이 필요할 때, 가족회의를 개최하고 다수결의 원칙에 따라서 "
                "결정을 한다.",
                "학교에서 학급의 반장을 뽑는 반장 선거를 한다."]]),
        PARAGRAPH("★ 일상생활에서도 민주주의를 적용할 수 있는 예를 생각해 봅시다."),
    ],

    english={
        "정치와 민주주의의 의미": dict(
            title="What politics and democracy mean",
            paragraphs=[
                "What comes to mind at the word 정치? For one person an "
                "election, for another the president, for another the law. "
                "Politics narrowly means the governing of a country, so it "
                "does bear closely on elections, on the president and on the "
                "law. In the wider sense, though, politics means the "
                "adjusting of people's differing interests in daily life as "
                "much as the governing of a state. Settling a rule at school "
                "or at work, holding a residents' meeting to solve something "
                "local — those are politics in daily life too.",

                "Politics of that kind can benefit the people only if it is "
                "conducted in accordance with democracy. That is, narrowing "
                "and adjusting the differences of opinion among the people by "
                "democratic means, so that the outcome serves them all. In "
                "Korea too it was once kings and nobles who debated and "
                "decided the affairs of the state. Today, by the principles "
                "of democracy, every citizen may speak freely about Korean "
                "society and take part in resolving its problems, whatever "
                "their standing, their wealth or their sex.",
            ],
        ),
        "한국의 주인은 국민": dict(
            title="Korea belongs to its people",
            paragraphs=[
                "The constitution is Korea's highest law, and holds the "
                "founding principles by which the country is led, the "
                "composition of its organs of state, and the fundamental "
                "rights and duties of its citizens. Article 1 of the Korean "
                "constitution sets down that the Republic of Korea is a "
                "republic founded on democracy, and that its citizens, as the "
                "owners of the state, are the root of all its power. That can "
                "be read as making plain that sovereignty in Korea belongs "
                "not to any particular individual or politician but to the "
                "Korean people, and that the intention is a democratic "
                "politics conducted for them and according to their will.",
            ],
        ),
        "권력 분립의 필요성": dict(
            title="Why power is divided",
            paragraphs=[
                "If one person decided everything a state does, the freedom "
                "and rights of its people would be hard to guarantee. Whoever "
                "held the power might rule only in favour of themselves, "
                "their family and their friends. So most democracies today, "
                "Korea among them, divide state power into several parts and "
                "set each of them independent, to keep it from gathering in "
                "one person or one group.",

                "The principle of having several bodies hold state power "
                "between them is called the separation of powers. To realise "
                "democracy, Korea divides state power into the legislature "
                "(the National Assembly), the executive (the government) and "
                "the judiciary (the courts). Because it is separated into "
                "three, this is also called 삼권 분립. Dividing power in this "
                "way makes it hard for one person or group to deal with the "
                "important affairs of state as they please. In the end it "
                "serves to protect the rights and interests of the people.",
            ],
        ),
        "삼권 분립을 통한 권력의 견제와 균형": dict(
            title="Checks and balance through the three powers",
            paragraphs=[
                "The laws made in the legislature, where the representatives "
                "the people elected are gathered, become the basic rules by "
                "which the state is run.",

                "The executive carries out a range of policies and activities "
                "for the people, according to the laws the legislature has "
                "enacted.",

                "The judiciary interprets and applies the laws the "
                "legislature has made, and holds trials.",

                "Each of the three checks the other two. The legislature may "
                "ask the Constitutional Court to remove a senior official of "
                "the executive or the judiciary who has broken the "
                "constitution or the law. The president, in the executive, "
                "may veto a bill the legislature has made. The judiciary may "
                "ask the Constitutional Court to rule on whether a bill made "
                "in the Assembly runs against the constitution.",

                "In this way the legislature, the executive and the judiciary "
                "are held in balance, each checking the others so that no one "
                "of them may use power as it likes.",
            ],
        ),
    },

    extraAnnotations={
        "정치": dict(
            hanja="政治", meaning="politics",
            characters=[("政", "정", "government — as in 정부 “government”, 정책"),
                        ("治", "치", "to govern, to cure — as in 통치, 자치")],
        ),
        "민주주의": dict(
            hanja="民主主義", meaning="democracy",
            characters=[("民", "민", "the people — as in 국민, 서민, 이주민"),
                        ("主", "주", "master, owner — as in 주인, 주권"),
                        ("義", "의", "principle, righteousness — as in 정의 “justice”")],
            notes=["民主, “the people as master”, over 主義, the suffix that "
                   "makes an -ism. The 주의 of 자본주의 “capitalism” and "
                   "사회주의 “socialism” too."],
        ),
        "민주적": dict(hanja="民主的", meaning="democratic"),
        "민주공화국": dict(
            hanja="民主共和國", meaning="a democratic republic",
            characters=[("共", "공", "together — as in 공동체, 공공"),
                        ("和", "화", "harmony — as in 평화 “peace”, 화합")],
            notes=["공화국 is a republic — literally the country of shared "
                   "harmony, as against a monarchy."],
        ),
        "민주화": dict(
            hanja="民主化", meaning="democratisation",
            characters=[("化", "화", "-isation — as in 도시화, 세계화")],
        ),
        "선거": dict(
            hanja="選擧", meaning="an election",
            characters=[("選", "선", "to choose — as in 선택, 선호하다"),
                        ("擧", "거", "to raise, to hold (an event)")],
        ),
        "통치": dict(
            hanja="統治", meaning="to govern, to rule",
            characters=[("統", "통", "to unify, to govern — as in 통합, 대통령"),
                        ("治", "치", "to govern — as in 정치, 자치")],
        ),
        "이해관계": dict(
            hanja="利害關係", meaning="interests at stake",
            characters=[("利", "리", "profit — as in 이익 “profit”, 유리하다"),
                        ("害", "해", "harm — as in 손해 “loss”, 해롭다"),
                        ("關", "관", "to relate — as in 관계, 관련"),
                        ("係", "계", "to connect")],
            notes=["Literally “the relation of gain and loss”. The 이해 here is "
                   "利害, not the 理解 of 이해하다 “to understand”."],
        ),
        "조정": dict(
            hanja="調整", meaning="to adjust, to mediate",
            characters=[("調", "조", "to tune — as in 조사 “survey”, 강조"),
                        ("整", "정", "to arrange — as in 정리 “tidying”, 조정")],
        ),
        "대통령": dict(
            hanja="大統領", meaning="the president",
            characters=[("統", "통", "to govern — as in 통치, 통합"),
                        ("領", "령", "to lead, a territory — as in 영토, 영역")],
        ),
        "밀접하다": dict(
            hanja="密接하다", meaning="to be close, intimate",
            characters=[("密", "밀", "dense, secret — as in 정밀하다, 비밀"),
                        ("接", "접", "to join — as in 접하다, 접촉")],
        ),
        "다스리다": dict(meaning="to rule, to govern"),
        "떠오르다": dict(meaning="to come to mind; to rise up"),
        "회의": dict(
            hanja="會議", meaning="a meeting",
            characters=[("會", "회", "to meet — as in 사회, 동호회"),
                        ("議", "의", "to deliberate — as in 논의, 의견")],
        ),
        "의견": dict(
            hanja="意見", meaning="an opinion",
            characters=[("意", "의", "intention, meaning — as in 의미, 동의"),
                        ("見", "견", "to see — as in 발견, 견학")],
        ),
        "이롭다": dict(
            hanja="利롭다", meaning="to be beneficial",
            characters=[("利", "리", "profit — the same 利 as in 이해관계")],
            notes=["Its opposite is 해롭다, chapter 8's word — 利 against 害."],
        ),
        "좁히다": dict(
            meaning="to narrow, to close (a gap)",
            notes=["The causative of 좁다 “to be narrow”. 의견 차이를 좁히다 is "
                   "the set phrase."],
        ),
        "이익": dict(
            hanja="利益", meaning="benefit, profit",
            characters=[("益", "익", "benefit — as in 권익 “rights and interests”")],
        ),
        "귀족": dict(
            hanja="貴族", meaning="the nobility",
            characters=[("貴", "귀", "noble — as in 존귀 “dignity”"),
                        ("族", "족", "clan — as in 가족, 유족")],
        ),
        "의논": dict(
            hanja="議論", meaning="to discuss, to talk over",
            characters=[("議", "의", "to deliberate — as in 회의, 논의"),
                        ("論", "론", "to argue — as in 토론, 무신론자")],
            notes=["The same two characters as 논의, in the other order, and "
                   "much the same sense — 의논 is the more everyday of the "
                   "two."],
        ),
        "원리": dict(
            hanja="原理", meaning="a principle",
            characters=[("原", "원", "origin — as in 원인 “cause”, 원칙"),
                        ("理", "리", "reason — as in 이유, 교리")],
        ),
        "신분": dict(
            hanja="身分", meaning="social standing, status",
            characters=[("身", "신", "body, self — as in 신분증, 신체"),
                        ("分", "분", "to divide — as in 부분, 분립")],
        ),
        "재산": dict(
            hanja="財産", meaning="property, wealth",
            characters=[("財", "재", "wealth — as in 문화재 “cultural property”"),
                        ("産", "산", "to produce, property — as in 생산, 부동산")],
        ),
        "성별": dict(hanja="性別", meaning="sex, gender"),
        "표출": dict(
            hanja="表出", meaning="to express, to give voice to",
            characters=[("表", "표", "surface, to show — as in 표현 “expression”"),
                        ("出", "출", "to go out — as in 출발, 진출")],
        ),
        "헌법": dict(
            hanja="憲法", meaning="the constitution",
            characters=[("憲", "헌", "law, constitution"),
                        ("法", "법", "law — as in 법원, 법적")],
        ),
        "구성": dict(
            hanja="構成", meaning="composition, make-up",
            characters=[("構", "구", "to construct — as in 구조, 구성원"),
                        ("成", "성", "to form — as in 성장, 완성")],
        ),
        "권리": dict(
            hanja="權利", meaning="a right",
            characters=[("權", "권", "authority, right — as in 권력, 권익"),
                        ("利", "리", "profit — as in 이익, 이롭다")],
        ),
        "의무": dict(
            hanja="義務", meaning="a duty",
            characters=[("義", "의", "righteousness — as in 민주주의, 정의"),
                        ("務", "무", "duty — as in 업무, 근무제")],
        ),
        "기반": dict(
            hanja="基盤", meaning="a foundation",
            characters=[("基", "기", "base — as in 기본, 기초"),
                        ("盤", "반", "a board, a base")],
        ),
        "공화국": dict(
            hanja="共和國", meaning="a republic",
            notes=["The full name 대한민국 ends in 民國, “the people's state”, "
                   "which is the same idea."],
        ),
        "주인": dict(
            hanja="主人", meaning="the owner, the master",
            characters=[("主", "주", "master — as in 주권, 민주주의")],
        ),
        "권력": dict(
            hanja="權力", meaning="power",
            characters=[("權", "권", "authority — as in 권리, 권익"),
                        ("力", "력", "force — as in 능력, 실력")],
            notes=["권리 is a right one may claim; 권력 is power over others. "
                   "The pair turns on 利 against 力."],
        ),
        "뿌리": dict(meaning="a root"),
        "명시": dict(
            hanja="明示", meaning="to state expressly",
            characters=[("明", "명", "bright, clear — as in 설명, 명당"),
                        ("示", "시", "to show — as in 전시, 제시")],
        ),
        "특정": dict(
            hanja="特定", meaning="particular, specified",
            characters=[("特", "특", "special — as in 특징, 특유"),
                        ("定", "정", "to fix — as in 지정, 정착")],
        ),
        "정치인": dict(hanja="政治人", meaning="a politician"),
        "주권": dict(
            hanja="主權", meaning="sovereignty",
            characters=[("主", "주", "master, owner — as in 주인, 민주주의"),
                        ("權", "권", "authority — as in 권력, 권리")],
            notes=["The right that belongs to the owner of the state. Article "
                   "1 puts it in the people."],
        ),
        "4·19혁명": dict(
            hanja="四一九革命", meaning="the April Revolution of 1960",
            notes=["Student and citizen protests against the rigged election "
                   "of 15 March brought down President 이승만."],
        ),
        "5·18 민주화 운동": dict(
            hanja="五一八民主化運動", meaning="the Gwangju Uprising of 1980",
            notes=["The people of Gwangju rose against the generals' seizure "
                   "of power; many were killed by soldiers as the protests "
                   "were put down."],
        ),
        "6월 민주 항쟁": dict(
            hanja="六月民主抗爭", meaning="the June Democratic Struggle of 1987",
            characters=[("抗", "항", "to resist — as in 저항 “resistance”"),
                        ("爭", "쟁", "to contend — as in 경쟁, 쟁점")],
            notes=["Nationwide protests for direct presidential elections and "
                   "a new constitution, which is the constitution Korea has "
                   "now."],
        ),
        "부정 선거": dict(
            hanja="不正選擧", meaning="a rigged election",
            characters=[("不", "불", "not — as in 불법, 불효"),
                        ("正", "정", "correct — as in 정식, 정시")],
        ),
        "반발": dict(
            hanja="反撥", meaning="a backlash, resistance",
            characters=[("反", "반", "against — as in 반대, 반영"),
                        ("撥", "발", "to push away")],
        ),
        "시위": dict(
            hanja="示威", meaning="a demonstration",
            characters=[("示", "시", "to show — as in 명시, 전시"),
                        ("威", "위", "authority, might — as in 위력")],
            notes=["Literally “a show of force”. The everyday word for a "
                   "protest march."],
        ),
        "이승만": dict(
            meaning="Lee Syng-man, first president of Korea",
            notes=["In office 1948-1960, brought down by the April "
                   "Revolution."],
        ),
        "물러나다": dict(meaning="to step down, to withdraw"),
        "세력": dict(
            hanja="勢力", meaning="a faction, a force",
            characters=[("勢", "세", "momentum, influence — as in 정세, 추세")],
        ),
        "집권": dict(
            hanja="執權", meaning="taking power",
            characters=[("執", "집", "to hold, to carry out — as in 집행")],
        ),
        "회복": dict(
            hanja="回復", meaning="recovery, restoration",
            characters=[("回", "회", "to turn round — as in 횟수, 회갑"),
                        ("復", "복", "to return — as in 복습")],
        ),
        "희생되다": dict(
            hanja="犧牲되다", meaning="to be sacrificed, to lose one's life",
            characters=[("犧", "희", "a sacrificial animal"),
                        ("牲", "생", "a sacrificial animal")],
        ),
        "직선제": dict(
            hanja="直選制", meaning="direct election",
            characters=[("直", "직", "direct, straight — as in 직접, 직업"),
                        ("制", "제", "system — as in 제도, 근무제")],
            notes=["The people vote for the president themselves. Its "
                   "opposite is 간선제, where an electoral body does — which "
                   "is what 1987 overturned."],
        ),
        "개정": dict(
            hanja="改正", meaning="amendment, revision",
            characters=[("改", "개", "to reform — as in 개신교, 개조"),
                        ("正", "정", "correct — as in 정식, 부정 선거")],
        ),
        "전국적": dict(hanja="全國的", meaning="nationwide"),
        "보장": dict(
            hanja="保障", meaning="to guarantee",
            characters=[("保", "보", "to protect — as in 보험, 보호"),
                        ("障", "장", "a barrier — as in 장벽")],
        ),
        "유리하다": dict(
            hanja="有利하다", meaning="to be advantageous",
            characters=[("有", "유", "to have — as in 고유, 유일하다"),
                        ("利", "리", "profit — as in 이익, 이롭다")],
            notes=["Its opposite is 불리하다."],
        ),
        "비롯하다": dict(
            meaning="to begin with, to include (foremost)",
            notes=["한국을 비롯한 “Korea and others like it”, literally "
                   "“beginning with Korea”. Related to 비롯되다 “to originate "
                   "in”, chapter 13's word."],
        ),
        "집단": dict(
            hanja="集團", meaning="a group, a collective",
            characters=[("集", "집", "to gather — as in 집중, 수집"),
                        ("團", "단", "group — as in 단체, 종교단체")],
        ),
        "집중": dict(
            hanja="集中", meaning="concentration",
            characters=[("集", "집", "to gather — as in 집단"),
                        ("中", "중", "middle — as in 중심, 중학교")],
        ),
        "독립": dict(
            hanja="獨立", meaning="independence",
            characters=[("獨", "독", "alone — as in 단독, 독특하다"),
                        ("立", "립", "to stand — as in 설립, 분립")],
        ),
        "원칙": dict(
            hanja="原則", meaning="a principle, a rule",
            characters=[("原", "원", "origin — as in 원리, 원인"),
                        ("則", "칙", "rule — as in 규칙")],
        ),
        "권력 분립": dict(
            hanja="權力分立", meaning="the separation of powers",
            characters=[("分", "분", "to divide — as in 부분, 분리"),
                        ("立", "립", "to stand — as in 독립, 설립")],
        ),
        "삼권 분립": dict(
            hanja="三權分立", meaning="the separation of the three powers",
            notes=["The three being 입법(legislative), 행정(executive) and "
                   "사법(judicial)."],
        ),
        "실현": dict(
            hanja="實現", meaning="realisation, bringing about",
            characters=[("實", "실", "real — as in 사실, 실천"),
                        ("現", "현", "to appear — as in 현재, 현상")],
        ),
        "입법부": dict(
            hanja="立法部", meaning="the legislature",
            characters=[("立", "립", "to establish — as in 설립, 독립"),
                        ("法", "법", "law — as in 헌법, 법원"),
                        ("部", "부", "department, branch — as in 법무부, 부처")],
            notes=["Chapter 21's subject: the 국회, the National Assembly."],
        ),
        "행정부": dict(
            hanja="行政部", meaning="the executive",
            characters=[("行", "행", "to do, to go — as in 행동, 시행"),
                        ("政", "정", "government — as in 정치, 정책")],
            notes=["Chapter 22's subject: the 정부, the government."],
        ),
        "사법부": dict(
            hanja="司法部", meaning="the judiciary",
            characters=[("司", "사", "to take charge of — as in 사회자")],
            notes=["Chapter 23's subject: the 법원, the courts."],
        ),
        "분리": dict(
            hanja="分離", meaning="separation",
            characters=[("分", "분", "to divide — as in 분립, 부분"),
                        ("離", "리", "to part — as in 이혼, 이착륙")],
        ),
        "처리": dict(
            hanja="處理", meaning="to deal with, to handle",
            characters=[("處", "처", "place, to deal with — as in 부처, 처음"),
                        ("理", "리", "reason, to manage — as in 관리, 원리")],
        ),
        "궁극적": dict(
            hanja="窮極的", meaning="ultimate, in the end",
            characters=[("窮", "궁", "poor, to exhaust"),
                        ("極", "극", "extreme, pole — as in 극복, 적극적")],
        ),
        "기여": dict(
            hanja="寄與", meaning="to contribute",
            characters=[("寄", "기", "to entrust, to send"),
                        ("與", "여", "to give — as in 수여, 여건")],
        ),
        "견제": dict(
            hanja="牽制", meaning="a check, a restraint",
            characters=[("牽", "견", "to pull, to lead"),
                        ("制", "제", "to control — as in 제도, 규제")],
            notes=["The 견제 of 견제와 균형 — checks and balances."],
        ),
        "운영": dict(
            hanja="運營", meaning="to run, to operate",
            characters=[("運", "운", "to move, fortune — as in 운동, 행운"),
                        ("營", "영", "to manage — as in 경영 “management”")],
        ),
        "제정": dict(
            hanja="制定", meaning="to enact (a law)",
            characters=[("制", "제", "system — as in 제도, 견제"),
                        ("定", "정", "to fix — as in 지정, 특정")],
        ),
        "집행": dict(
            hanja="執行", meaning="to carry out, to execute (a law, a budget)",
            characters=[("執", "집", "to hold, to take charge of — as in 집권, 고집"),
                        ("行", "행", "to go, to act — as in 행정, 실행, 시행")],
            notes=["What the 행정부 does with a law the 입법부 has enacted: "
                   "법률 집행. 집행되다 for the law being carried out."],
        ),
        "정책": dict(
            hanja="政策", meaning="a policy",
            characters=[("政", "정", "government — as in 정치, 행정부"),
                        ("策", "책", "a plan — as in 대책 “countermeasure”, 산책")],
        ),
        "펼치다": dict(meaning="to unfold, to carry out (a policy, a campaign)"),
        "해석": dict(
            hanja="解釋", meaning="interpretation",
            characters=[("解", "해", "to loosen, to resolve — as in 이해, 해소"),
                        ("釋", "석", "to explain, to release")],
        ),
        "적용": dict(
            hanja="適用", meaning="application",
            characters=[("適", "적", "suitable — as in 적합하다, 적응"),
                        ("用", "용", "to use — as in 이용, 활용")],
        ),
        "재판": dict(
            hanja="裁判", meaning="a trial",
            characters=[("裁", "재", "to judge, to cut out"),
                        ("判", "판", "to judge — as in 판단, 비판")],
        ),
        "고위": dict(
            hanja="高位", meaning="high-ranking",
            characters=[("高", "고", "high — as in 고등학교, 고령화"),
                        ("位", "위", "rank — as in 지위, 학위")],
        ),
        "공무원": dict(
            hanja="公務員", meaning="a public official",
            characters=[("公", "공", "public — as in 공적, 공공"),
                        ("務", "무", "duty — as in 의무, 업무"),
                        ("員", "원", "member — as in 구성원, 조합원")],
        ),
        "위반": dict(
            hanja="違反", meaning="a breach, to violate",
            characters=[("違", "위", "to go against"),
                        ("反", "반", "against — as in 반대, 반발")],
        ),
        "파면": dict(
            hanja="罷免", meaning="dismissal from office",
            characters=[("罷", "파", "to cease, to dismiss"),
                        ("免", "면", "to exempt — as in 면제 “exemption”")],
        ),
        "헌법재판소": dict(
            hanja="憲法裁判所", meaning="the Constitutional Court",
            notes=["Separate from the ordinary courts. It rules on whether a "
                   "law is constitutional and on the removal of high "
                   "officials — the impeachments of 2017 and 2004 went "
                   "through it."],
        ),
        "법안": dict(
            hanja="法案", meaning="a bill",
            characters=[("案", "안", "a plan, a proposal — as in 방안 “a plan”")],
        ),
        "거부": dict(
            hanja="拒否", meaning="refusal, veto",
            characters=[("拒", "거", "to refuse"),
                        ("否", "부", "no, or not — as in 여부, 안부")],
        ),
        "여부": dict(
            hanja="與否", meaning="whether or not",
            characters=[("與", "여", "to give, and — as in 수여, 여건"),
                        ("否", "부", "not — as in 거부, 안부")],
        ),
        "판단": dict(
            hanja="判斷", meaning="a judgement",
            characters=[("判", "판", "to judge — as in 재판, 비판"),
                        ("斷", "단", "to cut off — as in 단절, 판단")],
        ),
        "함부로": dict(
            meaning="recklessly, as one likes",
            notes=["Of doing something without due care or right. Often "
                   "misspelled 함부러."],
        ),
        "균형": dict(
            hanja="均衡", meaning="balance",
            characters=[("均", "균", "even — as in 평균 “average”"),
                        ("衡", "형", "a balance, scales")],
        ),
        "독재": dict(
            hanja="獨裁", meaning="dictatorship",
            characters=[("獨", "독", "alone — as in 독립, 독특하다"),
                        ("裁", "재", "to judge, to decide — as in 재판")],
            notes=["Literally “deciding alone”. 독재자 is a dictator."],
        ),
        "차지": dict(meaning="to take, to occupy (a share, a place)"),
        "대통령직": dict(hanja="大統領職", meaning="the office of president"),
        "정권": dict(
            hanja="政權", meaning="political power, a regime",
            characters=[("政", "정", "government — as in 정치, 정책"),
                        ("權", "권", "power — as in 권력, 권리")],
        ),
        "불법": dict(
            hanja="不法", meaning="illegality",
            characters=[("不", "불", "not — as in 부정, 불효")],
        ),
        "폭력": dict(
            hanja="暴力", meaning="violence",
            characters=[("暴", "폭", "violent, sudden — as in 폭죽 “firecracker”"),
                        ("力", "력", "force — as in 권력, 능력")],
        ),
        "억압당하다": dict(
            hanja="抑壓當하다", meaning="to be oppressed",
            characters=[("抑", "억", "to press down, to restrain"),
                        ("壓", "압", "to press — as in 압력 “pressure”"),
                        ("當", "당", "to undergo — as in 담당, 해당")],
        ),
        "비판": dict(
            hanja="批判", meaning="criticism",
            characters=[("批", "비", "to criticise, to approve"),
                        ("判", "판", "to judge — as in 판단, 재판")],
        ),
        "조직": dict(
            hanja="組織", meaning="an organisation",
            characters=[("組", "조", "to form — as in 조합원, 노조"),
                        ("織", "직", "to weave")],
        ),
        "단체": dict(
            hanja="團體", meaning="a body, a group",
            characters=[("團", "단", "group — as in 집단, 종교단체")],
        ),
        "갈등": dict(
            hanja="葛藤", meaning="conflict, friction",
            characters=[("葛", "갈", "arrowroot vine"),
                        ("藤", "등", "wisteria vine")],
            notes=["Two climbing plants tangled together — the image behind "
                   "the word."],
        ),
    },

    extraNotes=[
        # read and approved: the provenance is in this module's docstring,
        # so the page no longer carries it
        "The 권력 분립 diagram on p. 112 puts 국민 at the centre with the three "
        "branches around it and 견제 arrows between them. The three branches "
        "and what each does are set as a table; the arrows are described in "
        "the caption.",
    ],
)
