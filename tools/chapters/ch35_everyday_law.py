# -*- coding: utf-8 -*-
"""Chapter 35 — Everyday law.

Transcribed from the photos of pp. 182-185. Your English glosses on pp. 183,
184 and 185 are carried as the entries for the words they sit over, and the
review answers you wrote in the margin of p. 185 are carried as the blanks'
answers.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, MARGIN,
               TABLE, CELL, GLOSSARY)

CHAPTER = dict(
    number=35, slug="35-everyday-law",
    unit="법", title="생활 법률", titleEn="Everyday law",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 한국의 공공 시설이나 아파트 등에서 쓰레기를 모아 버리는 곳의 모습입니다.",
                  "Below is what the place for collecting and putting out "
                  "rubbish looks like at public facilities and blocks of "
                  "flats in Korea."),
        FIGURE("올림픽공원의 분리배출 수거함 — 종이류, 유리병, 프라스틱류, 고철·캔류"),
        HEADING(4, "01 사진과 같은 방식으로 쓰레기를 버릴 때의 {장점}과 {단점}은 무엇입니까?",
                translation="What are the advantages and the drawbacks of "
                            "putting rubbish out the way the photograph "
                            "shows?"),
        HEADING(4, "02 자신의 고향 나라와 한국의 쓰레기 버리는 방식에는 어떤 차이가 있습니까?",
                translation="How does putting out rubbish differ between your "
                            "home country and Korea?"),

        SECTION("goals", "학습목표"),
        BULLET("{경범죄}의 {개념}과 {사례}를 설명할 수 있다.", ordered=True,
               translation="Explain what a minor offence is, with examples."),
        BULLET("{음주 운전}과 {학교 폭력}에 대해 설명할 수 있다.", ordered=True,
               translation="Explain drink-driving and violence at school."),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"],
              [["기본", "법", "30. 외국인과 법", "준법의 중요성"]]),

        SECTION("part", "01 경범죄에는 무엇이 있을까?"),
        GLOSSARY(("사소하다", "보잘 것 없고 작음", "사소하다", "trivial, minor, petty"),
                 ("제재", "일정한 규칙으로 제한하거나 금지함", "제재",
                  "sanctions, restrictions"),
                 ("위법", "법을 위반함", "위법", "illegal"),
                 ("자가 격리",
                  "전염병에 걸렸거나 걸렸을 가능성이 있는 사람이 스스로 집에 머물면서 다른 사람으로부터 "
                  "떨어져 지내는 것", "자가 격리", "self-isolation")),
        HEADING(2, "경범죄", translation=
                "Minor offences" "\n\n"
                "Say ‘crime’ and people generally think of grave crimes — "
                "murder, robbery, assault. But even an act that looks "
                "trivial can bring a sanction where it harms others or does "
                "not fit public order. That is because it counts as a minor "
                "offence. A minor offence means a relatively light unlawful "
                "act committed in the course of everyday life: spitting in "
                "the street, cutting in line rather than waiting one’s "
                "turn." "\n\n"
                "Where an infectious disease such as COVID-19 breaks out, "
                "meanwhile, keeping to the safety rules in everyday life "
                "matters a great deal. Breaking safety rules such as "
                "self-isolation can bring a much heavier punishment than a "
                "minor offence. Someone who leaves the place of "
                "self-isolation as they please may have to pay a fine, and a "
                "foreigner may even be made to leave the country."),
        PARAGRAPH("일반적으로 {범죄}라고 하면 {살인}, {강도}, {폭행} 등 {중대한|중대하다} 범죄를 "
                  "{떠올린다|떠올리다}. 그러나 {사소한|사소하다} 것처럼 보이는 {행위}라도 남에게 피해를 "
                  "주거나 {공공질서}에 맞지 않는 경우에는 {제재}를 받을 수 있다. 이는 {경범죄}에 "
                  "{해당하기|해당하다} 때문이다. 경범죄란 길에 침을 {뱉거나|뱉다} 자기 {순서}를 기다리지 "
                  "않고 {새치기하는|새치기하다} 등 일상생활에서 {저지르는|저지르다} 비교적 가벼운 {위법} "
                  "행위를 말한다."),
        PARAGRAPH("한편, 코로나19와 같은 {전염병}이 발생했을 때는 일상생활에서의 {안전수칙}을 지키는 것이 "
                  "매우 중요하다. {자가 격리} 등과 같은 안전수칙을 {어길|어기다} 경우 경범죄보다 훨씬 무거운 "
                  "{처벌}을 받을 수 있다. 자가 격리 장소를 {함부로} {벗어난|벗어나다} 사람은 {벌금}을 낼 "
                  "수도 있고 외국인은 {강제 출국}이 될 수도 있다."),

        GLOSSARY(("무단투기", "아무렇게나 마구 내던져 버림", "무단투기",
                  "illegal disposal of rubbish"),
                 ("과태료", "형벌로서 내야 하는 벌금과 달리, 의무를 게을리한 사람에게 내도록 하는 돈",
                  "과태료", "a fine, a penalty"),
                 ("신고 포상금제", "쓰레기 무단투기를 한 사람을 신고하면 상으로 돈을 주는 제도",
                  "신고 포상금제", "the report reward system")),
        HEADING(2, "쓰레기 무단투기", translation=
                "Fly-tipping" "\n\n"
                "Putting rubbish somewhere other than the appointed place, or "
                "putting it out without the standard bag, counts as a minor "
                "offence and can bring a fine. Dropping a cigarette butt or "
                "waste paper anywhere brings a fine of 50,000 won; putting "
                "rubbish out in an ordinary bag rather than the standard bag, "
                "200,000 won; burying it in the ground, 700,000 won (as of "
                "2018). Most local authorities across the country run a "
                "reward scheme for reporting fly-tipping."),
        PARAGRAPH("쓰레기를 정해진 곳에 버리지 않거나 {종량제 봉투}에 넣어 버리지 않는 행위는 경범죄에 "
                  "해당하며 {과태료}를 낼 수 있다. {담배꽁초}나 {휴지}를 아무 데나 버리면 5만 원을, "
                  "쓰레기를 종량제봉투에 넣지 않고 일반 봉투에 넣어서 버리면 20만 원을, 땅에 "
                  "{묻어서|묻다} 버리면 70만 원을 과태료로 내야 한다(2018년 기준). 쓰레기 {무단투기}에 "
                  "대해 전국 대부분의 지방자치단체에서는 {신고 포상금제}를 실시하고 있다."),
        FIGURE("쓰레기 종량제 봉투 (사진 출처: 〈연합뉴스〉)"),

        GLOSSARY(("무단횡단", "정해진 규칙에 따르지 않고 길을 건넘", "무단횡단", "jaywalking"),
                 ("범칙금", "교통 규칙을 어겼을 때 내는 돈", "범칙금", "a fine, a penalty"),
                 ("건널목", "철로와 도로가 만나는 곳에서 사람들이 길을 건널 수 있도록 만들어 놓은 곳",
                  "건널목", "a level crossing")),
        HEADING(2, "무단횡단", translation=
                "Jaywalking" "\n\n"
                "In crossing the road one should wait for the signal where "
                "there is a crossing. Ignoring the signal and crossing "
                "because no cars are about (a fine of 20,000 won), or "
                "crossing where there is no crossing (a fine of 30,000 won), "
                "puts oneself and others in danger. One must not jaywalk "
                "where there is a level crossing either, not only where cars "
                "pass. Lately people jaywalk without realising it while "
                "walking and looking at a smartphone, so care is needed."),
        PARAGRAPH("길을 건널 때는 {횡단보도}가 있는 곳에서 {신호등}의 {신호}를 기다렸다가 건너야 한다. "
                  "그런데 도로에 차가 다니지 않는다고 해서 신호를 {무시하고|무시하다} 횡단보도를 "
                  "건너거나({범칙금} 2만원) 횡단보도가 없는 곳에서 길을 건너는 행위(범칙금 3만원)는 자신과 "
                  "타인을 {위험하게|위험하다} 만드는 행위이다. 자동차가 다니는 {건널목}뿐 아니라 {철도} "
                  "건널목이 있는 곳에서도 {무단횡단}을 해서는 안 된다. 최근에는 스마트폰을 보며 걷다가 자신도 "
                  "모르게 무단횡단을 하는 경우가 있으니 주의해야 한다."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "어디에 앉든지 안전띠는 필수!", translation=
                "Wherever you sit, the seat belt is a must!" "\n\n"
                "Every passenger must wear a seat belt in a car or an express "
                "coach. Someone sitting in the back must wear one as well as "
                "the driver and the front passenger. Not wearing a seat belt "
                "brings a fine of 30,000 won, and where a child under 13 is "
                "not wearing one the fine is 60,000 won. An infant under 6 "
                "must be seated in a car seat."),
        PARAGRAPH("{승용차}나 {고속버스} 등을 탈 때 모든 {승객}은 반드시 {안전띠}를 매야 한다. 승용차 "
                  "{운전석}이나 {조수석}은 물론 {뒷좌석}에 앉는 사람도 안전띠를 매야 한다. 안전띠를 하지 "
                  "않으면 3만원의 과태료를 내야하고, 13세 미만 어린이가 안전띠를 하지 않았을 때는 6만원의 "
                  "과태료를 내야 한다. 6세 미만의 {영·유아}는 {카시트}에 앉혀야 한다."),
        SOURCE("[출처] 한겨레(2018.09.27)"),
        FIGURE("뒷좌석 안전띠 필수"),

        SECTION("part", "02 음주운전과 학교폭력은 무엇일까?"),
        GLOSSARY(("적발되다", "감추어져 있던 일이 찾아져 밝혀짐", "적발되다",
                  "to be caught out, to be uncovered")),
        HEADING(2, "음주운전", translation=
                "Drink-driving" "\n\n"
                "Drink-driving means driving after taking alcohol, before "
                "returning to a normal state. Someone who drives after "
                "drinking is punished for breaching the Road Traffic Act even "
                "where no accident occurs. Because drink-driving threatens "
                "the lives of other drivers and pedestrians as well as the "
                "driver’s own, the law regulates it strictly." "\n\n"
                "A driver caught drink-driving faces up to five years’ "
                "imprisonment or a fine of up to twenty million won. Where "
                "someone is injured or killed as a result, the punishment is "
                "heavier still. Refusing when a traffic officer asks for a "
                "breath test is itself punishable, so one must always submit "
                "to the test. If one has drunk even a little it is better not "
                "to drive oneself but to use public transport or a "
                "substitute-driver service."),
        PARAGRAPH("{음주운전}이란 술을 마신 후 {정상적}인 상태로 {회복되기|회복되다} 이전에 운전하는 행위를 "
                  "말한다. 음주운전을 한 경우에는 사고가 발생하지 않았어도 {도로교통법} {위반}으로 처벌을 "
                  "받는다. 음주운전은 음주운전을 한 사람뿐만 아니라 다른 운전자와 {보행자}의 생명까지 "
                  "{위협하는|위협하다} 행위이기 때문에 법으로 {강력하게|강력하다} {규제하고|규제하다} 있다."),
        PARAGRAPH("음주운전을 하다가 {적발되면|적발되다} 운전자는 많게는 5년 이하의 {징역}에 "
                  "{처해지거나|처해지다} 2천만 원 이하의 벌금을 내야 한다. 음주운전으로 인해 사람이 다치거나 "
                  "{사망할|사망하다} 경우 처벌은 더욱 {강해진다|강해지다}. {교통경찰}이 운전자에게 {음주 "
                  "측정}을 요구할 때 이를 {거부하는|거부하다} 것만으로도 처벌을 받을 수 있으니 반드시 측정에 "
                  "{응해야|응하다} 한다. 술을 조금이라도 마셨다면 직접 운전하지 말고 대중교통이나 "
                  "{대리운전} 서비스를 이용하는 것이 좋다."),
        FIGURE("교통경찰의 음주 측정"),

        GLOSSARY(("모욕", "깔보고 욕되게 함", "모욕", "insult, to offend"),
                 ("따돌림", "누군가를 떼어놓거나 멀리 함", "따돌림", "being ostracised")),
        HEADING(2, "학교폭력", translation=
                "Violence at school" "\n\n"
                "Violence at school means acts inside or outside school, "
                "directed at a pupil, that cause physical, mental or "
                "financial harm. Where it occurs, help can be had through the "
                "school, the National Police Agency, the Ministry of "
                "Education, the Ministry of Gender Equality and Family and "
                "others." "\n\n"
                "Where physical assault, insult by word or deed, "
                "ostracisation, taking money or belongings away, or cyber "
                "violence through a group chat or messages occurs, one should "
                "first tell a teacher at the school or one’s parents. Where "
                "more urgent help is needed, ringing 117 with no area code "
                "connects one straight to the police agency’s school violence "
                "centre. One can also report it to the police agency’s cyber "
                "bureau (http://cyberbureau.police.go.kr/) and receive the "
                "guidance and support needed."),
        PARAGRAPH("{학교폭력}이란 학교 {안팎}에서 학생을 {대상}으로 한 {신체적}, 정신적, {재산상} 피해를 "
                  "주는 행위이다. 학교폭력이 발생했을 경우에는 학교, {경찰청}, {교육부}, {여성가족부} 등을 "
                  "통해 도움을 받을 수 있다."),
        PARAGRAPH("신체적 {폭행}, 언어나 행동을 통한 {모욕}, {따돌림}, 돈이나 물건을 {빼앗아|빼앗다} 가는 "
                  "행동, {단체 채팅방}이나 문자 등을 통한 {사이버 폭력} 등이 발생하면 우선 학교 {교사}나 "
                  "부모에게 알려야 한다. 보다 긴급한 도움이 필요할 경우에는 국번 없이 117로 전화하면 경찰청 "
                  "학교폭력센터로 바로 {연결되어|연결되다} 도움을 받을 수 있다. 또한, 경찰청 {사이버 "
                  "안전국}(http://cyberbureau.police.go.kr/)에 신고하여 필요한 안내와 지원을 받을 수도 "
                  "있다."),
        FIGURE("학교폭력"),
        MARGIN("▶ 학교폭력 예방 교육 및 전화·문자 상담",
               "교육부, 여성가족부, 경찰청 117",
               "청소년 사이버상담센터 1388"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "몰래카메라도 범죄예요", translation=
                "A hidden camera is a crime too" "\n\n"
                "몰래카메라 means a camera used to film someone’s body or "
                "actions secretly, without their consent, or the act of "
                "filming secretly. Installing a small camera out of sight, or "
                "filming unlawfully with a smartphone camera, is a grave "
                "crime that invades another’s privacy and is heavily "
                "punished. A hidden-camera offence carries up to seven years’ "
                "imprisonment — being shut in prison — or a fine of up to "
                "fifty million won under the Act on Special Cases Concerning "
                "the Punishment of Sexual Crimes."),
        PARAGRAPH("{몰래카메라}는 상대방의 {동의}를 받지 않고 몰래 상대방의 몸이나 행동을 "
                  "{촬영하기|촬영하다} 위해 사용하는 카메라 또는 몰래 촬영하는 행위를 말한다. 사람들의 눈에 "
                  "잘 {띄지|띄다} 않는 곳에 몰래 {소형} 카메라를 {설치하거나|설치하다} 스마트폰 카메라를 "
                  "이용하여 {불법} 촬영하는 것은 다른 사람의 {사생활}을 {침해하는|침해하다} 심각한 범죄로서 "
                  "무거운 처벌을 받는다. 몰래카메라 범죄는 {성폭력범죄}의 처벌 등에 관한 법에 따라 7년 이하의 "
                  "징역(감옥에 갇히는 것)이나 5천만 원 이하의 {벌금형}에 {처해진다|처해지다}."),
        FIGURE("나무에 설치된 몰래카메라"),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 경범죄에는 무엇이 있을까?"),
        BULLET("( 경범죄 )란 중대한 범죄와 달리, 일상생활에서 흔히 일어날 수 있는 비교적 가벼운 위법 행위를 "
               "가리킨다."),
        BULLET("쓰레기 ( 무단투기 )는 종량제봉투를 사용하지 않거나 정해진 장소가 아닌 곳에 버리는 행위이다."),
        BULLET("교통 신호를 지키지 않고 도로를 가로질러 가거나 횡단보도가 아닌 곳에서 도로를 가로질러 가는 "
               "( 무단횡단 )은 자신과 타인을 위험하게 하는 행위이다."),
        HEADING(3, "02 음주운전과 학교폭력은 무엇일까?"),
        BULLET("( 음주운전 )이란 술을 마신 후 정상적인 상태로 회복하기 이전에 운전하는 행위이다. 음주운전을 "
               "하다가 적발되면 강력한 처벌을 받게 된다."),
        BULLET("( 학교폭력 )이란 학교 안팎에서 학생을 대상으로 한 신체적, 정신적, 재산상의 피해를 주는 "
               "행위이다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "베를린 장벽에 그린 그림, 예술일까? 낙서일까?", translation=
                "A picture drawn on the Berlin Wall: art, or graffiti?" "\n\n"
                "A piece of the German ‘Berlin Wall’ is on show at "
                "Cheonggyecheon in Seoul. The city of Berlin gave the piece "
                "of the actual wall to Seoul as a gift, in the hope of "
                "Korea’s unification (2005). One day in 2018, though, A, an "
                "artist who does graffiti — leaving pictures or writing on "
                "walls or in public places with spray or paint — sprayed "
                "graffiti on this piece of the Berlin Wall and then "
                "photographed it and posted it on their social media. The "
                "court held that since the piece of the Berlin Wall is a "
                "historic symbol of the close relationship between Korea and "
                "Germany, doing graffiti on it amounted to a crime, and "
                "ordered a fine of five million won."),
        PARAGRAPH("서울 청계천에는 독일 ‘{베를린 장벽}’의 일부 {조각}이 {전시되어|전시되다} 있다. 이 베를린 "
                  "장벽 조각은 한국의 {통일}을 바란다는 의미에서 독일 베를린시가 실제 장벽의 일부를 서울시에 "
                  "선물로 준 것이다(2005년). 그런데 {그라피티}(스프레이나 페인트 등으로 공공장소 또는 벽에 "
                  "그림, 글자 등을 남기는 것) 작가인 A씨가 2018년 어느 날 이 베를린 장벽 조각에 스프레이로 "
                  "그라피티를 하고 나서 자신의 소셜 미디어에 사진으로 찍어 올렸다. {법원}은 베를린 장벽 조각은 "
                  "한국과 독일의 {친밀한|친밀하다} 관계를 보여주는 역사적인 {상징물}이므로 여기에 그라피티를 "
                  "한 것은 범죄에 해당한다고 보고 벌금 500만 원을 내도록 했다."),
        FIGURE("훼손된 베를린 장벽"),
        PARAGRAPH("★ 한국의 공공장소에 그려진 그림이나 글씨를 다른 나라(자신의 고향 나라 포함)의 것과 비교해 "
                  "보면 어떤 공통점과 차이점을 찾을 수 있습니까?",
                  "Comparing the pictures and writing on public places in "
                  "Korea with those of other countries, your home country "
                  "among them, what do they have in common and how do they "
                  "differ?"),
    ],

    extraAnnotations={
        "장점": dict(
            hanja="長點", meaning="a strong point, an advantage",
            characters=[("長", "장", "long, good at — as in 장기, 특장"),
                        ("點", "점", "a point — as in 시점, 요점")],
        ),
        "단점": dict(
            hanja="短點", meaning="a weak point, a drawback",
            characters=[("短", "단", "short — as in 단기, 단축"),
                        ("點", "점", "a point")],
        ),
        "경범죄": dict(
            hanja="輕犯罪", meaning="a minor offence, a misdemeanour",
            characters=[("輕", "경", "light — as in 경공업, 경상"),
                        ("犯罪", None, "a crime")],
        ),
        "개념": dict(
            hanja="槪念", meaning="a concept, what something means",
            characters=[("槪", "개", "general, outline — as in 개요"),
                        ("念", "념", "a thought — as in 이념, 개념")],
        ),
        "사례": dict(
            hanja="事例", meaning="a case, an example",
            characters=[("事", "사", "a matter — as in 사건, 사업"),
                        ("例", "례", "an example — as in 예를 들어, 사례")],
        ),
        "음주 운전": dict(
            hanja="飮酒運轉", meaning="drink-driving",
            characters=[("飮", "음", "to drink — as in 음료, 음식"),
                        ("酒", "주", "alcohol — as in 소주, 맥주"),
                        ("運轉", None, "driving")],
        ),
        "학교 폭력": dict(
            hanja="學校暴力", meaning="violence at school",
            characters=[("暴力", None, "violence — 暴 violent, 力 force")],
        ),
        "범죄": dict(
            hanja="犯罪", meaning="a crime",
            characters=[("犯", "범", "to violate — as in 범인, 방범"),
                        ("罪", "죄", "guilt — as in 유죄, 무죄")],
        ),
        "살인": dict(
            hanja="殺人", meaning="murder",
            characters=[("殺", "살", "to kill — as in 살해, 자살"),
                        ("人", "인", "person")],
        ),
        "강도": dict(
            hanja="强盜", meaning="robbery; a robber",
            characters=[("强", "강", "strong — as in 강제, 강력"),
                        ("盜", "도", "to steal — as in 절도, 도난")],
        ),
        "폭행": dict(
            hanja="暴行", meaning="assault",
            characters=[("暴", "폭", "violent — as in 폭력, 폭죽"),
                        ("行", "행", "to act — as in 행위, 행동")],
        ),
        "중대하다": dict(
            hanja="重大하다", meaning="to be grave, serious",
            characters=[("重", "중", "heavy — as in 중요, 존중"),
                        ("大", "대", "great — as in 대규모, 대학")],
            surfaces=["중대한"],
        ),
        "떠올리다": dict(
            meaning="to call to mind, to think of",
            surfaces=["떠올린다"],
        ),
        "사소하다": dict(
            hanja="些少하다", meaning="to be trivial, slight",
            characters=[("些", "사", "a little, some"),
                        ("少", "소", "few, little — as in 소수, 청소년")],
            surfaces=["사소한"],
        ),
        "행위": dict(
            hanja="行爲", meaning="an act, conduct",
            characters=[("行", "행", "to act — as in 행동, 시행"),
                        ("爲", "위", "to do, for — as in 위하다")],
        ),
        "공공질서": dict(
            hanja="公共秩序", meaning="public order",
            characters=[("公共", None, "public"),
                        ("秩序", None, "order")],
        ),
        "제재": dict(
            hanja="制裁", meaning="a sanction, a restriction imposed",
            characters=[("制", "제", "to control — as in 제도, 규제"),
                        ("裁", "재", "to judge, cut — as in 재판, 중재")],
        ),
        "해당하다": dict(
            hanja="該當하다", meaning="to count as, to fall under",
            surfaces=["해당하기"],
        ),
        "뱉다": dict(meaning="to spit out", surfaces=["뱉거나"]),
        "순서": dict(
            hanja="順序", meaning="one’s turn; order, sequence",
            characters=[("順", "순", "in order, obedient — as in 순찰, 순위"),
                        ("序", "서", "sequence — as in 질서")],
        ),
        "새치기하다": dict(
            meaning="to cut in line, to push in",
            surfaces=["새치기하는"],
        ),
        "저지르다": dict(
            meaning="to commit (an offence)",
            surfaces=["저지르는"],
        ),
        "위법": dict(
            hanja="違法", meaning="unlawful, breaking the law",
            characters=[("違", "위", "to violate — as in 위반, 위법"),
                        ("法", "법", "law")],
        ),
        "전염병": dict(
            hanja="傳染病", meaning="a contagious disease",
            characters=[("傳", "전", "to transmit — as in 전달, 전통"),
                        ("染", "염", "to be infected — as in 감염, 오염"),
                        ("病", "병", "illness")],
        ),
        "안전수칙": dict(
            hanja="安全守則", meaning="safety rules",
            characters=[("安全", None, "safety"),
                        ("守則", None, "rules to keep — 守 to guard, 則 rule")],
        ),
        "자가 격리": dict(
            hanja="自家隔離", meaning="self-isolation",
            characters=[("自家", None, "one’s own home"),
                        ("隔離", None, "isolation — 隔 to separate, 離 to part")],
        ),
        "어기다": dict(meaning="to break (a rule), to go against",
                     surfaces=["어길"]),
        "처벌": dict(
            hanja="處罰", meaning="punishment",
            characters=[("處", "처", "to handle — as in 처분, 처우"),
                        ("罰", "벌", "penalty — as in 벌금, 형벌")],
        ),
        "함부로": dict(
            meaning="carelessly, as one pleases",
            notes=["Chapter 33 has it of treating family carelessly; here of "
                   "leaving isolation."],
        ),
        "벗어나다": dict(
            meaning="to get out of, to leave",
            surfaces=["벗어난"],
        ),
        "벌금": dict(
            hanja="罰金", meaning="a fine (a criminal penalty)",
            characters=[("罰", "벌", "penalty — the same 罰 as in 처벌"),
                        ("金", "금", "money")],
            notes=["A 벌금 is imposed as a punishment; a 과태료 is for "
                   "neglecting a duty."],
        ),
        "강제 출국": dict(
            hanja="强制出國", meaning="being made to leave the country",
            notes=["Chapter 30’s 강제퇴거 by another name."],
        ),
        "종량제 봉투": dict(
            hanja="從量制封套", meaning="the standard rubbish bag",
            characters=[("從量制", None, "pay-by-volume — 從 according to, "
                                        "量 quantity, 制 system"),
                        ("封套", None, "a bag, an envelope")],
        ),
        "과태료": dict(
            hanja="過怠料", meaning="a fine for neglecting a duty",
            characters=[("過", "과", "fault — as in 과실, 초과"),
                        ("怠", "태", "idleness, neglect"),
                        ("料", "료", "a charge — as in 수수료, 위자료")],
        ),
        "담배꽁초": dict(meaning="a cigarette butt"),
        "휴지": dict(
            hanja="休紙", meaning="waste paper; tissue",
            characters=[("休", "휴", "to rest — as in 휴가, 휴식"),
                        ("紙", "지", "paper — as in 종이, 신문지")],
        ),
        "묻다": dict(meaning="to bury", surfaces=["묻어서"]),
        "무단투기": dict(
            hanja="無斷投棄", meaning="fly-tipping, dumping rubbish unlawfully",
            characters=[("無斷", None, "without leave — 無 without, 斷 to decide"),
                        ("投棄", None, "to throw away — 投 to throw, 棄 to discard")],
        ),
        "신고 포상금제": dict(
            hanja="申告褒賞金制", meaning="the reward-for-reporting scheme",
            characters=[("褒賞", None, "a reward — 褒 to praise, 賞 a prize")],
        ),
        "횡단보도": dict(
            hanja="橫斷步道", meaning="a pedestrian crossing",
            characters=[("橫斷", None, "crossing — 橫 across, 斷 to cut"),
                        ("步道", None, "a footpath — 步 to walk, 道 way")],
        ),
        "신호등": dict(
            hanja="信號燈", meaning="a traffic light",
            characters=[("信號", None, "a signal — 信 trust, 號 sign"),
                        ("燈", "등", "a lamp — as in 전등, 등불")],
        ),
        "신호": dict(hanja="信號", meaning="a signal"),
        "무시하다": dict(
            hanja="無視하다", meaning="to ignore, to disregard",
            characters=[("無", "무", "without — as in 무효, 무단"),
                        ("視", "시", "to look at — as in 시청, 중시")],
            surfaces=["무시하고"],
        ),
        "범칙금": dict(
            hanja="犯則金", meaning="a fine for a traffic offence",
            characters=[("犯", "범", "to violate"),
                        ("則", "칙", "rule — as in 원칙, 규칙"),
                        ("金", "금", "money")],
        ),
        "위험하다": dict(
            hanja="危險하다", meaning="to be dangerous",
            characters=[("危", "위", "danger — as in 위기, 위협"),
                        ("險", "험", "steep, risky — as in 보험, 험난")],
            surfaces=["위험하게"],
        ),
        "건널목": dict(
            meaning="a crossing (where a road meets a railway)",
        ),
        "철도": dict(
            hanja="鐵道", meaning="a railway",
            characters=[("鐵", "철", "iron — as in 철강, 지하철"),
                        ("道", "도", "a way — as in 도로, 인도")],
        ),
        "무단횡단": dict(
            hanja="無斷橫斷", meaning="jaywalking",
            characters=[("無斷", None, "without leave"),
                        ("橫斷", None, "crossing")],
        ),
        "승용차": dict(
            hanja="乘用車", meaning="a passenger car",
            characters=[("乘", "승", "to ride — as in 승객, 승차"),
                        ("用", "용", "to use — as in 사용, 이용"),
                        ("車", "차", "a vehicle — as in 자동차, 차량")],
        ),
        "고속버스": dict(
            hanja="高速버스", meaning="an express coach",
            characters=[("高速", None, "high speed — 高 high, 速 fast")],
        ),
        "승객": dict(
            hanja="乘客", meaning="a passenger",
            characters=[("乘", "승", "to ride — the same 乘 as in 승용차"),
                        ("客", "객", "a guest — as in 관광객, 고객")],
        ),
        "안전띠": dict(meaning="a seat belt", notes=["Also 안전벨트."]),
        "운전석": dict(
            hanja="運轉席", meaning="the driver’s seat",
            characters=[("運轉", None, "driving"),
                        ("席", "석", "a seat — as in 좌석, 참석")],
        ),
        "조수석": dict(
            hanja="助手席", meaning="the front passenger seat",
            characters=[("助手", None, "an assistant — 助 to help, 手 hand"),
                        ("席", "석", "a seat")],
        ),
        "뒷좌석": dict(meaning="the back seat"),
        "영·유아": dict(
            hanja="嬰幼兒", meaning="infants and toddlers",
            notes=["Chapter 9’s 영아 and 유아 together."],
        ),
        "카시트": dict(meaning="a child car seat"),
        "음주운전": dict(
            hanja="飮酒運轉", meaning="drink-driving",
        ),
        "정상적": dict(
            hanja="正常的", meaning="normal",
            characters=[("正常", None, "normal — 正 right, 常 usual")],
        ),
        "회복되다": dict(
            hanja="回復되다", meaning="to return to normal, to recover",
            characters=[("回", "회", "to turn back — as in 회의, 회복"),
                        ("復", "복", "to restore — as in 복구, 복지")],
            surfaces=["회복되기"],
        ),
        "도로교통법": dict(
            hanja="道路交通法", meaning="the Road Traffic Act",
        ),
        "위반": dict(
            hanja="違反", meaning="a breach, a violation",
            characters=[("違", "위", "to violate — the same 違 as in 위법"),
                        ("反", "반", "against — as in 반대, 반발")],
        ),
        "보행자": dict(
            hanja="步行者", meaning="a pedestrian",
            characters=[("步行", None, "walking — 步 to step, 行 to go"),
                        ("者", "자", "person")],
        ),
        "위협하다": dict(
            hanja="威脅하다", meaning="to threaten, to endanger",
            characters=[("威", "위", "might — as in 위력, 권위"),
                        ("脅", "협", "to threaten — as in 협박")],
            surfaces=["위협하는"],
        ),
        "강력하다": dict(
            hanja="强力하다", meaning="to be strong, forceful",
            characters=[("强", "강", "strong — as in 강도, 강제"),
                        ("力", "력", "force — as in 노력, 능력")],
            surfaces=["강력하게"],
        ),
        "규제하다": dict(
            hanja="規制하다", meaning="to regulate, to control",
            characters=[("規", "규", "rule — as in 규범, 규정"),
                        ("制", "제", "to control — as in 제재, 제도")],
            surfaces=["규제하고"],
        ),
        "적발되다": dict(
            hanja="摘發되다", meaning="to be caught, to be found out",
            characters=[("摘", "적", "to pick out, to point out"),
                        ("發", "발", "to reveal, send out — as in 발생, 발급")],
            surfaces=["적발되면"],
        ),
        "징역": dict(
            hanja="懲役", meaning="imprisonment with hard labour",
            characters=[("懲", "징", "to punish — as in 징계"),
                        ("役", "역", "service, duty — as in 병역, 역할")],
        ),
        "처해지다": dict(
            hanja="處해지다", meaning="to be sentenced to, to be subject to",
            surfaces=["처해지거나", "처해진다"],
        ),
        "사망하다": dict(
            hanja="死亡하다", meaning="to die",
            characters=[("死", "사", "death — as in 사고, 사망자"),
                        ("亡", "망", "to perish, to flee")],
            surfaces=["사망할"],
        ),
        "강해지다": dict(meaning="to become stronger, harsher",
                       surfaces=["강해진다"]),
        "교통경찰": dict(
            hanja="交通警察", meaning="a traffic police officer",
        ),
        "음주 측정": dict(
            hanja="飮酒測定", meaning="a breath test",
            characters=[("測定", None, "measurement — 測 to measure, 定 to fix")],
        ),
        "거부하다": dict(
            hanja="拒否하다", meaning="to refuse",
            characters=[("拒", "거", "to refuse — as in 거절"),
                        ("否", "부", "no, not — as in 여부, 부정")],
            surfaces=["거부하는"],
        ),
        "응하다": dict(
            hanja="應하다", meaning="to comply, to respond to",
            characters=[("應", "응", "to answer — as in 응답, 호응")],
            surfaces=["응해야"],
        ),
        "대리운전": dict(
            hanja="代理運轉", meaning="a substitute-driver service",
            characters=[("代理", None, "acting for someone — 代 to replace, "
                                       "理 to manage")],
            notes=["Chapter 3’s 대리운전기사 drives your car home for you."],
        ),
        "학교폭력": dict(
            hanja="學校暴力", meaning="violence at school",
        ),
        "안팎": dict(meaning="inside and outside"),
        "대상": dict(
            hanja="對象", meaning="the object, the target (of an act)",
            characters=[("對", "대", "facing — as in 대하다, 대응"),
                        ("象", "상", "an image, a form — as in 인상, 현상")],
        ),
        "신체적": dict(
            hanja="身體的", meaning="physical, of the body",
        ),
        "재산상": dict(
            hanja="財産上", meaning="in terms of property, financial",
        ),
        "경찰청": dict(
            hanja="警察廳", meaning="the National Police Agency",
            characters=[("警察", None, "the police"),
                        ("廳", "청", "an agency — as in 시청, 구청")],
        ),
        "교육부": dict(
            hanja="敎育部", meaning="the Ministry of Education",
        ),
        "여성가족부": dict(
            hanja="女性家族部",
            meaning="the Ministry of Gender Equality and Family",
        ),
        "모욕": dict(
            hanja="侮辱", meaning="an insult",
            characters=[("侮", "모", "to slight, to look down on"),
                        ("辱", "욕", "to disgrace — as in 욕설")],
        ),
        "따돌림": dict(
            meaning="being ostracised, being frozen out",
            notes=["집단 따돌림 is bullying by a group; 왕따 is the everyday word."],
        ),
        "빼앗다": dict(meaning="to take away by force", surfaces=["빼앗아"]),
        "단체 채팅방": dict(
            hanja="團體채팅房", meaning="a group chat",
        ),
        "사이버 폭력": dict(meaning="cyber violence, online abuse"),
        "교사": dict(
            hanja="敎師", meaning="a teacher",
            characters=[("敎", "교", "to teach — as in 교육, 교실"),
                        ("師", "사", "a master, a teacher — as in 강사, 의사")],
        ),
        "연결되다": dict(
            hanja="連結되다", meaning="to be connected, put through",
            characters=[("連", "련", "to link — as in 연락, 연속"),
                        ("結", "결", "to tie — as in 결혼, 결과")],
            surfaces=["연결되어"],
        ),
        "사이버 안전국": dict(
            meaning="the police agency’s cyber bureau",
        ),
        "몰래카메라": dict(
            meaning="a hidden camera; filming someone secretly",
            notes=["몰래 “secretly”. Also called 몰카."],
        ),
        "동의": dict(
            hanja="同意", meaning="consent",
            characters=[("同", "동", "same — as in 동등, 동일"),
                        ("意", "의", "intention — as in 의사, 합의")],
        ),
        "촬영하다": dict(
            hanja="撮影하다", meaning="to film, to photograph",
            characters=[("撮", "촬", "to take (a photograph)"),
                        ("影", "영", "a shadow, an image — as in 영화, 영상")],
            surfaces=["촬영하기"],
        ),
        "띄다": dict(meaning="to catch the eye, to be noticeable",
                   surfaces=["띄지"]),
        "소형": dict(
            hanja="小型", meaning="small, compact",
            characters=[("小", "소", "small — as in 소규모, 축소"),
                        ("型", "형", "a form, a model — as in 유형, 형태")],
        ),
        "설치하다": dict(
            hanja="設置하다", meaning="to install, to set up",
            characters=[("設", "설", "to establish — as in 시설, 설립"),
                        ("置", "치", "to place — as in 조치, 위치")],
            surfaces=["설치하거나"],
        ),
        "불법": dict(
            hanja="不法", meaning="unlawful, illegal",
        ),
        "사생활": dict(
            hanja="私生活", meaning="private life, privacy",
            characters=[("私", "사", "private — as in 사립, 사적"),
                        ("生活", None, "life, living")],
        ),
        "침해하다": dict(
            hanja="侵害하다", meaning="to invade, to violate",
            characters=[("侵", "침", "to encroach — as in 침입, 침략"),
                        ("害", "해", "harm — as in 피해, 손해")],
            surfaces=["침해하는"],
        ),
        "성폭력범죄": dict(
            hanja="性暴力犯罪", meaning="a sexual violence offence",
        ),
        "벌금형": dict(
            hanja="罰金刑", meaning="a sentence of a fine",
            characters=[("刑", "형", "a punishment — as in 형벌, 형법")],
        ),
        "베를린 장벽": dict(
            meaning="the Berlin Wall",
            notes=["장벽 = 障壁, a barrier wall."],
        ),
        "조각": dict(
            meaning="a piece, a fragment; a sculpture",
        ),
        "전시되다": dict(
            hanja="展示되다", meaning="to be exhibited, put on show",
            characters=[("展", "전", "to spread out — as in 발전, 전개"),
                        ("示", "시", "to show — as in 제시, 표시")],
            surfaces=["전시되어"],
        ),
        "통일": dict(
            hanja="統一", meaning="unification",
            characters=[("統", "통", "to unite, govern — as in 통치, 전통"),
                        ("一", "일", "one")],
        ),
        "그라피티": dict(
            meaning="graffiti",
            notes=["The page glosses it as leaving pictures or letters on a "
                   "public place or a wall with spray or paint."],
        ),
        "법원": dict(
            hanja="法院", meaning="a court",
            characters=[("法", "법", "law"),
                        ("院", "원", "an institution — as in 병원, 대법원")],
        ),
        "친밀하다": dict(
            hanja="親密하다", meaning="to be close, intimate",
            characters=[("親", "친", "close, kin — as in 친척, 친구"),
                        ("密", "밀", "dense, close — as in 밀집, 비밀")],
            surfaces=["친밀한"],
        ),
        "상징물": dict(
            hanja="象徵物", meaning="a symbol, a symbolic object",
            characters=[("象徵", None, "a symbol — chapter 1’s subject"),
                        ("物", "물", "a thing — as in 물건, 인물")],
        ),
    },

    extraNotes=[
        "The recycling bins on p. 182, the standard-bag photograph and the "
        "breath-test photograph on pp. 183-184, the school violence "
        "photograph, the hidden camera and the damaged Berlin Wall on p. 185 "
        "are not reproduced; their captions are.",
        "The review answers on p. 185 are the ones you wrote in the margin — "
        "경범죄, 무단투기, 음주운전, 학교폭력 — with 무단횡단 taken from the article "
        "for the gap you left. The page keeps them covered until asked for.",
    ],
)
