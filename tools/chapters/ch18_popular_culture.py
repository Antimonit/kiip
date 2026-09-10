# -*- coding: utf-8 -*-
"""Chapter 18 — Popular culture.

No Google Doc: yours stop at chapter 12. Transcribed from the photos of
pp. 96-99, so the Korean here is my reading of the page rather than yours,
and any error in it is mine.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, LABELS, FIGURE, TABLE,
               CELL, GLOSSARY)

CHAPTER = dict(
    number=18, slug="18-popular-culture",
    unit="문화", title="대중문화", titleEn="Popular culture",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 일상생활에서 나누는 대화의 한 {장면}입니다."),
        FIGURE("네 컷의 만화 — 친구들이 K-드라마 추천, 영화 개봉, 좋아하는 배우의 굿즈, "
            "프로야구 경기에 대해 이야기하는 장면"),
        LABELS("{정주행}", "{개봉}", "{굿즈}", "{프로야구팀}"),
        HEADING(4, "01 자신이 좋아하는 한국의 대중문화는 무엇입니까?"),
        HEADING(4, "02 자신의 고향 나라에서 인기 있는 대중문화는 무엇입니까?"),

        SECTION("goals", "학습목표"),
        BULLET("한국의 대중문화 종류와 특징을 설명할 수 있다.", ordered=True),
        BULLET("세계인이 좋아하는 한국 대중문화를 설명할 수 있다.", ordered=True),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", 2), "제목", "관련 내용"],
              [["기본", "문화", "19. 여가문화", "여가활동 참여하기"]]),

        SECTION("part", "01 한국에는 어떤 대중문화가 있을까?"),
        HEADING(2, "대중문화의 의미와 대중 매체와의 관계"),
        GLOSSARY(("대중 매체", "불특정의 많은 사람들에 대량의 정보를 전달하는 매체로 텔레비전, "
                          "신문, 라디오, 인터넷 등을 말함", "대중 매체"),
              ("SNS", "Social Network Service의 약자로 특정한 관심이나 활동을 공유하는 "
                      "사람들 사이의 관계망을 구축해 주는 온라인 서비스", "SNS")),
        PARAGRAPH("많은 사람이 즐기고 {누리는|누리다} 문화를 {대중문화}라고 한다. 대중문화에는 드라마, "
          "영화, 노래, {공연}, {전시}, 스포츠 경기, 게임 등이 있다. 또한 사람들의 옷이나 머리 "
          "모양 등과 같은 일상생활에서 볼 수 있는 {유행}도 여기에 포함된다. 한국의 대중문화는 "
          "특히 {대중 매체}와 관련이 깊다. TV, 라디오, 책, 신문은 물론 스마트폰을 {기반}으로 "
          "하는 {SNS} 등과 같은 대중 매체의 발달로 자신이 좋아하는 대중문화를 쉽게 {접할|접하다} "
          "수 있고 많은 사람들과 {공유}하기도 한다."),

        HEADING(2, "한국의 대중문화"),
        GLOSSARY(("사극", "역사 또는 역사 인물을 소재로 한 드라마", "사극"),
              ("멀티플렉스(MULTIPLEX)", "두 개 이상의 스크린을 가진 영화관", "멀티플렉스")),
        PARAGRAPH("한국인은 드라마를 즐겨 본다. 매일 아침과 저녁, 밤 시간에 방송되는 드라마 수가 "
          "{수십} 편에 이른다. {사극}, 로맨스, 스릴러 등 {장르}도 다양하다. {시청자}들은 배우의 "
          "{대사}나 옷에도 관심을 많이 갖는데 이는 금방 유행되기도 한다."),
        PARAGRAPH("한국인은 음악과 노래도 좋아한다. 특히, 많은 사람들이 즐겨 듣거나 부를 수 있도록 "
          "만들어진 노래인 ‘{가요}’를 즐겨 듣는다. 가요에는 {발라드}, 댄스, R&B, 힙합, "
          "{트로트} 등 다양한 장르가 있으며, {특정한|특정하다} 시기에 인기를 끄는 ‘{유행가}’도 "
          "자주 등장한다."),
        PARAGRAPH("영화도 한국의 중요한 대중문화 중 하나이다. 2000년대 무렵에 {멀티플렉스} 형태의 "
          "{영화관}이 늘어나면서 {관객} 수가 {급격히|급격하다} 성장하였다. 2018년 기준으로 "
          "한국에는 영화관이 약 500여 개 있으며, {연간} 영화관 관객 수는 2억 1639만 명으로 전 "
          "세계 5위에 {해당}한다. 또한 한국에서 {제작}한 영화는 한국뿐 아니라 해외 여러 "
          "나라에서 {상영}되고 있다."),
        PARAGRAPH("스포츠에서는 {프로} 야구와 프로 축구, 프로 농구와 프로 배구가 인기가 높다. 야구와 "
          "축구는 봄부터 가을, 농구와 배구는 가을부터 봄까지 경기가 진행된다."),
        FIGURE("드라마 ‘도깨비’ 포스터"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "한국의 ‘방’ 문화를 즐겨보셨나요?", translation=
          "Have you enjoyed Korea’s ‘방’ culture?" "\n\n"
          "Korea has a distinctive ‘방’ culture. Walk down the street and "
          "you will easily find a 노래방, a PC방, a 찜질방, a 만화방. The PC방 in "
          "particular spread widely once the internet arrived in the late "
          "1990s. What people mostly do at a PC방 is play games, and lately, "
          "as games have settled in as a part of popular culture, they are "
          "called ‘e-sports’. The 찜질방, where the traditional 온돌 can be "
          "felt, is also visited a great deal with friends, colleagues and "
          "family." "\n\n"
          "Lately, as the technology has improved, more people are visiting "
          "indoor baseball grounds and driving ranges that use screens. And "
          "this distinctive ‘방’ culture is often introduced abroad, so it "
          "has become an important part of the trip for foreigners visiting "
          "Korea."),
        PARAGRAPH("한국에는 {독특한|독특하다} ‘{방}’ 문화가 있다. 길거리를 걷다 보면 {노래방}, "
          "{PC방}, {찜질방}, {만화방} 등을 쉽게 {발견}할 수 있다. 특히, PC방은 1990년대 "
          "{후반} 이후 인터넷이 {보급}되면서 널리 퍼지게 되었다. PC방에서는 주로 게임을 많이 "
          "하는데 최근에는 게임도 하나의 대중문화로 자리 잡으면서 ‘{e스포츠}’로 불리고 있다. "
          "또한 전통 {온돌}문화를 느낄 수 있는 찜질방 역시 친구나 {동료}, 가족들과 함께 많이 "
          "찾는다."),
        PARAGRAPH("최근에는 기술이 발전함에 따라 {실내} 스크린을 {활용}한 야구장이나 {골프연습장}을 "
          "방문하는 사람들도 늘어나고 있다. 그리고 다른 나라에도 이러한 독특한 ‘방’ 문화가 자주 "
          "소개되어 한국을 찾는 외국인에게도 중요한 여행 {코스}가 되고 있다."),

        SECTION("part", "02 세계인이 좋아하는 한국 대중문화에는 무엇이 있을까?"),
        HEADING(2, "한류의 시작"),
        GLOSSARY(("한류", "한국의 대중문화, 즉 한국에서 제작된 드라마, 영화, 방송, 음악, 옷, 음식, "
                      "패션 등이 해외에서 널리 소비되는 문화적 현상", "한류")),
        PARAGRAPH("‘한국’ 하면 어떤 것이 {떠오르는지|떠오르다}에 대한 질문에 외국인들은 주로 드라마, "
          "K-POP, 한국 음식이라고 답했다. 2000년 {전후}, 한국의 영화와 드라마가 아시아 여러 "
          "나라로 {수출}되면서 한국의 대중문화와 {연예인}에 대한 관심이 높아지게 되었다. 이렇게 "
          "한국의 대중문화가 여러 나라로 {확산}되면서 {대중적} 인기를 끌게 된 {현상}을 "
          "{한류}(韓流, Korean wave)라고 한다."),

        HEADING(2, "세계인들이 좋아하는 한국 대중문화"),
        GLOSSARY(("예능 프로그램", "오락적인 내용으로 재미와 웃음을 주는 방송프로그램",
               "예능 프로그램")),
        PARAGRAPH("한국 {가수}들이 해외로 {진출}하면서 K-POP(케이팝)의 성장도 눈에 {띈다|띄다}. "
          "K-POP의 인기 {요인}으로는 가수들의 {매력적}인 {외모}와 스타일, 따라 부르기에 신나는 "
          "{가사}와 {리듬}, {뛰어난|뛰어나다} 춤 {실력}을 꼽을 수 있다. K-POP의 인기는 한국에 "
          "대한 {흥미}와 {호기심}으로 이어지면서 한국어와 한국문화를 배우는 외국인이 늘어나고 "
          "있다."),
        PARAGRAPH("한편, 비빔밥, 김치, {떡볶이}, 삼겹살, 불고기 등 여러 종류의 {특색} 있는 한국 음식에 "
          "대해서도 외국인들은 큰 관심을 보이고 있다. 한국 음식은 줄여서 ‘{한식}’이라고 "
          "부르는데, 외국인 {관광객}을 대상으로 전통 시장에서 한식을 {맛보거나|맛보다} 한식 "
          "요리 만들기를 직접 {체험}해 볼 수 있는 프로그램도 인기를 끌고 있다."),
        PARAGRAPH("또한 한국의 {스타}들이 하는 {화장법}이나 패션 등을 좋아하는 사람들이 늘어나고 있다. "
          "이는 ‘K-BEAUTY’와 ‘K-FASHION’ 등 새로운 한류의 {유형}으로 {주목} 받고 있다."),
        PARAGRAPH("그 밖에 {태권도}를 중심으로 한 한국의 스포츠와 {독창적}이고 다양한 장르의 영화도 "
          "{꾸준한|꾸준하다} 관심을 받고 있다. 특히, 최근에 여러 한국 영화들이 주요 국제 "
          "{영화제}에서 {수상}함으로써 {작품성}도 인정받고 있다. 또한 드라마뿐 아니라 한국의 "
          "{예능 프로그램} 형식이 해외로 수출되었고, {현지} 환경에 맞게 {리메이크}되어 큰 "
          "{호평}을 받고 있다."),
        FIGURE("2019 빌보드 뮤직 어워드에서 수상한 BTS(방탄소년단) (사진 출처: 〈연합뉴스〉)"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "제92회 아카데미 영화제 작품상 등 4관왕을 수상한 영화 ‘기생충’", translation=
          "‘Parasite’, winner of four prizes at the 92nd Academy Awards, "
          "Best Picture among them" "\n\n"
          "‘Parasite’, directed by Bong Joon-ho and starring Song Kang-ho, "
          "took the Palme d’Or, the top prize at the 72nd Cannes Film "
          "Festival, and then won in four categories at the 92nd Academy "
          "Awards: Best Picture, Best Director, Best Original Screenplay "
          "and Best International Feature. ‘Parasite’ tells the story of a "
          "rich family and a poor one, and was judged to combine artistry, "
          "popular appeal and craft in equal measure. Bong Joon-ho’s "
          "acceptance speech at the American Golden Globes, where the film "
          "won Best Foreign Language Film — “once you overcome the "
          "one-inch-tall barrier of subtitles, you can see so many more "
          "films, and all films are connected” — moved a great many people "
          "around the world."),
        PARAGRAPH("{봉준호} {감독}, {송강호} {주연}의 한국 영화 ‘{기생충}’이 제72회 {칸 영화제} "
          "최고상인 {황금종려상}에 이어 제92회 {아카데미 영화제}에서 {작품상}, {감독상}, "
          "{각본상}, {국제영화상} 등 4개 부분에서 수상하였다. 영화 ‘기생충’은 부자 가족과 가난한 "
          "가족의 이야기를 담고 있으며, 작품성과 {대중성}, {예술성}을 골고루 갖추었다는 평가를 "
          "받았다. 한편, 미국 {골든글로브} {시상식}에서 {외국어영화상}을 받은 봉준호 감독의 "
          "“1인치 정도 되는 {자막}의 {장벽}을 넘으면 여러분이 훨씬 더 많은 영화를 볼 수 있으며, "
          "영화는 모두 {연결}돼 있다”라는 {수상 소감}은 세계 많은 사람에게 큰 {감동}을 전해 "
          "주었다."),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 한국에는 어떤 대중문화가 있을까?"),
        BULLET("많은 사람들이 즐기고 누리는 문화를 (        )라고 한다."),
        BULLET("한국 가요 중 특정한 시기에 인기를 끄는 노래를 (        )라고 한다."),
        BULLET("한국의 스포츠 중에서 대표적으로 인기 있는 종목은 (        ), (        ), 프로 농구, "
          "프로 배구이다."),
        HEADING(3, "02 세계인이 좋아하는 한국 대중문화에는 무엇이 있을까?"),
        BULLET("드라마, 영화, 방송, 음악, 옷 등 한국의 대중문화가 세계 여러 나라로 확산되어 대중적 "
          "인기를 얻게 된 현상을 (        )라고 한다."),
        BULLET("한국의 가수들이 해외로 진출하면서 (        )이 크게 성장하고 있다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "한국인에게 사랑 받은 한국 영화", translation=
          "Korean films Koreans have loved" "\n\n"
          "A film is brought to completion through the work of its "
          "director, its crew and its actors. It also carries the culture of "
          "the country where it was made, and the feeling and the concerns "
          "its people can share. Films that more than ten million people "
          "have seen in Korea — ‘Miracle in Cell No. 7’, ‘Ode to My "
          "Father’, ‘Along with the Gods: The Two Worlds’ — were loved so "
          "widely because these elements are well expressed in them." "\n\n"
          "‘Miracle in Cell No. 7’, which unfolds a father’s love for his "
          "daughter with deep feeling and laughter; ‘Ode to My Father’, "
          "which draws the story of an ordinary father who lived his whole "
          "life for his family alone, from after the Korean War in the "
          "1950s down to the present; and ‘Along with the Gods: The Two "
          "Worlds’, which holds the culture of filial duty that treasures "
          "parents and family together with the stories of the traditional "
          "gods of Korean myth — all of them carry themes and values "
          "Koreans can understand and feel with."),
        PARAGRAPH("영화 한 편은 감독과 {스태프}, 배우들의 노력을 통해 {완성}된다. 또한 그 영화가 제작된 "
          "나라의 문화, 국민들이 공유할 수 있는 {정서}와 관심 등을 담고 있다. 한국에서 천만 명 "
          "이상이 {관람}한 ‘7번방의 선물’, ‘국제시장’, ‘신과 함께–죄와 벌’ 등의 영화도 이런 "
          "{요소}들이 잘 표현되어 많은 사랑을 받았다."),
        PARAGRAPH("딸에 대한 아버지의 사랑을 {진한|진하다} {감동}과 웃음으로 {풀어낸|풀어내다} "
          "‘7번방의 선물’, 1950년대 6·25 전쟁 이후로부터 현재에 {이르기까지|이르다} 오직 "
          "가족을 위해 평생을 살아온 {평범한|평범하다} 아버지의 이야기를 {그려낸|그려내다} "
          "‘국제시장’, 부모와 가족을 {소중하게|소중하다} 생각하는 효 문화 및 한국의 {신화} 속 "
          "전통 {신}들의 이야기가 담겨있는 ‘신과 함께–죄와 벌’ 모두 한국인들이 이해하고 "
          "{공감}할 수 있는 {주제}와 가치를 담고 있다."),
        FIGURE("7번방의 선물(2013)"),
        FIGURE("국제시장(2014)"),
        FIGURE("신과 함께(2017)"),
        PARAGRAPH("★ 자신의 고향 나라에서 인기 있었던 영화를 소개해 봅시다.",
          "Introduce a film that was popular in your home country."),
    ],

    english={
        "대중문화의 의미와 대중 매체와의 관계": dict(
            title="What popular culture means, and its bond with the mass media",
            paragraphs=[
                "The culture that a great many people enjoy and take part in "
                "is called 대중문화. It takes in drama, film, song, "
                "performance, exhibition, sporting fixtures and games. The "
                "fashions one sees in daily life — in how people dress, in "
                "how they wear their hair — belong to it too. Korean popular "
                "culture is bound up especially closely with the mass media. "
                "As those media have developed — television, radio, books and "
                "newspapers, and social networks built on the smartphone — "
                "people can come at the popular culture they like easily, and "
                "share it with a great many others.",
            ],
        ),
        "한국의 대중문화": dict(
            title="Popular culture in Korea",
            paragraphs=[
                "Koreans enjoy watching drama. The number broadcast each "
                "morning, evening and night runs into dozens. The genres are "
                "various too — historical, romance, thriller. Viewers take "
                "much interest in the actors' lines and clothes as well, and "
                "those become fashionable at once.",

                "Koreans are fond of music and song too. What they most enjoy "
                "listening to is 가요, songs written so that a great many "
                "people can enjoy hearing or singing them. 가요 covers many "
                "genres — ballad, dance, R&B, hip-hop, trot — and the "
                "유행가, the song that catches on in a particular season, "
                "appears often.",

                "Film is another of Korea's important popular cultures. "
                "Audiences grew sharply around the 2000s as multiplex cinemas "
                "increased in number. As of 2018 Korea has some five hundred "
                "cinemas, and the yearly cinema audience of 216.39 million "
                "puts it fifth in the world. Films made in Korea are shown "
                "not only at home but in a good many countries abroad.",

                "In sport, professional baseball and football, basketball and "
                "volleyball are all popular. Baseball and football run from "
                "spring to autumn, basketball and volleyball from autumn to "
                "spring.",
            ],
        ),
        "한류의 시작": dict(
            title="How the Korean wave began",
            paragraphs=[
                "Asked what comes to mind at the word “Korea”, foreigners "
                "mostly answered drama, K-POP and Korean food. Around the "
                "year 2000, as Korean films and dramas were exported to "
                "countries across Asia, interest in Korean popular culture "
                "and in its performers rose. The phenomenon of Korean popular "
                "culture spreading to many countries and taking hold with the "
                "public in this way is what is called 한류 — the Korean wave.",
            ],
        ),
        "세계인들이 좋아하는 한국 대중문화": dict(
            title="The Korean popular culture the world likes",
            paragraphs=[
                "As Korean singers have gone abroad, the growth of K-POP has "
                "become striking. Among the reasons for its popularity one "
                "may count the singers' attractive looks and style, lyrics "
                "and rhythms exhilarating to sing along to, and outstanding "
                "dancing. Its popularity carries over into interest and "
                "curiosity about Korea, and the number of foreigners learning "
                "Korean and Korean culture is rising.",

                "Foreigners also show great interest in the several kinds of "
                "distinctive Korean food — 비빔밥, kimchi, 떡볶이, 삼겹살, "
                "불고기. Korean food is called 한식 for short, and programmes "
                "aimed at foreign visitors, tasting 한식 at a traditional "
                "market or trying their hand at cooking it, are popular too.",

                "The number of people fond of the make-up and the fashion of "
                "Korean stars is rising as well. That is drawing notice as a "
                "new kind of 한류 under names like K-BEAUTY and K-FASHION.",

                "Beyond those, Korean sport with 태권도 at its centre, and "
                "films original in conception and various in genre, hold a "
                "steady interest. Several Korean films in particular have "
                "lately won prizes at the major international festivals, "
                "which has brought recognition of their quality as work. And "
                "the format of Korean entertainment programmes, not only of "
                "drama, has been sold abroad and remade to suit local "
                "conditions, to great acclaim.",
            ],
        ),
    },

    extraAnnotations={
        "보급": dict(
            hanja="普及", meaning="to spread, to become widespread",
            characters=[("普", "보", "widely, universal — as in 보통 “ordinary”"),
                        ("及", "급", "to reach — as in 급 “to extend to”")],
        ),
        "떠오르다": dict(
            meaning="to come to mind; to rise up",
            notes=["Of a thought surfacing and of the sun coming up alike."],
        ),
        "한식": dict(
            hanja="韓食", meaning="Korean food",
            characters=[("韓", "한", "Korea — as in 한국, 한복, 한류"),
                        ("食", "식", "food — as in 식사 “meal”, 한식당")],
            notes=["Short for 한국 음식, and the name the state uses in "
                   "promoting it abroad."],
        ),
        "대중문화": dict(
            hanja="大衆文化", meaning="popular culture",
            characters=[("大", "대", "great — as in 대규모, 대학교"),
                        ("衆", "중", "the multitude, the crowd"),
                        ("文", "문", "writing, culture — as in 문화, 인문학"),
                        ("化", "화", "-isation — as in 도시화, 세계화")],
            notes=["대중 is “the general public”, which is also the 대중 of "
                   "대중교통 “public transport”."],
        ),
        "장면": dict(
            hanja="場面", meaning="a scene",
            characters=[("場", "장", "place — as in 시장 “market”, 예식장"),
                        ("面", "면", "face, surface — as in 면적 “area”, 측면")],
        ),
        "정주행": dict(
            hanja="正走行", meaning="binge-watching, watching in order",
            characters=[("正", "정", "correct, straight — as in 정식, 정시"),
                        ("走", "주", "to run"),
                        ("行", "행", "to go — as in 여행 “travel”, 실행")],
            notes=["Coined against 역주행, which first meant driving the wrong "
                   "way and now also means an old song climbing the charts "
                   "again. 정주행 is watching a series through from the start."],
        ),
        "개봉": dict(
            hanja="開封", meaning="the release of a film",
            characters=[("開", "개", "to open — as in 개설 “to open (a course)”"),
                        ("封", "봉", "to seal — as in 봉투 “envelope”")],
            notes=["Literally “breaking the seal”, and used of opening a "
                   "letter as well as of a film opening."],
        ),
        "굿즈": dict(
            meaning="merchandise, goods",
            notes=["From the English “goods”, but narrowed: 굿즈 means "
                   "merchandise of a band, a drama or a character, not goods "
                   "in general."],
        ),
        "프로야구팀": dict(
            hanja="프로野球팀", meaning="a professional baseball team",
            characters=[("野", "야", "field, wild — as in 야외 “outdoors”"),
                        ("球", "구", "ball — as in 축구, 농구, 배구")],
            notes=["The 구(球) that ends the name of every ball game: 야구 "
                   "baseball, 축구 football, 농구 basketball, 배구 volleyball."],
        ),
        "누리다": dict(
            meaning="to enjoy, to have the benefit of",
            notes=["Of something one is entitled to — 자유를 누리다, 혜택을 "
                   "누리다. The 누리 of 누리집 is a different word."],
        ),
        "공연": dict(
            hanja="公演", meaning="a performance",
            characters=[("公", "공", "public — as in 공적, 공공"),
                        ("演", "연", "to perform — as in 연기 “acting”, 주연")],
        ),
        "전시": dict(
            hanja="展示", meaning="an exhibition",
            characters=[("展", "전", "to unfold, display — as in 발전 “development”"),
                        ("示", "시", "to show — as in 제시 “to present”, 지시")],
        ),
        "유행": dict(
            hanja="流行", meaning="a fashion, a trend",
            characters=[("流", "류", "to flow — as in 한류, 교류"),
                        ("行", "행", "to go — as in 정주행, 행동")],
            notes=["Literally “flowing along”. 유행하다 is also used of a "
                   "disease going round."],
        ),
        "대중 매체": dict(
            hanja="大衆媒體", meaning="the mass media",
            characters=[("媒", "매", "go-between — as in 중매 “matchmaking”"),
                        ("體", "체", "body — as in 단체, 공동체")],
        ),
        "SNS": dict(
            meaning="social network service",
            notes=["The usual Korean term where English says “social media”. "
                   "Spoken as the three letters, 에스엔에스."],
        ),
        "기반": dict(
            hanja="基盤", meaning="a base, a foundation",
            characters=[("基", "기", "base — as in 기본, 기독교"),
                        ("盤", "반", "a tray, a board — as in 윷판의 판")],
        ),
        "접하다": dict(
            hanja="接하다", meaning="to come into contact with, to encounter",
            characters=[("接", "접", "to join, to receive — as in 접촉, 접종")],
        ),
        "공유": dict(
            hanja="共有", meaning="to share",
            characters=[("共", "공", "together — as in 공동, 공존"),
                        ("有", "유", "to have — as in 고유, 유일하다")],
        ),
        "수십": dict(
            hanja="數十", meaning="dozens, some tens of",
            characters=[("數", "수", "number — as in 횟수, 다수")],
            notes=["The same pattern as 수백 “hundreds” and 수천 "
                   "“thousands”."],
        ),
        "사극": dict(
            hanja="史劇", meaning="a historical drama",
            characters=[("史", "사", "history — as in 역사 “history”"),
                        ("劇", "극", "drama, play — as in 연극 “theatre”")],
        ),
        "장르": dict(meaning="a genre"),
        "시청자": dict(
            hanja="視聽者", meaning="a viewer",
            characters=[("視", "시", "to see — as in 시력 “eyesight”, 중시"),
                        ("聽", "청", "to listen — as in 청취 “listening”"),
                        ("者", "자", "person — as in 가입자, 근로자")],
            notes=["시청 is watching-and-listening, hence 시청료, the licence "
                   "fee. A different 시청(市廳) is the city hall."],
        ),
        "대사": dict(
            hanja="臺詞", meaning="a line of dialogue",
            characters=[("臺", "대", "platform, stage — as in 무대 “stage”, 토대"),
                        ("詞", "사", "word, phrase — as in 가사 “lyrics”")],
        ),
        "가요": dict(
            hanja="歌謠", meaning="popular song",
            characters=[("歌", "가", "song — as in 가수 “singer”, 국가"),
                        ("謠", "요", "ballad, folk song")],
            notes=["The general word for Korean popular song, older than "
                   "K-POP and wider: ballad, dance, trot all count."],
        ),
        "발라드": dict(meaning="ballad"),
        "트로트": dict(
            meaning="trot",
            notes=["A Korean genre with a two-beat swing, from the foxtrot. "
                   "Long thought old-fashioned, and lately popular again."],
        ),
        "유행가": dict(
            hanja="流行歌", meaning="a hit song of the moment",
            notes=["유행 “fashion” + 가 “song”."],
        ),
        "멀티플렉스": dict(
            meaning="a multiplex cinema",
            notes=["CGV, 롯데시네마 and 메가박스 are the three chains, and "
                   "between them nearly the whole market."],
        ),
        "영화관": dict(
            hanja="映畫館", meaning="a cinema",
            characters=[("映", "영", "to project — as in 반영 “reflection”"),
                        ("畫", "화", "picture — as in 만화 “comic”, 그림"),
                        ("館", "관", "hall — as in 도서관, 박물관")],
        ),
        "관객": dict(
            hanja="觀客", meaning="an audience, a spectator",
            characters=[("觀", "관", "to watch — as in 관광 “sightseeing”, 관찰"),
                        ("客", "객", "guest — as in 문상객, 관광객")],
        ),
        "급격하다": dict(
            hanja="急激하다", meaning="to be sudden, sharp",
            characters=[("急", "급", "urgent — as in 긴급, 응급"),
                        ("激", "격", "violent, intense — as in 격려 “encourage”")],
        ),
        "연간": dict(
            hanja="年間", meaning="annual, over a year",
            characters=[("年", "년", "year — as in 연령, 연휴"),
                        ("間", "간", "between, during — as in 기간, 층간 소음")],
        ),
        "해당": dict(
            hanja="該當", meaning="to correspond to, to come to",
            characters=[("該", "해", "that, the said"),
                        ("當", "당", "to be fitting — as in 담당, 당국")],
        ),
        "제작": dict(
            hanja="製作", meaning="production, to make",
            characters=[("製", "제", "to manufacture — as in 제품 “product”"),
                        ("作", "작", "to make — as in 작품 “work”, 창작")],
        ),
        "상영": dict(
            hanja="上映", meaning="to screen, to show (a film)",
            characters=[("上", "상", "up, on — as in 상급, 향상"),
                        ("映", "영", "to project — as in 영화, 반영")],
        ),
        "프로": dict(
            meaning="professional",
            notes=["Short for the English “professional”. Its counterpart is "
                   "아마추어. Not the 프로 of 프로그램, which is a different "
                   "clipping."],
        ),
        "독특하다": dict(
            hanja="獨特하다", meaning="to be distinctive, singular",
            characters=[("獨", "독", "alone — as in 독립, 단독"),
                        ("特", "특", "special — as in 특징, 특유")],
        ),
        "방": dict(
            hanja="房", meaning="room — and a place of business named for one",
            notes=["노래방, PC방, 찜질방, 만화방: a small room hired by the hour "
                   "for one purpose. The suffix has become a Korean "
                   "institution, and the article's subject."],
        ),
        "노래방": dict(
            meaning="a karaoke room",
            notes=["Hired by the hour by a group, as against the Japanese "
                   "karaoke bar with its open room."],
        ),
        "PC방": dict(
            meaning="an internet café",
            notes=["Spread from the late 1990s with the internet, and the "
                   "home of Korean competitive gaming."],
        ),
        "찜질방": dict(
            meaning="a jjimjilbang, a heated bathhouse",
            notes=["A public bathhouse with hot rooms floored in the manner "
                   "of an 온돌, open all night, and cheap enough to sleep in."],
        ),
        "만화방": dict(hanja="漫畫房", meaning="a comic-book café"),
        "발견": dict(
            hanja="發見", meaning="to find, to discover",
            characters=[("發", "발", "to issue, to start — as in 발달, 발급"),
                        ("見", "견", "to see — as in 견학 “field study”, 의견")],
        ),
        "후반": dict(
            hanja="後半", meaning="the latter half",
            characters=[("後", "후", "after, behind — as in 이후, 오후"),
                        ("半", "반", "half — as in 반달, 반죽")],
            notes=["Its counterpart is 전반. 1990년대 후반 is the late 1990s."],
        ),
        "e스포츠": dict(
            meaning="esports",
            notes=["Korea took competitive gaming seriously first, out of the "
                   "PC방 of the late 1990s, and still supplies much of the "
                   "professional scene."],
        ),
        "온돌": dict(
            hanja="溫突", meaning="ondol, underfloor heating",
            characters=[("溫", "온", "warm — as in 온도 “temperature”"),
                        ("突", "돌", "to protrude, a flue")],
            notes=["Chapter 14's 온돌 — the heated stone floor. A 찜질방 is its "
                   "commercial descendant."],
        ),
        "동료": dict(
            hanja="同僚", meaning="a colleague",
            characters=[("同", "동", "same — as in 동일, 동문회"),
                        ("僚", "료", "an official, a colleague")],
        ),
        "실내": dict(
            hanja="室內", meaning="indoors",
            characters=[("室", "실", "room — as in 교실 “classroom”, 사무실"),
                        ("內", "내", "inside — as in 국내, 내국인")],
        ),
        "활용": dict(
            hanja="活用", meaning="to make use of",
            characters=[("活", "활", "living, active — as in 생활, 활동"),
                        ("用", "용", "to use — as in 이용, 유용하다")],
        ),
        "골프연습장": dict(
            hanja="골프練習場", meaning="a golf driving range",
            characters=[("練", "련", "to train — as in 훈련 “training”"),
                        ("習", "습", "to practise — as in 학습, 습관")],
            notes=["Often a screen range in a city building rather than an "
                   "open field — the 실내 the article mentions."],
        ),
        "코스": dict(meaning="a course, an itinerary"),
        "한류": dict(
            hanja="韓流", meaning="hallyu, the Korean wave",
            characters=[("韓", "한", "Korea — as in 한국, 한식, 한복"),
                        ("流", "류", "to flow, a current — as in 유행, 교류")],
            notes=["Coined in Chinese-language media in the late 1990s and "
                   "borrowed back into Korean. The 流 is a current flowing "
                   "outward."],
        ),
        "전후": dict(
            hanja="前後", meaning="around, either side of",
            characters=[("前", "전", "before — as in 이전, 전날"),
                        ("後", "후", "after — as in 이후, 후반")],
            notes=["2000년 전후 “around the year 2000”. A different 전후(戰後) "
                   "means post-war."],
        ),
        "수출": dict(
            hanja="輸出", meaning="export",
            characters=[("輸", "수", "to transport — as in 운수 “transport”"),
                        ("出", "출", "to go out — as in 출발, 진출")],
            notes=["Its counterpart is 수입(輸入), import — not the 수입(收入) "
                   "of chapter 4, which is income."],
        ),
        "연예인": dict(
            hanja="演藝人", meaning="an entertainer, a celebrity",
            characters=[("演", "연", "to perform — as in 공연, 주연"),
                        ("藝", "예", "art — as in 예술 “art”, 예능")],
        ),
        "확산": dict(
            hanja="擴散", meaning="to spread, to diffuse",
            characters=[("擴", "확", "to expand — as in 확충, 확대"),
                        ("散", "산", "to scatter — as in 분산 “dispersal”")],
        ),
        "대중적": dict(hanja="大衆的", meaning="popular, of the general public"),
        "현상": dict(
            hanja="現象", meaning="a phenomenon",
            characters=[("現", "현", "present, to appear — as in 현재, 현지"),
                        ("象", "상", "shape, image — as in 상징, 인상")],
        ),
        "가수": dict(
            hanja="歌手", meaning="a singer",
            characters=[("歌", "가", "song — as in 가요, 유행가"),
                        ("手", "수", "hand, a hand at — as in 선수 “player”")],
        ),
        "진출": dict(
            hanja="進出", meaning="to advance into, to break into",
            characters=[("進", "진", "to advance — as in 진학, 진행"),
                        ("出", "출", "to go out — as in 수출, 출신")],
        ),
        "띄다": dict(
            meaning="to be conspicuous, to catch the eye",
            notes=["눈에 띄다 “to stand out”. Not to be confused with 띠다 “to "
                   "bear, to take on”, which the same article uses in "
                   "다양성을 띨 것으로."],
        ),
        "요인": dict(
            hanja="要因", meaning="a factor, a cause",
            characters=[("要", "요", "essential — as in 중요, 요강"),
                        ("因", "인", "cause — as in 원인 “cause”, 인연")],
        ),
        "매력적": dict(
            hanja="魅力的", meaning="attractive, charming",
            characters=[("魅", "매", "to charm, to bewitch"),
                        ("力", "력", "power — as in 능력 “ability”, 영향력")],
        ),
        "외모": dict(
            hanja="外貌", meaning="looks, outward appearance",
            characters=[("外", "외", "outside — as in 외국, 국내외"),
                        ("貌", "모", "appearance, countenance")],
        ),
        "가사": dict(
            hanja="歌詞", meaning="lyrics",
            characters=[("詞", "사", "word, phrase — as in 대사 “dialogue”")],
            notes=["A different 가사(家事) means housework."],
        ),
        "리듬": dict(meaning="rhythm"),
        "뛰어나다": dict(meaning="to be outstanding, to excel"),
        "실력": dict(
            hanja="實力", meaning="ability, real skill",
            characters=[("實", "실", "real — as in 사실, 실질적"),
                        ("力", "력", "power — as in 매력적, 능력")],
        ),
        "흥미": dict(
            hanja="興味", meaning="interest",
            characters=[("興", "흥", "to rise, to prosper — as in 흥분 “excitement”"),
                        ("味", "미", "taste — as in 의미 “meaning”, 미각")],
        ),
        "호기심": dict(
            hanja="好奇心", meaning="curiosity",
            characters=[("好", "호", "to like — as in 선호하다, 호평"),
                        ("奇", "기", "strange, rare — as in 신기하다 “curious”"),
                        ("心", "심", "heart, mind — as in 관심, 자부심")],
        ),
        "떡볶이": dict(
            meaning="tteokbokki, rice cakes in chilli sauce",
            notes=["떡 + 볶이 from 볶다 “to stir-fry”. The commonest street "
                   "food, and one of the dishes foreigners meet first."],
        ),
        "특색": dict(
            hanja="特色", meaning="a distinctive character",
            characters=[("特", "특", "special — as in 특유, 독특하다"),
                        ("色", "색", "colour — as in 색깔 “colour”")],
        ),
        "관광객": dict(
            hanja="觀光客", meaning="a tourist",
            characters=[("觀", "관", "to watch — as in 관객, 관찰"),
                        ("光", "광", "light — as in 영광 “glory”, 관광")],
        ),
        "맛보다": dict(meaning="to taste, to sample"),
        "체험": dict(
            hanja="體驗", meaning="first-hand experience",
            characters=[("體", "체", "body — as in 단체, 정체성"),
                        ("驗", "험", "to test — as in 시험 “examination”")],
            notes=["체험 is doing a thing oneself; 경험 is having been through "
                   "it. Chapter 6's 농촌 체험 마을 is the same word."],
        ),
        "스타": dict(meaning="a star, a celebrity"),
        "화장법": dict(
            hanja="化粧法", meaning="a way of making up, cosmetic technique",
            characters=[("粧", "장", "to adorn"),
                        ("法", "법", "law, method — as in 방법 “method”, 헌법")],
            notes=["This 화장(化粧) is cosmetics; the 화장(火葬) of chapter 15 is "
                   "cremation."],
        ),
        "유형": dict(
            hanja="類型", meaning="a type, a kind",
            characters=[("類", "류", "kind — as in 종류, 장류"),
                        ("型", "형", "form, mould — as in 모형 “model”, 대형")],
        ),
        "주목": dict(
            hanja="注目", meaning="attention, notice",
            characters=[("注", "주", "to pour, to focus — as in 주의 “caution”"),
                        ("目", "목", "eye — as in 목표 “goal”, 과목")],
        ),
        "태권도": dict(
            hanja="太拳道", meaning="taekwondo",
            characters=[("拳", "권", "fist — as in 권투 “boxing”"),
                        ("道", "도", "way — as in 유도 “judo”, 황도")],
            notes=["An Olympic sport since 2000, and the sport most often "
                   "taken as standing for Korea abroad."],
        ),
        "독창적": dict(
            hanja="獨創的", meaning="original, inventive",
            characters=[("獨", "독", "alone — as in 독특하다, 독학"),
                        ("創", "창", "to create — as in 창업, 창시")],
        ),
        "꾸준하다": dict(meaning="to be steady, persistent"),
        "영화제": dict(
            hanja="映畫祭", meaning="a film festival",
            characters=[("祭", "제", "festival, rite — as in 축제, 제사")],
        ),
        "수상": dict(
            hanja="受賞", meaning="to win a prize",
            characters=[("受", "수", "to receive — as in 수강, 접수"),
                        ("賞", "상", "prize — as in 작품상, 상금")],
            notes=["A different 수상(水上) means “on the water”."],
        ),
        "작품성": dict(
            hanja="作品性", meaning="artistic quality",
            characters=[("作", "작", "to make — as in 제작, 창작"),
                        ("品", "품", "article, quality — as in 품종, 공산품")],
        ),
        "예능 프로그램": dict(
            hanja="藝能프로그램", meaning="an entertainment programme",
            characters=[("藝", "예", "art — as in 예술, 연예인"),
                        ("能", "능", "ability — as in 능력, 기능")],
            notes=["The variety show. Formats such as 복면가왕 have been sold "
                   "abroad and remade — The Masked Singer."],
        ),
        "현지": dict(
            hanja="現地", meaning="the local place, on the ground",
            characters=[("現", "현", "present — as in 현재, 현상"),
                        ("地", "지", "place — as in 지역, 지위")],
        ),
        "리메이크": dict(meaning="a remake"),
        "호평": dict(
            hanja="好評", meaning="a favourable reception",
            characters=[("好", "호", "good, to like — as in 호기심, 선호하다"),
                        ("評", "평", "to judge — as in 평가 “evaluation”")],
            notes=["Its counterpart is 악평."],
        ),
        "봉준호": dict(
            meaning="Bong Joon-ho, film director",
            notes=["Director of 기생충, 살인의 추억, 괴물 and 설국열차."],
        ),
        "감독": dict(
            hanja="監督", meaning="a director; a manager",
            characters=[("監", "감", "to oversee — as in 감시 “surveillance”"),
                        ("督", "독", "to supervise — as in 기독교's 督")],
            notes=["Of a film, and also of a sports team."],
        ),
        "송강호": dict(
            meaning="Song Kang-ho, actor",
            notes=["The father in 기생충, and a lead in much of Bong's work."],
        ),
        "주연": dict(
            hanja="主演", meaning="the leading role",
            characters=[("主", "주", "main — as in 주식, 주거"),
                        ("演", "연", "to perform — as in 공연, 연예인")],
        ),
        "기생충": dict(
            hanja="寄生蟲", meaning="Parasite (2019)",
            characters=[("寄", "기", "to depend on, to send — as in 기여"),
                        ("生", "생", "life — as in 생활, 학생"),
                        ("蟲", "충", "insect, worm")],
            notes=["The word means a parasite in the biological sense. The "
                   "first film not in English to take the Academy's Best "
                   "Picture."],
        ),
        "칸 영화제": dict(meaning="the Cannes Film Festival"),
        "황금종려상": dict(
            hanja="黃金棕櫺賞", meaning="the Palme d'Or",
            characters=[("黃", "황", "yellow — as in 황도"),
                        ("金", "금", "gold — as in 금 “gold”, 축의금")],
            notes=["Literally “the golden palm-frond prize”."],
        ),
        "아카데미 영화제": dict(meaning="the Academy Awards"),
        "작품상": dict(hanja="作品賞", meaning="the prize for best picture"),
        "감독상": dict(hanja="監督賞", meaning="the prize for best director"),
        "각본상": dict(
            hanja="脚本賞", meaning="the prize for best screenplay",
            characters=[("脚", "각", "leg"), ("本", "본", "root, book — as in 기본, 본관")],
            notes=["각본 is the screenplay."],
        ),
        "국제영화상": dict(hanja="國際映畫賞", meaning="the prize for best international feature"),
        "대중성": dict(hanja="大衆性", meaning="popular appeal"),
        "예술성": dict(
            hanja="藝術性", meaning="artistic merit",
            characters=[("術", "술", "skill, art — as in 기술 “technique”, 의술")],
        ),
        "골든글로브": dict(meaning="the Golden Globes"),
        "시상식": dict(
            hanja="施賞式", meaning="an awards ceremony",
            characters=[("施", "시", "to bestow — as in 시행 “to enforce”"),
                        ("式", "식", "ceremony — as in 결혼식, 입학식")],
        ),
        "외국어영화상": dict(hanja="外國語映畫賞", meaning="the prize for best foreign-language film"),
        "자막": dict(
            hanja="字幕", meaning="subtitles",
            characters=[("字", "자", "character, letter — as in 문자, 한자"),
                        ("幕", "막", "curtain, screen — as in 개막 “opening”")],
            notes=["Literally “the character curtain”."],
        ),
        "장벽": dict(
            hanja="障壁", meaning="a barrier",
            characters=[("障", "장", "to obstruct — as in 보장 “to guarantee”'s 障"),
                        ("壁", "벽", "wall — as in 벽 “wall”")],
        ),
        "연결": dict(
            hanja="連結", meaning="connection",
            characters=[("連", "련", "to link — as in 연휴, 연립"),
                        ("結", "결", "to tie — as in 결혼, 결속")],
        ),
        "수상 소감": dict(
            hanja="受賞所感", meaning="an acceptance speech",
            characters=[("所", "소", "that which — as in 소망, 산소"),
                        ("感", "감", "to feel — as in 감동, 안정감")],
        ),
        "감동": dict(
            hanja="感動", meaning="a stirring of feeling, being moved",
            characters=[("感", "감", "to feel — as in 감사, 호기심의 心"),
                        ("動", "동", "to move — as in 운동, 능동적")],
        ),
        "스태프": dict(meaning="crew, staff (on a production)"),
        "완성": dict(
            hanja="完成", meaning="completion",
            characters=[("完", "완", "complete — as in 보완 “to supplement”"),
                        ("成", "성", "to accomplish — as in 성장, 구성")],
        ),
        "정서": dict(
            hanja="情緖", meaning="sentiment, the feeling of a people",
            characters=[("情", "정", "feeling — as in 감정, 정보")],
        ),
        "관람": dict(
            hanja="觀覽", meaning="to view, to attend (a film, a match)",
            characters=[("觀", "관", "to watch — as in 관객, 관광"),
                        ("覽", "람", "to look over — as in 열람 “perusal”")],
        ),
        "요소": dict(
            hanja="要素", meaning="an element, a factor",
            characters=[("要", "요", "essential — as in 요인, 중요"),
                        ("素", "소", "element — as in 영양소, 소재")],
        ),
        "진하다": dict(meaning="to be deep, strong (of colour, feeling, flavour)"),
        "풀어내다": dict(
            meaning="to unfold, to tell (a story)",
            notes=["풀다 “to loosen, to solve” + 내다. Of a story told out at "
                   "length."],
        ),
        "이르다": dict(
            meaning="to reach, to come to",
            notes=["Also a separate 이르다 “to be early”, and a third meaning "
                   "“to tell on someone”."],
        ),
        "평범하다": dict(
            hanja="平凡하다", meaning="to be ordinary",
            characters=[("平", "평", "flat, even — as in 평등, 평생"),
                        ("凡", "범", "common, all")],
        ),
        "그려내다": dict(meaning="to depict, to portray"),
        "소중하다": dict(
            hanja="所重하다", meaning="to be precious",
            characters=[("所", "소", "that which — as in 소감, 소망"),
                        ("重", "중", "heavy, important — as in 중요, 존중")],
        ),
        "신화": dict(
            hanja="神話", meaning="a myth, mythology",
            characters=[("神", "신", "god — as in 신성, 천지신명"),
                        ("話", "화", "talk, story — as in 대화 “conversation”")],
        ),
        "신": dict(
            hanja="神", meaning="a god",
            notes=["The same 神 as in 신성 “sacred” and 무신론자 “atheist”."],
        ),
        "공감": dict(
            hanja="共感", meaning="empathy, feeling with",
            characters=[("共", "공", "together — as in 공유, 공존"),
                        ("感", "감", "to feel — as in 감동, 감사")],
        ),
        "주제": dict(
            hanja="主題", meaning="a theme, a subject",
            characters=[("主", "주", "main — as in 주연, 주식"),
                        ("題", "제", "topic, title — as in 제목 “title”, 문제")],
        ),
        "특정하다": dict(
            hanja="特定하다", meaning="to be particular, specified",
            characters=[("特", "특", "special — as in 특색, 특유"),
                        ("定", "정", "to fix — as in 지정, 정착")],
        ),
    },

    extraNotes=[
        "The warm-up on p. 96 is a four-panel comic. The speech bubbles are "
        "too small to read reliably off the photograph, so the panels are "
        "described in one caption and only the four words you wrote beside "
        "them — 정주행, 개봉, 굿즈, 프로야구팀 — are set as labels.",
        "The page reads 뛰어난 춤 실력을 뽑을 수 있다 as far as I can make out, "
        "which would be a slip for 꼽을; the book writes 꼽을 수 있다 elsewhere, "
        "so it is set that way here. Worth checking.",
        "The 기생충 box says 4개 부분, where 부문 is the word for a category of "
        "award. It is set as printed, since it is the book's own slip.",
    ],
)
