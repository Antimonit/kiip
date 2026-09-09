# -*- coding: utf-8 -*-
"""제1편 사회 — the spread that closes the part, pp. 48-51.

대단원 정리 and a matching quiz, then 단원 종합 평가, then two pages on the
days the country marks: 5대 국경일 and the 국가 기념일. Transcribed from the
photos.

The answers to the quiz and to the 종합 평가 are mine, worked out from the
chapters; the book keeps its own in 정답보기 on p. 262, which is not
photographed.
"""

from . import SECTION, HEADING, PARAGRAPH, BULLET, FIGURE, TABLE, VERSE

PART = dict(
    number=1, slug="part-1", part=True,
    unit="사회", title="대단원 마무리", titleEn="Closing the part",

    append=[
        SECTION("summary", "대단원 정리"),
        HEADING(3, "키워드로 보는 한국사회"),
        TABLE([["1. 한국의 상징", "공식 국가명, 국기, 국화, 국가, 국가 문장, 한글"],
               ["2. 가족", "확대가족, 핵가족, 1인 가족, 가족문화, 호칭, 촌수"],
               ["3. 일터",
                "한국인들이 선호하는 일터, 여성의 경제활동, 정규 근무, 탄력적 근무 시간제, "
                "교대 근무, 직장 문화"],
               ["4. 교통와 통신",
                "교통수단, 교통카드, 환승 할인, 버스 전용 차로제, 우편, 택배, 휴대 전화, "
                "인터넷"],
               ["5. 주거", "단독 주택, 공동 주택, 전세, 월세, 반전세, 부동산"],
               ["6. 도시와 농촌",
                "도시화, 위성도시, 도시재생, 농촌의 고령화, 농산물 직거래, 기계화, 자동화"],
               ["7. 복지", "사회보험, 공공부조, 긴급복지지원, 외국인 종합 안내센터"],
               ["8. 의료와 안전",
                "의료 기관, 동네 의원, 보건소, 종합병원, 행정안전부, 긴급 신고 전화"]]),

        SECTION("quiz", "퀴즈"),
        PARAGRAPH("한국의 상징과 관련 있는 정답 단어 3개를 {조합}하여 아래 퀴즈의 정답을 "
                  "찾아보세요."),
        PARAGRAPH("퀴즈: 세계에서 가장 큰 {야외} {벽화}는?"),
        TABLE(["한국상징", "정답단어"],
              [["주택", "부산"],
               ["복지", "목포"],
               ["무궁화", "인천"],
               ["농촌", "서울"],
               ["사회보험", "수원"],
               ["인터넷", "대구"],
               ["애국가", "사일로"],
               ["공공부조", "이화"],
               ["교통수단", "재생"],
               ["건강보험", "디자인"],
               ["태극기", "벽화"],
               ["통신수단", "조각"]]),
        PARAGRAPH("정답 ( 인천 사일로 벽화 )"),

        SECTION("exam", "단원 종합 평가"),
        HEADING(4, "01 〈보기〉에서 설명하는 것은 무엇인가?"),
        VERSE("조선의 세종대왕이 만들었다.",
              "매년 10월 9일에 기념 행사를 개최하고 있다.",
              "사람의 발음 기관과 하늘, 땅, 사람 모양을 본떠 만들었다."),
        BULLET("① 한글"),
        BULLET("② 태극기"),
        BULLET("③ 애국가"),
        BULLET("④ 국가 문장"),
        PARAGRAPH("정답 ( ① )"),

        HEADING(4, "02 한국 사회에 관한 설명으로 옳은 것을 〈보기〉에서 모두 고른 것은?"),
        VERSE("ㄱ. 직업별 남녀 간 불균형이 뚜렷해지고 있다.",
              "ㄴ. 여성의 사회 진출이 과거에 비해 활발해졌다.",
              "ㄷ. 과거에는 확대가족이 많았으나 요즘은 핵가족 형태가 많다.",
              "ㄹ. 아내의 가족과 남편의 가족에 대한 호칭 구분이 명확해지고 있다."),
        BULLET("① ㄱ, ㄷ"),
        BULLET("② ㄱ, ㄹ"),
        BULLET("③ ㄴ, ㄷ"),
        BULLET("④ ㄴ, ㄹ"),
        PARAGRAPH("정답 ( ③ )"),

        HEADING(4, "03 다음 중 대중교통 이용 장려 제도와 관련이 깊은 것은?"),
        BULLET("① 인터넷"),
        BULLET("② 사회보험"),
        BULLET("③ 환승 제도"),
        BULLET("④ 도시 재생"),
        PARAGRAPH("정답 ( ③ )"),

        HEADING(4, "04 다음 중 공동 주택에 속하지 않는 것은?"),
        BULLET("① 아파트"),
        BULLET("② 연립주택"),
        BULLET("③ 다세대 주택"),
        BULLET("④ 다가구 주택"),
        PARAGRAPH("정답 ( ④ )"),

        HEADING(4, "05 안전한 생활을 위한 방법으로 옳지 않은 것은?"),
        BULLET("① 작업할 때는 보호 장비를 반드시 착용한다."),
        BULLET("② 긴급한 사고가 발생했을 때는 빨리 118에 전화한다."),
        BULLET("③ 정부 차원에서 매년 실시하는 재난 대비 훈련에 참여한다."),
        BULLET("④ 평상시 비상구와 구급 상자, 소화기 설치 위치를 확인해 둔다."),
        PARAGRAPH("정답 ( ② )"),

        HEADING(4, "06 〈보기〉의 ㉠, ㉡에서 설명하는 복지 제도로 옳은 것은?"),
        VERSE("㉠ 아파서 병원에 갈 때 의료비의 일부를 지원 받을 수 있다.",
              "㉡ 나이가 들어 더 이상 돈을 벌기 어려울 때 매달 일정 금액을 생활비로 지급받을 수 "
              "있다."),
        BULLET("① 병원보험 / 긴급복지"),
        BULLET("② 의료급여 / 노후자금"),
        BULLET("③ 고용보험 / 공공부조"),
        BULLET("④ 건강보험 / 국민연금"),
        PARAGRAPH("정답 ( ④ )"),

        SECTION("feature", "5대 국경일의 유래와 의미"),
        HEADING(3, "국경일: 나라의 경사스러운 날을 기념하기 위하여 법률로써 지정한 날"),
        PARAGRAPH("{국경일}은 1949년 10월 1일 법률 제53호 〈국경일에 관한 법률〉에 의하여 "
                  "지정되었다. 이 법률에 의해 {삼일절}, {제헌절}, {광복절}, {개천절}이 국경일로 "
                  "지정되어 네 개의 국경일을 4대 국경일이라고 {불렀으며|부르다}, 2006년부터는 "
                  "{한글날}도 국경일에 포함되어 5대 국경일이 되었다. 국경일에는 태극기를 "
                  "{게양}한다."),

        HEADING(4, "3월 1일(삼일절): 일본의 지배에 저항하여 일어난 독립 만세 운동을 기념하는 날"),
        PARAGRAPH("1919년 3월 1일 민족 대표 33인의 {독립 선언서} {낭독}으로 시작된 독립 만세 "
                  "운동은 당시 한국을 지배하고 있는 {일제}의 {압박}에 {항거}하기 위해 전 "
                  "세계에 민족의 {자주 독립}을 {선언}하고 독립 만세를 외친 민족 운동이었다. "
                  "이러한 한국의 자주 독립 {정신}을 기념하기 위하여 정부는 1949년에 3월 1일을 "
                  "국경일로 정하였다."),
        FIGURE("태극기를 든 사람들이 만세를 부르는 그림"),

        HEADING(4, "7월 17일(제헌절): 대한민국 최초의 헌법이 제정된 날을 기념하는 날"),
        PARAGRAPH("자유 민주주의를 기본으로 한 대한민국 헌법의 {제정}(1948년 7월 12일)과 "
                  "{공포}(국민에게 알림, 1948년 7월 17일)를 {축하}하고, {준법정신}을 높일 "
                  "목적으로 제정된 국경일이다. 국경일들은 모두 {공휴일}(공적으로 쉬기로 정해진 "
                  "날)로 되어 왔으나, 2008년부터는 국경일의 {지위}는 유지하지만 공휴일에서는 "
                  "{제외}되었다."),
        FIGURE("대한민국헌법 제1장 제1조 — ① 대한민국은 민주공화국이다. ② 대한민국의 주권은 "
               "국민에게 있고, 모든 권력은 국민으로부터 나온다."),

        HEADING(4, "8월 15일(광복절): 일본의 지배에서 벗어나 독립한 것을 기념하는 날"),
        PARAGRAPH("1945년 8월 15일 일본의 {항복}으로 제2차 세계 대전이 {종식}되어 한국이 "
                  "독립하였고, 1948년 8월 15일 대한민국 정부가 {수립}되었다. 대한민국 정부는 "
                  "일본의 지배로부터 벗어난 날과 {독립국}으로서 정부가 수립된 날을 기념하기 위해 "
                  "매년 8월 15일을 광복절이라 하고 국경일로 지정하였다. ‘{광복}’이란 ‘빛을 "
                  "되찾다’는 뜻으로서 잃었던 {국권}의 {회복}을 의미한다."),
        FIGURE("광복으로 서울 서대문형무소를 나서는 독립지사들의 환호하는 모습. "
               "한국학중앙연구원"),

        HEADING(4, "10월 3일(개천절): 한국 최초의 국가인 고조선이 만들어진 것을 기념하는 날"),
        PARAGRAPH("기원전 2333년(戊辰年), {음력} 10월 3일에 {국조} {단군}이 최초의 민족 국가인 "
                  "{단군조선}을 {건국}했음을 {기리는|기리다} 뜻으로 제정되었다. 여기서 "
                  "{개천}(開天; 하늘이 열림)이라 함은 최초의 국가 {고조선}을 {건설}한 사건을 "
                  "{상징적}으로 표현한 것으로 민족의 {탄생}이나 {민족사}의 시작을 의미한다. 음력 "
                  "10월 3일로 {지켜오다가|지키다} 그 뒤 음력보다 {양력}을 주로 쓰게 되면서, "
                  "개천절도 1949년에 양력 10월 3일로 바뀌었다."),
        FIGURE("단군릉, 개천절 기념행사. 한국학중앙연구원"),

        HEADING(4, "10월 9일(한글날): 세종대왕이 한글 만든 것을 기념하는 날"),
        PARAGRAPH("〈훈민정음〉 해례본(해설한 책)에 적힌 ‘정통(正統) 11년 9월 {상한}(上澣)-세종 "
                  "28년 9월’을 양력으로 {환산}하면 10월 9일이 되어, 이날을 훈민정음을 "
                  "{반포}(세상에 널리 퍼뜨려 모두 알게 함)한 날로 {확정}하였다. 그리하여 한글 "
                  "{창제} 500주년인 1946년부터 10월 9일을 한글날로 지켜 오고 있다."),
        FIGURE("훈민정음을 반포하는 세종대왕 그림"),

        SECTION("feature", "국가 기념일"),
        HEADING(3, "국가 기념일: 국가가 제정·주관하는 기념일"),
        PARAGRAPH("{국가 기념일}이란 ‘각종 기념일 등에 관한 {규정}’(대통령령)에 따라 국가가 "
                  "제정·{주관}하는 기념일로, ‘{법정 기념일}’이라고도 한다. 국가 기념일은 원래 "
                  "공휴일이 아니지만, 일부 기념일이 공휴일이 되었다. 국가 기념일로 지정되면 "
                  "{주관 부처}(정부 조직의 부와 처)가 정해지고, 이후 부처 {자체적}으로 예산을 "
                  "확보해 {기념식}과 관련 행사를 전국적인 {범위}로 행할 수 있다."),
        PARAGRAPH("[4월 5일] 식목일, [4월 19일] 4·19혁명 기념일, [4월 20일] 장애인의 날, "
                  "[5월 1일] 근로자의 날, [5월 5일] 어린이날, [5월 8일] 어버이날, "
                  "[5월 15일] 스승의 날, [5월 18일] 5·18 민주화 운동 기념일, "
                  "[5월 셋째 월요일] 성년의 날, [6월 6일] 현충일, [10월 1일] 국군의 날 등 총 "
                  "51개의 기념일이 지정돼 있다."),

        HEADING(4, "6월 6일(현충일): 국가를 위해 자신의 목숨을 바친 분들을 기리는 날"),
        PARAGRAPH("한국은 1948년 8월에 정부를 수립한 뒤, 2년도 못 되어 1950년에 6·25 전쟁을 "
                  "겪었는데 이 때 25만 명 이상의 국군이 사망하였다. 그래서 정부는 1956년에 "
                  "대통령령으로 6월 6일을 {현충일}로 정하고, {추모} 행사를 갖도록 하였다. 그 후 "
                  "매년 6월 6일 현충일이 되면 대통령과 정부 사람들은 각종 추모 기념식을 갖고 "
                  "{현충원}(국가를 위해 목숨을 바친 분들이 {안장}되어 있는 {국립묘지})을 "
                  "{참배}한다. 오전 10시 정각에 사이렌 소리와 함께 전 국민은 1분간 {경건히} "
                  "{묵념}을 하고 나라를 위해 싸우다 숨진 국군 {장병} 및 {순국선열}(나라를 위해 "
                  "목숨을 바친 분)들을 추모하는 시간을 갖는다. 현충일에는 각 {관공서}를 비롯하여 "
                  "각 기업, 단체, 가정 등에서 태극기를 게양한다."),
        FIGURE("현충원 모습"),

        HEADING(4, "10월 1일(국군의 날): 한국 군대의 창설과 발전을 기념하여 정한 날"),
        PARAGRAPH("1950년 10월 1일은 한국군이 {남침}한 북한 {공산군}을 {반격}한 끝에 "
                  "{38선}(북위 38°선)을 {돌파}한 날로서, 이 날의 {의의}를 살리기 위하여 국군의 "
                  "날로 지정하였다."),
        PARAGRAPH("이 날에는 육군·해군·공군·해병대 및 육군사관학교, 해군사관학교, 공군사관학교, "
                  "육군3사관학교, 국군간호사관학교 {생도}들의 {행진} 등 각종 기념 행사가 열리기도 "
                  "한다."),
        FIGURE("국군의 날 행진 모습"),
    ],

    extraAnnotations={
        "부르다": dict(
            meaning="to call (something) by a name",
            notes=["4대 국경일이라고 불렀으며 — “were called the four great "
                   "national holidays”. 부르다 also means to sing and to "
                   "summon."],
        ),
        "상징적": dict(
            hanja="象徵的", meaning="symbolic",
            characters=[("象", "상", "image, likeness — as in 상징, 현상"),
                        ("徵", "징", "a sign — as in 징조, 특징"),
                        ("的", "적", "the adjective suffix")],
        ),
        "조합": dict(
            hanja="組合", meaning="combining, a combination",
            characters=[("組", "조", "to organise — as in 조직, 조합원"),
                        ("合", "합", "to join — as in 합의, 결합")],
        ),
        "야외": dict(
            hanja="野外", meaning="outdoors",
            characters=[("野", "야", "field, wild — as in 분야, 야구"),
                        ("外", "외", "outside — as in 외국, 국내외")],
        ),
        "벽화": dict(
            hanja="壁畫", meaning="a mural",
            characters=[("壁", "벽", "wall — as in 벽지, 담벼락"),
                        ("畫", "화", "picture — as in 그림's 畫, 영화")],
            notes=["The quiz's answer is 인천 사일로 벽화 — the grain silos at "
                   "Incheon port, painted in 2018 and held to be the largest "
                   "outdoor mural in the world."],
        ),
        "국경일": dict(
            hanja="國慶日", meaning="a national holiday",
            characters=[("慶", "경", "auspicious, to celebrate — as in 경사, 경축"),
                        ("日", "일", "day — as in 평일, 기념일")],
            notes=["Five of them: 삼일절, 제헌절, 광복절, 개천절, 한글날. Not the "
                   "same as 공휴일, a day off — 제헌절 is a 국경일 but not a "
                   "holiday from work."],
        ),
        "삼일절": dict(hanja="三一節", meaning="Independence Movement Day, 1 March"),
        "제헌절": dict(
            hanja="制憲節", meaning="Constitution Day, 17 July",
            characters=[("制", "제", "to establish — as in 제정, 제도"),
                        ("憲", "헌", "constitution — as in 헌법")],
        ),
        "광복절": dict(
            hanja="光復節", meaning="Liberation Day, 15 August",
            characters=[("光", "광", "light — as in 광고, 관광"),
                        ("復", "복", "to restore — as in 회복, 복구")],
        ),
        "개천절": dict(
            hanja="開天節", meaning="National Foundation Day, 3 October",
            characters=[("開", "개", "to open — as in 개최, 공개"),
                        ("天", "천", "heaven — as in 천지, 천문대")],
        ),
        "한글날": dict(
            meaning="Hangul Day, 9 October",
            notes=["The only 국경일 named for a piece of writing. Chapter 1 "
                   "tells the story."],
        ),
        "게양": dict(
            hanja="揭揚", meaning="hoisting (a flag)",
            characters=[("揭", "게", "to raise, to put up — as in 게시"),
                        ("揚", "양", "to raise up — as in 선양")],
        ),
        "독립 선언서": dict(hanja="獨立宣言書", meaning="the declaration of independence"),
        "낭독": dict(
            hanja="朗讀", meaning="reading aloud",
            characters=[("朗", "랑", "bright, clear"),
                        ("讀", "독", "to read — as in 독서, 구독")],
        ),
        "일제": dict(
            hanja="日帝", meaning="imperial Japan",
            notes=["Short for 일본 제국주의. 일제 강점기 is the colonial period, "
                   "1910-1945."],
        ),
        "압박": dict(
            hanja="壓迫", meaning="oppression, pressure",
            characters=[("壓", "압", "to press — as in 압력, 탄압"),
                        ("迫", "박", "to press upon, urgent — as in 박해")],
        ),
        "항거": dict(
            hanja="抗拒", meaning="resistance",
            characters=[("抗", "항", "to resist — as in 저항, 반항"),
                        ("拒", "거", "to refuse — as in 거부, 거절")],
        ),
        "자주 독립": dict(
            hanja="自主獨立", meaning="self-determination and independence",
        ),
        "선언": dict(
            hanja="宣言", meaning="a declaration",
            characters=[("宣", "선", "to proclaim — as in 선전, 선포"),
                        ("言", "언", "word, to say — as in 언어, 발언")],
        ),
        "정신": dict(hanja="精神", meaning="spirit, mind"),
        "제정": dict(
            hanja="制定", meaning="enactment (of a law)",
            characters=[("制", "제", "to institute — as in 제도, 제헌절"),
                        ("定", "정", "to fix — as in 확정, 지정")],
        ),
        "공포": dict(
            hanja="公布", meaning="promulgation, making public",
            characters=[("布", "포", "cloth; to spread — as in 반포, 배포")],
            notes=["Not the 공포 “fear” (恐怖) of 공포 영화."],
        ),
        "축하": dict(hanja="祝賀", meaning="congratulation, celebration"),
        "준법정신": dict(
            hanja="遵法精神", meaning="respect for the law",
            characters=[("遵", "준", "to comply with — as in 준수")],
        ),
        "공휴일": dict(
            hanja="公休日", meaning="a public holiday",
            notes=["A day off in law. 제헌절 kept its standing as a 국경일 in "
                   "2008 but stopped being one of these."],
        ),
        "지위": dict(hanja="地位", meaning="standing, status"),
        "제외": dict(
            hanja="除外", meaning="exclusion",
            characters=[("除", "제", "to remove — as in 면제, 삭제")],
        ),
        "항복": dict(
            hanja="降伏", meaning="surrender",
            characters=[("降", "항", "to surrender; 강 to descend — as in 하강"),
                        ("伏", "복", "to lie prostrate")],
        ),
        "종식": dict(
            hanja="終熄", meaning="an end, cessation",
            characters=[("終", "종", "end — as in 최종, 종료")],
        ),
        "수립": dict(hanja="樹立", meaning="establishment (of a government)"),
        "독립국": dict(hanja="獨立國", meaning="an independent state"),
        "광복": dict(
            hanja="光復", meaning="liberation, the recovery of light",
            notes=["Literally the light restored — which is how the article "
                   "glosses it: 빛을 되찾다."],
        ),
        "국권": dict(hanja="國權", meaning="national sovereignty"),
        "회복": dict(hanja="回復", meaning="recovery, restoration"),
        "음력": dict(
            hanja="陰曆", meaning="the lunar calendar",
            characters=[("陰", "음", "shade, negative — the 음 of 음양"),
                        ("曆", "력", "calendar — as in 달력, 양력")],
            notes=["설날 and 추석 are reckoned by it. 양력 is the solar "
                   "calendar."],
        ),
        "양력": dict(hanja="陽曆", meaning="the solar calendar"),
        "국조": dict(
            hanja="國祖", meaning="the founding father of the nation",
            characters=[("祖", "조", "ancestor — as in 조상, 조부모")],
        ),
        "단군": dict(
            meaning="Dangun, the legendary founder of Gojoseon",
            notes=["Said to have founded the first Korean state in 2333 BC, "
                   "which is the year 개천절 marks."],
        ),
        "단군조선": dict(hanja="檀君朝鮮", meaning="Dangun's Joseon, the first Korean state"),
        "건국": dict(
            hanja="建國", meaning="the founding of a country",
            characters=[("建", "건", "to build — as in 건설, 건의")],
        ),
        "기리다": dict(meaning="to commemorate, to honour"),
        "개천": dict(
            hanja="開天", meaning="the opening of heaven",
            notes=["The book explains the characters itself: 하늘이 열림."],
        ),
        "고조선": dict(hanja="古朝鮮", meaning="Gojoseon, the ancient Korean state"),
        "건설": dict(hanja="建設", meaning="construction, founding"),
        "탄생": dict(
            hanja="誕生", meaning="birth",
            characters=[("誕", "탄", "to be born — as in 탄신"),
                        ("生", "생", "to live, to be born — as in 생일, 학생")],
        ),
        "민족사": dict(hanja="民族史", meaning="the history of a people"),
        "지키다": dict(meaning="to keep, to observe (a day, a rule)"),
        "상한": dict(
            hanja="上澣", meaning="the first ten days of a lunar month",
            notes=["An old way of dividing the month into 상한, 중한, 하한. The "
                   "date in the 해례본 is what Hangul Day is reckoned from."],
        ),
        "환산": dict(
            hanja="換算", meaning="conversion (of one reckoning into another)",
            characters=[("換", "환", "to exchange — as in 교환, 환전"),
                        ("算", "산", "to reckon — as in 계산, 예산")],
        ),
        "반포": dict(
            hanja="頒布", meaning="promulgation, publishing abroad",
            characters=[("頒", "반", "to distribute"),
                        ("布", "포", "to spread — the same 布 as in 공포")],
        ),
        "확정": dict(hanja="確定", meaning="settling, fixing"),
        "창제": dict(
            hanja="創製", meaning="the creation (of a writing system)",
            characters=[("創", "창", "to originate — as in 창조, 창업"),
                        ("製", "제", "to make — as in 제작, 제품")],
            notes=["Used almost only of 한글: 한글 창제."],
        ),
        "국가 기념일": dict(
            hanja="國家記念日", meaning="a national day of remembrance",
            notes=["Fifty-one of them, set by presidential decree rather than "
                   "by statute, which is what separates them from a 국경일."],
        ),
        "규정": dict(hanja="規定", meaning="a regulation"),
        "주관": dict(
            hanja="主管", meaning="to preside over, to have charge of",
            characters=[("主", "주", "main — as in 주인, 주권"),
                        ("管", "관", "to manage — as in 관리, 보관")],
        ),
        "법정 기념일": dict(hanja="法定記念日", meaning="a statutory day of remembrance"),
        "주관 부처": dict(
            hanja="主管部處", meaning="the ministry in charge",
            notes=["부 and 처 are the two ranks chapter 22 sets out."],
        ),
        "자체적": dict(hanja="自體的", meaning="on its own, internally"),
        "기념식": dict(hanja="記念式", meaning="a commemorative ceremony"),
        "범위": dict(hanja="範圍", meaning="scope, extent"),
        "현충일": dict(
            hanja="顯忠日", meaning="Memorial Day, 6 June",
            characters=[("顯", "현", "to make manifest — as in 현저하다"),
                        ("忠", "충", "loyalty — as in 충성, 충신")],
        ),
        "추모": dict(
            hanja="追慕", meaning="remembrance of the dead",
            characters=[("追", "추", "to pursue, to follow — as in 추가, 추천"),
                        ("慕", "모", "to long for, to admire")],
        ),
        "현충원": dict(
            hanja="顯忠院", meaning="the national cemetery",
            notes=["서울현충원 at 동작동 and 대전현충원 are the two."],
        ),
        "안장": dict(
            hanja="安葬", meaning="burial, interment",
            characters=[("葬", "장", "to bury — as in 장례식")],
        ),
        "국립묘지": dict(
            hanja="國立墓地", meaning="a national cemetery",
            characters=[("墓", "묘", "grave — as in 성묘, 묘비")],
        ),
        "참배": dict(
            hanja="參拜", meaning="paying respects at a grave or shrine",
            characters=[("參", "참", "to take part — as in 참여, 참석"),
                        ("拜", "배", "to bow — as in 세배, 예배")],
        ),
        "경건히": dict(hanja="敬虔히", meaning="reverently"),
        "묵념": dict(
            hanja="默念", meaning="a silent tribute",
            characters=[("默", "묵", "silent — as in 침묵, 묵비권"),
                        ("念", "념", "thought — as in 기념, 개념")],
            notes=["The minute of silence at ten in the morning on 현충일, "
                   "marked by sirens across the country."],
        ),
        "장병": dict(
            hanja="將兵", meaning="officers and men, servicemen",
            characters=[("將", "장", "general, commander — as in 장군"),
                        ("兵", "병", "soldier — as in 병사, 군병")],
        ),
        "순국선열": dict(
            hanja="殉國先烈", meaning="patriotic martyrs",
            characters=[("殉", "순", "to die for a cause"),
                        ("國", "국", "country — as in 국가, 국권"),
                        ("先", "선", "earlier, ancestor — as in 선조, 선배"),
                        ("烈", "렬", "ardent, heroic — as in 치열, 열사")],
            notes=["Those who died for the country before liberation; the "
                   "book glosses it 나라를 위해 목숨을 바친 분."],
        ),
        "관공서": dict(hanja="官公署", meaning="a government office"),
        "남침": dict(
            hanja="南侵", meaning="an invasion of the south",
            characters=[("南", "남", "south — as in 남한, 남북"),
                        ("侵", "침", "to invade — as in 침략, 침해")],
        ),
        "공산군": dict(
            hanja="共産軍", meaning="the communist army",
            characters=[("共", "공", "together — as in 공동, 공공"),
                        ("産", "산", "to produce — as in 생산, 재산")],
        ),
        "반격": dict(
            hanja="反擊", meaning="a counter-attack",
            characters=[("反", "반", "opposite — as in 반대, 반면"),
                        ("擊", "격", "to strike — as in 공격, 충격")],
        ),
        "38선": dict(
            hanja="三八線", meaning="the 38th parallel",
            notes=["The line the peninsula was divided along in 1945; the "
                   "armistice line of 1953 runs near but not on it."],
        ),
        "돌파": dict(
            hanja="突破", meaning="a breakthrough",
            characters=[("突", "돌", "to dash, sudden — as in 돌발, 충돌"),
                        ("破", "파", "to break — as in 파괴, 돌파구")],
        ),
        "의의": dict(
            hanja="意義", meaning="significance",
            characters=[("意", "의", "meaning, intent — as in 의미, 의견"),
                        ("義", "의", "righteousness, meaning — as in 정의, 의무")],
        ),
        "생도": dict(
            hanja="生徒", meaning="a cadet",
            characters=[("徒", "도", "follower, disciple — as in 신도")],
        ),
        "행진": dict(
            hanja="行進", meaning="a march, a parade",
            characters=[("行", "행", "to go — as in 행사, 여행"),
                        ("進", "진", "to advance — as in 진행, 추진")],
        ),
    },

    extraNotes=[
        "The 대단원 정리 on pp. 48-49 is a mind map of eight boxes rather than "
        "a table; the boxes are set here in chapter order, which the map "
        "itself does not have.",
        "The 대단원 정리 box for chapter 4 reads 교통와 통신, where the chapter "
        "is 교통과 통신. That is the book's own slip and stands as printed.",
        "The quiz's answers and the 종합 평가's are mine, worked out from the "
        "chapters, since 정답보기 on p. 262 is not photographed. The quiz "
        "wants the three words that are symbols of Korea — 무궁화, 애국가, "
        "태극기 — and their partners spell 인천 사일로 벽화.",
        "Pages 52-53, the opener for 제2편 교육, carry the part's name and "
        "nothing else, so there is nothing to transcribe.",
    ],
)
