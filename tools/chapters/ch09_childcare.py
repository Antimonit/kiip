# -*- coding: utf-8 -*-
"""Chapter 9 — Childcare.

Transcribed in your Google Doc (9.html), whose text is carried in `blocks`
below as the Doc had it. First transcribed from the photos of pp. 48-51; the
two readings were compared line by line when your Doc arrived, and every
difference proved to be a slip in the Doc, listed as fixes below.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, FIGURE, MARGIN, TABLE,
               CELL, GLOSSARY)

CHAPTER = dict(
    number=9, slug="09-childcare",
    unit="교육", title="보육 제도", titleEn="Childcare",

    blocks=[
        SECTION("warmup", "생각해 봅시다"),
        MARGIN("{영아} 0-2세", "{유아} 3-5세"),
        PARAGRAPH("다음은 한국의 출산 및 보육 제도 관련 사진입니다."),
        FIGURE("임신한 여성의 모습 · 갓 태어난 아기의 모습 · 어린이집에서 노는 모습 · 유치원에서 함께 식사하는 " "모습"),
        HEADING(4, "01 한국에서 본인이나 주변의 가족(지인)이 이와 같은 상황과 관련하여 어떤 지원을 받았습니까?"),
        HEADING(4, "02 자신의 고향 나라에서 임신, 출산, 보육과 관련하여 이루어지고 있는 지원에 대해 말해 봅시다."),
        SECTION("goals", "학습목표"),
        BULLET("한국의 임신 출산 및 보육 제도에 대하여 알 수 있다.", ordered=True),
        BULLET("한국의 영유아 보육·교육기관에 대하여 알 수 있다.", ordered=True),
        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"], [["심화", "국민",
              "4. 대한민국 국민을 위한 복지", "사회보험"]]),
        SECTION("part", "01 출산과 보육을 지원하는 제도에는 무엇이 있을까?"),
        GLOSSARY(("국민행복카드", "임신확인서를 가지고 가까운 은행에 가도 되고 인터넷이나 전화로도 발급받을 수 있다.",
              "국민행복카드"),
              ("산전", "아이를 낳기 전", "산전"),
              ("임산부 교육프로그램", "모유 수유 교실, 임산부 체조 교실, 출산 준비 교실, 아기 마사지 교실 등",
              "임산부 교육프로그램"),
              ("보육", "아이를 보살피고 돌봄", "보육")),
        HEADING(2, "출산을 지원하는 제도", translation="Systems that Support Childbirth" "\n\n"
          "Korea supports the costs needed for pregnancy, childbirth, "
          "and childcare in order to encourage childbirth and reduce "
          "the economic burden of raising children. Once pregnant, "
          "the government supports part of the costs needed for a "
          "pregnant woman's health management and childbirth through "
          "the 'National Happiness Card.'" "\n\n"
          "Pregnant women can also receive health center services — "
          "all pregnant women (including marriage immigrants) can "
          "receive free prenatal checkups just by registering at a "
          "health center, and can receive nutritional supplements "
          "needed during pregnancy. Beyond this, there are various "
          "services and pregnant-women's education programs offered "
          "depending on each region's health center. After "
          "childbirth, each local government also provides childbirth "
          "support funds or childbirth congratulatory money, and "
          "detailed information can be found by inquiring at the city "
          "hall, district office, or county office."),
        PARAGRAPH("한국은 출산을 {장려하}고 {양육}에 대한 {경제}적 부담을 줄여주기 위해 임신, 출산, 양육에 필요한 "
          "비용을 지원하고 있다. 임신을 하게 되면 정부에서 임산부의 건강 관리와 출산에 필요한 비용의 일부를 "
          "‘국민행복카드’를 통해 지원한다."),
        PARAGRAPH("{임산부}를 위한 보건소 서비스도 받을 수 있는데 모든 임산부(결혼 이민자 포함)는 보건소에 등록하기만 "
          "하면 무료 산전검사를 받을 수 있으며 임신 중에 필요한 {영양제}를 받을 수 있다. 그 외에도 각 지역의 "
          "보건소에 따라 지원하는 서비스와 임산부 교육프로그램이 다양하게 있다. 출산 후에는 각 지방 자치 단체별로 "
          "출산 지원금이나 출산 축하금을 지원하기도 하는데 상세한 사항은 시청, 구청, 군청에 문의하면 알 수 " "있다."),
        HEADING(2, "보육과 유아 교육을 지원하는 제도", translation=
          "Systems Supporting Childcare and Early Childhood Education" "\n\n"
          "Childcare fees or preschool tuition are supported for "
          "citizens' infant/toddler children (ages 0 to 5 and under) "
          "attending daycare centers or kindergartens before entering "
          "elementary school. You can apply for the 'Children's "
          "Happiness Card' at a bank, online, or by phone, and use "
          "this card to pay for daycare center childcare fees or "
          "kindergarten tuition." "\n\n"
          "The support amount differs depending on the child's age or "
          "the type of institution (daycare center vs. kindergarten). "
          "Even if a child isn't sent to a daycare center or "
          "kindergarten and is raised at home instead, a childcare "
          "allowance is provided depending on the child's age." "\n\n"
          "Besides supporting childcare fees or the childcare "
          "allowance, since September 2018 the government has also "
          "been paying a child allowance in order to reduce the "
          "economic burden of raising children and to promote (증진) "
          "children's rights and welfare. The child allowance is "
          "provided to households with a child under 7 years old."),
        GLOSSARY(("증진", "기운이나 세력이 점점 더 늘어 가고 나아감", "증진")),
        PARAGRAPH("초등학교에 입학하기 전 어린이집이나 유치원을 다니는 국민의 영·유아(0~만 5세 이하) 자녀를 대상으로 "
          "{보육비}나 유아 학비가 지원된다. 은행을 방문하거나 인터넷, 전화로 ‘아이행복카드’를 신청하고 이 "
          "카드로 어린이집 보육비나 유치원 유아 학비를 결제할 수 있다."),
        PARAGRAPH("자녀의 나이나 기관의 {유형}(어린이집, 유치원)에 따라 지원 금액이 다르다. 어린이집이나 유치원을 "
          "이용하지 않고 집에서 {양육하}는 경우에도 자녀의 {연령}에 따라 양육 {수당}이 지원되고 있다."),
        PARAGRAPH("정부에서는 보육료나 양육 수당 지원 외에도 2018년 9월부터 아동 양육에 따른 경제적 부담을 줄이고 "
          "아동의 권리와 복지 증진을 위해 아동 수당을 지급하고 있다. 아동 수당은 만 7세 미만 아동이 있는 "
          "가정에 지원하고 있다."),
        FIGURE("보육 기관 보육료를 아이행복카드로 결제할 수 있다."),
        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "맞벌이, 출장이나 야근 등으로 급한 돌봄이 필요하다면?"),
        PARAGRAPH("정부에서는 부모의 맞벌이 등으로 양육 공백이 발생하는 가정의 만 12세 이하의 아동을 대상으로 아이 "
          "돌보미가 찾아가는 돌봄 서비스를 제공하고 있다. 부모의 출장이나 야근 등으로 일시적인 돌봄이 필요할 "
          "경우, 아동의 질병으로 인해 보육 시설 이용이 어려운 경우에도 돌봄 서비스를 제공한다. 이를 통해 아동을 "
          "안전하게 보호하고 부모의 일과 가정 생활이 균형을 이룰 수 있도록 지원한다. 서비스 신청은 아이 돌봄 "
          "지원 사업 누리집(https://dolbom.go.kr)에서 가능하다."),
        SECTION("part", "02 영·유아를 위한 보육과 교육은 어디에서 담당할까?"),
        HEADING(2, "어린이집", translation="Daycare Centers" "\n\n"
          "Daycare centers (어린이집) handle childcare and education for "
          "infants and toddlers from age 0 up to before elementary "
          "school entry (age 5), and are childcare institutions "
          "designated by the Ministry of Health and Welfare (보건복지부). "
          "Types include: national/public daycare centers (국·공립 어린이집) "
          "established by the government or local governments, "
          "private daycare centers (사립 어린이집) established by private "
          "individuals, workplace daycare centers (직장 어린이집) intended "
          "for company employees' children, daycare centers "
          "established by religious organizations such as churches or "
          "Catholic parishes, and home daycare centers (가정 어린이집) "
          "where infants/toddlers are cared for in an ordinary " "household."
          "\n\n" "Daycare center hours operate as 'basic childcare' (기본 보육) "
          "from 9 a.m. to 4 p.m., and 'extended childcare' (연장 보육) "
          "from 4 p.m. to 7:30 p.m. — the homeroom teacher is in "
          "charge of the basic childcare class, and a dedicated "
          "extended-childcare teacher (연장 보육 전담 교사) is in charge of "
          "the extended childcare class. Depending on the "
          "institution, childcare services may also be offered such "
          "as 24-hour childcare, where both daytime childcare "
          "(07:30–19:30) and nighttime childcare (19:30–07:30 the "
          "next day) are provided, holiday childcare, and hub-based "
          "nighttime childcare (거점형 야간 보육)."),
        GLOSSARY(("연장", "시간이나 길이를 늘림", "연장"),
              ("전담", "전문적으로 맡음", "전담"),
              ("거점", "어떤 활동의 근거가 되는 중요한 지점", "거점")),
        PARAGRAPH("어린이집은 0세부터 초등학교 입학 전(만 5세)까지의 영·유아의 보육과 교육을 담당하며 {보건복지부}에서 "
          "지정한 보육 기관이다. 정부나 지방 자치 단체에서 {설립한} 국·공립 어린이집, 민간인이 설립한 {사립} "
          "어린이집, 회사의 직원 자녀를 대상으로 하는 직장 어린이집, 교회나 성당 등과 같은 종교 단체에서 "
          "{세운} 어린이집, 일반 {가정}에서 영·유아를 {돌보는}가정 어린이집 등이 있다."),
        PARAGRAPH("어린이집 보육 시간은 오전 9시부터 오후 4시까지의 ‘기본 보육’과 오후 4시부터 오후 7시 30분까 "
          "‘연장 보육’으로 운영되며 ‘{기본 보육반}’은 {담임 교사가|담임} ‘연장 보육반’은 연장 보육 "
          "전담교사가 담당한다. 기관에 따라 주간 보육(07:30~19:30)과 야간 "
          "보육(19:30~익일07:30)이 모두 이루어지는 24시간 보육, 휴일 보육, 거점형 야간 보육 등의 "
          "보육 서비스 지원하기도 한다."),
        HEADING(2, "유치원", translation="Kindergarten" "\n\n"
          "Kindergarten (유치원) is an educational institution handling "
          "the education of young children from age 3 up to before "
          "elementary school entry (age 5), and falls under the "
          "jurisdiction of the Ministry of Education. There are "
          "national/public kindergartens (국·공립 유치원) established by "
          "the government or local governments, and private "
          "kindergartens (사립 유치원) established by individuals, "
          "corporations, or religious organizations. They generally "
          "operate from around 9 a.m. to 2 p.m. on weekdays, and for "
          "the children of dual-income parents, an all-day class "
          "(종일반) may also run from around 7 a.m. to 8 p.m." "\n\n"
          "Kindergarten tuition is generally cheaper at "
          "national/public kindergartens than at private ones. "
          "Because of this, parents wanting to send their children to "
          "a national/public kindergarten often have to wait a long "
          "time after applying."),
        GLOSSARY(("관할", "일정한 권한을 가지고 통제 하거나 지배함", "관할"),
              ("법인", "법적으로 권리와 의무를 가지는 조직", "법인")),
        PARAGRAPH("유치원은 만 3세부터 초등학교 입학 전(만 5세)까지의 유아의 교육을 담당하는 교육 기관으로 교육부의 "
          "관할 아래 있다. 정부나 지방 자치 단체에서 설립한 국·공립 유치원과 개인이나 법인, 종교단체가 설립한 "
          "사립 유치원이 있다. 보통 평일 오전 9시~오후 2시 정도까지 운영 되며, 맞벌이 부모의 자녀를 위하여 "
          "오전 7시~오후 8시 정도까지 종일반이 운영되기도 한다."),
        PARAGRAPH("유치원 교육비는 일반적으로 국·공립이 사립보다 저렴한 편이다. 그래서 국·공립 유치원에 자녀를 보내려면 "
          "신청을 한 이후에 오랫동안 기다려야 하는 경우가 많다."),
        FIGURE("어린이집이나 유치원에서 실시하는 여러 가지 활동"),
        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "야간 돌봄 서비스를 제공하는 24시간 어린이집"),
        PARAGRAPH("24시간 어린이집은 부모의 야간 경제 활동, 한 부모 또는 조손가정 등의 불가피한 경우 24시간 "
          "동안(07:30~다음날 07:30) 보육 서비스를 제공한다. 자녀를 24시간 어린이집에 보냈다 하더라도 "
          "부모(보호자)는 최소한 주 3회 이상 아동과 전화 또는 방문 등의 방식으로 아동과 접촉해야 하고 최소한 "
          "주 1회 이상 아동을 가정에 데려가 보호해야 한다."),
        PARAGRAPH("이외에 야간 돌봄이 필요한 영유아들을 권역별로 지정된 거점형 이간보육 어린이집에서 전담 보육교사가 함께 "
          "돌봐주는 서비스도 있다. 서비스를 신청하면 오후 5시 이후 보육 교사 또는 보육 도우미가 주간 이용 "
          "어린이집에서 거점형 야간 보육 어린이집으로 아이를 데려와 돌봐주며 보호자는 거점형 야간보육 어린이집에 "
          "방문하여 아이를 데려오면 된다."),
        SECTION("review", "주요 내용정리"),
        HEADING(2, "01 출산과 보육을 지원하는 제도에는 무엇이 있을까?"),
        BULLET("임신을 하게 되면 정부에서 임산부의 건강 관리와 출산에 필요한 비용의 일부를 (   )를 통해 지원한다."),
        BULLET("(   )이나 (   )을 다니는 영·유아를 대상으로 보육비나 유아 학비가 (   )를 통해 지급된다."),
        BULLET("집에서 양육하는 경우에도 자녀의 연령에 따라 (   )이 지원된다."),
        HEADING(2, "02 영·유아를 위한 보육과 교육은 어디에서 담당할까?"),
        BULLET("(   )은 0세부터,만 5세까지 아이들의 보육과 교육을 담당하며 (   )에서 저정한 시설이다."),
        BULLET("(   )은 만 3세부터 초등학교 입학 전 만 (   )까지의 유아들이 다니는 교육부 관할 교육 " "기관이다."),
        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "태교와 산후조리 문화", translation="Taegyo and Postpartum Care Culture"
          "\n\n" "In Korea, it has traditionally been believed that a "
          "mother's mindset and behavior during pregnancy greatly "
          "affect the fetus (태아, \"the child in the womb\") "
          "emotionally, psychologically, and physically. So there is "
          "a tradition, in order to have a healthy child, of a "
          "pregnant woman being careful in everything, avoiding "
          "negative thoughts or rough behavior, and trying to speak "
          "and act with a peaceful mind — this is called 태교 "
          "(literally \"teaching the fetus\"). Reading good writing "
          "aloud to the fetus or playing it music also counts as part " "of 태교."
          "\n\n" "After giving birth, women undergo postpartum care (산후 조리). "
          "At this time, seaweed soup (미역국) is typically eaten. "
          "Seaweed, rich in nutrients, purifies the new mother's "
          "blood and helps breast milk flow well. What's eaten after "
          "childbirth differs by country. For example, in Vietnam, "
          "dishes of stir-fried chicken, shrimp, and beef, along with "
          "a vegetable called '사오옷' (probably referring to a specific "
          "Vietnamese herb — the romanization here is a bit unclear), "
          "are commonly eaten, which is said to help remove residue "
          "from inside the womb."),
        PARAGRAPH("한국에서는 임신 중 엄마의 마음과 {몸가짐}이 태아(뱃속의 아이)에게 {정서적}·{심리적}·{신체적}으로 "
          "영향을 많이 {미친다}고 생각해 왔다. 그래서 건강한 자녀를 얻기 위해서는 임신한 여성이 모든 일에 "
          "대해서 조심하고 나쁜 생각이나 거친 행동을 하지 않으며 편안한 마음으로 말이나 행동을 하려는 전통이 "
          "있는데 이를 {태교}(태아를 가르침)라고 한다. 태아에게 좋은 글을 읽어 주거나 음악을 들려주는 것도 "
          "태교에 해당한다."),
        PARAGRAPH("아이를 낳고 나면 산후 조리를 한다. 이때 보통 미역국을 먹는다. 영양분이 풍부한 미역은 산모의 피를 "
          "맑게 해 주고 모유가 잘 나오도록 한다. 출산 후 먹는 음식은 나라마다 다르다. 예를 들어 베트남에서는 "
          "닭고기, 새우, 쇠고기를 볶은 요리와 ‘샤오옷’이라는 채소를 많이 먹는데 이는 자궁 속 찌꺼기를 빼는 데 "
          "도움을 준다고 한다."),
        FIGURE("한국의 산후 조리 음식 중 하나인 미역국"),
        PARAGRAPH("* 자신의 고향 나라와 한국의 태교 문화나 산후 조리 문화를 비교하여 이야기해 봅시다."),
    ],
    annotations={
        "교육": dict(
            meaning="보호+ 교육",
        ),
        "국민행복카드": dict(
            meaning="\"National Happiness Card\"",
            notes=["國民 (citizens)", "幸福 (happiness)",
                "a voucher card for pregnancy/childbirth-related medical "
                "expenses; can be issued by bringing a pregnancy "
                "confirmation document to a nearby bank, or applied for "
                "online/by phone"],
        ),
        "산전": dict(
            meaning="before childbirth/prenatal",
            notes=["産 (to give birth/produce, same 産 as in 부동산, 농산물)",
                "前 (before)", "아이를 낳기 전 = \"before giving birth to a child\""],
        ),
        "임산부 교육프로그램": dict(
            meaning="education programs for pregnant women",
            characters=[("妊", None, "to be pregnant +"), ("産", None,
                "to give birth +"), ("婦", None, "woman)")],
            notes=["妊産婦 (pregnant woman,", "敎育 (education)",
                "모유 수유 교실, 임산부 체조 교실, 출산 준비 교실, 아기 마사지 교실 등 = "
                "\"breastfeeding class, prenatal exercise class for "
                "pregnant women, birth preparation class, baby massage "
                "class, etc.\""],
        ),
        "보육": dict(
            meaning="childcare",
            notes=["保 (to protect, same 保 as in 보건소, 보증금)",
                "育 (to raise, same 育 as in 양육, 체육)",
                "아이를 보살피고 돌보다 = \"to look after and care for a child\""],
        ),
        "장려하": dict(
            headword="장려하다",
            meaning="to encourage/promote",
            notes=["獎 (to encourage)", "勵 (to encourage/exert effort)",
                "출산을 장려하다 = \"to encourage childbirth\""],
        ),
        "양육": dict(
            meaning="childrearing",
            notes=["養 (to nurture, same 養 as in 영양제 \"nutritional "
                "supplement\")", "育 (to raise, same 育 as in 보육, 체육)",
                "양육에 대한 경제적 부담 = \"the economic burden of childrearing\""],
        ),
        "경제": dict(
            meaning="economy",
            notes=["經 (to manage/pass through, same 經 as in 경제적)",
                "濟 (to aid/relieve, same 濟 as in 경제적)",
                "경제적 부담 = \"economic burden\""],
        ),
        "임산부": dict(
            meaning="pregnant woman",
            notes=["妊 (pregnant)", "産 (to give birth, same 産 as in 출산, 부동산)",
                "婦 (woman, same 婦 as in 부부's related root)",
                "임산부를 위한 보건소 서비스 = \"health center services for pregnant "
                "women\""],
        ),
        "영양제": dict(
            meaning="nutritional supplement",
            notes=["營養 (nutrition, 營 = to manage/operate + 養 = to nurture, "
                "same 養 as in 양육)",
                "劑 (medicine/preparation, same 劑 as in 진통제 \"painkiller\")",
                "임신 중에 필요한 영양제 = \"nutritional supplements needed during "
                "pregnancy\""],
        ),
        "증진": dict(
            meaning="enhancement/promotion",
            notes=["增 (to increase, same 增 as in 증가 \"increase\")",
                "進 (to advance, same 進 as in 진출, 진료)",
                "energy or strength gradually increasing and advancing"],
        ),
        "보육비": dict(
            meaning="childcare fee",
            notes=["어린이집 보육비 = \"daycare center childcare fee\""],
        ),
        "유형": dict(
            meaning="type/category",
            notes=["類 (kind/category, same 類 as in 종류 \"type/kind\")",
                "型 (mold/pattern, same 型 as in 대형 \"large-type/size\")",
                "기관의 유형(어린이집, 유치원)에 따라 = \"depending on the type of "
                "institution (daycare center, kindergarten)\""],
        ),
        "양육하": dict(
            headword="양육하다",
            meaning="to raise/rear (a child)",
            characters=[("養", None, "to nurture"), ("育", None, "to raise")],
            notes=["아이를 양육하다 = \"to raise a child\""],
        ),
        "연령": dict(
            meaning="age",
            notes=["자녀의 연령에 따라 = \"depending on the child's age\""],
        ),
        "수당": dict(
            meaning="allowance",
            notes=["手 (hand, here used in an extended sense related to \"hand "
                "out/give\")", "當 (to correspond to)",
                "양육 수당 = \"childcare allowance\", 아동 수당 = \"child "
                "allowance\""],
        ),
        "영·유아": dict(
            meaning="infants and toddlers",
            notes=["嬰兒 (infant, 嬰 = infant/baby + 兒 = child)",
                "幼兒 (toddler/young child, 幼 = young + 兒 = child)",
                "영·유아(0~만 5세 이하) = \"infants and toddlers (age 0 to 5 and "
                "under)\""],
        ),
        "연장": dict(
            meaning="extension",
            notes=["延 (to extend/prolong, same 延 as in 연기하다 \"to postpone\")",
                "長 (long, same 長 as in 최장 \"longest\")",
                "체류기간을 5개월로 연장하다 = \"to extend the stay period to 5 ""months\""
                ],
        ),
        "전담": dict(
            meaning="sole responsibility/dedicated charge",
            notes=["專 (exclusive/sole, same 專 as in 전용)",
                "擔 (to shoulder/take charge of, same 擔 as in 부담)",
                "전담 인력 = \"dedicated staff/personnel\""],
        ),
        "거점": dict(
            meaning="base/hub",
            notes=["據 (to rely on/base oneself on)",
                "點 (point, same 點 as in 쟁점)",
                "지역 거점 병원 = \"regional hub hospital\", a key location "
                "serving as the basis for some activity"],
        ),
        "보건복지부": dict(
            meaning="Ministry of Health and Welfare",
            notes=["保健 (health protection, already covered — same root as 보건소)"
                , "福祉 (welfare, 福 = blessing/fortune, same 福 as in 국민행복카드 + 祉 "
                "= happiness/blessing)",
                "部 (ministry, same 部 as in 법무부, 여성가족부)",
                "보건복지부에서 지정한 보육 기관 = \"a childcare institution designated "
                "by the Ministry of Health and Welfare\""],
        ),
        "설립한": dict(
            headword="설립하다",
            meaning="to establish/found",
            notes=["設 (to set up, same 設 as in 시설)",
                "立 (to stand, same 立 as in 사립, 연립 주택)",
                "정부나 지방 자치 단체에서 설립하다 = \"established by the government or "
                "local governments\""],
        ),
        "사립": dict(
            meaning="private (institution)",
            notes=["私 (private, same 私 as in 사기업 \"private enterprise\")",
                "立 (to stand/establish, same 立 as in 설립, 연립 주택)",
                "사립 유치원 = \"private kindergarten\", contrasted with 국·공립 "
                "(national/public)"],
        ),
        "세운": dict(
            headword="세우다",
            meaning="to build/erect",
            notes=["교회나 성당 등과 같은 종교 단체에서 세우다 = \"built by religious "
                "organizations such as churches or Catholic parishes\""],
        ),
        "가정": dict(
            meaning="home/household",
            notes=["家 (house/family, same 家 as in 가족)",
                "庭 (courtyard, extended to mean \"home\")",
                "일반 가정에서 영·유아를 돌보다 = \"caring for infants/toddlers in an "
                "ordinary household\""],
        ),
        "돌보는": dict(
            headword="돌보다",
            meaning="to look after/take care of",
            notes=["일반 가정에서 영·유아를 돌보는 가정 어린이집 = \"home daycare centers that "
                "look after infants/toddlers in an ordinary household\""],
        ),
        "기본 보육반": dict(
            meaning="basic childcare class",
            notes=["기본 보육반은 담임 교사가 담당한다 = \"the homeroom teacher is in charge "
                "of the basic childcare class\""],
        ),
        "담임": dict(
            headword="담임 교사",
            meaning="homeroom teacher",
            notes=["기본 보육반은 담임 교사가 담당한다 = \"the basic childcare class is "
                "handled by the homeroom teacher\""],
            surfaces=["담임 교사가"],
        ),
        "관할": dict(
            meaning="jurisdiction",
            notes=["管 (to manage/oversee, same 管 as in 보관 \"storage\")",
                "轄 (to govern/control)",
                "controlling or governing with a certain authority"],
        ),
        "법인": dict(
            meaning="legal entity/corporation",
            notes=["法 (law, same 法 as in 법무부, 법률)",
                "人 (person, same 人 as in 개인, 국민)",
                "an organization that legally holds rights and obligations, "
                "i.e. a corporate/juridical person"],
        ),
        "몸가짐": dict(
            meaning="bearing/conduct/deportment",
            notes=["몸 + 가지다", "임신 중 엄마의 마음과 몸가짐 = \"the mother's mindset and "
                "bearing/conduct during pregnancy\""],
        ),
        "정서적": dict(
            meaning="emotional",
            notes=["情緖 (emotion, 情 = feeling)",
                "정서적으로 영향을 미치다 = \"to have an emotional effect/influence\""],
        ),
        "심리적": dict(
            meaning="psychological",
            notes=["心理 (psychology/mentality, 心 = heart/mind + 理 = "
                "reason/principle)", "심리적인 안정 = \"psychological stability\""],
        ),
        "신체적": dict(
            meaning="physical",
            characters=[("身", None, "body/self, same 身 as in 신분증 +"), ("體",
                None, "body)")],
            notes=["身體 (body,", "신체적으로 영향을 미치다 = \"to have a physical effect\""
                ],
        ),
        "미친다": dict(
            meaning="to reach/have an effect on",
            notes=["영향을 많이 미친다고 생각해 왔다 = \"has been thought that it greatly "
                "affects/influences\""],
        ),
        "태교": dict(
            meaning="prenatal education/taegyo",
            notes=["胎 (fetus/womb, same 胎 as in 태아 \"fetus\")",
                "敎 (to teach, same 敎 as in 교육)",
                "literally \"teaching the fetus\" — the traditional "
                "practice of a pregnant woman maintaining good behavior and "
                "mindset believed to positively influence the unborn child"],
        ),
    },
    chapterGlossary=["교육"],
    fixes=[
        ("한국의 임신 출산", "한국의 임신·출산", "the middle dot is missing"),
        ("영유아 보육·교육기관", "영유아 보육·교육 기관", "spacing"),
        ("30분까", "30분까지", "the Doc drops 지 at the line break"),
        ("통제 하거나", "통제하거나", "spacing"),
        ("조손가정", "조손 가정", "spacing"),
        ("거점형 이간보육", "거점형 야간보육", "typo — 이간 for 야간"),
        ("0세부터,만 5세까지", "0세부터 만 5세까지", "a comma stands where a space belongs"),
        ("에서 저정한", "에서 지정한", "typo — 저정 for 지정"),
        ("* 자신의", "★ 자신의", "the page uses a star for the discussion prompt"),
    ],
    approved={
        # read against the photos of pp. 54-57 and accepted
        "한국의 임신 출산", "영유아 보육·교육기관", "30분까", "통제 하거나",
        "조손가정", "거점형 이간보육", "0세부터,만 5세까지", "에서 저정한",
        "* 자신의",
    },
    headwords={"불가피한": "불가피하다", "저렴한": "저렴하다", "풍부한": "풍부하다",
               "담임 교사가": "담임"},
    english={
        "출산을 지원하는 제도": dict(
            title="What supports childbirth",
            paragraphs=[
                "Korea supports the costs that pregnancy, childbirth and the raising "
                "of a child require, so as to encourage births and lessen the "
                "financial burden of bringing a child up. On becoming pregnant, part "
                "of the cost of an expectant mother's health care and of the birth is "
                "supported by the government through the National Happiness Card.",

                "Public health centre services for expectant mothers can also be had: "
                "any expectant mother, marriage immigrants included, need only "
                "register at the health centre to receive free antenatal examinations, "
                "and can be given the nutritional supplements needed during pregnancy. "
                "Beyond this there are various services and antenatal education "
                "programmes according to the health centre of each area. After the "
                "birth, individual local authorities sometimes provide a childbirth "
                "grant or a congratulatory payment; the particulars can be had by "
                "asking at the city, district or county office.",
            ],
        ),
        "보육과 유아 교육을 지원하는 제도": dict(
            title="What supports childcare and early education",
            paragraphs=[
                "Childcare fees or early-years tuition are supported for the infant "
                "and preschool children of nationals — from birth to the age of five "
                "— who attend a nursery or a kindergarten before entering primary "
                "school. One applies for the Child Happiness Card at a bank, over the "
                "internet or by telephone, and can pay nursery fees or kindergarten "
                "tuition with it.",

                "The amount supported differs with the child's age and with the kind "
                "of institution, nursery or kindergarten. Where a child is raised at "
                "home rather than at a nursery or kindergarten, a home care allowance "
                "is provided according to the child's age.",

                "Besides childcare fees and the home care allowance, the government "
                "has since September 2018 paid a child benefit, to lessen the "
                "financial burden of raising a child and to advance children's rights "
                "and welfare. It is provided to households with a child under the age "
                "of seven.",
            ],
        ),
        "어린이집": dict(
            title="The nursery",
            paragraphs=[
                "A nursery is a childcare institution designated by the Ministry of "
                "Health and Welfare, responsible for the care and education of "
                "children from birth until they enter primary school at five. There "
                "are national and public nurseries established by the government or a "
                "local authority; private nurseries established by individuals; "
                "workplace nurseries for the children of a company's employees; "
                "nurseries founded by religious bodies such as churches; and home "
                "nurseries, where infants and preschoolers are looked after in an "
                "ordinary household.",

                "Nursery hours run as basic care, from nine in the morning to four in "
                "the afternoon, and extended care, from four until half past seven in "
                "the evening; the basic class is taken by the class teacher and the "
                "extended class by a teacher dedicated to it. Depending on the "
                "institution, childcare services may also be provided such as "
                "round-the-clock care combining daytime hours (07:30–19:30) with night "
                "hours (19:30–07:30 the following day), holiday care, and hub-based "
                "night care.",
            ],
        ),
        "유치원": dict(
            title="The kindergarten",
            paragraphs=[
                "A kindergarten is an educational institution responsible for the "
                "education of preschool children, from the age of three until they "
                "enter primary school at five, and it comes under the Ministry of "
                "Education. There are national and public kindergartens established by "
                "the government or a local authority, and private ones established by "
                "individuals, legal persons or religious bodies. They usually operate "
                "on weekdays from about nine in the morning to two in the afternoon, "
                "and an all-day class is sometimes run from about seven in the morning "
                "to eight in the evening for the children of two-earner parents.",

                "Kindergarten fees are generally cheaper at national and public "
                "kindergartens than at private ones. So to send a child to a national "
                "or public kindergarten one often has to wait a long time after "
                "applying.",
            ],
        ),
    },

    extraAnnotations={
        "영아": dict(
            hanja="嬰兒", meaning="an infant, a baby",
            characters=[("嬰", "영", "infant"),
                        ("兒", "아", "child — the same 兒 as in 육아, 신생아")],
            notes=["Nought to two, per your note at the top of p. 54. 영·유아 taken "
                   "together is the whole preschool range, and 보육 is what is done "
                   "for them."],
        ),
        "유아": dict(
            hanja="幼兒", meaning="a preschool child",
            characters=[("幼", "유", "young — as in 유치원, 유년"),
                        ("兒", "아", "child")],
            notes=["Three to five, per your note. Paired with 영아 as 영·유아 — and the "
                   "centre dot is how Korean joins two words that share a head."],
        ),
        "보육": dict(
            hanja="保育", meaning="childcare",
            characters=[("保", "보", "to protect — the same 保 as in 보험, 보장, 보건소"),
                        ("育", "육", "to raise — the same 育 as in 교육, 양육, 육아")],
            notes=["Your note on the title page takes it apart as 보호 + 교육, "
                   "protection plus education, which is exactly what the two "
                   "characters are.",
                   "The chapter's division follows the ministries: 보육 is the "
                   "어린이집 under 보건복지부, 교육 is the 유치원 under 교육부."],
        ),
        "양육": dict(
            hanja="養育", meaning="bringing up a child",
            characters=[("養", "양", "to nurture, feed — as in 영양 “nutrition”, 피부양자"),
                        ("育", "육", "to raise")],
            notes=["Met in chapter 3, of women leaving work over 출산과 양육. Broader "
                   "than 보육, which is care given by an institution; 양육 is the "
                   "whole raising of a child, and 양육 수당 is what is paid when it is "
                   "done at home."],
        ),
        "임산부": dict(
            hanja="臨産婦", meaning="an expectant mother",
            characters=[("臨", "임", "to face, be about to — as in 임시 “temporary”"),
                        ("産", "산", "to give birth, produce — the same 産 as in 출산, 산업"),
                        ("婦", "부", "woman, wife — as in 부부 “married couple”, 주부")],
            notes=["Strictly 임부 is pregnant and 산부 has just given birth; 임산부 "
                   "covers both. Not to be confused with 임신부, which is the pregnant "
                   "one only."],
        ),
        "국민행복카드": dict(
            meaning="the National Happiness Card",
            notes=["The card through which the state's support for pregnancy and birth "
                   "is paid. Obtainable at a bank with a certificate of pregnancy, or "
                   "online or by telephone.",
                   "Its counterpart later in the chapter is the 아이행복카드, for "
                   "nursery and kindergarten fees — the same naming, one step further "
                   "on."],
        ),
        "산전": dict(
            hanja="産前", meaning="antenatal, before the birth",
            characters=[("産", "산", "to give birth"),
                        ("前", "전", "before — as in 전후, 오전")],
            notes=["Its opposite 산후 appears in the discussion at the end of the "
                   "chapter: 산후 조리, the care taken after the birth."],
        ),
        "영양제": dict(
            hanja="營養劑", meaning="a nutritional supplement",
            characters=[("營", "영", "to manage, nourish — as in 운영 “operation”, 경영"),
                        ("養", "양", "to nourish — the same 養 as in 양육"),
                        ("劑", "제", "preparation, agent — the same 劑 as in 세제")],
            notes=["Not the 영 of 영아 — that is 嬰. Here 영양 is nutrition."],
        ),
        "자치": dict(
            hanja="自治", meaning="self-government",
            characters=[("自", "자", "self — the same 自 as in 자가, 자신"),
                        ("治", "치", "to govern, heal — as in 정치 “politics”, 치료")],
            notes=["지방 자치 단체, the local authority, is the phrase this chapter and "
                   "chapters 6 to 8 all lean on — shortened in speech to 지자체."],
        ),
        "영·유아": dict(
            meaning="infants and preschool children",
            notes=["The two words of your margin note joined: 영아 nought to two, "
                   "유아 three to five. The whole range a 어린이집 takes."],
        ),
        "보육비": dict(
            hanja="保育費", meaning="childcare fees",
            characters=[("費", "비", "expense — the same 費 as in 진료비, 생계비, 교육비")],
        ),
        "학비": dict(
            hanja="學費", meaning="tuition fees",
            characters=[("學", "학", "to learn — the same 學 as in 학교, 학세권"),
                        ("費", "비", "expense")],
            notes=["The page keeps 보육비 for the nursery and 유아 학비 for the "
                   "kindergarten — the fee is named after which institution it is "
                   "paid to."],
        ),
        "아이행복카드": dict(
            meaning="the Child Happiness Card",
            notes=["Pays nursery fees and kindergarten tuition. Applied for at a bank, "
                   "online or by telephone, like the 국민행복카드 before it."],
        ),
        "유형": dict(
            hanja="類型", meaning="a type, a category",
            characters=[("類", "류", "kind, sort — as in 종류 “kind”, 분류"),
                        ("型", "형", "form, mould — as in 형태 “form”, 모형")],
            notes=["Met in chapter 2's 가구 유형별 비율 chart. 유형별 is “by type”."],
        ),
        "연령": dict(
            hanja="年齡", meaning="age",
            characters=[("年", "년", "year — the same 年 as in 노년, 미성년"),
                        ("齡", "령", "age — the same 齡 as in 고령화")],
            notes=["The formal word beside the everyday 나이 — met in chapter 2's "
                   "margin glossary."],
        ),
        "양육 수당": dict(
            hanja="養育手當", meaning="the home care allowance",
            characters=[("手", "수", "hand — as in 수술, 착수"),
                        ("當", "당", "to correspond to — the same 當 as in 담당, 해당")],
            notes=["수당 is an allowance paid on top of something else — 초과근무 수당 "
                   "is overtime pay. Paid where a child is raised at home instead of "
                   "at a nursery, so 보육료 and 양육 수당 are alternatives, not both."],
        ),
        "아동 수당": dict(
            hanja="兒童手當", meaning="child benefit",
            characters=[("兒", "아", "child — the same 兒 as in 영아, 유아"),
                        ("童", "동", "child — as in 아동, 동화 “fairy tale”")],
            notes=["Paid since September 2018 to households with a child under seven, "
                   "and paid regardless of how the child is cared for — which is what "
                   "separates it from the 양육 수당."],
        ),
        "증진": dict(
            hanja="增進", meaning="advancement, furthering",
            characters=[("增", "증", "to increase — as in 증가 “increase”, 증대"),
                        ("進", "진", "to advance — the same 進 as in 진출, 진학")],
            notes=["Of something abstract being built up: 복지 증진, 건강 증진, "
                   "친선 증진."],
        ),
        "공백": dict(
            hanja="空白", meaning="a gap, a blank",
            characters=[("空", "공", "empty, sky — as in 공항 “airport”, 공간"),
                        ("白", "백", "white — the same 白 as in 백성, 백색소음")],
            notes=["Literally empty white — the blank on a page, and by extension any "
                   "gap. 양육 공백 is the hole in care that two working parents leave, "
                   "and 경력 공백 the gap in a career, close kin to chapter 3's "
                   "경력 단절."],
        ),
        "아이 돌보미": dict(
            meaning="a child carer, a childminder",
            notes=["Native Korean throughout: 돌보다 “to look after” plus the "
                   "agent-forming 미, as in 도우미 “helper”. The scheme sends one to "
                   "the house."],
        ),
        "일시적": dict(
            hanja="一時的", meaning="temporary",
            characters=[("一", "일", "one"),
                        ("時", "시", "time — the same 時 as in 한시적, 시간"),
                        ("的", "적", "-ic, -al")],
            notes=["Close to chapter 7's 한시적, but 일시적 is “for the moment” while "
                   "한시적 is “for a fixed term”."],
        ),
        "설립": dict(
            hanja="設立", meaning="to establish, found",
            characters=[("設", "설", "to set up — as in 설치 “installation”, 시설, 설명"),
                        ("立", "립", "to stand — the same 立 as in 연립 주택")],
        ),
        "국·공립 어린이집": dict(
            hanja="國公立어린이집", meaning="a national or public nursery",
            characters=[("國", "국", "national — as in 국가, 국립"),
                        ("公", "공", "public — the same 公 as in 공공부조, 공기업"),
                        ("立", "립", "to stand, established")],
            notes=["국립 is founded by the state, 공립 by a local authority, and the "
                   "centre dot joins them because they are treated as one class "
                   "against 사립."],
        ),
        "민간인": dict(
            hanja="民間人", meaning="a private individual",
            characters=[("民", "민", "people — the same 民 as in 국민, 난민"),
                        ("間", "간", "between — the same 間 as in 층간 소음, 가족 간"),
                        ("人", "인", "person")],
            notes=["민간 is the private sector as against the state — 민간 기업, "
                   "민간인. Also the civilian as against the soldier."],
        ),
        "직장 어린이집": dict(
            hanja="職場어린이집", meaning="a workplace nursery",
            notes=["For the children of a company's staff. Large employers in Korea "
                   "are required to provide one or pay towards places."],
        ),
        "가정 어린이집": dict(
            hanja="家庭어린이집", meaning="a home nursery",
            characters=[("家", "가", "house — the same 家 as in 가족, 자가"),
                        ("庭", "정", "courtyard, home — as in 정원 “garden”")],
            notes=["Run in an ordinary flat or house, and the smallest of the kinds "
                   "listed. Korea has a great many of them."],
        ),
        "연장": dict(
            hanja="延長", meaning="extension, prolonging",
            characters=[("延", "연", "to extend, delay"),
                        ("長", "장", "long — as in 장기 “long term”, 최장")],
            notes=["Met in chapter 6's article on seasonal workers, of the period of "
                   "stay being extended. Here it is the nursery day: 연장 보육 after "
                   "기본 보육."],
        ),
        "담임": dict(
            hanja="擔任", meaning="the teacher in charge of a class",
            characters=[("擔", "담", "to shoulder — the same 擔 as in 담당, 부담"),
                        ("任", "임", "to appoint, entrust — as in 임무, 책임")],
            notes=["담임 선생님 is the homeroom teacher, and the person a Korean parent "
                   "deals with about anything at all."],
        ),
        "전담": dict(
            hanja="專擔", meaning="taking sole charge of something",
            characters=[("專", "전", "exclusive — the same 專 as in 전용 “dedicated”"),
                        ("擔", "담", "to shoulder")],
            notes=["The same 專 as the 전용 차로 of chapter 4: given over to one "
                   "purpose only. A 전담 교사 does nothing but the extended class."],
        ),
        "거점": dict(
            hanja="據點", meaning="a hub, a base of operations",
            characters=[("據", "거", "to rely on, occupy — as in 근거 “grounds”, 의거"),
                        ("點", "점", "point — the same 點 as in 쟁점, 장점")],
            notes=["거점형 야간 보육 gathers the night care of a whole area into one "
                   "designated nursery, rather than every nursery staying open."],
        ),
        "교육부": dict(
            hanja="敎育部", meaning="the Ministry of Education",
            characters=[("敎", "교", "to teach — the same 敎 as in 교육, 유교"),
                        ("育", "육", "to raise"),
                        ("部", "부", "ministry — the same 部 as in 법무부, 보건복지부")],
            notes=["The kindergarten's ministry, as 보건복지부 is the nursery's. The "
                   "whole of part 02 turns on that split."],
        ),
        "관할": dict(
            hanja="管轄", meaning="jurisdiction",
            characters=[("管", "관", "to manage, pipe — as in 관리 “management”, 기관"),
                        ("轄", "할", "linchpin, to control")],
            notes=["관할 아래 있다 is to come under someone's authority; 관할 구역 is the "
                   "area an office covers."],
        ),
        "법인": dict(
            hanja="法人", meaning="a legal person, a corporation",
            characters=[("法", "법", "law — the same 法 as in 법무부, 법률"),
                        ("人", "인", "person")],
            notes=["A body the law treats as a person, able to hold rights and duties "
                   "of its own. Set against 개인, the natural person, in the same "
                   "sentence."],
        ),
        "종일반": dict(
            hanja="終日班", meaning="the all-day class",
            characters=[("終", "종", "to end — as in 종료 “termination”, 최종"),
                        ("日", "일", "day"),
                        ("班", "반", "class, group — as in 반장, 기본 보육반")],
            notes=["종일 is all day long. Run for the children of 맞벌이 parents, whose "
                   "day does not end at two."],
        ),
        "저렴": dict(
            hanja="低廉", meaning="to be inexpensive",
            characters=[("低", "저", "low — the same 低 as in 저소득층, 최저"),
                        ("廉", "렴", "cheap, upright")],
            notes=["A shade more formal than 싸다, and the word used in writing about "
                   "prices."],
        ),
        "조손 가정": dict(
            hanja="祖孫家庭", meaning="a grandparent-and-grandchild household",
            characters=[("祖", "조", "ancestor, grandparent — the same 祖 as in 조부모"),
                        ("孫", "손", "grandchild — as in 손자, 손녀")],
            notes=["A household of grandparents raising grandchildren, with the middle "
                   "generation absent. Named with 한 부모 가정 as the cases that qualify "
                   "for round-the-clock care."],
        ),
        "불가피": dict(
            hanja="不可避", meaning="unavoidable",
            characters=[("不", "불", "not — the same 不 as in 부동산, 불편"),
                        ("可", "가", "possible — as in 가능 “possible”, 허가"),
                        ("避", "피", "to avoid — the same 避 as in 대피")],
            notes=["Literally not-able-to-avoid. 불가피한 경우 is the standard phrase in "
                   "Korean rules for the case that has to be allowed for."],
        ),
        "보호자": dict(
            hanja="保護者", meaning="a guardian",
            characters=[("保", "보", "to protect"),
                        ("護", "호", "to guard — as in 보호, 간호사 “nurse”"),
                        ("者", "자", "person")],
            notes=["The word on every Korean form where English would say parent or "
                   "guardian, and used here because it need not be the parent."],
        ),
        "접촉": dict(
            hanja="接觸", meaning="contact",
            characters=[("接", "접", "to join, meet — the same 接 as in 접근하다, 예방 접종"),
                        ("觸", "촉", "to touch")],
        ),
        "권역": dict(
            hanja="圈域", meaning="a zone, a catchment",
            characters=[("圈", "권", "sphere, zone — the same 圈 as in 역세권, 수도권"),
                        ("域", "역", "region — the same 域 as in 광역시, 지역")],
            notes=["Two words for area put together, used of a service area drawn for "
                   "a purpose — here the area a hub nursery covers."],
        ),
        "몸가짐": dict(
            meaning="one's bearing, how one carries oneself",
            notes=["Native Korean: 몸 “body” plus 가짐 from 가지다 “to hold”. Covers "
                   "conduct and demeanour together, which is why the passage pairs it "
                   "with 마음."],
        ),
        "태아": dict(
            hanja="胎兒", meaning="an unborn child, a foetus",
            characters=[("胎", "태", "womb — the same 胎 as in 태교"),
                        ("兒", "아", "child — the same 兒 as in 영아, 유아, 아동")],
            notes=["Glossed in line on the page as 뱃속의 아이."],
        ),
        "태교": dict(
            hanja="胎敎", meaning="prenatal education",
            characters=[("胎", "태", "womb"),
                        ("敎", "교", "to teach — the same 敎 as in 교육, 교육부")],
            notes=["Literally teaching the womb, and glossed in line as 태아를 가르침. "
                   "The tradition holds that the mother's mind and conduct reach the "
                   "child, so reading well and hearing music count as part of it."],
        ),
        "산후 조리": dict(
            hanja="産後調理", meaning="postnatal care",
            characters=[("産", "산", "to give birth — the same 産 as in 산전, 출산"),
                        ("後", "후", "after — the same 後 as in 전후, 중후반"),
                        ("調", "조", "to adjust, tune — as in 조절, 조화"),
                        ("理", "리", "reason, to manage — the same 理 as in 원리, 관리")],
            notes=["조리 is regulating and setting right — the same word as cooking, "
                   "from the same idea of preparing properly. 산후조리원 is the "
                   "residential centre where it is now often done, and is close to a "
                   "Korean institution."],
        ),
        "미역국": dict(
            meaning="seaweed soup",
            notes=["What a Korean mother eats after giving birth, and what everyone "
                   "eats on their birthday for that reason. Also, by an old joke, what "
                   "one must not eat before an exam: 미역국을 먹다 means to fail."],
        ),
        "산모": dict(
            hanja="産母", meaning="a mother who has just given birth",
            characters=[("産", "산", "to give birth"),
                        ("母", "모", "mother — as in 모유, 부모")],
        ),
        "모유": dict(
            hanja="母乳", meaning="breast milk",
            characters=[("母", "모", "mother"),
                        ("乳", "유", "milk — as in 우유 “cow's milk”, 두유")],
            notes=["모유 수유 is breastfeeding, and one of the classes the health "
                   "centre's antenatal programme offers."],
        ),
        "자궁": dict(
            hanja="子宮", meaning="the womb",
            characters=[("子", "자", "child — the same 子 as in 구급상자, 자녀"),
                        ("宮", "궁", "palace — as in 경복궁, 궁전")],
            notes=["Literally the child's palace."],
        ),
    },

    extraNotes=[
        "This is the first chapter of the 교육 unit rather than 사회 — the page header "
        "reads 9 교육 and the footer 02 교육.",
        "Pages 52-53, the opener for 제2편 교육, are not transcribed: they carry "
        "the part's name and nothing else.",
    ],
)
