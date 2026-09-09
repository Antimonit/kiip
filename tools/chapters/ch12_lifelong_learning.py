# -*- coding: utf-8 -*-
"""Chapter 12 — Lifelong learning.

Transcribed in your Google Doc (12.html), whose text is carried in `blocks`
below as the Doc had it, checked against the photos of pp. 66-69. The Doc
covers the whole chapter; the four photo labels, the three captions and the
table's own caption come from the pages.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, LABELS,
               TABLE, CELL, GLOSSARY)

CHAPTER = dict(
    number=12, slug="12-lifelong-learning",
    unit="교육", title="평생 교육", titleEn="Lifelong learning",

    blocks=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("우리 주변에는 다양한 교육 프로그램을 제공하는 기관이 있습니다."),
        LABELS("{도서관}", "요리 교실", "공예 교실", "{바리스타}"),
        HEADING(4, "01 사진에 제시된 프로그램과 관련된 경험이 있습니까? 혹은 주변에서 배우는 사람을 본 적이 있습니까?"),
        HEADING(4, "02 앞으로 한국에서 배워 보고 싶은 분야와 그 이유는 무엇입니까?"),
        SECTION("goals", "학습목표"),
        BULLET("평생 교육과 평생 교육 기관에 대해 설명할 수 있다.", ordered=True),
        BULLET("이주민을 위한 교육 기관과 프로그램을 설명할 수 있다.", ordered=True),
        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"], [["심화", "역사", "8. 사회 변동",
              "저출산 현상, 고령화 사회"]]),
        SECTION("part", "01 평생 교육이란 무엇일까?"),
        HEADING(2, "평생 교육의 의미와 영역"),
        GLOSSARY(("4차 산업혁명", "첨단 정보통신기술이 경제·사회 전반에 융합되어 혁신적인 변화가 나타나는 차세대 산업혁명"),
              ("기대 수명", "출생한 사람이 출생 이후 생존할 것으로 예상되는 기간"),
              ("문해", "문자를 읽고 쓸 수 있는 일 또는 그러한 일을 할 수 있는 능력"),
              ("보완", "모자라거나 부족한 것을 보충하여 완전하게 함")),
        TABLE(["영역", "내용"], [["기초 문해 교육", "문자를 읽고 쓰고 셈하는 기초 능력"],
              ["학력 보완 교육", "경제적인 사정 등으로 정규 학교에 진학하지 못한 성인이나 소외 계층에게 학습 기회 제공"],
              ["직업 능력 교육", "근로자의 직무 능력을 향상시키거나 실업자의 취업이나 창업 지원"],
              ["문화 예술 교육", "음악, 미술, 스포츠 등"],
              ["인문 교양 교육", "경제, 경영, 외국어, 컴퓨터 등"],
              ["시민 참여 교육", "시민성 함양"]]),
        FIGURE("평생 교육 6대 영역"),
        PARAGRAPH("학교 교육을 모두 마치고 직장 생활을 하면서 또는 은퇴를 한 이후에도 공부를 계속하는 사람이 많다. 4차 "
          "산업혁명과 같은 급속한 사회 변화에 대응하고 늘어나는 기대 수명에 맞추어 자아실현을 하기 위해서는 새로운 "
          "지식이나 기술을 배울 필요가 있기 때문이다. 이처럼 나이나 상황에 관계없이 본인이 관심을 가지거나 필요로 "
          "하는 분야에 대해 계속 공부하는 것을 평생 교육이라고 한다."),
        PARAGRAPH("한국 성인의 평생 학습 참여율은 43.4%(교육부 2019)로 성인 10명 중 4.3명의 성인이 평생 "
          "학습에 참여하고 있는 것으로 나타났다. 직장인, 주부, 노년층, 외국인 주민, 장애인, 북한 이탈 주민 "
          "등 대상에 따라 적절한 평생 교육 프로그램이 운영되고 있다."),
        HEADING(2, "평생 교육 기관과 지원 제도"),
        GLOSSARY(("평생 학습 계좌제 누리집", "http://www.all.go.kr"),
              ("소외 계층", "사회의 여러 정책이나 시설의 혜택을 받지 못하여 도움이 필요한 계층(저소득층, 장애인 등)"),
              ("평생 교육 바우처 지원", "https://www.lllcard.kr")),
        PARAGRAPH("평생 교육은 국가평생 교육진흥원 및 시·도 평생 교육진흥원, 시·군·구 평생 학습관, 학교 부설 평생 "
          "교육원외에도 행정복지센터, 도서관, 문화 시설, 박물관, 사회 복지관, 노인 복지관, 장애인 복지관, "
          "청소년 수련 시설 등에서 실시되고 있다. 지역 주민이 자유롭게 참여할 수 있는 다양한 평생 교육 "
          "프로그램이 개설되어 있고, 수강료도 비교적 저렴한 편이다. 최근에는 인터넷 등 미디어를 이용한 평생 "
          "교육도 늘어나고 있다."),
        PARAGRAPH("이러한 다양한 평생 학습 경험은 온라인 학습 계좌에서 누적·관리할 수 있는데 이를 학력·자격 인정이나 "
          "고용 정보로 활용할 수 있도록 하는 평생 학습 계좌제가 운영되고 있다."),
        PARAGRAPH("이 외 소외 계층을 대상으로 평생 교육에 필요한 비용의 일부를 국가가 지원하는 평생 교육 바우처 제도가 "
          "있으며 평생 교육 종합 정보 시스템인 평생 학습 포털에서는 개인 맞춤형 평생 학습 서비스를 제공한다."),
        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "평생 교육에 대한 모든 정보는 여기로: 늘 배움"),
        PARAGRAPH("국가평생학습포털 늘배움(www.lifelongedu.go.kr)은 누구나, 언제, 어디서나 원하는 평생 "
          "학습 정보를 이용할 수 있는 평생 교육 종합 정보 시스템이다. 그동안의 평생 교육은 오프라인 프로그램 "
          "중심으로 운영되어 수요자 요구에 부합하는 체계적이고 종합적인 평생 학습 지원에는 한계가 있었다. 평생 "
          "학습 참여 기회가 부족한 소외 계층이나 평생 교육 기반이 부족한 지역 주민을 포함하여 전 국민이 시간과 "
          "공간의 제약 없이 평생 학습을 가까이에서 누릴 수 있도록 전국 평생 교육 강좌 및 기관 정보뿐만 아니라 "
          "온라인을 통한 학습이 가능하도록 양질의 온라인 교육 콘텐츠를 제공한다."),
        SECTION("part", "02 이주민을 위한 교육에는 무엇이 있을까?"),
        GLOSSARY(("사회통합정보망",
              "사회통합프로그램, 국제결혼 안내 프로그램, 결혼 이민자 조기 적응 프로그램 등에 대하여 자세하게 안내하고 "
              "있으며, 누리집을 통해 원하는 교육과정에 직접 참여 신청을 할 수 있다. 누리집 "
              "접속(www.socinet.go.kr) → 회원가입 → 프로그램 참여 신청, 각종 평가 신청", None,
              "(soci-net)")),
        HEADING(2, "이주민 적응과 정착을 지원하는 교육"),
        PARAGRAPH("이주민의 한국 사회 적응을 돕기 위한 교육 서비스도 확대되고 있다. 대표적으로는 이민자 조기 적응 "
          "프로그램과 사회통합프로그램(KIIP)이 있다. 이민자 조기 적응 프로그램은 국제 결혼을 통해 처음 "
          "입국하는 새내기 결혼 이민자를 대상으로 기초 생활 정보, 상호 문화 이해(부부 교육), 체류 절차 등 "
          "한국 생활에 필요한 각종 정보를 제공한다."),
        PARAGRAPH("사회통합프로그램은 국내 이민자가 한국 사회의 능동적인 구성원으로 적응하고 자립할 수 있도록 지원하기 위하여 "
          "법무부 장관이 인정하는 교육 과정(한국어와 한국 문화 및 한국 사회 이해)을 이수한 이민자에게 체류허가나 "
          "국적 취득 시 혜택을 주는 제도이다."),
        PARAGRAPH("또한, 중도 입국 청소년과 외국인 학생을 위한 교육 지원으로 다문화 학생 언어 발달 지원 및 다문화 가정 "
          "방문 교육, 다문화 학생의 정체성 회복 및 사회성 함양 지원, 직업 훈련을 통한 이주 배경 청소년의 자립 "
          "지원, 중도 입국 학생 개인별 특성에 맞춘 맞춤형 서비스 지원 등이 있다."),
        HEADING(2, "이주민 직업 관련 교육"),
        GLOSSARY(("창업", "사업 등을 처음으로 이루어 시작함"),
              ("재정착", "일정한 곳에 다시 자리를 잡아 머물러 삶")),
        PARAGRAPH("고용노동부에서는 취업이나 창업을 원하는 사람이 직업 교육을 받을 수 있도록 내일배움카드를 발급하여 "
          "지원하고 있다. 컴퓨터, 웹디자인, 네일아트, 피부미용, 바리스타, 제과제빵, 요리 등 취업을 위한 "
          "다양한 교육을 받을 수 있다."),
        PARAGRAPH("고용 보험에 가입한 적이 있는 외국인 또는 고용 보험에 가입한 적이 없더라도 결혼 이민자인 경우에는 "
          "교육비를 지원받을 수 있다."),
        PARAGRAPH("이외에도 한국산업인력공단 외국인고용지원센터에서는 체류 기간이 끝나도 한국에 안정적으로 재정착할 수 있도록 "
          "입국 후 3년 이상 된 외국인근로자를 대상으로 자동차 정비, 중장비 운전, 용접, 전기·전자, 한식 조리, "
          "제과제빵 등의 직업 훈련 프로그램을 지원하고 있다."),
        FIGURE("이주민을 위한 원목 공예수업"),
        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "학점 은행제와 독학 학위제"),
        PARAGRAPH("학점 은행제는 학교 밖에서 이루어지는 다양한 형태의 학습 및 자격을 학점으로 인정받고, 학점이 누적되어 "
          "일정 기준을 충족하면 학위 취득이 가능한 제도이다. 학사 학위는 전공 및 교양학점을 포함하여 140학점 "
          "이상, 전문 학사는 전공 및 교양 학점을 포함하여 80학점 이상(3년제는 120학점 이상)의 학점을 "
          "인정받고 법적 요건을 충족할 경우 학위를 취득할 수 있다. (학점은행제 : " "http://www.cb.or.kr)"),
        PARAGRAPH("독학 학위제는 국가에서 실시하는 학위 취득 시험에 합격한 사람에게 학사 학위를 수여하는 제도이다. "
          "국문학, 영문학, 심리학, 경영학 등 11개 전공 분야가 있다. (독학 학위제 : "
          "https://bdes.nile.or.kr)"),
        SECTION("review", "주요 내용정리"),
        HEADING(3, "평생 교육이란 무엇일까?"),
        BULLET("나이나 상황에 관계없이 본인이 관심을 가지거나 필요로 하는 분야에 대해 계속 공부하는 것을 (        )이라고 한다."),
        BULLET("최근에는 온라인을 활용한 (        ) 평생 교육이 증가하고 있다."),
        BULLET("평생 학습 경험을 온라인 학습 계좌에서 누적·관리할 수 있는 (        ), 소외 계층을 대상으로 평생 "
          "교육에 필요한 비용의 일부를 지원하는 (        ) 제도, 평생 교육 종합 정보 시스템인 (        )이 " "운영되고 있다."),
        HEADING(3, "이주민을 위한 교육에는 무엇이 있을까?"),
        BULLET("이주민의 한국 사회 적응을 돕기 위한 대표적인 교육으로는 이민자 조기 적응 프로그램과 (        )이 있다."),
        BULLET("고용노동부에서는 취업이나 창업을 희망하는 사람에게 직업에 필요한 기술과 기능을 익힐 수 있는 교육을 받을 "
          "수 있도록 (        )를 발급하여 지원하고 있다."),
        BULLET("(        ) 가입 이력이 있는 외국인이나 (        )도 취업을 위한 교육 지원을 받을 수 있다."),
        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "대학의 우수한 강좌를 집에서 들어보자", translation=
          "Take a university’s best courses at home" "\n\n"
          "MOOC means a course, put together for learning goals defined in "
          "advance, with no limit on the number of students (Massive), open "
          "to everyone (Open) and web-based (Online)." "\n\n"
          "Its distinguishing feature is that learning runs both ways, "
          "between teacher and learner and between one learner and another: "
          "questions and answers between teacher and student, discussion, "
          "quizzes, feedback on assignments and other course management, and "
          "the running of a learning community." "\n\n"
          "The Korean MOOC (K-MOOC) too, some three full years after it "
          "first opened in October 2015, had as of December 2018 about 7.9 "
          "million site visits, some 770,000 course registrations and around "
          "350,000 members, so the interest of individual learners is "
          "growing steadily."),
        PARAGRAPH("MOOC는 {수강} {인원}에 제한 없이(Massive), 모든 사람이 수강 가능하며(Open), 웹 "
          "기반으로(Online) 미리 정의된 학습 목표를 위해 구성된 강좌(Course)를 의미한다."),
        PARAGRAPH("교수-학생 간 질문과 응답, 토론, 퀴즈, 과제 피드백 등의 학습 관리, 학습 커뮤니티 운영 등 "
          "교수-학습자 간, 학습자-학습자 간 양방향 학습이 가능하다는 특징을 가지고 있다."),
        PARAGRAPH("한국형 무크(K-MOOC)도 2015년 10월 처음 시작한 이후 만 3년 정도가 지난 2018년 12월 "
          "기준으로 누리집 방문 약 790만 건, 수강 신청 약 77만 건, 회원 가입자 수는 약 35만 명으로, "
          "개인 학습자들의 관심이 꾸준히 증가하고 있다."),
        FIGURE("K-MOOC — 한국형 온라인 공개 강좌"),
        SOURCE("[출처] http://www.kmooc.kr"),
        PARAGRAPH("★ 본인이 관심을 갖고 있거나 직업상 필요한 분야의 강의는 무엇인지 이야기해 봅시다.",
          "Talk about which courses in the fields you are interested in, or "
          "need for your work, you would take."),
    ],
    headwords={"마치고": "마치다", "맞추어": "맞추다", "누리집": "누리집",
               "충족하면": "충족하다", "이수한": "이수하다", "발급하여": "발급하다",
               "저렴한": "저렴하다", "개설되어": "개설되다"},

    english={
        "평생 교육의 의미와 영역": dict(
            title="What lifelong learning means, and where it reaches",
            paragraphs=[
                "Many people carry on studying while in work after finishing "
                "their schooling, or even after retiring. It is because, to "
                "keep up with rapid social change like the fourth industrial "
                "revolution and to realise oneself over a lengthening life "
                "expectancy, one needs to learn new knowledge and new skills. "
                "Studying on in a field one is interested in or has need of, "
                "whatever one's age or circumstances, is what is meant by "
                "lifelong learning.",

                "The rate at which Korean adults take part in lifelong "
                "learning stands at 43.4% (Ministry of Education, 2019) — "
                "4.3 adults in every ten. Programmes are run to suit "
                "different groups: people in work, homemakers, the elderly, "
                "foreign residents, disabled people, North Korean defectors "
                "and others.",
            ],
        ),
        "평생 교육 기관과 지원 제도": dict(
            title="Where lifelong learning happens, and what supports it",
            paragraphs=[
                "Lifelong learning is carried on at the National Institute "
                "for Lifelong Education, at the metropolitan and provincial "
                "institutes, at the city, county and district lifelong "
                "learning centres, and at lifelong education centres attached "
                "to schools — and beyond those, at community service centres, "
                "libraries, cultural facilities, museums, welfare centres for "
                "the general public, for the elderly and for disabled people, "
                "and at youth training facilities. A wide range of programmes "
                "is open for local residents to join freely, and the fees are "
                "comparatively low. Lately, lifelong learning using the "
                "internet and other media has been growing.",

                "This varied experience of lifelong learning can be "
                "accumulated and managed in an online learning account, and a "
                "lifelong learning account system is run so that it can be "
                "used towards recognition of attainment or qualification, or "
                "as employment information.",

                "Besides that there is the lifelong education voucher, under "
                "which the state pays part of the cost of lifelong learning "
                "for people in underserved groups, and the lifelong learning "
                "portal — the comprehensive information system for lifelong "
                "education — offers a service tailored to the individual.",
            ],
        ),
        "이주민 적응과 정착을 지원하는 교육": dict(
            title="Education that helps migrants settle in",
            paragraphs=[
                "Educational services helping migrants adapt to Korean "
                "society are also being widened. The main ones are the Early "
                "Adaptation Programme for immigrants and the Korea "
                "Immigration and Integration Program (KIIP). The Early "
                "Adaptation Programme is for newly arrived marriage migrants "
                "entering the country through an international marriage, and "
                "provides the various things needed for life in Korea — basic "
                "information about daily life, mutual cultural understanding "
                "(couples' education), residence procedures and so on.",

                "The KIIP is a scheme under which a migrant who completes a "
                "course recognised by the Minister of Justice — Korean "
                "language, and Korean culture and society — is given "
                "advantages when applying for permission to stay or for "
                "citizenship, the aim being to help migrants living in Korea "
                "adapt as active members of society and stand on their own "
                "feet.",

                "There is also educational support for young people who "
                "arrived partway through their schooling and for foreign "
                "students: help with language development for multicultural "
                "students, home visits to multicultural families, support for "
                "multicultural students in recovering their sense of identity "
                "and in developing socially, support through vocational "
                "training for young people of migrant background to become "
                "independent, and services fitted to the particular needs of "
                "each mid-entry student.",
            ],
        ),
        "이주민 직업 관련 교육": dict(
            title="Vocational education for migrants",
            paragraphs=[
                "The Ministry of Employment and Labor issues the Tomorrow "
                "Learning Card, so that anyone wanting to find work or start "
                "a business can take vocational training. A wide range of "
                "courses aimed at employment is available — computing, web "
                "design, nail art, skin care, barista work, baking and "
                "confectionery, cooking and more.",

                "A foreign national who has at some point been enrolled in "
                "employment insurance, or a marriage migrant even without "
                "such a record, can have the cost of the course covered.",

                "Besides these, the Foreign Workforce Support Center of the "
                "Human Resources Development Service of Korea runs vocational "
                "training — car maintenance, heavy equipment operation, "
                "welding, electrics and electronics, Korean cooking, baking "
                "and confectionery and so on — for foreign workers who have "
                "been in the country three years or more, so that they can "
                "resettle securely in Korea even after their period of stay "
                "comes to an end.",
            ],
        ),
    },

    extraAnnotations={
        "평생 교육": dict(
            hanja="平生敎育", meaning="lifelong learning",
            characters=[("平", "평", "flat, even — as in 평화 “peace”, 평균 “average”"),
                        ("生", "생", "life — as in 생활 “living”, 학생")],
            notes=["평생 on its own means “one's whole life”. The chapter's "
                   "subject is education that is not confined to school."],
        ),
        "도서관": dict(
            hanja="圖書館", meaning="a library",
            characters=[("圖", "도", "picture, chart — as in 지도 “map”"),
                        ("書", "서", "writing, book — as in 서류 “documents”"),
                        ("館", "관", "a hall, a building — as in 박물관 “museum”, "
                                    "체육관 “gymnasium”")],
        ),
        "바리스타": dict(
            meaning="a barista",
            notes=["From the Italian. Barista training is one of the "
                   "commonest vocational courses in the chapter's list."],
        ),
        "4차 산업혁명": dict(
            hanja="四次産業革命", meaning="the fourth industrial revolution",
            characters=[("革", "혁", "leather, to change — as in 개혁 “reform”"),
                        ("命", "명", "life, command — as in 생명 “life”, 운명")],
            notes=["혁명 is “revolution” in the sense of an upheaval, not a "
                   "rotation. 차 here counts an ordinal: the fourth."],
        ),
        "기대 수명": dict(
            hanja="期待壽命", meaning="life expectancy",
            characters=[("期", "기", "period, term — as in 기간 “period”, 학기"),
                        ("待", "대", "to wait — as in 대기 “waiting”, 초대 “invite”"),
                        ("壽", "수", "long life — as in 장수 “longevity”"),
                        ("命", "명", "life — as in 생명 “life”")],
            notes=["The 수명 is the span of a life; 기대 수명 is the span one is "
                   "expected to have at birth."],
        ),
        "문해": dict(
            hanja="文解", meaning="literacy",
            characters=[("文", "문", "writing — as in 문자 “letters”, 문학"),
                        ("解", "해", "to loosen, to understand — as in 이해, 해결")],
            notes=["Literally “understanding writing”. 기초 문해 교육 is the "
                   "teaching of reading, writing and reckoning to adults."],
        ),
        "보완": dict(
            hanja="補完", meaning="to make up what is lacking",
            characters=[("補", "보", "to mend, supplement — as in 보충 “supplement”"),
                        ("完", "완", "complete — as in 완성 “completion”, 완전")],
            notes=["학력 보완 교육 is schooling for adults who could not finish "
                   "the regular course."],
        ),
        "자아실현": dict(
            hanja="自我實現", meaning="self-realisation",
            characters=[("自", "자", "self — as in 자기 “oneself”, 자유"),
                        ("我", "아", "I, me"),
                        ("實", "실", "real, fruit — as in 사실 “fact”, 실제"),
                        ("現", "현", "to appear, present — as in 현재 “now”")],
        ),
        "소외 계층": dict(
            hanja="疏外階層", meaning="an underserved group",
            characters=[("疏", "소", "distant, sparse"),
                        ("外", "외", "outside — as in 외국 “abroad”, 재외국민"),
                        ("階", "계", "step, rank — as in 계단 “stairs”"),
                        ("層", "층", "layer, storey — as in 층간 소음, 저소득층")],
            notes=["Literally the layer left outside. Used of people who do "
                   "not reach the benefits a policy or facility offers."],
        ),
        "계좌": dict(
            hanja="計座", meaning="an account",
            notes=["Ordinarily a bank account. The 학습 계좌 borrows the idea: "
                   "learning is paid into it and accumulates like money."],
        ),
        "바우처": dict(
            meaning="a voucher",
            notes=["From the English. The state pays part of a course fee "
                   "directly rather than reimbursing the learner."],
        ),
        "누리집": dict(
            meaning="a website",
            notes=["A pure-Korean coinage for 웹사이트, from 누리 “the world”. "
                   "Government bodies use it in preference to the loanword."],
        ),
        "이주민": dict(
            hanja="移住民", meaning="a migrant",
            characters=[("移", "이", "to move — as in 이사 “moving house”, 이민"),
                        ("住", "주", "to dwell — as in 주거 “housing”, 주소"),
                        ("民", "민", "people — as in 국민 “citizen”, 난민")],
        ),
        "사회통합프로그램": dict(
            meaning="the Korea Immigration and Integration Program (KIIP)",
            notes=["The course this book is the textbook for. Completing it "
                   "counts towards permission to stay and towards "
                   "citizenship."],
        ),
        "조기": dict(
            hanja="早期", meaning="an early stage",
            characters=[("早", "조", "early — as in 조식 “breakfast”"),
                        ("期", "기", "period — the same 期 as in 기대 수명")],
        ),
        "새내기": dict(
            meaning="a newcomer, a first-year",
            notes=["A pure-Korean word, most often used of first-year "
                   "university students; here of a newly arrived marriage "
                   "migrant."],
        ),
        "능동적": dict(
            hanja="能動的", meaning="active, acting of oneself",
            characters=[("能", "능", "ability — as in 가능 “possible”, 능력"),
                        ("動", "동", "to move — as in 운동 “exercise”, 활동")],
            notes=["The opposite is 수동적, passive."],
        ),
        "자립": dict(
            hanja="自立", meaning="standing on one's own",
            characters=[("自", "자", "self — as in 자유 “freedom”"),
                        ("立", "립", "to stand, establish — as in 설립, 국립")],
        ),
        "이수": dict(
            hanja="履修", meaning="to complete a course",
            characters=[("履", "이", "to tread, to carry out — as in 이력서"),
                        ("修", "수", "to cultivate — as in 수업 “lesson”, 연수")],
        ),
        "중도 입국": dict(
            hanja="中途入國", meaning="entering the country partway through",
            characters=[("中", "중", "middle — as in 중학교, 중심"),
                        ("途", "도", "way, road — as in 용도 “use”")],
            notes=["Said of a child who joins a parent in Korea after being "
                   "raised abroad, and so enters Korean school mid-course."],
        ),
        "정체성": dict(
            hanja="正體性", meaning="identity",
            characters=[("正", "정", "correct — as in 정확 “accurate”, 정시"),
                        ("體", "체", "body — as in 신체 “body”, 단체")],
        ),
        "함양": dict(
            hanja="涵養", meaning="to cultivate, to build up",
            characters=[("涵", "함", "to soak, to nurture"),
                        ("養", "양", "to nurture — as in 양육 “bringing up”, 양성")],
            notes=["Used of qualities rather than skills: 시민성 함양, "
                   "사회성 함양."],
        ),
        "창업": dict(
            hanja="創業", meaning="starting a business",
            characters=[("創", "창", "to create — as in 창조 “creation”"),
                        ("業", "업", "work, trade — as in 직업 “occupation”, 농업")],
        ),
        "재정착": dict(
            hanja="再定着", meaning="resettlement",
            characters=[("再", "재", "again — as in 재개발 “redevelopment”"),
                        ("定", "정", "to fix, settle — as in 결정 “decision”"),
                        ("着", "착", "to attach, arrive — as in 도착 “arrival”")],
        ),
        "내일배움카드": dict(
            meaning="the Tomorrow Learning Card",
            notes=["A card the Ministry of Employment and Labor issues to "
                   "cover the cost of vocational courses. 내일 puns on "
                   "“tomorrow” and 내 일 “my work”."],
        ),
        "학점 은행제": dict(
            hanja="學點銀行制", meaning="the academic credit bank system",
            characters=[("點", "점", "point, dot — as in 점수 “score”, 초점"),
                        ("銀", "은", "silver — as in 은행 “bank”"),
                        ("制", "제", "system — as in 제도 “system”")],
            notes=["Learning done outside a university is banked as credit, "
                   "and a degree follows once enough has accumulated."],
        ),
        "독학 학위제": dict(
            hanja="獨學學位制", meaning="the self-study degree system",
            characters=[("獨", "독", "alone — as in 독립 “independence”, 단독"),
                        ("學", "학", "to learn — as in 학교, 학위")],
            notes=["A bachelor's degree awarded on passing a state "
                   "examination, with no attendance required."],
        ),
        "강좌": dict(
            hanja="講座", meaning="a course, a lecture series",
            characters=[("講", "강", "to lecture — as in 강의 “lecture”, 강사"),
                        ("座", "좌", "seat — as in 계좌 “account”, 좌석")],
        ),
        "수강": dict(
            hanja="受講", meaning="taking a course",
            characters=[("受", "수", "to receive — as in 접수 “reception”, 수업"),
                        ("講", "강", "to lecture — the same 講 as in 강좌")],
        ),
        "인원": dict(
            hanja="人員", meaning="the number of people, a headcount",
            characters=[("人", "인", "person — as in 인구 “population”, 개인"),
                        ("員", "원", "a member — as in 회원 “member”, 직원 “staff”")],
            notes=["수강 인원 = the number of people taking a course. "
                   "인원 제한 is a cap on numbers."],
        ),
        "양방향": dict(
            hanja="兩方向", meaning="two-way, interactive",
            characters=[("兩", "량", "both, two — as in 양쪽 “both sides”"),
                        ("方", "방", "direction, way — as in 방법 “method”"),
                        ("向", "향", "to face — as in 방향 “direction”")],
        ),
    },
)
