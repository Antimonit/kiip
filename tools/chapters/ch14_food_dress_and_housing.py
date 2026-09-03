# -*- coding: utf-8 -*-
"""Chapter 14 — Traditional food, dress and housing.

No Google Doc: yours stop at chapter 12. Transcribed from the photos of
pp. 80-83, so the Korean here is my reading of the page rather than yours,
and any error in it is mine.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, MARGIN, FIGURE,
               TABLE, CELL, GLOSSARY, CHART)

CHAPTER = dict(
    number=14, slug="14-food-dress-and-housing",
    unit="문화", title="전통 의식주", titleEn="Traditional food, dress and housing",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 세계 여러 지역에 있는 {한식당}의 개수와 변화를 나타낸 것입니다."),
        CHART("전 세계 한식당 운영 현황(농림축산식품부·한식진흥원, 2017)(단위: 개) — 90개 "
              "국가에서 33,499개의 한식당이 운영되고 있음. 아시아 안에서는 중국이 "
              "15,985개(47.7%), 일본이 9,238개(27.6%)를 차지한다.", "개",
              [("아시아", 28151), ("북중미", 3850), ("유럽", 864),
               ("오세아니아", 392), ("남미", 157), ("중동", 57), ("아프리카", 28)]),
        HEADING(4, "01 자신의 고향 나라에 있는 한식당에서 먹어 본 한국 음식은 무엇입니까? "
             "한국에 와서 한국 음식을 처음 먹어 보았다면 가장 맛있게 먹은 음식은 무엇입니까?"),
        HEADING(4, "02 자신의 고향 나라 음식과 한국 음식의 공통점과 차이점은 무엇입니까?"),

        SECTION("goals", "학습목표"),
        BULLET("한국의 음식 종류와 특징을 설명할 수 있다.", ordered=True),
        BULLET("한복과 한옥의 특징을 설명할 수 있다.", ordered=True),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", 2), "제목", "관련 내용"],
              [["기본", "문화", "16. 명절", "설날과 추석"]]),

        SECTION("part", "01 한국 음식의 종류와 특징은 무엇일까?"),
        MARGIN("{전골}", "{국물}", "{찌개}"),
        HEADING(2, "한국 음식의 종류와 특징"),
        GLOSSARY(("토양", "흙(농작물이 자랄 수 있는 흙)", "토양"),
              ("특유", "특별히 가지고 있음", "특유"),
              ("발효", "효모 등과 같은 미생물의 작용으로 분해하는 것", "발효")),
        PARAGRAPH("한국인은 “밥 먹었어?”, “식사는 하셨어요?”라는 질문으로 {안부} 인사를 대신하기도 할 "
          "만큼 일상생활에서 음식 먹는 것을 중요하게 여긴다. 한국 음식은 기본적으로 밥, {국}, "
          "{반찬} 등으로 구성된다. 밥과 국은 {숟가락}으로, 반찬은 {젓가락}으로 먹는 것이 "
          "일반적이다."),
        PARAGRAPH("한국의 {주식}은 쌀로 만든 밥이다. 한국의 {토양}과 {기후}는 {벼농사}에 "
          "{적합하다}. 밥을 먹을 때는 국이나 반찬과 함께 먹는다. 국은 고기, 해물, 채소 등 "
          "{재료}를 물에 넣고 푹 끓여 만든 음식으로, 그 재료에 따라 {특유}의 맛이 난다. 그 "
          "밖에 {탕}, {찌개}, {전골} 등을 먹기도 하며, 국에 밥을 말아 먹는 ‘{국밥}’도 하나의 "
          "요리로 {정착}되었다."),
        PARAGRAPH("반찬은 밥을 먹을 때 함께 먹는 음식으로 가장 대표적인 것은 김치다. 김치는 {배추}, "
          "{무}, 오이 등의 채소를 소금에 {절이고|절이다} {양념}을 {버무려|버무리다} "
          "{발효}시킨 음식이다. 몸에 좋은 {영양소}를 골고루 갖추고 있어 전 세계에서 "
          "{인정받는|인정받다} 건강 식품이다. 김치는 지역에 따라 넣는 재료와 만드는 방식이 "
          "다양하다. 겨울이 되기 전 11월말~12월초에 많은 양의 김치를 한꺼번에 "
          "{담그는|담그다} {김장}의 풍습은 지금까지 이어져 내려오고 있다."),
        PARAGRAPH("또 다른 발효 음식인 {된장}, {간장}, {고추장} 같은 {장류}나 {새우젓}, 오징어젓 "
          "등의 {젓갈류}도 반찬으로 먹거나 다른 반찬을 만드는 데 많이 사용된다. 또한 채소를 "
          "양념과 섞어 만든 {나물}, {김}이나 생선 구이, 고기류를 재료로 해서 만든 음식도 "
          "한국인이 많이 먹는 반찬이다."),
        FIGURE("한상차림"),
        FIGURE("김치"),

        HEADING(2, "다양한 한국 음식과 한식의 세계화"),
        GLOSSARY(("K-Food", "Korean-Food의 약자로, 한국 음식, 한국 식품 및 한식 문화를 포함한 것",
               "K-Food")),
        PARAGRAPH("한국에는 밥, 국, 반찬으로 이루어진 기본적인 {식단} 외에 특별히 요리로 만들어 먹는 "
          "음식도 많다. {비빔밥}, {삼계탕}, {불고기}, {삼겹살}, {떡국} 등이 그 예이다. "
          "최근에는 한국 음식이 방송이나 인터넷 등을 통해 해외에 더욱 널리 알려지면서 "
          "{K-Food}란 이름으로 인기를 끌고 있다. 이와 함께 한국 음식을 세계 곳곳에 "
          "{보급}하고자 하는 ‘{한식}의 {세계화}’도 진행되고 있다."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "한국인이 즐겨 먹는 전통 음식, 떡"),
        PARAGRAPH("한국인은 예로부터 쌀과 같은 {곡식}을 이용해서 {떡}을 만들어 먹었다. 떡은 명절, "
          "{제사}, 생일잔치, {손님맞이}를 할 때 특히 많이 먹는 음식이다. 가족, 이웃, "
          "친척들과 함께 나누어 먹기도 하고 선물을 하는 경우도 많다. 재료와 만드는 방법에 따라 "
          "떡의 종류는 매우 다양한데 {인절미}, {송편}, {가래떡} 등이 대표적이다. 아기가 태어난 "
          "지 {백일}이 되거나 1년이 된 것을 기념할 때는 {백설기}를, 새로운 곳으로 이사를 간 "
          "사람은 이웃에게 {시루떡}을 나누어 주기도 한다."),

        SECTION("part", "02 한복과 한옥의 특징은 무엇일까?"),
        HEADING(2, "한복의 특징"),
        MARGIN("{생활한복}"),
        PARAGRAPH("{한복}은 예부터 전해 내려오는 한국 {고유}의 옷이다. 오늘날 한복의 모습은 "
          "{조선시대} 중반에 만들어진 것으로 알려져 있다. 한복을 입을 때 기본적으로 여자는 "
          "{치마}와 {저고리}를, 남자는 {바지}와 저고리를 입는다. 저고리 위에 여자는 {배자}를, "
          "남자는 {조끼}를 입으며, 외출할 때 여자는 {마고자}, 남자는 {두루마기}를 입는다."),
        PARAGRAPH("한복은 계절에 따라 {옷감}이 다르다. 여름에는 바람이 잘 통하는 {삼베}나 {모시}로 "
          "옷을 만들어 시원하게 입었고, 겨울에는 {솜}이나 {비단}으로 옷을 만들어 따뜻하게 "
          "입었다."),
        PARAGRAPH("오늘날 한복은 설날이나 추석 같은 명절, {돌잔치}, 결혼식 등 특별하고 중요한 날에만 "
          "입는 옷이 되었다. 대부분의 사람들이 집 밖에서 활동하는 시간이 많기 때문에 한복보다는 "
          "활동하기에 더 편한 옷을 많이 입는다. 한편, 한복의 전통적인 디자인을 따르면서도 "
          "{활동성}과 {실용성}을 높인 {생활한복}도 꾸준히 인기를 끌고 있다."),
        FIGURE("여자 한복과 남자 한복"),

        HEADING(2, "한옥의 특징"),
        MARGIN("{온돌}", "{대청마루}"),
        SOURCE("* 출처: 두산백과"),
        PARAGRAPH("{한옥}은 한국의 전통적인 생활 모습이 {반영}된 집이다."),
        PARAGRAPH("한옥은 {지붕}을 만드는 재료에 따라 {기와집}과 {초가집}으로 나뉜다. 기와집은 흙으로 "
          "만들어 구운 {기와}를 지붕에 {얹은|얹다} 집으로 과거에 주로 {신분}이 높은 사람이 "
          "살았다. 초가집은 지붕에 {볏짚}이나 {억새} 등과 같은 풀을 얹은 집으로 과거에 주로 "
          "{서민}들이 많이 살았다."),
        PARAGRAPH("한옥에는 {온돌}과 {대청마루}가 있다. 온돌은 {아궁이}에 불을 때어 방을 따뜻하게 하는 "
          "{난방} 장치에 해당한다. 대청마루는 방과 방 사이에 긴 {널빤지}를 깔아 만든 공간이다. "
          "겨울에는 온돌을 이용해 따뜻하게 만든 방에서 주로 생활하고, 여름에는 시원하고 바람이 "
          "잘 통하는 대청마루에서 더위를 피했다."),
        FIGURE("기와집의 모습"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "한국의 조상들이 선호했던 집의 위치"),
        MARGIN("{배산임수}"),
        PARAGRAPH("한국인은 남쪽을 향해 지은 {남향집}을 좋아한다. 남향집에 {햇볕}이 잘 들기 때문이다. "
          "또한 과거에는 집 앞에 강이나 {냇물}이 흐르고, 뒤에는 산이 있는 곳을 "
          "{선호하였다|선호하다}. {뒷산} 덕분에 겨울철 찬 바람을 막고 {땔감}을 쉽게 구할 수 "
          "있으며 생활이나 농사에 필요한 물을 쉽게 구할 수 있어서 편리했다. 이런 곳은 좋은 "
          "장소라는 의미에서 {명당}이라고 불렸다."),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 한국 음식의 종류와 특징은 무엇일까?"),
        BULLET("한국 음식은 기본적으로 (        ), (        ), (        )으로 구성된다."),
        BULLET("(        )이란 겨울이 되기 전, 11월 말~12월 초에 많은 양의 김치를 담그는 풍습을 "
          "말한다."),
        BULLET("한국에는 김치, 각종 장류, 젓갈류와 같은 (        ) 음식을 반찬으로 많이 먹는다."),
        HEADING(3, "02 한복과 한옥의 특징은 무엇일까?"),
        BULLET("한복은 한국 고유의 옷으로 남자 한복은 (        )와 (        ), 여자 한복은 "
          "(        )와 (        )를 기본으로 한다."),
        BULLET("한옥은 지붕의 재료에 따라 (        )과 (        )으로 구분된다."),
        BULLET("한옥은 한국의 전통적인 생활 모습을 반영한 집이다. 방을 따뜻하게 해주는 (        )과 "
          "여름을 시원하게 보낼 수 있는 (        )가 있다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "한국의 식사예절에는 무엇이 있을까?"),
        BULLET("웃어른이 먼저 수저를 들 때까지 기다린다."),
        BULLET("밥그릇이나 국그릇을 손으로 들고 먹지 않는다."),
        BULLET("기침이나 {재채기}는 얼굴을 옆으로 돌리고 손으로 입을 가리고 한다."),
        BULLET("숟가락과 젓가락을 동시에 들지 않고 한 번에 하나씩만 들고 사용한다."),
        BULLET("입안에 음식이 있을 때는 {가급적} 말하지 않는다."),
        BULLET("사용하던 수저로 반찬을 너무 {뒤적이지|뒤적이다} 않고 깨끗이 집어서 먹는다."),
        PARAGRAPH("★ 자신의 고향 나라와 한국의 식사예절의 공통점과 차이점에 대해 이야기해 봅시다."),
    ],

    english={
        "한국 음식의 종류와 특징": dict(
            title="Korean food: its kinds and its character",
            paragraphs=[
                "Koreans set enough store by eating in daily life that “Have "
                "you eaten?” or “Have you had your meal?” can stand in for "
                "asking how someone is. A Korean meal is made up basically of "
                "rice, soup and side dishes. The rice and the soup are "
                "generally eaten with a spoon, the side dishes with "
                "chopsticks.",

                "The Korean staple is rice. Korea's soil and climate suit "
                "growing it. Rice is eaten together with soup or with side "
                "dishes. 국 is made by putting meat, seafood or vegetables "
                "into water and simmering them long, and it takes its "
                "particular flavour from whatever went in. There are also "
                "탕, 찌개 and 전골, and 국밥 — rice stirred into the soup — has "
                "settled into a dish in its own right.",

                "Of the side dishes eaten with rice, the great one is kimchi. "
                "Kimchi is made by salting vegetables such as Chinese "
                "cabbage, radish or cucumber, mixing seasoning through them "
                "and letting them ferment. It carries a full range of "
                "nutrients and is recognised the world over as a healthy "
                "food. What goes into it and how it is made vary from region "
                "to region. The custom of 김장 — putting down a great "
                "quantity at once from late November to early December, "
                "before the winter — has come down to the present day.",

                "Other fermented foods are used as side dishes or in making "
                "them: the pastes, such as 된장, 간장 and 고추장, and the "
                "salted seafoods, such as 새우젓 and 오징어젓. Vegetables "
                "dressed with seasoning as 나물, laver, grilled fish and "
                "dishes made from meat are also side dishes Koreans eat a "
                "great deal of.",
            ],
        ),
        "다양한 한국 음식과 한식의 세계화": dict(
            title="The range of Korean food, and its going out into the world",
            paragraphs=[
                "Besides the basic table of rice, soup and side dishes, Korea "
                "has many dishes prepared as dishes in their own right. "
                "비빔밥, 삼계탕, 불고기, 삼겹살 and 떡국 are examples. Korean food "
                "has lately become far better known abroad through broadcast "
                "and the internet, and has taken hold under the name K-Food. "
                "Along with it, a campaign to spread Korean food across the "
                "world — the “globalisation of 한식” — is under way.",
            ],
        ),
        "한복의 특징": dict(
            title="What marks out the 한복",
            paragraphs=[
                "The 한복 is the dress proper to Korea, handed down from "
                "early times. Its present shape is understood to have been "
                "settled in the middle of the Joseon period. Worn plainly, a "
                "woman puts on the 치마 and the 저고리, a man the 바지 and the "
                "저고리. Over the 저고리 a woman wears the 배자 and a man the "
                "조끼, and going out a woman wears the 마고자, a man the "
                "두루마기.",

                "The cloth changes with the season. In summer it was made "
                "from hemp or ramie, which the wind passes through, and worn "
                "cool; in winter from padded cotton or from silk, and worn "
                "warm.",

                "Today the 한복 has become a dress worn only on days that are "
                "special and important — the seasonal festivals such as 설날 "
                "and 추석, a first-birthday party, a wedding. Since most "
                "people spend much of their time out of the house, they "
                "mostly wear clothes easier to move in. Meanwhile the "
                "생활한복, which keeps to the traditional design while making "
                "it easier to move and wear, holds its popularity steadily.",
            ],
        ),
        "한옥의 특징": dict(
            title="What marks out the 한옥",
            paragraphs=[
                "The 한옥 is a house in which the traditional Korean way of "
                "living is reflected.",

                "한옥 divide, by what the roof is made of, into the 기와집 and "
                "the 초가집. The 기와집 has fired clay tiles laid on the roof, "
                "and was lived in mostly by people of high rank. The 초가집 "
                "has grasses such as rice straw or silver grass laid on the "
                "roof, and was lived in mostly by common people.",

                "A 한옥 has the 온돌 and the 대청마루. The 온돌 amounts to a "
                "heating system: a fire is lit in the 아궁이 and warms the "
                "room. The 대청마루 is a space made by laying long boards "
                "between one room and another. In winter people lived mostly "
                "in the room the 온돌 kept warm; in summer they escaped the "
                "heat on the 대청마루, which is cool and open to the wind.",
            ],
        ),
    },

    extraAnnotations={
        "숟가락": dict(
            meaning="a spoon",
            notes=["Together with 젓가락 it makes 수저. The Korean spoon is "
                   "for rice and soup; almost everything else is picked up "
                   "with chopsticks."],
        ),
        "젓가락": dict(
            meaning="chopsticks",
            notes=["Korean chopsticks are metal and flat, unlike the wooden "
                   "Chinese and Japanese kinds."],
        ),
        "적합하다": dict(
            hanja="適合하다", meaning="to be suited to",
            characters=[("適", "적", "suitable — as in 적성 “aptitude”, 적응"),
                        ("合", "합", "to join, fit — as in 통합, 조합원")],
        ),
        "재료": dict(
            hanja="材料", meaning="an ingredient, material",
            characters=[("材", "재", "material, timber — as in 인재 “talent”"),
                        ("料", "료", "material, fee — as in 요리 “cooking”, 수수료")],
        ),
        "배추": dict(
            meaning="Chinese cabbage",
            notes=["The cabbage of 김장 kimchi. 배추김치 is what is meant when "
                   "someone says kimchi without qualifying it."],
        ),
        "무": dict(
            meaning="Korean radish",
            notes=["Short, thick and white, not the small red radish. Used in "
                   "kimchi, in soups and pickled on its own as 깍두기."],
        ),
        "절이다": dict(
            meaning="to salt down, to pickle",
            notes=["The first step of making kimchi: the salt draws the water "
                   "out of the leaves."],
        ),
        "버무리다": dict(meaning="to mix together, to toss (with seasoning)"),
        "인정받다": dict(
            hanja="認定받다", meaning="to be recognised, acknowledged",
            characters=[("認", "인", "to recognise — as in 인식, 확인"),
                        ("定", "정", "to fix — as in 결정, 확정 일자")],
        ),
        "담그다": dict(
            meaning="to put down (kimchi, sauce); to soak",
            notes=["김치를 담그다 is the set phrase — one does not 만들다 kimchi."],
        ),
        "된장": dict(
            meaning="doenjang, fermented soybean paste",
            notes=["What is left of the soybeans after the liquid is drawn "
                   "off as 간장."],
        ),
        "간장": dict(
            meaning="soy sauce",
            notes=["간 “saltiness” + 장 “paste”. Made in the same crock as "
                   "된장 and separated from it."],
        ),
        "고추장": dict(
            meaning="gochujang, red chilli paste",
            notes=["고추 “chilli” + 장. Sweet as well as hot, from the malted "
                   "grain fermented with it."],
        ),
        "새우젓": dict(
            meaning="salted fermented shrimp",
            notes=["Used as a seasoning rather than eaten alone — a spoonful "
                   "goes into kimchi and into soups."],
        ),
        "김": dict(
            meaning="laver, dried seaweed sheets",
            notes=["Toasted and salted, eaten with rice. The same syllable is "
                   "also “steam” and a common surname."],
        ),
        "비빔밥": dict(
            meaning="bibimbap, rice mixed with vegetables",
            notes=["From 비비다 “to mix” + 밥. Rice under 나물, an egg and "
                   "고추장, stirred together at the table."],
        ),
        "삼계탕": dict(
            hanja="蔘鷄湯", meaning="samgyetang, chicken and ginseng soup",
            characters=[("蔘", "삼", "ginseng"), ("鷄", "계", "chicken"),
                        ("湯", "탕", "soup — the same 湯 as in 탕")],
            notes=["Eaten in the hottest days of summer, on the principle of "
                   "meeting heat with heat."],
        ),
        "불고기": dict(
            meaning="bulgogi, marinated grilled beef",
            notes=["불 “fire” + 고기 “meat”. Sweetened with soy and pear."],
        ),
        "삼겹살": dict(
            hanja="三겹살", meaning="samgyeopsal, pork belly",
            notes=["Literally “three-layered flesh”, for the bands of fat and "
                   "meat. Grilled at the table."],
        ),
        "떡국": dict(
            meaning="tteokguk, sliced rice-cake soup",
            notes=["Eaten at 설날; eating a bowl is spoken of as gaining a "
                   "year."],
        ),
        "한식": dict(
            hanja="韓食", meaning="Korean food",
            characters=[("韓", "한", "Korea — as in 한복, 한옥"),
                        ("食", "식", "food — as in 식사 “meal”, 식품")],
        ),
        "떡": dict(
            meaning="tteok, rice cake",
            notes=["Grain steamed and usually pounded. Not a cake in the "
                   "Western sense — it is chewy rather than crumbly."],
        ),
        "손님맞이": dict(
            meaning="receiving guests",
            notes=["손님 “guest” + 맞이 from 맞다 “to meet, receive”."],
        ),
        "치마": dict(meaning="a skirt"),
        "바지": dict(meaning="trousers"),
        "조끼": dict(meaning="a waistcoat, vest"),
        "지붕": dict(meaning="a roof"),
        "기와": dict(
            meaning="a roof tile",
            notes=["Clay shaped and fired. 기와집 is the house roofed with "
                   "them."],
        ),
        "얹다": dict(meaning="to lay on top of, to place on"),
        "선호하다": dict(
            hanja="選好하다", meaning="to prefer",
            characters=[("選", "선", "to choose — as in 선발 “selection”, 선택"),
                        ("好", "호", "to like, good — as in 호감 “liking”")],
        ),
        "뒷산": dict(
            meaning="the hill behind (a house or village)",
            notes=["뒤 “behind” + 산, with the ㅅ of the compound. The 산 of "
                   "배산임수."],
        ),
        "뒤적이다": dict(
            meaning="to rummage, to poke about in",
            notes=["Turning the food over in a shared dish looking for the "
                   "best piece — the thing the last rule warns against."],
        ),
        "한식당": dict(
            hanja="韓食堂", meaning="a Korean restaurant",
            characters=[("韓", "한", "Korea — as in 한국, 한복, 한옥"),
                        ("食", "식", "food, to eat — as in 식사 “meal”, 식품"),
                        ("堂", "당", "hall — as in 식당 “restaurant”, 봉안당")],
        ),
        "안부": dict(
            hanja="安否", meaning="news of someone's wellbeing",
            characters=[("安", "안", "peace, safe — as in 안전 “safety”, 안정"),
                        ("否", "부", "or not, no — as in 여부 “whether or not”")],
            notes=["Literally “well or not”. 안부 인사 is the asking after "
                   "someone that “Have you eaten?” stands in for."],
        ),
        "주식": dict(
            hanja="主食", meaning="a staple food",
            characters=[("主", "주", "main, master — as in 주요 “main”, 집주인")],
            notes=["Not to be confused with 주식(株式), a share in a company."],
        ),
        "토양": dict(
            hanja="土壤", meaning="soil",
            characters=[("土", "토", "earth — as in 국토 “national territory”"),
                        ("壤", "양", "soil, ground")],
        ),
        "기후": dict(
            hanja="氣候", meaning="climate",
            characters=[("氣", "기", "air, energy — as in 기분 “mood”, 인기"),
                        ("候", "후", "season, weather")],
        ),
        "벼농사": dict(
            meaning="rice farming",
            notes=["벼 is the growing plant, 쌀 the uncooked grain, 밥 the "
                   "cooked rice — three separate words where English has "
                   "one."],
        ),
        "특유": dict(
            hanja="特有", meaning="peculiar to, characteristic",
            characters=[("特", "특", "special — as in 특별 “special”, 특징"),
                        ("有", "유", "to have — as in 유명 “famous”, 고유")],
        ),
        "국": dict(
            meaning="soup",
            notes=["The thinnest of the three: 국 is a clear soup eaten with "
                   "rice, 찌개 is thicker and shared from the pot, 전골 is "
                   "cooked at the table."],
        ),
        "찌개": dict(
            meaning="a thick stew",
            notes=["Saltier and thicker than 국, set in the middle of the "
                   "table for everyone."],
        ),
        "전골": dict(
            meaning="a hotpot cooked at the table",
            notes=["The ingredients are arranged raw in a shallow pan and "
                   "simmered in front of the diners."],
        ),
        "국물": dict(
            meaning="the liquid of a soup or stew",
            notes=["국 + 물 “water”. The broth as against the solids in it."],
        ),
        "탕": dict(
            hanja="湯", meaning="a soup simmered long",
            notes=["The Sino-Korean word beside the native 국, and generally "
                   "richer: 삼계탕, 갈비탕, 설렁탕."],
        ),
        "국밥": dict(
            meaning="rice in soup",
            notes=["Rice served in the broth rather than beside it — the "
                   "quickest of Korean meals."],
        ),
        "반찬": dict(
            hanja="飯饌", meaning="a side dish",
            characters=[("飯", "반", "cooked rice"),
                        ("饌", "찬", "a prepared dish")],
        ),
        "정착": dict(
            hanja="定着", meaning="to settle, to take hold",
            characters=[("定", "정", "to fix — as in 결정 “decision”, 확정 일자"),
                        ("着", "착", "to attach — as in 도착 “arrival”, 재정착")],
        ),
        "발효": dict(
            hanja="醱酵", meaning="fermentation",
            characters=[("醱", "발", "to ferment"), ("酵", "효", "yeast, leaven")],
            notes=["The 효 here is 酵 “yeast”, not the 孝 of filial duty in "
                   "chapter 13."],
        ),
        "김장": dict(
            meaning="the winter kimchi-making",
            notes=["The one great batch put down in late November or early "
                   "December to last the winter. Listed by UNESCO as "
                   "intangible cultural heritage."],
        ),
        "양념": dict(
            meaning="seasoning",
            notes=["The mixture — chilli, garlic, ginger, salted seafood — "
                   "worked through the salted vegetables."],
        ),
        "영양소": dict(
            hanja="營養素", meaning="a nutrient",
            characters=[("營", "영", "to manage, run — as in 운영 “operation”"),
                        ("養", "양", "to nourish — as in 양육, 양성"),
                        ("素", "소", "element, plain — as in 요소 “element”")],
        ),
        "장류": dict(
            hanja="醬類", meaning="the fermented soy pastes",
            characters=[("醬", "장", "paste, sauce — the 장 of 된장, 간장, 고추장"),
                        ("類", "류", "kind, class — as in 종류 “kind”, 인류")],
        ),
        "젓갈류": dict(
            meaning="salted, fermented seafood",
            notes=["젓갈 is seafood salted down and left to ferment; 새우젓 is "
                   "shrimp, 오징어젓 squid. A spoonful goes into kimchi."],
        ),
        "나물": dict(
            meaning="seasoned vegetables",
            notes=["A vegetable blanched or raw, dressed with 양념. The "
                   "several small dishes on a 비빔밥 are 나물."],
        ),
        "식단": dict(
            hanja="食單", meaning="a menu, the make-up of a meal",
            characters=[("單", "단", "single, a list — as in 단독 “single”, 명단")],
        ),
        "K-Food": dict(
            meaning="K-Food",
            notes=["Short for Korean Food, and covering the dishes, the "
                   "packaged foods and the culture around them together — "
                   "formed like K-pop and K-drama."],
        ),
        "보급": dict(
            hanja="普及", meaning="to spread, to disseminate",
            characters=[("普", "보", "widely, universal — as in 보통 “ordinary”"),
                        ("及", "급", "to reach")],
        ),
        "세계화": dict(
            hanja="世界化", meaning="globalisation",
            characters=[("世", "세", "world, generation — as in 세대 “generation”"),
                        ("界", "계", "boundary, world — as in 한계 “limit”"),
                        ("化", "화", "-isation — as in 도시화, 고령화")],
        ),
        "곡식": dict(
            hanja="穀食", meaning="grain",
            characters=[("穀", "곡", "grain — as in 곡물 “cereals”")],
        ),
        "제사": dict(
            hanja="祭祀", meaning="the memorial rite for an ancestor",
            characters=[("祭", "제", "rite, festival — as in 축제 “festival”"),
                        ("祀", "사", "to sacrifice, to offer")],
        ),
        "인절미": dict(
            meaning="injeolmi, a soft pounded rice cake",
            notes=["Steamed glutinous rice pounded and rolled in bean "
                   "powder."],
        ),
        "송편": dict(
            hanja="松편", meaning="songpyeon, a half-moon rice cake",
            characters=[("松", "송", "pine tree")],
            notes=["Steamed on a bed of pine needles, which is where the 松 "
                   "comes from. Eaten at 추석."],
        ),
        "가래떡": dict(
            meaning="garaetteok, a long cylindrical rice cake",
            notes=["Sliced across into ovals to make 떡국."],
        ),
        "백설기": dict(
            meaning="baekseolgi, a plain white steamed rice cake",
            notes=["Its pure white stands for a clean start, which is why it "
                   "is made for a baby's hundredth day and first birthday."],
        ),
        "시루떡": dict(
            meaning="siruttteok, a steamed layer cake with red bean",
            notes=["The cake shared with the neighbours on moving house — "
                   "chapter 5's 이사떡."],
        ),
        "백일": dict(
            hanja="百日", meaning="the hundredth day after a birth",
            notes=["Marked because a baby surviving its first hundred days "
                   "once meant the worst danger had passed."],
        ),
        "한복": dict(
            hanja="韓服", meaning="hanbok, Korean dress",
            characters=[("服", "복", "clothes — as in 의복 “clothing”, 교복")],
        ),
        "고유": dict(
            hanja="固有", meaning="proper to, native",
            characters=[("固", "고", "firm, solid — as in 고정 “fixed”"),
                        ("有", "유", "to have — the same 有 as in 특유")],
        ),
        "조선시대": dict(
            hanja="朝鮮時代", meaning="the Joseon period (1392-1897)",
            characters=[("朝", "조", "morning, dynasty"),
                        ("鮮", "선", "fresh, bright")],
        ),
        "저고리": dict(
            meaning="jeogori, the upper garment of the 한복",
            notes=["Worn by both men and women; what differs is what goes "
                   "below it — 치마 for a woman, 바지 for a man."],
        ),
        "배자": dict(hanja="褙子", meaning="baeja, a woman's sleeveless overjacket"),
        "마고자": dict(meaning="magoja, a woman's outdoor jacket"),
        "두루마기": dict(
            meaning="durumagi, a man's long outer coat",
            notes=["Pure Korean, from 두루 “all round” — a coat closed all "
                   "the way round."],
        ),
        "옷감": dict(
            meaning="cloth, fabric",
            notes=["옷 “clothes” + 감 “material”. The same 감 as in 땔감, "
                   "firewood."],
        ),
        "삼베": dict(meaning="hemp cloth"),
        "모시": dict(meaning="ramie cloth"),
        "비단": dict(hanja="緋緞", meaning="silk"),
        "솜": dict(meaning="cotton wool, padding"),
        "돌잔치": dict(
            meaning="a first-birthday party",
            notes=["돌 is the first anniversary of a birth; 잔치 is a feast."],
        ),
        "활동성": dict(hanja="活動性", meaning="ease of movement"),
        "실용성": dict(
            hanja="實用性", meaning="practicality",
            characters=[("實", "실", "real — as in 실질적, 사실"),
                        ("用", "용", "to use — as in 이용 “use”, 활용")],
        ),
        "생활한복": dict(
            hanja="生活韓服", meaning="everyday hanbok",
            notes=["A 한복 cut for ordinary wear: the traditional lines kept, "
                   "the fastenings and the fabric made practical."],
        ),
        "한옥": dict(
            hanja="韓屋", meaning="hanok, a traditional Korean house",
            characters=[("屋", "옥", "house — as in 양옥 “Western-style house”")],
        ),
        "반영": dict(
            hanja="反映", meaning="to reflect",
            characters=[("反", "반", "opposite, back — as in 반대 “opposite”"),
                        ("映", "영", "to shine, project — as in 영화 “film”")],
        ),
        "기와집": dict(
            meaning="a tile-roofed house",
            notes=["기와 are fired clay roof tiles. The house of the "
                   "well-born, as against the 초가집."],
        ),
        "초가집": dict(
            hanja="草家집", meaning="a thatched house",
            characters=[("草", "초", "grass — as in 약초 “medicinal herb”"),
                        ("家", "가", "house, family — as in 가족, 국가")],
        ),
        "신분": dict(
            hanja="身分", meaning="social rank, status",
            characters=[("身", "신", "body, self — as in 신체 “body”, 신분증"),
                        ("分", "분", "to divide, part — as in 부분 “part”, 분산")],
        ),
        "서민": dict(
            hanja="庶民", meaning="the common people",
            characters=[("庶", "서", "common, numerous"),
                        ("民", "민", "people — as in 국민, 이주민")],
        ),
        "볏짚": dict(meaning="rice straw"),
        "억새": dict(meaning="silver grass, eulalia"),
        "온돌": dict(
            hanja="溫突", meaning="ondol, underfloor heating",
            characters=[("溫", "온", "warm — as in 온도 “temperature”, 기온"),
                        ("突", "돌", "to protrude, a chimney")],
            notes=["Smoke from the 아궁이 is drawn under the stone floor, "
                   "which holds the heat. It is why Koreans sit and sleep on "
                   "the floor rather than on furniture."],
        ),
        "대청마루": dict(
            hanja="大廳마루", meaning="the main wooden-floored hall",
            characters=[("大", "대", "great — as in 대규모, 대학교"),
                        ("廳", "청", "hall, office — as in 교육청 “education office”")],
            notes=["An open floored space between the rooms, raised off the "
                   "ground so the air moves under it — the summer counterpart "
                   "to the 온돌."],
        ),
        "아궁이": dict(
            meaning="the firebox of an 온돌",
            notes=["The mouth where the fire is lit, usually in the kitchen; "
                   "the same fire cooks and heats the floor next door."],
        ),
        "난방": dict(
            hanja="煖房", meaning="heating",
            characters=[("煖", "난", "warm"), ("房", "방", "room — as in 방 “room”")],
            notes=["Its opposite is 냉방, cooling."],
        ),
        "널빤지": dict(meaning="a wooden plank"),
        "배산임수": dict(
            hanja="背山臨水", meaning="mountain behind, water in front",
            characters=[("背", "배", "back — as in 배경 “background”"),
                        ("山", "산", "mountain — as in 등산 “hiking”"),
                        ("臨", "임", "to face, to look out on"),
                        ("水", "수", "water — as in 수도 “water supply”, 홍수")],
            notes=["The four-character phrase for the ideal siting of a "
                   "house: the hill at its back, the stream before it. The "
                   "page describes it without naming it."],
        ),
        "남향집": dict(
            hanja="南向집", meaning="a south-facing house",
            characters=[("南", "남", "south — as in 남미 “South America”"),
                        ("向", "향", "to face — as in 방향 “direction”, 향상")],
        ),
        "명당": dict(
            hanja="明堂", meaning="an auspicious site",
            characters=[("明", "명", "bright, clear — as in 설명 “explanation”"),
                        ("堂", "당", "hall, place — as in 식당, 봉안당")],
            notes=["From geomancy: the spot where the land's energy gathers. "
                   "Used loosely now of any prime location."],
        ),
        "땔감": dict(
            meaning="firewood",
            notes=["From 때다 “to burn (fuel)” + 감 “material”, the same 감 as "
                   "in 옷감."],
        ),
        "냇물": dict(meaning="a stream, a brook"),
        "햇볕": dict(
            meaning="sunlight, the warmth of the sun",
            notes=["햇볕 is the sun's warmth on the skin; 햇빛 is its light. "
                   "The page wants the warmth."],
        ),
        "재채기": dict(meaning="a sneeze"),
        "가급적": dict(
            hanja="可及的", meaning="as far as possible",
            characters=[("可", "가", "possible — as in 가능 “possible”, 불가피"),
                        ("及", "급", "to reach — the same 及 as in 보급")],
        ),
    },

    extraNotes=[
        "Chapter 14 has no Google Doc: the Korean is transcribed from the "
        "photos of pp. 80-83 rather than from a transcription of yours, so "
        "mistakes in it are mine and it is worth reading against the pages.",
        "The warm-up on p. 80 is a world map with a bubble over each region "
        "and a small bar chart of 2009, 2014 and 2017 beside it. Only the "
        "2017 totals are drawn here, as one bar per region; the China and "
        "Japan figures are given in the caption.",
        "The six rules of table manners on p. 83 each sit beside a drawing. "
        "The drawings are not reproduced, so the rules are set as a list.",
    ],
)
