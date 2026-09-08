# -*- coding: utf-8 -*-
"""제5편 경제 — the spread that closes the part, pp. 156-159.

대단원 정리 and a 가로세로 퀴즈, then 단원 종합 평가, then two pages on the
money itself: 화폐 이야기, the coins and the notes with what is pictured on
each. Transcribed from the photos.

The answers to the crossword and to the 종합 평가 are mine, worked out from
the chapters; the book keeps its own in 정답보기 on p. 262, which is not
photographed.
"""

from . import SECTION, HEADING, PARAGRAPH, BULLET, FIGURE, TABLE

PART = dict(
    number=5, slug="part-5", part=True,
    unit="경제", title="대단원 마무리", titleEn="Closing the part",

    append=[
        SECTION("summary", "대단원 정리"),
        HEADING(4, "25. 일상생활과 경제 활동"),
        BULLET("경제 활동이란 재화와 서비스를 만들고 사고 파는 모든 활동을 말함"),
        BULLET("합리적 선택의 필요성: {희소성}으로 인해 가치 있는 것을 결정하는 것이 필요함"),
        HEADING(4, "26. 경제 성장"),
        BULLET("한국의 빠른 경제 성장 과정을 ‘한강의 기적’이라 부름"),
        BULLET("자유무역협정(FTA)을 통해 무역 규모를 확대함"),
        HEADING(4, "27. 장보기와 소비자 보호"),
        BULLET("최근에는 모바일 {기기}를 활용한 온라인 쇼핑이 증가함"),
        BULLET("소비자에게는 권리와 책임이 있음"),
        HEADING(4, "28. 금융기관 이용하기"),
        BULLET("은행은 입금, 출금, 대출, 송금, 공과금 납부 등의 업무를 맡고 있음"),
        BULLET("최근에는 지점을 따로 만들지 않고, 온라인 네트워크를 통한 인터넷 전문 은행이 "
               "등장함"),
        HEADING(4, "29. 취업하기"),
        BULLET("일자리 지원을 위해 정부는 맞춤형 정책을 시행하고 있음"),
        BULLET("취업할 때는 근로 계약서를 반드시 작성하고, 근로자의 기본 권리를 알아두어야 함"),
        HEADING(4, "찾아볼 곳"),
        BULLET("국가지표체계 — www.index.go.kr"),
        BULLET("통계청 — www.kostat.go.kr"),
        BULLET("한국무역협회 — www.kita.net"),
        BULLET("한국소비자원 — www.kca.go.kr"),
        BULLET("한국은행 — www.bok.or.kr"),
        BULLET("한국산업인력공단 — www.hrdkorea.or.kr"),

        SECTION("quiz", "가로 세로 퀴즈"),
        FIGURE("여덟 칸씩 가로세로로 짜인 낱말 퍼즐 판. 가로 열쇠 ㉮~㉲와 세로 열쇠 ①~④가 "
               "시작하는 칸에 번호가 적혀 있다."),
        HEADING(4, "가로 열쇠"),
        BULLET("㉮ 한국에서 화폐를 발행하는 은행 ( 한국은행 )"),
        BULLET("㉯ 제품을 구입하고 사용할 때 누릴 수 있는 권리를 ○○○기본법으로 정해 놓음 "
               "( 소비자 )"),
        BULLET("㉰ 본인의 이름으로만 금융 거래를 할 수 있도록 한 제도 ( 금융실명제 )"),
        BULLET("㉱ 대형 마트에 비해 좀 더 비싸고 고급스러운 물건을 많이 파는 시장 ( 백화점 )"),
        BULLET("㉲ 은행 계좌를 만들기 위해서는 반듯이 본인이 ○○○을 가지고 은행을 방문해야 함 "
               "( 신분증 )"),
        HEADING(4, "세로 열쇠"),
        BULLET("① 한국의 빠른 경제 성장을 ‘○○의 기적’이라고 부름 ( 한강 )"),
        BULLET("② 국가 간 상품이나 서비스의 자유로운 수출과 수입을 위한 약속 ( 자유무역협정 )"),
        BULLET("③ 사람이 살아가는 데 필요한 재화와 서비스를 만들어 사고 팔며 사용하는 모든 활동 "
               "( 경제 활동 )"),
        BULLET("④ 사람들이 많이 이동하는 곳에 주로 있고, 24시간 이용할 수 있는 시장 ( 편의점 )"),

        SECTION("exam", "단원 종합 평가"),
        HEADING(4, "01 한국의 경제 성장 과정을 ‘한강의 기적’이라고 부르는 이유는?"),
        BULLET("① 한강이 없었다면 경제 성장을 할 수 없었기 때문이다."),
        BULLET("② 한강 주변의 공장에서 생산된 제품이 많았기 때문이다."),
        BULLET("③ 세계가 놀랄 정도로 빠른 경제 성장을 이루었기 때문이다."),
        BULLET("④ 로봇 산업, 생명 공학, 신소재 산업이 발달하고 있기 때문이다."),
        PARAGRAPH("정답 ( ③ )"),

        HEADING(4, "02 시장에 대한 설명으로 옳지 않은 것은?"),
        BULLET("① 전통 시장에서는 가격 흥정을 하는 모습을 흔히 볼 수 있다."),
        BULLET("② 5일장은 교통이 편리해지고 도시의 인구가 늘어나면서 활성화되고 있다."),
        BULLET("③ 대형 마트는 주차장이 넓고 물건의 종류가 많아 사람들에게 인기가 있다."),
        BULLET("④ 슈퍼마켓은 주로 집 근처 동네에 위치하고 있으며 식료품을 구매할 수 있다."),
        PARAGRAPH("정답 ( ② )"),

        HEADING(4, "03 소비자가 보호 받을 권리에 대한 설명으로 옳은 것을 〈보기〉에서 모두 고른 "
                   "것은?"),
        BULLET("ㄱ. 한국에는 법으로 소비자의 권리를 규정하고 있다.", level=2),
        BULLET("ㄴ. 제품을 구입한 후에는 교환이나 환불이 되지 않는다.", level=2),
        BULLET("ㄷ. 외국인의 경우 소비 생활에서 문제가 발생한 경우 해결할 수 없다.", level=2),
        BULLET("ㄹ. 제품에서 문제가 발생한 경우에는 우선 구입한 상점이나 기업과 상담을 한다.",
               level=2),
        BULLET("① ㄱ, ㄴ"),
        BULLET("② ㄱ, ㄹ"),
        BULLET("③ ㄴ, ㄷ"),
        BULLET("④ ㄷ, ㄹ"),
        PARAGRAPH("정답 ( ② )"),

        HEADING(4, "04 금융기관에 대한 설명으로 옳은 것은?"),
        BULLET("① 농협에서는 예금 업무가 가능하지만 우체국에서는 할 수 없다."),
        BULLET("② 은행은 사람들의 돈을 맡아주는 예금, 빌려주는 대출 업무만 담당하고 있다."),
        BULLET("③ 상호저축은행은 시중은행보다 금리가 낮은 편이지만 그에 비해 안전성은 높다."),
        BULLET("④ {점포}를 마련하지 않고 온라인 네트워크를 통해 금융 서비스를 제공하는 은행도 "
               "있다."),
        PARAGRAPH("정답 ( ④ )"),

        HEADING(4, "05 〈보기〉에서 설명하는 것으로 옳은 것은?"),
        BULLET("가짜 이름이나 다른 사람이 아닌 오직 본인의 이름으로만 금융 거래를 할 수 있도록 한 "
               "제도", level=2),
        BULLET("① 리콜제"),
        BULLET("② 금융실명제"),
        BULLET("③ 자유무역협정"),
        BULLET("④ 인터넷 뱅킹"),
        PARAGRAPH("정답 ( ② )"),

        HEADING(4, "06 일자리 지원을 위한 정부의 대책에 대한 설명으로 옳지 않은 것은?"),
        BULLET("① 60세 이상 국민의 재취업 지원을 하고 있다."),
        BULLET("② {임신} 또는 육아 여성의 근로 시간을 {연장}하고 있다."),
        BULLET("③ 실업자에게 다양한 교육 프로그램을 제공하고 있다."),
        BULLET("④ 청년에게는 구직 활동 지원금 정책을 시행하고 있다."),
        PARAGRAPH("정답 ( ② )"),

        SECTION("feature", "화폐 이야기"),
        PARAGRAPH("화폐는 물건을 사고 팔 때 사용하는 수단인 {동시}에 각 나라의 {특색}이 "
                  "{반영}되어 있다. 즉, 화폐에는 그 나라나 지역을 대표하는 {훌륭}한 {인물}이나 "
                  "{상징}이 {담겨|담기다} 있다. 한국의 화폐에도 인물, 자연, 동물 등이 {소재}로 "
                  "{활용}되었다. {최초} {발행} 시기와 담겨 있는 그림에 대한 설명은 다음과 같다."),
        HEADING(3, "동전"),
        TABLE(["동전", "최초 발행", "그림"],
              [["1원 (일 원)",
                "1966년 8월 16일 (현재 사용되는 모습과 같은 동전은 1983년 1월 15일)", "무궁화"],
               ["5원 (오 원)",
                "1966년 8월 16일 (현재 사용되는 모습과 같은 동전은 1983년 1월 15일)", "거북선"],
               ["10원 (십 원)",
                "1966년 8월 16일 (현재 사용되는 모습과 같은 동전은 2006년 12월 18일)", "다보탑"],
               ["50원 (오십 원)",
                "1972년 12월 1일 (현재 사용되는 모습과 같은 동전은 1983년 1월 15일)", "벼이삭"],
               ["100원 (백 원)",
                "1970년 11월 30일 (현재 사용되는 모습과 같은 동전은 1983년 1월 15일)",
                "충무공 이순신"],
               ["500원 (오백 원)", "1982년 6월 12일", "두루미"]]),
        HEADING(3, "지폐"),
        TABLE(["지폐", "최초 발행", "그림"],
              [["1,000원 (천 원)",
                "1975년 8월 14일 (현재 사용되는 모습과 같은 지폐는 2007년 1월 22일)",
                "앞: 이황, 성균관 명륜당, 매화 / 뒤: 정선의 계상정거도"],
               ["5,000원 (오천 원)",
                "1972년 7월 1일 (현재 사용되는 모습과 같은 지폐는 2006년 1월 2일)",
                "앞: 이이, 오죽헌과 오죽 / 뒤: 신사임당의 초충도"],
               ["10,000원 (만 원)",
                "1973년 6월 12일 (현재 사용되는 모습과 같은 지폐는 2007년 1월 22일)",
                "앞: 세종대왕, 일월오봉도, 용비어천가 / "
                "뒤: 혼천의, 천상열차분야지도, 보현산 천문대 망원경"],
               ["50,000원 (오만 원)", "2009년 6월 23일",
                "앞: 신사임당, 묵포도도, 초충도수병의 가지 / "
                "뒤: 어몽룡의 월매도, 이정의 풍죽도"]]),
    ],

    english={
        "화폐 이야기": dict(
            title="The story on the money",
            paragraphs=[
                "Money is the means of buying and selling, and at the same "
                "time it carries the character of the country that issues it. "
                "A banknote holds a distinguished figure, or a symbol, that "
                "stands for the country or the region. Korean money too draws "
                "on people, nature and animals for its subjects. When each "
                "was first issued, and what is pictured on it, is as follows.",
            ],
        ),
    },

    extraAnnotations={
        "희소성": dict(
            hanja="稀少性", meaning="scarcity",
            characters=[("稀", "희", "rare — as in 희귀하다"),
                        ("少", "소", "few — as in 소수, 감소")],
            notes=["The premise of economics: wants exceed what there is, so "
                   "choosing is unavoidable. It is why the book keeps "
                   "returning to 합리적 선택."],
        ),
        "기기": dict(hanja="機器", meaning="a device"),
        "점포": dict(
            hanja="店鋪", meaning="a shop premises",
            characters=[("店", "점", "shop — as in 상점, 편의점"),
                        ("鋪", "포", "shop, to spread out")],
        ),
        "임신": dict(
            hanja="妊娠", meaning="pregnancy",
            characters=[("妊", "임", "to conceive"),
                        ("娠", "신", "to be pregnant")],
        ),
        "연장": dict(hanja="延長", meaning="extension, lengthening"),
        "동시": dict(
            hanja="同時", meaning="the same time",
            characters=[("同", "동", "same — as in 동일, 공동"),
                        ("時", "시", "time — as in 시간, 임시")],
            notes=["A와 동시에 “at once A and…”."],
        ),
        "특색": dict(
            hanja="特色", meaning="a distinctive character",
            characters=[("特", "특", "special — as in 특징, 특산품"),
                        ("色", "색", "colour — as in 색깔, 염색")],
        ),
        "반영": dict(
            hanja="反映", meaning="reflection, being reflected in",
            characters=[("反", "반", "opposite, to reflect — as in 반면, 반대"),
                        ("映", "영", "to project — as in 영화, 상영")],
        ),
        "훌륭": dict(meaning="being fine, admirable"),
        "인물": dict(
            hanja="人物", meaning="a figure, a personage",
            characters=[("物", "물", "thing — as in 물건, 인물화")],
        ),
        "상징": dict(
            hanja="象徵", meaning="a symbol",
            characters=[("象", "상", "form, image — as in 상상, 현상"),
                        ("徵", "징", "sign — as in 징조")],
            notes=["Chapter 1 is 한국의 상징."],
        ),
        "담기다": dict(meaning="to be contained in, to be held"),
        "소재": dict(
            hanja="素材", meaning="subject matter, material",
            characters=[("素", "소", "element, plain — as in 요소, 신소재"),
                        ("材", "재", "material — as in 재료, 인재")],
        ),
        "활용": dict(hanja="活用", meaning="use, putting to use"),
        "최초": dict(hanja="最初", meaning="the first"),
        "발행": dict(
            hanja="發行", meaning="issuance",
            notes=["Of money, a document or a newspaper alike."],
        ),
    },

    extraNotes=[
        "The crossword grid is not reproduced; its clues are, with the "
        "answers covered. Those answers, and the answers to the 종합 평가, are "
        "mine — worked out from the chapters, since 정답보기 on p. 262 is not "
        "photographed.",
        "Clue ㉲ prints 반듯이 where 반드시 is the word. That is the book's own "
        "slip and stands as printed.",
        "대단원 정리 prints each chapter's points as two bullets in a table "
        "cell; they are set here as a heading with its bullets beneath, since "
        "a cell holds one run of text.",
        "화폐 이야기 keeps its two tables. The pictures on each coin and note "
        "are the book's own words; the front and back of a note are joined in "
        "one cell with a slash, as a cell holds one run of text.",
        "The coins and notes themselves are not reproduced.",
    ],
)
