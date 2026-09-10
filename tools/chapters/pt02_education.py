# -*- coding: utf-8 -*-
"""제2편 교육 — the spread that closes the part, pp. 70-73.

Not a chapter: every 편 ends with four pages of its own — 대단원 정리 and a
quiz, then 단원 종합 평가, then two illustrated features. Transcribed from the
photos.

제2편's quiz is not a crossword: nine statements are listed with a syllable
beside each, and the four that are true of Korean primary school combine into
the answer. The answers to it and to the 종합 평가 are mine, worked out from
chapters 9-12. The book keeps its own in 정답보기 on p. 262, which is not
photographed, so if one of mine is wrong the book is not to blame.
"""

from . import SECTION, HEADING, PARAGRAPH, BULLET, FIGURE, TABLE

PART = dict(
    number=2, slug="part-2", part=True,
    unit="교육", title="대단원 마무리", titleEn="Closing the part",

    append=[
        SECTION("summary", "대단원 정리"),
        TABLE([["한국의 교육", ""],
               ["초·중·고 운영",
                "교과와 창의적 체험 활동을 구성, 방과 후 학교 운영, 1학기는 3월 초 2학기는 8-9월 시작"],
               ["초등학교",
                "6년, 만 6세부터 입학, 취학 통지서, 기초 능력 기본 생활 습관과 바른 인성 함양에 중점"],
               ["출산 지원", "산모의 건강 관리와 출산에 필요한 비용 지원"],
               ["유치원", "만 3세부터 만5세까지 유아들이 다니는 교육부 관할 교육기관"],
               ["중학교", "3년, 자유 학년제, 기본 능력 및 민주 시민으로서 갖추어야 할 내용 다룸"],
               ["보육 지원",
                "어린이집이나 유치원 다니는 영유아(만 0-5세): 보육비, 집에서 양육하는 경우: 양육수당"],
               ["어린이집", "만 0세부터 만 5세 아이들의 보육과 교육 담당. 보건복지부 관할 보육기관"],
               ["고등학교", "3년, 진로 개척 능력과 세계 시민으로서의 자질 함양"]]),

        SECTION("quiz", "퀴즈"),
        PARAGRAPH("한국 초등학교와 관련 있는 정답 단어 4개를 조합하여 퀴즈의 정답을 찾아보세요.",
                  "Find the answer to the quiz by combining the four answer "
                  "syllables that belong to Korean primary school."),
        PARAGRAPH("퀴즈: 세계에서 바다와 가장 가까이 있는 한국의 기차역 이름은?",
                  "Quiz: what is the name of the Korean railway station "
                  "closest to the sea in the world?"),
        TABLE(["초등 관련", "정답단어", "초등 관련", "정답단어"],
              [["자유 학년", "부", "알림장", "역"],
               ["3년", "목", "수능", "강"],
               ["6년", "정", "수시 모집", "포"],
               ["양육 수당", "산", "특성화 중", "서"],
               ["45분", "울", "40분", "동"],
               ["취학 통지서", "진", "입시", "릉"]]),
        PARAGRAPH("정답 ( 정동진역 — 6년, 40분, 취학 통지서, 알림장 )",
                  "The four that are true of primary school are 6년, 40분, "
                  "취학 통지서 and 알림장; their syllables make 정동진역."),

        SECTION("exam", "단원 종합 평가"),
        HEADING(4, "01 〈보기〉에서 설명하는 것은 무엇인가?"),
        BULLET("관찰, 답사, 견학 등"),
        BULLET("가족과 함께 실시하는 것도 가능"),
        BULLET("미리 학교에 신청하면 출석으로 인정받음."),
        BULLET("① 공개 수업"),
        BULLET("② 학습 발표회"),
        BULLET("③ 현장 체험 학습"),
        BULLET("④ 창의적 체험 활동"),
        PARAGRAPH("정답 ( ③ )"),

        HEADING(4, "02 한국 교육에 관한 설명으로 옳은 것을 〈보기〉에서 모두 고른 것은?"),
        BULLET("ㄱ. 한국의 교육열은 높지 않다."),
        BULLET("ㄴ. 대학 진학률이 높은 편이다."),
        BULLET("ㄷ. 학력이 취업, 결혼 등에 유리하다고 생각하는 경향이 많다."),
        BULLET("ㄹ. 대학 진학 경쟁이 치열하여 사교육비 지출이 줄어들고 있다."),
        BULLET("① ㄱ, ㄷ"),
        BULLET("② ㄱ, ㄹ"),
        BULLET("③ ㄴ, ㄷ"),
        BULLET("④ ㄷ, ㄹ"),
        PARAGRAPH("정답 ( ③ )"),

        HEADING(4, "03 다음 중 보육료 지원 제도와 관련이 깊은 것은?"),
        BULLET("① 보건 수당"),
        BULLET("② 양육 수당"),
        BULLET("③ 배움 카드"),
        BULLET("④ 보건소 서비스"),
        PARAGRAPH("정답 ( ② )"),

        HEADING(4, "04 다음 중 평생 교육과 관련 있는 것이 아닌 것은?"),
        BULLET("① 자유 학년제"),
        BULLET("② 독학 학위제"),
        BULLET("③ 평생 학습 계좌제"),
        BULLET("④ 평생 교육 바우처 지원"),
        PARAGRAPH("정답 ( ① )"),

        HEADING(4, "05 한국 교육 제도에 대한 설명으로 옳지 않은 것은?"),
        BULLET("① 초등학교와 중학교는 의무 교육 기간이다."),
        BULLET("② 1학기는 8월말~9월초, 2학기는 3월초에 시작한다."),
        BULLET("③ 운영 주체에 따라 국립, 공립, 사립 학교로 구분된다."),
        BULLET("④ 초등학교 6년, 중학교 3년, 고등학교 3년으로 구성된다."),
        PARAGRAPH("정답 ( ② )"),

        HEADING(4, "06 〈보기〉의 ㉠, ㉡에서 설명하는 제도로 옳은 것은?"),
        BULLET("㉠ 학교생활기록부, 논술이나 실기를 중심으로 대학에 지원하는 방법이다."),
        BULLET("㉡ 법무부가 인정하는 교육 과정을 이수한 이민자에게 체류 허가나 국적 취득 시 혜택을 "
               "주는 제도이다."),
        BULLET("① 수시 모집 — 사회통합프로그램"),
        BULLET("② 수시 모집 — 이민자조기적응프로그램"),
        BULLET("③ 정시 모집 — 사회통합프로그램"),
        BULLET("④ 정시 모집 — 이민자조기적응프로그램"),
        PARAGRAPH("정답 ( ① )"),

        SECTION("feature", "다문화 학생을 위한 교육 기관"),
        PARAGRAPH("시·도 교육청 또는 다문화 교육포털(www.nime.or.kr)을 통해 거주 지역의 다문화 유치원, "
                  "다문화 예비학교, 다문화 중점 학교 등에 대한 현황을 확인할 수 있다.",
                  "Through a provincial or metropolitan office of education, "
                  "or the multicultural education portal (www.nime.or.kr), "
                  "one can find what multicultural kindergartens, "
                  "preparatory schools and focus schools there are in the "
                  "area where one lives."),
        HEADING(4, "다문화 유치원"),
        PARAGRAPH("다문화 유아를 위한 언어 및 기초 학습 등 맞춤형 교육을 지원하고, 모든 유아와 학부모를 "
                  "대상으로 다문화 이해 교육 프로그램을 운영한다.",
                  "It supports tailored teaching for multicultural infants — "
                  "language, basic learning and so on — and runs programmes "
                  "on understanding a multicultural society for all the "
                  "children and their parents."),
        HEADING(4, "다문화 예비학교"),
        PARAGRAPH("중도 입국한 국제 결혼 가정 자녀 학생이나 외국인 학생의 경우, 부족한 한국어 실력 등의 "
                  "이유로 바로 일반 학교로 진학하는 데 어려움을 겪을 수 있다. 이러한 다문화 학생들의 학교 "
                  "적응을 돕기 위해 한국어 및 한국 문화를 집중 교육하는 다문화 예비 학교가 운영되고 있다.",
                  "A student from an international marriage who arrived "
                  "mid-schooling, or a foreign student, may have difficulty "
                  "going straight into an ordinary school because their "
                  "Korean is not yet good enough. To help such students "
                  "settle into school, multicultural preparatory schools are "
                  "run that teach Korean and Korean culture intensively."),
        HEADING(4, "다문화 중점 학교"),
        PARAGRAPH("일반 학교 중 다문화 학생들이 다수 재학하고 있는 학교를 다문화 중점 학교로 지정하여, 모든 "
                  "학생을 대상으로 다문화 인식 제고 등 다문화 친화적 교육프로그램을 기획·운영하고 있다.",
                  "Ordinary schools with a large number of multicultural "
                  "students are designated multicultural focus schools, and "
                  "plan and run multicultural-friendly programmes for every "
                  "student, such as raising awareness of a multicultural "
                  "society."),
        HEADING(4, "다문화 학생을 위한 대안 학교"),
        PARAGRAPH("학업을 중단하거나 개인적 특성에 맞는 교육을 원하는 다문화 학생을 위한 학력 인정 "
                  "대안학교가 운영되고 있다. 한국어, 영어, 제2외국어를 동시에 배우는 다중 언어 특화 교육 "
                  "실시하고 있는 지구촌학교, 취업 능력 향상을 위한 직업 교육을 실시하고 있는 "
                  "서울다솜관광고등학교, 한국폴리텍다솜고등학교, 다양한 특성화 프로그램(학력 신장, 진로 "
                  "과정, 체험 활동)을 운영하고 있는 인천한누리학교 등이 있다.",
                  "Alternative schools with recognised standing are run for "
                  "multicultural students who have broken off their studies "
                  "or want teaching suited to their own character. Among "
                  "them are 지구촌학교, which specialises in multilingual "
                  "teaching where Korean, English and a second foreign "
                  "language are learnt at once; 서울다솜관광고등학교 and "
                  "한국폴리텍다솜고등학교, which give vocational education to "
                  "improve employability; and 인천한누리학교, which runs a range "
                  "of specialised programmes — raising attainment, career "
                  "courses, hands-on activities."),
        FIGURE("네 자료 사진 — 경상남도 다문화유치원 현황, 경기도 양평중 다문화 예비학교 안내문(베트남어), "
               "청도 교육지원청 제공 다문화 중점학교 현수막, 다문화 대안학교인 지구촌 학교 신입생 모집 "
               "안내"),

        SECTION("feature", "책도 읽고 체험도 하는 별별 도서관"),
        HEADING(4, "삼청공원 숲속도서관 — 숲 속의 열린 도서관"),
        PARAGRAPH("서울시 종로구 북촌로 134-3 / 02-734-3900. 도심에서 살짝 벗어난 이곳은 피톤치드 "
                  "뿜뿜! 도서관 맞은편 ‘유아 숲 체험장’에서 뛰어놀며, 자연과 함께 독서해봐요.",
                  "134-3 Bukchon-ro, Jongno-gu, Seoul / 02-734-3900. Just "
                  "outside the city centre, the place is full of the scent of "
                  "the woods. Run about in the ‘infant forest playground’ "
                  "opposite the library, and read with nature around you."),
        HEADING(4, "의정부 과학도서관 — 별도 보고 책도 보고!"),
        PARAGRAPH("의정부시 추동로 124번길 52 / 031-828-8670. 과학꿈나무들은 모두 여기로! 과학 "
                  "도서는 물론 야간관측, 4D 체험까지 할 수 있는 과학도서관에서 꿈을 키워봐요.",
                  "52 Chudong-ro 124beon-gil, Uijeongbu / 031-828-8670. All "
                  "budding scientists this way! Grow your dream at a science "
                  "library where there is night observation and 4D as well as "
                  "science books."),
        HEADING(4, "농부네 텃밭 도서관 — 시골마을 속 책놀이터"),
        PARAGRAPH("광양시 진상면 청도길 19-7 / 010-7172-5025. 독서는 기본! 마당 위를 짚라인으로 "
                  "날아다니고, 작은 연못에서 물 배도 타는 신나는 도서관입니다!",
                  "19-7 Cheongdo-gil, Jinsang-myeon, Gwangyang / "
                  "010-7172-5025. Reading is only the start! A library where "
                  "you fly over the yard on a zip line and ride a boat on a "
                  "little pond."),
        HEADING(4, "문정헌 — 글이 샘솟는 집"),
        PARAGRAPH("경북 경주시 태종로 755 / 054-742-6070. 고분들 사이 고즈넉한 한옥도서관, "
                  "신라시대의 정취를 느끼며 낭만적인 독서여행을 떠나보세요!",
                  "755 Taejong-ro, Gyeongju, Gyeongsangbuk-do / "
                  "054-742-6070. A quiet 한옥 library among the old burial "
                  "mounds; set off on a romantic reading journey with the air "
                  "of the Silla period about you."),
        FIGURE("네 도서관 홍보물 — 삼청공원 숲속도서관, 의정부 과학도서관, 농부네 텃밭 도서관, 문정헌"),
    ],

    extraNotes=[
        "제2편's closing spread runs pp. 70-73.",
        "The 대단원 정리 is a mind map of nine boxes rather than a table; the "
        "한국의 교육 box at its centre carries no text of its own, and the "
        "boxes are set here in the order the map reads.",
        "The quiz is not a crossword. Nine statements are listed with a "
        "syllable beside each; the four true of primary school — 6년, 40분, "
        "취학 통지서, 알림장 — give 정동진역. That answer and the 종합 평가 answers "
        "are mine, since 정답보기 on p. 262 is not photographed.",
        "The screenshots and posters on pp. 72-73 are not reproduced; their "
        "captions and the text beside them are.",
    ],
)
