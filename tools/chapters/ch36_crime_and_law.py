# -*- coding: utf-8 -*-
"""Chapter 36 — Crime and the law.

Transcribed from the photos of pp. 186-189. Your English glosses on pp. 186,
187 and 188 are carried as the entries for the words they sit over; the 민법
and 형법 you wrote beside the two warm-up pictures are set as their labels.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, MARGIN,
               TABLE, CELL, GLOSSARY)

CHAPTER = dict(
    number=36, slug="36-crime-and-law",
    unit="법", title="범죄와 법", titleEn="Crime and the law",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 서로 다른 법이 {적용되는|적용되다} 장면입니다.",
                  "Below are scenes to which different laws apply."),
        FIGURE("밤늦게 피아노를 쳐서 옆집 사람이 잠을 못 자는 그림 · 뉴스에서 범죄 사건을 보며 검찰의 처벌을 "
               "떠올리는 그림"),
        HEADING(4, "01 두 장면에 다른 법이 적용되는 이유는 무엇입니까?",
                translation="Why do different laws apply to the two scenes?"),
        HEADING(4, "02 국가의 {강제적} {개입}이 필요한 것은 어느 쪽일까요? 그 이유는 무엇인가요?",
                translation="Which of them needs the state to step in with "
                            "force? Why?"),

        SECTION("goals", "학습목표"),
        BULLET("{형법}의 의미와 {죄형 법정주의}에 대해 설명할 수 있다.", ordered=True,
               translation="Explain what the criminal law means, and the "
                           "principle of no crime without law."),
        BULLET("{법집행기관}으로서 {경찰}과 {검찰}의 역할을 설명할 수 있다.", ordered=True,
               translation="Explain the part the police and the prosecution "
                           "play as the bodies that enforce the law."),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"],
              [["심화", "법", "20. 범죄와 법",
                "범죄와 성범죄, 형벌의 종류, 형사 재판의 과정 및 권리 보장"]]),

        SECTION("part", "01 한국에서 형법은 어떤 기능을 할까?"),
        GLOSSARY(("범죄", "사회의 안전과 질서를 해치는 반사회적 행위로 법에 규정되어 있음", "범죄",
                  "a crime, an offence"),
                 ("형벌", "범죄를 저지른 사람에게 국가가 부과하는 처벌", "형벌",
                  "a punishment, a penalty"),
                 ("사형", "범죄를 저지른 사람의 생명을 빼앗는 형벌", "사형",
                  "the death penalty"),
                 ("벌금형", "범죄를 저지른 사람의 일부 재산을 빼앗는 형벌", "벌금형",
                  "a monetary penalty"),
                 ("절취", "몰래 훔쳐감", "절취", "to steal"),
                 ("징역형", "일정 기간 동안 교도소에 갇혀 있는 형벌", "징역형",
                  "a prison sentence")),
        HEADING(2, "형법의 의미", translation=
                "What the criminal law means" "\n\n"
                "To keep order in society and protect people’s freedoms and "
                "rights, people’s bad acts must be prevented and punished. "
                "What serves as the standard for that is the criminal law. "
                "The criminal law defines as crimes the acts that do people "
                "great harm and threaten society, and lays down the "
                "punishments for those who commit them."),
        PARAGRAPH("{사회질서}를 유지하고 사람들의 자유와 권리를 보호하기 위해서는 사람들의 나쁜 행동을 막고 "
                  "{처벌할|처벌하다} 필요가 있다. 이때 {기준}이 되는 것이 바로 {형법}이다. 형법은 사람들에게 "
                  "큰 피해를 주고 사회에 {위협}이 되는 행위를 {범죄}로 {규정하고|규정하다}, 범죄를 "
                  "{저지른|저지르다} 사람들에 대한 {형벌}을 정해 놓았다."),
        TABLE(["형법 조항", "범죄 내용", "형벌 내용"],
              [["제250조", "사람을 살해한 자는", "{사형}에 처할 수 있다."],
               ["제260조", "사람의 신체에 대하여 폭행을 가한 자는", "{벌금형}에 처할 수 있다."],
               ["제329조", "타인의 재물을 {절취}한 자는", "{징역형}에 처할 수 있다."]]),

        HEADING(2, "죄형 법정주의", translation=
                "No crime without law" "\n\n"
                "죄형 법정주의 is the principle that what acts are crimes, and "
                "what punishment is to follow for them, must be laid down in "
                "law in advance. Through it people can know beforehand the "
                "criminal acts they must not do in our society and behave "
                "accordingly. And even someone who has committed a crime "
                "does not receive punishment beyond what is necessary, but "
                "only as much as the law lays down."),
        PARAGRAPH("{죄형 법정주의}는 어떤 행위가 범죄인지, 그 범죄에 대해 어떤 처벌을 할 것인지를 미리 법으로 "
                  "정해 두어야 한다는 {원칙}이다. 이를 통해 사람들은 우리 사회에서 하지 말아야 할 범죄 행위를 "
                  "미리 알고 {적절하게|적절하다} 행동할 수 있다. 또한 범죄를 저지른 사람이라도 필요 이상의 "
                  "{지나친|지나치다} 형벌을 받지 않고 법에 정해진 만큼의 형벌을 받게 된다."),
        FIGURE("범죄와 형벌이 저울에 균형을 이루는 그림"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "점점 늘어나는 사이버 범죄", translation=
                "Cyber crime, on the rise" "\n\n"
                "Crime carried out over an information network such as the "
                "internet is called cyber crime. According to police agency "
                "figures for 2019, more than 400 cyber crimes occur a day on "
                "average. Among the kinds are internet fraud (68%), cyber "
                "defamation or insult (10.1%) and cyber breach of copyright "
                "(6.1%). To avoid falling victim to cyber crime, never click "
                "a file, an email or a text message of unknown origin, and it "
                "is best not to install unverified apps on a smartphone. "
                "Checking the police agency’s ‘Cyber Cop’ app also lets one "
                "look up whether the other party’s telephone number or "
                "account number has been reported for fraud."),
        PARAGRAPH("인터넷과 같은 {정보통신망}을 통해 이뤄지는 범죄를 {사이버 범죄}라고 한다. 2019년 경찰청 "
                  "자료에 따르면 하루 평균 400건이 넘는 사이버 범죄가 발생하고 있다. 범죄 유형으로는 인터넷 "
                  "{사기}(68%), 사이버 {명예훼손}이나 {모욕}(10.1%), 사이버 {저작권침해}(6.1%) 등이 "
                  "있다. 사이버 범죄의 {피해자}가 되지 않기 위해서는 {출처} {불명}의 파일이나 이메일, "
                  "문자메시지는 절대 클릭하지 않도록 하며, 스마트폰에 {미확인} 앱을 깔지 않는 것이 좋다. "
                  "또한 경찰청의 ‘{사이버앱}’을 확인하면 상대방의 전화번호나 계좌번호가 사기로 신고된 "
                  "{이력}을 {조회할|조회하다} 수 있다."),
        FIGURE("‘4월 2일은 사이버범죄 예방의 날, 4.2데이’ 홍보물"),

        SECTION("part", "02 범죄를 막기 위해 경찰과 검찰은 어떤 일을 할까?"),
        GLOSSARY(("수사", "범죄가 발생한 것으로 여겨질 때 범인과 증거를 찾고 수집함", "수사",
                  "an investigation"),
                 ("범죄 용의자", "범죄 혐의가 뚜렷하지는 않으나 가능성이 있어서 조사 대상이 된 사람",
                  "범죄 용의자", "a criminal suspect")),
        HEADING(2, "법을 집행하는 기관", translation=
                "The bodies that enforce the law" "\n\n"
                "A state body that prevents and investigates criminal acts "
                "under the law and keeps order in society is called a law "
                "enforcement body. Such a body receives reports from those "
                "harmed by crime, investigates criminal suspects and "
                "sometimes arrests them. Establishing, through that process, "
                "whether someone has broken the law is precisely the part a "
                "law enforcement body plays. In Korea the police and the "
                "prosecution are the leading law enforcement bodies."),
        PARAGRAPH("법에 따라 범죄 행위를 {예방하고|예방하다} {수사}하며 사회질서를 유지하는 국가기관을 "
                  "{법집행기관}이라고 한다. 법집행기관은 범죄 피해를 입은 사람들의 신고를 받고 {범죄 용의자}를 "
                  "{조사하며|조사하다} {체포하기도|체포하다} 한다. 이와 같은 과정을 통해, 누군가가 법을 "
                  "{위반한|위반하다} 사실이 있었는지를 {밝혀내는|밝혀내다} 일이 바로 법집행기관의 역할이다. "
                  "한국에서는 {경찰}과 {검찰}이 대표적인 법집행기관이다."),

        GLOSSARY(("단속", "법을 어겼는지를 살피는 것", "단속", "enforcement, a crackdown"),
                 ("지구대", "각 지역의 파출소 3~4개를 하나로 묶어서 지역 내 범죄를 해결할 수 있도록 한 것",
                  "지구대")),
        HEADING(2, "경찰의 역할", translation=
                "What the police do" "\n\n"
                "When one has been harmed by another or comes to know of a "
                "crime, one should contact the police. The police protect "
                "people’s lives, bodies and property, prevent and investigate "
                "crime, and keep public order through traffic enforcement, "
                "drink-driving checks and the like. Each area has a police "
                "station and a district unit that citizens can go to "
                "themselves to ask for help. One can also ring 112, with no "
                "area code, and have the help of the police."),
        PARAGRAPH("다른 사람으로부터 피해를 입었거나 범죄 사실을 알게 되었을 때는 경찰에 연락해야 한다. 경찰은 "
                  "국민의 {생명}과 신체, 재산을 보호하는 일, 범죄를 예방하고 수사하는 일, 교통 {단속}, "
                  "음주운전 단속 등을 통해 {공공질서}를 지키는 일을 한다. 지역마다 {경찰서}와 {지구대}가 "
                  "있어서 시민이 직접 찾아가 도움을 {요청할|요청하다} 수 있다. 또한, 국번 없이 112에 "
                  "전화하여 경찰의 도움을 받을 수도 있다."),

        GLOSSARY(("청구", "어떤 일을 해 달라고 요청하는 것", "청구", "a claim, an application")),
        HEADING(2, "검찰의 역할", translation=
                "What the prosecution does" "\n\n"
                "The prosecution investigates crime, gathers the evidence "
                "relating to it and applies to the court for a trial. For an "
                "ordinary crime either the police or the prosecution may "
                "investigate in Korea, but the power to decide finally that "
                "something amounts to a crime and send it to trial rests with "
                "the prosecution. Someone within the prosecution who handles "
                "and takes responsibility for the work on a crime is called a "
                "prosecutor. A prosecutor takes part in the criminal trial "
                "directly, proving the facts of the crime and applying to the "
                "court for the punishment of the offender."),
        PARAGRAPH("{검찰}은 범죄를 수사하고 범죄와 관련한 {증거}를 모아서 {법원}에 재판을 {청구}한다. "
                  "일반적인 범죄의 경우 한국에서는 경찰이나 검찰 모두 수사할 수 있지만 {최종적}으로 범죄가 "
                  "된다고 판단하여 재판에 넘길 수 있는 {권한}은 검찰이 갖고 있다. 검찰 내에서 범죄 관련 "
                  "{업무}를 {담당하고|담당하다} 책임지는 역할을 하는 사람을 {검사}라고 한다. 검사는 {형사 "
                  "재판}에 직접 {참여하여|참여하다} 범죄자의 범죄 사실을 증명하고 범죄자에 대한 형벌을 법원에 "
                  "청구하는 역할을 한다."),
        FIGURE("형사재판의 모습 — 판사석, 검사석, 변호인석, 증인석, 피고인석"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "고위공직자 범죄수사처(공수처)가 새로 만들어졌어요", translation=
                "The Corruption Investigation Office for High-ranking "
                "Officials has been created" "\n\n"
                "On 30 December 2019 the National Assembly passed the law "
                "creating a new body to investigate the crimes of "
                "high-ranking public officials. Until then the power to send "
                "an offender to trial — the power to prosecute — was held by "
                "the prosecution service in Korea. Under the new law, "
                "however, the Corruption Investigation Office for "
                "High-ranking Officials (공수처 for short) can investigate the "
                "criminal acts of senior officials and their families. Where "
                "a judge, a prosecutor or a senior police officer is to be "
                "prosecuted, the office can bring the prosecution itself. For "
                "the office to keep its political neutrality and help "
                "establish the rule of law in Korea, continued attention and "
                "effort are needed."),
        PARAGRAPH("2019년 12월 30일 고위 공직자의 범죄를 수사하는 기관을 새로 만드는 법({공수처법})이 "
                  "국회를 {통과했다|통과하다}. 이전까지 한국에서 범죄자를 재판에 넘길 수 있는 권한인 "
                  "{기소권}은 검찰이 가지고 있었다. 그런데 공수처법으로 인해 고위 {공무원}과 그 가족의 범죄 "
                  "행위에 대해서는 {고위공직자 범죄수사처}(약칭: 공수처)가 수사할 수 있게 되었다. {판사}나 "
                  "검사, 높은 {직급}의 경찰 등이 {기소} 대상이 될 경우에는 공수처가 기소도 할 수 있게 "
                  "되었다. 공수처가 정치적 {중립성}을 유지하면서 한국의 {법질서} {확립}에 도움이 되도록 하기 "
                  "위해서는 {지속적}인 관심과 노력이 필요하다."),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 한국에서 형법은 어떤 기능을 할까?"),
        BULLET("형법은 사람들에게 큰 피해를 주고 사회에 위협이 되는 행위를 (        )로 규정하고 그러한 "
               "행위를 한 사람들에 대한 (        )을 정해 놓았다."),
        BULLET("(            )는 어떤 행위가 범죄인지, 그 범죄에 대해 어떤 처벌을 할 것인지를 미리 "
               "법으로 정해 두어야 한다는 원칙이다."),
        HEADING(3, "02 범죄를 막기 위해 경찰과 검찰은 어떤 일을 할까?"),
        BULLET("법에 따라 범죄 행위를 예방하고 수사하며 사회질서를 유지하는 국가기관을 (            )이라고 "
               "한다."),
        BULLET("(        )은 국민의 생명과 신체, 재산을 보호하는 일, 범죄를 예방하고 수사하는 일, 교통 "
               "단속, 음주운전 단속 등을 실시한다. 국번 없이 (        )에 전화하면 경찰의 도움을 받을 수 "
               "있다."),
        BULLET("범죄에 대한 수사 이후 최종적으로 재판에 넘길 수 있는 권한은 (        )이 가지고 있다. "
               "검사는 (        ) 재판에 직접 참여한다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "외국인을 위한 범죄 예방 교실", translation=
                "The crime prevention class for foreigners" "\n\n"
                "As the number of foreigners staying in Korea grows, crime "
                "involving foreigners is growing too. Some of it is "
                "deliberate, but there are also cases of carrying a weapon "
                "such as a knife without knowing Korean culture well, or of "
                "taking another’s belongings in the belief that something "
                "picked up may be kept. So Korea runs a crime prevention "
                "class for foreigners staying in the country, teaching how to "
                "avoid crime in daily life and the basic rules of order. The "
                "programme is for foreign workers, marriage immigrants and "
                "the children of multicultural families, and one can apply "
                "for it by visiting a police station or by telephone."),
        PARAGRAPH("한국에 체류하는 외국인이 증가하면서 외국인이 관련된 범죄도 늘어나고 있다. 이러한 범죄에는 "
                  "{고의적}인 것뿐 아니라 한국의 문화를 잘 모르고 칼과 같은 {흉기}를 가지고 다니는 경우, 주운 "
                  "물건을 가져가도 된다고 생각하여 남의 물건을 가져가는 경우도 있다. 그래서 한국에서는 국내에 "
                  "체류하는 외국인을 대상으로 생활 속의 범죄 예방 {요령}, 기초 질서 등을 "
                  "{교육하는|교육하다} 외국인 범죄 예방 교실 프로그램을 운영하고 있다. 이 프로그램은 외국인 "
                  "근로자, 결혼 이민자, 다문화가정 자녀 등을 대상으로 하며, 경찰서에 방문하거나 전화로 외국인 "
                  "범죄 예방 교육을 신청하면 된다."),
        FIGURE("외국인 범죄예방교실 (사진 출처: 〈연합뉴스〉)"),
        PARAGRAPH("★ 한국에서 생활하면서 본인에게 가장 필요하다고 생각하는 법교육 내용은 무엇인지, 그 이유는 "
                  "무엇인지 말해 봅시다.",
                  "Say what teaching about the law you think you most need "
                  "while living in Korea, and why."),
    ],

    extraAnnotations={
        "적용되다": dict(
            hanja="適用되다", meaning="to apply, to be applied (of a law)",
            characters=[("適", "적", "suitable — as in 적합, 적절"),
                        ("用", "용", "to use — as in 사용, 이용")],
            surfaces=["적용되는"],
        ),
        "강제적": dict(
            hanja="强制的", meaning="compulsory, by force",
            characters=[("强制", None, "by force — as in 강제퇴거")],
        ),
        "개입": dict(
            hanja="介入", meaning="intervention, stepping in",
            characters=[("介", "개", "to mediate — as in 중개, 소개"),
                        ("入", "입", "to enter — as in 입국, 입원")],
        ),
        "형법": dict(
            hanja="刑法", meaning="the criminal law",
            characters=[("刑", "형", "punishment — as in 형벌, 사형"),
                        ("法", "법", "law")],
            notes=["Set against 민법 (民法), the civil law, which governs "
                   "matters between private parties."],
        ),
        "죄형 법정주의": dict(
            hanja="罪刑法定主義",
            meaning="no crime and no punishment without law",
            characters=[("罪", "죄", "guilt, a crime — as in 범죄, 유죄"),
                        ("刑", "형", "punishment"),
                        ("法定", None, "laid down by law"),
                        ("主義", None, "-ism, principle")],
            notes=["nulla poena sine lege: what is a crime and what "
                   "punishment follows must be in the law beforehand."],
        ),
        "법집행기관": dict(
            hanja="法執行機關", meaning="a law enforcement body",
            characters=[("執行", None, "to carry out — chapter 20’s 집행"),
                        ("機關", None, "an institution, a body")],
        ),
        "경찰": dict(
            hanja="警察", meaning="the police",
            characters=[("警", "경", "to warn, guard — as in 경고, 경비"),
                        ("察", "찰", "to observe — as in 관찰, 순찰")],
        ),
        "검찰": dict(
            hanja="檢察", meaning="the prosecution service",
            characters=[("檢", "검", "to examine — as in 검사, 점검"),
                        ("察", "찰", "to observe — the same 察 as in 경찰")],
        ),
        "사회질서": dict(
            hanja="社會秩序", meaning="social order",
        ),
        "처벌하다": dict(
            hanja="處罰하다", meaning="to punish",
            characters=[("處", "처", "to handle — as in 처분, 처우"),
                        ("罰", "벌", "penalty — as in 벌금, 형벌")],
            surfaces=["처벌할"],
        ),
        "기준": dict(
            hanja="基準", meaning="a standard, the measure applied",
            characters=[("基", "기", "a base — as in 기본, 기초"),
                        ("準", "준", "a level — as in 표준, 준비")],
        ),
        "위협": dict(
            hanja="威脅", meaning="a threat",
            characters=[("威", "위", "might — as in 권위, 위력"),
                        ("脅", "협", "to threaten — as in 협박")],
        ),
        "범죄": dict(
            hanja="犯罪", meaning="a crime, an offence",
            characters=[("犯", "범", "to violate — as in 위반, 범인"),
                        ("罪", "죄", "guilt — as in 유죄, 무죄")],
        ),
        "규정하다": dict(
            hanja="規定하다", meaning="to define, to lay down",
            characters=[("規", "규", "rule — as in 규범, 규칙"),
                        ("定", "정", "to fix — as in 제정, 지정")],
            surfaces=["규정하고"],
        ),
        "저지르다": dict(
            meaning="to commit (a crime)",
            surfaces=["저지른"],
        ),
        "형벌": dict(
            hanja="刑罰", meaning="a punishment imposed by the state",
            characters=[("刑", "형", "punishment — as in 형법, 사형"),
                        ("罰", "벌", "penalty — as in 벌금, 처벌")],
        ),
        "사형": dict(
            hanja="死刑", meaning="the death penalty",
            characters=[("死", "사", "death — as in 사망, 사고"),
                        ("刑", "형", "punishment")],
        ),
        "벌금형": dict(
            hanja="罰金刑", meaning="a sentence of a fine",
        ),
        "절취": dict(
            hanja="竊取", meaning="theft, stealing",
            characters=[("竊", "절", "to steal — as in 절도"),
                        ("取", "취", "to take — as in 취득, 취업")],
        ),
        "징역형": dict(
            hanja="懲役刑", meaning="a sentence of imprisonment",
            characters=[("懲役", None, "imprisonment with labour")],
        ),
        "원칙": dict(
            hanja="原則", meaning="a principle",
            characters=[("原", "원", "origin — as in 원금, 원래"),
                        ("則", "칙", "rule — as in 규칙, 범칙금")],
        ),
        "적절하다": dict(
            hanja="適切하다", meaning="to be appropriate, fitting",
            characters=[("適", "적", "suitable — as in 적용, 적합"),
                        ("切", "절", "to cut, urgent — as in 친절, 절실")],
            surfaces=["적절하게"],
        ),
        "지나치다": dict(
            meaning="to be excessive, to go too far",
            surfaces=["지나친"],
        ),
        "정보통신망": dict(
            hanja="情報通信網", meaning="an information and communications network",
            characters=[("情報", None, "information"),
                        ("通信", None, "communication"),
                        ("網", "망", "a net — as in 통신망, 그물")],
        ),
        "사이버 범죄": dict(meaning="cyber crime"),
        "사기": dict(
            hanja="詐欺", meaning="fraud",
            characters=[("詐", "사", "to deceive"),
                        ("欺", "기", "to cheat")],
        ),
        "명예훼손": dict(
            hanja="名譽毁損", meaning="defamation",
            characters=[("名譽", None, "reputation, honour — 名 name, 譽 praise"),
                        ("毁損", None, "damage — 毁 to destroy, 損 to lose")],
        ),
        "모욕": dict(
            hanja="侮辱", meaning="insult",
            characters=[("侮", "모", "to slight"),
                        ("辱", "욕", "to disgrace — as in 욕설")],
        ),
        "저작권침해": dict(
            hanja="著作權侵害", meaning="breach of copyright",
            characters=[("著作權", None, "copyright — 著 to write, 作 to make, "
                                        "權 right"),
                        ("侵害", None, "infringement")],
        ),
        "피해자": dict(
            hanja="被害者", meaning="a victim",
            characters=[("被害", None, "harm suffered — 被 to receive, 害 harm"),
                        ("者", "자", "person")],
        ),
        "출처": dict(
            hanja="出處", meaning="the source, where something comes from",
            characters=[("出", "출", "to come out — as in 출국, 출생"),
                        ("處", "처", "a place — as in 처소, 부처")],
        ),
        "불명": dict(
            hanja="不明", meaning="unknown, unclear",
            characters=[("不", "불", "not — as in 불법, 불구"),
                        ("明", "명", "clear — as in 분명, 명확")],
        ),
        "미확인": dict(
            hanja="未確認", meaning="unverified",
            characters=[("未", "미", "not yet — as in 미등록, 미혼"),
                        ("確認", None, "confirmation")],
        ),
        "사이버앱": dict(
            meaning="the police agency’s ‘Cyber Cop’ app",
            notes=["It shows whether a number or an account has been "
                   "reported for fraud."],
        ),
        "이력": dict(
            hanja="履歷", meaning="a record, a history",
            characters=[("履", "리", "to tread, to fulfil — as in 이행"),
                        ("歷", "력", "a record — as in 경력, 학력")],
        ),
        "조회하다": dict(
            hanja="照會하다", meaning="to look up, to make an enquiry",
            characters=[("照", "조", "to shine on, to check against"),
                        ("會", "회", "to meet — as in 회의, 조회")],
            surfaces=["조회할"],
        ),
        "예방하다": dict(
            hanja="豫防하다", meaning="to prevent",
            characters=[("豫", "예", "in advance — as in 예약, 예비"),
                        ("防", "방", "to guard against — as in 방지, 방역")],
            surfaces=["예방하고"],
        ),
        "수사": dict(
            hanja="搜査", meaning="a criminal investigation",
            characters=[("搜", "수", "to search"),
                        ("査", "사", "to investigate — as in 심사, 조사")],
        ),
        "범죄 용의자": dict(
            hanja="犯罪容疑者", meaning="a criminal suspect",
            characters=[("容疑", None, "suspicion — 容 to allow, 疑 to doubt"),
                        ("者", "자", "person")],
            notes=["A 용의자 is suspected; a 피의자 (chapter 23) is formally "
                   "under investigation."],
        ),
        "조사하다": dict(
            hanja="調査하다", meaning="to investigate, to look into",
            characters=[("調", "조", "to adjust, to survey — as in 조정, 조사"),
                        ("査", "사", "to investigate")],
            surfaces=["조사하며"],
        ),
        "체포하다": dict(
            hanja="逮捕하다", meaning="to arrest",
            characters=[("逮", "체", "to catch up with"),
                        ("捕", "포", "to catch — as in 포획, 체포")],
            surfaces=["체포하기도"],
        ),
        "위반하다": dict(
            hanja="違反하다", meaning="to breach, to violate",
            characters=[("違", "위", "to violate — as in 위법"),
                        ("反", "반", "against — as in 반대, 반발")],
            surfaces=["위반한"],
        ),
        "밝혀내다": dict(
            meaning="to establish, to bring to light",
            surfaces=["밝혀내는"],
        ),
        "생명": dict(
            hanja="生命", meaning="life",
            characters=[("生", "생", "life — as in 생활, 학생"),
                        ("命", "명", "life, an order — as in 수명, 명령")],
        ),
        "단속": dict(
            hanja="團束", meaning="enforcement, checking for breaches",
            characters=[("團", "단", "a group — as in 단체, 집단"),
                        ("束", "속", "to bind — as in 약속, 구속")],
        ),
        "공공질서": dict(hanja="公共秩序", meaning="public order"),
        "경찰서": dict(
            hanja="警察署", meaning="a police station",
            characters=[("警察", None, "the police"),
                        ("署", "서", "an office — as in 부서, 서명")],
        ),
        "지구대": dict(
            hanja="地區隊", meaning="a district police unit",
            characters=[("地區", None, "a district — 地 ground, 區 zone"),
                        ("隊", "대", "a unit — as in 부대, 방범대")],
            notes=["Three or four 파출소 tied together to deal with crime in "
                   "the area."],
        ),
        "요청하다": dict(
            hanja="要請하다", meaning="to request, to ask for",
            surfaces=["요청할"],
        ),
        "증거": dict(
            hanja="證據", meaning="evidence",
            characters=[("證", "증", "evidence — as in 증명, 영수증"),
                        ("據", "거", "to rely on — as in 근거")],
        ),
        "법원": dict(
            hanja="法院", meaning="a court",
            characters=[("法", "법", "law"),
                        ("院", "원", "an institution — as in 병원, 대법원")],
        ),
        "청구": dict(
            hanja="請求", meaning="an application, a claim",
            characters=[("請", "청", "to ask — as in 신청, 요청"),
                        ("求", "구", "to seek — as in 요구, 추구")],
        ),
        "최종적": dict(
            hanja="最終的", meaning="final, in the end",
            characters=[("最", "최", "most — as in 최근, 최고"),
                        ("終", "종", "to end — as in 종료, 최종")],
        ),
        "권한": dict(
            hanja="權限", meaning="authority, a power held",
            characters=[("權", "권", "power — as in 권리, 권력"),
                        ("限", "한", "a limit — as in 제한, 한도")],
        ),
        "업무": dict(
            hanja="業務", meaning="work, duties",
            characters=[("業", "업", "business — as in 취업, 기업"),
                        ("務", "무", "duty — as in 의무, 공무원")],
        ),
        "담당하다": dict(
            hanja="擔當하다", meaning="to take charge of",
            characters=[("擔", "담", "to bear — as in 부담, 담임"),
                        ("當", "당", "to be in charge — as in 당사자, 해당")],
            surfaces=["담당하고"],
        ),
        "검사": dict(
            hanja="檢事", meaning="a prosecutor",
            characters=[("檢", "검", "to examine — as in 검찰, 점검"),
                        ("事", "사", "a matter, an affair — as in 사건, 판사")],
            notes=["Not the 검사 “examination, test”, which is 檢査."],
        ),
        "형사 재판": dict(
            hanja="刑事裁判", meaning="a criminal trial",
            characters=[("刑事", None, "criminal (in the legal sense)"),
                        ("裁判", None, "a trial — chapter 23")],
        ),
        "참여하다": dict(
            hanja="參與하다", meaning="to take part in",
            characters=[("參", "참", "to join — as in 참석, 참가"),
                        ("與", "여", "to give, to take part — as in 수여")],
            surfaces=["참여하여"],
        ),
        "공수처법": dict(
            hanja="公搜處法",
            meaning="the Act on the Corruption Investigation Office for "
                    "High-ranking Officials",
        ),
        "통과하다": dict(
            hanja="通過하다", meaning="to pass (a law, an examination)",
            characters=[("通", "통", "to pass — as in 통행, 교통"),
                        ("過", "과", "to pass by — as in 과정, 초과")],
            surfaces=["통과했다"],
        ),
        "기소권": dict(
            hanja="起訴權", meaning="the power to prosecute",
            characters=[("起訴", None, "to prosecute — 起 to raise, 訴 to sue"),
                        ("權", "권", "right, power")],
        ),
        "공무원": dict(
            hanja="公務員", meaning="a public official",
            characters=[("公務", None, "public duty"),
                        ("員", "원", "member — as in 회원, 구성원")],
        ),
        "고위공직자 범죄수사처": dict(
            hanja="高位公職者犯罪搜査處",
            meaning="the Corruption Investigation Office for High-ranking "
                    "Officials (공수처)",
            characters=[("高位", None, "high-ranking"),
                        ("公職者", None, "a holder of public office"),
                        ("搜査處", None, "an investigation office")],
        ),
        "판사": dict(
            hanja="判事", meaning="a judge",
            characters=[("判", "판", "to judge — as in 판결, 재판"),
                        ("事", "사", "a matter — as in 검사, 사건")],
        ),
        "직급": dict(
            hanja="職級", meaning="a grade, a rank in service",
            characters=[("職", "직", "a post — as in 직장, 직업"),
                        ("級", "급", "a grade — as in 학급, 등급")],
        ),
        "기소": dict(
            hanja="起訴", meaning="prosecution, bringing a charge",
        ),
        "중립성": dict(
            hanja="中立性", meaning="neutrality",
            characters=[("中立", None, "neutral — 中 middle, 立 to stand"),
                        ("性", "성", "-ness, nature — as in 전문성, 가능성")],
        ),
        "법질서": dict(
            hanja="法秩序", meaning="the legal order, the rule of law",
        ),
        "확립": dict(
            hanja="確立", meaning="establishment, putting on a firm footing",
            characters=[("確", "확", "certain — as in 확인, 확정"),
                        ("立", "립", "to stand, establish — as in 설립, 국립")],
        ),
        "지속적": dict(
            hanja="持續的", meaning="continued, sustained",
            characters=[("持", "지", "to hold — as in 유지, 지참"),
                        ("續", "속", "to continue — as in 계속, 연속")],
        ),
        "고의적": dict(
            hanja="故意的", meaning="deliberate, intentional",
            characters=[("故意", None, "intent — 故 cause, 意 intention")],
        ),
        "흉기": dict(
            hanja="凶器", meaning="a weapon (used to harm)",
            characters=[("凶", "흉", "ill, ominous"),
                        ("器", "기", "an implement — as in 기구, 무기")],
        ),
        "요령": dict(
            hanja="要領", meaning="the knack, the essentials of how to do "
                                 "something",
            characters=[("要", "요", "to require — as in 요건, 요구"),
                        ("領", "령", "to lead, to receive — as in 영수증, 대통령")],
        ),
        "교육하다": dict(
            hanja="敎育하다", meaning="to teach, to educate",
            surfaces=["교육하는"],
        ),
    },

    extraNotes=[
        "The two 생각해 봅시다 illustrations on p. 186 are described in the "
        "caption; the words you wrote beside them — 민법 for the first and 형법 "
        "for the second — are the answer to the first question.",
        "The scales illustration on p. 187, the cyber crime poster, the "
        "criminal trial illustration on p. 188 and the crime prevention class "
        "photograph on p. 189 are not reproduced; their captions are.",
        "The 형법 조항 table on p. 187 is set as a table, with the words it "
        "marks clickable in the cells.",
        "The review gaps on p. 189 are blank in the book and left blank here.",
    ],
)
