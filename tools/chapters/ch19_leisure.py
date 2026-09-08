# -*- coding: utf-8 -*-
"""Chapter 19 — Leisure.

No Google Doc: yours stop at chapter 12. Transcribed from the photos of
pp. 100-103, so the Korean here is my reading of the page rather than yours,
and any error in it is mine.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, LABELS, FIGURE, TABLE,
               CELL, GLOSSARY, CHART)

CHAPTER = dict(
    number=19, slug="19-leisure",
    unit="문화", title="여가문화", titleEn="Leisure",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 한국인이 {여가} 시간에 즐기는 {주요} 활동입니다."),
        LABELS("{텔레비전 시청}", "{영화 관람}", "{등산}", "{배드민턴}"),
        HEADING(4, "01 한국에서 직장 일이나 {가정} 일, 공부 등에서 {벗어난|벗어나다} 자유로운 시간에 "
             "무엇을 합니까?"),
        HEADING(4, "02 자신의 고향 나라에서는 여가 활동으로 주로 무엇을 합니까?"),

        SECTION("goals", "학습목표"),
        BULLET("한국의 여가문화 종류와 특징을 설명할 수 있다.", ordered=True),
        BULLET("여가활동에 능동적으로 참여할 수 있다.", ordered=True),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", 2), "제목", "관련 내용"],
              [[CELL("기본", down=2), "사회", "12. 평생 교육", "평생 교육기관과 지원제도"],
               ["문화", "18. 대중문화", "한국의 대중문화"]]),

        SECTION("part", "01 한국에는 어떤 여가문화가 있을까?"),
        HEADING(2, "여가가 있는 삶"),
        GLOSSARY(("1인당 국민소득", "평균적으로 국민 한 사람이 일정 기간(1년)에 벌어들이는 소득",
               "1인당 국민소득"),
              ("국민여가활성화기본법", "자유로운 여가활동을 할 수 있는 기반을 만들고 여가활동을 "
                                    "통하여 삶의 질을 향상시킬 수 있도록 지원하는 법",
               "국민여가활성화기본법")),
        PARAGRAPH("일과 생활이 {균형}을 {갖춘|갖추다} 삶을 살아가기 위해서는 자신이 좋아하고 흥미를 "
          "느낄 수 있는 활동에 참여하는 시간이 필요하다. 이를 ‘{여가}’라고 하며, 이와 관련하여 "
          "{형성}된 문화를 ‘{여가문화}’라고 한다. 한국은 2000년대 초·중반 무렵 "
          "{주 5일 근무제} {시행}을 시작으로 현재 {1인당 국민소득} 3만 달러 시대, "
          "{주 52시간 근무제} {도입}, 평균 {기대 수명} 증가와 같은 변화를 맞이하면서 여가의 "
          "{중요성}이 더욱 높아지고 있다. 한국 정부에서도 여가가 있는 삶을 {보장} 받을 수 "
          "있도록 ‘{국민여가활성화기본법}’을 {제정}하기도 하였다."),

        HEADING(2, "한국의 여가"),
        GLOSSARY(("동호회", "취미나 공통의 관심사, 목표를 가지고 정보를 나누면서 함께 즐기는 "
                        "사람들의 모임", "동호회")),
        PARAGRAPH("{문화체육관광부}의 ‘2018 국민여가활동 조사’에 따르면 한국인의 {평일}과 {휴일} 여가 "
          "시간이 예전에 비해 증가하였고, {월평균} 여가 {비용} 역시 {상승}한 것으로 나타났다. "
          "이는 과거보다 여가를 더 중요하게 여기고 있음을 보여준다."),
        PARAGRAPH("한국인이 가장 많이 참여한 여가활동은 {휴식}활동으로 TV 시청, {낮잠}, {산책}, 찜질방 "
          "등이 여기에 해당한다. 또한, 쇼핑, {외식}, 인터넷 {검색}, {1인 미디어}, SNS 등과 같은 "
          "{취미}·{오락}활동 {비중}도 높다. 한편, 친구를 만나 이야기를 나누기도 하고, {친지} 및 "
          "친척을 방문하여 {오붓한|오붓하다} 시간을 보내기도 한다. 또한, 운동이나 {악기}, "
          "{독서}, 외국어 등 여러 분야에서 자신이 좋아하거나 배우고 싶은 것을 다른 사람들과 함께 "
          "공유할 수 있는 {동호회}가 {활성화} 되어 있다. 스포츠·{문화예술} {관람}도 한국에서 "
          "인기 있는 여가활동이다. 스포츠 {경기장}을 직접 방문하여 응원하기도 하며, "
          "{박물관}·{미술관}에서 {전시회} 관람, {공연장}에서 콘서트, {뮤지컬}, {연극}을 즐기기도 "
          "한다. {코로나19} 이후에는 전시나 공연 온라인 서비스를 통해 관람하는 새로운 {형태}의 "
          "여가문화도 나타났다."),
        FIGURE("여가시간 및 여가비용 추이(문화체육관광부, 국민여가활동조사 2018) — 평일과 휴일의 "
            "여가 시간, 그리고 월평균 여가 비용이 2006년부터 2018년까지 어떻게 움직였는지를 "
            "겹쳐 그린 그래프"),
        FIGURE("‘슈퍼주니어’의 온라인 콘서트 모습"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "여행을 떠나요! 대한민국 구석구석에 대한 여행 정보"),
        PARAGRAPH("{한국관광공사}가 운영하는 ‘{대한민국 구석구석}’ 누리집(korean.visitkorea.or.kr)에서는 "
          "각 {지역별} 여행 정보와 전국의 {축제} 정보를 {월별}로 확인할 수 있다. 이 "
          "누리집에서는 가족과 함께 가는 여행, 휴식과 {회복}이 필요한 여행, 아이들이 좋아하는 "
          "여행 등 주제에 따른 {관광} 코스도 자세히 안내하고 있다. ‘대한민국 구석구석’ 블로그, "
          "페이스북, 트위터, 인스타그램 등에서도 다양한 정보와 여행 사진을 {참고}할 수 있다."),

        SECTION("part", "02 여가활동에는 어떻게 참여할 수 있을까?"),
        HEADING(2, "여가활동 참여하기"),
        GLOSSARY(("행정복지센터", "지역 주민의 생활 업무를 처리하고, 문화 및 복지 서비스를 지원하는 "
                            "행정기관", "행정복지센터"),
              ("평생학습관", "지역주민을 대상으로 인문교양, 문화예술, 직업능력 향상, 시민참여 "
                          "등의 평생학습 프로그램을 운영", "평생학습관")),
        PARAGRAPH("여가활동에 참여하는 방법은 점점 쉽고 다양해지고 있다. 영화, 스포츠, 공연과 같은 "
          "문화예술 관람을 원하면 직접 방문하여 {입장권}을 살 수도 있고 스마트폰 "
          "{어플}(앱)이나 누리집을 통해 {예매}할 수도 있다."),
        PARAGRAPH("또한 각 지역의 {행정복지센터}나 {평생학습관}의 여가 프로그램에도 적은 비용으로 참여할 "
          "수 있다. 각 {기관}은 지역 주민이 무엇을 배우기를 원하는지 조사하여 "
          "음악/미술/외국어/건강/컴퓨터/요리 등 다양한 프로그램을 제공하고 있다. {백화점}이나 "
          "{대형 마트}의 {문화센터}에서도 다양한 프로그램을 만들어 놓고 있는데 여기에 참여하는 "
          "사람도 많다."),
        PARAGRAPH("학교, 지역, 회사, 인터넷 {커뮤니티} 등에는 다양한 동호회가 있다. 사진, 축구, 미술, "
          "독서 등 자신이 흥미를 가진 분야를 찾아 {가입}하여 다른 사람들과 공통의 {관심사}나 "
          "정보를 나누면서 함께 즐길 수 있다."),
        FIGURE("수원 평생학습관 누리집"),

        HEADING(2, "변화하는 여가문화"),
        GLOSSARY(("웹툰(WEBTOON)", "웹(WEB)과 카툰(CARTOON)의 합성어로서 인터넷 만화를 지칭함",
               "웹툰")),
        PARAGRAPH("일과 삶의 균형({워라벨}: Work and Life Balance), 휴식이 있는 삶에 대한 {요구}가 "
          "높아지면서 여가문화는 더욱 강조될 것으로 예상된다. 예를 들어, 건강에 대한 관심이 "
          "{지속적}으로 높아짐으로써 {헬스}, 수영, {요가} 등에 대한 {수요}가 계속 늘어날 것이다. "
          "금요일 오후부터 주말을 이용한 국내외 여행이 {일상화}되고, {자연휴양림} 등에서 "
          "{캠핑}을 즐기는 사람도 증가할 것이다."),
        PARAGRAPH("또한 {스마트기기}를 활용하여 {웹서핑}, {모바일메신저}, SNS활동, 게임, 쇼핑, 음악 "
          "{감상}, 인터넷 방송 시청, {웹툰} 읽기 등은 물론 직접 온라인 {콘텐츠}를 "
          "{만들어내는|만들어내다} 방식의 여가활동을 즐기는 사람도 더욱 늘어날 것이다."),
        CHART("스마트기기를 활용한 여가활동(문화체육관광부, 국민여가활동조사 2018)(단위: %) — "
              "스마트 기기 활용자 기준, 복수 응답", "%",
              [("웹서핑", 31.3), ("모바일 메신저", 17.9), ("SNS활동", 14.6),
               ("게임", 14.1), ("TV시청", 4.4), ("쇼핑", 3.9), ("음악감상", 3.8),
               ("인터넷방송 시청", 2.7), ("웹툰 읽기", 2.7), ("웹소설 읽기", 2.0)]),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "문화가 있는 날을 아세요?"),
        PARAGRAPH("‘{문화가 있는 날}’은 2014년 1월 29일 처음 시작되었다. 매달 마지막 수요일에 "
          "일상에서 문화를 쉽게 접할 수 있도록 다양한 문화 혜택을 제공하고 있다. ‘문화가 있는 "
          "날’에는 영화관, 공연장, 박물관, 미술관, {문화재} 등 전국의 2천여 개 {문화시설}을 "
          "{할인} 또는 무료로 즐길 수 있다. {더불어} 직장인도 {퇴근} 후 이용이 가능하도록 일부 "
          "문화시설은 {야간 개방}을 한다. 예를 들어 2020년 기준으로 영화관에서는 매달 마지막 "
          "수요일 저녁 5시~9시까지의 영화는 5,000원으로 관람할 수 있다. "
          "(누리집: www.culture.go.kr)"),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 한국에는 어떤 여가문화가 있을까?"),
        BULLET("한국은 1인당 국민소득 3만 달러 시대, 주 (        ) 근무제 도입 등과 같은 변화를 "
          "맞이하면서 여가의 중요성이 더욱 높아지고 있다."),
        BULLET("운동이나 악기, 독서, 외국어 등 자신이 좋아하거나 배우고 싶은 것을 다른 사람들과 "
          "정보를 나누면서 함께 즐기는 (        )가 활성화되어 있다."),
        HEADING(3, "02 여가활동에는 어떻게 참여할 수 있을까?"),
        BULLET("지역 주민의 생활 업무를 처리하고, 문화 및 복지 서비스를 지원하는 행정기관인 "
          "(        )를 통해 여가 프로그램에 참여할 수 있다."),
        BULLET("(        )과 (        )의 균형, 휴식이 있는 삶에 대한 기대가 높아지면서 여가문화는 "
          "더욱 중시될 것이다."),
        BULLET("(        ) 관리에 대한 관심이 지속적으로 늘어남으로써 헬스, 수영, 요가에 대한 수요도 "
          "증가할 것이다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "한국인의 여가활동의 목적은?", translation=
          "What do Koreans do leisure activities for?" "\n\n"
          "According to the 2018 National Leisure Activity Survey report, "
          "the main purpose of Koreans’ leisure activities turned out to be "
          "‘personal enjoyment’. The proportions answering ‘peace of mind "
          "and rest’, ‘relieving stress’, ‘self-satisfaction’ and ‘spending "
          "time with the family’ were also generally high." "\n\n"
          "Among those aged 15–19 and in their twenties, more than 39% do "
          "leisure activities ‘for personal enjoyment’, while among those in "
          "their fifties and above, doing leisure activities ‘for health’ "
          "was found to be more common than in other age groups."),
        PARAGRAPH("2018 국민여가활동조사 {보고서}에 따르면 한국 국민의 여가활동의 {주된|주되다} 목적은 "
          "‘개인의 즐거움’으로 나타났다. 그리고 ‘마음의 {안정}과 휴식’, ‘스트레스 {해소}’, "
          "‘{자기만족}’, ‘가족과 시간을 함께하기’ 등에 응답한 {비율}도 {대체로} 높게 나타났다."),
        PARAGRAPH("15–19세, 20대에서는 39% 이상이 ‘개인의 즐거움을 위해’ 여가활동을 하고 있으며, "
          "50대 이상에서는 ‘건강을 위해’ 여가활동을 하는 경우가 다른 {연령대}보다 많은 것으로 "
          "나타났다."),
        TABLE(["여가활동 목적", "2015", "2018"],
              [["개인의 즐거움", "37.1", "32.5"],
               ["마음의 안정과 휴식", "16.9", "18.2"],
               ["스트레스 해소", "14.0", "14.7"],
               ["건강을 위해", "10.3", "10.1"],
               ["자기만족", "8.0", "8.8"],
               ["대인관계", "5.2", "5.1"],
               ["가족과 시간을 함께하기", "3.2", "4.7"],
               ["시간을 보내기", "3.0", "3.8"],
               ["자기 개발", "2.3", "2.0"]]),
        PARAGRAPH("★ 자신이 한국에서 즐겨하는 여가활동과 그 목적을 서로 이야기해 봅시다.",
          "Talk with each other about the leisure activities you enjoy in "
          "Korea and what you do them for."),
    ],

    english={
        "여가가 있는 삶": dict(
            title="A life with leisure in it",
            paragraphs=[
                "Living a life in which work and living are in balance takes "
                "time spent on the activities one likes and can take an "
                "interest in. That is what is meant by 여가, and the culture "
                "formed around it is 여가문화. Korea began the five-day "
                "working week around the early to middle 2000s, and as it has "
                "met further changes since — an era of thirty thousand "
                "dollars of national income a head, the introduction of the "
                "52-hour week, a rising average life expectancy — the "
                "importance of leisure has risen further still. The "
                "government has gone so far as to enact a Framework Act on "
                "the Promotion of National Leisure, so that a life with "
                "leisure in it may be guaranteed.",
            ],
        ),
        "한국의 여가": dict(
            title="Leisure in Korea",
            paragraphs=[
                "By the Ministry of Culture, Sports and Tourism's 2018 survey "
                "of national leisure activity, Koreans' leisure time on both "
                "working days and holidays has increased against what it was, "
                "and monthly spending on leisure has risen as well. That "
                "shows leisure being held more important than it was.",

                "The leisure activity Koreans took part in most was rest — "
                "watching television, napping, walking, the 찜질방 and the "
                "like. Hobbies and amusements weigh heavily too: shopping, "
                "eating out, searching the internet, one-person media, social "
                "networks. Some meet friends and talk; some visit relatives "
                "and kin and spend a snug hour with them. There are also "
                "flourishing clubs, in which what one likes or wants to learn "
                "— sport, an instrument, reading, a foreign language — can be "
                "shared with others. Going to sport and to the arts is "
                "popular here as well. People go to the ground itself to "
                "cheer, see exhibitions at museums and galleries, and enjoy "
                "concerts, musicals and plays at the theatre. Since Covid-19 "
                "a new form of leisure has appeared too, watching exhibitions "
                "and performances through online services.",
            ],
        ),
        "여가활동 참여하기": dict(
            title="Taking part in leisure",
            paragraphs=[
                "Ways of taking part in leisure are becoming easier and more "
                "various. Someone wanting to see a film, a sporting fixture "
                "or a performance can go and buy a ticket in person, or book "
                "through a smartphone app or a website.",

                "The leisure programmes at a district's community service "
                "centre or lifelong learning centre can also be joined for "
                "little money. Each of them surveys what local residents want "
                "to learn and offers a range accordingly — music, art, "
                "languages, health, computing, cooking. The culture centres at "
                "department stores and the large supermarkets put on a range "
                "of programmes too, and a good many people go to those.",

                "Schools, districts, companies and internet communities all "
                "have clubs of various kinds. One can find a field one is "
                "interested in — photography, football, art, reading — join "
                "it, and enjoy it with others while sharing a common interest "
                "and what one knows.",
            ],
        ),
        "변화하는 여가문화": dict(
            title="How leisure is changing",
            paragraphs=[
                "As the demand grows for a balance between work and life — "
                "워라벨, Work and Life Balance — and for a life with rest in "
                "it, leisure culture is expected to be stressed further. "
                "Interest in health, for one thing, keeps rising, so demand "
                "for the gym, for swimming and for yoga will go on "
                "increasing. Travel at home and abroad from Friday afternoon "
                "through the weekend will become an ordinary thing, and more "
                "people will camp in the recreational forests and the like.",

                "More people, too, will take their leisure through smart "
                "devices — surfing the web, mobile messaging, social "
                "networks, games, shopping, listening to music, watching "
                "internet broadcasts, reading 웹툰 — and, beyond all that, in "
                "making online content themselves.",
            ],
        ),
    },

    extraAnnotations={
        "여가": dict(
            hanja="餘暇", meaning="leisure, free time",
            characters=[("餘", "여", "surplus, remaining — as in 여유 “leeway”"),
                        ("暇", "가", "leisure, idle time")],
            notes=["Literally “time left over”. The chapter's subject, and "
                   "the 여가 of 여가활동 and 여가문화."],
        ),
        "여가문화": dict(hanja="餘暇文化", meaning="leisure culture"),
        "주요": dict(
            hanja="主要", meaning="main, principal",
            characters=[("主", "주", "main — as in 주식, 주연"),
                        ("要", "요", "essential — as in 요인, 중요")],
        ),
        "텔레비전 시청": dict(
            hanja="텔레비전視聽", meaning="watching television",
            characters=[("視", "시", "to see — as in 시청자, 중시"),
                        ("聽", "청", "to listen — as in 청취")],
        ),
        "영화 관람": dict(
            hanja="映畫觀覽", meaning="going to the cinema",
            characters=[("觀", "관", "to watch — as in 관객, 관광"),
                        ("覽", "람", "to look over — as in 열람")],
        ),
        "등산": dict(
            hanja="登山", meaning="hill walking, hiking",
            characters=[("登", "등", "to climb — as in 등교 “going to school”"),
                        ("山", "산", "mountain — as in 산소, 배산임수")],
            notes=["The commonest outdoor pastime in Korea, which is a "
                   "mountainous country: 등산 is walking up a hill, not "
                   "technical climbing."],
        ),
        "배드민턴": dict(meaning="badminton"),
        "가정": dict(
            hanja="家庭", meaning="the home, the household",
            characters=[("家", "가", "house, family — as in 가족, 국가"),
                        ("庭", "정", "courtyard, garden")],
        ),
        "벗어나다": dict(
            meaning="to get out of, to break free from",
            notes=["Of escaping a place, a state or an obligation: 일에서 "
                   "벗어나다, 가난에서 벗어나다."],
        ),
        "균형": dict(
            hanja="均衡", meaning="balance, equilibrium",
            characters=[("均", "균", "even — as in 평균 “average”"),
                        ("衡", "형", "a balance, a scale")],
        ),
        "갖추다": dict(
            meaning="to be equipped with, to have in place",
            notes=["Of having what is needed: 조건을 갖추다, 예를 갖추다 — the "
                   "last of these appeared in chapter 15's funeral."],
        ),
        "형성": dict(
            hanja="形成", meaning="formation, to take shape",
            characters=[("形", "형", "form — as in 형태 “form”, 유형"),
                        ("成", "성", "to accomplish — as in 구성, 완성")],
        ),
        "주 5일 근무제": dict(
            hanja="週五日勤務制", meaning="the five-day working week",
            characters=[("週", "주", "week — as in 주말 “weekend”, 매주"),
                        ("勤", "근", "diligent, to serve — as in 근로자, 출근"),
                        ("務", "무", "duty — as in 업무 “work”, 의무"),
                        ("制", "제", "system — as in 제도, 학점 은행제")],
            notes=["Phased in from 2004. Before it, Saturday morning was a "
                   "working half-day."],
        ),
        "주 52시간 근무제": dict(
            hanja="週五十二時間勤務制", meaning="the 52-hour week",
            notes=["A cap of forty regular hours plus twelve of overtime, "
                   "phased in from 2018. Chapter 3 mentions it too."],
        ),
        "시행": dict(
            hanja="施行", meaning="to put into effect, to enforce",
            characters=[("施", "시", "to bestow, to carry out — as in 시상식"),
                        ("行", "행", "to go, to do — as in 행동, 유행")],
        ),
        "1인당 국민소득": dict(
            hanja="一人當國民所得", meaning="national income per head",
            characters=[("當", "당", "per, to correspond — as in 해당, 담당"),
                        ("所", "소", "that which — as in 소망, 소감"),
                        ("得", "득", "to obtain — as in 취득 “acquisition”")],
            notes=["Korea passed thirty thousand US dollars in 2018."],
        ),
        "도입": dict(
            hanja="導入", meaning="introduction, bringing in",
            characters=[("導", "도", "to guide — as in 지도자, 유도"),
                        ("入", "입", "to enter — as in 입구, 수입")],
        ),
        "기대 수명": dict(
            hanja="期待壽命", meaning="life expectancy",
            notes=["Chapter 12's word: the span one is expected to have at "
                   "birth."],
        ),
        "중요성": dict(hanja="重要性", meaning="importance"),
        "보장": dict(
            hanja="保障", meaning="to guarantee",
            characters=[("保", "보", "to protect — as in 보험, 보호"),
                        ("障", "장", "a barrier — as in 장벽 “barrier”")],
        ),
        "국민여가활성화기본법": dict(
            hanja="國民餘暇活性化基本法", meaning="the Framework Act on the Promotion of National Leisure",
            notes=["Enacted in 2015. 기본법 is a framework act — one that sets "
                   "the principles other statutes work within."],
        ),
        "제정": dict(
            hanja="制定", meaning="to enact (a law)",
            characters=[("制", "제", "system, to regulate — as in 제도, 규제"),
                        ("定", "정", "to fix — as in 지정, 정착")],
        ),
        "문화체육관광부": dict(
            hanja="文化體育觀光部", meaning="the Ministry of Culture, Sports and Tourism",
            characters=[("體", "체", "body — as in 체육 “physical education”"),
                        ("育", "육", "to raise — as in 교육, 보육"),
                        ("觀", "관", "to watch — as in 관광, 관객"),
                        ("光", "광", "light — as in 관광, 영광")],
        ),
        "평일": dict(
            hanja="平日", meaning="a weekday, a working day",
            characters=[("平", "평", "flat, ordinary — as in 평범하다, 평등")],
        ),
        "휴일": dict(
            hanja="休日", meaning="a holiday, a day off",
            characters=[("休", "휴", "to rest — as in 휴식, 연휴")],
        ),
        "월평균": dict(
            hanja="月平均", meaning="the monthly average",
            characters=[("均", "균", "even — the same 均 as in 균형")],
        ),
        "비용": dict(
            hanja="費用", meaning="cost, expense",
            characters=[("費", "비", "to spend — as in 학비, 생활비"),
                        ("用", "용", "to use — as in 이용, 활용")],
        ),
        "상승": dict(
            hanja="上昇", meaning="a rise, to go up",
            characters=[("上", "상", "up — as in 향상, 상영"),
                        ("昇", "승", "to ascend")],
            notes=["Its counterpart is 하락."],
        ),
        "휴식": dict(
            hanja="休息", meaning="rest",
            characters=[("休", "휴", "to rest — as in 휴일, 연휴"),
                        ("息", "식", "breath, to rest — as in 자식 “one's child”")],
        ),
        "낮잠": dict(
            meaning="a nap",
            notes=["낮 “daytime” + 잠 “sleep”. Its counterpart is 밤잠."],
        ),
        "산책": dict(
            hanja="散策", meaning="a walk, a stroll",
            characters=[("散", "산", "to scatter, to disperse — as in 확산, 분산"),
                        ("策", "책", "a plan, a staff — as in 정책 “policy”")],
        ),
        "외식": dict(
            hanja="外食", meaning="eating out",
            characters=[("外", "외", "outside — as in 외국, 국내외"),
                        ("食", "식", "food, to eat — as in 식사, 한식")],
        ),
        "검색": dict(
            hanja="檢索", meaning="a search",
            characters=[("檢", "검", "to examine — as in 검사 “inspection”, 검진"),
                        ("索", "색", "to search for")],
        ),
        "1인 미디어": dict(
            meaning="one-person media",
            notes=["A channel made and run by one person — a streamer, a "
                   "YouTuber. Chapter 4's 1인 방송 is the same idea."],
        ),
        "취미": dict(
            hanja="趣味", meaning="a hobby",
            characters=[("趣", "취", "interest, taste"),
                        ("味", "미", "taste — as in 흥미, 의미")],
        ),
        "오락": dict(
            hanja="娛樂", meaning="amusement, entertainment",
            characters=[("娛", "오", "to amuse"),
                        ("樂", "락", "pleasure, music — as in 음악 “music”")],
            notes=["The 오락 of 예능 프로그램's 오락적인 내용 in chapter 18."],
        ),
        "비중": dict(
            hanja="比重", meaning="weight, relative share",
            characters=[("比", "비", "to compare — as in 비율, 비교"),
                        ("重", "중", "heavy — as in 중요, 존중")],
        ),
        "친지": dict(
            hanja="親知", meaning="close acquaintances",
            characters=[("親", "친", "close, kin — as in 친척, 친구"),
                        ("知", "지", "to know — as in 지식 “knowledge”, 지혜")],
            notes=["Those one knows well, not necessarily blood relatives — "
                   "the article pairs it with 친척."],
        ),
        "오붓하다": dict(
            meaning="to be snug, cosy and companionable",
            notes=["Of a small gathering that feels close and unhurried. A "
                   "pure-Korean word, and a hard one to render — “a snug "
                   "hour” comes near."],
        ),
        "악기": dict(
            hanja="樂器", meaning="a musical instrument",
            characters=[("樂", "악", "music — the same 樂 as in 오락, read 락 there"),
                        ("器", "기", "vessel, implement — as in 그릇의 용기, 기구")],
            notes=["The same character 樂 reads 악 in 음악 and 악기, but 락 in "
                   "오락 and 낙원 — “music” against “pleasure”."],
        ),
        "독서": dict(
            hanja="讀書", meaning="reading",
            characters=[("讀", "독", "to read — as in 독학 “self-study”"),
                        ("書", "서", "book, writing — as in 도서관, 서류")],
        ),
        "동호회": dict(
            hanja="同好會", meaning="a club, a society of enthusiasts",
            characters=[("同", "동", "same — as in 동일, 동문회"),
                        ("好", "호", "to like — as in 호기심, 선호하다"),
                        ("會", "회", "society — as in 향우회, 교회")],
            notes=["Literally “the society of those who like the same "
                   "thing”."],
        ),
        "활성화": dict(
            hanja="活性化", meaning="to become active, to flourish",
            characters=[("活", "활", "living — as in 생활, 활동"),
                        ("性", "성", "nature — as in 다양성, 중요성"),
                        ("化", "화", "-isation — as in 도시화, 일상화")],
        ),
        "문화예술": dict(hanja="文化藝術", meaning="culture and the arts"),
        "관람": dict(
            hanja="觀覽", meaning="to view, to attend",
            characters=[("觀", "관", "to watch — as in 관객, 관광"),
                        ("覽", "람", "to look over")],
        ),
        "경기장": dict(
            hanja="競技場", meaning="a stadium, a ground",
            characters=[("競", "경", "to compete — as in 경쟁 “competition”"),
                        ("技", "기", "skill — as in 기술 “technique”"),
                        ("場", "장", "place — as in 장례식장, 예식장")],
        ),
        "박물관": dict(
            hanja="博物館", meaning="a museum",
            characters=[("博", "박", "wide, broad — as in 박사 “doctorate”"),
                        ("物", "물", "thing — as in 물건 “object”, 매물"),
                        ("館", "관", "hall — as in 도서관, 영화관")],
        ),
        "미술관": dict(
            hanja="美術館", meaning="an art gallery",
            characters=[("美", "미", "beautiful — as in 미국 “America”, 미용"),
                        ("術", "술", "art, skill — as in 예술성, 기술")],
        ),
        "전시회": dict(
            hanja="展示會", meaning="an exhibition",
            characters=[("展", "전", "to display — as in 발전 “development”"),
                        ("示", "시", "to show — as in 제시, 지시")],
        ),
        "공연장": dict(hanja="公演場", meaning="a performance venue, a theatre"),
        "뮤지컬": dict(meaning="a musical"),
        "연극": dict(
            hanja="演劇", meaning="a play, theatre",
            characters=[("演", "연", "to perform — as in 공연, 주연"),
                        ("劇", "극", "drama — as in 사극 “historical drama”")],
        ),
        "코로나19": dict(
            meaning="Covid-19",
            notes=["Korean uses the number rather than the year: 코로나19, "
                   "read 코로나 일구."],
        ),
        "형태": dict(
            hanja="形態", meaning="a form, a shape",
            characters=[("形", "형", "form — as in 형성, 유형"),
                        ("態", "태", "condition — as in 태도, 상태")],
        ),
        "한국관광공사": dict(
            hanja="韓國觀光公社", meaning="the Korea Tourism Organization",
            characters=[("社", "사", "company, society — as in 회사, 사회")],
        ),
        "대한민국 구석구석": dict(
            meaning="“Every Corner of Korea”, the state tourism site",
            notes=["구석 is a corner or nook; doubling it gives “every last "
                   "corner”. The English name of the site is Visit Korea."],
        ),
        "지역별": dict(
            hanja="地域別", meaning="by region",
            characters=[("別", "별", "to separate, by — as in 성별, 유형별")],
            notes=["The suffix -별 “by, per” makes 월별 “by month”, 연령별 “by "
                   "age”, 지역별 “by region”."],
        ),
        "축제": dict(
            hanja="祝祭", meaning="a festival",
            characters=[("祝", "축", "to celebrate — as in 축하, 축의금"),
                        ("祭", "제", "rite, festival — as in 제사, 영화제")],
        ),
        "월별": dict(hanja="月別", meaning="by month, monthly"),
        "회복": dict(
            hanja="回復", meaning="recovery",
            characters=[("回", "회", "to turn round — as in 횟수, 회갑"),
                        ("復", "복", "to return, again — as in 복습 “revision”")],
        ),
        "관광": dict(
            hanja="觀光", meaning="tourism, sightseeing",
            characters=[("觀", "관", "to watch — as in 관람, 관객"),
                        ("光", "광", "light — as in 영광 “glory”")],
            notes=["Literally “to look at the light” — an old phrase for "
                   "seeing the sights of a place."],
        ),
        "참고": dict(
            hanja="參考", meaning="reference; to consult",
            characters=[("參", "참", "to take part — as in 참여, 참가"),
                        ("考", "고", "to think, to examine — as in 고려")],
        ),
        "입장권": dict(
            hanja="入場券", meaning="an admission ticket",
            characters=[("場", "장", "place — as in 경기장, 공연장"),
                        ("券", "권", "ticket, certificate — as in 상품권")],
        ),
        "어플": dict(
            meaning="an app",
            notes=["Clipped from 애플리케이션. 앱 is the newer and now commoner "
                   "form; the page gives both."],
        ),
        "예매": dict(
            hanja="豫買", meaning="advance booking",
            characters=[("豫", "예", "beforehand — as in 예방, 예상"),
                        ("買", "매", "to buy — as in 구매 “purchase”, 매매")],
        ),
        "행정복지센터": dict(
            hanja="行政福祉센터", meaning="a community service centre",
            notes=["The office once called 동사무소 and then 주민센터. It "
                   "handles residence registration and runs local "
                   "programmes."],
        ),
        "평생학습관": dict(
            hanja="平生學習館", meaning="a lifelong learning centre",
            notes=["Chapter 12's 평생 학습관 — the local centre where the "
                   "courses are held."],
        ),
        "기관": dict(
            hanja="機關", meaning="an institution, an organ",
            characters=[("機", "기", "machine, workings — as in 기능, 계기"),
                        ("關", "관", "to relate, a barrier — as in 관계, 관련")],
        ),
        "백화점": dict(
            hanja="百貨店", meaning="a department store",
            characters=[("百", "백", "hundred — as in 백일, 백지장"),
                        ("貨", "화", "goods — as in 화물 “freight”"),
                        ("店", "점", "shop — as in 상점 “shop”, 서점")],
            notes=["Literally “the hundred-goods shop”."],
        ),
        "대형 마트": dict(
            hanja="大型마트", meaning="a hypermarket",
            characters=[("型", "형", "form, size — as in 유형, 형태")],
        ),
        "문화센터": dict(
            meaning="a culture centre",
            notes=["The classes a department store or supermarket runs for "
                   "its customers — cookery, flower arranging, languages."],
        ),
        "커뮤니티": dict(meaning="a community, an online forum"),
        "가입": dict(
            hanja="加入", meaning="to join, to enrol",
            characters=[("加", "가", "to add — as in 추가 “addition”"),
                        ("入", "입", "to enter — as in 도입, 입구")],
        ),
        "관심사": dict(
            hanja="關心事", meaning="a matter of interest",
            characters=[("事", "사", "affair, matter — as in 사례, 무사하다")],
        ),
        "워라벨": dict(
            meaning="work-life balance",
            notes=["From the initials of Work and Life Balance. The standard "
                   "spelling is 워라밸; the page prints 워라벨."],
        ),
        "요구": dict(
            hanja="要求", meaning="a demand, a requirement",
            characters=[("要", "요", "essential — as in 주요, 요인"),
                        ("求", "구", "to seek — as in 요구, 구하다")],
        ),
        "지속적": dict(
            hanja="持續的", meaning="continuous, sustained",
            characters=[("持", "지", "to hold — as in 유지 “to maintain”"),
                        ("續", "속", "to continue — as in 계속 “continuation”")],
        ),
        "헬스": dict(
            meaning="the gym, working out",
            notes=["From “health”, but meaning weight training. A gym is a "
                   "헬스장 or 헬스클럽."],
        ),
        "요가": dict(meaning="yoga"),
        "수요": dict(
            hanja="需要", meaning="demand",
            characters=[("需", "수", "to need, to require"),
                        ("要", "요", "essential — as in 요구, 주요")],
            notes=["Its counterpart is 공급, supply. Not the 수요 of 수요일, "
                   "Wednesday."],
        ),
        "일상화": dict(
            hanja="日常化", meaning="to become an everyday thing",
            characters=[("常", "상", "usual, constant — as in 일상 “daily life”")],
        ),
        "자연휴양림": dict(
            hanja="自然休養林", meaning="a recreational forest",
            characters=[("養", "양", "to nurture — as in 양육, 함양"),
                        ("林", "림", "forest — as in 산림 “forest”")],
            notes=["A state-run forest with cabins and camping, managed by "
                   "the Korea Forest Service."],
        ),
        "캠핑": dict(meaning="camping"),
        "스마트기기": dict(
            hanja="스마트機器", meaning="a smart device",
            characters=[("機", "기", "machine — as in 기관, 기능"),
                        ("器", "기", "implement — as in 악기, 용기")],
            notes=["Two different 기 characters side by side: 機 the mechanism "
                   "and 器 the implement."],
        ),
        "웹서핑": dict(meaning="web surfing"),
        "모바일메신저": dict(
            meaning="a mobile messenger",
            notes=["In Korea this means KakaoTalk, which nearly everyone "
                   "uses."],
        ),
        "감상": dict(
            hanja="鑑賞", meaning="appreciation, listening to or looking at",
            characters=[("鑑", "감", "to examine, a mirror"),
                        ("賞", "상", "to appreciate; a prize — as in 수상, 작품상")],
            notes=["음악 감상 “listening to music”, 영화 감상 “watching films” — "
                   "with attention, not idly. A different 감상(感想) means "
                   "one's impressions."],
        ),
        "웹툰": dict(
            meaning="webtoon",
            notes=["WEB + CARTOON. Korean webtoons scroll vertically on a "
                   "phone rather than paging, and the form has been exported "
                   "along with the word."],
        ),
        "콘텐츠": dict(meaning="content"),
        "만들어내다": dict(meaning="to produce, to turn out"),
        "문화가 있는 날": dict(
            meaning="Culture Day",
            notes=["The last Wednesday of every month, since January 2014. "
                   "Discounted or free admission at some two thousand "
                   "venues."],
        ),
        "문화재": dict(
            hanja="文化財", meaning="a cultural property, a heritage site",
            characters=[("財", "재", "wealth, property — as in 재산 “property”")],
        ),
        "문화시설": dict(
            hanja="文化施設", meaning="a cultural facility",
            characters=[("施", "시", "to institute — as in 시행, 시상식"),
                        ("設", "설", "to establish — as in 설립, 시설")],
        ),
        "할인": dict(
            hanja="割引", meaning="a discount",
            characters=[("割", "할", "to cut, to divide"),
                        ("引", "인", "to pull — as in 인상 “a rise (in price)”")],
        ),
        "더불어": dict(
            meaning="together with, along with",
            notes=["From 더불다. 더불어 살다 “to live alongside others” — "
                   "chapter 13's 생활협동조합 uses it."],
        ),
        "퇴근": dict(
            hanja="退勤", meaning="leaving work",
            characters=[("退", "퇴", "to withdraw — as in 은퇴 “retirement”, 퇴사"),
                        ("勤", "근", "to serve — as in 근무제, 근로자")],
            notes=["Its counterpart is 출근, going in to work."],
        ),
        "야간 개방": dict(
            hanja="夜間開放", meaning="opening in the evening",
            characters=[("夜", "야", "night — as in 야간보육, 야근"),
                        ("開", "개", "to open — as in 개봉, 개설"),
                        ("放", "방", "to release — as in 방송 “broadcast”, 개방")],
        ),
        "보고서": dict(
            hanja="報告書", meaning="a report",
            characters=[("報", "보", "to report — as in 정보 “information”"),
                        ("告", "고", "to tell — as in 신고 “to report”, 광고")],
        ),
        "주되다": dict(hanja="主되다", meaning="to be the main, principal"),
        "안정": dict(
            hanja="安定", meaning="stability, calm",
            characters=[("安", "안", "peace — as in 안전, 안부"),
                        ("定", "정", "to settle — as in 정착, 지정")],
        ),
        "해소": dict(
            hanja="解消", meaning="to relieve, to clear away",
            characters=[("解", "해", "to loosen, to resolve — as in 이해, 해결"),
                        ("消", "소", "to extinguish — as in 소화기 “extinguisher”")],
            notes=["스트레스 해소 “relieving stress” — the set phrase."],
        ),
        "자기만족": dict(
            hanja="自己滿足", meaning="self-satisfaction, contentment",
            characters=[("滿", "만", "full — as in 만점 “full marks”"),
                        ("足", "족", "foot; enough — as in 부족 “lack”, 만족")],
        ),
        "비율": dict(
            hanja="比率", meaning="a proportion, a rate",
            characters=[("比", "비", "to compare — as in 비중, 비교"),
                        ("率", "률", "rate — as in 진학률, 출산율")],
        ),
        "대체로": dict(
            hanja="大體로", meaning="on the whole, generally",
            characters=[("體", "체", "body, substance — as in 전반적, 단체")],
        ),
        "연령대": dict(
            hanja="年齡帶", meaning="an age group",
            characters=[("齡", "령", "age — as in 고령화, 연령"),
                        ("帶", "대", "a band, a belt — as in 지대 “zone”")],
        ),
    },

    extraNotes=[
        "Chapter 19 has no Google Doc: the Korean is transcribed from the "
        "photos of pp. 100-103 rather than from a transcription of yours, so "
        "mistakes in it are mine and it is worth reading against the pages.",
        "The 여가시간 및 여가비용 추이 figure on p. 101 is not drawn. It layers "
        "three series over eight years — leisure hours on working days and on "
        "holidays, and monthly cost — and its numbers cannot be read reliably "
        "off the photograph, so it is described rather than reproduced with "
        "invented values.",
        "The 여가활동 목적 figure on p. 103 gives two years side by side, which "
        "one bar chart cannot show, so it is set as a table of 2015 against "
        "2018.",
        "The page prints 워라벨 where the standard spelling is 워라밸. It is "
        "set as printed.",
    ],
)
