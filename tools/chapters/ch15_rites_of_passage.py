# -*- coding: utf-8 -*-
"""Chapter 15 — Rites of passage.

No Google Doc: yours stop at chapter 12. Transcribed from the photos of
pp. 84-87, so the Korean here is my reading of the page rather than yours,
and any error in it is mine.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, LABELS, MARGIN, FIGURE,
               TABLE, CELL, GLOSSARY)

CHAPTER = dict(
    number=15, slug="15-rites-of-passage",
    unit="문화", title="의례", titleEn="Rites of passage",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        MARGIN("{통과의례}"),
        PARAGRAPH("다음은 한국의 대표적인 {의례}와 관련된 사진입니다."),
        LABELS("{결혼식}", "{돌잔치}", "{장례식}", "{제사}"),
        HEADING(4, "01 한국에서 생활하면서 사진에 나온 의례 중에 직접 경험해 보았거나 TV, 영화 등을 "
             "통해 본 것이 있습니까?"),
        HEADING(4, "02 자신의 고향 나라와 한국의 의례 사이의 공통점과 차이점은 무엇입니까?"),

        SECTION("goals", "학습목표"),
        BULLET("한국의 결혼식, 돌잔치, 성년식 문화를 설명할 수 있다.", ordered=True),
        BULLET("한국의 장례식, 제사 문화를 설명할 수 있다.", ordered=True),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", 2), "제목", "관련 내용"],
              [[CELL("기본", down=2), CELL("문화", down=2), "13. 전통 가치", "한국의 효와 예절"],
               ["16. 명절", "설날과 추석"]]),

        SECTION("part", "01 결혼식, 돌잔치, 성년식은 어떤 모습일까?"),
        HEADING(2, "가정의 탄생, 결혼식"),
        GLOSSARY(("서약", "맹세하고 약속함", "서약"),
              ("신랑", "갓 결혼하였거나 곧 결혼하는 남자", "신랑"),
              ("신부", "갓 결혼하였거나 곧 결혼하는 여자", "신부"),
              ("축의금", "축하하는 마음을 나타내기 위해 내는 돈", "축의금")),
        PARAGRAPH("남자와 여자가 부부가 되기로 {서약}하는 {의례}를 {결혼식}이라고 한다. 한국에서는 "
          "남녀 모두 만 18세가 되면 결혼할 수 있지만, 만 19세가 안된 {미성년자}의 경우는 "
          "부모의 {동의}가 있어야 결혼할 수 있다. 결혼식을 한다고 해서 {정식}으로 부부가 되는 "
          "것은 아니다. 시·군·구청에 {혼인 신고}를 해야 {법적}인 부부로 인정받는다."),
        PARAGRAPH("일반적으로 {신랑}과 {신부}는 가족, 친척, 친구, 직장 동료 등 많은 사람들의 축하 "
          "속에서 결혼식을 한다. 결혼식은 주로 {예식장}, 교회, {성당}, 호텔 등에서 한다. "
          "결혼식에 초대 받은 사람들은 {축의금}을 준비해 가서 축하의 마음을 전한다."),

        HEADING(2, "첫 번째 생일, 돌잔치"),
        PARAGRAPH("{돌}은 아이가 태어난 지 1년이 되는 첫 생일을 말한다. {돌잔치}에는 아이가 "
          "{무사히|무사하다} 첫 생일을 {맞이한|맞이하다} 것을 {기념}하고, 앞으로 잘 자라기를 "
          "바라는 {소망}이 담겨있다. 이 날은 가족이나 가까운 사람들이 모여 같이 음식을 먹으며 "
          "아이의 첫 생일을 축하한다. 또한 여러 물건을 {상} 위에 올려 놓고, 아이가 "
          "{골라잡은|골라잡다} 물건으로 아이의 미래를 {예상}해 보는 {돌잡이}를 보며 함께 "
          "즐거워한다."),

        HEADING(2, "성인으로 성장, 성년식"),
        GLOSSARY(("성인", "어른이 된 사람. 일반적으로 만 19세 이상을 가리킴", "성인"),
              ("자부심", "자기 자신의 가치나 능력을 믿고 당당히 여기는 마음", "자부심")),
        PARAGRAPH("한국에서는 만 19세가 된 {젊은이}에게 {성인}이 되었음을 축하하고 {자부심}을 높이기 "
          "위해 매년 5월 셋째 월요일을 ‘{성년의 날}’로 기념하고 있다. 대체로 고등학교를 졸업한 "
          "이후에 만 19세를 맞이하게 된다. 결혼이나 {선거} 등은 만 18세부터 할 수 있지만 "
          "{흡연}이나 {음주} 등은 법적으로 만 19세부터 가능하다. ‘성년의 날’ 선물로는 "
          "{장미꽃}과 {향수}가 대표적이다."),
        FIGURE("2019 성년의 날 기념식(여성가족부) (사진 출처: 〈연합뉴스〉)"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "백일을 축하합니다!"),
        PARAGRAPH("옛날에는 의료 기술이 발달하지 못했기 때문에 아이가 태어난 지 얼마 안 돼 죽는 경우가 "
          "적지 않았다. 그래서 한국에서는 아이가 태어난 지 {백일}(100일)이 되는 날에 그동안 "
          "건강히 잘 자란 것을 기념하는 {백일잔치}를 열었다. 백일잔치에는 가족과 가까운 친척이 "
          "모여 아이의 백일을 축하해 주며, 이웃이나 친한 사람들에게 백일을 기념하는 떡을 "
          "{돌리기도|돌리다} 한다. 또한 아이의 성장과 아름다운 {추억}을 남기기 위해 백일 "
          "사진을 찍는다."),

        SECTION("part", "02 장례식과 제사는 어떤 모습일까?"),
        HEADING(2, "죽은 사람을 떠나 보냄, 장례식"),
        GLOSSARY(("고인", "죽은 사람", "고인"),
              ("문상객", "죽은 사람의 가족을 위로하기 위해 장례식장을 방문하는 손님", "문상객"),
              ("조의금", "위로하는 마음을 나타내기 위해 내는 돈", "조의금"),
              ("유족", "죽은 사람의 남아있는 가족", "유족"),
              ("묵념", "머리를 숙여 경건한 마음으로 기도함", "묵념"),
              ("매장", "시신을 땅에 묻음", "매장"),
              ("화장", "시신을 불에 태워서 그 남은 뼈를 모아 장례를 지냄", "화장")),
        PARAGRAPH("사람이 죽었을 때, 예를 갖추어 {고인}을 보내는 의례를 {장례}라고 한다. 일반적으로 "
          "한국에서는 병원 내 또는 단독 {장례식장}에서 3일 동안 장례 {절차}를 진행하며, 첫째 "
          "날과 둘째 날에는 {문상객}을 받는다."),
        PARAGRAPH("문상객은 {엄숙한|엄숙하다} 마음으로 검정색 계열의 {단정한|단정하다} 옷을 입고 "
          "{조의금}을 준비한다. 장례식장에 들어가면 고인에게 절을 두 번, {유족}에게는 한 번의 "
          "절을 한다. 종교에 따라 조금씩 차이가 있는데, {개신교}의 경우 절 대신에 {묵념}을 "
          "하기도 한다. 문상객은 유족에게 {위로}의 마음을 담아 {간결한|간결하다} 인사말을 "
          "전한다. 셋째 날은 고인을 보내 드리는 날이다. 고인을 {묘지}에 {매장}하기도 하고, "
          "{화장}을 거친 후 {봉안당}이나 {추모공원}에 모시기도 한다."),
        FIGURE("봉안당 모습"),

        HEADING(2, "조상을 정성껏 섬김, 제사"),
        MARGIN("{음복}"),
        PARAGRAPH("돌아가신 {조상}을 생각하며 음식을 {바치고|바치다} {정성}을 다하는 의례를 "
          "{제사}라고 한다. 조상이 돌아가신 날({기일})에는 {기제사}, 명절에는 {차례}를 지낸다. "
          "한국에서는 조상을 잘 모셔야 {자손}들이 잘 된다고 믿어온 풍습이 있다."),
        PARAGRAPH("제사를 지낼 때에는 가족이 함께 모여 {추모}하는 마음으로 제사 음식 앞에서 조상에게 "
          "절을 두 번 한다."),
        PARAGRAPH("제사를 마친 후에는 가족들이 함께 모여 제사 음식을 나누어 먹는다. 이를 {음복}이라고 "
          "한다. 음복은 조상이 주는 {복}을 나누어 받는다는 의미가 담겨 있다."),
        PARAGRAPH("최근에는 종교나 가정의 {여건}에 따라 제사를 지내는 방식도 다양해지고 있다. "
          "{전반적}으로 제사를 드리는 {횟수}나 시간, 제사 음식의 종류가 {간소화}되고 있다."),
        FIGURE("전통적인 제사상 모습"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "장례 문화가 바뀌고 있다"),
        PARAGRAPH("1970~80년대까지는 한국에서 장례를 할 때 대부분 매장을 {선호했지만|선호하다}, 시대가 "
          "변화하면서 화장을 원하는 인구가 늘고 있다. 화장을 {희망}하는 이유로는 매장에 비해 "
          "{위생적}인 관리와 {간편한|간편하다} 절차, 저렴한 비용 등을 들 수 있다. 화장을 한 뒤 "
          "남은 {유골}은 봉안당이나 추모공원에 모셔두고 조상이 돌아가신 날이나 명절 무렵에 "
          "방문한다. 최근에는 환경과 {생태}를 강조하는 {자연장}도 {주목}을 받고 있다. 자연장은 "
          "화장한 유골을 나무, {화초}, {잔디} 주변에 묻는 방식이다. 이를 통해 생활 공간 "
          "가까이에 고인을 모시면서 자연환경 {보존}에도 {기여}할 수 있다."),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 결혼식, 돌잔치, 성년식은 어떤 모습일까?"),
        BULLET("한국에서는 남녀 모두 만 (        )세가 되면 결혼을 할 수 있다."),
        BULLET("아이의 첫 생일에 여러 물건을 상 위에 올려놓고, 아이가 골라잡은 물건으로 아이의 "
          "미래를 예상해 보는 것을 (        )라고 한다."),
        BULLET("만 19세가 된 젊은이들에게 성인이 되었음을 축하하기 위해 매년 5월 셋째 월요일을 "
          "(        )로 지정하고 있다."),
        HEADING(3, "02 장례식과 제사는 어떤 모습일까?"),
        BULLET("장례는 일반적으로 (        )일 동안 절차를 진행한다."),
        BULLET("장례식을 거친 후 종교나 신념에 따라 고인을 묘지에 매장하기도 하고, (        )을 "
          "거친 후 봉안당이나 추모공원에 모시기도 한다."),
        BULLET("제사를 마친 후에 가족들이 함께 모여 제사 음식을 나누어 먹는 것을 (        )이라고 "
          "한다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "부모님, 오래 오래 사세요!", translation=
          "Mother, Father, may you live long!" "\n\n"
          "In Korea the sixtieth birthday one meets after being born is "
          "called 환갑, or 회갑. In the old days, when average life "
          "expectancy was short, sixty and over meant a long life, and that "
          "was regarded as a great blessing. So when a parent reached 환갑, "
          "the children would invite relatives and friends and hold a feast, "
          "wishing their parent long life. Now that life expectancy has "
          "grown longer, a 환갑 feast is rarely held, and it is more common "
          "to hold a 칠순 feast (고희연) celebrating the seventieth year."),
        PARAGRAPH("한국에서는 태어나서 60번째 맞이하는 생일을 {환갑} 또는 {회갑}이라 한다. 평균 "
          "{수명}이 짧았던 옛날에는 60살 이상은 {장수}를 의미했고, 이는 큰 {복}으로 여겨졌다. "
          "그래서 부모가 환갑을 맞이하면 자녀들은 친척과 친구들을 초대하여 잔치를 열어 부모가 "
          "오래 사시기를 {기원하였다|기원하다}. 평균 수명이 길어진 요즘에는 환갑 잔치를 여는 "
          "경우는 {드물고|드물다} 70살을 축하하는 {칠순} 잔치({고희연})를 하는 경우가 많다."),
        FIGURE("칠순 잔치(고희연) 모습"),
        TABLE(["나이", "일컫는 말"],
              [["15세", "지학"], ["20세", "약관/방년"], ["30세", "입지"],
               ["40세", "불혹"], ["50세", "지천명"], ["60세", "육순/이순"],
               ["61세", "환갑/회갑"], ["70세", "칠순/고희"], ["80세", "팔순"],
               ["90세", "구순"], ["100세", "상수"], ["120세", "천수"]]),
        PARAGRAPH("★ 자신의 고향 나라에서 부모의 장수를 기원하는 의식이 있다면 소개해 봅시다.",
          "If your home country has a rite that wishes a parent long life, "
          "introduce it."),
    ],

    english={
        "가정의 탄생, 결혼식": dict(
            title="A household begins: the wedding",
            paragraphs=[
                "The rite in which a man and a woman vow to become husband "
                "and wife is the wedding. In Korea both may marry once they "
                "are eighteen, but a minor who has not turned nineteen needs "
                "a parent's consent. Holding a wedding does not of itself "
                "make a couple married. The marriage has to be registered at "
                "the city, county or district office to be recognised in law.",

                "Bride and groom generally marry amid the congratulations of "
                "a great many people — family, relatives, friends, colleagues "
                "from work. Weddings are held mostly at wedding halls, at "
                "churches, at Catholic churches, at hotels. Those invited "
                "bring a gift of money and with it their good wishes.",
            ],
        ),
        "첫 번째 생일, 돌잔치": dict(
            title="The first birthday: the 돌잔치",
            paragraphs=[
                "돌 means the first birthday, a year after the child was "
                "born. The 돌잔치 marks the child having reached it safely, "
                "and carries the wish that it should grow up well. On the day "
                "family and those close to them gather, eat together and "
                "celebrate. Various objects are also set out on a table, and "
                "everyone enjoys the 돌잡이 — guessing the child's future from "
                "whichever object it takes hold of.",
            ],
        ),
        "성인으로 성장, 성년식": dict(
            title="Coming of age: the 성년식",
            paragraphs=[
                "Korea marks the third Monday in May as the Coming of Age "
                "Day, congratulating young people who have turned nineteen on "
                "becoming adults and raising their sense of their own worth. "
                "Nineteen is generally reached after leaving high school. "
                "Marriage and voting are open from eighteen, but smoking and "
                "drinking are lawful only from nineteen. The usual presents "
                "for the day are roses and perfume.",
            ],
        ),
        "죽은 사람을 떠나 보냄, 장례식": dict(
            title="Seeing the dead away: the funeral",
            paragraphs=[
                "The rite of seeing off the deceased with due propriety when "
                "someone has died is the 장례. In Korea it generally runs "
                "three days, at a funeral hall inside a hospital or standing "
                "on its own, and callers are received on the first and second "
                "days.",

                "A caller comes soberly, in neat clothes of black or "
                "near-black, with a gift of condolence money. Entering the "
                "hall they bow twice to the deceased and once to the bereaved "
                "family. Practice differs a little with religion; Protestants "
                "may stand in silent prayer instead of bowing. The caller "
                "offers the family a few brief words of comfort. The third "
                "day is the day of parting. The deceased may be buried in a "
                "cemetery, or cremated and laid in a charnel house or a "
                "memorial park.",
            ],
        ),
        "조상을 정성껏 섬김, 제사": dict(
            title="Serving the ancestors with care: the 제사",
            paragraphs=[
                "The rite of setting out food and giving one's whole care "
                "while thinking of an ancestor who has died is called 제사. "
                "On the anniversary of the death it is the 기제사; at the "
                "seasonal festivals it is the 차례. Korea has long held the "
                "custom of believing that a family prospers by serving its "
                "ancestors well.",

                "At a 제사 the family gathers and, in remembrance, bows twice "
                "to the ancestor before the food set out for them.",

                "When the rite is over the family sits down together and eats "
                "that food. This is called 음복. It carries the sense of "
                "sharing out the blessing the ancestor gives.",

                "Lately the way a 제사 is held has grown various, according to "
                "religion and to a household's circumstances. On the whole "
                "the number of rites, the time they take and the range of "
                "food are all being simplified.",
            ],
        ),
    },

    extraAnnotations={
        "조상": dict(
            hanja="祖上", meaning="an ancestor",
            characters=[("祖", "조", "forefather — as in 조부 “grandfather”"),
                        ("上", "상", "above — as in 상급 “higher grade”")],
        ),
        "추모": dict(
            hanja="追慕", meaning="to remember the dead",
            characters=[("追", "추", "to follow after — as in 추억, 추적"),
                        ("慕", "모", "to long for, to yearn")],
        ),
        "선호하다": dict(
            hanja="選好하다", meaning="to prefer",
            characters=[("選", "선", "to choose — as in 선발 “selection”, 선거"),
                        ("好", "호", "to like, good — as in 호감 “liking”")],
        ),
        "의례": dict(
            hanja="儀禮", meaning="a rite, a ceremony",
            characters=[("儀", "의", "ceremony, manner — as in 의식 “ceremony”"),
                        ("禮", "례", "rite, courtesy — as in 예절, 예의")],
        ),
        "통과의례": dict(
            hanja="通過儀禮", meaning="a rite of passage",
            characters=[("通", "통", "to pass through — as in 교통, 통신"),
                        ("過", "과", "to pass, excess — as in 과거 “the past”")],
            notes=["The word covers the whole set this chapter deals with: "
                   "the first birthday, coming of age, marriage, the "
                   "funeral."],
        ),
        "결혼식": dict(
            hanja="結婚式", meaning="a wedding",
            characters=[("結", "결", "to tie, bind — as in 결과 “result”, 체결"),
                        ("婚", "혼", "marriage — as in 혼인, 기혼"),
                        ("式", "식", "ceremony, form — as in 형식 “form”, 입학식")],
        ),
        "서약": dict(
            hanja="誓約", meaning="a vow, a pledge",
            characters=[("誓", "서", "to swear an oath"),
                        ("約", "약", "to promise — as in 약속 “promise”, 계약")],
        ),
        "미성년자": dict(
            hanja="未成年者", meaning="a minor",
            characters=[("未", "미", "not yet — as in 미래 “future”, 미혼"),
                        ("成", "성", "to become — as in 성장 “growth”, 성인"),
                        ("年", "년", "year — as in 연령 “age”, 노년")],
            notes=["Literally “one who has not yet come of age”."],
        ),
        "동의": dict(
            hanja="同意", meaning="consent, agreement",
            characters=[("同", "동", "same — as in 동일 “identical”, 동문회"),
                        ("意", "의", "intention, meaning — as in 의미, 의식")],
        ),
        "정식": dict(
            hanja="正式", meaning="formal, official",
            characters=[("正", "정", "correct, proper — as in 정확 “accurate”")],
        ),
        "혼인 신고": dict(
            hanja="婚姻申告", meaning="registration of a marriage",
            characters=[("姻", "인", "marriage, in-law"),
                        ("申", "신", "to state, report — as in 신청 “application”"),
                        ("告", "고", "to tell — as in 광고 “advertisement”, 신고")],
            notes=["The wedding is the ceremony; the 혼인 신고 at the district "
                   "office is what makes the marriage exist in law."],
        ),
        "법적": dict(
            hanja="法的", meaning="legal, in law",
            characters=[("法", "법", "law — as in 법무부, 헌법")],
        ),
        "신랑": dict(
            hanja="新郞", meaning="a bridegroom",
            characters=[("新", "신", "new — as in 신입 “new entrant”, 신생아"),
                        ("郞", "랑", "a young man")],
        ),
        "신부": dict(
            hanja="新婦", meaning="a bride",
            characters=[("婦", "부", "woman, wife — as in 주부, 효부")],
            notes=["The same 신부 is also the word for a Catholic priest, "
                   "written 神父 — different characters, same sound."],
        ),
        "예식장": dict(
            hanja="禮式場", meaning="a wedding hall",
            characters=[("場", "장", "place, ground — as in 시장 “market”, 직장")],
            notes=["A building given over to weddings, which run one after "
                   "another through the day."],
        ),
        "성당": dict(
            hanja="聖堂", meaning="a Catholic church",
            characters=[("聖", "성", "holy, sacred"),
                        ("堂", "당", "hall — as in 식당, 봉안당")],
            notes=["교회 is the Protestant church, 성당 the Catholic one, 절 "
                   "the Buddhist temple."],
        ),
        "축의금": dict(
            hanja="祝儀金", meaning="congratulatory money",
            characters=[("祝", "축", "to celebrate — as in 축하 “congratulation”"),
                        ("儀", "의", "ceremony — the same 儀 as in 의례"),
                        ("金", "금", "gold, money — as in 요금 “fee”, 보증금")],
            notes=["Given in a white envelope at a wedding. Its counterpart "
                   "at a funeral is the 조의금."],
        ),
        "돌": dict(
            meaning="the first anniversary of a birth",
            notes=["Pure Korean. 돌잔치 is the party, 돌잡이 the game of "
                   "grasping."],
        ),
        "돌잔치": dict(
            meaning="the first-birthday feast",
            notes=["돌 + 잔치 “feast”. Once it marked survival through the "
                   "dangerous first year; now it is a large family party."],
        ),
        "돌잡이": dict(
            meaning="doljabi, the grasping game at a 돌잔치",
            notes=["Objects are set on a table and what the child picks up is "
                   "read as its future — thread for long life, money for "
                   "wealth, a pencil for scholarship, now sometimes a "
                   "stethoscope or a microphone."],
        ),
        "무사하다": dict(
            hanja="無事하다", meaning="to be safe and sound",
            characters=[("無", "무", "without — as in 무료 “free of charge”, 무상"),
                        ("事", "사", "affair, incident — as in 사건, 사례")],
            notes=["Literally “without incident”."],
        ),
        "맞이하다": dict(
            meaning="to greet, to meet (a day, a guest)",
            notes=["The verb for coming up to a time as well as for receiving "
                   "a person: 생일을 맞이하다, 손님을 맞이하다."],
        ),
        "기념": dict(
            hanja="紀念", meaning="commemoration",
            characters=[("紀", "기", "record, era"),
                        ("念", "념", "thought — as in 이념 “ideology”, 묵념")],
        ),
        "소망": dict(
            hanja="所望", meaning="a hope, a wish",
            characters=[("所", "소", "place, that which — as in 장소 “place”"),
                        ("望", "망", "to look far, to hope — as in 희망 “hope”")],
        ),
        "골라잡다": dict(
            meaning="to pick out and take hold of",
            notes=["고르다 “to choose” + 잡다 “to grasp” — exactly what the "
                   "child does at the 돌잡이."],
        ),
        "예상": dict(
            hanja="豫想", meaning="to expect, to foresee",
            characters=[("豫", "예", "beforehand — as in 예방 “prevention”, 예약"),
                        ("想", "상", "to think — as in 사상 “thought”")],
        ),
        "상": dict(
            hanja="床", meaning="a low table",
            notes=["The small legged table food is set on and carried in. "
                   "제사상 is the table laid for the ancestral rite."],
        ),
        "성인": dict(
            hanja="成人", meaning="an adult",
            characters=[("成", "성", "to become — the same 成 as in 미성년자"),
                        ("人", "인", "person — as in 인구, 개인")],
        ),
        "성년의 날": dict(
            hanja="成年의날", meaning="Coming of Age Day",
            notes=["The third Monday in May. Roses and perfume are the "
                   "customary presents."],
        ),
        "자부심": dict(
            hanja="自負心", meaning="self-esteem, pride in oneself",
            characters=[("自", "자", "self — as in 자유 “freedom”, 자립"),
                        ("負", "부", "to bear, to carry"),
                        ("心", "심", "heart, mind — as in 관심 “interest”, 중심")],
        ),
        "젊은이": dict(
            meaning="a young person",
            notes=["From 젊다 “to be young”. Its counterpart is 늙은이."],
        ),
        "선거": dict(
            hanja="選擧", meaning="an election",
            characters=[("選", "선", "to choose — as in 선발, 선호하다"),
                        ("擧", "거", "to raise, to hold (an event)")],
        ),
        "흡연": dict(
            hanja="吸煙", meaning="smoking",
            characters=[("吸", "흡", "to inhale — as in 호흡 “breathing”"),
                        ("煙", "연", "smoke")],
        ),
        "음주": dict(
            hanja="飮酒", meaning="drinking alcohol",
            characters=[("飮", "음", "to drink — as in 음료 “beverage”, 음식"),
                        ("酒", "주", "alcohol — as in 맥주 “beer”, 소주")],
        ),
        "장미꽃": dict(hanja="薔薇꽃", meaning="a rose"),
        "향수": dict(
            hanja="香水", meaning="perfume",
            characters=[("香", "향", "fragrance — as in 향기 “scent”"),
                        ("水", "수", "water — as in 수도, 배산임수")],
            notes=["A different 향수(鄕愁) means homesickness — 鄕 “home "
                   "village” as in 고향, 향우회."],
        ),
        "백일": dict(
            hanja="百日", meaning="the hundredth day after a birth",
            characters=[("百", "백", "hundred — as in 백지장, 수백만")],
        ),
        "백일잔치": dict(
            meaning="the hundredth-day feast",
            notes=["Held because a baby that lived a hundred days was thought "
                   "past the worst danger. 백설기, the plain white rice cake, "
                   "is made for it."],
        ),
        "돌리다": dict(
            meaning="to hand round, to distribute; to turn",
            notes=["떡을 돌리다 is to send rice cake round to the neighbours — "
                   "the same verb as turning something."],
        ),
        "추억": dict(
            hanja="追憶", meaning="a memory, a recollection",
            characters=[("追", "추", "to pursue, follow after — as in 추모, 추적"),
                        ("憶", "억", "to remember")],
        ),
        "장례식": dict(
            hanja="葬禮式", meaning="a funeral",
            characters=[("葬", "장", "to bury — as in 매장, 화장, 자연장"),
                        ("禮", "례", "rite — the same 禮 as in 의례, 예절")],
        ),
        "장례": dict(hanja="葬禮", meaning="funeral rites"),
        "장례식장": dict(
            hanja="葬禮式場", meaning="a funeral hall",
            notes=["Most Korean funerals are held at a hall inside a hospital "
                   "over three days, with the family receiving callers."],
        ),
        "고인": dict(
            hanja="故人", meaning="the deceased",
            characters=[("故", "고", "old, the late — as in 고향, 연고"),
                        ("人", "인", "person")],
            notes=["Literally “the person of before”. The respectful word for "
                   "someone who has died."],
        ),
        "절차": dict(
            hanja="節次", meaning="a procedure, the order of things",
            characters=[("節", "절", "joint, section — as in 명절, 예절"),
                        ("次", "차", "order, time — as in 차시, 4차 산업혁명")],
        ),
        "문상객": dict(
            hanja="問喪客", meaning="a caller at a funeral",
            characters=[("問", "문", "to ask — as in 질문 “question”, 방문"),
                        ("喪", "상", "mourning, loss"),
                        ("客", "객", "guest — as in 관광객 “tourist”, 승객")],
        ),
        "엄숙하다": dict(
            hanja="嚴肅하다", meaning="to be solemn",
            characters=[("嚴", "엄", "strict, stern"),
                        ("肅", "숙", "solemn, respectful")],
        ),
        "단정하다": dict(
            hanja="端正하다", meaning="to be neat, well-ordered",
            characters=[("端", "단", "end, upright"),
                        ("正", "정", "correct — the same 正 as in 정식, 정확")],
        ),
        "조의금": dict(
            hanja="弔意金", meaning="condolence money",
            characters=[("弔", "조", "to mourn, to condole"),
                        ("意", "의", "intention, feeling — as in 동의, 의식")],
            notes=["Given in a white envelope, as the 축의금 is at a wedding. "
                   "The etiquette differs: nothing red, nothing bright."],
        ),
        "유족": dict(
            hanja="遺族", meaning="the bereaved family",
            characters=[("遺", "유", "to leave behind — as in 유골, 유산"),
                        ("族", "족", "family, clan — as in 가족, 친족")],
        ),
        "개신교": dict(
            hanja="改新敎", meaning="Protestantism",
            characters=[("改", "개", "to reform, alter — as in 개조, 개혁"),
                        ("新", "신", "new — as in 신랑, 신문"),
                        ("敎", "교", "teaching, religion — as in 유교, 종교")],
            notes=["Literally “the reformed religion”. 천주교 is Catholicism; "
                   "together they are 기독교."],
        ),
        "묵념": dict(
            hanja="默念", meaning="silent prayer, a moment's silence",
            characters=[("默", "묵", "silent"),
                        ("念", "념", "thought — the same 念 as in 기념")],
        ),
        "위로": dict(
            hanja="慰勞", meaning="comfort, consolation",
            characters=[("慰", "위", "to console"),
                        ("勞", "로", "labour, toil — as in 노동, 근로자")],
        ),
        "간결하다": dict(
            hanja="簡潔하다", meaning="to be brief and plain",
            characters=[("簡", "간", "simple, brief — as in 간편, 간소화"),
                        ("潔", "결", "clean, pure")],
        ),
        "묘지": dict(
            hanja="墓地", meaning="a grave, a cemetery",
            characters=[("墓", "묘", "grave"),
                        ("地", "지", "ground — as in 지역, 지위")],
        ),
        "매장": dict(
            hanja="埋葬", meaning="burial",
            characters=[("埋", "매", "to bury"),
                        ("葬", "장", "funeral rites — the same 葬 as in 화장")],
            notes=["A different 매장(賣場) means a shop floor — 賣 “to sell”."],
        ),
        "화장": dict(
            hanja="火葬", meaning="cremation",
            characters=[("火", "화", "fire — as in 화재 “fire”, 화요일"),
                        ("葬", "장", "funeral rites")],
            notes=["Not the 화장(化粧) of 화장품, cosmetics — different "
                   "characters, same sound."],
        ),
        "추모공원": dict(
            hanja="追慕公園", meaning="a memorial park",
            notes=["Where cremated remains are laid, an alternative to the "
                   "봉안당."],
        ),
        "봉안당": dict(
            hanja="奉安堂", meaning="a charnel house, a columbarium",
            notes=["Also called 납골당. Where the ashes are kept after "
                   "cremation."],
        ),
        "제사": dict(
            hanja="祭祀", meaning="the memorial rite for an ancestor",
            characters=[("祭", "제", "rite, festival — as in 축제 “festival”"),
                        ("祀", "사", "to offer sacrifice")],
        ),
        "기일": dict(
            hanja="忌日", meaning="the anniversary of a death",
            characters=[("忌", "기", "to shun, to mourn"),
                        ("日", "일", "day — as in 백일, 생일")],
        ),
        "기제사": dict(
            hanja="忌祭祀", meaning="the rite on the anniversary of a death",
            notes=["Held at night on the eve of the 기일. Its counterpart at "
                   "the festivals is the 차례."],
        ),
        "차례": dict(
            hanja="茶禮", meaning="the ancestral rite at a festival",
            characters=[("茶", "차", "tea — as in 녹차 “green tea”"),
                        ("禮", "례", "rite — as in 의례, 장례")],
            notes=["Literally “the tea rite”. Held in the morning at 설날 and "
                   "추석. A different 차례(次例) means “order, turn”."],
        ),
        "정성": dict(
            hanja="精誠", meaning="wholehearted care, devotion",
            characters=[("精", "정", "refined, essence — as in 정밀하다"),
                        ("誠", "성", "sincerity — as in 성실 “sincere”")],
        ),
        "바치다": dict(
            meaning="to offer up, to dedicate",
            notes=["Used of what is offered to an ancestor, a god or a "
                   "cause — not of an ordinary gift."],
        ),
        "자손": dict(
            hanja="子孫", meaning="descendants",
            characters=[("子", "자", "child — as in 자녀, 효자"),
                        ("孫", "손", "grandchild — as in 손자, 효손")],
        ),
        "음복": dict(
            hanja="飮福", meaning="sharing the food of the rite",
            characters=[("飮", "음", "to drink — as in 음주, 음식"),
                        ("福", "복", "blessing, fortune — as in 복지 “welfare”")],
            notes=["Literally “drinking the blessing”. Eating what was set "
                   "out for the ancestor is receiving a share of what they "
                   "give back."],
        ),
        "복": dict(
            hanja="福", meaning="blessing, good fortune",
            notes=["The same 福 as in 복지 “welfare” and 행복 “happiness”."],
        ),
        "여건": dict(
            hanja="與件", meaning="conditions, the circumstances given",
            characters=[("與", "여", "to give — as in 수여 “to confer”, 참여"),
                        ("件", "건", "matter, item — as in 사건 “incident”, 조건")],
        ),
        "전반적": dict(
            hanja="全般的", meaning="overall, general",
            characters=[("全", "전", "whole — as in 전국 “nationwide”, 안전"),
                        ("般", "반", "sort, general — as in 일반 “general”")],
        ),
        "횟수": dict(
            hanja="回數", meaning="the number of times",
            characters=[("回", "회", "to turn, a time — as in 회갑, 향우회"),
                        ("數", "수", "number — as in 수학, 다수")],
        ),
        "간소화": dict(
            hanja="簡素化", meaning="simplification",
            characters=[("簡", "간", "simple — the same 簡 as in 간결하다"),
                        ("素", "소", "plain, element — as in 영양소, 요소")],
        ),
        "희망": dict(
            hanja="希望", meaning="to hope for, to wish",
            characters=[("希", "희", "to hope, rare"),
                        ("望", "망", "to look far — the same 望 as in 소망")],
        ),
        "위생적": dict(
            hanja="衛生的", meaning="hygienic",
            characters=[("衛", "위", "to guard — as in 방위 “defence”"),
                        ("生", "생", "life — as in 생활, 위생")],
        ),
        "간편하다": dict(
            hanja="簡便하다", meaning="to be simple and easy",
            characters=[("便", "편", "convenient — as in 편리 “convenient”, 편의")],
        ),
        "유골": dict(
            hanja="遺骨", meaning="cremated remains, bones left behind",
            characters=[("遺", "유", "to leave behind — the same 遺 as in 유족"),
                        ("骨", "골", "bone — as in 납골당")],
        ),
        "생태": dict(
            hanja="生態", meaning="ecology, the living world",
            characters=[("態", "태", "form, condition — as in 상태 “condition”")],
        ),
        "자연장": dict(
            hanja="自然葬", meaning="natural burial",
            notes=["Cremated remains buried among trees, flowers or grass, "
                   "rather than kept in a 봉안당."],
        ),
        "주목": dict(
            hanja="注目", meaning="attention, notice",
            characters=[("注", "주", "to pour, to focus — as in 주의 “caution”"),
                        ("目", "목", "eye — as in 목표 “goal”, 과목")],
        ),
        "화초": dict(
            hanja="花草", meaning="flowering plants",
            characters=[("花", "화", "flower"),
                        ("草", "초", "grass — as in 약초, 초가집")],
        ),
        "잔디": dict(meaning="lawn grass, turf"),
        "보존": dict(
            hanja="保存", meaning="preservation",
            characters=[("保", "보", "to protect — as in 보험 “insurance”, 보장"),
                        ("存", "존", "to exist — as in 존재 “existence”")],
        ),
        "기여": dict(
            hanja="寄與", meaning="to contribute",
            characters=[("寄", "기", "to send, to entrust"),
                        ("與", "여", "to give — the same 與 as in 여건, 수여")],
        ),
        "환갑": dict(
            hanja="還甲", meaning="the sixtieth birthday",
            characters=[("還", "환", "to return — as in 환전 “currency exchange”"),
                        ("甲", "갑", "the first of the ten heavenly stems")],
            notes=["The sixty-year cycle of stems and branches comes round to "
                   "where it began, so the year of one's birth returns. Also "
                   "called 회갑."],
        ),
        "회갑": dict(
            hanja="回甲", meaning="the sixtieth birthday",
            characters=[("回", "회", "to turn round — the same 回 as in 횟수")],
        ),
        "수명": dict(
            hanja="壽命", meaning="lifespan",
            characters=[("壽", "수", "long life — as in 장수"),
                        ("命", "명", "life — as in 생명, 운명")],
        ),
        "장수": dict(
            hanja="長壽", meaning="longevity",
            characters=[("長", "장", "long — as in 장기 “long term”, 사장")],
        ),
        "기원하다": dict(
            hanja="祈願하다", meaning="to pray for, to wish for",
            characters=[("祈", "기", "to pray — as in 기도 “prayer”"),
                        ("願", "원", "to wish — as in 소원 “a wish”, 지원")],
        ),
        "드물다": dict(meaning="to be rare, uncommon"),
        "칠순": dict(
            hanja="七旬", meaning="the seventieth birthday",
            characters=[("七", "칠", "seven"),
                        ("旬", "순", "a period of ten — as in 육순, 팔순, 구순")],
            notes=["旬 counts a decade of years here. 육순 is sixty, 팔순 "
                   "eighty, 구순 ninety."],
        ),
        "고희연": dict(
            hanja="古稀宴", meaning="the seventieth-birthday feast",
            characters=[("古", "고", "old — as in 고궁, 고대"),
                        ("稀", "희", "rare, sparse"),
                        ("宴", "연", "a feast")],
            notes=["고희 comes from a line of Du Fu: “to live seventy years "
                   "has been rare since old times”."],
        ),
    },

    extraNotes=[
        "The 장례식 article on p. 86 is hard to read: the sentences about the "
        "third day appear twice over, once faintly. I have taken the fainter "
        "run as show-through from the facing page and kept the darker one, "
        "but that paragraph is worth checking against the book.",
        "The table of age names on p. 87 is printed as four age-and-name "
        "pairs across, three rows deep. It is set here as a single "
        "two-column table of twelve rows, which reads better on a narrow "
        "screen.",
        "The 관련 단원 table on p. 84 merges 기본 and 문화 across its two rows. "
        "A merged cell cannot be expressed here, so both values repeat.",
    ],
)
