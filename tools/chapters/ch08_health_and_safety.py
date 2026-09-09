# -*- coding: utf-8 -*-
"""Chapter 8 — Health care and safety.

Transcribed in your Google Doc (8.html), whose text is carried in `blocks`
below as the Doc had it. First transcribed from the photos of pp. 44-47; the
two readings were compared line by line when your Doc arrived, and every
difference proved to be a slip in the Doc, listed as fixes below. The Doc has
no 학습목표 or 관련 단원 확인하기 section, so those two are inserted here from the page.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, LABELS,
               MARGIN, TABLE, CELL, CHART, GLOSSARY)

CHAPTER = dict(
    number=8, slug="08-health-and-safety",
    unit="사회", title="의료와 안전", titleEn="Health care and safety",

    blocks=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 우리가 일상생활에서 갑자기 겪을 수 있는 상황입니다."),
        LABELS("{화재}", "{소독}", "{지진}"),
        HEADING(4, "01 각 상황이 발생하면 자신의 고향 나라에서는 어떻게 대처합니까?"),
        MARGIN("구급차/응급차"),
        HEADING(4, "02 각 상황에 적절히 대처하기 위해 알고 싶은 점이나 궁금한 점은 무엇입니까?"),
        SECTION("goals", "학습목표"),
        BULLET("한국의 의료 기관 종류와 이용 방법을 설명할 수 있다.", ordered=True),
        BULLET("안전한 생활을 위한 생활 수칙과 대처 요령을 알고 실천할 수 있다.", ordered=True),
        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"], [["심화", "국민",
              "4. 대한민국 국민을 위한 복지", "사회보험"]]),
        SECTION("part", "01 한국에서 의료 기관은 어떻게 이용할까?"),
        HEADING(2, "의료 기관의 종류와 이용 방법", translation=
          "Types of Medical Institutions and How to Use Them" "\n\n"
          "Types of medical institutions include neighborhood clinics "
          "(동네 의원), public health centers (보건소), and general "
          "hospitals (종합 병원). For cases where illness isn't severe — "
          "like having a cold or poor digestion — people go to a "
          "neighborhood clinic for treatment. A public health center "
          "is a public health institution run by the state to protect "
          "residents' health and prevent/manage disease. You can get "
          "vaccinations or various disease screenings there, and "
          "treatment costs are cheaper than at regular hospitals. If "
          "treatment at a neighborhood clinic doesn't cure the "
          "illness, or if a more precise examination is needed, you "
          "can get a referral letter (진료 의뢰서) from the clinic or "
          "health center and go receive treatment at a general " "hospital."
          "\n\n" "Besides Western medicine, you can also use clinics or "
          "hospitals that utilize Korea's traditional medicine (한의원, "
          "한방 병원). There, you can receive acupuncture, moxibustion, "
          "or have herbal medicine (한약) prepared by decocting "
          "medicinal herbs." "\n\n"
          "If you suddenly become seriously ill or injured and it's "
          "difficult to go to the hospital yourself, you can call "
          "119. Then 119 paramedics will come, provide basic "
          "emergency treatment, and take you by ambulance to the "
          "emergency room of a nearby hospital."),
        GLOSSARY(("정밀하다", "빈틈이 없고 자세하다", "정밀하다"),
              ("침", "바늘처럼 생긴 가늘고 긴 의료 기구", "침"),
              ("뜸", "약물을 태우거나 태운 김을 쏘여 자극을 줌으로써 질병을 치료하는 방법", "뜸")),
        PARAGRAPH("의료 기관의 종류에는 {동네 의원}, {보건소}, {종합 병원} 등이 있다. 감기에 걸렸거나 소화가 잘 "
          "안 되는 등 병이 심하지 않은 경우에는 동네 의원에 가서 진료를 받는다. 보건소는 지역 주민의 건강과 "
          "질병 예방 및 관리를 위해 국가가 운영하는 공공 보건 기관이다. 예방 {접종|예방 접종}이나 "
          "{각종}{질병} 검사 등을 할 수 있으며 일반 병원보다 진료비가 싸다. 동네 의원을 통해 치료를 "
          "받았는데도 병이 잘 낫지 않거나 보다 정밀한 검사를 필요로 하는 경우에는 동네 의원이나 보건소에서 진료 "
          "{의뢰서|진료 의뢰서}를 받아 종합 병원에 가서 진료를 받을 수 있다."),
        PARAGRAPH("{서양 의학} 이외에 한국의 전통 의학을 활용한 한의원이나 {한방} 병원도 이용할 수 있다. 여기서는 "
          "침을 맞거나 뜸을 뜨거나 약초 등을 달여서 만든 {한약}을 지을 수 있다."),
        PARAGRAPH("갑자기 크게 아프거나 다쳤는데 직접 병원에 가기 어려운 경우에는 119에 전화할 수 있다. 그러면 119 "
          "{대원}이 찾아와 기본적인 응급 처치를 한 후 응급차로 가까운 병원의 응급실에 데려다 준다."),
        HEADING(2, "건강보험 제도", translation="Health Insurance System" "\n\n"
          "Korea operates a health insurance system where people pay "
          "a set amount of insurance premium each month, based on "
          "income and assets, etc. If you enroll in health insurance, "
          "when using hospitals or pharmacies for things like "
          "disease-related tests, treatment, or childbirth, the "
          "National Health Insurance Service (국민건강보험공단) covers part "
          "of the treatment cost, so you can use medical institutions "
          "at low cost. Also, people who work at companies can "
          "generally receive a free health checkup once every 2 "
          "years. All citizens must enroll in health insurance, and "
          "enrollees are divided into workplace subscribers (직장 가입자) "
          "and regional subscribers (지역 가입자). Family members of "
          "workplace or regional subscribers can, if certain "
          "conditions are met, receive the same health insurance "
          "benefits as the subscriber as a dependent (피부양자)."),
        GLOSSARY(("약초", "약으로 쓰는 풀", "약초"),
              ("응급 처치", "위급한 상황에 있는 환자에게 당장 필요한 치료를 하는 것", "응급 처치"),
              ("피부양자", "다른 사람에게서 부양을 받는 사람", "피부양자")),
        SOURCE("▶ 긴급 신고 전화"),
        TABLE([["화재 구조 · 응급 환자 · 긴급 인명 사고", "119"],
               ["범죄", "112"],
               ["해양 긴급", "122"],
               ["마약 범죄", "1301"],
               ["사이버 테러", "118"],
               ["시설물", "120"],
               ["수도 고장", "121"],
               ["전기 고장", "123"]]),
        PARAGRAPH("한국은 {소득} 및 {재산} 등에 따라 매달 일정 금액의 {보험료}를 납부하는 건강보험 제도를 실시하고 "
          "있다. 건강보험에 가입하면 질병 관련 검사, 치료, 아이 출산 등과 같이 병원이나 약국을 이용할 때 "
          "{국민건강보험공단}에서 진료비의 일부를 부담해 주기 때문에 적은 비용으로 의료 기관을 이용할 수 있다. "
          "그리고 직장에 다니는 사람들은 일반적으로 2년에 한 번씩 무료 건강 {검진|건강 검진}을 받을 수 있다. "
          "모든 국민은 건강보험에 가입해야 하는데 직장 가입자와 지역 가입자로 구분된다. 직장 가입자나 지역 "
          "가입자의 가족은 일정한 조건이 되면 피부양자로서 가입자와 동일하게 건강보험 혜택을 받을 수 있다."),
        FIGURE("건강보험증 — 건강보험증이나 신분증을 가지고 의료기관에 방문하면 보험 혜택을 받을 수 있다."),
        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "외국인도 건강보험에 가입할 수 있을까?"),
        PARAGRAPH("외국인 등록을 한 사람 중 건강보험이 적용되는 사업장에 근무하거나 공무원으로 채용된 사람은 직장 가입자가 "
          "된다. 배우자가 직장 가입자에 해당하는 경우 배우자의 건강보험에 피부양자로 등록하면 되는데(배우자 외에도 "
          "미성년 자녀, 부모 등도 등록 가능) 피부양자 확인에 필요한 서류를 국민건강보험공단에 내면 된다. "
          "(필요한 서류 : 피부양자 자격 취득 신고서, 외국인 등록증 사본, 가족 관계 증명서). 외국인 등록을 "
          "한 사람 중 직장 가입자와 피부양자에 해당되지 않으면서 6개월 이상 거주한 사람은 지역 건강보험에 가입을 "
          "해야 한다. 2019년 7월 16일부터 한국에 6개월 이상 체류하면 지역 가입자에 해당되어 자동으로 "
          "건강보험에 가입되고 건강 보험료를 납부하게 된다."),
        SECTION("part", "02 안전한 생활을 위해서는 어떻게 해야 할까?"),
        GLOSSARY(("재난", "뜻밖에 일어난 재앙과 고난", "재난"),
              ("대비", "앞으로 일어날지 모르는 어떠한 일에 적절히 행동하기 위하여 미리 준비함", "대비"),
              ("원전", "원자력발전소, 핵분열이나 핵융합 같은 원자력 에너지를 이용하여 전기를 생산해내는 발전소이다", "원전"
              ),
              ("안전사고", "안전 교육의 부족, 또는 부주의로 일어나는 사고", "안전사고"),
              ("매뉴얼",
              "직무를 수행하는 데 필요한 작업상의 지식이나 작업진행 방법 등에 관한 기본적인 사항을 체계적으로 정리한 것",
              "매뉴얼"),
              ("대응", "어떤 일이나 사태에 맞추어 태도나 행동을 취함", "대응"),
              ("긴급신고전화", "범죄 112        재난 119        민원 110        감염병 1339",
              "긴급신고전화"),
              ("해롭다", "나쁜 점이 있다", "해롭다")),
        HEADING(2, "안전한 생활을 위한 방법", translation="Ways to Stay Safe in Daily Life"
          "\n\n" "Korea prepares for various disasters centered around the "
          "Ministry of the Interior and Safety (행정안전부), which "
          "oversees national disaster management, along with central "
          "government ministries, local governments, and public "
          "institutions. Once a year, the \"Disaster Response Safe "
          "Korea Training\" (재난 대응 안전 한국 훈련) is carried out, "
          "involving all disaster management responsible agencies and "
          "citizens — and educational institutions like schools and "
          "kindergartens also conduct earthquake and fire evacuation "
          "drills. Beyond this, central ministries and local "
          "governments must also independently carry out disaster "
          "preparedness drills at least once a year, mandatorily. "
          "Through this, they have opportunities to directly practice "
          "response manuals for things like fires, epidemics, leaks "
          "of harmful chemical substances, and nuclear power plant "
          "safety accidents." "\n\n"
          "Individual effort in daily life to prepare for and respond "
          "to disasters is also important. When an urgent disaster or "
          "major accident occurs, one should call an emergency report "
          "number and explain their current location and the accident "
          "situation in detail." "\n\n"
          "Additionally, in ordinary times, one should also check "
          "whether there are facilities, pollutants, or causes of "
          "infectious disease nearby that could harm safety, and if "
          "such things are found, report them to the relevant "
          "authorities. For example, if you find an incorrect sign, "
          "you can report or suggest it through 'Safety Sinmungo' "
          "(안전신문고) on the National Sinmungo (국민신문고) website, "
          "preventing accidents in advance."),
        PARAGRAPH("한국은 국가 재난 관리를 담당하는 {행정안전부}를 중심으로 중앙 {부처}·{지방 자치 단체}·공공 기관이 "
          "다양한 재난에 대비하고 있다. 매년 1회 모든 재난 관리 책임 기관 및 국민이 참여하는 「{재난 대응 "
          "안전 한국 훈련}」을 실시하는데 학교, 유치원 등과 같은 교육 기관에서도 지진 {대피}, 화재 대피 "
          "{훈련}을 한다. 이 외에도 중앙 부처 및 지방 자치 단체 등에서 {자체적으로} 매년 1회 이상 재난 "
          "대비 훈련을 {의무적으로|의무적} 실시해야 한다. 이를 통해 화재, {전염병}, 해로운 화학 물질 유출, "
          "원전 안전사고 등에 대한 대응 매뉴얼을 직접 실천하는 기회를 가지고 있다."),
        PARAGRAPH("일상생활에서 각 {개인}이 재난에 대비하고 대응하는 노력도 중요하다. 긴급한 재난이나 큰 사고가 발생했을 "
          "때는 긴급신고전화 등을 통해 현재 자신의 위치와 사고 상황을 자세히 설명해야 한다."),
        PARAGRAPH("그리고 평소에도 자신의 주변에서 안전을 {해칠|해치다} 수 있는 시설, 오염 {물질}, 전염병 원인 등이 "
          "있는지 {살피고} 그러한 것을 발견할 경우에는 관계 {당국}에 신고해야 한다. 예를 들어, 잘못된 표지판을 "
          "발견할 경우 {국민신문고} 누리집 안에 있는 ‘안전신문고’를 통해 신고하거나 {건의하여|건의} 미리 "
          "사고를 예방할 수 있다."),
        FIGURE("지진 발생 시 대피요령 — 계단 이용, 엘리베이터 사용 금지, 탁자 아래로, 넓은 곳으로 대피"),
        HEADING(2, "안전한 직장 생활을 위한 방법", translation="Ways to Ensure Safe Working Life"
          "\n\n" "To prevent workplace safety accidents, it's good to "
          "regularly clean the workplace and surrounding walkways and "
          "keep things well organized in daily life. When working, "
          "protective equipment such as work clothes, safety helmets, "
          "and safety shoes must always be worn. Harmful substances "
          "should be sorted and stored by type in designated "
          "locations and containers. In ordinary times, one should "
          "check the locations of emergency exits, first-aid kits, "
          "and fire extinguishers, and learn in advance the meanings "
          "of safety/health signs."),
        PARAGRAPH("직장 안전사고 예방을 위해서는 평소에 {작업장}과 주변 {통로}를 자주 청소하고 정리 {정돈}을 잘해 "
          "두는 것이 좋다. 작업할 때는 작업복, {안전모}, 안전화 등 보호 장비를 반드시 착용해야 한다. 해로운 "
          "물질은 종류별로 정해진 장소와 {용기}에 구분해서 보관한다. {평상시}에는 비상구 와 {구급상자}, "
          "소화기 설치 위치를 확인하며 안전·보건표지의 의미도 미리 알아두도록 한다."),
        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "똑똑한 CCTV로 대한민국의 안전을 높입니다"),
        PARAGRAPH("혹시 누군가가 어린이에게 몰래 다가가 어린이의 안전을 해치고 달아나거나 사람이 없는 밤 시간에 자동차 "
          "사고를 내고 아무런 조치도 없이 그냥 가버리는 상황이 발생하면 어떻게 해야 할까? 잘못을 하고도 달아난 "
          "사람은 아무도 못 봤을 거라고 생각할 수 있지만, 한국에는 생활 주변 곳곳에 CCTV가 설치되어 있어 "
          "다른 사람의 안전을 해치는 행위를 하는 사람을 찾아낼 수 있다. 사람의 얼굴은 물론 소지품, 행동 패턴, "
          "차량 번호 등을 지능적으로 포착해서 분석하게 되면 누가 잘못을 했고 누가 피해를 입었는지 알 수 있다. "
          "한국 정부와 각 지방의 시, 군, 구에서 설치한 스마트 CCTV 시스템은 단지 범죄자 추적만이 아니라 "
          "안전을 해치는 행위를 사전에 발견하여 예방하는 데도 기여할 수 있다."),
        SECTION("review", "주요 내용정리"),
        HEADING(2, "01 한국에서 의료 기관은 어떻게 이용할까?"),
        BULLET("의료 기관의 종류에는 ( 동네 의원 ), 보건소, ( 종합 병원 ) 등이 있다."),
        BULLET("( 보건소 )는 지역 주민의 건강과 질병 예방 및 관리를 위해 국가가 운영하는 공공 보건 기관이다."),
        BULLET("( 건강보험 )에 가입하면 비교적 적은 비용으로 의료 기관을 이용할 수 있다."),
        HEADING(2, "02 안전한 생활을 위해서는 어떻게 해야 할까?"),
        BULLET("국가 재난 관리를 담당하는 ( 행정안전부 )를 중심으로 지진 대피, 화재 대피, 비상 대비 등 다양한 "
          "재난에 대비한 훈련을 실시하고 있다."),
        BULLET("긴급한 재난이나 큰 사고가 발생했을 때는 ( 긴급신고전화 ) 등을 통해 현재 자신의 위치와 사고 상황을 "
          "자세히 설명해야 한다."),
        BULLET("작업할 때는 ( 작업복 ), ( 안전모 ), 안전화 등 ( 보호 장비 )를 반드시 착용한다."),
        BULLET("평상시에는 ( 비상구 )와 구급상자, ( 소화기 ) 설치 위치를 확인하며 안전·보건 표지의 의미도 미리 "
          "알아두도록 한다."),
        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "외국인이 겪는 산업 재해 발생 비율, 내국인보다 6배 높아 언어적 차이를 고려한 작업장 안전 교육 필요",
          translation=
          "Industrial accidents among foreigners run six times higher than "
          "among Koreans — workplace safety training that takes language "
          "differences into account is needed" "\n\n"
          "According to figures from the Ministry of Employment and Labour "
          "and the Korea Occupational Safety and Health Agency, the accident "
          "rate among Korean workers covered by industrial accident "
          "insurance was 0.18%, while among foreign workers it was 1.16% — "
          "about six times higher. From 2012 to May 2017 a total of 33,708 "
          "foreign workers were injured at work, 511 of them fatally. One "
          "reason accidents are relatively frequent appears to be that "
          "workplace safety training is given without sufficient regard for "
          "language or cultural differences. Measures to deal with this are "
          "needed."),
        PARAGRAPH("고용노동부·안전보건공단 자료에 따르면 산재 보험에 가입된 내국인 근로자의 산재 발생률은 0.18%인 반면 "
          "외국인근로자는 1.16%로 6배 정도 높았다. 2012년부터 2017년 5월까지 산재를 당한 외국인 "
          "근로자 수는 총 33,708명이고 이 중 사망자는 511명이다. 사고 발생이 상대적으로 많은 이유 중 "
          "하나는 언어나 문화적 차이를 충분히 고려하지 않은 채 사업장 안전 교육이 이루어지기 때문인 것으로 "
          "보인다. 이에 대한 대책이 필요하다."),
        CHART("외국인 근로자 산업 재해자 수, 총 재해자(안전보건공단)(단위: 명)", "명", [["2012년", 6404],
              ["2013년", 5586],
              ["2014년", 6044],
              ["2015년", 6649],
              ["2016년", 8728],
              ["2017년", 6302]]),
        CHART("그 가운데 사망자 수(단위: 명)", "명", [["2012년", 106],
              ["2013년", 88],
              ["2014년", 85],
              ["2015년", 103],
              ["2016년", 88],
              ["2017년", 107]]),
        SOURCE("[출처] 연합뉴스(2017. 10. 12)"),
        PARAGRAPH("★ 본인이 직장에서 받았던 안전 교육의 내용이나 방법에 대해 이야기해 봅시다. 또는 가정이나 직장에 꼭 "
          "필요하다고 생각하는 안전 교육 내용을 이야기해 봅시다.",
          "Talk about what the safety training you were given at work "
          "covered, and how it was given. Or talk about the safety training "
          "you think is really needed at home or at work."),
    ],
    annotations={
        "정밀하다": dict(
            meaning="to be precise/detailed",
            notes=["精 (refined/precise, same 精 as in 정미소 \"rice mill\", which "
                "uses the same \"refining\" sense)",
                "密 (dense/close, same 密 as in 친밀하다) — literally "
                "\"refined-dense\"",
                "having no gaps and being thorough/detailed",
                "정밀 검사 = \"precision examination/detailed checkup\"."],
        ),
        "침": dict(
            meaning="acupuncture needle",
            notes=["a thin, long, needle-shaped medical instrument",
                "침을 맞다 = to receive acupuncture"],
        ),
        "뜸": dict(
            meaning="moxibustion",
            notes=["a treatment method where medicinal substances are burned, "
                "and the resulting heat/smoke is applied to the body to "
                "stimulate it and treat illness",
                "뜸을 뜨다 = to receive moxibustion treatment"],
        ),
        "동네 의원": dict(
            meaning="neighborhood clinic",
            notes=["동네 (a native/mixed word for \"neighborhood\")",
                "의원 (醫院, clinic, 醫 = medicine/doctor + 院 = "
                "institution/hall, same 院 as in 병원 \"hospital\")",
                "a small local clinic for minor ailments"],
        ),
        "보건소": dict(
            meaning="public health center",
            notes=["保健 (health protection, 保 = to protect + 健 = healthy, same "
                "健 as in 건강 \"health\")", "所 (place, same 所 as in 정미소, 소유권)",
                "a government-run local health facility"],
        ),
        "종합 병원": dict(
            meaning="general hospital",
            notes=["綜合 (comprehensive/general, 綜 = to combine + 合 = to "
                "combine, doubled emphasis)",
                "病院 (hospital, 病 = illness/disease + 院 = institution)",
                "a large hospital covering multiple medical departments"],
        ),
        "예방 접종": dict(
            meaning="접종 — vaccination/inoculation",
            notes=["接 (to touch/connect, same 接 as in 접근하다 \"to access\")",
                "種 (seed/type, here meaning \"to plant/introduce\")",
                "예방 접종 = \"preventive vaccination\", the process of "
                "injecting a vaccine into the body"],
            surfaces=["접종"],
        ),
        "각종": dict(
            meaning="various kinds/all sorts",
            notes=["各 (each, same 各 as in 각각 \"each/respectively\")",
                "種 (kind/type, same 種 as in 품종)",
                "각종 질병 검사 = \"various disease screenings\""],
        ),
        "질병": dict(
            meaning="disease/illness",
            notes=["疾 (illness)", "病 (disease, same 病 as in 병원)",
                "a formal/general term for illness, often used in "
                "medical/policy contexts (as opposed to 병, the everyday "
                "word)"],
        ),
        "진료 의뢰서": dict(
            meaning="의뢰서 — referral letter/request form",
            notes=["依賴 (依 = to depend on + 賴 = to rely on, together meaning "
                "\"to request/entrust\")",
                "書 (document, same 書 as in 계약서 \"contract document\")",
                "진료 의뢰서 = \"medical referral letter\", a document "
                "requesting further treatment elsewhere"],
            surfaces=["의뢰서"],
        ),
        "서양 의학": dict(
            meaning="Western medicine",
            notes=["西洋 (the West, 西 = west + 洋 = ocean/foreign, same 洋 as in "
                "태평양 \"Pacific Ocean\")",
                "醫學 (medicine as a field of study, 醫 = medicine + 學 = "
                "study/learning, same 學 as in 대학 \"university\")",
                "medicine based on modern Western scientific practice, "
                "contrasted with 한의학"],
        ),
        "한방": dict(
            meaning="traditional Korean medicine (as a field/practice)",
            notes=["韓 (Korea/Korean, same 韓 as in 한국)",
                "方 (method/way, same 方 as in 방법 \"method\")",
                "한방 병원 = \"traditional Korean medicine hospital\", short "
                "for 한의학의 방법 (methods of Korean medicine)"],
        ),
        "한약": dict(
            meaning="traditional herbal medicine",
            notes=["韓 (Korea/Korean, same 韓 as in 한국)",
                "藥 (medicine, same 藥 as in 약초 \"medicinal herb\")",
                "herbal medicine prepared according to traditional Korean "
                "medical practice, e.g. by decocting herbs"],
        ),
        "대원": dict(
            meaning="team member/crew member",
            notes=["隊 (unit/squad, same 隊 as in 군대 \"military\")",
                "員 (member/personnel, same 員 as in 직원 \"employee\")",
                "119 대원 = \"119 rescue/paramedic team member\", someone "
                "belonging to an organized response unit"],
        ),
        "약초": dict(
            meaning="medicinal herb",
            notes=["藥 (medicine, same 藥 as in 한약 \"herbal medicine\")",
                "草 (grass/plant, same 草 as in 초원 \"grassland/meadow\")",
                "a plant used as medicine"],
        ),
        "응급 처치": dict(
            meaning="emergency treatment/first aid",
            notes=["應急 (urgent response, 應 = to respond + 急 = urgent, same 急 "
                "as in 급하다 \"urgent\")",
                "處置 (treatment/handling, 處 = to handle/deal with + 置 = to "
                "place/set)",
                "giving a patient in an urgent situation the treatment they "
                "need right away"],
        ),
        "피부양자": dict(
            meaning="dependent",
            notes=["被扶養 (被 = to receive/passive marker + 扶養 = to support "
                "financially, 扶 = to support + 養 = to nurture, same 養 as in "
                "양육 \"childrearing\")", "者 (person, same 者 as in 근로자, 세입자)",
                "a person who receives financial support from someone else, "
                "e.g. for health insurance purposes"],
        ),
        "소득": dict(
            meaning="income",
            notes=["所 (that which, same 所 as in 소유권 \"ownership rights\")",
                "得 (to obtain/gain, same 得 as in 득실 \"gains and losses\")",
                "소득이 최저 생계비보다 적은 경우 = \"when income is less than the "
                "minimum cost of living\""],
        ),
        "재산": dict(
            meaning="property/assets",
            notes=["財 (wealth/goods, same 財 as in 문화재 \"cultural property\")",
                "産 (to produce/property, same 産 as in 부동산 \"real estate\", "
                "농산물)", "소득 및 재산 = \"income and assets\""],
        ),
        "보험료": dict(
            meaning="insurance premium",
            notes=["保險 (insurance, 保 = to protect + 險 = risk/danger, same 保 as "
                "in 보증금)", "料 (fee, same 料 as in 혼잡 통행료 \"congestion toll\")",
                "매달 일정 금액의 보험료를 납부하다 = \"to pay a set amount of insurance "
                "premium each month\""],
        ),
        "국민건강보험공단": dict(
            meaning="National Health Insurance Service",
            notes=["the government agency administering Korea's national "
                "health insurance"],
        ),
        "건강 검진": dict(
            meaning="검진 — checkup/medical examination",
            notes=["檢 (to inspect/examine, same 檢 as in 검사 "
                "\"examination/inspection\")",
                "診 (to diagnose, same 診 as in 진료 \"medical treatment\")",
                "건강 검진 = \"health checkup\""],
            surfaces=["검진"],
        ),
        "재난": dict(
            meaning="disaster",
            notes=["災 (disaster/calamity, same 災 as in 산재 \"industrial "
                "accident\", 산업재해)",
                "難 (hardship/difficulty, same 難 as in 취업난 \"job-market "
                "difficulty\")", "an unexpected calamity and hardship"],
        ),
        "대비": dict(
            meaning="preparation (against future risk)",
            notes=["對 (facing/against, same 對 as in 대응, 반대 \"opposition\")",
                "備 (to prepare, same 備 as in 준비 \"preparation\")",
                "preparing in advance so one can act appropriately for "
                "something that may happen in the future"],
        ),
        "원전": dict(
            meaning="nuclear power plant",
            notes=["原子力 (nuclear power, 原 = origin/source + 子 = particle/small "
                "unit + 力 = force/power)",
                "發電所 (power plant, 發 = to generate/emit + 電 = electricity + "
                "所 = place)",
                "short for 원자력발전소, a power plant that generates electricity "
                "using nuclear energy from fission or fusion"],
        ),
        "안전사고": dict(
            meaning="safety accident",
            notes=["安全 (safety, 安 = peaceful/safe + 全 = whole/complete, same 安 "
                "as in 불안하다 \"anxious\")",
                "事故 (accident, 事 = matter/affair + 故 = incident/cause, same "
                "事 as in 사건, 농사)",
                "an accident occurring due to lack of safety education or "
                "carelessness"],
        ),
        "매뉴얼": dict(
            meaning="manual",
            notes=["a systematic summary of the basic knowledge and work "
                "procedures needed to perform a job"],
        ),
        "대응": dict(
            meaning="response",
            notes=["對 (facing/against, same 對 as in 대비)",
                "應 (to respond, same 應 as in 응급 \"emergency response\")",
                "taking an attitude or action matched to a certain "
                "situation or event"],
        ),
        "긴급신고전화": dict(
            meaning="emergency report phone numbers",
            notes=["緊急 (urgent, 緊 = tight/urgent + 急 = urgent, same 急 as in "
                "응급)",
                "申告 (report, 申 = to state + 告 = to inform, same 告 as in 광고 "
                "\"advertisement\")",
                "電話 (phone, 電 = electricity + 話 = speech)",
                "crime 112, disaster 119, civil complaints 110, infectious "
                "disease 1339"],
        ),
        "해롭다": dict(
            meaning="to be harmful",
            notes=["해 (harm, from 害)", "롭다 (adjective suffix\"-ful\")",
                "to have a bad/harmful aspect to it"],
        ),
        "행정안전부": dict(
            meaning="Ministry of the Interior and Safety",
            notes=["行政 (administration, 行 = to act/go + 政 = governance, same 行 "
                "as in 통행, 여행)", "安全 (safety, already covered)",
                "部 (ministry, same 部 as in 법무부, 고용노동부)",
                "the government ministry overseeing domestic administration "
                "and national safety/disaster management"],
        ),
        "부처": dict(
            meaning="government ministry/department",
            notes=["部 (ministry, same 部 as in 행정안전부, 법무부)",
                "處 (office/department, same 處 as in 응급 처치 \"emergency "
                "treatment\")",
                "중앙 부처 = \"central government ministries\", a general term "
                "for government departments"],
        ),
        "지방 자치 단체": dict(
            meaning="local government",
            notes=["地方 (region/locality, 地 = land + 方 = direction/place, same "
                "地 as in 농지 \"farmland\")",
                "自治 (self-governance, 自 = self + 治 = to govern, same 自 as "
                "in 자아실현, 자신)",
                "團體 (organization/body, 團 = group + 體 = body, same 團 as in "
                "국민건강보험공단's 공단-related root)",
                "the full form of 지자체, referring to city/provincial/county "
                "governments as opposed to the central government"],
        ),
        "재난 대응 안전 한국 훈련": dict(
            meaning="\"Disaster Response Safe Korea Training\"",
            notes=["災難 (disaster, already covered)",
                "對應 (response, already covered)",
                "安全 (safety, already covered)", "韓國 (Korea)",
                "訓練 (training/drill, already covered below)",
                "an annual nationwide disaster-response drill involving "
                "government agencies and citizens"],
        ),
        "대피": dict(
            meaning="evacuation",
            notes=["待 (to wait, same 待 as in 기대하다 \"to expect/wait for\")",
                "避 (to avoid/flee, same 避 as in 피난 \"refuge\", 회피하다 \"to "
                "avoid\")",
                "to temporarily flee/take shelter so as not to suffer harm "
                "or danger"],
        ),
        "훈련": dict(
            meaning="training/drill",
            notes=["訓 (to instruct)", "練 (to practice/train)",
                "재난 대비 훈련 = \"disaster preparedness drill\""],
        ),
        "자체적으로": dict(
            meaning="on one's own/independently",
            notes=["自體 (self/itself, 自 = self + 體 = body, same 自 as in 자치, "
                "자아실현)",
                "중앙 부처 및 지방 자치 단체 등에서 자체적으로 실시하다 = \"central ministries and "
                "local governments carrying it out on their "
                "own/independently\""],
        ),
        "의무적": dict(
            headword="의무적으로",
            meaning="mandatorily/obligatorily",
            notes=["義務 (duty/obligation, 義 = righteousness/duty + 務 = "
                "task/duty, same 務 as in 법무부, 업무)",
                "매년 1회 이상 실시해야 한다 앞에 붙어 \"must be carried out "
                "mandatorily/as an obligation\""],
            surfaces=["의무적으로"],
        ),
        "전염병": dict(
            meaning="infectious disease",
            notes=["傳染 (contagion, 傳 = to transmit + 染 = to be "
                "stained/infected, same 傳 as in 전통 \"tradition\")",
                "病 (disease, same 病 as in 질병, 종합 병원)",
                "a disease that spreads from person to person, i.e. an "
                "epidemic/contagious illness"],
        ),
        "개인": dict(
            meaning="individual (person)",
        ),
        "해치다": dict(
            meaning="to harm/damage",
            notes=["안전을 해칠 수 있는 시설 = \"facilities that could harm safety\""],
            surfaces=["해칠"],
        ),
        "물질": dict(
            meaning="substance/material",
            notes=["物 (thing/object, same 物 as in 농산물, 소화물)",
                "質 (quality/substance, same 質 as in 수질 \"water quality\")",
                "오염 물질 = \"pollutant/polluting substance\""],
        ),
        "살피고": dict(
            headword="살피다",
            meaning="to look into/examine carefully",
        ),
        "당국": dict(
            meaning="the authorities",
            notes=["當 (to face/handle)",
                "局 (bureau/office, similarly-formed 局 in 우체국 \"post "
                "office\")",
                "관계 당국에 신고하다 = \"to report to the relevant authorities\""],
        ),
        "국민신문고": dict(
            meaning="\"National Sinmungo\" (Korea's civil petition/complaint "
                "website)",
            notes=["named after the Joseon-era 신문고, a drum citizens could beat "
                "at the palace to appeal directly to the king; now a "
                "government website where citizens can file civil "
                "complaints, reports, and suggestions"],
        ),
        "건의": dict(
            headword="건의하다",
            meaning="to propose/suggest",
            notes=["建議 (建 = to establish/set up + 議 = to discuss/deliberate, "
                "same 議 as in 회의 \"meeting\")",
                "신고하거나 건의하여 = \"by reporting or proposing, and "
                "[thereby]...\""],
            surfaces=["건의하여"],
        ),
        "작업장": dict(
            meaning="workplace/work site",
            notes=["평소에 작업장을 자주 청소하다 = \"to regularly clean the workplace in "
                "daily life\""],
        ),
        "통로": dict(
            meaning="passage/walkway",
            notes=["通 (to pass through, same 通 as in 통행, 통신망)",
                "路 (road/path, same 路 as in 차로 \"lane\")",
                "주변 통로 = \"surrounding walkways/passages\""],
        ),
        "정돈": dict(
            meaning="arranging/tidying",
            notes=["整 (to arrange/put in order, same 整 as in 정리)",
                "頓 (to settle/arrange)",
                "정리 정돈 = \"organizing and tidying up\""],
        ),
        "안전모": dict(
            meaning="safety helmet",
            notes=["작업복, 안전모, 안전화 = \"work clothes, safety helmet, safety "
                "shoes\""],
        ),
        "용기": dict(
            meaning="container",
            notes=["容 (to contain/hold, same 容 as in 내용 \"content\")",
                "器 (vessel/tool, same 器 as in 기관 \"organ/institution\")",
                "정해진 장소와 용기에 구분해서 보관하다 = \"to sort and store in designated "
                "locations and containers\""],
        ),
        "평상시": dict(
            meaning="normal/ordinary times",
            notes=["平常 (usual, 平 = flat/even, same 平 as in 평등 + 常 = "
                "usual/normal, same 常 as in 비상구)", "時 (time)",
                "평상시에는 비상구 위치를 확인하다 = \"in ordinary times, check the "
                "location of the emergency exit\""],
        ),
        "구급상자": dict(
            meaning="first-aid kit",
            notes=["救急 (emergency rescue, 救 = to rescue/save + 急 = urgent, "
                "same 急 as in 응급)",
                "箱子 (box, 箱 = box + 子 = suffix for small objects, same 子 as "
                "in 신생아's related root)",
                "비상구와 구급상자, 소화기 설치 위치 = \"the locations of the emergency "
                "exit, first-aid kit, and fire extinguisher\""],
        ),
    },
    headwords={"해로운": "해롭다", "해칠": "해치다", "달여서": "달이다",
               "달아나거나": "달아나다",
               "건의하여": "건의", "의무적으로": "의무적",
               # the Doc comments on half of a compound; file it under the whole
               "접종": "예방 접종", "의뢰서": "진료 의뢰서", "검진": "건강 검진"},
    english={
        "의료 기관의 종류와 이용 방법": dict(
            title="Kinds of medical institution, and how to use them",
            paragraphs=[
                "The kinds of medical institution include the neighbourhood clinic, "
                "the public health centre and the general hospital. Where the illness "
                "is not serious — a cold, say, or poor digestion — one goes to the "
                "neighbourhood clinic to be seen. The public health centre is a public "
                "health body run by the state for the health of local residents and "
                "the prevention and management of disease. Vaccinations and various "
                "screenings can be had there, and its fees are cheaper than an "
                "ordinary hospital's. Where treatment at a neighbourhood clinic has "
                "not cleared the illness up, or where a more thorough examination is "
                "needed, one can get a referral from the clinic or the health centre "
                "and be seen at a general hospital.",

                "Besides Western medicine, there are Korean medicine clinics and "
                "Korean medicine hospitals, which draw on Korea's traditional "
                "medicine. There one can be given acupuncture, have moxibustion "
                "applied, or have a herbal remedy made up by decocting medicinal "
                "plants.",

                "If one is suddenly badly ill or injured and cannot get to a hospital "
                "oneself, one can telephone 119. A 119 crew will then come, give basic "
                "first aid, and take one by ambulance to the emergency room of the "
                "nearest hospital.",
            ],
        ),
        "건강보험 제도": dict(
            title="The health insurance system",
            paragraphs=[
                "Korea operates a health insurance system under which a set amount is "
                "paid each month according to income, property and so on. Once "
                "insured, when one uses a hospital or a pharmacy — for tests or "
                "treatment relating to illness, for childbirth and the like — the "
                "National Health Insurance Service bears part of the cost, so medical "
                "institutions can be used at little expense. People in employment can "
                "also generally have a free health check once every two years. All "
                "nationals must join, and are classed either as workplace subscribers "
                "or as regional subscribers. The family of either kind of subscriber "
                "can, on meeting certain conditions, receive the same health insurance "
                "benefits as the subscriber, as a dependant.",
            ],
        ),
        "안전한 생활을 위한 방법": dict(
            title="How to live safely",
            paragraphs=[
                "In Korea the central ministries, local authorities and public bodies "
                "prepare for a range of disasters, with the Ministry of the Interior "
                "and Safety, which is responsible for national disaster management, at "
                "the centre. Once a year the Safe Korea Disaster Response Exercise is "
                "held, in which every body responsible for disaster management takes "
                "part along with the public, and educational institutions such as "
                "schools and kindergartens hold earthquake and fire evacuation drills. "
                "Beyond this, the central ministries and local authorities must "
                "themselves hold disaster preparedness exercises at least once a year. "
                "Through these there is an opportunity to put into practice the "
                "response manuals for fire, infectious disease, the release of harmful "
                "chemicals, accidents at nuclear plants and the like.",

                "The effort each person makes in daily life to prepare for and respond "
                "to disaster matters too. When an urgent disaster or a serious accident "
                "occurs, one should explain one's present location and the "
                "circumstances of the accident in detail, through the emergency "
                "numbers. In ordinary times too one should look about for facilities, "
                "polluting substances or sources of infection that might endanger "
                "safety, and report anything found to the authority concerned. A "
                "faulty road sign, for instance, can be reported or raised through the "
                "Safety Report page within the e-People website, and the accident "
                "prevented before it happens.",
            ],
        ),
        "안전한 직장 생활을 위한 방법": dict(
            title="How to be safe at work",
            paragraphs=[
                "To prevent accidents at work it is as well to clean the workplace and "
                "the passages around it often, and to keep things in order. When "
                "working, protective equipment — work clothes, a safety helmet, safety "
                "boots — must always be worn. Harmful substances are kept separately, "
                "by type, in the places and containers appointed for them. In ordinary "
                "times one should know where the emergency exit, the first aid box and "
                "the fire extinguisher are, and learn in advance what the safety and "
                "health signs mean.",
            ],
        ),
    },

    extraAnnotations={
        "화재": dict(
            hanja="火災", meaning="a fire",
            characters=[("火", "화", "fire — as in 화요일, 소화기"),
                        ("災", "재", "disaster — the same 災 as in 재난, 산재")],
        ),
        "소독": dict(
            hanja="消毒", meaning="disinfection",
            characters=[("消", "소", "to extinguish, dispel — the same 消 as in 소극적"),
                        ("毒", "독", "poison — as in 독약, 중독 “addiction”")],
            notes=["Literally putting out the poison. 소독약 is disinfectant; "
                   "소독하다 is what the figure on p. 44 shows being done."],
        ),
        "지진": dict(
            hanja="地震", meaning="an earthquake",
            characters=[("地", "지", "ground, earth — the same 地 as in 지위, 지역"),
                        ("震", "진", "to shake, tremble")],
        ),
        "동네 의원": dict(
            hanja="洞네醫院", meaning="the neighbourhood clinic",
            characters=[("洞", "동", "village, district — as in 동네, 동사무소"),
                        ("醫", "의", "medicine — the same 醫 as in 의료, 의사"),
                        ("院", "원", "institution — as in 병원, 학원")],
            notes=["의원 is a small clinic, 병원 a hospital: the size is in the word. "
                   "The chapter's route runs 의원 → 보건소 → 종합 병원, and going "
                   "straight to the last needs a referral."],
        ),
        "보건소": dict(
            hanja="保健所", meaning="a public health centre",
            characters=[("保", "보", "to protect — the same 保 as in 보험, 보장"),
                        ("健", "건", "healthy — the same 健 as in 건강"),
                        ("所", "소", "place — the same 所 as in 정미소, 조선소")],
            notes=["Run by the state, one to a district. Cheaper than a private clinic, "
                   "and where vaccinations and screening are done."],
        ),
        "종합 병원": dict(
            hanja="綜合病院", meaning="a general hospital",
            characters=[("綜", "종", "to gather, comprehensive"),
                        ("合", "합", "to combine — the same 合 as in 화합, 조합"),
                        ("病", "병", "illness — as in 병원, 질병"),
                        ("院", "원", "institution")],
        ),
        "진료": dict(
            hanja="診療", meaning="medical examination and treatment",
            characters=[("診", "진", "to diagnose — as in 진단, 건강 검진"),
                        ("療", "료", "to treat — the same 療 as in 의료, 치료")],
            notes=["진료를 받다 is to be seen by a doctor; 진료비 is the fee."],
        ),
        "예방 접종": dict(
            hanja="豫防接種", meaning="vaccination",
            characters=[("豫", "예", "beforehand — as in 예방, 예보 “forecast”"),
                        ("防", "방", "to defend — as in 소방서 “fire station”, 국방"),
                        ("接", "접", "to join, contact — the same 接 as in 접근하다"),
                        ("種", "종", "kind, seed — the same 種 as in 품종")],
        ),
        "정밀하다": dict(
            hanja="精密", meaning="to be precise, thorough",
            characters=[("精", "정", "refined, fine — the same 精 as in 정미소"),
                        ("密", "밀", "dense, close — the same 密 as in 친밀하다")],
            notes=["정밀 검사 is the detailed examination that sends one from a clinic "
                   "to a general hospital."],
        ),
        "진료 의뢰서": dict(
            hanja="診療依賴書", meaning="a referral letter",
            characters=[("依", "의", "to depend on, entrust"),
                        ("賴", "뢰", "to rely on"),
                        ("書", "서", "document — as in 계약서, 신고서")],
            notes=["What one needs to be seen at a general hospital under the insurance "
                   "system: without it the visit is charged differently."],
        ),
        "한의원": dict(
            hanja="韓醫院", meaning="a Korean medicine clinic",
            characters=[("韓", "한", "Korea — the same 韓 as in 한국, 한옥"),
                        ("醫", "의", "medicine"),
                        ("院", "원", "institution")],
        ),
        "침": dict(
            hanja="鍼", meaning="acupuncture; an acupuncture needle",
            characters=[("鍼", "침", "needle")],
            notes=["침을 맞다 is to receive acupuncture — literally to be struck with "
                   "the needle. A homonym of 침 “saliva” and of the 침 in 침대 “bed”, "
                   "both unrelated."],
        ),
        "뜸": dict(
            meaning="moxibustion",
            notes=["Native Korean. Burning a preparation on or above the skin so the "
                   "heat treats the illness, as the page glosses it. 뜸을 뜨다 is the "
                   "verb that goes with it."],
        ),
        "약초": dict(
            hanja="藥草", meaning="a medicinal herb",
            characters=[("藥", "약", "medicine — as in 약국 “pharmacy”, 한약"),
                        ("草", "초", "grass, plant — as in 초원, 잡초")],
        ),
        "한약": dict(
            hanja="韓藥", meaning="Korean herbal medicine",
            characters=[("韓", "한", "Korea"),
                        ("藥", "약", "medicine")],
            notes=["한약을 짓다 is the set phrase — 짓다 as in making up a prescription, "
                   "the same verb as building a house or cooking rice."],
        ),
        "대원": dict(
            hanja="隊員", meaning="a member of a crew or team",
            characters=[("隊", "대", "troop, team — as in 부대, 군대"),
                        ("員", "원", "member — as in 직원, 공무원, 상담원")],
            notes=["119 대원 is the crew that answers the call. A different 원 from the "
                   "院 of 병원."],
        ),
        "응급 처치": dict(
            hanja="應急處置", meaning="first aid",
            characters=[("應", "응", "to respond — the same 應 as in 응답, 복수응답"),
                        ("急", "급", "urgent — the same 急 as in 긴급"),
                        ("處", "처", "to deal with, place — as in 처리, 대처"),
                        ("置", "치", "to place, set — as in 설치 “installation”, 조치")],
        ),
        "응급차": dict(
            hanja="應急車", meaning="an ambulance",
            notes=["구급차 is the commoner word, and your note on p. 44 pairs the two. "
                   "응급 is the emergency; 구급 is the rescuing from it."],
        ),
        "응급실": dict(
            hanja="應急室", meaning="the emergency room",
            characters=[("室", "실", "room — as in 교실 “classroom”, 사무실")],
        ),
        "보험료": dict(
            hanja="保險料", meaning="an insurance premium",
            characters=[("料", "료", "fee — the same 料 as in 통행료, 요금")],
            notes=["Worth keeping apart from 보험금, which is the sum paid out. 료 is "
                   "what you pay, 금 is what you get."],
        ),
        "납부": dict(
            hanja="納付", meaning="payment of a due",
            characters=[("納", "납", "to pay in, deliver — as in 납세, 반납"),
                        ("付", "부", "to attach, hand over — as in 부담, 첨부")],
            notes=["Used of what is owed to the state or an institution — tax, "
                   "premiums, fees — rather than ordinary buying, which is 지불."],
        ),
        "국민건강보험공단": dict(
            hanja="國民健康保險公團", meaning="the National Health Insurance Service",
            characters=[("公", "공", "public — the same 公 as in 공기업, 공단"),
                        ("團", "단", "body, group — the same 團 as in 국민연금공단")],
            notes=["The other great 공단 beside 국민연금공단 in chapter 7: one runs the "
                   "health insurance, the other the pension."],
        ),
        "부담": dict(
            hanja="負擔", meaning="to bear a cost; a burden",
            characters=[("負", "부", "to bear, carry"),
                        ("擔", "담", "to shoulder — the same 擔 as in 담당")],
            notes=["Both the money borne and the feeling of being burdened: "
                   "진료비를 부담하다, and 부담스럽다 for anything that weighs on one."],
        ),
        "건강 검진": dict(
            hanja="健康檢診", meaning="a health check-up",
            characters=[("檢", "검", "to examine — as in 검사, 검색"),
                        ("診", "진", "to diagnose — the same 診 as in 진료")],
            notes=["Free every two years for people in employment, per the page."],
        ),
        "직장 가입자": dict(
            hanja="職場加入者", meaning="a workplace subscriber",
            characters=[("職", "직", "post, job — the same 職 as in 직장, 이직"),
                        ("場", "장", "place — as in 시장, 작업장"),
                        ("加", "가", "to add — the same 加 as in 가입")],
            notes=["Insured through an employer, with the premium split. Your note at "
                   "the foot of p. 45 pairs it with 지역 가입자."],
        ),
        "지역 가입자": dict(
            hanja="地域加入者", meaning="a regional subscriber",
            characters=[("地", "지", "ground, place"),
                        ("域", "역", "region — the same 域 as in 광역시")],
            notes=["Insured in one's own right rather than through an employer, and "
                   "paying the whole premium. Since 16 July 2019 a foreign resident "
                   "staying six months or more is enrolled here automatically."],
        ),
        "피부양자": dict(
            hanja="被扶養者", meaning="a dependant",
            characters=[("被", "피", "to be subjected to — the passive prefix, as in "
                                    "피해 “damage suffered”, 피고"),
                        ("扶", "부", "to support — the same 扶 as in 공공부조"),
                        ("養", "양", "to raise, nourish — the same 養 as in 양육"),
                        ("者", "자", "person")],
            notes=["The 被 is what makes it passive: 부양자 supports, 피부양자 is "
                   "supported. The same prefix turns 해 “harm” into 피해 “harm "
                   "suffered”."],
        ),
        "배우자": dict(
            hanja="配偶者", meaning="a spouse",
            characters=[("配", "배", "to match, distribute — the same 配 as in 택배, 배송"),
                        ("偶", "우", "pair, mate"),
                        ("者", "자", "person")],
        ),
        "해당": dict(
            hanja="該當", meaning="to correspond to, fall under",
            characters=[("該", "해", "that, the said"),
                        ("當", "당", "to correspond — the same 當 as in 담당, 상당하다")],
            notes=["해당하다 is the word for meeting a category's terms: "
                   "직장 가입자에 해당하는 경우. 해당 사항 없음, “not applicable”, is on "
                   "every Korean form."],
        ),
        "미성년": dict(
            hanja="未成年", meaning="a minor, under age",
            characters=[("未", "미", "not yet — the same 未 as in 미혼"),
                        ("成", "성", "to become, complete — the same 成 as in 조성, 형성"),
                        ("年", "년", "year")],
            notes=["Literally not yet of full years. Its 未 is the same as in 미혼 "
                   "“not yet married”."],
        ),
        "재난": dict(
            hanja="災難", meaning="a disaster",
            characters=[("災", "재", "disaster — the same 災 as in 화재, 산재"),
                        ("難", "난", "difficulty — the same 難 as in 취업난, 난민")],
        ),
        "대비": dict(
            hanja="對備", meaning="preparing against something",
            characters=[("對", "대", "to face, against — as in 대응, 대책, 대상"),
                        ("備", "비", "to prepare — as in 준비, 예비")],
            notes=["Worth separating from 대응: 대비 is getting ready before, 대응 is "
                   "acting when it happens. The passage uses both in one sentence.",
                   "A homonym of 대비 “contrast”, which is 對比 — the second character "
                   "differs."],
        ),
        "행정안전부": dict(
            hanja="行政安全部", meaning="the Ministry of the Interior and Safety",
            characters=[("行", "행", "to go, conduct — the same 行 as in 통행, 시행"),
                        ("政", "정", "government — the same 政 as in 정책, 정부"),
                        ("部", "부", "ministry — the same 部 as in 법무부, 보건복지부")],
            notes=["행정 is public administration; this is the ministry that runs it, "
                   "and with it national disaster management."],
        ),
        "대피": dict(
            hanja="待避", meaning="taking shelter, evacuating",
            characters=[("待", "대", "to wait — as in 기대, 초대"),
                        ("避", "피", "to avoid, flee — as in 회피, 도피")],
            notes=["Literally waiting out of the way. 대피 훈련 is an evacuation drill; "
                   "대피소 is a shelter."],
        ),
        "의무적": dict(
            hanja="義務的", meaning="compulsory",
            characters=[("義", "의", "duty, righteousness — as in 정의 “justice”, 의미"),
                        ("務", "무", "duty — the same 務 as in 업무협약, 공무원"),
                        ("的", "적", "-ic, -al")],
        ),
        "유출": dict(
            hanja="流出", meaning="leakage, an outflow",
            characters=[("流", "류", "to flow — as in 유통, 조류"),
                        ("出", "출", "to go out — the same 出 as in 출입국, 진출")],
            notes=["Of chemicals here; also used of data — 개인정보 유출 is a leak of "
                   "personal information."],
        ),
        "원전": dict(
            hanja="原電", meaning="a nuclear power plant",
            characters=[("原", "원", "origin — the same 原 as in 원리, 원칙적"),
                        ("電", "전", "electricity — the same 電 as in 전광판, 전기")],
            notes=["Short for 원자력 발전소. Korea has several, which is why they appear "
                   "in a list of things to drill for."],
        ),
        "안전사고": dict(
            hanja="安全事故", meaning="an avoidable accident",
            characters=[("安", "안", "peace, safe — as in 안전, 안정"),
                        ("全", "전", "whole, complete — as in 전체, 전국"),
                        ("事", "사", "matter — the same 事 as in 사례, 사건"),
                        ("故", "고", "cause, incident — as in 사고, 고장")],
            notes=["The page's gloss is pointed: an accident arising from too little "
                   "safety training or from carelessness. Not misfortune — negligence."],
        ),
        "매뉴얼": dict(
            meaning="a manual",
            notes=["From English. The page's gloss is worth reading: the knowledge and "
                   "procedures a job needs, set out in order."],
        ),
        "대응": dict(
            hanja="對應", meaning="responding, dealing with",
            characters=[("對", "대", "to face — the same 對 as in 대비, 대책"),
                        ("應", "응", "to respond — the same 應 as in 응급, 응답")],
        ),
        "긴급신고전화": dict(
            hanja="緊急申告電話", meaning="the emergency numbers",
            characters=[("申", "신", "to report, state — as in 신청 “application”, 신고"),
                        ("告", "고", "to tell — as in 보고 “report”, 광고")],
            notes=["119 fire and ambulance, 112 crime, 110 government enquiries, 1339 "
                   "infectious disease. The table on p. 45 adds more: 118 cyber, 120 "
                   "facilities, 122 maritime, 121 water, 123 electricity, 1301 drugs."],
        ),
        "해롭다": dict(
            hanja="害", meaning="to be harmful",
            characters=[("害", "해", "harm — the same 害 as in 산업재해, 피해")],
            notes=["해로운 물질 is a harmful substance. Its opposite is 유익하다, and "
                   "해치다 is the verb: to do the harm."],
        ),
        "해치다": dict(
            hanja="害치다", meaning="to harm, to do damage to",
            characters=[("害", "해", "harm — the same 害 as in 해롭다, 피해, 산업재해")],
            notes=["The verb to 해롭다's adjective: 해롭다 is that a thing is harmful, "
                   "해치다 that someone does the harm. 안전을 해치다 to endanger safety, "
                   "건강을 해치다 to ruin one's health, 기분을 해치다 to spoil a mood.",
                   "Not 해지다 “to wear out, to fray”, which is what the Doc had "
                   "here — one letter apart, and the reason this page carries a "
                   "correction."],
        ),
        "달아나다": dict(
            meaning="to run away, to make off",
            notes=["Of someone leaving the scene: 몰래 다가가 안전을 해치고 달아나다 — "
                   "to slip up to a child, do them harm and make off. The hit-and-run "
                   "driver of the same paragraph 아무런 조치도 없이 달아난다.",
                   "달아나다 is the running; 도망가다 is the same act seen as escape, "
                   "and 도주하다 the word a news report would use."],
        ),
        "당국": dict(
            hanja="當局", meaning="the authorities",
            characters=[("當", "당", "the said, to correspond — the same 當 as in 해당"),
                        ("局", "국", "bureau, office — as in 우체국 “post office”, 방송국")],
            notes=["관계 당국 is the authority concerned — whichever office the matter "
                   "belongs to."],
        ),
        "건의": dict(
            hanja="建議", meaning="a suggestion put to an authority",
            characters=[("建", "건", "to build, propose — as in 건설 “construction”, 건물"),
                        ("議", "의", "to discuss — as in 회의 “meeting”, 의논")],
        ),
        "예방": dict(
            hanja="豫防", meaning="prevention",
            characters=[("豫", "예", "beforehand — the same 豫 as in 예방 접종, 예보"),
                        ("防", "방", "to defend — the same 防 as in 소방서, 국방")],
        ),
        "안전모": dict(
            hanja="安全帽", meaning="a safety helmet",
            characters=[("帽", "모", "hat — as in 모자 “hat”")],
        ),
        "안전화": dict(
            hanja="安全靴", meaning="safety boots",
            characters=[("靴", "화", "shoe — as in 운동화 “trainers”, 구두")],
            notes=["A third 화 for the collection: not the 化 of 도시화 nor the 火 of "
                   "화재, but the 靴 of footwear."],
        ),
        "착용": dict(
            hanja="着用", meaning="wearing, putting on",
            characters=[("着", "착", "to attach, wear — as in 도착 “arrival”, 정착"),
                        ("用", "용", "to use — the same 用 as in 전용, 이용")],
            notes=["The formal word on every safety notice: 안전모를 착용하십시오. In "
                   "speech one says 쓰다, 신다 or 입다 according to what it is."],
        ),
        "용기": dict(
            hanja="容器", meaning="a container",
            characters=[("容", "용", "to contain, appearance — as in 내용 “contents”, 용량"),
                        ("器", "기", "vessel, implement — as in 기구, 식기")],
            notes=["A homonym of 용기 “courage”, which is 勇氣 — different characters "
                   "entirely."],
        ),
        "비상구": dict(
            hanja="非常口", meaning="an emergency exit",
            characters=[("非", "비", "not — as in 비혼, 비공식"),
                        ("常", "상", "usual, constant — as in 평상시, 일상"),
                        ("口", "구", "mouth, opening — the same 口 as in 가구, 출입구")],
            notes=["비상 is literally the not-usual: the emergency. The green running "
                   "figure on every Korean sign."],
        ),
        "구급상자": dict(
            hanja="救急箱子", meaning="a first aid box",
            characters=[("救", "구", "to rescue — as in 구조 “rescue”, 구급차"),
                        ("急", "급", "urgent — the same 急 as in 응급, 긴급"),
                        ("箱", "상", "box"),
                        ("子", "자", "child; a noun suffix")],
        ),
        "소화기": dict(
            hanja="消火器", meaning="a fire extinguisher",
            characters=[("消", "소", "to extinguish — the same 消 as in 소독, 소극적"),
                        ("火", "화", "fire — the same 火 as in 화재"),
                        ("器", "기", "implement — the same 器 as in 용기")],
            notes=["Literally the fire-putting-out implement. A homonym of 소화기 "
                   "“digestive organs”, 消化器 — and the 소화 of 소화가 잘 안 되다 on "
                   "p. 45 is that other one."],
        ),
        "조치": dict(
            hanja="措置", meaning="a measure taken",
            characters=[("措", "조", "to arrange, handle"),
                        ("置", "치", "to place — the same 置 as in 응급 처치, 설치")],
            notes=["아무런 조치도 없이 is the phrase in the box: without taking any "
                   "measure at all — the hit-and-run driver."],
        ),
        "소지품": dict(
            hanja="所持品", meaning="belongings carried on one",
            characters=[("所", "소", "that which — the same 所 as in 소득, 소유권"),
                        ("持", "지", "to hold — as in 유지 “maintenance”, 지참"),
                        ("品", "품", "article — the same 品 as in 품종, 일회용품")],
        ),
        "지능적": dict(
            hanja="知能的", meaning="intelligent, done by machine intelligence",
            characters=[("知", "지", "to know — the same 知 as in 친지, 지식"),
                        ("能", "능", "ability — as in 능력 “ability”, 가능"),
                        ("的", "적", "-ic, -al")],
            notes=["인공지능 is artificial intelligence; here it is the CCTV doing the "
                   "recognising."],
        ),
        "포착": dict(
            hanja="捕捉", meaning="catching, capturing",
            characters=[("捕", "포", "to catch — as in 체포 “arrest”"),
                        ("捉", "착", "to seize")],
            notes=["Of catching something fleeting — an image, a moment, an "
                   "opportunity: 기회를 포착하다."],
        ),
        "추적": dict(
            hanja="追跡", meaning="tracking, pursuit",
            characters=[("追", "추", "to chase — the same 追 as in 추구"),
                        ("跡", "적", "trace, footprint")],
            notes=["Following the traces left behind. 추적하다 of a suspect, a parcel "
                   "or a contact."],
        ),
        "기여": dict(
            hanja="寄與", meaning="contribution",
            characters=[("寄", "기", "to entrust, send — as in 기부 “donation”"),
                        ("與", "여", "to give — the same 與 as in 여건")],
            notes=["기여하다 takes 에: 예방하는 데도 기여할 수 있다."],
        ),
        "산재": dict(
            hanja="産災", meaning="an industrial accident",
            notes=["Short for 산업재해, and for the insurance against it. Met in "
                   "chapters 6 and 7 as 산재보험."],
        ),
        "내국인": dict(
            hanja="內國人", meaning="a national, a citizen of this country",
            characters=[("內", "내", "inside — as in 국내 “domestic”, 시내"),
                        ("國", "국", "country"),
                        ("人", "인", "person")],
            notes=["The counterpart of 외국인, and the comparison the article turns on: "
                   "0.18% against 1.16%."],
        ),
        "발생률": dict(
            hanja="發生率", meaning="rate of occurrence",
            characters=[("發", "발", "to occur, issue — the same 發 as in 재개발, 발달"),
                        ("生", "생", "to arise"),
                        ("率", "률", "rate — the same 率 as in 도시화율, 비율")],
        ),
        "사망자": dict(
            hanja="死亡者", meaning="a person killed, a fatality",
            characters=[("死", "사", "death — the same 死 as in 사별하다"),
                        ("亡", "망", "to perish, flee"),
                        ("者", "자", "person")],
        ),
        "고려": dict(
            hanja="考慮", meaning="consideration, taking into account",
            characters=[("考", "고", "to think, consider — as in 참고 “reference”"),
                        ("慮", "려", "to be anxious, ponder")],
            notes=["A homonym of 고려 the dynasty, 高麗, from which the name Korea "
                   "comes. The article's point is that safety training is given "
                   "without 고려 of language difference."],
        ),
    },

    extraNotes=[
        "The 긴급 신고 전화 box on p. 45 is one titled box holding eight number "
        "pairs, laid out two pairs to a row to fit the margin. It is set here as a "
        "headerless table of eight rows, the book's left-hand column first — the "
        "emergency lines — then its right, the faults and enquiries. The book gives "
        "those two groups no names, so neither does this.",
        "The figure on p. 47 plots total casualties and deaths on one graphic at very "
        "different scales. It is split into two here, because a single bar chart would "
        "flatten the death figures to nothing.",
        "The 생각해 봅시다 photos on p. 44 carry three labels in your hand — 화재, 소독, "
        "지진 — for four pictures. The second picture, of someone on the telephone, has "
        "none, and is left out of the labels.",
    ],
)
