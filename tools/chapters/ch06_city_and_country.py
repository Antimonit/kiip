# -*- coding: utf-8 -*-
"""Chapter 6 — The city and the countryside.

Transcribed in your Google Doc (6.html), whose text is carried in `blocks`
below as the Doc had it. First transcribed from the photos of pp. 36-39; the
two readings were compared line by line when your Doc arrived, and every
difference proved to be a slip in the Doc, listed as fixes below.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, MARGIN,
               TABLE, CELL, CHART, GLOSSARY)

CHAPTER = dict(
    number=6, slug="06-city-and-country",
    unit="사회", title="도시와 농촌", titleEn="The city and the countryside",

    blocks=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 한국의 도시와 농촌의 모습입니다."),
        FIGURE("도시의 모습"),
        HEADING(4, "01 두 사진을 통해 알 수 있는 도시와 농촌의 차이점은 무엇입니까?"),
        FIGURE("농촌의 모습"),
        HEADING(4, "02 본인은 도시와 농촌 중 어느 쪽 풍경에 더 익숙합니까? 그 이유는 무엇입니까?"),
        SECTION("goals", "학습목표"),
        BULLET("한국 도시의 특징과 변화를 설명할 수 있다.", ordered=True),
        BULLET("한국 농촌의 특징과 변화를 설명할 수 있다.", ordered=True),
        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"], [["기본", "경제", "26. 경제 성장",
              "대한민국 경제 성장과정"],
              ["심화", "역사", "8. 사회변동", "저출산 현상, 고령화 사회"]]),
        SECTION("part", "01 한국 도시는 어떤 특징이 있을까?"),
        MARGIN("{농업}", "{공업}", "{서비스업}"),
        HEADING(2, "도시의 특징과 변화", translation="Characteristics and Changes of Cities"
          "\n\n" "\"Korea's urbanization began in earnest as "
          "industrialization took place from the 1960s onward. From "
          "the 1970s, more than half the population came to live in "
          "cities, and now over 90% of the total population resides "
          "in cities. Cities have many companies, universities, "
          "public institutions, medical facilities, and cultural "
          "facilities, making life convenient." "\n\n"
          "The Seoul Capital Area (수도권 — Seoul, Incheon, Gyeonggi) "
          "makes up only about 12% of the national territory (국토), "
          "but is home to about 50% of the total population, making "
          "it a representative urbanized region. Many people also "
          "live in regional metropolitan cities (광역시) such as Busan, "
          "Daegu, Gwangju, Daejeon, and Ulsan." "\n\n"
          "To disperse (분산) functions concentrated in the metropolis, "
          "many satellite cities (위성 도시 — note: your text has a typo, "
          "\"위성 도시,\" but this should read 위성 도시) have been built, "
          "especially around Seoul. Examples include Bundang and "
          "Ilsan, which handle residential functions; Gwacheon, which "
          "handles administrative functions; Ansan and Bucheon, which "
          "have many industrial areas; and Dongducheon and Osan, "
          "which have military facilities. Recently, a phenomenon of "
          "counter-urbanization (역도시화) has also emerged, where people "
          "move to areas around large cities in search of a cleaner, "
          "more pleasant environment.\""),
        GLOSSARY(("도시화", "도시의 생활 양식이 도시 외 지역으로 확대되는 현상", "도시화"),
              ("산업화", "공업 등과 같은 생산 활동이 크게 확대되는 현상", "산업화"),
              ("도시화율", "전체 인구 중 도시에 사는 인구의 비율", "도시화율"),
              ("국토", "한 나라의 통치권이 미치는 지역", "국토"),
              ("분산", "나누어 각각 흩어지게 함", "분산"),
              ("위성 도시", "대도시의 주변에 있는 중소 규모의 도시", "위성 도시")),
        PARAGRAPH("한국의 도시화는 1960년대 이후 산업화가 이루어지면서 {본격적으로|본격적} 시작되었다. "
          "1970년대부터는 인구의 절반 이상이 도시에서 살게 되었고, 현재는 총인구 중 90%가 넘는 사람이 "
          "도시에 거주하고 있다. 도시에는 기업체, 대학, 공공 기관, 의료 시설, 문화 시설 등이 많아 생활이 " "편리하다."),
        PARAGRAPH("서울, 인천, 경기 등 수도권은 국토 {면적}의 약 12% 정도에 {불과하}지만 총인구의 약 50%가 살고 "
          "있는 대표적인 도시화 지역이다. 부산, 대구, 광주, 대전, 울산 등과 같은 지방의 {광역시}에도 많은 "
          "사람이 살고 있다."),
        PARAGRAPH("{대도시}에 집중된 기능을 분산시키기 위해 특히 서울 주변에는 위성 도시들이 많이 만들어졌다. 주거 "
          "기능을 담당하는 분당이나 일산, 행정 기능을 담당하는 과천, 공업 지역이 많은 안산이나 부천, {군사} "
          "시설이 있는 동두천, 오산 등이 그 예이다. 최근에는 보다 깨끗하고 {쾌적한|쾌적하다} 환경을 찾아 "
          "대도시 주변 지역으로 이동하는 {역도시화} 현상도 나타나고 있다."),
        CHART("도시화율(단위: %)", "%", [["1960년", 39.1],
              ["1970년", 50.1],
              ["1980년", 68.7],
              ["1990년", 79.6],
              ["2000년", 88.3],
              ["2010년", 90.9],
              ["2019년", 92.0]]),
        HEADING(2, "도시 문제와 대책", translation="Urban Problems and Countermeasures"
          "\n\n" "\"Urban problems arise in many cities. Traffic, "
          "environmental, and housing problems are representative "
          "examples. To solve traffic problems such as traffic "
          "congestion, insufficient public transportation, and lack "
          "of parking facilities, measures like expanding public "
          "transportation (대중교통수단 확충), transfer discounts, the "
          "bus-only lane system, and congestion tolls (혼잡 통행료) are "
          "being implemented. To solve environmental problems such as "
          "air pollution and water pollution, efforts like energy "
          "conservation, waste separation and collection, and "
          "regulation of disposable products are being made. "
          "Meanwhile, to solve problems of housing shortages or aging "
          "housing, measures such as distributing public rental "
          "housing, building new towns, and urban redevelopment "
          "projects are being implemented.\""),
        GLOSSARY(("확충", "늘리고 넓혀 충실하게 함", "확충"),
              ("혼잡 통행료", "교통 혼잡 지역을 통행하는 자가용을 대상으로 통행료를 받는 제도", "혼잡 통행료")),
        PARAGRAPH("많은 도시에서 도시 문제가 발생한다. 교통, 환경, 주택 문제 등이 대표적인 예이다. 교통 혼잡, "
          "대중교통 부족, 주차 시설 부족 등과 같은 교통 문제를 해결하기 위해 대중교통수단 확충, 대중교통 환승 "
          "할인, 버스 전용 차로제, 혼잡 통행료 등을 실시하고 있다. {대기} 오염, {수질} 오염 등과 같은 "
          "환경 문제를 해결하기 위해서 에너지 절약, 쓰레기 분리수거, 일회용품 {규제} 등의 노력을 {기울}이고 "
          "있다. 한편, 주택 부족이나 낡은 주택 문제를 해결하기 위해 공공 임대 주택 {보급}, 신도시 건설, "
          "도시 재개발 사업 등을 실시하고 있다."),
        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "도시 재생 사업으로 확 달라진 우리 마을 (부산 영도 깡깡이 마을)"),
        PARAGRAPH("부산시 영도구의 깡깡이 마을은 우리나라 최초의 조선소가 세워져 번영을 누렸던 곳이다. 지금은 다소 발전이 "
          "뒤쳐졌지만 기존의 역사적 시설들을 새롭게 정비하면서 최근 관광객의 방문이 증가하고 있다. 도시 재생 "
          "사업은 도시 안의 쇠퇴한 지역에 새로운 기능을 도입하여 지역을 다시 일으키는 사업이다. 이를 통해 "
          "낙후되었던 지역에 관광객이 늘고 일자리가 많아지는 등 활기를 찾는 긍정적인 효과가 나타나고 있다."),
        FIGURE("부산 도시 재생 지역 중 하나인 부산 영도의 깡깡이 마을"),
        SECTION("part", "02 한국 농촌은 어떤 특징이 있을까?"),
        MARGIN("농촌 사람들은 이웃집 숟가락 개수를 안다"),
        HEADING(2, "농촌의 특징과 변화", translation=
          "Characteristics and Changes of Rural Areas" "\n\n"
          "\"In rural areas, since many people have farmed together "
          "and lived in the same village for a long time, "
          "relationships between people tend to be close-knit. Rural "
          "areas have facilities such as: the village hall, a space "
          "for holding meetings or gathering to rest; agricultural "
          "product storage warehouses, which can safely store crops "
          "for long periods; rice mills, where harvested rice is "
          "milled; and artificial waterways, which draw water from "
          "nearby streams to supply water to farmland." "\n\n"
          "Even up until the 1960s, Korea's rural population was "
          "larger than its urban population. However, as the trend of "
          "leaving villages for cities — for study, employment, "
          "marriage, etc. — increased, the rural population greatly "
          "declined. According to a 2018 Statistics Korea survey, the "
          "rural population is about 2.3 million, just a bit over 5% "
          "of the total population. Rural areas are now facing new "
          "changes. By selling agricultural products directly to "
          "cities through direct-sale farmers' markets or websites, "
          "benefits are being provided to both rural producers and "
          "urban consumers. Additionally, rural areas run weekend "
          "farms or rural experience programs, and hold festivals "
          "that promote local tradition and culture using their "
          "natural environment and local specialty products — "
          "sometimes developing these into tourism industries.\""),
        GLOSSARY(("찧다", "곡식의 껍질을 벗기거나 가루로 만들려고 내리침", "찧다"),
              ("촌락", "주로 시골에서 여러 집이 모여 사는 곳", "촌락"),
              ("직거래", "물건을 파는 사람과 사는 사람이 중간 상인을 거치지 않고 직접 거래", "직거래")),
        PARAGRAPH("{농촌}은 {대체로} 함께 {농사}를 지으며 같은 마을에서 오랫동안 살아온 사람들이 많아 사람 간의 "
          "관계가 친밀한 편이다. 농촌에는 회의를 하거나 모여서 쉬는 공간인 마을 {회관}, {농산물}을 안전하게 "
          "오랜 기간 {보관}할 수 있는 농산물 저장 창고, {수확한} 벼를 찧는{정미소}, 주변의 하천에서 물을 "
          "끌어와 {농지}에 물을 {공급해} 주는 인공 수로 등의 시설이 있다."),
        PARAGRAPH("1960년대까지만 해도 한국에는 농촌 인구가 도시 인구보다 더 많았다. 그러나 공부, 취업, 결혼 등을 "
          "위해 촌락을 떠나 도시로 이동하는 현상이 증가하면서 농촌의 인구는 크게 줄어들었다. 2018년 {통계청} "
          "조사에 따르면 농촌 인구는 약 230만 명으로 전체 인구의 5%를 조금 넘는 수준이다. 농촌은 새로운 "
          "변화를 맞이하고 있다. 농산물 직거래장터나 사이트를 통해 농산물을 도시에 직접 판매하면서 농촌의 생산자와 "
          "도시의 소비자 모두에게 {이익}을 주고 있다. 또한, 주말 {농장}이나 농촌 체험 프로그램을 운영하거나 "
          "자연환경, {특산물} 등을 이용하여 지역의 전통과 문화를 알리는 축제를 열고 이를 {관광업}으로 " "발전시키기도 한다."),
        CHART("농가인구(통계청, 2018)(단위: 천 명)", "천 명", [["2016년", 2496],
              ["2017년", 2422],
              ["2018년", 2315]]),
        CHART("농가의 고령인구 비율, 65세 이상(통계청, 2018)(단위: %)", "%", [["2016년", 40.3],
              ["2017년", 42.5],
              ["2018년", 44.7]]),
        HEADING(2, "농촌 문제와 대책", translation="Rural Problems and Countermeasures"
          "\n\n" "Rural areas also have problems that need solving. First is "
          "the labor shortage caused by the aging of the rural "
          "population. According to a 2018 Statistics Korea survey, "
          "elderly people are so numerous in rural areas that those "
          "aged 65 and over make up about 45% of the population. To "
          "address this, local governments in rural regions are "
          "providing substantial support to people wanting to return "
          "to farming (귀농). Efforts are also continuing to raise "
          "agricultural productivity through new technology, crop "
          "variety development, and mechanization/automation of " "farming."
          "\n\n" "Meanwhile, rural areas are lacking compared to cities in "
          "aspects such as cultural facilities, medical facilities, "
          "and digitalization. To solve this, closed schools and "
          "village halls are sometimes converted into cultural "
          "facilities, and convenience facilities such as clinics and "
          "hospitals are being increased. Digitalization education, "
          "such as internet training, is also being carried out."),
        GLOSSARY(("귀농", "도시에서 다른 일을 하던 사람이 농촌으로 돌아감", "귀농"),
              ("생산성", "효율적으로 생산할 수 있는 정도", "생산성"),
              ("개조", "고쳐서 다시 만듦", "개조")),
        PARAGRAPH("농촌에도 해결해야 할 문제가 있다. 우선 농촌 인구의 {고령화}로 인한 {일손} 부족을 꼽을 수 있다. "
          "2018년 통계청 조사에 따르면, 농촌에는 만 65세 이상 인구가 약 45%를 {차지할} 정도로 노인이 "
          "많다. 이를 해결하기 위해 농촌 지역의 {지방자치단체}에서는 귀농을 하려는 사람에게 많은 지원을 하고 "
          "있다. 또한 새로운 기술이나 {품종} 개발, 농업의 기계화, 자동화 등을 통해 농촌의 생산성을 높이는 "
          "노력도 계속하고 있다. 한편, 농촌은 문화 시설, 의료 시설, {정보화} 등의 {측면}에서 도시에 비해 "
          "부족한 측면이 있다. 이를 해결하기 위해 {폐교}, 마을 회관 등을 문화 시설로 개조하기도 하고 "
          "병·의원 등과 같은 편의 시설을 늘리고 있다. 또한 인터넷 등과 같은 정보화 교육을 실시하기도 한다."),
        FIGURE("딸기 수확 로봇 — 일손 부족 문제를 해결하기 위해 여러 기술이 개발되고 있다."),
        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "한국의 농촌을 체험해 볼까?"),
        PARAGRAPH("농촌 생활을 체험을 할 수 있는 농촌 체험 마을이 많이 조성되고 있다. 농사 체험, 특산물이나 농작물 "
          "수확 체험, 수확한 작물을 활용한 음식 만들기, 고추장 만들기, 두부 만들기, 메기 잡기, 야외 사육 "
          "체험, 원두막 만들기, 도자기 만들기 등 다양한 농촌 문화를 체험할 수 있다. 농어촌 정보 포털 "
          "서비스(농어촌 알리미, https://www.alimi.or.kr)를 통해 전국에서 운영 중인 농촌 체험 "
          "마을 정보를 얻을 수 있다."),
        SECTION("review", "주요 내용정리"),
        MARGIN("{농번기}", "{농한기}"),
        HEADING(2, "01 한국 도시는 어떤 특징이 있을까?"),
        BULLET("한국의 도시화는 1960년대 이후 (   )가 이루어지면서 시작되었으며 현재는 총인구 중 약 90%가 ( "
          "도시 )에 거주하고 있다."),
        BULLET("도시에는 기업체, 대학, 공공 기관, 의료 시설, 문화 시설 등이 많아 생활이 편리하다. 특히 대도시에 "
          "이러한 기능이 집중되어 있는데 이를 분산시키기 위해 (   )가 만들어졌다."),
        BULLET("도시에서는 (   ) 문제, (   ) 문제, 주택 문제 등과 같은 도시 문제가 발생한다. 이를 해결하기 위해 대중교통 이용 장려, 에너지 절약, 신도시 건설과 같은 다양한 노력을 기울이고 있다."),
        HEADING(2, "02 한국 농촌은 어떤 특징이 있을까?"),
        BULLET("농촌은 (   ) 장터나 사이트 운영, 주말 농장이나 농촌 체험 프로그램 운영, 자연환경이나 특산물을 "
          "이용한 (   ) 개최 등을 통해 농촌은 변화하려는 노력을 계속하고 있다."),
        BULLET("농촌에는 주로 (   )이 많고 젊은 사람들이 많지 않아서 일손이 부족하다. 이를 해결하기 위해 귀농 "
          "지원, 농업의 기계화, 자동화 등의 노력이 이루어지고 있다."),
        SECTION("discuss", "이야기 나누기"),
        HEADING(2, "외국인 계절 근로자 최장 '5개월' 고용", translation=
          "Foreign Seasonal Workers to Be Employed for a Maximum of "
          "'5 Months'" "\n\n"
          "The foreign seasonal worker system is designed to allow "
          "foreign workers to work short-term in designated farm "
          "jobs, in order to ease labor shortages during the busy "
          "farming season (농번기). Seasonal workers are selected either "
          "from family members within the 4th degree of kinship (4촌) "
          "of marriage immigrants residing in Korea, or from people "
          "selected by local governments in countries that have "
          "signed a memorandum of understanding(MOU) with a Korean "
          "local government. Previously, workers entered on a "
          "\"short-term employment (C-4) visa\" and could stay for 3 "
          "months, but this time a new \"(E-8) visa\" has been "
          "created, extending the stay period to 5 months. "
          "Additionally, previously, in the case of marriage "
          "immigrants' family members, industrial accident insurance "
          "(산재보험) enrollment was not permitted on the grounds that "
          "they were family rather than in an employment relationship "
          "with the farm household in question — but now, if an "
          "employment relationship is recognized through an "
          "employment contract, marriage immigrants' family members "
          "can also enroll in industrial accident insurance."),
        PARAGRAPH("외국인 계절 {근로자} 제도는 {농번기} 일손 부족을 {완화하|완화}고자 외국인 근로자들이 {단기간} "
          "지정된 농가에서 일할 수 있도록 한 것이다. 계절 근로자는 한국에 거주하는 결혼이민자의 4촌 이내 가족 "
          "또는 우리 지방자치단체와 업무{협약|업무협약}(MOU)을 {체결한|체결} 국가의 {지자체}가 {선정한} "
          "사람 중에서 뽑는다. 기존에는 ‘단기취업(C-4) 비자’로 들어와 3개월 체류할 수 있었으나 이번에 ‘(E-8) 비자’를 신설하여 5개월로 체류기간을 연장할 수 있게 되었다. 또한 기존에는 결혼이민자 가족의 "
          "경우 해당 농가와 {고용}관계가 아닌 가족이라는 이유로 {산재}보험 가입을 허용하지 않았으나 근로계약서를 "
          "통해 고용관계가 인정되면 결혼이민자의 가족도 산재보험에 가입할 수 있게 되었다."),
        CHART("외국인 계절 근로자 배정현황(법무부·농림축산식품부)(단위: 명)", "명", [["2015년", 19],
              ["2016년", 241],
              ["2017년", 1175],
              ["2018년", 2936],
              ["2019년", 3612],
              ["2020년", 5000]]),
        SOURCE("[출처] 농민신문(2019.12.18)"),
        PARAGRAPH("★ 계절 근로자 제도의 좋은 점과 보완되어야 할 점에 대해 이야기해 봅시다.",
          "Talk about what is good about the seasonal worker system and what "
          "still needs to be put right."),
    ],
    annotations={
        "도시화": dict(
            meaning="urbanization",
        ),
        "산업화": dict(
            meaning="industrialization",
        ),
        "도시화율": dict(
            meaning="urbanization rate",
        ),
        "국토": dict(
            meaning="national territory",
        ),
        "분산": dict(
            meaning="dispersion/decentralization",
            notes=["인구 분산 = \"population dispersion,\" a common policy term "
                "for spreading population away from overcrowded cities"],
        ),
        "위성 도시": dict(
            meaning="satellite city",
        ),
        "본격적": dict(
            headword="본격적으로",
            meaning="in earnest/full-scale",
            notes=["본격적으로 시작되었다 = \"began in earnest/full swing\""],
            surfaces=["본격적으로"],
        ),
        "면적": dict(
            meaning="\"area\"",
            notes=["건물의 총 면적 = \"the building's total floor area\"."],
        ),
        "불과하": dict(
            headword="불과하다",
            meaning="merely/to be no more than",
            notes=["literally \"not exceeding,\" used to downplay a small "
                "amount.", "12% 정도에 불과하지만 = \"though it's merely about 12%\""],
        ),
        "광역시": dict(
            meaning="metropolitan city",
            notes=["a designation for Korea's major regional cities (Busan, "
                "Daegu, etc.) that have metropolitan-level administrative "
                "status separate from their surrounding province"],
        ),
        "대도시": dict(
            meaning="big city/metropolis",
        ),
        "군사": dict(
            meaning="military affairs",
        ),
        "쾌적하다": dict(
            meaning="pleasant/comfortable",
            notes=["쾌적한 환경 = \"a pleasant environment\", as in your passage."],
            surfaces=["쾌적한"],
        ),
        "역도시화": dict(
            meaning="counter-urbanization/reverse urbanization",
            notes=["逆 (reverse/opposite, same 逆 as in 역방향 \"opposite "
                "direction\")", "도시화 (urbanization)",
                "the phenomenon of people moving away from large cities "
                "toward surrounding areas, the opposite trend of 도시화"],
        ),
        "확충": dict(
            meaning="expansion and enhancement",
            notes=["literally \"expanding and filling\", meaning to increase "
                "and strengthen something (facilities, systems, capacity) "
                "so it becomes more substantial",
                "시설 확충 = \"expansion of facilities\""],
        ),
        "혼잡 통행료": dict(
            meaning="congestion toll",
            notes=["a system that charges a toll fee to private cars (자가용) "
                "passing through traffic-congested areas, intended to "
                "discourage driving in heavily congested zones and "
                "encourage public transit use"],
        ),
        "대기": dict(
            meaning="atmosphere",
            notes=["대기 오염 = \"air pollution\""],
        ),
        "수질": dict(
            meaning="water quality",
            notes=["수질 오염 = \"water pollution\""],
        ),
        "규제": dict(
            meaning="regulation",
            notes=["規 (rule/standard, same 規 as in 규모 \"scale\")",
                "制 (system/regulation, same 制 as in 제도)",
                "일회용품 규제 = \"regulation of disposable products\""],
        ),
        "기울": dict(
            headword="기울다",
            meaning="to tilt/lean",
            notes=["기울이다 — to devote/incline",
                "노력을 기울이다 — \"to devote effort/make an effort\""],
        ),
        "보급": dict(
            meaning="distribution/spread",
            notes=["공공 임대 주택 보급 = \"distribution of public rental housing\""],
        ),
        "찧다": dict(
            meaning="to pound/mill (grain)",
            notes=["벼를 찧다 = \"to mill rice\""],
        ),
        "촌락": dict(
            meaning="village/settlement",
            notes=["村 (village, same 村 as in 농촌)",
                "落 (to settle/fall, here meaning a settled place)",
                "a place where several households live together, mainly in "
                "rural areas."],
        ),
        "직거래": dict(
            meaning="direct transaction",
            notes=["buying/selling directly between seller and buyer without "
                "going through a middleman",
                "농산물 직거래 = \"direct farm-produce sales\""],
        ),
        "농촌": dict(
            meaning="rural village/countryside",
        ),
        "대체로": dict(
            meaning="generally/on the whole",
        ),
        "농사": dict(
            meaning="farming",
            notes=["農 (farming)", "事 (affair/matter, same 事 as in 사건, 군사)",
                "농사를 짓다 = \"to farm/do farming\""],
        ),
        "회관": dict(
            meaning="hall/assembly building",
            notes=["會 (meeting/gathering, same 會 as in 회의 \"meeting\")",
                "館 (building/hall, same 館 as in 도서관 \"library\")",
                "마을 회관 = \"village hall\""],
        ),
        "농산물": dict(
            meaning="agricultural products",
            notes=["農 (farming)",
                "産 (to produce, same 産 as in 부동산 \"real estate\" and 산업 "
                "\"industry\")", "物 (thing/object, same 物 as in 소화물)",
                "crops/farm produce"],
        ),
        "보관": dict(
            meaning="storage/safekeeping",
            notes=["保 (to protect/keep, same 保 as in 보증금)",
                "管 (to manage/tube — extended to mean \"to keep/oversee\")",
                "안전하게 보관하다 = \"to store safely\""],
        ),
        "수확한": dict(
            headword="수확하다",
            meaning="to harvest",
            notes=["수확한 벼 = \"harvested rice\""],
        ),
        "정미소": dict(
            meaning="\"rice mill\"",
            notes=["精 (to refine/polish, same 精 as in 정밀 \"precision\")",
                "米 (rice, uncooked grain)", "所 (place, same 所 as in 소유권's 所)",
                "literally \"rice-refining place\", a facility where "
                "harvested rice grains are milled/polished into edible "
                "white rice"],
        ),
        "농지": dict(
            meaning="farmland",
        ),
        "공급해": dict(
            headword="공급하다",
            meaning="to supply",
            notes=["供 (to provide)",
                "給 (to give, same 給 as in 월급 \"monthly salary\")",
                "물을 공급하다 = \"to supply water\"", "수요 = \"demand\""],
        ),
        "통계청": dict(
            meaning="Statistics Korea",
            notes=["the government agency that compiles national statistics"],
        ),
        "이익": dict(
            meaning="benefit/profit",
            notes=["利 (benefit/advantage, same 利 as in 편리하다 \"convenient\")",
                "益 (benefit/gain, same 益 as in 유익하다 \"beneficial\")",
                "이익을 주다 = \"to provide benefit\"",
                "이익을 얻다 = \"to gain profit\""],
        ),
        "농장": dict(
            meaning="\"farm\"",
            notes=["주말 농장 = \"weekend farm\""],
        ),
        "특산물": dict(
            meaning="local specialty product",
            notes=["a product distinctively associated with/produced in a "
                "particular region"],
        ),
        "관광업": dict(
            meaning="tourism industry",
            notes=["관광업으로 발전시키다 = \"to develop into a tourism industry\""],
        ),
        "귀농": dict(
            meaning="return to farming",
            notes=["someone who was doing other work in the city returning to "
                "rural areas to farm"],
        ),
        "생산성": dict(
            meaning="productivity",
            notes=["生産 (production, 生 = life/produce, 産 = to produce, same 産 "
                "as in 농산물, 부동산)", "性 (-ness/quality suffix, same 性 as in 접근성 "
                "\"accessibility\")",
                "the degree to which something can be produced efficiently"],
        ),
        "개조": dict(
            meaning="renovation/remodeling",
            notes=["改 (to change/reform, same 改 as in 개선 \"improvement\")",
                "造 (to make/build, same 造 as in 제조 \"manufacturing\")",
                "문화 시설로 개조하다 = \"to renovate/convert into a cultural "
                "facility\""],
        ),
        "고령화": dict(
            meaning="aging",
            characters=[("高", None, "high"), ("齡", None, "age, same 齡 as in 연령"
                ), ("化", None, "(-ization suffix)")],
            notes=["인구의 고령화 = \"the aging of the population\""],
        ),
        "일손": dict(
            meaning="manpower/labor hands",
            notes=["일 (\"work\") + 손 (\"hand\")", "일손 부족 = \"labor shortage\""],
        ),
        "차지할": dict(
            headword="차지하다",
            meaning="to occupy/take up",
            notes=["45%를 차지할 정도로 = \"to the extent of occupying/making up "
                "45%\""],
        ),
        "지방자치단체": dict(
            meaning="local government",
            notes=["literally \"local self-governing body\", referring to "
                "city/provincial/county governments as opposed to the "
                "central government"],
        ),
        "품종": dict(
            meaning="variety/breed (of crop, livestock, etc.)",
            notes=["品 (item/quality, same 品 as in 제품 \"product\")",
                "種 (species/type, same 種 as in 종류 \"kind/type\")",
                "새로운 품종 개발 = \"development of new crop varieties\""],
        ),
        "정보화": dict(
            meaning="informatization/digitalization",
            notes=["정보화 교육 = \"digital literacy education\""],
        ),
        "측면": dict(
            meaning="aspect/side",
            notes=["側 (side, same 側 as in 측정 \"measurement\")",
                "面 (face/surface, same 面 as in 면적)",
                "여러 측면에서 = \"from various aspects\""],
        ),
        "폐교": dict(
            meaning="closed/abandoned school",
            notes=["a school building no longer in use due to closure (common "
                "in depopulating rural areas)"],
        ),
        "근로자": dict(
            meaning="worker/laborer",
            notes=["a formal term for \"worker\", commonly used in labor "
                "law/policy contexts"],
        ),
        "농번기": dict(
            meaning="busy farming season",
            notes=["the season when farm work is at its busiest "
                "(planting/harvesting times)"],
        ),
        "완화": dict(
            headword="완화하다",
            meaning="to ease/alleviate",
            notes=["일손 부족을 완화하고자 = \"in order to ease the labor shortage\""],
            surfaces=["완화하"],
        ),
        "단기간": dict(
            meaning="short period/short-term",
            notes=["단기간 일하다 = \"to work short-term\""],
        ),
        "업무협약": dict(
            meaning="협약 — agreement/accord",
            notes=["協 (to cooperate, same 協 as in 협력 \"cooperation\")",
                "約 (promise/agreement, same 約 as in 계약 \"contract\")",
                "업무협약 = \"business/cooperation agreement(MOU)\""],
            surfaces=["협약"],
        ),
        "체결": dict(
            headword="체결하다",
            meaning="to conclude/sign (an agreement)",
            notes=["협약을 체결하다 = \"to conclude/sign an agreement\""],
            surfaces=["체결한"],
        ),
        "지자체": dict(
            meaning="지방자치단체 — local government",
        ),
        "선정한": dict(
            headword="선정하다",
            meaning="to select/designate",
            notes=["지자체가 선정한 사람 = \"people selected by the local government\""],
        ),
        "고용": dict(
            meaning="employment",
        ),
        "산재": dict(
            meaning="산업재해 —  industrial accident",
            notes=["산재보험 = \"industrial accident insurance\", covering workers "
                "injured on the job"],
        ),
    },
    headwords={"쾌적한": "쾌적하다", "뒤쳐졌지만": "뒤쳐지다", "낙후되었던": "낙후되다",
               # the Doc comments on half of a compound; file it under the whole
               "본격적으로": "본격적", "완화하": "완화", "체결한": "체결",
               "협약": "업무협약"},

    english={
        "도시의 특징과 변화": dict(
            title="What marks a Korean city, and how it changed",
            paragraphs=[
                "Urbanisation in Korea began in earnest as industrialisation "
                "proceeded from the 1960s on. From the 1970s more than half the "
                "population came to live in cities, and at present more than 90 per "
                "cent of the total population resides in them. Cities have many "
                "businesses, universities, public institutions, medical facilities and "
                "cultural facilities, which makes life convenient.",

                "The capital region — Seoul, Incheon and Gyeonggi — comes to only "
                "about 12 per cent of the national territory, yet about 50 per cent "
                "of the total population lives there, which makes it the urbanised "
                "region above all others. A great many people also live in the "
                "provincial metropolitan cities such as Busan, Daegu, Gwangju, "
                "Daejeon and Ulsan.",

                "To disperse the functions concentrated in the large cities, a great "
                "many satellite cities were built, particularly around Seoul. Bundang "
                "and Ilsan, which carry the residential function; Gwacheon, which "
                "carries the administrative one; Ansan and Bucheon, with their "
                "industrial districts; Dongducheon and Osan, with their military "
                "installations — these are the examples. Lately there is also "
                "counter-urbanisation, people moving out to the areas around the large "
                "cities in search of a cleaner and pleasanter environment.",
            ],
        ),
        "도시 문제와 대책": dict(
            title="The problems of cities, and what is done about them",
            paragraphs=[
                "Urban problems arise in many cities. Those of transport, the "
                "environment and housing are the standing examples. To solve transport "
                "problems such as congestion, too little public transport and too few "
                "parking places, there are expanded public transport, transfer "
                "discounts, bus-only lanes and congestion charges. To solve "
                "environmental problems such as air and water pollution, efforts are "
                "put into saving energy, separating refuse for collection and "
                "regulating disposable goods. To solve the shortage of housing and the "
                "problem of housing that has aged, meanwhile, there is the supply of "
                "public rental housing, the building of new towns and urban "
                "redevelopment.",
            ],
        ),
        "농촌의 특징과 변화": dict(
            title="What marks the countryside, and how it changed",
            paragraphs=[
                "In the countryside many people have farmed together and lived in the "
                "same village a long time, so relations between them tend to be close. "
                "A rural village has such facilities as the village hall, a space for "
                "holding meetings or gathering to rest; the produce store, where crops "
                "can be kept safely for long periods; the mill, where the harvested "
                "rice is hulled; and artificial watercourses, which draw water from "
                "the streams nearby and supply it to the fields.",

                "As late as the 1960s the rural population of Korea was larger than "
                "the urban one. But as more and more people left the villages for the "
                "cities to study, to find work or to marry, the rural population fell "
                "sharply. According to a 2018 survey by Statistics Korea it is about "
                "2.3 million, a little over 5 per cent of the whole. The countryside "
                "is meeting new changes. Selling produce directly to the cities "
                "through direct-trade markets and websites benefits both the rural "
                "producer and the urban consumer. Weekend farms and rural experience "
                "programmes are run as well, and festivals held that make a region's "
                "traditions and culture known through its natural setting and local "
                "specialities, and these are sometimes grown into a tourist trade.",
            ],
        ),
        "농촌 문제와 대책": dict(
            title="The problems of the countryside, and what is done about them",
            paragraphs=[
                "The countryside has problems of its own to solve. The first to point "
                "to is the shortage of hands caused by the ageing of the rural "
                "population. According to a 2018 survey by Statistics Korea, the "
                "elderly are so numerous in the countryside that those aged 65 and "
                "over make up about 45 per cent of it. To address this, local "
                "authorities in rural areas give a great deal of support to those who "
                "mean to return to farming. Efforts also continue to raise rural "
                "productivity through new techniques, the development of varieties, "
                "and the mechanisation and automation of agriculture. The countryside "
                "is, meanwhile, less well provided than the city in respect of "
                "cultural facilities, medical facilities and access to information. To "
                "address that, closed schools and village halls are converted into "
                "cultural facilities and amenities such as clinics and surgeries are "
                "being added. Education in the use of the internet and the like is "
                "also provided.",
            ],
        ),
    },

    extraAnnotations={
        "농업": dict(
            hanja="農業", meaning="agriculture",
            characters=[("農", "농", "farming — the 農 of 농촌, 농사, 농민"),
                        ("業", "업", "occupation, industry — the same 業 as in 산업, 취업")],
            notes=["Your note in the margin of p. 37 sets the three sectors side by "
                   "side: 농업, 공업, 서비스업."],
        ),
        "공업": dict(
            hanja="工業", meaning="industry, manufacturing",
            characters=[("工", "공", "work, craft — as in 공장 “factory”, 공사"),
                        ("業", "업", "occupation, industry")],
            notes=["Narrower than English “industry”: it is manufacturing "
                   "specifically, which is what 산업화 expands."],
        ),
        "서비스업": dict(
            meaning="the service industry",
            notes=["English 서비스 plus 業. The third of the three sectors in your "
                   "margin note, after 농업 and 공업."],
        ),
        "도시화": dict(
            hanja="都市化", meaning="urbanisation",
            characters=[("都", "도", "capital, city — as in 수도 “capital”, 도시"),
                        ("市", "시", "city, market — the same 市 as in 시외버스, 시장"),
                        ("化", "화", "-isation — the same 化 as in 산업화, 고령화")],
            notes=["The page glosses it as the spread of the city's way of living "
                   "beyond the city, which is broader than people simply moving in."],
        ),
        "산업화": dict(
            hanja="産業化", meaning="industrialisation",
            characters=[("産", "산", "to produce — as in 생산, 부동산"),
                        ("業", "업", "occupation, industry"),
                        ("化", "화", "-isation")],
        ),
        "도시화율": dict(
            hanja="都市化率", meaning="the rate of urbanisation",
            characters=[("率", "률/율", "rate, proportion — as in 비율, 이혼율, 경쟁률")],
            notes=["The share of the whole population living in cities. The figure "
                   "beside the passage runs from 39.1% in 1960 to 92% in 2019."],
        ),
        "본격적": dict(
            hanja="本格的", meaning="in earnest, full-scale",
            characters=[("本", "본", "origin, main — the same 本 as in 본뜨다, 해례본"),
                        ("格", "격", "form, standard — as in 자격 “qualification”, 격차"),
                        ("的", "적", "-ic, -al — as in 탄력적, 소극적")],
        ),
        "거주": dict(
            hanja="居住", meaning="to reside",
            characters=[("居", "거", "to dwell — as in 독거노인, 거처"),
                        ("住", "주", "to dwell — the same 住 as in 주거, 주택")],
        ),
        "수도권": dict(
            hanja="首都圈", meaning="the capital region",
            characters=[("首", "수", "head — as in 수상, 수석"),
                        ("都", "도", "capital, city"),
                        ("圈", "권", "sphere, zone — the same 圈 as in 역세권, 생활권")],
            notes=["Seoul, Incheon and Gyeonggi taken together: 12 per cent of the "
                   "land and about half the population."],
        ),
        "국토": dict(
            hanja="國土", meaning="national territory",
            characters=[("國", "국", "country — the same 國 as in 한국, 국기"),
                        ("土", "토", "earth, soil — as in 토지 “land”, 영토")],
        ),
        "광역시": dict(
            hanja="廣域市", meaning="a metropolitan city",
            characters=[("廣", "광", "wide, broad — as in 광고 “advertisement”, 확대"),
                        ("域", "역", "region — as in 지역, 영역"),
                        ("市", "시", "city")],
            notes=["An administrative rank of its own, level with a province: Busan, "
                   "Daegu, Gwangju, Daejeon, Ulsan and Incheon."],
        ),
        "분산": dict(
            hanja="分散", meaning="to disperse, spread out",
            characters=[("分", "분", "to divide — as in 분리 “separation”, 분업"),
                        ("散", "산", "to scatter — as in 확산 “spread”, 해산")],
        ),
        "위성 도시": dict(
            hanja="衛星都市", meaning="a satellite city",
            characters=[("衛", "위", "to guard — as in 위생 “hygiene”, 호위"),
                        ("星", "성", "star — as in 화성 “Mars”, 성좌")],
            notes=["A middling town round a large city that takes on one of its "
                   "functions: housing at Bundang and Ilsan, administration at "
                   "Gwacheon, industry at Ansan and Bucheon."],
        ),
        "역도시화": dict(
            hanja="逆都市化", meaning="counter-urbanisation",
            characters=[("逆", "역", "reverse, against — as in 역방향, 반역"),
                        ("都", "도", "city"),
                        ("化", "화", "-isation")],
            notes=["The 역 turns 도시화 around: people leaving the city for its edges. "
                   "A different 역 from the 驛 of 지하철역."],
        ),
        "혼잡": dict(
            hanja="混雜", meaning="congestion, crowdedness",
            characters=[("混", "혼", "to mix — as in 혼합 “mixture”, 혼동"),
                        ("雜", "잡", "mixed, miscellaneous — as in 복잡하다 “complicated”")],
        ),
        "확충": dict(
            hanja="擴充", meaning="expansion, building out",
            characters=[("擴", "확", "to expand — the same 擴 as in 확대 “enlargement”"),
                        ("充", "충", "to fill — as in 충전 “charging”, 보충")],
            notes=["Glossed on the page as 늘리고 넓혀 충실하게 함 — not just more of a "
                   "thing but a fuller provision of it."],
        ),
        "혼잡 통행료": dict(
            hanja="混雜通行料", meaning="a congestion charge",
            characters=[("通", "통", "to pass through — the same 通 as in 교통, 통행"),
                        ("行", "행", "to go — as in 여행, 행동"),
                        ("料", "료", "fee, material — as in 요금, 자료")],
            notes=["Charged on private cars passing through a congested area. In Seoul "
                   "the Namsan tunnels are the standing example."],
        ),
        "분리수거": dict(
            hanja="分離收去", meaning="separating refuse for collection",
            characters=[("分", "분", "to divide"),
                        ("離", "리", "to separate — as in 이혼 “divorce”, 거리"),
                        ("收", "수", "to collect — as in 수입, 수거"),
                        ("去", "거", "to go, remove — as in 과거 “the past”, 제거")],
            notes=["Sorting waste into food, paper, plastic, glass and the rest, which "
                   "in Korea is a legal duty rather than a courtesy."],
        ),
        "규제": dict(
            hanja="規制", meaning="regulation, restriction",
            characters=[("規", "규", "rule — the same 規 as in 대규모, 규칙"),
                        ("制", "제", "system, to control — the same 制 as in 제도, 차로제")],
        ),
        "재개발": dict(
            hanja="再開發", meaning="redevelopment",
            characters=[("再", "재", "again — the same 再 as in 재해석하다, 재취업"),
                        ("開", "개", "to open — as in 개발, 개천절"),
                        ("發", "발", "to issue, develop — as in 발달, 발음")],
            notes=["Clearing and rebuilding, as against 도시 재생, which keeps what is "
                   "there and puts it to a new use. The chapter has both."],
        ),
        "조선소": dict(
            hanja="造船所", meaning="a shipyard",
            characters=[("造", "조", "to make, build — as in 제조 “manufacture”, 개조"),
                        ("船", "선", "ship — as in 여객선, 선박"),
                        ("所", "소", "place — the same 所 as in 정미소, 주소")],
            notes=["Korea's first was at 깡깡이 마을 in Yeongdo, Busan, which is what the "
                   "box is about."],
        ),
        "번영": dict(
            hanja="繁榮", meaning="prosperity",
            characters=[("繁", "번", "flourishing, numerous"),
                        ("榮", "영", "glory, thriving — the same 榮 as in 영광 “glory”")],
        ),
        "도시 재생": dict(
            hanja="都市再生", meaning="urban regeneration",
            characters=[("再", "재", "again"),
                        ("生", "생", "life, to be born — as in 생활, 학생")],
            notes=["Bringing a new function into a district that has declined, so as "
                   "to raise it again — keeping the fabric rather than clearing it, "
                   "which is what separates it from 재개발."],
        ),
        "쇠퇴": dict(
            hanja="衰退", meaning="decline",
            characters=[("衰", "쇠", "to weaken, wane"),
                        ("退", "퇴", "to retreat — the same 退 as in 은퇴, 퇴근, 퇴사")],
        ),
        "낙후": dict(
            hanja="落後", meaning="to have fallen behind",
            characters=[("落", "락/낙", "to fall — as in 낙엽 “fallen leaves”, 하락"),
                        ("後", "후", "behind, after — the same 後 as in 전후, 중후반")],
        ),
        "찧다": dict(
            meaning="to pound, to hull grain",
            notes=["Native Korean. Glossed on the page as striking grain to take off "
                   "the husk or make it into flour — what a 정미소 does to harvested "
                   "rice."],
        ),
        "정미소": dict(
            hanja="精米所", meaning="a rice mill",
            characters=[("精", "정", "refined, fine — as in 정확 “precise”, 정신"),
                        ("米", "미", "rice — as in 백미, 현미"),
                        ("所", "소", "place — the same 所 as in 조선소")],
        ),
        "수로": dict(
            hanja="水路", meaning="a watercourse, channel",
            characters=[("水", "수", "water — as in 수질 “water quality”, 수도"),
                        ("路", "로", "road, way — the same 路 as in 차로 “lane”, 도로")],
        ),
        "촌락": dict(
            hanja="村落", meaning="a village, a rural settlement",
            characters=[("村", "촌", "village — the 村 of 농촌, and a different 촌 from "
                                    "the 寸 of 촌수"),
                        ("落", "락", "to fall, a settlement")],
            notes=["Worth keeping apart from 촌수 in chapter 2: same sound, different "
                   "character, unrelated meaning."],
        ),
        "직거래": dict(
            hanja="直去來", meaning="direct trade, selling without a middleman",
            characters=[("直", "직", "direct, straight — as in 직접, 직장"),
                        ("去", "거", "to go — the same 去 as in 분리수거, 과거"),
                        ("來", "래", "to come — as in 미래 “the future”, 내일")],
            notes=["거래 is a transaction, 직거래 one made face to face. The page says it "
                   "benefits the rural producer and the urban consumer alike, by "
                   "cutting out the 중간 상인."],
        ),
        "특산물": dict(
            hanja="特産物", meaning="a local speciality",
            characters=[("特", "특", "special — the same 特 as in 특색, 특송"),
                        ("産", "산", "to produce — the same 産 as in 산업, 생산"),
                        ("物", "물", "thing — as in 물건, 매물")],
        ),
        "관광업": dict(
            hanja="觀光業", meaning="the tourist trade",
            characters=[("觀", "관", "to look at — as in 관심 “interest”, 관점"),
                        ("光", "광", "light — the same 光 as in 전광판, 광복절"),
                        ("業", "업", "occupation, industry")],
        ),
        "고령화": dict(
            hanja="高齡化", meaning="the ageing of a population",
            characters=[("高", "고", "high — the same 高 as in 고속버스, 고등학교"),
                        ("齡", "령", "age — the same 齡 as in 연령"),
                        ("化", "화", "-isation")],
            notes=["Named in chapter 2's 관련 단원 table as well. Here it is the cause "
                   "the page gives for the shortage of hands."],
        ),
        "일손": dict(
            meaning="hands, labour",
            notes=["Native Korean: 일 “work” plus 손 “hand”. 일손이 부족하다 is the set "
                   "phrase for being short of workers."],
        ),
        "귀농": dict(
            hanja="歸農", meaning="returning to farming",
            characters=[("歸", "귀", "to return — as in 귀국 “returning home”, 귀가"),
                        ("農", "농", "farming — the same 農 as in 농업, 농촌")],
            notes=["Of a city dweller who takes up farming. 귀촌 is the neighbouring "
                   "word for moving to the countryside without farming."],
        ),
        "품종": dict(
            hanja="品種", meaning="a variety, a breed",
            characters=[("品", "품", "article, quality — as in 제품 “product”, 일회용품"),
                        ("種", "종", "kind, seed — as in 종류 “kind”, 인종")],
        ),
        "생산성": dict(
            hanja="生産性", meaning="productivity",
            characters=[("生", "생", "to produce, life"),
                        ("産", "산", "to produce"),
                        ("性", "성", "nature, property — the same 性 as in 양성평등, 활성화")],
        ),
        "정보화": dict(
            hanja="情報化", meaning="informatisation, getting online",
            characters=[("情", "정", "feeling, information — as in 정보 “information”"),
                        ("報", "보", "to report — as in 보고 “report”, 예보"),
                        ("化", "화", "-isation")],
            notes=["The spread of computers and the internet through a society. The "
                   "page counts it with cultural and medical facilities as something "
                   "the countryside has less of."],
        ),
        "폐교": dict(
            hanja="廢校", meaning="a closed school",
            characters=[("廢", "폐", "to abolish, discard — as in 폐지 “abolition”"),
                        ("校", "교", "school — the same 校 as in 학교, 등교")],
            notes=["Both the closing of a school and the empty building left behind. "
                   "Here it is the building, converted into a cultural facility — a "
                   "common sight in depopulated areas."],
        ),
        "개조": dict(
            hanja="改造", meaning="to convert, remodel",
            characters=[("改", "개", "to change, reform — as in 개혁, 개선"),
                        ("造", "조", "to make, build — the same 造 as in 조선소")],
        ),
        "조성": dict(
            hanja="造成", meaning="to create, lay out",
            characters=[("造", "조", "to make, build"),
                        ("成", "성", "to complete, become — as in 형성 “formation”, 성장")],
            notes=["Used of building something out on the ground: 마을을 조성하다, "
                   "공원을 조성하다."],
        ),
        "원두막": dict(
            hanja="園頭幕", meaning="a melon-field hut",
            characters=[("園", "원", "garden — the same 園 as in 전원 주택, 공원"),
                        ("頭", "두", "head"),
                        ("幕", "막", "curtain, tent — as in 천막, 개막")],
            notes=["A raised shelter of poles and matting put up in a field to watch "
                   "the crop from and shelter in. Building one is offered as a rural "
                   "experience."],
        ),
        "농번기": dict(
            hanja="農繁期", meaning="the busy farming season",
            characters=[("農", "농", "farming"),
                        ("繁", "번", "busy, flourishing — the same 繁 as in 번영"),
                        ("期", "기", "period — as in 기간 “period”, 시기")],
            notes=["Your note in the margin of p. 39, paired with 농한기. It is what "
                   "the seasonal worker scheme in the discussion exists for."],
        ),
        "농한기": dict(
            hanja="農閑期", meaning="the slack farming season",
            characters=[("閑", "한", "leisure, idle — the same 閑 as in 한적하다, 한가하다"),
                        ("期", "기", "period")],
            notes=["The other half of your margin note. 번 and 한 are the opposition: "
                   "busy against idle."],
        ),
        "계절 근로자": dict(
            hanja="季節勤勞者", meaning="a seasonal worker",
            characters=[("季", "계", "season — as in 사계절, 계절"),
                        ("節", "절", "joint, season — the same 節 as in 명절, 1절"),
                        ("勤", "근", "to work — the same 勤 as in 근무, 야근"),
                        ("勞", "로", "to labour — as in 근로자, 노동"),
                        ("者", "자", "person")],
        ),
        "완화": dict(
            hanja="緩和", meaning="to ease, relieve",
            characters=[("緩", "완", "slow, loose"),
                        ("和", "화", "harmony — the same 和 as in 화합, 평화")],
            notes=["Also in chapter 3, of the gender imbalance easing."],
        ),
        "결혼이민자": dict(
            hanja="結婚移民者", meaning="a marriage immigrant",
            characters=[("結", "결", "to tie, conclude — as in 결혼, 결과"),
                        ("移", "이", "to move — the same 移 as in 이직, 이사"),
                        ("民", "민", "people — the same 民 as in 국민, 훈민정음"),
                        ("者", "자", "person")],
            notes=["The legal term for someone who has come to Korea by marrying a "
                   "citizen — the 다문화 가족 of chapter 2 seen from the other side."],
        ),
        "업무협약": dict(
            hanja="業務協約", meaning="a memorandum of understanding",
            characters=[("業", "업", "work"),
                        ("務", "무", "duty — as in 의무 “duty”, 공무원"),
                        ("協", "협", "to cooperate — as in 협력, 협동"),
                        ("約", "약", "to promise — as in 약속 “promise”, 계약")],
        ),
        "체결": dict(
            hanja="締結", meaning="to conclude, enter into",
            characters=[("締", "체", "to tie, bind"),
                        ("結", "결", "to tie, conclude")],
            notes=["Of treaties and agreements: 협약을 체결하다, 계약을 체결하다."],
        ),
        "체류": dict(
            hanja="滯留", meaning="to stay, remain in a country",
            characters=[("滯", "체", "to stagnate, be held up — as in 정체 “stagnation”"),
                        ("留", "류", "to remain — as in 유학 “studying abroad”, 잔류")],
            notes=["The word on every visa: 체류기간 is the period of stay, 체류자격 the "
                   "status of residence."],
        ),
        "산재보험": dict(
            hanja="産災保險", meaning="industrial accident insurance",
            characters=[("産", "산", "to produce"),
                        ("災", "재", "disaster — as in 재난 “disaster”, 화재"),
                        ("保", "보", "to protect — the same 保 as in 보증금, 보호"),
                        ("險", "험", "risk — as in 위험 “danger”, 보험")],
            notes=["Short for 산업재해보상보험. The point of the article is that a "
                   "marriage immigrant's family could not join it until a written "
                   "contract established them as employed rather than kin."],
        ),
    },

    extraNotes=[
        "The 알아두면 좋아요 on p. 38 prints 농촌 생활을 체험을 할 수 있는, with 을 twice. "
        "It is set here as printed rather than corrected, since it is the book's slip "
        "and not a transcription error.",
        "The three figures are given as bars from the values printed on them. The "
        "농가인구 and 고령인구 figures are one graphic on the page and are split into two "
        "here, because they are counted in different units.",
    ],
)
