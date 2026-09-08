# -*- coding: utf-8 -*-
"""Chapter 10 — Primary and secondary education.

No Google Doc. Transcribed from the photos of pages 58-61, so the Korean here
is my reading of the page rather than yours, and any error in it is mine.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, MARGIN, FIGURE, TABLE,
               CELL, GLOSSARY)

CHAPTER = dict(
    number=10, slug="10-school-education",
    unit="교육", title="초·중등 교육", titleEn="Primary and secondary education",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        MARGIN("{초등학교} 6년", "{중학교} + {고등학교} 3+3년", "고등 — 대학교 + 대학원"),
        PARAGRAPH("다음은 한국에서 볼 수 있는 초등학교와 중학교의 모습입니다."),
        FIGURE("초등학교 교실의 모습"),
        HEADING(4, "01 각 교실의 모습에서 다른 점은 무엇입니까?"),
        FIGURE("중학교 교실의 모습"),
        HEADING(4, "02 한국 학교의 모습과 본인 출신국의 학교 모습은 어떤 점이 다릅니까?"),

        SECTION("goals", "학습목표"),
        BULLET("한국 교육 제도의 특징을 설명할 수 있다.", ordered=True),
        BULLET("한국 초·중등 교육 기관의 종류와 특징을 설명할 수 있다.", ordered=True),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", 2), "제목", "관련 내용"],
              [["기본", "교육", "11. 고등 교육과 입시",
                "한국의 교육열, 고등 교육 기관, 입학 방법, 고등 교육 기관 유형"]]),

        SECTION("part", "01 한국 교육 제도의 특징은 무엇일까?"),
        HEADING(2, "한국의 교육 제도와 주요 교육 일정(학사 일정)"),
        GLOSSARY(("무상", "비용이나 대가가 없음", "무상"),
              ("의무 교육", "개인이 국가나 사회의 구성원으로서 의무적으로 받아야 하는 교육, "
               "이와 동시에 국가가 그 구성원에게 의무적으로 제공해야 하는 교육. 한국은 의무 "
               "교육 기간이 9년이다(초등학교 6년 + 중학교 3년).", "의무 교육"),
              ("법인", "법적으로 권리와 의무를 가지는 조직", "법인")),
        PARAGRAPH("한국의 초·중등 교육은 초등학교 6년, 중학교 3년, 고등학교 3년으로 구성되며 교육은 "
          "{무상}으로 제공된다. 이 중, 초등학교 6년과 중학교 3년은 {의무 교육} 기간이다. 교육 "
          "기관은 설립과 운영 주체에 따라 국립(국가), 공립(지방 자치 단체), 사립 학교({법인}이나 "
          "개인)가 있다. 집에서 가까운 학교에 {배정}하는 공립과 달리 국립 또는 사립 교육 기관은 "
          "학생을 특정 기준을 두어 별도로 선발하거나 {추첨}을 통해 선발한다. 교육 활동은 1년을 "
          "1학기와 2학기로 나누어 운영하는데 1학기는 3월초, 2학기는 8월말~9월초에 시작한다."),
        TABLE(["학기", "행사명", "내용", "시기"],
              [[CELL("1학기", down=5), "입학식(시업식)", "새 학년 새 학기가 시작되는 날",
                "3월 첫 평일"],
               ["학교 교육 설명회", "학부모에게 학교 교육 과정을 소개하는 날", "3월"],
               ["현장 체험 학습", "교실에서 벗어나 야외로 나가 수업하는 날", "4월, 10월 등"],
               ["운동회(체육 대회)", "전교생 또는 학년별 체육 대회를 하는 날",
                "5월 (또는 10월)"],
               ["공개 수업의 날", "학교 수업을 공개하는 날", "학교마다 다름"],
               [CELL("2학기", down=5), "여름 방학식", "1학기를 마치고 방학을 맞이하는 날",
                "7월 말"],
               ["여름 개학식", "2학기를 시작하는 날", "8월 말, 9월초"],
               ["학습 발표회", "1년 동안 학습한 내용을 발표하는 날", "11월"],
               ["겨울 방학식", "겨울 방학을 맞이하는 날", "12월말, 1월초"],
               ["종업식(졸업식)", "학년을 마치는 날", "1월~2월"]]),

        HEADING(2, "학교 교육 활동"),
        GLOSSARY(("차시", "학교 수업의 기본 단위", "차시"),
              ("탄력적", "고정되어 있지 않고 유연하게 변할 수 있음", "탄력적"),
              ("교외", "학교 밖", "교외"),
              ("정규", "정식으로 된 규정", "정규"),
              ("방과", "그날의 수업을 마침", "방과")),
        PARAGRAPH("초·중등 교육과정은 크게 {교과}(국어, 수학, 사회 등)와 {창의적} 체험 활동(자율, "
          "동아리, 봉사, {진로})으로 구성된다. 초등학교는 1개 {차시} 수업이 40분, 중학교는 "
          "45분, 고등학교는 50분을 {원칙}으로 하되 상황에 따라 {탄력적}으로 운영할 수 있다. "
          "학교 교육은 교실이나 운동장, 도서관, {강당} 등에서 실시되는 수업뿐 아니라 현장 체험 "
          "학습(직접 {관찰}, {답사}, {견학} 등)으로도 이루어진다. 현장 체험 학습은 각 가정별로도 "
          "실시할 수 있으므로 미리 {교외} 체험 학습을 신청하면 된다. {정규} 교육 과정 이외에 "
          "학생들의 {소질} 및 {적성}을 개발하면서 {사교육비} 부담도 줄일 수 있도록 다양한 "
          "‘{방과} 후 학교 프로그램’을 운영하고 있다."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "외국인 자녀의 학교 입학은 어떻게?"),
        PARAGRAPH("Q 누구나 학교에 다닐 수 있나요? — 「{헌법}」과 「UN 아동의 권리에 관한 {협약}」에 "
          "따라 아동·청소년의 의무 교육을 보장하고 있기 때문에 체류 {신분}에 관계없이 외국인 "
          "학생, {중도입국} 학생도 학교 교육을 받을 수 있다."),
        PARAGRAPH("Q 학교에 입학하려면 어떤 서류를 챙겨가야 하나요? — ① 출입국에 관한 사실이나 외국인 "
          "등록을 증명할 수 있는 서류(없으면 거주 사실을 확인할 수 있는 서류) ② {학력}을 증명할 "
          "수 있는 서류(졸업 증명서 또는 재학 사실 증명 서류, 성적 증명서 등) 등"),

        SECTION("part", "02 한국의 초·중등 교육 기관에는 어떤 것이 있을까?"),
        HEADING(2, "초등학교 입학과 교육 내용"),
        GLOSSARY(("취학 통지서", "어린이가 학교에 들어가는 것을 허락하거나 알리는 문서",
               "취학 통지서"),
              ("예비 소집일", "입학 등록을 하는 날로 취학 통지서를 챙겨가야 한다.",
               "예비 소집일")),
        PARAGRAPH("초등학교는 만 6세부터 다닐 수 있다. {취학 통지서}는 아동이 입학하기 전 해의 12월에 "
          "지역의 행정복지센터에서 집으로 보내준다. 여기에는 아동이 입학하게 될 집 근처의 학교 "
          "이름과 주소, {예비 소집일}, 입학식에 대한 정보가 담겨있다. 아동의 성장 상태, 학업 "
          "능력 등 {개인차}에 따라 1년 먼저 입학하거나 1년 {연기}할 수도 있다."),
        PARAGRAPH("초등학교에서 배우는 내용은 일상생활과 기초적인 학습에 필요한 읽기, 쓰기, {셈하기} "
          "능력 기르기, 기본적인 지식 배우기, 올바른 생활 습관 갖기 등에 {초점}을 둔다. "
          "학교에서는 학부모에게 각종 교육 정보를 가정 {통신문}이나 {알림장}을 통해 안내한다. "
          "학기가 종료되는 시점에는 학생들의 출석과 {결석} 상황, 교과 학습 발달 상황, 행동 특성 "
          "및 종합 의견 등을 기록하여 학부모에게 {생활 통지표}를 배부한다."),
        FIGURE("초등학교 입학식"),

        HEADING(2, "중·고등학교 입학과 교육 내용"),
        GLOSSARY(("배정", "나누어 정함", "배정"),
              ("검정고시", "어떤 자격에 필요한 지식, 학력, 기술 등이 있는지 검사하기 위해 "
               "실시하는 시험", "검정고시"),
              ("함양", "능력이나 품성 등을 길러 갖춤", "함양")),
        MARGIN("상업 → 은행 취업", "농업"),
        PARAGRAPH("중학교는 크게 일반 중학교와 {특성화} 중학교(체육, 예술, 국제중)로 구분된다. 일반 "
          "중학교에 {진학}하는 경우 보통 집에서 가까운 학교에 {배정}되며 특정 분야의 재능이 있는 "
          "학생을 교육하는 특성화 중학교는 별도의 과정을 거쳐 선발한다. 중학교 교육 과정은 "
          "중학생의 학습과 일상생활에 필요한 기본 능력, {민주} 시민으로서 갖추어야 할 지식과 "
          "기능 등을 다룬다. 중학교 3년 과정 중 1년은 {자유 학년제}로 운영된다. 이 기간에는 "
          "중간·기말고사를 보지 않고, {토론}·{실습} 위주의 참여형 수업과 직장 체험 활동 같은 "
          "{진로 탐색} 교육을 받도록 한다."),
        PARAGRAPH("중학교를 졸업하거나 {검정고시}와 같이 중학교 학력을 인정받는 시험에 합격한 사람은 "
          "고등학교에 입학할 수 있다. 고등학교는 크게 일반 고등학교와 {특수 목적 고등학교}, "
          "{특성화 고등학교}, {자율형 고등학교} 등으로 구분된다. 고등학교 교육 과정은 중학교 "
          "교육의 성과를 바탕으로 학생의 적성과 소질에 맞는 진로 개척 능력과 세계 시민으로서의 "
          "{자질}을 {함양}하는 데 중점을 둔다."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "온라인으로 만나는 학교, 온라인 개학"),
        PARAGRAPH("2020년 코로나19 확산으로 인해 처음으로 시행된 교육 정책으로, 교사와 학생이 대면하지 "
          "않고 {원격}으로 수업을 진행하는 것이다. ▶ 교사와 학생이 화상 연결로 수업하는 ‘실시간 "
          "{쌍방향}형’ ▶ EBS 콘텐츠나 교사가 녹화한 강의를 보는 ‘콘텐츠 활용형’ ▶ 독후감 등 "
          "과제를 내주는 ‘과제 수행형’ 3개 유형으로 운영된다. 장애학생들은 장애유형 정도를 "
          "고려하여 온라인 수업(점역파일, 자막지원, 보조공학기기 지원 등)과 1:1 방문교육 등 "
          "{맞춤}형으로 실시한다. 다문화 학생들에게는 한국어와 한국문화를 배울 수 있는 프로그램과 "
          "다문화 콘텐츠를 제공하고 이를 다국어 가정통신문으로 안내한다. 저소득층 학생들에게는 "
          "스마트기기 {대여}, 통신비를 지원하는 등 모든 학생들이 온라인 개학에 참여할 수 있도록 "
          "정책을 시행하였다."),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 한국 교육 제도의 특징은 무엇일까?"),
        BULLET("한국의 초·중등 교육 과정은 초등학교 (    )년, 중학교 (    )년, 고등학교 (    )년으로 "
          "구성된다."),
        BULLET("초등학교 6년과 중학교 3년은 (        ) 기간으로 무상 교육이 제공된다."),
        BULLET("각 학년은 1학기와 2학기로 구성되며, 1학기 시작은 매년 (        )월이다."),
        BULLET("교육 기관은 국가에서 설립하여 운영하는 (        ) 학교, 지방자치단체에서 설립하여 "
          "운영하는 (        ) 학교, 개인이나 법인이 설립하여 운영하는 사립 학교로 구분된다."),
        BULLET("교육 과정은 교과와 (        )으로 구성되며 교육은 교실에서 뿐만 아니라 직접 체험하며 "
          "효과적으로 학습할 수 있도록 (        )으로도 이루어진다."),
        BULLET("(        ) 프로그램은 정규 교육 과정 이외에 학교에서 다양한 형태의 프로그램을 "
          "운영하는 것이다."),
        HEADING(3, "02 한국의 초·중등 교육 기관에는 어떤 것이 있을까?"),
        BULLET("초등학교 입학은 만 (    )세부터 가능하고, 입학 시기를 조정하고자 할 경우 "
          "행정복지센터에 미리 신청 서류를 제출해야 한다."),
        BULLET("중학교 3년 과정 중 1년은 중간·기말고사를 보지 않고, 토론·실습 위주의 참여형 수업과 "
          "직장 체험 활동 같은 진로 탐색 교육을 받도록 하는 (        )로 운영된다."),
        BULLET("고등학교는 일반 고등학교, 특수 목적 고등학교, 특성화 고등학교, 자율형 고등학교 등으로 "
          "구분된다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "한국에서도 홈스쿨링을?", translation=
          "Home schooling in Korea too?" "\n\n"
          "Home schooling means education at home, through one’s parents or "
          "others, instead of going to school. Some parents take it up "
          "because they see school education as ill-suited to an individual "
          "child’s character and abilities, and lately the number of Korean "
          "families doing so has been growing. It is done with the good "
          "intention of educating a child better, but in law it is a breach "
          "of compulsory education, and a fine of up to a million won may "
          "have to be paid. Experts say that while home schooling can be a "
          "good way of teaching a lesson suited to each child, it needs "
          "safeguards, since on the other hand the child may have some "
          "difficulty forming social relationships, or may be neglected."),
        PARAGRAPH("{홈스쿨링}은 학교에 가는 대신에 집에서 부모 등을 통해 교육을 받는 {재택} 교육을 "
          "말한다. 일부 부모들은 학교 교육이 개별 아이의 특성과 능력에 맞추기 어렵다고 보고 "
          "홈스쿨링을 실시하는데 최근 한국에도 홈스쿨링을 실시하는 가정이 늘어나고 있다. 자녀 "
          "교육을 더 잘 하고자 하는 좋은 {의도}에서 실시하는 것이기는 하지만 법적으로는 의무 "
          "교육을 {위반}한 것이라서 100만 원 이하의 {과태료}를 낼 수도 있다. 전문가들은 "
          "홈스쿨링이 각 아이에게 맞는 수업을 할 수 있는 좋은 방법이 될 수 있기는 하지만, 다른 "
          "{한편}으로 사회적 관계 {형성}에 다소 어려움을 겪거나 아동이 {방치}될 수도 있다는 "
          "점에서 {보완}이 필요하다고 말한다."),
        PARAGRAPH("★ 홈스쿨링에 대한 본인의 생각(찬성, 반대, 유의점 등)을 이야기해 봅시다.",
          "Talk about what you yourself think of home schooling — for, "
          "against, what to watch out for, and so on."),
    ],

    english={
        "한국의 교육 제도와 주요 교육 일정(학사 일정)": dict(
            title="The education system and the school year",
            paragraphs=[
                "Primary and secondary education in Korea consists of six years of "
                "primary school, three of middle school and three of high school, and "
                "the education is provided free of charge. Of these, the six years of "
                "primary and the three of middle school are the period of compulsory "
                "education. Educational institutions are national (the state), public "
                "(a local authority) or private (a legal person or an individual), "
                "according to who founds and runs them. Unlike public schools, which "
                "assign a child to the school nearest home, national and private "
                "institutions select their pupils separately against particular "
                "criteria, or by lot. The year of teaching is run as two semesters, "
                "the first beginning in early March and the second at the end of "
                "August or the beginning of September.",
            ],
        ),
        "학교 교육 활동": dict(
            title="What school teaching consists of",
            paragraphs=[
                "The primary and secondary curriculum divides broadly into subjects — "
                "Korean, mathematics, social studies and so on — and creative "
                "experiential activities: self-directed, club, voluntary and "
                "career-related. A single period is 40 minutes at primary school, 45 "
                "at middle school and 50 at high school as a rule, though this may be "
                "run flexibly as circumstances require. School education is not only "
                "lessons held in the classroom, the playground, the library or the "
                "hall, but also field study — direct observation, site visits, "
                "study trips. Field study may also be undertaken by an individual "
                "family, in which case one applies in advance for off-site study. "
                "Besides the regular curriculum, a range of after-school programmes "
                "are run, which develop pupils' aptitudes and talents while also "
                "lessening the burden of private tuition fees.",
            ],
        ),
        "초등학교 입학과 교육 내용": dict(
            title="Entering primary school, and what is taught there",
            paragraphs=[
                "Primary school may be attended from the age of six. The admission "
                "notice is sent to the home by the local administrative welfare centre "
                "in the December before the child enters. It carries the name and "
                "address of the school near the home that the child will attend, the "
                "date of the preliminary call, and information about the entrance "
                "ceremony. According to individual differences — the child's growth, "
                "academic ability and so on — entry may be brought forward or deferred "
                "by a year.",

                "What is taught at primary school centres on what daily life and basic "
                "learning require: building the ability to read, write and count, "
                "learning basic knowledge, acquiring sound habits of living. The school "
                "informs parents of various educational matters through the home "
                "newsletter or the communication book. At the close of a semester the "
                "school records pupils' attendance and absence, their progress in each "
                "subject, and notes on their conduct and a general comment, and "
                "distributes a report card to the parents.",
            ],
        ),
        "중·고등학교 입학과 교육 내용": dict(
            title="Entering middle and high school, and what is taught there",
            paragraphs=[
                "Middle schools divide broadly into ordinary ones and specialised ones "
                "— physical education, the arts, international studies. A child going "
                "on to an ordinary middle school is usually assigned to the school near "
                "home, while a specialised middle school, which educates pupils with a "
                "talent in a particular field, selects them through a separate process. "
                "The middle school curriculum covers the basic abilities that a middle "
                "school pupil's study and daily life require, and the knowledge and "
                "skills a democratic citizen should have. One of the three years is run "
                "as the free-year system. During it there are no mid-term or final "
                "examinations; instead pupils take participatory lessons centred on "
                "discussion and practical work, and career exploration such as "
                "workplace experience.",

                "Anyone who has finished middle school, or has passed an examination "
                "recognised as equivalent to it such as the qualification examination, "
                "may enter high school. High schools divide broadly into ordinary "
                "ones, special-purpose ones, specialised ones and autonomous ones. The "
                "high school curriculum builds on what was achieved at middle school "
                "and puts its weight on the ability to open up a career suited to the "
                "pupil's aptitude and talent, and on cultivating the qualities of a "
                "global citizen.",
            ],
        ),
    },

    extraAnnotations={
        "초등학교": dict(
            hanja="初等學校", meaning="primary school",
            characters=[("初", "초", "first, beginning — as in 초반 “early phase”, 최초"),
                        ("等", "등", "grade, rank — the same 等 as in 양성평등, 고등"),
                        ("學", "학", "to learn — the same 學 as in 학비, 학교"),
                        ("校", "교", "school — the same 校 as in 폐교, 학교")],
            notes=["Six years, from age six. Your note on the title page sets out the "
                   "whole ladder: 6 + 3 + 3, then university."],
        ),
        "중학교": dict(
            hanja="中學校", meaning="middle school",
            characters=[("中", "중", "middle — as in 중후반, 중소기업")],
            notes=["Three years, and the end of compulsory education. 중등 교육 covers "
                   "both this and high school, which is why the chapter's title pairs "
                   "초등 with 중등."],
        ),
        "고등학교": dict(
            hanja="高等學校", meaning="high school",
            characters=[("高", "고", "high — the same 高 as in 고속버스, 고령화"),
                        ("等", "등", "grade")],
            notes=["Three years, and not compulsory — though nearly everyone attends. "
                   "Note that 고등 교육 means higher education, the university stage, "
                   "not high school: 고등학교 is 중등 교육."],
        ),
        "무상": dict(
            hanja="無償", meaning="free of charge",
            characters=[("無", "무", "without — as in 무료 “free”, 무선 “wireless”"),
                        ("償", "상", "to compensate — the same 償 as in 보상, 산업재해보상")],
            notes=["Literally without recompense. 무상 교육 is education provided at no "
                   "cost, which the page distinguishes from 의무 교육, the education one "
                   "is obliged to receive — the two happen to coincide for nine years."],
        ),
        "의무 교육": dict(
            hanja="義務敎育", meaning="compulsory education",
            characters=[("義", "의", "duty — the same 義 as in 의무적, 정의"),
                        ("務", "무", "duty — the same 務 as in 공무원, 업무협약")],
            notes=["The page's gloss cuts both ways, and that is the point: the "
                   "individual must receive it and the state must provide it. Nine "
                   "years in Korea, and the reason homeschooling can be fined."],
        ),
        "법인": dict(
            hanja="法人", meaning="a legal person, a corporation",
            characters=[("法", "법", "law — the same 法 as in 법무부, 헌법"),
                        ("人", "인", "person")],
            notes=["A body the law treats as a person, able to hold rights and duties "
                   "of its own. Set against 개인 in the same sentence, as the two "
                   "kinds of founder a private school can have."],
        ),
        "배정": dict(
            hanja="配定", meaning="assignment, allocation",
            characters=[("配", "배", "to distribute — the same 配 as in 택배, 배우자"),
                        ("定", "정", "to fix — the same 定 as in 확정 일자, 지정")],
            notes=["Being allotted a place rather than choosing it: the public school "
                   "nearest home. Met in chapter 6's 계절 근로자 배정현황."],
        ),
        "추첨": dict(
            hanja="抽籤", meaning="a draw, selection by lot",
            characters=[("抽", "추", "to draw out — as in 추출"),
                        ("籤", "첨", "a lot, a slip drawn")],
            notes=["How over-subscribed national and private schools pick pupils where "
                   "no test applies."],
        ),
        "교과": dict(
            hanja="敎科", meaning="school subjects, the taught curriculum",
            characters=[("敎", "교", "to teach — the same 敎 as in 교육, 태교"),
                        ("科", "과", "branch, department — as in 학과, 내과")],
            notes=["Set against 창의적 체험 활동 as the two halves of the curriculum: "
                   "the subjects, and everything else."],
        ),
        "창의적": dict(
            hanja="創意的", meaning="creative",
            characters=[("創", "창", "to create — as in 창업 “starting a business”, 창작"),
                        ("意", "의", "intent, meaning — the same 意 as in 의도, 의미"),
                        ("的", "적", "-ic, -al")],
            notes=["The same 창 as the 창업 of chapter 3, where retirees start "
                   "businesses."],
        ),
        "진로": dict(
            hanja="進路", meaning="one's course in life, career path",
            characters=[("進", "진", "to advance — the same 進 as in 진출, 증진"),
                        ("路", "로", "road — the same 路 as in 수로, 차로")],
            notes=["Literally the road forward. 진로 탐색 is exploring it, and one of "
                   "the four creative activities."],
        ),
        "차시": dict(
            hanja="次時", meaning="a lesson period",
            characters=[("次", "차", "order, next — the same 次 as in 점차, 개인차"),
                        ("時", "시", "time — the same 時 as in 일시적, 시간")],
            notes=["The counting unit for lessons: 1차시 is one period, 40 minutes at "
                   "primary school."],
        ),
        "원칙": dict(
            hanja="原則", meaning="a principle, the rule",
            characters=[("原", "원", "origin — the same 原 as in 원전, 원리"),
                        ("則", "칙", "rule — the same 則 as in 원칙적, 규칙")],
            notes=["원칙으로 하되 is the phrase here: the rule, but with what follows "
                   "allowed. Chapter 7's 원칙적으로 works the same way."],
        ),
        "탄력적": dict(
            hanja="彈力的", meaning="flexible, elastic",
            characters=[("彈", "탄", "to spring, bounce — as in 탄력"),
                        ("力", "력", "force — as in 능력, 영향력"),
                        ("的", "적", "-ic, -al")],
            notes=["Met in chapter 3, of flexible working hours. Here it is the length "
                   "of a lesson."],
        ),
        "강당": dict(
            hanja="講堂", meaning="an assembly hall",
            characters=[("講", "강", "to lecture — as in 강의 “lecture”, 강사"),
                        ("堂", "당", "hall — as in 성당 “cathedral”, 식당")],
        ),
        "관찰": dict(
            hanja="觀察", meaning="observation",
            characters=[("觀", "관", "to look at — the same 觀 as in 관광업, 관심"),
                        ("察", "찰", "to examine — as in 경찰 “police”, 시찰")],
        ),
        "답사": dict(
            hanja="踏査", meaning="a site visit, field survey",
            characters=[("踏", "답", "to tread, step on"),
                        ("査", "사", "to investigate — as in 조사 “survey”, 검사")],
            notes=["Literally treading and surveying — going to the place and looking. "
                   "Not the 답 of 대답 “answer”, which is 答."],
        ),
        "견학": dict(
            hanja="見學", meaning="a study visit",
            characters=[("見", "견", "to see — as in 의견 “opinion”, 발견"),
                        ("學", "학", "to learn")],
            notes=["Seeing in order to learn: the school trip to a factory, a museum, "
                   "a newspaper office."],
        ),
        "교외": dict(
            hanja="校外", meaning="outside the school",
            characters=[("校", "교", "school — the same 校 as in 학교, 폐교"),
                        ("外", "외", "outside — the same 外 as in 시외버스, 재외 동포")],
            notes=["Its opposite 교내 is within the school. A homonym of 교외(郊外), the "
                   "outskirts of a city — different first character."],
        ),
        "정규": dict(
            hanja="正規", meaning="regular, formally prescribed",
            characters=[("正", "정", "correct — the same 正 as in 훈민정음, 정확"),
                        ("規", "규", "rule — the same 規 as in 규제, 원칙")],
            notes=["Met in chapter 3 as 정규 근무, the standard working hours. Here it "
                   "is the standard curriculum, against which 방과 후 sits."],
        ),
        "소질": dict(
            hanja="素質", meaning="a natural aptitude",
            characters=[("素", "소", "plain, element — as in 요소 “element”, 소재"),
                        ("質", "질", "quality — the same 質 as in 수질, 물질")],
        ),
        "적성": dict(
            hanja="適性", meaning="aptitude, fitness for something",
            characters=[("適", "적", "to suit — the same 適 as in 쾌적하다, 적합하다"),
                        ("性", "성", "nature — the same 性 as in 생산성, 양성평등")],
            notes=["Paired with 소질 throughout Korean writing on education: what one "
                   "is suited to and what one is naturally good at."],
        ),
        "사교육비": dict(
            hanja="私敎育費", meaning="the cost of private tuition",
            characters=[("私", "사", "private — the same 私 as in 사립, 사생활"),
                        ("敎", "교", "to teach"),
                        ("育", "육", "to raise"),
                        ("費", "비", "expense — the same 費 as in 보육비, 학비")],
            notes=["사교육 is everything outside the school — the 학원 above all — and "
                   "its cost is a standing subject of Korean public argument. The "
                   "after-school programmes exist partly to hold it down."],
        ),
        "방과": dict(
            hanja="放課", meaning="the end of the school day",
            characters=[("放", "방", "to release — as in 방학 “school holiday”, 개방"),
                        ("課", "과", "lesson, task — as in 과제 “assignment”, 과목")],
            notes=["Literally letting the lesson go. 방과 후 is after school, and the "
                   "same 放 gives 방학, the holiday."],
        ),
        "헌법": dict(
            hanja="憲法", meaning="the constitution",
            characters=[("憲", "헌", "constitution, law"),
                        ("法", "법", "law — the same 法 as in 법인, 법무부")],
            notes=["Met in chapter 1's 제헌절, the day the first constitution was "
                   "promulgated."],
        ),
        "협약": dict(
            hanja="協約", meaning="a convention, an agreement",
            characters=[("協", "협", "to cooperate — the same 協 as in 업무협약"),
                        ("約", "약", "to promise — the same 約 as in 계약, 약속")],
        ),
        "신분": dict(
            hanja="身分", meaning="status",
            characters=[("身", "신", "body, self — the same 身 as in 신분증, 자신"),
                        ("分", "분", "to divide, portion — the same 分 as in 분산, 부분")],
            notes=["체류 신분 is one's residence status, and the point of the box is "
                   "that schooling does not depend on it."],
        ),
        "중도입국": dict(
            hanja="中途入國", meaning="entering the country partway through childhood",
            characters=[("中", "중", "middle"),
                        ("途", "도", "way, route — as in 용도, 도중"),
                        ("入", "입", "to enter — the same 入 as in 출입국, 세입자"),
                        ("國", "국", "country")],
            notes=["중도입국 학생 is a child who arrives in Korea after starting school "
                   "elsewhere — typically the child of a marriage immigrant, brought "
                   "over later. They have a particular place in Korean education "
                   "policy, and the box says they may attend school like anyone else."],
        ),
        "학력": dict(
            hanja="學歷", meaning="educational attainment",
            characters=[("學", "학", "to learn"),
                        ("歷", "력", "to pass through, record — the same 歷 as in 경력, 역사")],
            notes=["The record of what one has completed. Worth keeping apart from "
                   "학력(學力), which is academic ability — same sound, and the page "
                   "uses both."],
        ),
        "취학 통지서": dict(
            hanja="就學通知書", meaning="the admission notice",
            characters=[("就", "취", "to take up — the same 就 as in 취업, 취직"),
                        ("學", "학", "to learn"),
                        ("通", "통", "to pass, communicate — the same 通 as in 통행, 통신"),
                        ("知", "지", "to know — the same 知 as in 친지, 지능적"),
                        ("書", "서", "document — the same 書 as in 의뢰서, 계약서")],
            notes=["취학 is entering schooling, as 취업 is entering employment — the "
                   "same 就. Sent from the 행정복지센터 the December before."],
        ),
        "예비 소집일": dict(
            hanja="豫備召集日", meaning="the preliminary call day",
            characters=[("豫", "예", "beforehand — the same 豫 as in 예방, 예방 접종"),
                        ("備", "비", "to prepare — the same 備 as in 대비, 준비"),
                        ("召", "소", "to summon"),
                        ("集", "집", "to gather — as in 집중 “concentration”, 수집")],
            notes=["The day one registers, bringing the 취학 통지서."],
        ),
        "개인차": dict(
            hanja="個人差", meaning="individual difference",
            characters=[("個", "개", "individual — as in 개인, 개별"),
                        ("人", "인", "person"),
                        ("差", "차", "difference — as in 차이 “difference”, 격차")],
            notes=["The grounds on which entry can be brought forward or held back a "
                   "year."],
        ),
        "연기": dict(
            hanja="延期", meaning="postponement",
            characters=[("延", "연", "to extend, delay — the same 延 as in 연장"),
                        ("期", "기", "period — the same 期 as in 농번기, 학기")],
            notes=["A homonym of 연기 “acting” (演技) and 연기 “smoke”, which is native "
                   "Korean. Three different 연기."],
        ),
        "셈하기": dict(
            meaning="counting, reckoning",
            notes=["Native Korean, from 셈 “a count” — the third of reading, writing "
                   "and counting. 셈하다 rather than the Sino-Korean 계산하다."],
        ),
        "초점": dict(
            hanja="焦點", meaning="focus",
            characters=[("焦", "초", "to scorch, burn"),
                        ("點", "점", "point — the same 點 as in 쟁점, 거점")],
            notes=["The burning point of a lens. 초점을 두다 is to place the focus on "
                   "something."],
        ),
        "통신문": dict(
            hanja="通信文", meaning="a home newsletter",
            characters=[("通", "통", "to communicate — the same 通 as in 통신망, 통행"),
                        ("信", "신", "message, trust — the same 信 as in 통신, 신용"),
                        ("文", "문", "writing — the same 文 as in 문자, 문맹")],
            notes=["가정 통신문 is the letter home from school — a fixture of Korean "
                   "parenting, and chapter 10's box notes it is issued in several "
                   "languages for multicultural families."],
        ),
        "알림장": dict(
            meaning="the communication book",
            notes=["Native Korean 알림 “notice” plus 帳 “ledger”. The notebook a "
                   "primary pupil carries between school and home."],
        ),
        "결석": dict(
            hanja="缺席", meaning="absence",
            characters=[("缺", "결", "to lack, be missing — as in 결점, 결핍"),
                        ("席", "석", "seat — as in 좌석 “seat”, 참석")],
            notes=["Literally the missing seat. Its opposite 출석 is attendance."],
        ),
        "생활 통지표": dict(
            hanja="生活通知表", meaning="the school report",
            characters=[("表", "표", "table, list — as in 시간표 “timetable”, 표지")],
            notes=["Records attendance, progress by subject, conduct and a general "
                   "comment, and goes home at the end of a semester."],
        ),
        "특성화": dict(
            hanja="特性化", meaning="specialisation",
            characters=[("特", "특", "special — the same 特 as in 특산물, 특송"),
                        ("性", "성", "nature"),
                        ("化", "화", "-isation — the same 化 as in 도시화, 정보화")],
            notes=["특성화 중학교 and 특성화 고등학교 are schools built round one field. "
                   "At high school level they are largely vocational, which is what "
                   "your margin note on p. 60 is getting at — 상업 leading to a bank "
                   "job, 농업 to farming."],
        ),
        "진학": dict(
            hanja="進學", meaning="going on to the next stage of schooling",
            characters=[("進", "진", "to advance — the same 進 as in 진로, 진출"),
                        ("學", "학", "to learn")],
            notes=["Met in chapter 3 as 대학 진학률, the rate of going on to "
                   "university."],
        ),
        "민주": dict(
            hanja="民主", meaning="democratic",
            characters=[("民", "민", "people — the same 民 as in 국민, 난민"),
                        ("主", "주", "master — the same 主 as in 주체적, 집주인")],
            notes=["The people as master, which is also how chapter 1 glosses "
                   "대한민국: 국민 모두가 주인이 되는 나라."],
        ),
        "자유 학년제": dict(
            hanja="自由學年制", meaning="the free-year system",
            characters=[("自", "자", "self — the same 自 as in 자치, 자율"),
                        ("由", "유", "reason, from — as in 이유 “reason”, 자유"),
                        ("制", "제", "system — the same 制 as in 제도, 차로제")],
            notes=["One of the three middle school years run without mid-term or final "
                   "examinations, given over to discussion, practical work and career "
                   "exploration. Introduced to take some weight off the exam ladder."],
        ),
        "토론": dict(
            hanja="討論", meaning="discussion, debate",
            characters=[("討", "토", "to discuss, attack"),
                        ("論", "론", "to argue — as in 논리 “logic”, 논쟁")],
        ),
        "실습": dict(
            hanja="實習", meaning="practical work",
            characters=[("實", "실", "actual, real — as in 실제, 실현"),
                        ("習", "습", "to practise — the same 習 as in 학습, 풍습")],
        ),
        "진로 탐색": dict(
            hanja="進路探索", meaning="career exploration",
            characters=[("探", "탐", "to search — as in 탐구, 탐험"),
                        ("索", "색", "to seek — as in 검색 “search”, 모색")],
        ),
        "검정고시": dict(
            hanja="檢定考試", meaning="the qualification examination",
            characters=[("檢", "검", "to examine — the same 檢 as in 건강 검진, 검사"),
                        ("定", "정", "to fix, determine — the same 定 as in 배정, 확정"),
                        ("考", "고", "to consider, test — the same 考 as in 고려"),
                        ("試", "시", "to test — as in 시험, 입시")],
            notes=["The route to a school-leaving qualification without attending — "
                   "how someone who left school early, or was homeschooled, gets into "
                   "high school or university."],
        ),
        "특수 목적 고등학교": dict(
            hanja="特殊目的高等學校", meaning="a special-purpose high school",
            characters=[("特", "특", "special"),
                        ("殊", "수", "different, particular"),
                        ("目", "목", "eye, item — as in 목표 “aim”, 과목"),
                        ("的", "적", "target, purpose")],
            notes=["Shortened to 특목고. Science, foreign language and international "
                   "high schools — the most competitive tier, and distinct from the "
                   "largely vocational 특성화고."],
        ),
        "특성화 고등학교": dict(
            hanja="特性化高等學校", meaning="a specialised high school",
            notes=["Shortened to 특성화고, and the successor to the old 실업계 "
                   "vocational schools. Your margin note on p. 60 gives the idea: a "
                   "commerce course leading to a bank, an agriculture course to "
                   "farming."],
        ),
        "자율형 고등학교": dict(
            hanja="自律型高等學校", meaning="an autonomous high school",
            characters=[("自", "자", "self"),
                        ("律", "률", "law, rule — as in 법률, 규율"),
                        ("型", "형", "type — the same 型 as in 유형, 거점형")],
            notes=["Shortened to 자율고 or 자사고. Free to set much of its own "
                   "curriculum and to select pupils, and much argued over in Korea "
                   "for that reason."],
        ),
        "자질": dict(
            hanja="資質", meaning="qualities, calibre",
            characters=[("資", "자", "resources, capital — as in 자원, 투자"),
                        ("質", "질", "quality — the same 質 as in 소질, 물질")],
            notes=["Close to 소질 but wider: 소질 is a talent for something, 자질 the "
                   "qualities a role requires. The page uses both within two "
                   "sentences."],
        ),
        "함양": dict(
            hanja="涵養", meaning="cultivation, fostering",
            characters=[("涵", "함", "to soak, immerse"),
                        ("養", "양", "to nurture — the same 養 as in 양육, 영양제")],
            notes=["Growing a quality in someone slowly, by soaking rather than "
                   "teaching: 인격 함양, 자질 함양."],
        ),
        "원격": dict(
            hanja="遠隔", meaning="remote, at a distance",
            characters=[("遠", "원", "far — as in 원거리, 영원 “eternity”"),
                        ("隔", "격", "to separate — the same 隔 as in 격차")],
            notes=["원격 수업 is the remote lesson, and 원격 근무 remote work."],
        ),
        "쌍방향": dict(
            hanja="雙方向", meaning="two-way, interactive",
            characters=[("雙", "쌍", "pair — as in 쌍둥이 “twins”"),
                        ("方", "방", "direction, way — the same 方 as in 한방, 방법"),
                        ("向", "향", "direction — the same 向 as in 경향, 방향")],
            notes=["The live video lesson, against the recorded 콘텐츠 활용형 and the "
                   "assignment-based 과제 수행형."],
        ),
        "맞춤": dict(
            meaning="tailored, made to fit",
            notes=["Native Korean, from 맞추다 “to fit”. 맞춤형 is the bespoke version "
                   "of anything — 맞춤 교육, 맞춤형 서비스, and 맞춤옷 for tailored "
                   "clothes."],
        ),
        "대여": dict(
            hanja="貸與", meaning="lending, hire",
            characters=[("貸", "대", "to lend — as in 대출 “a loan”, 임대"),
                        ("與", "여", "to give — the same 與 as in 여건, 기여")],
            notes=["Met in chapter 4's 무인 대여 시스템 for public bicycles. Here it is "
                   "smart devices lent to pupils on low incomes."],
        ),
        "홈스쿨링": dict(
            meaning="homeschooling",
            notes=["From English. Its Korean gloss in the passage is 재택 교육, "
                   "education at home."],
        ),
        "재택": dict(
            hanja="在宅", meaning="at home",
            characters=[("在", "재", "to be at — the same 在 as in 재외 동포, 현재"),
                        ("宅", "택", "house — the same 宅 as in 택배, 주택")],
            notes=["재택근무 is working from home, and became a common word in 2020 for "
                   "the same reason 원격 수업 did."],
        ),
        "의도": dict(
            hanja="意圖", meaning="intention",
            characters=[("意", "의", "intent — the same 意 as in 창의적, 의미"),
                        ("圖", "도", "picture, plan — as in 지도 “map”, 도서관")],
        ),
        "위반": dict(
            hanja="違反", meaning="violation, breach",
            characters=[("違", "위", "to go against"),
                        ("反", "반", "to oppose, reverse — as in 반대 “opposition”, 반응")],
            notes=["Of a law or a rule: 의무 교육을 위반하다, 규정 위반, 신호 위반."],
        ),
        "과태료": dict(
            hanja="過怠料", meaning="an administrative fine",
            characters=[("過", "과", "to exceed, fault — the same 過 as in 과정, 과거"),
                        ("怠", "태", "idle, negligent"),
                        ("料", "료", "fee — the same 料 as in 통행료, 보험료")],
            notes=["A fine for a breach of administrative duty, and not a criminal "
                   "penalty — which is 벌금. Homeschooling risks the first, not the "
                   "second."],
        ),
        "한편": dict(
            meaning="on the other hand; meanwhile",
            notes=["Literally one side. Met throughout the earlier chapters as "
                   "“meanwhile”; here 다른 한편으로 is explicitly the other side of the "
                   "argument."],
        ),
        "형성": dict(
            hanja="形成", meaning="formation",
            characters=[("形", "형", "form, shape — the same 形 as in 형태, 유형"),
                        ("成", "성", "to complete, become — the same 成 as in 조성, 성장")],
            notes=["Met in chapter 3, of colleagues forming a close relationship at a "
                   "회식 — 관계를 형성하다, the same phrase the experts use here."],
        ),
        "방치": dict(
            hanja="放置", meaning="neglect, leaving unattended",
            characters=[("放", "방", "to release, let go — the same 放 as in 방과, 방학"),
                        ("置", "치", "to place — the same 置 as in 조치, 설치")],
            notes=["Literally letting something lie where it is. Of a child it is the "
                   "legal word for neglect."],
        ),
        "보완": dict(
            hanja="補完", meaning="supplementing, making good a shortfall",
            characters=[("補", "보", "to supplement — the same 補 as in 보상, 보충"),
                        ("完", "완", "complete — as in 완성 “completion”, 완화")],
            notes=["Met in chapter 6's discussion prompt: 보완되어야 할 점, the points "
                   "that need shoring up. Not replacing a thing but filling in what it "
                   "lacks."],
        ),
    },

    extraNotes=[
        "The 학사 일정 table on p. 59 groups its rows under 1학기 and 2학기 with a merged "
        "cell down the side. That is set here as a 학기 column repeating the value on "
        "every row, since a row-spanning cell is not something the table block can "
        "express.",
        "The 알아두면 좋아요 on p. 59 is a pair of questions and answers. Each Q and its "
        "answer is set as one paragraph, joined by a dash.",
    ],
)
