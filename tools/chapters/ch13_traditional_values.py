# -*- coding: utf-8 -*-
"""Chapter 13 — Traditional values.

No Google Doc: yours stop at chapter 12. Transcribed from the photos of
pp. 76-79, so the Korean here is my reading of the page rather than yours,
and any error in it is mine.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, LABELS, MARGIN, FIGURE,
               TABLE, CELL, GLOSSARY)

CHAPTER = dict(
    number=13, slug="13-traditional-values",
    unit="문화", title="전통 가치", titleEn="Traditional values",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 일상생활에서 종종 실수하는 {높임말}과 관련된 표현입니다."),
        TABLE(["틀린 표현 (X)", "올바른 표현 (O)"],
              [["사장님, 밥 먹었어?", "사장님, 식사하셨어요?"],
               ["시어머니께서 오시는 중이시다.", "시어머니께서 오시는 중이다."],
               ["할아버지: 엄마, 집에 있니? 손자: 네, 집에 있어요.",
                "할아버지: 엄마, 집에 있니? 손자: 네, 집에 계세요."],
               ["선생님 옷이 예쁘세요.", "선생님 옷이 예뻐요."]]),
        HEADING(4, "01 한국에서 높임말을 사용하면서 실수했던 경험이 있습니까?"),
        HEADING(4, "02 한국에서 높임말을 배울 때 어떤 점이 어려웠습니까?"),

        SECTION("goals", "학습목표"),
        BULLET("한국의 전통 가치인 효와 예절의 특징을 설명할 수 있다.", ordered=True),
        BULLET("한국에서 공동체와 연고를 중시하는 이유를 설명할 수 있다.", ordered=True),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", 2), "제목", "관련 내용"],
              [[CELL("기본", down=2), CELL("문화", down=2), "15. 의례", "한국의 대표적인 의례"],
               ["16. 명절", "설날과 추석"]]),

        SECTION("part", "01 효와 예절은 무엇일까?"),
        MARGIN("{불효}", "{효자}", "{효녀}", "{효부}", "{효손}"),
        HEADING(2, "한국의 효(孝)"),
        GLOSSARY(("유교", "중국 공자의 가르침을 기본으로 하는 유학을 종교적으로 표현한 말", "유교"),
              ("조상", "이미 돌아가신, 부모 위의 어른", "조상"),
              ("봉안당(납골당)", "죽은 사람의 유골(시신을 태우고 남은 뼈)을 보관해 두는 곳",
               "봉안당"),
              ("추모", "죽은 사람을 그리워함", "추모"),
              ("공경", "공손히 받들어 모심", "공경")),
        PARAGRAPH("한국 사회가 그동안 많은 변화를 겪어 왔지만, 전통적으로 이어져 온 가치와 문화는 "
          "지금도 한국인의 일상생활에 많은 {영향}을 {끼치고|끼치다} 있다. 그 대표적인 예로 "
          "{효}와 {예절}을 꼽을 수 있다."),
        PARAGRAPH("{유교} 문화의 영향을 받은 한국에서는 부모를 잘 {섬기고|섬기다} 기쁘게 해 드리고자 "
          "하는 효를 중시한다. 자녀가 성장하면서 취직, 결혼 등으로 부모와 떨어져 지내는 경우가 "
          "많지만, 명절이나 부모의 생일이 되면 자녀가 부모를 직접 {찾아뵙는다|찾아뵙다}. "
          "이러한 문화는 효에서 {비롯된|비롯되다} 것이다. 효는 살아계신 부모뿐 아니라 "
          "돌아가신 {조상}에게도 적용된다. 그래서 많은 사람들이 명절이면 조상의 {묘}나 "
          "{봉안당}을 찾아 {추모}한다. 효는 다른 {웃어른}을 존중하고 {공경}하는 행동으로 "
          "이어지기도 한다."),
        PARAGRAPH("한국에서는 버스나 지하철에서 노인에게 자리를 {양보}하거나 노인의 무거운 짐을 함께 "
          "들어주는 모습을 자주 볼 수 있다. 이는 웃어른을 {공손히|공손하다} 모시고자 하는 유교 "
          "문화가 지금까지 이어져 오고 있음을 보여주는 {사례}이다."),
        FIGURE("지하철에서 노인에게 자리를 양보하는 모습"),

        HEADING(2, "한국의 예절"),
        GLOSSARY(("공적", "개인적인 것이 아니라 여러 사람들이나 단체, 국가 등에 관계되는 것",
               "공적"),
              ("높임말", "주로 자신보다 나이가 많은 상대에게 공경하는 마음을 담아 하는 말. "
                        "‘존댓말’이라고도 함", "높임말")),
        PARAGRAPH("한국인은 다른 사람과의 관계에서 예절을 중요하게 여긴다. 예절은 다른 사람을 대할 때 "
          "존중하는 마음을 담은 {말투}나 행동을 가리킨다."),
        PARAGRAPH("일반적으로 웃어른과 인사를 나눌 때는 고개를 {숙여|숙이다} 인사한다. 웃어른과 "
          "식사할 때는 웃어른이 먼저 {수저}를 들 때까지 잠시 기다린다. 웃어른에게 물건을 "
          "{건네거나|건네다} 받을 때는 두 손으로 주고받는다. 명절이나 결혼식 등과 같은 날에는 "
          "부모를 비롯한 웃어른께 {절}을 한다."),
        PARAGRAPH("예절은 웃어른을 대할 때만 필요한 것은 아니다. 어떤 사람을 처음 만났거나 {공적}인 "
          "자리에서는 각자의 {지위}나 나이에 관계없이 서로 {높임말}을 사용한다. 특히 언어 "
          "예절은 다른 사람과의 관계에서 가장 기본적인 것으로서 매우 {강조}되고 있다. 그래서 "
          "가정이나 학교에서도 아이가 어릴 때부터 높임말을 정확히 쓰는 습관을 "
          "{기르도록|기르다} 가르친다."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "만 65세 이상 노인을 위한 복지 혜택(2020년 기준)", translation=
          "Welfare benefits for people aged 65 and over (as of 2020)" "\n\n"
          "As Korea has become an ageing society, much effort has gone not "
          "only into respect for the old but into raising their quality of "
          "life in practical ways. A range of welfare benefits is provided "
          "to those aged 65 and over; the main ones are these."),
        PARAGRAPH("한국은 {고령화} 사회가 되면서 노인 공경 뿐 아니라 {실질적}으로 노인의 삶의 질이 "
          "{향상}될 수 있도록 많은 노력을 기울이고 있다. 만 65세 이상의 노인들에게 다양한 복지 "
          "{혜택}을 지원하고 있으며, 그 대표적인 예는 다음과 같다."),
        BULLET("지하철, 도시철도 무료",
          translation="Free travel on the subway and urban railways."),
        BULLET("KTX, SRT, 새마을호, 무궁화 기차 30% 할인(주말 및 공휴일 제외)",
          translation="30% off KTX, SRT, Saemaul and Mugunghwa trains "
                      "(except weekends and public holidays)."),
        BULLET("{고궁} 및 국공립 박물관 무료",
          translation="Free entry to the old palaces and to national and "
                      "public museums."),
        BULLET("치과 임플란트 및 {틀니} 70% 할인 지원",
          translation="70% off dental implants and dentures."),
        BULLET("국가 예방 접종 지원(폐렴구균/인플루엔자)",
          translation="State-funded vaccination (pneumococcus and "
                      "influenza)."),
        BULLET("노인 일자리 및 사회활동 지원 프로그램 참여",
          translation="A place on the programmes supporting work and "
                      "social activity for older people."),

        SECTION("part", "02 공동체와 연고를 중요하게 여기는 모습은 어떻게 나타날까?"),
        HEADING(2, "공동체를 중요하게 생각하는 한국인"),
        GLOSSARY(("공동체 의식", "공동의 목적이나 생활 방식 등을 가진 집단에 소속되어 있다는 생각",
               "공동체 의식"),
              ("두레", "마을 사람들끼리 힘을 모아 공동으로 농사일을 하기 위한 조직", "두레"),
              ("품앗이", "일을 서로 거들어 주어 품을 지고 갚는 교환노동", "품앗이"),
              ("상부상조", "서로 의지하고 서로 도움", "상부상조"),
              ("계기", "어떤 일이 일어나도록 하는 결정적인 원인이나 기회", "계기")),
        PARAGRAPH("한국인은 자신과 관련된 이야기를 할 때, ‘우리 엄마’, ‘우리 동네’ 등과 같이 ‘우리’라는 "
          "표현을 자주 사용한다. 이는 과거 {농경} 사회에서 만들어진 {공동체 의식}과 관련이 "
          "깊다. 농사를 지을 때는 많은 일손이 필요하기 때문에 과거에는 가까이서 함께 살면서 "
          "함께 밥 먹고 함께 일을 하곤 했다. 그에 따라 과거 농촌에서는 ‘{두레}’와 ‘{품앗이}’와 "
          "같은 {상부상조} 풍습을 많이 볼 수 있었다."),
        PARAGRAPH("공동체 의식은 나라에 중요한 일이 있을 때 함께 힘을 모으는 {계기}가 되기도 한다. "
          "한국이 1997년 {외환} 위기를 맞이했을 때 많은 국민이 ‘금 모으기 운동’을 통해 위기를 "
          "{극복}하는 데 도움을 주었다. 2002년 월드컵 축구 대회 때 수백만 명이 모여 길거리 "
          "{응원}을 했던 것을 시작으로 국가적인 스포츠 경기가 있을 때 많은 사람들이 {대규모} "
          "응원을 벌이는 모습도 한국인의 공동체 의식을 보여주는 사례라고 할 수 있다."),
        FIGURE("2002 한·일 월드컵 길거리 응원 모습"),

        HEADING(2, "연고를 중시하는 한국인"),
        GLOSSARY(("본관", "성씨 조상, 즉 시조가 태어난 거주지를 뜻함(예: 안동 김씨, 경주 이씨, "
                      "밀양 박씨)", "본관"),
              ("인연", "사람과 사람 사이의 연결 고리나 관계", "인연"),
              ("향우회", "고향이나 출신 지역이 같은 사람들의 친목 조직", "향우회"),
              ("동문회", "같은 학교를 졸업한 사람들이 모여 만든 조직", "동문회")),
        PARAGRAPH("한국에서는 처음 만나는 사람으로부터 나이, 사는 곳, 직장 등 개인적인 것에 대한 질문을 "
          "받기도 한다. 이는 {지나친|지나치다} 관심으로 {비춰질|비춰지다} 수도 있다. 그런데 "
          "이러한 질문을 하는 이유는 자신과 비슷한 점이 있는지 찾아보고 그것을 활용하여 "
          "가까워지고 싶어 하기 때문이다. 이렇게 서로의 {공통점}을 연결 고리로 하여 맺어지는 "
          "관계를 {연고}라고 한다."),
        PARAGRAPH("가족이나 {친족} 등 같은 {핏줄}로 연결된 인간관계를 {혈연}이라고 한다. 같은 "
          "{성씨}일 경우 “어디 O(성)씨 세요?”와 같은 질문을 통해 동일한 {본관}이라면 중요한 "
          "{인연}으로 생각한다. 그리고 같은 고향이나 출신 지역에 따라 이어진 인연을 {지연}이라고 "
          "한다. 직장 생활을 하면서 같은 지역 출신을 만나면 반가움을 드러내며 또한 "
          "{적극적}으로 {향우회}에 참여해 {친목}을 다지는 사람들도 있다. 같은 학교를 졸업한 "
          "사람들이 서로 인연을 맺은 관계는 {학연}이라고 한다. 특히, 한국에서는 출신 고등학교와 "
          "대학교를 통해 맺어지는 인연이 중시되고 있으며 {동문회}를 통해 {교류}를 이어가고 "
          "있다."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "‘생활협동조합(생협)’에 대해 들어 봤나요?", translation=
          "Have you heard of the ‘생활협동조합’ — the consumer co-operative?" "\n\n"
          "A 생활협동조합 is an arrangement in which members share everyday "
          "food and manufactured goods — things made in factories — among "
          "themselves. At a co-operative one can buy goods safely and "
          "relatively cheaply, through the producer. It also helps in "
          "putting the spirit of mutual aid into practice: an effort to "
          "live alongside one’s neighbours, and ethical consumption that "
          "protects the earth and sustains life. Among the best-known "
          "co-operatives are 한살림, 두레생협 and ICOOP생협."),
        PARAGRAPH("{생활협동조합}이란 {조합원}들 간에 일상적인 식품과 {공산품}(공장에서 생산한 물건) "
          "등을 서로 나누는 형태를 말한다. 생활협동조합에서는 생산자를 통해 비교적 싼 가격으로 "
          "안전하게 물품을 살 수 있다. 뿐만 아니라 이웃과 더불어 살려는 노력, 지구를 지키고 "
          "생명을 살리는 {윤리적} 소비를 통해 상부상조 정신을 {실천}하는 데도 도움이 된다. "
          "대표적인 생협으로는 한살림, 두레생협, ICOOP생협 등이 있다."),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 효와 예절은 무엇일까?"),
        BULLET("한국인은 가정에서 부모를 잘 섬기고 기쁘게 해 드리는 (        )의 가치를 중요하게 "
          "생각한다."),
        BULLET("(        )은 다른 사람을 대할 때 존중하는 마음을 담은 말투나 행동이다."),
        BULLET("한국에서는 어떤 사람을 처음 만났거나 공적인 자리에서는 각자의 지위나 나이에 "
          "관계없이 (        )을 사용한다."),
        HEADING(3, "02 공동체와 연고를 중요하게 여기는 모습은 어떻게 나타날까?"),
        BULLET("과거 농촌에서는 두레나 품앗이처럼 서로 의지하고 서로 돕는 (        ) 풍습이 많이 "
          "있었다."),
        BULLET("같은 고향이나 출신 지역에 따라 이어진 인연을 (        )이라고 한다."),
        BULLET("같은 학교를 졸업한 사람들이 모여 만든 조직을 (        )라고 한다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "공동체 의식을 담고 있는 한국의 속담", translation=
          "Korean proverbs that carry a sense of community" "\n\n"
          "A 속담 is a short, plain saying handed down from long ago that "
          "carries a lesson or a satire. Every country in the world has "
          "proverbs that express its own culture and feeling. In Korea, "
          "where a sense of community is held to matter, proverbs carrying "
          "that meaning have been handed down too."),
        PARAGRAPH("{속담}은 예로부터 전해 오는 짧고 쉬우면서 {교훈}이나 {풍자}를 담고 있는 말을 "
          "뜻한다. 세계 여러 나라에는 그 나라만의 문화와 {정서}를 표현하는 속담이 존재한다. "
          "공동체 의식을 중요하게 생각하는 한국에서도 이러한 의미를 담은 속담이 전해 내려오고 "
          "있다."),
        TABLE(["콩 한 조각도 나눠 먹는다.", "백지장도 맞들면 낫다.", "손이 많으면 일도 쉽다."],
              [["작고 사소한 음식이라도 다른 사람을 배려하는 마음으로 서로 나눠 먹음",
                "백지장처럼 가벼운 것이라도 서로 돕고 협력한다면 훨씬 쉽고 효과적임",
                "여러 사람들이 모여 힘을 합치면 무슨 일이든 쉽게 해결할 수 있음"]]),
        PARAGRAPH("★ 자신의 고향 나라에서 전해 내려오는 속담을 소개해 봅시다.",
          "Introduce a proverb handed down in your home country."),
    ],

    english={
        "한국의 효(孝)": dict(
            title="Filial duty in Korea",
            paragraphs=[
                "Korean society has been through a great deal of change, and "
                "yet the values and the culture handed down from the past "
                "still bear heavily on daily life. Filial duty and courtesy "
                "are the clearest examples.",

                "Korea, shaped by Confucian culture, sets store by 효 — "
                "serving one's parents well and giving them pleasure. As "
                "children grow up they often live apart from their parents "
                "for work or marriage, but at the seasonal festivals and on a "
                "parent's birthday they go and call on them in person. That "
                "custom comes out of 효. Filial duty extends not only to "
                "living parents but to ancestors who have died. That is why "
                "so many people visit the family grave or the charnel house "
                "at the festivals to remember them. It carries over, too, "
                "into respect and deference towards one's elders generally.",

                "One often sees a seat given up to an elderly person on a bus "
                "or the underground, or a heavy load carried for them. It is "
                "a sign that the Confucian culture of treating one's elders "
                "with deference has come down to the present day.",
            ],
        ),
        "한국의 예절": dict(
            title="Courtesy in Korea",
            paragraphs=[
                "Koreans consider courtesy important in their dealings with "
                "others. 예절 means the manner of speech and the conduct that "
                "carry respect towards the person one is dealing with.",

                "Generally one bows the head when greeting an elder. Eating "
                "with an elder, one waits until they have picked up their "
                "spoon and chopsticks. Handing something to an elder, or "
                "taking something from them, one uses both hands. On days "
                "such as the seasonal festivals or a wedding, one bows to "
                "one's parents and to one's elders.",

                "Courtesy is not needed only towards elders. On meeting "
                "someone for the first time, or in a formal setting, people "
                "use honorific speech with one another whatever their rank or "
                "age. Courtesy in language is stressed particularly hard, as "
                "the most basic thing in any dealing with another person. "
                "That is why at home and at school alike children are taught "
                "from an early age the habit of using honorifics correctly.",
            ],
        ),
        "공동체를 중요하게 생각하는 한국인": dict(
            title="Koreans and the sense of community",
            paragraphs=[
                "When Koreans speak of anything of their own they often use "
                "the word 우리, “our” — 우리 엄마, “our mum”; 우리 동네, “our "
                "neighbourhood”. It has much to do with the sense of "
                "community formed in the farming society of the past. Working "
                "the land takes many hands, so people once lived close "
                "together, ate together and worked together. Hence the "
                "customs of mutual aid one used to see in the countryside, "
                "such as 두레 and 품앗이.",

                "That sense of community can also become the occasion for "
                "pulling together when something important befalls the "
                "country. When Korea met the foreign exchange crisis of 1997, "
                "many people helped it through by way of the gold-collecting "
                "campaign. And from the millions who gathered to cheer in the "
                "streets at the 2002 World Cup onwards, the sight of large "
                "crowds cheering whenever there is a national sporting "
                "occasion is another instance of the Korean sense of "
                "community.",
            ],
        ),
        "연고를 중시하는 한국인": dict(
            title="Koreans and the ties they are born into",
            paragraphs=[
                "In Korea someone met for the first time may ask personal "
                "questions — one's age, where one lives, where one works. It "
                "can look like excessive curiosity. The reason for such "
                "questions, though, is to look for something the two have in "
                "common and to use it to get closer. A relationship formed by "
                "taking a shared point as the link is what is meant by 연고.",

                "A human relationship joined by the same blood — family or "
                "kin — is called 혈연. Where the family name is the same, a "
                "question like “Which 씨 are you?” establishes whether the "
                "ancestral seat is the same, and if it is, that is thought a "
                "meaningful tie. A tie following from the same home town or "
                "region is called 지연. Some people, meeting someone from "
                "their own region at work, show their pleasure openly and "
                "join the regional association to build the friendship up. A "
                "relationship between people who graduated from the same "
                "school is called 학연. Ties formed through one's high school "
                "and university are given particular weight in Korea, and are "
                "kept up through the alumni association.",
            ],
        ),
    },

    extraAnnotations={
        "끼치다": dict(
            meaning="to exert, to cause (an influence, trouble)",
            notes=["Almost always with 영향 “influence” or 폐 “trouble”. "
                   "영향을 끼치다 and 영향을 미치다 are interchangeable."],
        ),
        "섬기다": dict(
            meaning="to serve, to wait on (a parent, a lord)",
            notes=["Reserved for those one owes duty to. The verb at the "
                   "heart of 효."],
        ),
        "찾아뵙다": dict(
            meaning="to call on (someone senior)",
            notes=["The humble form of 찾아보다. 뵙다 is the humble “to see”, "
                   "used when the person seen is one's superior."],
        ),
        "비롯되다": dict(
            meaning="to originate in, to stem from",
            notes=["From 비롯하다. 부모를 비롯한 웃어른 in the same chapter is the "
                   "other use: “one's elders, beginning with one's parents”."],
        ),
        "공손하다": dict(
            hanja="恭遜하다", meaning="to be respectful, deferential",
            characters=[("恭", "공", "respectful — the same 恭 as in 공경"),
                        ("遜", "손", "modest, yielding")],
        ),
        "숙이다": dict(
            meaning="to bow, to lower (the head)",
            notes=["고개를 숙이다 is the small bow of greeting, as against 절, "
                   "the full bow from the waist or the floor."],
        ),
        "수저": dict(
            meaning="spoon and chopsticks together",
            notes=["A contraction of 숟가락 and 젓가락. Korea is unusual in "
                   "using both at every meal, and the pair has its own word."],
        ),
        "건네다": dict(meaning="to hand over, to pass"),
        "절": dict(
            meaning="a formal bow",
            notes=["Not the light nod of 고개를 숙이다 but the deep bow made to "
                   "elders at 설날 and at weddings. The same syllable is also "
                   "the word for a Buddhist temple."],
        ),
        "기르다": dict(
            meaning="to bring up, to cultivate (a habit)",
            notes=["Used of children, animals, hair and habits alike."],
        ),
        "응원": dict(
            hanja="應援", meaning="cheering, support",
            characters=[("應", "응", "to respond — as in 응급 “emergency”"),
                        ("援", "원", "to help — as in 지원 “support”")],
        ),
        "지나치다": dict(
            meaning="to be excessive; to pass by",
            notes=["Two senses from one verb: to go past something, and to go "
                   "too far."],
        ),
        "비춰지다": dict(
            meaning="to be seen as, to come across as",
            notes=["The passive of 비추다 “to shine on, to reflect”. What the "
                   "questions look like from outside."],
        ),
        "높임말": dict(
            meaning="honorific speech",
            notes=["A pure-Korean compound: 높이다 “to raise” + 말 “speech”. "
                   "Also called 존댓말. The chapter's warm-up table is four "
                   "ways of getting it wrong."],
        ),
        "효": dict(
            hanja="孝", meaning="filial duty",
            characters=[("孝", "효", "filial piety — the 老 “old” of an elder "
                                    "over the 子 “child” who supports them")],
            notes=["The single character carries the whole idea: serving "
                   "one's parents. It heads a family of words — 효자 a "
                   "dutiful son, 효녀 a dutiful daughter, 효부 a dutiful "
                   "daughter-in-law, 효손 a dutiful grandchild, and 불효 the "
                   "failure to be any of them."],
        ),
        "불효": dict(
            hanja="不孝", meaning="failing in filial duty",
            characters=[("不", "불", "not — as in 불가능 “impossible”, 불편")],
        ),
        "효자": dict(hanja="孝子", meaning="a dutiful son"),
        "효녀": dict(hanja="孝女", meaning="a dutiful daughter"),
        "효부": dict(
            hanja="孝婦", meaning="a dutiful daughter-in-law",
            characters=[("婦", "부", "woman, wife — as in 주부 “homemaker”, 부부")],
        ),
        "효손": dict(
            hanja="孝孫", meaning="a dutiful grandchild",
            characters=[("孫", "손", "grandchild — as in 손자 “grandson”")],
        ),
        "예절": dict(
            hanja="禮節", meaning="courtesy, propriety",
            characters=[("禮", "례", "rite, courtesy — as in 예의 “manners”, 의례"),
                        ("節", "절", "joint, measure, restraint — as in 명절, 계절")],
        ),
        "유교": dict(
            hanja="儒敎", meaning="Confucianism",
            characters=[("儒", "유", "the scholar, the Confucian"),
                        ("敎", "교", "teaching — as in 교육, 종교 “religion”")],
            notes=["유학(儒學) is the body of learning; 유교 is the same thing "
                   "spoken of as a religion."],
        ),
        "조상": dict(
            hanja="祖上", meaning="an ancestor",
            characters=[("祖", "조", "forefather — as in 할아버지의 조부, 조국"),
                        ("上", "상", "above — as in 상급 “higher grade”")],
        ),
        "봉안당": dict(
            hanja="奉安堂", meaning="a charnel house, a columbarium",
            characters=[("奉", "봉", "to offer up, to serve reverently"),
                        ("安", "안", "peace, rest — as in 안전 “safety”, 안정"),
                        ("堂", "당", "hall — as in 식당 “restaurant”, 강당")],
            notes=["Where the ashes are kept. Also called 납골당(納骨堂), "
                   "“the hall where the bones are laid”; 봉안당 is the gentler "
                   "of the two words."],
        ),
        "추모": dict(
            hanja="追慕", meaning="to remember the dead",
            characters=[("追", "추", "to pursue, to follow after — as in 추적"),
                        ("慕", "모", "to long for, to yearn")],
        ),
        "공경": dict(
            hanja="恭敬", meaning="reverence, deference",
            characters=[("恭", "공", "respectful — the same 恭 as in 공손하다"),
                        ("敬", "경", "to revere — as in 존경 “respect”")],
        ),
        "웃어른": dict(
            meaning="one's elders",
            notes=["Pure Korean: 웃- “upper” + 어른 “adult”. Not 윗어른 — this "
                   "is one of the few words where the 웃- form is standard."],
        ),
        "묘": dict(hanja="墓", meaning="a grave"),
        "영향": dict(
            hanja="影響", meaning="influence",
            characters=[("影", "영", "shadow — as in 영상 “image, video”"),
                        ("響", "향", "echo, sound")],
            notes=["Literally “shadow and echo” — what one thing leaves on "
                   "another."],
        ),
        "양보": dict(
            hanja="讓步", meaning="giving way, yielding",
            characters=[("讓", "양", "to yield"),
                        ("步", "보", "a step — as in 산책의 보행 “walking”")],
        ),
        "사례": dict(
            hanja="事例", meaning="a case, an instance",
            characters=[("事", "사", "affair, matter — as in 사건 “incident”, 사업"),
                        ("例", "례", "example — as in 예를 들어 “for example”")],
            notes=["The 사 here is 事, not the 私 of 사립 nor the 社 of 회사."],
        ),
        "공적": dict(
            hanja="公的", meaning="public, official",
            characters=[("公", "공", "public — as in 공공 “public”, 국·공립"),
                        ("的", "적", "-ic, -al — the ending that makes an "
                                    "adjective, as in 사회적, 적극적")],
            notes=["Its opposite is 사적(私的), private."],
        ),
        "말투": dict(
            meaning="a manner of speaking, tone",
            notes=["말 “speech” + 투 “manner, style”. The same 투 as in 글투, "
                   "the way someone writes."],
        ),
        "지위": dict(
            hanja="地位", meaning="position, standing",
            characters=[("地", "지", "ground, place — as in 지역 “region”"),
                        ("位", "위", "rank — as in 학위 “degree”, 순위")],
        ),
        "강조": dict(
            hanja="強調", meaning="emphasis",
            characters=[("強", "강", "strong — as in 강하다 “to be strong”"),
                        ("調", "조", "tune, tone — as in 조사 “survey”, 조절")],
        ),
        "고령화": dict(
            hanja="高齡化", meaning="population ageing",
            characters=[("高", "고", "high — as in 고등학교, 고속버스"),
                        ("齡", "령", "age, years — as in 연령 “age”"),
                        ("化", "화", "-isation — as in 도시화, 산업화")],
        ),
        "실질적": dict(
            hanja="實質的", meaning="substantive, in real terms",
            characters=[("實", "실", "real, fruit — as in 사실 “fact”, 실제"),
                        ("質", "질", "quality, substance — as in 품질 “quality”")],
        ),
        "향상": dict(
            hanja="向上", meaning="improvement",
            characters=[("向", "향", "to face, towards — as in 방향 “direction”"),
                        ("上", "상", "up — the same 上 as in 조상")],
        ),
        "혜택": dict(
            hanja="惠澤", meaning="a benefit",
            characters=[("惠", "혜", "favour, grace"),
                        ("澤", "택", "marsh, bounty")],
        ),
        "고궁": dict(
            hanja="古宮", meaning="an old royal palace",
            characters=[("古", "고", "old, ancient — as in 고대 “antiquity”"),
                        ("宮", "궁", "palace — as in 경복궁, 창덕궁")],
            notes=["The 고 here is 古 “ancient”, not the 高 “high” of 고령화."],
        ),
        "틀니": dict(
            meaning="dentures",
            notes=["Pure Korean, from 틀 “a frame” + 이 “tooth”."],
        ),
        "공동체 의식": dict(
            hanja="共同體意識", meaning="a sense of community",
            characters=[("共", "공", "together — as in 공공 “public”, 공동"),
                        ("同", "동", "same — as in 동일 “identical”, 동문"),
                        ("體", "체", "body — as in 단체 “organisation”, 정체성"),
                        ("識", "식", "to know — as in 지식 “knowledge”, 인식")],
        ),
        "농경": dict(
            hanja="農耕", meaning="agriculture, tilling",
            characters=[("農", "농", "farming — as in 농업, 농촌, 귀농"),
                        ("耕", "경", "to plough")],
        ),
        "두레": dict(
            meaning="a village work band",
            notes=["Pure Korean. The villagers put their labour together to "
                   "farm as one; the word survives in co-operative names such "
                   "as 두레생협."],
        ),
        "품앗이": dict(
            meaning="labour exchange between neighbours",
            notes=["From 품 “labour” + 앗이. You work a day on my field and I "
                   "work a day on yours — a debt in labour rather than money, "
                   "and unlike 두레 it is between two households."],
        ),
        "상부상조": dict(
            hanja="相扶相助", meaning="mutual aid",
            characters=[("相", "상", "mutual, each other — as in 상호 “mutual”"),
                        ("扶", "부", "to support, prop up"),
                        ("助", "조", "to help — as in 도움의 원조, 보조")],
            notes=["A four-character phrase: 相扶 “support each other”, 相助 "
                   "“help each other”."],
        ),
        "계기": dict(
            hanja="契機", meaning="an occasion, a turning point",
            characters=[("契", "계", "a bond, a contract — as in 계약 “contract”"),
                        ("機", "기", "machine, occasion — as in 기회 “chance”, 기관")],
        ),
        "외환": dict(
            hanja="外換", meaning="foreign exchange",
            characters=[("外", "외", "outside — as in 외국 “abroad”, 재외국민"),
                        ("換", "환", "to exchange — as in 교환 “exchange”, 환전")],
            notes=["외환 위기 is the 1997 Asian financial crisis, remembered in "
                   "Korea as the IMF 사태."],
        ),
        "극복": dict(
            hanja="克服", meaning="to overcome",
            characters=[("克", "극", "to conquer"),
                        ("服", "복", "clothes, to submit — as in 옷의 의복")],
        ),
        "대규모": dict(
            hanja="大規模", meaning="large scale",
            characters=[("規", "규", "rule, compass — as in 규제 “regulation”"),
                        ("模", "모", "pattern, model — as in 모방 “imitation”")],
        ),
        "연고": dict(
            hanja="緣故", meaning="a personal tie, a connection",
            characters=[("緣", "연", "a bond, an affinity — as in 인연, 혈연"),
                        ("故", "고", "reason, the old — as in 고향 “home town”")],
            notes=["The web of blood, place and school that puts two Koreans "
                   "in relation to each other: 혈연, 지연, 학연."],
        ),
        "혈연": dict(
            hanja="血緣", meaning="a blood tie",
            characters=[("血", "혈", "blood — as in 혈액 “blood”, 헌혈")],
        ),
        "지연": dict(
            hanja="地緣", meaning="a tie of place",
            characters=[("地", "지", "ground, place — the same 地 as in 지위")],
            notes=["Not to be confused with 지연(遲延), a delay."],
        ),
        "학연": dict(hanja="學緣", meaning="a tie of schooling"),
        "인연": dict(
            hanja="因緣", meaning="a tie, an affinity between people",
            characters=[("因", "인", "cause — as in 원인 “cause”, 요인")],
            notes=["Originally Buddhist: the causes and conditions that bring "
                   "two people together."],
        ),
        "본관": dict(
            hanja="本貫", meaning="the ancestral seat of a clan",
            characters=[("本", "본", "root, origin — as in 기본 “basic”, 본격적"),
                        ("貫", "관", "to pierce through, a lineage")],
            notes=["A Korean family name goes with a place: 안동 김씨 are the "
                   "Kims of Andong, 경주 이씨 the Lees of Gyeongju. Same name "
                   "and same 본관 means the same clan."],
        ),
        "성씨": dict(
            hanja="姓氏", meaning="a family name",
            characters=[("姓", "성", "surname"), ("氏", "씨", "clan, Mr/Ms")],
        ),
        "친족": dict(
            hanja="親族", meaning="kin, relatives",
            characters=[("親", "친", "close, parent — as in 친구 “friend”, 친목"),
                        ("族", "족", "clan, tribe — as in 가족 “family”, 민족")],
        ),
        "핏줄": dict(
            meaning="blood line",
            notes=["Pure Korean: 피 “blood” + 줄 “line”, with the ㅅ of the "
                   "compound. The everyday word for 혈연."],
        ),
        "공통점": dict(
            hanja="共通點", meaning="a point in common",
            characters=[("通", "통", "to pass through — as in 통신, 교통")],
        ),
        "친목": dict(
            hanja="親睦", meaning="fellowship, friendly relations",
            characters=[("睦", "목", "harmonious, on good terms")],
        ),
        "향우회": dict(
            hanja="鄕友會", meaning="a home-town association",
            characters=[("鄕", "향", "home village — as in 고향 “home town”"),
                        ("友", "우", "friend — as in 우정 “friendship”"),
                        ("會", "회", "meeting, society — as in 사회, 회사")],
        ),
        "동문회": dict(
            hanja="同門會", meaning="an alumni association",
            characters=[("同", "동", "same — as in 동일 “identical”"),
                        ("門", "문", "gate — as in 대문 “front gate”, 전문")],
            notes=["Literally “the society of the same gate” — those who went "
                   "in at the same school door."],
        ),
        "교류": dict(
            hanja="交流", meaning="exchange, keeping in touch",
            characters=[("交", "교", "to cross, exchange — as in 교통, 교환"),
                        ("流", "류", "to flow — as in 유행 “fashion”, 조류")],
        ),
        "적극적": dict(
            hanja="積極的", meaning="active, forward",
            characters=[("積", "적", "to pile up — as in 면적 “area”, 누적"),
                        ("極", "극", "extreme, pole — as in 극복, 적극")],
            notes=["Its opposite is 소극적, retiring — the pair appear "
                   "together in chapter 3."],
        ),
        "생활협동조합": dict(
            hanja="生活協同組合", meaning="a consumer co-operative",
            characters=[("協", "협", "to co-operate — as in 협약 “agreement”"),
                        ("組", "조", "to form, a group — as in 조직 “organisation”"),
                        ("合", "합", "to join — as in 통합 “integration”, 합격")],
            notes=["Shortened to 생협. 한살림, 두레생협 and ICOOP생협 are the "
                   "best known."],
        ),
        "조합원": dict(hanja="組合員", meaning="a member of a co-operative"),
        "공산품": dict(
            hanja="工産品", meaning="a manufactured article",
            characters=[("工", "공", "work, craft — as in 공업 “industry”, 공학"),
                        ("産", "산", "to produce — as in 생산, 산업체"),
                        ("品", "품", "goods, article — as in 품종, 상품")],
        ),
        "윤리적": dict(
            hanja="倫理的", meaning="ethical",
            characters=[("倫", "윤", "human relations, order"),
                        ("理", "리", "reason, principle — as in 이유 “reason”, 관리")],
        ),
        "실천": dict(
            hanja="實踐", meaning="putting into practice",
            characters=[("實", "실", "real — the same 實 as in 실질적"),
                        ("踐", "천", "to tread, to carry out")],
        ),
        "속담": dict(
            hanja="俗談", meaning="a proverb",
            characters=[("俗", "속", "custom, the common — as in 풍속 “custom”"),
                        ("談", "담", "to talk — as in 상담 “consultation”, 대담")],
            notes=["The three on this page all say the same thing about "
                   "pulling together. 백지장도 맞들면 낫다 — even a sheet of "
                   "paper is easier lifted at both ends — is the one an "
                   "English speaker already knows as “many hands make light "
                   "work”."],
        ),
        "교훈": dict(
            hanja="敎訓", meaning="a lesson, a moral",
            characters=[("訓", "훈", "to instruct — as in 훈련 “training”")],
        ),
        "풍자": dict(
            hanja="諷刺", meaning="satire",
            characters=[("諷", "풍", "to recite, to satirise"),
                        ("刺", "자", "to pierce — as in 자극 “stimulus”")],
        ),
        "정서": dict(
            hanja="情緖", meaning="sentiment, the feeling of a people",
            characters=[("情", "정", "feeling — as in 감정 “emotion”, 정보"),
                        ("緖", "서", "thread end, beginning")],
        ),
    },

    extraNotes=[
        "The 관련 단원 table on p. 76 merges 기본 and 문화 across its two rows. "
        "A merged cell cannot be expressed here, so both values repeat.",
        "The third row of the warm-up table is two lines of dialogue on the "
        "page — 할아버지 asking and 손자 answering. They are set on one line "
        "here.",
    ],
)
