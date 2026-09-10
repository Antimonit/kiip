# -*- coding: utf-8 -*-
"""Chapter 16 — The seasonal festivals.

No Google Doc: yours stop at chapter 12. Transcribed from the photos of
pp. 88-91, so the Korean here is my reading of the page rather than yours,
and any error in it is mine.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, LABELS, FIGURE, TABLE,
               CELL, GLOSSARY)

CHAPTER = dict(
    number=16, slug="16-seasonal-festivals",
    unit="문화", title="명절", titleEn="The seasonal festivals",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 세계 여러 나라의 대표적인 {명절} 모습입니다."),
        LABELS("{한국 추석}", "{필리핀 만성절}", "{미국 추수감사절}", "{중국 중추절}"),
        HEADING(4, "01 자신의 고향 나라의 대표적인 명절은 무엇입니까?"),
        HEADING(4, "02 한국에서 설날이나 추석을 보내면서 기억에 남는 일은 무엇입니까?"),

        SECTION("goals", "학습목표"),
        BULLET("한국의 대표적인 명절인 설날에 대해 설명할 수 있다.", ordered=True),
        BULLET("한국의 대표적인 명절인 추석에 대해 설명할 수 있다.", ordered=True),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", 2), "제목", "관련 내용"],
              [[CELL("기본", down=2), CELL("문화", down=2), "13. 전통 가치",
                "한국의 효와 예절"],
               ["15. 의례", "한국의 대표적인 의례, 제사"]]),

        SECTION("part", "01 설날에는 무엇을 할까?"),
        HEADING(2, "설날, 새해 복 많이 받으세요!"),
        GLOSSARY(("신정", "새로운 방식(서양식)에 따른 정월(1월) 첫날", "신정"),
              ("양력", "해(日)의 변화를 기준으로 날짜를 표기하는 방식", "양력"),
              ("음력", "달(月)의 변화를 기준으로 날짜를 표기하는 방식", "음력"),
              ("산소", "조상의 묘지를 높여 부르는 말", "산소"),
              ("세배", "설날 아침, 아랫사람이 윗사람에게 큰절로 인사드리는 것", "세배")),
        PARAGRAPH("한국에서는 “새해 복 많이 받으세요.”라는 새해 인사를 일 년에 두 번씩 한다. "
          "{신정}이라고 불리는 {양력} 1월 1일에 한 번, 그리고 {설날}이라고 불리는 {음력} "
          "1월 1일에 또 한 번을 한다. 신정에는 하루만 쉬지만, 설날에는 전날과 다음 날을 "
          "포함하여 3일을 쉰다. 설날은 한 해를 시작하면서 건강과 {풍요}를 {기원}하는 한국 "
          "최대 명절 중 하나이다."),
        PARAGRAPH("설날에는 조상에게 감사하는 마음을 담아 {차례}를 지낸다. 또한, 조상의 {산소}를 찾아 "
          "{성묘}를 하거나 {봉안당}, {추모 공원} 등을 방문하기도 한다. 설날 아침에는 부모님이나 "
          "{조부모}님 등 집안의 {윗사람}에게 {세배}를 하며 건강과 {장수}를 기원한다. 세배를 "
          "받은 윗사람은 자녀나 {손주} 등 {아랫사람}에게 새해에도 잘 지내라고 {덕담}을 하며 "
          "아이들에게는 {세뱃돈}을 준다."),
        PARAGRAPH("설날에는 {설빔}이라 하여 새로 옷이나 신발을 준비하기도 한다."),
        PARAGRAPH("요즘은 설 {연휴}를 보내는 모습도 바뀌고 있다. 여전히 설이 되면 멀리 떨어져 있던 "
          "가족이 모여 함께 시간을 보내는 모습이 일반적이지만, 최근에는 연휴를 이용해 "
          "{국내외} 여행을 떠나는 사람도 늘고 있다."),
        FIGURE("세배하는 모습"),

        HEADING(2, "설날의 대표적인 음식과 놀이"),
        GLOSSARY(("장수", "건강하게 오래 사는 것", "장수")),
        PARAGRAPH("설날 아침에 차례와 세배를 마친 후에는 {떡국}을 먹는다. 떡국은 흰 {가래떡}을 얇게 "
          "{썰어|썰다} 끓인 것으로 설날의 대표적인 음식이다. 흰 가래떡은 건강과 {장수}를 "
          "{상징}하며, 떡국 한 그릇을 먹으면 나이도 한 살 더 먹는다는 의미가 담겨 있다. 그리고 "
          "가족과 {친척}들이 함께 모여 {윷놀이} 등과 같은 {전통놀이}를 즐긴다."),
        FIGURE("설날 아침에 먹는 떡국"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "설날의 대표적인 전통놀이, 윷놀이", translation=
          "윷놀이, the game of 설날" "\n\n"
          "윷놀이 is the traditional Korean game many people enjoy at 설날. It "
          "is a kind of board game, made up of four wooden 윷 sticks, four "
          "pieces and a board. According to how many sticks land face up, "
          "from one to four, the throw is called 도, 개, 걸 or 윷; when none "
          "lands face up it is called 모. A piece is moved by the number of "
          "sticks that landed face up, and whoever gets all four of their "
          "pieces round the set path of the board and out first wins."),
        PARAGRAPH("{윷놀이}는 설날에 많은 사람들이 즐기는 대표적인 한국의 전통놀이다. 나무로 만든 "
          "{윷가락} 네 개와 윷 {말} 네 개, {윷판}으로 이루어진 일종의 보드게임이다. "
          "{뒤집어진|뒤집어지다} 개수에 따라 하나부터 네 개까지 도, 개, 걸, 윷이라고 부르며 "
          "모두 뒤집어지지 않았을 때는 모라고 한다. 윷가락이 뒤집어진 개수대로 윷 말을 "
          "움직이며, 윷 말 네 개가 윷판의 정해진 길을 다 돌고 먼저 나오면 이긴다."),

        SECTION("part", "02 추석에는 무엇을 할까?"),
        HEADING(2, "추석, 더도 말고 덜도 말고 한가위만 같아라!"),
        GLOSSARY(("수확", "농작물이나 성과를 거두어 들임", "수확"),
              ("햅쌀", "그 해에 새로 거둔 쌀", "햅쌀"),
              ("햇과일", "그 해에 새로 거둔 과일", "햇과일")),
        PARAGRAPH("{추석}은 음력 8월 15일이며, {한가위} 또는 {가배}라고도 불린다. 설날과 함께 한국에서 "
          "가장 큰 명절로 꼽힌다. 추석은 곡식을 {수확}하는 시기로 그 해 농사에 대해 감사하는 "
          "풍습에서 {유래}되었다. 설날과 마찬가지로 추석 전날과 다음 날을 포함한 3일이 "
          "{휴일}로 {지정}되어 있다. ‘더도 말고 덜도 말고 한가위만 같아라.’라는 속담이 있는데, "
          "이것은 수확 {무렵}이라 먹을 것이 많고 날씨도 좋은 추석을 옛사람들이 얼마나 "
          "좋아했는지 잘 보여준다."),
        PARAGRAPH("추석 아침에는 {햅쌀}과 {햇과일}, {송편} 등 많은 음식을 준비하여 {정성껏} 차례를 "
          "지내고 성묘를 한다. 일반적으로 추석이 되기 전에 조상의 산소를 미리 찾아 여름 동안 "
          "{무성하게|무성하다} 자란 풀을 깨끗하게 정리하는 {벌초}를 해 놓는다. 최근에는 "
          "{화장} 장례 비율이 늘어나면서 봉안당이나 추모 공원을 찾는 사람도 많다."),
        FIGURE("성묘하는 모습"),

        HEADING(2, "추석의 대표적인 음식과 놀이"),
        GLOSSARY(("강강술래", "추석날 밤에 여자들이 서로 손을 잡고 둥근 원을 그리면서 뛰는 민속놀이",
               "강강술래")),
        PARAGRAPH("추석의 대표적인 음식은 {송편}이다. 송편은 {멥쌀}가루로 {반죽}을 하고, {녹두}, 콩, "
          "{깨}, 팥 등을 넣고 {반달} 모양으로 {빚어낸|빚다} 떡이다. 송편을 찔 때는 {솔잎}을 "
          "넣는데, 그 이유는 송편끼리 붙는 것을 막아 모양 그대로를 {유지}할 수 있기 때문이다. "
          "또한 솔잎에 들어있는 {성분}이 송편이 쉽게 {상하는|상하다} 것을 막아준다."),
        PARAGRAPH("추석에 많이 했던 전통 놀이로는 {씨름}이나 {강강술래}를 꼽을 수 있다. 추석 밤에는 "
          "{보름달}을 보면서 {소원}을 비는 {달맞이}를 하는 사람도 많다."),
        FIGURE("추석의 대표음식, 송편"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "24절기를 알아볼까요?", translation=
          "Shall we look at the 24 solar terms?" "\n\n"
          "‘입춘’, which announces the start of spring, ‘경칩’, when the frogs "
          "come out, and ‘동지’, the longest night, when 팥죽 is cooked and "
          "eaten, are among the 24 solar terms. The 24 terms were made to "
          "divide the seasons by the position of the ecliptic, the path the "
          "sun travels, and were useful in a farming society greatly "
          "affected by the weather. They still help with farming today, and "
          "the food and the customs that go with them carry on in everyday "
          "life."),
        PARAGRAPH("봄의 시작을 알리는 ‘{입춘}’, 개구리가 튀어나온다는 ‘{경칩},’ 밤이 가장 길며 "
          "{팥죽}을 {쑤어|쑤다} 먹는 ‘{동지}’ 등은 {24절기} 중 하나이다. 24절기는 태양이 "
          "움직이는 길인 {황도}의 위치에 따라 계절적 구분을 하기 위해 만들어진 것인데 과거 "
          "날씨에 영향을 크게 받는 {농경}사회에 {유용하게|유용하다} 활용되었다. 24절기는 "
          "지금도 농사를 지을 때 도움을 받으며, 일상생활에서도 먹는 음식이나 풍습이 이어져 오고 "
          "있다."),
        TABLE(["계절", "절기"],
              [["봄", "입춘(立春), 우수(雨水), 경칩(驚蟄), 춘분(春分), 청명(淸明), 곡우(穀雨)"],
               ["여름", "입하(立夏), 소만(小滿), 망종(芒種), 하지(夏至), 소서(小暑), 대서(大暑)"],
               ["가을", "입추(立秋), 처서(處暑), 백로(白露), 추분(秋分), 한로(寒露), 상강(霜降)"],
               ["겨울", "입동(立冬), 소설(小雪), 대설(大雪), 동지(冬至), 소한(小寒), 대한(大寒)"]]),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 설날에는 무엇을 할까?"),
        BULLET("설날에는 새해를 맞이해서 새 옷이나 신발을 준비하기도 하는데 이를 (        )이라고 "
          "한다."),
        BULLET("설날 아침에 아랫사람이 윗사람에게 큰절로 인사드리는 것을 (        )라고 한다."),
        BULLET("(        )은 설날의 대표적인 음식으로 차례와 세배를 마친 후에 먹는다."),
        HEADING(3, "02 추석에는 무엇을 할까?"),
        BULLET("‘더도 말고 덜도 말고 (        )만 같아라’라는 속담은 추석과 같이 평생 먹을 것이 "
          "풍성하기를 기원하는 의미를 갖고 있다."),
        BULLET("추석의 대표적인 음식은 (        )으로 멥쌀가루로 반죽을 하고, 녹두, 콩, 깨, 팥 등을 "
          "넣고 반달 모양으로 만든 떡이다."),
        BULLET("추석 밤에는 보름달을 보면서 소원을 비는 (        )를 하는 사람도 많다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "새해 첫날, 세계 여러 나라에서는 어떤 음식을 먹을까?", translation=
          "On New Year’s Day, what do people eat around the world?" "\n\n"
          "Korea eats 떡국 at 설날, wishing for health and long life. "
          "Similarly, countries around the world begin the new year eating "
          "food that carries their hopes and expectations for the year. "
          "Here are some examples."),
        PARAGRAPH("한국은 설날에 떡국을 먹으며 건강과 장수를 기원한다. 이와 비슷하게 세계 각 나라에서는 "
          "한 해에 대한 {소망}과 기대를 담은 음식을 먹으며 새해를 시작한다. 그 예는 다음과 "
          "같다."),
        TABLE(["중국: 자오쯔", "베트남: 바인쯩", "미국: 호핑존", "스페인: 포도"],
              [["중국 전통 만두이며, 이 음식을 먹으면 귀와 입이 열려 복이 몸속으로 들어온다고 믿음",
                "찹쌀떡 안에 돼지고기와 녹두를 넣고 쪄서 만든 음식이며, 한 해의 안녕과 복을 기원함",
                "검은콩, 쌀, 돼지고기에 채소를 끓여 만든 음식이며, 부와 행운의 의미가 담겨있음",
                "신년 종소리에 맞춰 포도 12알을 먹으며, 1년 12달을 무사히 보내기를 기원함"]]),
        PARAGRAPH("★ 자신의 고향 나라에서 새해 첫날에 특별히 먹는 음식을 소개해 봅시다.",
          "Introduce the food eaten especially on New Year’s Day in your "
          "home country."),
    ],

    english={
        "설날, 새해 복 많이 받으세요!": dict(
            title="설날: may you receive much fortune in the new year",
            paragraphs=[
                "Koreans give the new year's greeting “새해 복 많이 받으세요” "
                "twice a year. Once on the first of January by the solar "
                "calendar, which is called 신정, and once again on the first "
                "of the first month by the lunar calendar, which is 설날. 신정 "
                "is a single day off; 설날 runs to three, taking in the day "
                "before and the day after. 설날 is one of the greatest of "
                "Korean festivals, wishing health and plenty on the year as "
                "it opens.",

                "At 설날 the 차례 rite is held, carrying the family's thanks "
                "to its ancestors. People also visit the ancestral graves to "
                "tend them, or go to a charnel house or a memorial park. On "
                "the morning of 설날 the 세배 bow is made to the elders of the "
                "household — parents, grandparents — with a wish for their "
                "health and long life. The elder who has received the bow "
                "gives the younger ones, children and grandchildren, words of "
                "blessing for the year to come, and gives the children money.",

                "새 옷 and shoes are sometimes got ready for 설날, which is "
                "called 설빔.",

                "The way the 설 holiday is spent is changing. The usual sight "
                "is still of a family gathered from far apart to spend the "
                "time together, but lately more people take the holiday to "
                "travel, at home or abroad.",
            ],
        ),
        "설날의 대표적인 음식과 놀이": dict(
            title="What is eaten and played at 설날",
            paragraphs=[
                "떡국 is eaten on the morning of 설날, once the 차례 and the "
                "세배 are done. It is made by slicing white 가래떡 thin and "
                "boiling it, and it is the dish of the day. The white 가래떡 "
                "stands for health and long life, and a bowl of 떡국 carries "
                "the sense of gaining a year of age. Family and relatives "
                "also gather to enjoy the old games, 윷놀이 among them.",
            ],
        ),
        "추석, 더도 말고 덜도 말고 한가위만 같아라!": dict(
            title="추석: neither more nor less, let it always be 한가위",
            paragraphs=[
                "추석 falls on the fifteenth of the eighth lunar month, and is "
                "also called 한가위 or 가배. With 설날 it is reckoned the "
                "greatest of Korean festivals. It comes at the time the grain "
                "is harvested, and grew out of the custom of giving thanks for "
                "the year's farming. As with 설날, three days are set as "
                "holiday, taking in the day before and the day after. There is "
                "a proverb — “neither more nor less, let it always be "
                "한가위” — which shows well how fond people once were of "
                "추석, when food was plentiful with the harvest in and the "
                "weather was fine.",

                "On the morning of 추석 a good deal of food is prepared — the "
                "new season's rice and fruit, 송편 and more — for the 차례 "
                "rite, done with care, and for tending the graves. Generally "
                "the ancestral graves are visited beforehand and the grass "
                "that has grown thick over the summer is cut back, which is "
                "called 벌초. Lately, as cremation has become the commoner "
                "funeral, many go to a charnel house or a memorial park "
                "instead.",
            ],
        ),
        "추석의 대표적인 음식과 놀이": dict(
            title="What is eaten and played at 추석",
            paragraphs=[
                "The dish of 추석 is 송편. It is a rice cake made by working a "
                "dough of non-glutinous rice flour, filling it with mung "
                "bean, soybean, sesame or red bean, and shaping it into a "
                "half-moon. Pine needles go in when 송편 is steamed, to keep "
                "the cakes from sticking to each other so that they hold "
                "their shape. What is in the needles also keeps the 송편 from "
                "spoiling quickly.",

                "Of the old games much played at 추석, 씨름 and 강강술래 stand "
                "out. On the night of 추석 many look at the full moon and make "
                "a wish, which is called 달맞이.",
            ],
        ),
    },

    extraAnnotations={
        "명절": dict(
            hanja="名節", meaning="a seasonal festival",
            characters=[("名", "명", "name — as in 이름의 성명, 유명"),
                        ("節", "절", "joint, season — as in 계절 “season”, 예절")],
            notes=["The great days of the lunar year — 설날 and 추석 above "
                   "all — as against 국경일, the national days fixed by "
                   "statute."],
        ),
        "한국 추석": dict(
            meaning="Chuseok, the Korean harvest festival",
            notes=["The subject of the chapter's second article."],
        ),
        "필리핀 만성절": dict(
            hanja="필리핀萬聖節", meaning="the Philippine All Saints' Day",
            characters=[("萬", "만", "ten thousand, all — as in 만세"),
                        ("聖", "성", "holy — as in 성당 “Catholic church”")],
            notes=["1 November. Families spend the day at the cemetery with "
                   "their dead, which is why the photo shows a graveyard."],
        ),
        "미국 추수감사절": dict(
            hanja="美國秋收感謝節", meaning="the American Thanksgiving",
            characters=[("秋", "추", "autumn — the same 秋 as in 추석"),
                        ("收", "수", "to gather in — as in 수확 “harvest”"),
                        ("感", "감", "to feel — as in 감사 “thanks”, 감정"),
                        ("謝", "사", "to thank, to apologise")],
        ),
        "중국 중추절": dict(
            hanja="中國中秋節", meaning="the Chinese Mid-Autumn Festival",
            characters=[("中", "중", "middle — as in 중학교, 중도 입국"),
                        ("秋", "추", "autumn — as in 추석, 추수")],
            notes=["The same day as 추석, the fifteenth of the eighth lunar "
                   "month — the Chinese festival that shares the date."],
        ),
        "설날": dict(
            meaning="Seollal, the lunar new year",
            notes=["설 “new year” + 날 “day”. Three days of holiday, and the "
                   "one occasion the whole country travels at once."],
        ),
        "신정": dict(
            hanja="新正", meaning="the solar new year, 1 January",
            characters=[("新", "신", "new — as in 신랑, 신문"),
                        ("正", "정", "correct; the first month — as in 정월")],
            notes=["Introduced under the Western calendar and kept as a "
                   "single day off, against 설날's three. Once called 구정 by "
                   "contrast — the “old new year” — a name now avoided."],
        ),
        "양력": dict(
            hanja="陽曆", meaning="the solar calendar",
            characters=[("陽", "양", "sun, positive — as in 태양 “the sun”, 양옥"),
                        ("曆", "력", "calendar — as in 달력 “calendar”")],
        ),
        "음력": dict(
            hanja="陰曆", meaning="the lunar calendar",
            characters=[("陰", "음", "shade, negative — the opposite of 陽")],
            notes=["설날, 추석 and the 절기 all run on this calendar, which is "
                   "why their dates move against the solar year."],
        ),
        "풍요": dict(
            hanja="豊饒", meaning="abundance, plenty",
            characters=[("豊", "풍", "abundant — as in 풍부하다 “plentiful”"),
                        ("饒", "요", "rich, generous")],
        ),
        "기원": dict(
            hanja="祈願", meaning="to pray for, to wish for",
            characters=[("祈", "기", "to pray — as in 기도 “prayer”"),
                        ("願", "원", "to wish — as in 소원 “a wish”")],
        ),
        "차례": dict(
            hanja="茶禮", meaning="the ancestral rite at a festival",
            characters=[("茶", "차", "tea — as in 녹차 “green tea”"),
                        ("禮", "례", "rite — as in 의례, 예절")],
            notes=["Literally “the tea rite”, held in the morning at 설날 and "
                   "추석. Its counterpart on the anniversary of a death is the "
                   "기제사."],
        ),
        "산소": dict(
            hanja="山所", meaning="an ancestral grave",
            characters=[("山", "산", "mountain — as in 등산 “hiking”, 배산임수"),
                        ("所", "소", "place — as in 장소 “place”, 소망")],
            notes=["The respectful word for a 묘. A different 산소(酸素) means "
                   "oxygen."],
        ),
        "성묘": dict(
            hanja="省墓", meaning="tending an ancestral grave",
            characters=[("省", "성", "to examine, to reflect"),
                        ("墓", "묘", "grave — as in 묘지 “cemetery”")],
        ),
        "봉안당": dict(
            hanja="奉安堂", meaning="a charnel house, a columbarium",
            notes=["Where ashes are kept after cremation. Also 납골당."],
        ),
        "추모 공원": dict(
            hanja="追慕公園", meaning="a memorial park",
            notes=["The other place cremated remains are laid, an alternative "
                   "to the 봉안당."],
        ),
        "조부모": dict(
            hanja="祖父母", meaning="grandparents",
            characters=[("祖", "조", "forefather — as in 조상 “ancestor”"),
                        ("父", "부", "father — as in 부모 “parents”"),
                        ("母", "모", "mother")],
        ),
        "윗사람": dict(
            meaning="one's senior, someone above one",
            notes=["The plain counterpart of 아랫사람. 웃어른 in chapter 13 is "
                   "the more formal word."],
        ),
        "아랫사람": dict(meaning="one's junior, someone below one"),
        "손주": dict(
            hanja="孫주", meaning="grandchildren",
            characters=[("孫", "손", "grandchild — as in 손자, 자손, 효손")],
            notes=["Covers grandsons and granddaughters together, where 손자 "
                   "and 손녀 name them apart."],
        ),
        "세배": dict(
            hanja="歲拜", meaning="the new year bow",
            characters=[("歲", "세", "year, age — as in 만 19세, 세월"),
                        ("拜", "배", "to bow — as in 숭배 “worship”")],
            notes=["The deep bow a younger person makes to an elder on the "
                   "morning of 설날. The money that comes back is 세뱃돈."],
        ),
        "세뱃돈": dict(
            meaning="new year money",
            notes=["세배 + 돈, with the ㅅ of the compound. Given to children "
                   "by the elders they have bowed to."],
        ),
        "덕담": dict(
            hanja="德談", meaning="words of blessing",
            characters=[("德", "덕", "virtue — as in 덕분 “thanks to”"),
                        ("談", "담", "to talk — as in 상담, 속담")],
            notes=["What an elder says back after receiving a 세배 — a wish "
                   "for the year, spoken as though already true."],
        ),
        "장수": dict(
            hanja="長壽", meaning="long life",
            characters=[("長", "장", "long — as in 장기 “long term”"),
                        ("壽", "수", "long life — as in 수명 “lifespan”")],
        ),
        "설빔": dict(
            meaning="new clothes for 설날",
            notes=["설 + 빔, from 비음 “finery”. Clothes, and often shoes, put "
                   "on new for the new year."],
        ),
        "연휴": dict(
            hanja="連休", meaning="consecutive holidays",
            characters=[("連", "련", "to connect — as in 연결 “connection”, 연립"),
                        ("休", "휴", "to rest — as in 휴일 “holiday”, 방학")],
        ),
        "국내외": dict(
            hanja="國內外", meaning="at home and abroad",
            characters=[("內", "내", "inside — as in 내국인 “a national”"),
                        ("外", "외", "outside — as in 외국 “abroad”, 재외국민")],
        ),
        "떡국": dict(
            meaning="tteokguk, sliced rice-cake soup",
            notes=["Eaten on the morning of 설날. Eating a bowl is spoken of "
                   "as gaining a year — 한 살 더 먹는다."],
        ),
        "가래떡": dict(
            meaning="garaetteok, a long cylindrical rice cake",
            notes=["Sliced across into ovals for 떡국. Its whiteness is what "
                   "stands for health and long life."],
        ),
        "상징": dict(
            hanja="象徵", meaning="a symbol; to stand for",
            characters=[("象", "상", "shape, elephant — as in 현상 “phenomenon”"),
                        ("徵", "징", "sign — as in 특징 “characteristic”")],
        ),
        "윷놀이": dict(
            meaning="yutnori, the four-stick game",
            notes=["A board game played at 설날 with four wooden sticks, four "
                   "pieces and a board. The throw is read from how many "
                   "sticks land face up."],
        ),
        "윷가락": dict(meaning="one of the four sticks of 윷놀이"),
        "윷판": dict(meaning="the board of 윷놀이"),
        "말": dict(
            meaning="a piece, a counter (in a board game)",
            notes=["The same word as 말 “horse” — the piece is thought of as "
                   "a horse moving round the board. Not the 말 of 말투 "
                   "“speech”."],
        ),
        "뒤집어지다": dict(
            meaning="to be turned over, to land face up",
            notes=["What the 윷 sticks do. From 뒤집다 “to turn over”."],
        ),
        "전통놀이": dict(
            hanja="傳統놀이", meaning="a traditional game",
            characters=[("傳", "전", "to hand down — as in 전통 “tradition”"),
                        ("統", "통", "to unify, govern — as in 통합, 대통령")],
        ),
        "추석": dict(
            hanja="秋夕", meaning="Chuseok, the harvest festival",
            characters=[("秋", "추", "autumn — as in 추수 “harvest”"),
                        ("夕", "석", "evening")],
            notes=["Literally “the autumn evening”, for the full moon it "
                   "falls on."],
        ),
        "한가위": dict(
            meaning="Hangawi, the native name for 추석",
            notes=["한 “great” + 가위, an old word for the middle of autumn. "
                   "The pure-Korean name beside the Sino-Korean 추석."],
        ),
        "가배": dict(
            hanja="嘉排", meaning="Gabae, an old name for 추석",
            notes=["The name recorded in the Samguk Sagi for the festival, "
                   "said to date from the reign of Silla's third king."],
        ),
        "수확": dict(
            hanja="收穫", meaning="harvest",
            characters=[("收", "수", "to gather in — as in 수입 “income”"),
                        ("穫", "확", "to reap")],
        ),
        "유래": dict(
            hanja="由來", meaning="origin; to originate in",
            characters=[("由", "유", "cause, from — as in 이유 “reason”, 자유"),
                        ("來", "래", "to come — as in 미래 “future”, 내일")],
        ),
        "휴일": dict(
            hanja="休日", meaning="a holiday, a day off",
            characters=[("休", "휴", "to rest — the same 休 as in 연휴")],
        ),
        "지정": dict(
            hanja="指定", meaning="to designate",
            characters=[("指", "지", "finger, to point — as in 지시 “instruction”"),
                        ("定", "정", "to fix — as in 결정 “decision”, 정착")],
        ),
        "무렵": dict(
            meaning="around the time of",
            notes=["A bound noun: 수확 무렵 “around harvest time”, 저녁 무렵 "
                   "“towards evening”."],
        ),
        "햅쌀": dict(
            meaning="the new season's rice",
            notes=["From 해 “year” + 쌀. The first rice of the year's "
                   "harvest, which is what the 차례 is set with."],
        ),
        "햇과일": dict(
            meaning="the new season's fruit",
            notes=["The same 햇- as 햅쌀, and as 햇살, 햇빛."],
        ),
        "정성껏": dict(
            meaning="with all one's care",
            notes=["From 정성 “devoted care” + -껏 “to the utmost”. The way a "
                   "rite is meant to be performed."],
        ),
        "무성하다": dict(
            hanja="茂盛하다", meaning="to grow thick, to be rank",
            characters=[("茂", "무", "luxuriant"),
                        ("盛", "성", "flourishing — as in 성행 “prevalence”")],
        ),
        "벌초": dict(
            hanja="伐草", meaning="cutting the grass on a grave",
            characters=[("伐", "벌", "to cut down, to fell"),
                        ("草", "초", "grass — as in 화초, 초가집")],
            notes=["Done in the weeks before 추석, so that the grave is clean "
                   "when the family comes to tend it."],
        ),
        "화장": dict(
            hanja="火葬", meaning="cremation",
            characters=[("火", "화", "fire — as in 화재 “fire”"),
                        ("葬", "장", "funeral rites — as in 장례, 매장")],
        ),
        "송편": dict(
            hanja="松편", meaning="songpyeon, a half-moon rice cake",
            characters=[("松", "송", "pine tree")],
            notes=["The 松 is the pine whose needles it is steamed on — which "
                   "is what the article goes on to explain."],
        ),
        "멥쌀": dict(
            meaning="non-glutinous rice",
            notes=["Ordinary rice, as against 찹쌀, the sticky kind. 송편 is "
                   "made from 멥쌀 flour; 인절미 from 찹쌀."],
        ),
        "반죽": dict(meaning="dough; to knead"),
        "녹두": dict(hanja="綠豆", meaning="mung bean"),
        "깨": dict(meaning="sesame"),
        "반달": dict(
            meaning="a half moon",
            notes=["반 “half” + 달 “moon” — the shape 송편 is folded into."],
        ),
        "솔잎": dict(
            meaning="pine needles",
            notes=["솔 is the native word for the pine; 松 is its character. "
                   "The needles keep the cakes apart and keep them fresh."],
        ),
        "유지": dict(
            hanja="維持", meaning="to maintain, to keep",
            characters=[("維", "유", "to tie, to sustain"),
                        ("持", "지", "to hold — as in 지속 “continuation”")],
        ),
        "성분": dict(
            hanja="成分", meaning="a component, a constituent",
            characters=[("成", "성", "to form — as in 성장, 구성"),
                        ("分", "분", "part — as in 부분 “part”, 신분")],
        ),
        "상하다": dict(meaning="to spoil, to go off"),
        "씨름": dict(
            meaning="ssireum, Korean wrestling",
            notes=["Two wrestlers grip a belt at the waist and try to throw "
                   "each other. The great match of the year was held at 추석."],
        ),
        "강강술래": dict(
            meaning="ganggangsullae, a circle dance",
            notes=["Women join hands and circle under the full moon of 추석, "
                   "singing. Listed by UNESCO as intangible cultural "
                   "heritage."],
        ),
        "보름달": dict(
            meaning="the full moon",
            notes=["보름 is the fifteenth of a lunar month, which is when the "
                   "moon is full — and the date of 추석."],
        ),
        "소원": dict(
            hanja="所願", meaning="a wish",
            characters=[("所", "소", "that which — as in 소망, 장소"),
                        ("願", "원", "to wish — as in 기원 “to pray for”")],
        ),
        "달맞이": dict(
            meaning="daremaji, greeting the moon",
            notes=["달 “moon” + 맞이 “meeting”, the same 맞이 as in 손님맞이. "
                   "Looking at the full moon of 추석 and making a wish."],
        ),
        "24절기": dict(
            hanja="二十四節氣", meaning="the twenty-four solar terms",
            characters=[("節", "절", "joint, division — as in 명절, 계절"),
                        ("氣", "기", "air, energy — as in 기후 “climate”, 기온")],
            notes=["The solar year cut into twenty-four, six to a season. "
                   "They run on the sun rather than the moon, which is why "
                   "they fall on nearly the same date every year."],
        ),
        "입춘": dict(
            hanja="立春", meaning="the beginning of spring",
            characters=[("立", "립", "to stand, to set up — as in 설립, 국립"),
                        ("春", "춘", "spring — as in 청춘 “youth”")],
            notes=["The first of the twenty-four terms, around 4 February. "
                   "The 立 of 입춘, 입하, 입추 and 입동 opens each season."],
        ),
        "경칩": dict(
            hanja="驚蟄", meaning="the waking of the insects",
            characters=[("驚", "경", "to be startled — as in 경악"),
                        ("蟄", "칩", "to hibernate")],
            notes=["Around 5 March: the term at which hibernating creatures "
                   "are startled awake — the frogs the page mentions."],
        ),
        "동지": dict(
            hanja="冬至", meaning="the winter solstice",
            characters=[("冬", "동", "winter — as in 동면 “hibernation”"),
                        ("至", "지", "to reach, the extreme — as in 지극")],
            notes=["The longest night, around 22 December. 팥죽 is eaten on "
                   "it, the red bean warding off ill luck."],
        ),
        "팥죽": dict(
            meaning="red bean porridge",
            notes=["Eaten at 동지. The red of the beans was held to keep bad "
                   "spirits off — the same thinking as the 팥고물 on 이사떡."],
        ),
        "쑤다": dict(
            meaning="to cook (porridge), to boil down",
            notes=["The verb used only of 죽 and the like: 죽을 쑤다."],
        ),
        "황도": dict(
            hanja="黃道", meaning="the ecliptic",
            characters=[("黃", "황", "yellow — as in 황색"),
                        ("道", "도", "way, road — as in 도로 “road”, 수도")],
            notes=["The path the sun appears to travel over the year. The "
                   "twenty-four terms divide it into twenty-four."],
        ),
        "농경": dict(
            hanja="農耕", meaning="agriculture, tilling",
            characters=[("農", "농", "farming — as in 농업, 농촌"),
                        ("耕", "경", "to plough")],
        ),
        "유용하다": dict(
            hanja="有用하다", meaning="to be useful",
            characters=[("有", "유", "to have — as in 유명 “famous”, 고유"),
                        ("用", "용", "to use — as in 이용 “use”, 활용")],
        ),
        "소망": dict(
            hanja="所望", meaning="a hope, a wish",
            characters=[("望", "망", "to look far, to hope — as in 희망 “hope”")],
        ),
        "친척": dict(
            hanja="親戚", meaning="relatives",
            characters=[("親", "친", "close, kin — as in 친구, 친족"),
                        ("戚", "척", "kinsman")],
        ),
        "썰다": dict(meaning="to slice, to cut up"),
        "빚다": dict(
            meaning="to shape (dough), to mould",
            notes=["Used of 송편, 만두 and pottery alike — shaping something "
                   "soft by hand."],
        ),
    },

    extraNotes=[
        "The 24절기 box on p. 90 is a table of four seasons against six terms "
        "each; the terms are set as one cell a season rather than one cell a "
        "term, which is how the page prints them.",
        "The four new-year dishes on p. 91 each have a photograph under the "
        "description. The photographs are not reproduced.",
        "The page prints ‘경칩,’ with the comma inside the closing quotation "
        "mark, which is the book's own slip. It is set as printed.",
    ],
)
