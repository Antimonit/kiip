# -*- coding: utf-8 -*-
"""Chapter 11 — Higher education and university entrance.

Transcribed in your Google Doc (11.html), whose text is carried in `blocks`
below as the Doc had it, checked against the photos of pp. 62-65. The Doc
stops after the 유학생 table, so 주요 내용정리 and 이야기 나누기 are transcribed from p. 65
and appended.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, LABELS,
               MARGIN, TABLE, CELL, CHART, GLOSSARY)

CHAPTER = dict(
    number=11, slug="11-higher-education",
    unit="교육", title="고등 교육과 입시", titleEn="Higher education and entrance exams",

    blocks=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("한국에서는 수능이나 중요한 시험을 보는 사람들에게 시험을 잘 보라는 의미로 보통 아래와 같은 선물을 " "건넵니다."),
        LABELS("{엿}", "{찹쌀떡}", "포크", "휴지"),
        HEADING(4, "01 각 선물의 의미는 무엇이라고 생각합니까?"),
        HEADING(4, "02 자신의 고향 나라에서는 시험을 잘 보라는 의미로 어떤 선물을 건넵니까?"),
        MARGIN("찍다", "풀다"),
        SECTION("goals", "학습목표"),
        BULLET("한국 입시 제도의 특징을 설명할 수 있다.", ordered=True),
        BULLET("한국 고등 교육 기관의 종류와 특징을 설명할 수 있다.", ordered=True),
        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"], [["기본", "교육",
              "10. 초·중등 교육", "교육 제도, 초·중등 교육 기관"]]),
        SECTION("part", "01 한국은 왜 대학 진학률이 높을까?"),
        HEADING(2, "한국의 교육열"),
        GLOSSARY(("교육열", "교육에 대한 열정이나 의지, 노력"),
              ("인재", "어떤 일을 할 수 있는 능력을 갖춘 사람"),
              ("진학률", "전체 졸업생 중 상급학교에 들어가는 학생의 비율"),
              ("사회적 지위", "개인이 사회 구조 속에서 차지하는 위치"),
              ("사교육", "공교육(학교 교육)을 보충하기 위하여 학교 교육 밖에서 하는 교육(학원, 과외 등)")),
        CHART("상급학교진학률 현황(교육통계서비스, 2020)(단위: %) — 고등학교에서 고등교육 기관으로의 진학률. "
              "초등학교에서 중학교로는 어느 해나 100.0%, 중학교에서 고등학교로는 99.6~99.7%로 거의 변하지 "
              "않는다.", "%", [["2000년", 62.0],
              ["2005년", 73.4],
              ["2010년", 75.4],
              ["2016년", 69.8],
              ["2017년", 68.9],
              ["2018년", 69.7],
              ["2019년", 70.4],
              ["2020년", 72.5]]),
        PARAGRAPH("한국은 교육열이 매우 높은 나라로 꼽히고 있다. 한국의 높은 교육열은 우수한 인재를 많이 길러내 한국 "
          "경제가 짧은 기간에 빠르게 성장하도록 하는 데에 이바지했다는 평가를 받고 있다."),
        PARAGRAPH("중학교 진학률과 고등학교 진학률은 거의 100%이며, 대학 진학률도 70%를 넘었다. 한국의 대학 "
          "진학률은 경제협력개발기구(OECD) 평균(약 40%)에 비해 훨씬 높다. 학력은 사회적 지위를 끌어올릴 "
          "수 있는 중요한 방법 중 하나로 인식되며 특히 대학을 졸업해야 취업이나 결혼 등에 유리하다고 생각하는 "
          "경향이 많다. 그래서 좋은 대학에 들어가기 위한 경쟁이 치열한데 이에 따라 입시 스트레스나 사교육비 지출 "
          "부담이 높은 편이다."),
        HEADING(2, "대학 입학 방법"),
        GLOSSARY(("학교 생활 기록부",
              "학생이 초중고 학교에서 어떻게 생활하면서 성장하고 변화했는지를 기록한 문서. 학생의 출석, 결석, 친구 "
              "관계, 봉사 활동, 성적 등이 종합적으로 기록되어 있다.", "학교 생활 기록부"),
              ("수시", "특별히 정해진 시기가 없이 상황에 따라 시기를 정함", "수시"),
              ("모집 요강", "사람 등을 뽑기 위하여 알리는 내용", "모집 요강"),
              ("재외국민", "국외에 거주하고 있으나 국적을 유지하고 있는 국민", "재외국민")),
        PARAGRAPH("대학에 진학하고자 할 때는 학교 생활 기록부를 중심으로 하는 수시 모집에 지원하거나 대학 수학 능력 "
          "시험에 응시하여 나온 결과인 수능 성적을 중심으로 하는 정시 모집에 지원할 수 있다. 대학 수학 능력 "
          "시험은 고등학교 졸업 예정자나 졸업자 및 이에 해당하는 학력을 가진 사람이면 누구나 볼 수 있고 매년 "
          "11월에 실시되며 대학 진학을 위해 치러야 하는 가장 중요한 시험이라고 할 수 있다."),
        PARAGRAPH("대학교마다 학생 선발 방법이 다르므로 학생은 각 대학에서 제시한 모집 요강을 살펴보고 지원을 해야 한다. "
          "일부 대학에서는 ‘다문화 가정 자녀’를 지원 조건으로 하여 선발하는 경우도 있으며 재외국민, 외국인, "
          "결혼 이주민인 경우에는 ‘재외국민 및 외국인 특별전형’에 응시할 수 있다."),
        SECTION("aside", "알아두면 좋아요"),
        HEADING(2, "대학생 멘토링과 이중 언어 학습 지원"),
        PARAGRAPH("각 시·도 교육청에서는 대학생과 학생을 연결하여 학생의 학교적응과 기초 학습을 지원하는 대학생 멘토링 "
          "제도를 운영하고 있다. 대학생 멘토가 멘티 학생이 재학중인 학교를 방문하여 방과 후 또는 방학 동안 "
          "학습을 도와준다. 주당 20시간(방학 중에는 주당 40시간) 정도 멘토링을 받을 수 있다. 또한 이중 "
          "언어 학습을 장려하기 위하여 다문화가족지원센터에서 이중 언어 환경 조성 프로그램 및 이중 언어 교재를 "
          "개발하여 보급하고 있으며 교육부와 각 시도 교육청에서 매년 ‘이중 언어 말하기 대회’를 개최하고 있다."),
        FIGURE("이중 언어 말하기 대회"),
        SECTION("part", "02 한국의 고등 교육 기관에는 어떤 것이 있을까?"),
        GLOSSARY(("학위",
              "어떤 부문의 학문을 전문적으로 익히고 공부하여 일정한 수준에 오른 사람에게 대학에서 주는 자격. 학사, "
              "석사, 박사가 있다."),
              ("인문학", "언어, 문학, 역사, 철학 등을 연구하는 학문"),
              ("산업체", "생산하는 업체")),
        HEADING(2, "고등 교육 기관 유형"),
        PARAGRAPH("한국의 고등 교육 기관으로는 대학교와 대학원이 있다. 대학교에서는 학사 학위를, 대학원에서는 석사 학위와 "
          "박사학위를 받을 수 있다."),
        PARAGRAPH("대학교에는 4년제 종합대학교, 교육대학교, 전문대학교, 방송통신대학교, 사이버대학교, 기술대학교 등이 "
          "있다. 4년제 종합대학교는 인문학, 사회과학, 법학, 자연과학, 공학, 의학 등 다양한 분야의 학문을 "
          "교육하고 연구하는 종합적인 고등 교육 기관이다. 교육대학교는 초등학교 교원을 양성할 목적으로 설립된 "
          "4년제 대학교이다."),
        PARAGRAPH("전문대학교는 일반적으로 2~3년제이며 제빵, 간호, 기술 등 직업과 관련된 전문 기술을 가르쳐 전문 "
          "직업인을 양성한다. 한편, 방송이나 인터넷 등을 통해 공부하는 방송통신대학교나 사이버대학교 등도 인기가 "
          "높다. 방송통신대학교는 4년제 국립대학교이고 사이버대학교는 2~4년제 사립대학교이다. 이 외에 산업체 "
          "근로자가 회사에 근무하면서 전문적인 지식·기술을 교육 받을 수 있는 기술대학교도 있다."),
        HEADING(2, "대학원"),
        GLOSSARY(("전문성", "어떤 영역에서 보통 수준 이상의 수행 능력을 보이는 것")),
        PARAGRAPH("대학교 졸업 후 전문적인 학문이나 기술을 더 연구하고 싶은 경우 대학원에 진학한다. 대학원 과정은 석사 "
          "과정과 박사 과정으로 구성된다. 각각 2~3년 정도씩 공부한 후 논문 제출 자격 종합 시험에 합격하고, "
          "논문이 통과되면 석사학위, 박사학위를 얻게 된다. 특히 박사학위를 받은 사람은 그 분야의 전문가로 " "인정받는다."),
        PARAGRAPH("기초 학문 연구와 교육을 주로 하는 일반대학원과 경영대학원·교육대학원·행정대학원·통역대학원·환경대학원 등 "
          "특정 분야의 연구와 교육을 하는 전문대학원, 직업인 또는 일반 성인의 계속 교육을 위하여 주로 야간에 "
          "수업을 진행하여 직장인의 전문성 확보를 지원하는 특수대학원이 있다."),
        PARAGRAPH("4년제 종합대학교, 교육대학교 등에는 석·박사학위를 수여하는 대학원을 두고 있다. 방송통신대학교나 "
          "사이버대학교 대학원에서도 석사학위 취득이 가능하다."),
        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "국내 대학에 재학 중인 외국인 유학생의 비율은?"),
        PARAGRAPH("최근 몇 년간 한국 내 대학의 외국인 유학생 비율은 점점 늘어나고 있는 추세이다. 한국교육개발원이 "
          "제공하는 교육통계서비스에 의하면 한국에 체류하는 외국인 유학생 숫자는 15만 명을 훌쩍 넘어섰다(2020 "
          "기준). 단기 어학연수나 교환 학생이 아니라 정규 학위 과정에 등록한 학생도 8만 명 이상이다. 유학생의 "
          "출신 국가를 살펴보면 중국, 베트남, 몽골, 우즈베키스탄, 일본, 미국 순으로 많다. 이에 따라 외국인 "
          "유학생을 위한 숙소와 학비 지원, 각종 문화 행사 지원 등과 같은 정책도 실시되고 있다."),
        TABLE(["구분", "1995년", "2005년", "2010년", "2015년", "2020년"], [["유학생수",
              "1,983", "22,526", "83,843", "91,332", "153,695"]]),
        FIGURE("외국인 유학생 증가현황 연도별 외국인 유학생 수(교육통계서비스, 2020)"),
    ],
    annotations={
        "학교 생활 기록부": dict(
            meaning="school life record",
            notes=["a document recording how a student lived, grew, and "
                "changed while at elementary/middle/high school; "
                "comprehensively records attendance, absences, friendships, "
                "volunteer activities, grades, etc."],
        ),
        "수시": dict(
            meaning="rolling/as-needed basis",
            notes=["隨 (to follow/accord with)", "時 (time)",
                "deciding the timing according to circumstances, without a "
                "specially fixed period — e.g. 수시 모집 = \"rolling "
                "admissions\" (as opposed to 정시, fixed-schedule admissions)"],
        ),
        "모집 요강": dict(
            meaning="recruitment guidelines",
            notes=["募集 (recruitment)", "要綱 (outline/guidelines)",
                "content announced in order to select people (e.g. "
                "university admissions guidelines)"],
        ),
        "재외국민": dict(
            meaning="overseas citizen",
            notes=["在外 (residing abroad)", "國民 (citizens)",
                "a citizen who resides outside the country but retains "
                "their nationality"],
        ),
    },
    headwords={"꼽히고": "꼽히다", "길러내": "길러내다", "이바지했다는": "이바지하다",
               "끌어올릴": "끌어올리다", "치열한데": "치열하다", "응시하여": "응시하다",
               "살펴보고": "살펴보다", "양성한다": "양성하다", "수여하는": "수여하다",
               "넘어섰다": "넘어서다"},
    append=[
        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 한국은 왜 대학 진학률이 높을까?"),
        BULLET("한국에서는 (        )이 사회적 지위를 끌어올릴 수 있는 중요한 방법의 하나로 "
          "인식되고 있다. 특히 대학을 졸업해야 취업이나 결혼 등에 유리하다고 생각하는 경향이 "
          "많다."),
        BULLET("좋은 대학에 진학하기 위한 (        )이 치열하여 입시 스트레스나 사교육비 지출 "
          "부담이 높은 편이다."),
        BULLET("대학에 진학하고자 할 때는 (        )모집이나 (        )모집에 지원한다."),
        HEADING(3, "02 한국의 고등 교육 기관에는 어떤 것이 있을까?"),
        BULLET("한국의 고등 교육 기관으로는 (        )와 (        )이 있다. 대학교에서는 "
          "(        )학위를, 대학원에서는 석사학위와 (        )학위를 받을 수 있다."),
        BULLET("최근에는 학교에 출석하지 않고 방송이나 (        ) 등을 통해 공부하는 "
          "방송통신대학교나 (        ) 대학교에 대한 인기가 높다."),
        BULLET("대학교에서 배운 지식을 토대로 전문적인 학문이나 기술을 더 연구하고 싶은 경우 "
          "(        )에 진학한다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "한국 수능 날의 풍경", translation=
          "The scene on Korea’s university entrance exam day" "\n\n"
          "The foreign press reported with interest on the scene of "
          "government, business and citizens joining forces on the day of "
          "the College Scholastic Ability Test to give students a quiet "
          "environment and every convenience. Britain’s Telegraph reported "
          "that “so that students do not meet traffic jams on their way to "
          "the exam halls, most staff at government bodies and large "
          "companies start work an hour later than usual, and the Ministry "
          "of National Defence makes sure there are no air force flights or "
          "large-scale army artillery drills during the exam”, and that “the "
          "Ministry of Land, Infrastructure and Transport even bans aircraft "
          "taking off and landing at airports in Korea for the 40 minutes in "
          "which students sit the English listening test.” America’s ABC "
          "News also described the students’ own particular culture, saying "
          "that on the morning of the exam “first- and second-year high "
          "school students hand out warm coffee and snacks in front of the "
          "exam halls and cheer their seniors on.” It went on to say that "
          "“the churches and temples are full of parents praying for their "
          "children to do well”, and published a photograph of Jogyesa "
          "temple."),
        PARAGRAPH("해외 언론들은 대학수학능력시험 날 학생들에게 조용한 환경과 편의 제공을 위해 "
          "정부·기업·시민들이 힘을 모아 애쓰는 풍경을 흥미롭게 보도했다. 영국의 텔레그래프는 "
          "“학생들이 시험장으로 향할 때 {교통 체증}을 겪지 않도록 정부기관과 대기업의 직원들은 "
          "대부분 평소보다 한 시간 늦게 출근하고, {국방부}는 시험 중 공군 비행이나 육군의 "
          "대규모 {포격} 훈련이 없도록 확인한다”며 “{국토교통부}는 학생들이 영어 듣기 시험을 "
          "치르는 40분 간 한국 내 공항에서 항공기의 {이착륙}을 금지하기도 한다.”고 보도했다. "
          "미국의 ABC 뉴스도 수능 날 아침 “고등학교 1, 2학년 학생들은 시험장 앞에서 따뜻한 "
          "커피와 과자를 나눠주고, {선배}들을 {응원}한다.”며 학생들만의 독특한 문화를 "
          "소개했다. 이어 “교회와 절은 자식들이 시험을 잘 치르기를 {기도}하는 부모들로 "
          "가득하다.”며 {조계사}의 모습을 담은 사진을 게재했다."),
        FIGURE("시험에 지각한 수험생을 수송하고 안내하는 경찰 (사진 출처: 〈연합뉴스〉)"),
        SOURCE("[출처] 뉴시스(2018. 11. 01)"),
        PARAGRAPH("★ 자신의 고향 나라와 한국의 교육열, 입시 문화를 비교하여 이야기해 봅시다.",
          "Compare the zeal for education and the entrance-exam culture of "
          "your home country with Korea’s and talk about them."),
    ],

    english={
        "한국의 교육열": dict(
            title="Korea's zeal for education",
            paragraphs=[
                "Korea is reckoned a country with a very high zeal for "
                "education. That zeal is credited with raising a great many "
                "able people, and so with helping the Korean economy grow "
                "quickly over a short period.",

                "The rate going on to middle school and the rate going on to "
                "high school are both close to 100%, and the rate going on to "
                "university has passed 70%. Korea's rate of university entry "
                "is far above the OECD average of about 40%. Educational "
                "attainment is seen as one of the important ways of raising "
                "one's social standing, and there is a widespread feeling "
                "that a university degree in particular puts one at an "
                "advantage in finding work, in marrying and so on. "
                "Competition to get into a good university is therefore "
                "fierce, and with it the strain of the entrance exams and the "
                "burden of spending on private tuition run high.",
            ],
        ),
        "대학 입학 방법": dict(
            title="How university admission works",
            paragraphs=[
                "Someone wanting to go on to university can apply either "
                "through the rolling admissions round, which turns on the "
                "school life record, or through the fixed admissions round, "
                "which turns on the 수능 score — the result of sitting the "
                "College Scholastic Ability Test. The test may be taken by "
                "anyone due to graduate from high school, anyone who has "
                "graduated, and anyone holding equivalent attainment; it is "
                "held every November, and it is the single most important "
                "examination to be sat on the way to university.",

                "Because each university selects its students differently, a "
                "student has to read the admissions guidelines that each one "
                "publishes before applying. Some universities select on the "
                "condition that the applicant is a child of a multicultural "
                "family, and an overseas citizen, a foreign national or a "
                "marriage migrant may sit the special admission for overseas "
                "citizens and foreign nationals.",
            ],
        ),
        "고등 교육 기관 유형": dict(
            title="Kinds of higher-education institution",
            paragraphs=[
                "Korea's higher-education institutions are the university and "
                "the graduate school. A university confers the bachelor's "
                "degree; a graduate school confers the master's and the "
                "doctorate.",

                "Universities include the four-year comprehensive university, "
                "the university of education, the junior college, the "
                "broadcast and correspondence university, the cyber "
                "university and the technical university. The four-year "
                "comprehensive university is a general institution that "
                "teaches and researches across many fields — the humanities, "
                "social science, law, natural science, engineering, medicine "
                "and others. The university of education is a four-year "
                "university founded to train primary school teachers.",

                "The junior college generally runs two to three years, and "
                "trains skilled professionals by teaching a trade — baking, "
                "nursing, engineering and the like. Meanwhile the broadcast "
                "and correspondence university and the cyber university, "
                "where the study is done over broadcast or the internet, are "
                "also popular. The broadcast and correspondence university is "
                "a four-year national university; the cyber university is a "
                "private one running two to four years. There is besides the "
                "technical university, where a worker at an industrial firm "
                "can be taught specialist knowledge and skills while staying "
                "in the job.",
            ],
        ),
        "대학원": dict(
            title="The graduate school",
            paragraphs=[
                "Someone who wants to take a subject or a skill further after "
                "graduating goes on to a graduate school. The graduate course "
                "is made up of the master's course and the doctoral course. "
                "After two to three years of study on each, the student "
                "passes a comprehensive examination qualifying them to submit "
                "a thesis, and on the thesis passing receives the master's or "
                "the doctoral degree. A holder of a doctorate in particular "
                "is recognised as an expert in the field.",

                "There is the general graduate school, which mostly research "
                "and teaches the basic disciplines; the professional graduate "
                "school, which researches and teaches one field — business, "
                "education, public administration, interpreting, the "
                "environment and so on; and the special graduate school, "
                "which teaches mainly in the evening, for the continuing "
                "education of working people and other adults, and supports "
                "them in securing professional expertise.",

                "Four-year comprehensive universities, universities of "
                "education and the like hold graduate schools conferring "
                "master's and doctoral degrees. A master's degree can also be "
                "taken at the graduate school of a broadcast and "
                "correspondence university or a cyber university.",
            ],
        ),
    },

    extraAnnotations={
        "엿": dict(
            meaning="yeot, a hard grain toffee",
            notes=["Given before an exam because it sticks: 붙다 means both "
                   "“to stick” and “to pass an exam”. 찹쌀떡 is given for the "
                   "same reason."],
        ),
        "찹쌀떡": dict(
            meaning="a glutinous rice cake",
            notes=["Sticky, so it carries the same wish as 엿 — that the "
                   "result should stick."],
        ),
        "찍다": dict(
            meaning="to spear, to stab — and so, to guess an answer",
            notes=["The joke behind the fork: 찍다 is what you do with a fork, "
                   "and it is also what you do when you pick an answer on a "
                   "multiple-choice paper without knowing it."],
        ),
        "풀다": dict(
            meaning="to unroll, to loosen — and so, to solve",
            notes=["The joke behind the box of tissues: you 풀다 a roll of "
                   "paper, and you 풀다 a problem."],
        ),
        "교육열": dict(
            hanja="敎育熱", meaning="zeal for education",
            characters=[("敎", "교", "to teach — as in 교육, 교사 “teacher”"),
                        ("育", "육", "to raise — as in 보육 “childcare”, 양육"),
                        ("熱", "열", "heat, fever — as in 열정 “passion”, 발열")],
            notes=["Literally the “education fever”. The word is used of the "
                   "country as a whole, not of one keen parent."],
        ),
        "인재": dict(
            hanja="人材", meaning="a capable person, talent",
            characters=[("人", "인", "person — as in 인구 “population”, 개인"),
                        ("材", "재", "material, timber — as in 재료 “material”")],
            notes=["The same 材 as in 재료: a person thought of as the stuff a "
                   "country is built from."],
        ),
        "진학률": dict(
            hanja="進學率", meaning="the rate of going on to the next school",
            characters=[("進", "진", "to advance — as in 진행 “progress”, 진로"),
                        ("學", "학", "to learn — as in 학교, 학생"),
                        ("率", "률", "rate — as in 비율 “ratio”, 출산율")],
        ),
        "사회적 지위": dict(
            hanja="社會的地位", meaning="social standing",
            characters=[("地", "지", "ground, place — as in 지역 “region”"),
                        ("位", "위", "position, rank — as in 순위 “ranking”")],
        ),
        "사교육": dict(
            hanja="私敎育", meaning="private education",
            characters=[("私", "사", "private, personal — as in 사립 “private "
                                    "(school)”, 사생활 “private life”")],
            notes=["The opposite of 공교육(公敎育), schooling by the state. In "
                   "practice it means 학원 and 과외 — the cram school and the "
                   "private tutor."],
        ),
        "학력": dict(
            hanja="學歷", meaning="educational attainment",
            characters=[("歷", "력", "to pass through, history — as in 역사, "
                                    "이력서 “résumé”")],
            notes=["The record of how far one has been educated. Not to be "
                   "confused with 학력(學力), ability gained by study."],
        ),
        "수능": dict(
            hanja="修能", meaning="the college entrance exam",
            notes=["Short for 대학수학능력시험, the College Scholastic Ability "
                   "Test. Sat on one day in November, and the day the rest of "
                   "the country arranges itself around."],
        ),
        "정시": dict(
            hanja="定時", meaning="the fixed admissions round",
            characters=[("定", "정", "to fix, settle — as in 결정 “decision”"),
                        ("時", "시", "time — as in 시간, 시기 “period”")],
            notes=["The round that runs to a set timetable and turns on the "
                   "수능 score. Its opposite is 수시."],
        ),
        "특별전형": dict(
            hanja="特別銓衡", meaning="special admission track",
            notes=["A selection route outside the ordinary one, for "
                   "applicants in a named situation — here overseas citizens "
                   "and foreign nationals."],
        ),
        "학위": dict(
            hanja="學位", meaning="an academic degree",
            characters=[("學", "학", "to learn — as in 학교, 학생"),
                        ("位", "위", "position, rank — the same 位 as in "
                                    "사회적 지위")],
        ),
        "학사": dict(hanja="學士", meaning="a bachelor's degree"),
        "석사": dict(hanja="碩士", meaning="a master's degree"),
        "박사": dict(
            hanja="博士", meaning="a doctorate",
            characters=[("博", "박", "wide, broad — as in 박물관 “museum”")],
        ),
        "인문학": dict(
            hanja="人文學", meaning="the humanities",
            characters=[("文", "문", "writing, culture — as in 문화, 문학")],
        ),
        "산업체": dict(
            hanja="産業體", meaning="an industrial firm",
            characters=[("産", "산", "to produce — as in 생산 “production”, 산업"),
                        ("體", "체", "body, entity — as in 단체 “organisation”")],
        ),
        "전문성": dict(
            hanja="專門性", meaning="professional expertise",
            characters=[("專", "전", "sole, exclusive — as in 전문 “speciality”"),
                        ("門", "문", "gate — as in 대문 “front gate”"),
                        ("性", "성", "nature, -ness — as in 가능성 “possibility”")],
        ),
        "양성": dict(
            hanja="養成", meaning="to train up, to bring on",
            characters=[("養", "양", "to nurture — as in 양육 “bringing up”"),
                        ("成", "성", "to accomplish — as in 성장 “growth”")],
        ),
        "논문": dict(
            hanja="論文", meaning="a thesis, a paper",
            characters=[("論", "론", "to argue — as in 토론 “debate”, 이론"),
                        ("文", "문", "writing — as in 문장 “sentence”")],
        ),
        "수여": dict(
            hanja="授與", meaning="to confer, to award",
            characters=[("授", "수", "to give, to teach — as in 교수 “professor”"),
                        ("與", "여", "to give — as in 참여 “participation”")],
        ),
        "유학생": dict(
            hanja="留學生", meaning="a student studying abroad",
            characters=[("留", "류", "to stay — as in 체류 “stay, sojourn”"),
                        ("學", "학", "to learn"),
                        ("生", "생", "person, life — as in 학생, 신생아")],
        ),
        "어학연수": dict(
            hanja="語學硏修", meaning="a language course abroad",
            characters=[("語", "어", "word, language — as in 한국어, 언어"),
                        ("硏", "연", "to study, grind — as in 연구 “research”"),
                        ("修", "수", "to cultivate, repair — as in 수업 “lesson”")],
        ),
        "멘토링": dict(
            meaning="mentoring",
            notes=["From the English. The mentor is 멘토 and the person "
                   "mentored is 멘티."],
        ),
        "이중 언어": dict(
            hanja="二重言語", meaning="bilingual, two languages",
            characters=[("二", "이", "two"),
                        ("重", "중", "heavy, layered — as in 중요 “important”, "
                                    "이중 “double”")],
        ),
        "교통 체증": dict(
            hanja="交通滯症", meaning="a traffic jam",
            characters=[("滯", "체", "to be blocked, stagnant — as in 정체"),
                        ("症", "증", "a symptom — as in 증상 “symptom”")],
            notes=["Literally a “congestion symptom”, as though the roads "
                   "were suffering an illness."],
        ),
        "국방부": dict(
            hanja="國防部", meaning="the Ministry of National Defense",
            characters=[("防", "방", "to defend — as in 예방 “prevention”, 방지")],
        ),
        "국토교통부": dict(
            hanja="國土交通部", meaning="the Ministry of Land, Infrastructure and Transport",
            notes=["The same 국토 as in chapter 6 — the country's land."],
        ),
        "포격": dict(
            hanja="砲擊", meaning="artillery fire",
            characters=[("砲", "포", "cannon"),
                        ("擊", "격", "to strike — as in 공격 “attack”")],
        ),
        "이착륙": dict(
            hanja="離着陸", meaning="take-off and landing",
            characters=[("離", "이", "to leave, separate — as in 이혼 “divorce”"),
                        ("着", "착", "to arrive, attach — as in 도착 “arrival”"),
                        ("陸", "륙", "land — as in 대륙 “continent”")],
            notes=["A compound of 이륙 “take-off” and 착륙 “landing”, with the "
                   "shared 륙 written once."],
        ),
        "선배": dict(
            hanja="先輩", meaning="a senior, someone further along",
            characters=[("先", "선", "earlier — as in 선생 “teacher”, 우선"),
                        ("輩", "배", "a set, a generation")],
            notes=["Here the year above at school. The counterpart is 후배."],
        ),
        "응원": dict(
            hanja="應援", meaning="to cheer on, to support",
            characters=[("應", "응", "to respond — as in 응급 “emergency”, 응시"),
                        ("援", "원", "to help — as in 지원 “support”")],
        ),
        "기도": dict(
            hanja="祈禱", meaning="prayer",
            characters=[("祈", "기", "to pray"), ("禱", "도", "to pray")],
        ),
        "조계사": dict(
            hanja="曹溪寺", meaning="Jogyesa, a Buddhist temple in Seoul",
            notes=["The head temple of the Jogye Order, the largest school of "
                   "Korean Buddhism. 사(寺) is the ending on temple names."],
        ),
    },
)
