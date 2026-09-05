# -*- coding: utf-8 -*-
"""Chapter 1 — Symbols of Korea.

Source: 1.html (Google Docs HTML export)
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, LABELS,
               COLUMNS, COLUMN,
               MARGIN, VERSE, TABLE, CELL, GLOSSARY)

CHAPTER = dict(
    number=1, slug="01-symbols-of-korea",
    unit="사회", title="한국의 상징", titleEn="Symbols of Korea",

    blocks=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 대한민국 여권 사진입니다."),
        FIGURE("차세대 전자여권 — 남색 표지에 나라 문장과 대한민국 여권, "
               "REPUBLIC OF KOREA, PASSPORT"),
        HEADING(3, "01 여권에서 찾을 수 있는 한국의 상징은 무엇입니까?"),
        HEADING(3, "02 한국의 국기, 국화, 국가에 대해 보거나 들은 경험에 대해 이야기 해 봅시다!"),
        SECTION("goals", "학습목표"),
        BULLET("한국의 {공식} 국가명과 그 의미를 설명할 수 있다.", ordered=True),
        BULLET("한국의 상징과 한글의 특징을 설명할 수 있다.", ordered=True),
        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"], [["심화", "국민",
              "1. 대한민국의 정체성과 헌법", "대한민국의 정체성"]]),
        SECTION("part", "01 한국의 국기와 국가는 무엇일까?"),
        HEADING(2, "한국의 공식 국가명"),
        GLOSSARY(("공식", "국가적이나 사회적으로 인정 된 {공적인}{방식}", "공식")),
        PARAGRAPH("한국의 공식 국가명은 대한민국이다. 대한민국은 국민 모두가 주인이 되는 나라를 의미 하며 대한민국이라는 "
          "국가명을 줄여서 한국이라고 한다. 한자로는 XXXX, 영어로는 Republic of Korea라고 한다. "
          "남한이나 South Korea라고 하는 경우도 있는데, 이것은 북한과 {구별}하여 부르는 {명칭}이다."),
        HEADING(3, "한국의 국기"),
        FIGURE("태국기"),
        LABELS("건 : 하늘", "감 : 물", "리 : 불", "곤 : 땅", "양 (positive)",
               "음 (negative)"),
        GLOSSARY(("국기", "나라를 상징하는 깃발"),
              ("존귀", "높고 귀함", None, "(nobility) (존댓말 귀하다)"),
              ("조화", "서로 잘 어울림"),
              ("평화", "갈등이 없이 평온함"),
              ("화합", "와복하게 어울림", None, "(harmony)")),
        PARAGRAPH("한국의 국기를 태극기(XXX)라고 부른다. 태극기는 흰색 바탕에 발강과 파랑의 태극 모양이 중앙에 있고, "
          "그 주변에 검은색의 4괘가 있다. 흰색은 밝음 과 순수, 평화를 의미한다. 빨강은 존귀를, 파랑은 "
          "희망을, 빨강과 파랑이 합쳐진 태극은 {조화로운|조화롭다} 우주를 나타낸다. 4괘는 각각 하늘(건), "
          "땅(곤), 물(감), 불(리)을 가리키며 자연의 조화를 의미한다. 이를 통해 태극기는 평화와 화합을 "
          "{강조} 하고 있음을 알 수 있다. {국경일}이나 {국가기념일에}는 태극기를 집 대문이나 창문 등에 " "단다."),
        HEADING(2, "한국의 국가"),
        GLOSSARY(("국가", "국가는 '나라'라는 의미와 '나라를 대표하는 노래'라는 두 가지 의미가 있다.")),
        PARAGRAPH("나라마다 그 나라를 대표하는 노래인 국가가 있다. 한국에서는 국가를 애국가라고 하는데, '나라를 사랑하는 "
          "마음을 담은 노래'라는 뜻이다. 1900년대 초에 만들어진 {애국가}는 4절로 구성 되어 있다."),
        VERSE("1절: 동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세",
              "2절: 남산 위에 저 소나무 철갑을 두른 듯 바람서리 불변함은 우리 기상일세",
              "3절: 가을 하늘 공활한데 높고 구름 없이 밝은 달은 우리 가슴 일편단심일세",
              "4절: 이 기상과 이 맘으로 충성을 다하여 괴로우나 즐거우나 나라 사랑하세 후렴(각 절마다): 무궁화 "
              "{삼천리} 화려강산 대한사람 대한으로 길이 보전하세"),
        MARGIN("추석", "서울 X", "남산- 앞산"),
        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "태극기는 언제 달까?"),
        PARAGRAPH("태극기는 매일 달아도 되는데 특히 다음과 같은 날에는 더 많이 볼 수 있다."),
        TABLE([["3월 1일(삼일절)", "일본의 지배에 저항하여 일어난 독립 만세 운동을 기념하는 날"],
              ["6월 6일(현충일)", "국가를 위해 자신의 목숨을 바친 분들을 기리는 날(조의를 표하는 날)"],
              ["7월 17일(제헌절)", "대한민국 최초의 헌법이 제정된 날을 기념하는 날"],
              ["8월 15일(광복절)", "일본의 지배에서 벗어나 독립한 것을 기념하는 날"],
              ["10월 3일(개천절)", "한국 최초의 국가인 고조선이 만들어진 것을 기념하는 날"],
              ["10월 9일(한글날)",
              "세종대왕이 훈민정음(한글)을 반포한 것을 기념하고, 한글의 연구•보급을 장려하기 위하여 정한 날"]]),
        LABELS("경축일 및 평일", "{조기 깃발}", "{조의}(XX)를 표하는 날", "> 조의금"),
        SECTION("part", "02 한국의 국화와 문자는 무엇일까?"),
        GLOSSARY(("권위", "사회적으로 인정을 받고 영향 력을 끼칠 수 있는 힘", "권위"),
              ("훈장", "국가나 사회에 공로(노력과 수고)가 큰 사람에게 국가에서 표창(널리 알려 칭찬)하기 위하여 주는 것",
              "훈장")),
        HEADING(2, "한국의 국화"),
        PARAGRAPH("한국을 {상징하|상징하다}는 꽃은 무궁화이다. 무궁화는 '영원히 피고 또 피어서 지지 않는 꽃'이라는 "
          "뜻을 담고 있다."),
        PARAGRAPH("실제로 무궁화는 보통 7월에서 10월 사이에 매일 꽃을 피우는데 나무 하나에서 약 2천여 개의 꽃 송이가 "
          "핀다. 무궁화는 오래전부터 나라를 상징 하는 꽃으로 사랑받아 왔다. 무궁화와 태극기 모양을 기초로 하여 "
          "국가의 권위를 상징하는 국가 문장이 만들어졌으며 나라의 중요한 문서, 훈장, 대통령 표창장, 여권 등에 "
          "활용되고 있다."),
        GLOSSARY(("발음기관", "말의 소리를 내는 데 쓰이는 몸의 부분", "발음기관"),
              ("훈민정음", "백성을 가르치는 바른 소리", "훈민정음"),
              ("해례본", "예를 들어서 {해설한|해설하다} 책", "해례본"),
              ("문맹", "글을 읽거나 쓸 줄 모름", "문맹")),
        HEADING(2, "한국의 문자"),
        PARAGRAPH("대한민국 {고유}{문자}인 한글은 1443년 조선의 세종대왕이 만들었다. 한글의 자음은 혀, 목, 입술 "
          "등 발음기관의 모양을, 모음은 하늘(•), 땅(ㅡ), 사람(ㅣ)의 모양을 {본떠|본뜨다} 만들었다."),
        PARAGRAPH("자음(14개)과 모음(10개) 모두 24개의 문자를 {조합}하여 모든 글자를 만들 수 있다. 글자를 "
          "만드는 {원리}가 간단하고 과학적 이어서 한글은 배우기 쉽고 사용하기에 편리하다는 {평가}를 받고 있다."),
        PARAGRAPH("세종대왕이 학자들과 함께 만든 책 「훈민정음 해례본®」에는 한글을 만든 목적을 밝히고 있는데, 그것은 "
          "글을 읽을 줄 모르는 {백성}이 쉽게 배워 쓸 수 있는 글자를 만드는 것이다. 훈민정음 해례본이 만들어진 "
          "날을 기념하여 10월 9일을 한글날로, 정해, 기념하고 있다. 유네스코에서도 이 책을 세계기록유산으로 "
          "{지정하|지정하다}였고 세계 {곳곳}에서 문맹을 없애는 데 {공}이 큰 사람이나 단체에게 "
          "'세종대왕상'이라는 이름의 상을 주고 있다."),
        FIGURE("한글 자음과 모음으로 글을 구성할 수 있는 휴대폰 자판"),
        MARGIN("세계기록  world record"),
        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "국경일, 기념식, 국제행사, 스포츠 경기는 어떻게 시작할까?"),
        PARAGRAPH("한국에서는 중요한 행사를 할 때 국기(태극기)에 대한 {경례}를 한다. 이 때 국기에 대한 {맹세}를 "
          "함께 하기도 한다."),
        COLUMNS(
            COLUMN("국기에 대한 {경례}",
                   "{차렷}{자세}에서 시선은 국기를 {향하|향하다}고, 오른손을 펴서 왼쪽 가슴에 "
                   "댄다."),
            COLUMN("국기에 대한 {맹세}",
                   "나는 자랑스러운 태극기 앞에 자유롭고 정의로운 대한민국의 무궁한 {영향}을 "
                   "위하여 {출성}을 다할 것을 굳게 {다짐}합니다.")),
    ],

    # p. 19 is not in the Doc, which stops at the foot of p. 18
    append=[
        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 한국의 국기와 국가는 무엇일까?"),
        BULLET("한국의 공식 국가명은 ( 대한민국 )이다."),
        BULLET("한국의 국기인 ( 태극기 )에는 ( 평화 )와 ( 화합 )의 의미가 담겨 있다."),
        BULLET("한국의 국가는 ( 애국가 )라고 불리는데 이것은 ( 나라 )를 사랑하는 마음을 담은 "
               "노래라는 의미를 가진다."),
        HEADING(3, "02 한국의 국화와 문자는 무엇일까?"),
        BULLET("한국을 상징하는 꽃은 ( 무궁화 )이다."),
        BULLET("한국의 국가 문장은 ( 무궁화 )와 ( 태극기 ) 모양을 기초로 하고 있다."),
        BULLET("한국의 고유한 문자인 ( 한글 )은 1443년에 조선의 ( 세종대왕 )이 만들었다."),
        BULLET("한글의 자음과 모음은 사람의 ( 발음기관 )과 하늘, 땅, ( 사람 )의 모양을 본떠 "
               "만들어졌다."),
        BULLET("한글은 ( 자음 ) 14개와 ( 모음 ) 10개 모두 24개의 문자로 구성되어 있다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "여러 나라의 국기"),
        LABELS("중국", "베트남", "필리핀", "몽골", "캄보디아", "태국"),
        FIGURE("여섯 나라의 국기 — 중국, 베트남, 필리핀, 몽골, 캄보디아, 태국"),
        PARAGRAPH("★ 자신의 고향 나라 국기의 의미나 특징을 소개해 봅시다."),
    ],
    annotations={
        "무궁화": dict(
            meaning="chrysanthemum",
        ),
        "공식": dict(
            meaning="formal/official",
            notes=["official"],
        ),
        "공적인": dict(
            meaning="official",
        ),
        "방식": dict(
            meaning="method",
        ),
        "구별": dict(
            meaning="distinguish",
        ),
        "명칭": dict(
            meaning="name/title",
        ),
        "조화롭다": dict(
            meaning="harmonious",
            surfaces=["조화로운"],
        ),
        "강조": dict(
            meaning="emphasis/stress",
        ),
        "국경일": dict(
            meaning="national holiday",
        ),
        "국가기념일에": dict(
            meaning="national memorial day",
        ),
        "애국가": dict(
            meaning="national anthem",
        ),
        "삼천리": dict(
            meaning="3000리 — 1200km",
        ),
        "조기 깃발": dict(
            meaning="flag at half-mast",
        ),
        "조의": dict(
            meaning="condolence",
        ),
        "권위": dict(
            meaning="authority/prestige",
            characters=[("權", None, "power/right"), ("威", None,
                "dignity/awe-inspiring")],
            notes=["The power to be socially recognized and to exert "
                "influence. It's not physical force — it's the kind of "
                "influence that comes from status, expertise, position, or "
                "respect that society grants someone (e.g., a doctor's "
                "medical authority, a judge's legal authority, an expert's "
                "authority on a subject)."],
        ),
        "훈장": dict(
            meaning="medal/badge",
            characters=[("勳", None, "merit/meritorious deed"), ("章", None,
                "badge/seal")],
            notes=["An award given by the state to honor someone who has made "
                "great contributions (effort and labor) to the nation or "
                "society — literally, something given \"to publicly "
                "praise\" (표창) that person's service. Think of things like "
                "a national medal of honor, an order of merit, or a state "
                "decoration given to war heroes, scientists, cultural "
                "figures, etc.", "인장 — seal/stamp"],
        ),
        "상징하다": dict(
            meaning="symbolize",
            surfaces=["상징하"],
        ),
        "발음기관": dict(
            meaning="발음(pronunciation) 기관(organ/organization) = vocal organs",
            notes=["The parts of the body used to produce speech sounds — "
                "lips, tongue, throat, teeth, etc. The key point: when King "
                "Sejong designed Hangeul's consonants (ㄱ, ㄴ, ㅁ, ㅅ, ㅇ, "
                "etc.), he based their shapes on these articulatory organs. "
                "For example, ㄱ mimics the shape of the tongue root "
                "blocking the throat, and ㄴ mimics the tongue tip touching "
                "the upper gum ridge."],
        ),
        "훈민정음": dict(
            meaning="korean script",
            characters=[("訓", None, "teach"), ("民", None, "people"), ("正", None
                , "correct"), ("音", None, "sound")],
            notes=["This term has two related meanings:",
                "The writing system itself (created by King Sejong in 1443) "
                "— what we now call Hangeul",
                "The book published in 1446 to formally introduce that "
                "writing system to the public"],
        ),
        "해례본": dict(
            meaning="When Hunminjeongeum was published, it wasn't just the "
                "letters handed out on their own — scholars (like Jeong "
                "Inji and other members of the Hall of Worthies) wrote a "
                "detailed commentary explaining why the letters were "
                "designed this way and how to use them. Because this "
                "document survives, we actually know the precise design "
                "principles behind Hangeul — which is rare among the "
                "world's writing systems (most scripts' origins are "
                "guesswork). This is why the Hunminjeongeum Haeryebon is a "
                "Korean National Treasure and a UNESCO Memory of the World "
                "item.",
            characters=[("解", None, "explain"), ("例", None, "example"), ("本",
                None, "book")],
        ),
        "해설하다": dict(
            meaning="explain/interpret",
            surfaces=["해설한"],
        ),
        "문맹": dict(
            meaning="illiteracy",
            characters=[("文", None, "writing/text"), ("盲", None, "blind")],
            notes=["The inability to read or write. This is part of why King "
                "Sejong created Hangeul in the first place — Chinese "
                "characters (hanja), the writing system in use at the time, "
                "were too difficult for most commoners to learn, so "
                "illiteracy was widespread. Sejong wanted an alphabet "
                "ordinary people could learn easily.", "맹인 — blind person"],
        ),
        "고유": dict(
            hanja="固有",
            meaning="\"unique/native/indigenous",
        ),
        "문자": dict(
            hanja="文字",
            meaning="\"script/writing system/character\"",
        ),
        "본뜨다": dict(
            meaning="to trace/model a shape after something else",
            notes=["본 in 본뜨다 comes from 本 (origin/model/pattern) — same 本 "
                "hanja you saw in 해례본 (본 = \"book/edition,\" from the same "
                "root meaning \"basis/original\"). So 본뜨다 literally carries "
                "the sense of \"to take as a model/basis and copy the "
                "shape.\""],
            surfaces=["본떠"],
        ),
        "조합": dict(
            hanja="組合",
            meaning="combination/assembly",
            notes=["조합하다 — 組 (weave/organize) + 合 (combine/unite) + 하다",
                "합치다 = 合 (unite/merge) + 치다"],
        ),
        "원리": dict(
            hanja="原理",
            meaning="principle",
            notes=["원 = origin/source, 리 = reason/logic — same 理 as in",
                "물리 \"physics\"", "논리 \"logic\""],
        ),
        "평가": dict(
            hanja="評價",
            meaning="appraisal / evaluation",
            notes=["평가 — evaluation/assessment",
                "평 = to judge/critique, 가 = value/price — same 價 as in",
                "가격 \"price\""],
        ),
        "백성": dict(
            hanja="百姓",
            meaning="\"the people/subjects\" (of a nation), specifically in the "
                "older/traditional sense",
            notes=["common people under a monarch, as opposed to the ruling "
                "class. 百 (hundred) + 姓 (surname/family name) — literally "
                "\"the hundred [family] names,\" an old way of referring to "
                "\"all the common people.\" 이 is the subject marker.",
                "글을 읽을 줄 모르는 백성이 — \"the common people who don't know how "
                "to read\"",
                "백성 is somewhat archaic/historical now — in modern Korean "
                "you'd more commonly say 국민 (國民) for \"citizens/the "
                "people\" of a country. 백성 is specifically used when "
                "talking about pre-modern/dynastic contexts (like Joseon), "
                "which is why it fits naturally here talking about King "
                "Sejong's era."],
        ),
        "지정하다": dict(
            headword="지정",
            hanja="指定",
            meaning="designation/official appointment",
            surfaces=["지정하"],
        ),
        "곳곳": dict(
            meaning="here & there / everywhere",
        ),
        "공": dict(
            hanja="功",
            meaning="merit/contribution/achievement",
        ),
        "경례": dict(
            meaning="salute / bow",
        ),
        "맹세": dict(
            meaning="vow / pledge",
        ),
        "차렷": dict(
            meaning="attention ?",
        ),
        "자세": dict(
            meaning="pose",
        ),
        "향하다": dict(
            meaning="look / face",
            surfaces=["향하"],
        ),
        "영향": dict(
            meaning="honor / glory",
        ),
        "출성": dict(
            meaning="fidelity / loyalty",
        ),
        "다짐": dict(
            meaning="promise / pledge",
        ),
    },
    fixes=[
        ("XXXX", "大韓民國", "hanja that could not be typed into the doc, restored"),
        ("태극기(XXX)", "태극기(太極旗)", "hanja that could not be typed into the doc, restored"),
        ("(XX)를 표하는", "(弔意)를 표하는", "hanja that could not be typed into the doc, restored"),
        ("태국기", "태극기", "typo — 국 for 극"),
        ("와복하게", "화목하게", "typo — 화합 is glossed 화목하게 어울림"),
        ("=출성", "충성", "typo — the pledge reads 충성을 다할 것을"),
        ("=영향", "영광", "typo — the pledge reads 무궁한 영광을 위하여"),
        ("해례본®", "해례본", "stray footnote marker picked up from the page"),
        ("인정 된", "인정된", "spacing"),
        ("=공적인", "공적인 ", "missing space, lost where the two words are annotated separately",
         ("공적인방식", "공적인 방식")),
        ("의미 하며", "의미하며", "spacing"),
        ("구성 되어", "구성되어", "spacing"),
        ("밝음 과", "밝음과", "spacing"),
        (" 하고 있음을", "하고 있음을", "spacing",
         ("강조 하고", "강조하고")),
        ("상징 하는", "상징하는", "spacing"),
        ("영향 력을", "영향력을", "spacing"),
        ("꽃 송이", "꽃송이", "spacing"),
        ("과학적 이어서", "과학적이어서", "spacing"),
        ("이야기 해 봅시다", "이야기해 봅시다", "spacing"),
        ("한글날로, 정해, 기념하고", "한글날로 정해 기념하고", "stray commas"),
        ("연구•보급", "연구·보급", "bullet used for a middle dot"),
        ("발강과 파랑", "빨강과 파랑", "typo — 발강 for 빨강; the sentence goes on to say 빨강은 존귀를"),
    ],
    approved={
        # read against the photos of pp. 16-19 and accepted
        "XXXX", "태극기(XXX)", "(XX)를 표하는", "태국기", "와복하게", "=출성",
        "=영향", "해례본®", "인정 된", "=공적인", "의미 하며", "구성 되어",
        "밝음 과", "상징 하는", "영향 력을", "꽃 송이", "과학적 이어서",
        "이야기 해 봅시다", "한글날로, 정해, 기념하고", "연구•보급", "발강과 파랑",
        " 하고 있음을",
    },
    headwords={"상징하": "상징하다", "조화로운": "조화롭다", "본떠": "본뜨다",
               "지정하": "지정하다", "해설한": "해설하다", "향하": "향하다"},
    english={
        "한국의 공식 국가명": dict(
            title="Korea's official name",
            paragraphs=[
                "Korea's official name is 대한민국. 대한민국 means a country in which "
                "all of the people are its owners, and the name is shortened to 한국. "
                "In hanja it is written 大韓民國, and in English Republic of Korea. It "
                "is sometimes called 남한 or South Korea, a way of naming it in "
                "distinction from North Korea.",
            ],
        ),
        "태극기": dict(
            title="The 태극기",
            paragraphs=[
                "Korea's flag is called the 태극기(太極旗). It has a white ground with "
                "a red and blue 태극 at the centre and four black trigrams around it. "
                "White stands for brightness, purity and peace. Red stands for "
                "nobility and blue for hope, and the 태극 in which the two are joined "
                "represents a universe in harmony. The four trigrams point to sky "
                "(건), earth (곤), water (감) and fire (리), and stand for the harmony "
                "of nature. From all this one can see that the flag emphasises peace "
                "and unity. On national holidays and days of remembrance the 태극기 is "
                "hung at the gate of the house or in a window.",
            ],
        ),
        "한국의 국가": dict(
            title="Korea's national anthem",
            paragraphs=[
                "Every country has a national anthem, a song that stands for it. In "
                "Korea the anthem is called the 애국가, which means “a song holding the "
                "love of one's country”. The 애국가, written in the early 1900s, has "
                "four verses.",
            ],
        ),
        "한국의 국화": dict(
            title="Korea's national flower",
            paragraphs=[
                "The flower that stands for Korea is the 무궁화, the rose of Sharon. "
                "Its name carries the sense of “a flower that blooms and blooms "
                "forever and never falls”.",

                "In fact the 무궁화 flowers every day from about July to October, and a "
                "single tree will put out some two thousand blooms. It has been loved "
                "as the flower of the country since long ago. The national emblem, "
                "which stands for the authority of the state, was designed from the "
                "shapes of the 무궁화 and the 태극기, and it is used on important state "
                "documents, medals, presidential citations and passports.",
            ],
        ),
        "한국의 문자": dict(
            title="Korea's script",
            paragraphs=[
                "한글, Korea's own script, was created in 1443 by King Sejong of "
                "Joseon. Its consonants were shaped after the speech organs — the "
                "tongue, the throat, the lips — and its vowels after the shapes of "
                "heaven (•), earth (ㅡ) and man (ㅣ).",

                "From 24 letters in all, 14 consonants and 10 vowels, every syllable "
                "can be composed. Because the principle behind forming a letter is "
                "simple and scientific, 한글 is held to be easy to learn and "
                "convenient to use.",

                "The book King Sejong made with his scholars, the 훈민정음 해례본, sets "
                "out why 한글 was created: to make a script that common people who "
                "could not read would be able to learn and use easily. October 9th is "
                "kept as 한글날 in commemoration of the day that book was completed. "
                "UNESCO has listed it as a Memory of the World, and an award named the "
                "King Sejong Prize is given to people and organisations around the "
                "world who have done much to end illiteracy.",
            ],
        ),
    },
    extraAnnotations={
        "무궁화": dict(
            hanja="無窮花", meaning="the rose of Sharon, Korea's national flower",
            characters=[("無", "무", "not, without — as in 무료, 무선"),
                        ("窮", "궁", "to exhaust, to run out — as in 무궁무진"),
                        ("花", "화", "flower — as in 국화, 화초")],
            notes=["Literally the flower without end, which is what the article "
                   "says of it: 영원히 피고 또 피어서 지지 않는 꽃. One tree opens "
                   "some two thousand blooms between July and October.",
                   "Hibiscus syriacus, not the chrysanthemum — that is 국화(菊花), "
                   "a homonym of 국화(國花) “national flower”."],
        ),
        # the margin glosses the book leaves without a breakdown of their own
        "국기": dict(
            hanja="國旗", meaning="a national flag",
            characters=[("國", "국", "country — as in 국가, 국민, 한국"),
                        ("旗", "기", "flag, banner — as in 태극기, 깃발's 旗")],
            notes=["국기 the flag and 국가 the country are a syllable apart and "
                   "share their 國; the flag's 旗 is the one to hold on to."],
        ),
        "조화": dict(
            hanja="調和", meaning="harmony, things sitting well together",
            characters=[("調", "조", "to tune, to adjust — as in 조정, 조사"),
                        ("和", "화", "harmony, peace — as in 화합, 평화")],
            notes=["Of parts that suit one another: 자연의 조화, 색의 조화. 화합 is "
                   "people coming together instead, and the two share 和."],
        ),
        "평화": dict(
            hanja="平和", meaning="peace",
            characters=[("平", "평", "level, even — as in 평등, 공평, 평일"),
                        ("和", "화", "harmony — the same 和 as in 조화, 화합")],
            notes=["Literally level and harmonious. The flag's white stands for "
                   "밝음과 순수, 평화."],
        ),
        "국가": dict(
            hanja="國家 / 國歌",
            meaning="a country; a national anthem — two words, one sound",
            characters=[("家", "가", "house, household — as in 가족, 국가's 家"),
                        ("歌", "가", "song — as in 노래's 歌, 가수 “singer”")],
            notes=["The margin says as much: 국가 means both ‘나라’ and ‘나라를 "
                   "대표하는 노래’. They are different words — 國家 the state, "
                   "國歌 the anthem — and only the writing tells them apart.",
                   "This article is about the second: Korea's 국가 is 애국가."],
        ),
        "공식": dict(
            hanja="公式", meaning="official, formal",
            characters=[("公", "공", "public — as in 공공, 공무원, 공개"),
                        ("式", "식", "form, ceremony — as in 방식, 결혼식")],
            notes=["공식 국가명 is the name the state goes by in law, against the "
                   "everyday 한국. Also a formula in mathematics.",
                   "The margin glosses it 국가적이나 사회적으로 인정된 공적인 방식."],
        ),
        "발음기관": dict(
            hanja="發音器官", meaning="the organs of speech",
            characters=[("發", "발", "to issue forth — as in 발행, 발달"),
                        ("音", "음", "sound — as in 음악, 모음, 자음"),
                        ("器", "기", "vessel, implement — as in 용기, 소화기"),
                        ("官", "관", "organ; official — as in 기관, 장관")],
            notes=["The tongue, throat and lips the consonants were drawn from: "
                   "ㄱ the back of the tongue, ㄴ the tip, ㅁ the mouth."],
        ),
        "존귀": dict(
            hanja="尊貴", meaning="noble, held in honour",
            characters=[("尊", "존", "to revere, hold high — as in 존경 “respect”, 존중 “esteem”, and the 존 of 존댓말"),
                        ("貴", "귀", "precious, noble — as in 귀하다 “to be precious”, 귀중품 “valuables”")],
            notes=["Of the 태극기 colours the passage assigns 존귀 to red: 빨강은 존귀를, "
                   "파랑은 희망을 나타낸다."],
        ),
        "화합": dict(
            hanja="和合", meaning="harmony, coming together as one",
            characters=[("和", "화", "harmony, peace — as in 평화 “peace”, 조화 “harmony”"),
                        ("合", "합", "to join, unite — as in 합치다 “to combine”, 조합 “assembly”")],
            notes=["Glossed on the page as 화목하게 어울림. Distinct from 조화, which is things "
                   "fitting together well; 화합 is people becoming one."],
        ),
        "양": dict(
            hanja="陽", meaning="yang, the bright and active principle",
            characters=[("陽", "양", "sun, bright, positive — as in 태양 “sun”, 양지 “sunny spot”")],
            notes=["The red half of the 태극. Paired with 음(陰); together 음양 is the pair of "
                   "forces whose balance the 태극 stands for."],
        ),
        "음": dict(
            hanja="陰", meaning="yin, the dark and receptive principle",
            characters=[("陰", "음", "shade, dark, negative — as in 음지 “shady spot”, 음력 “lunar calendar”")],
            notes=["The blue half of the 태극, paired with 양(陽)."],
        ),
    },
)
