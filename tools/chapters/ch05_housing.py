# -*- coding: utf-8 -*-
"""Chapter 5 — Housing.

Transcribed in your Google Doc (5.html), whose text is carried in `blocks`
below as the Doc had it. Originally transcribed from the photos of pp. 32-35;
when your Doc arrived the two were compared line by line and every difference
turned out to be a slip in the Doc, so those are listed as fixes below rather
than corrections to the reading of the page.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, FIGURE, LABELS, GROUP,
               MARGIN, TABLE, CELL, GLOSSARY)

CHAPTER = dict(
    number=5, slug="05-housing",
    unit="사회", title="주거", titleEn="Housing",

    blocks=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 한국에서 볼 수 있는 집의 모습입니다."),
        LABELS(GROUP("{단독 주택}", "{양옥}", "{한옥}"), GROUP("{공동 주택}", "{빌라}",
               "{아파트}")),
        HEADING(4, "01 한국에서 많이 본 집의 모습은 어떤 것 입니까?"),
        HEADING(4, "02 지금 본인이 살고 있는 집은 어떤 형태입니까? 어떤 점이 편리하고 어떤 점이 불편합니까?"),
        SECTION("goals", "학습목표"),
        BULLET("한국에서 많이 볼 수 있는 집의 {형태}와 주거 문화의 특징을 설명할 수 있다.", ordered=True),
        BULLET("한국인의 거주 형태와 집 구하는 방법을 설명할 수 있다.", ordered=True),
        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"], [["기본", "법", "34. 재산과 법",
              "부동산과 등기부 등본, 부동산 거래 과정"]]),
        SECTION("part", "01 한국인이 많이 살고 있는 집의 형태는 무엇일까?"),
        HEADING(2, "집의 형태", translation="Types of Homes" "\n\n"
          "\"The types of homes Koreans live in can broadly be "
          "divided into single-family homes (단독 주택 — including "
          "general houses, multi-household houses, etc.) and "
          "multi-unit housing (공동 주택 — including multi-family houses, "
          "row houses, apartments, etc.)." "\n\n"
          "단독 주택 (single-family housing) generally refers to a house "
          "built individually so that one household can live "
          "independently. This category also includes 다가구 주택 "
          "(multi-household houses), built so that several households "
          "can each occupy their own independent space. A 다가구 주택 is a "
          "building of 3 stories or fewer, where ownership of the "
          "entire building belongs to one landlord, and the other "
          "households rent their units from that owner." "\n\n"
          "공동 주택 (multi-unit housing) refers to a housing form built "
          "within one building so that several households can each "
          "live independently. This includes 다세대 주택 (multi-family "
          "housing), 연립 주택 (row/townhouse), and 아파트 (apartments). "
          "Unlike 다가구 주택, a 다세대 주택 has different owners for different "
          "parts/units of the building. A 연립 주택 is housing of 4 "
          "stories or fewer, and sometimes even has living space on "
          "basement level 1. A 연립 주택 has a larger total building area "
          "than a 다세대 주택. An apartment (아파트) is multi-unit housing of "
          "5 stories or more, and is often built on a large scale, "
          "ranging from hundreds to thousands of households.\""),
        GLOSSARY(("세", "다른 사람의 건물 등을 빌려 쓰는 대가로 내는 돈", "세")),
        PARAGRAPH("한국인이 거주하는 집의 형태는 크게 {단독} 주택(일반 주택, 다가구 주택 등)과 {공동} 주택(다세대 "
          "주택, {연립} 주택, 아파트 등)으로 나눌 수 있다. 단독 주택은 보통 한 가구가 독립적으로 생활할 수 "
          "있도록 집을 한 채씩 각각 {지은} 형태를 말한다. 단독 주택에는 여러 가구가 각각의 독립적인 공간을 "
          "{차지하며} 살 수 있도록 지은 다가구 주택도 포함된다. {다가구} 주택은 3층 이하의 건물이며 전체에 "
          "대한 {소유권}은 집주인이 가지고 있고 나머지 가구는 거기에 세를 들어 산다."),
        PARAGRAPH("공동 주택은 한 건물에 여러 가구가 각각 독립된 생활을 할 수 있게 만든 집의 형태를 말한다. 다세대 "
          "주택, 연립 주택, 아파트 등이 있다. 다세대 주택은 다가구 주택과 달리 건물의 부분 별로 주인이 "
          "다르다. 연립 주택은 4층 이하의 주택으로, 종종 지하 1층에도 주{거공간}이 있는 경우가 있다. 연립 "
          "주택은 다세대 주택보다 건물의 총 {면적}이 더 넓다. 아파트는 5층 이상의 공동 주택이며, {수백} "
          "가구에서 {수 천} 가구까지 {대규모}로 치어지는 경우가 많다."),
        LABELS("단독 주택(일반 주택)", "단독 주택(다가구 주택)", "공동 주택(다세대 주택)"),
        HEADING(2, "주거 문화의 변화", translation="Changes in Housing Culture" "\n\n"
          "\"Korea's housing forms are changing rapidly. In the past, "
          "single-family houses (단독 주택) made up the majority, but as "
          "population concentrated in cities, the number of "
          "households living in multi-unit housing (공동 주택) has grown "
          "larger than those in single-family homes. Apartments (아파트) "
          "in particular tend to be built in locations with "
          "convenient transportation, and are equipped with various "
          "amenities like playgrounds and fitness rooms, so many "
          "people prefer living in apartments. However, conflicts "
          "between neighbors sometimes worsen due to noise between "
          "floors (층간 소음)." "\n\n"
          "Recently, as one-person and two-person households "
          "increase, demand for studio apartments (원룸) or small "
          "housing has been rising. Some people preparing for old age "
          "around retirement, or those who want to live in a pleasant "
          "natural environment, build and live in country houses (전원 "
          "주택) in quiet areas on the outskirts of large cities.\""),
        GLOSSARY(("층간 소음", "건물의 한 층에서 발생한 소리 가 다른 층에 전달되어 피해를 주는 것", "층간 소음"),
              ("쾌적", "기분이 상쾌하고 즐거움", "쾌적"),
              ("한적", "한가하고 고요함", "한적"),
              ("전원 주택", "도시에서 조금 떨어져 있어서 자연의 분위기를 느낄 수 있도 록 지은 집", "전원 주택")),
        PARAGRAPH("한국의 주거 형태는 빠르게 변화하고 있다. 과거에는 단독 주택이 대부분이었으나 도시에 {인구}가 "
          "집중되면서 단독 주택보다 공동 주택에 살고 있는 가구 수가 많아졌다. 특히 아파트는 {대체로} 교통이 "
          "편리한 곳에 지어지고 놀이터, {체력 단련실} 등 여러 가지 편의 {시설}이 {갖추어져} 있어서 많은 "
          "사람들이 아파트에서 사는 것을 선호한다. 그러나 층간 소음으로 인해 이웃 간의 {갈등}이 심해지는 경우도 "
          "있다. 최근에는 1인 가구, 2인 가구가 늘어나면서 원룸이나 소형 주택에 대한 {수요}가 늘고 있다. "
          "은퇴를 맞아 {노년}을 준비하는 사람들이나 쾌적한 자연 환경에 살기 원하는 사람들은 대도시 주변의 한적한 "
          "지역에 전원 주택을 짓고 사는 경우도 있다."),
        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "공공 임대 주택이란?"),
        PARAGRAPH("대도시는 집값이 비싸기 때문에 서민들이 집을 구하기 어렵다. 그래서 정부에서는 아파트와 같은 공동 주택을 "
          "지어 경제적으로 어려운 사람들이 싼 값에 집을 사거나 빌릴 수 있도록 하고 있다. 기초생활수급자 등 "
          "사회의 보호가 필요한 계층을 위한 공공 임대 주택뿐만 아니라 대학생, 신혼부부, {사회초년생}(일을 "
          "시작한 지 얼마 되지 않은 사람) 등 젊은 층을 위한 임대 주택(행복 주택), 소득이 낮은 독거노인(혼자 "
          "사는 노인)을 위한 임대 주택(공공 실버 주택), 다문화 가족, 한부모 가족을 위한 임대 주택 등 다양한 "
          "사람들의 주거 안정을 지원하고 있다."),
        SECTION("part", "02 한국에서는 집을 어떻게 구할까?"),
        HEADING(2, "거주 형태와 집 구하는 방법", translation=
          "Housing forms and methods of finding a house" "\n\n"
          "\"In Korea, housing arrangements can be divided into 자가 "
          "(owned home), 전세 (jeonse), and 월세 (wolse/monthly rent). 자가 "
          "refers to living in a house one personally owns. 전세 is a "
          "system where you deposit a set amount of money with the "
          "landlord as a security deposit (보증금) and use the house or "
          "room for the contract period — this system is widely used "
          "almost exclusively in Korea. Jeonse contracts are usually "
          "made in 2-year units, and by law, the landlord cannot "
          "cancel/break (파기) the contract within those 2 years unless "
          "the tenant wants to. To safely get the deposit back after "
          "the contract period ends, it's a good idea to go to the "
          "community welfare center before or after moving and get a "
          "fixed-date certification (확정 일자).\""),
        GLOSSARY(("세입자", "세를 내고 남의 집이나 방 따위를 빌려 쓰는 사람", "세입자"),
              ("파기", "계약이나 약속 등을 깨뜨려 무 효로 하는 것", "파기"),
              ("확정 일자", "집을 계약한 날짜에 대해 법원이나 행정복지센터(주민센터) 등이 사실임을 증명해 준 날짜",
              "확정 일자"),
              ("중개", "두 사람 사이에서 일을 맡아 잘 진행되도록 함", "중개"),
              ("부동산/중개 업소", "다른 사람을 위하여 부동산 거래를 대리하거나 중개하고 수수료를 받는 영업소",
              "부동산/중개 업소")),
        PARAGRAPH("한국에서 집에 거주하는 형태는 {자가}, 전세, 월세로 나눌 수 있다. 자가는 자기가 소유한 집에 살고 "
          "있는 것을 말한다. 전세는 집주인에게 {일정한} 돈을 {보증금}으로 {맡기}고 계약 기간 동안 집이나 "
          "방을 빌려 쓰는 방식으로 한국에서만 널리 활용된다. 전세 계약은 보통 2년 단위로 하며, 집주인은 "
          "세입자가 원하지 않는 한 2년 이내에는 계약을 파기할 수 없도록 법률로 규정되어 있다. 계약 기간이 "
          "끝나고 보증금을 안전하게 돌려받기 위해서는 이사 전후에 행정복지센터에 가서 확정 일자를 받아 두는 것이 "
          "좋다. 월세는 집주인에게 매달 일정한 돈을 내고 집이나 방을 빌려 쓰는 방식이다. 월세의 경우도 어느 "
          "정도의 보증금을 내야 하는 경우가 많은데 그 금액은 전세에 비해 적다. 최근에는 전세와 월세를 {혼합한} "
          "반전세라는 방식도 많아지고 있는데 반전세의 보증금은 전세보다는 적고 월세보다는 많은 편이다."),
        PARAGRAPH("집을 사거나 전세 또는 월세를 구할 때는 부동산 중개업소(공인 중개사)를 통해 알아보는 것이 안전하다. "
          "공인 중개사는 집 계약을 할 때 계약자가 반드시 확인해야 할 사항들을 대신 확인해 주고 계약에 필요한 "
          "서류 준비에 도움을 주기 때문에 안전하고 편리하게 부동산을 거래할 수 있다."),
        HEADING(2, "주거 선택 기준", translation="Criteria for Choosing Housing" "\n\n"
          "\"These days, when people move, most use a full-service "
          "packing move (포장 이사, a Korean moving service where movers "
          "pack, transport, and unpack everything). Regarding where "
          "to live, things people consider important include "
          "transportation, educational conditions, residential "
          "environment, and convenience facilities. People who "
          "consider whether it's convenient to commute to work or "
          "travel to other areas prefer areas near subway stations or "
          "places with convenient transportation. People who "
          "prioritize the surrounding conditions for their children's "
          "education look for homes in areas where educational "
          "facilities are well-developed. It's good to consider your "
          "current financial situation and future plans, examine "
          "whether to buy a house or rent it via jeonse or monthly "
          "rent, and choose the method that suits you best.\""),
        GLOSSARY(("포장 이사", "이삿짐 업체에서 이삿침을 포장한 뒤 목적지까지 날라 주는 서비스", "포장 이사")),
        PARAGRAPH("요즘은 이사를 할 때 대부분 포장 이사를 이용한다. 어디에서 거주할 것인가와 관련하여 중요하게 여기는 "
          "것으로는 교통, 교육 {여건}, {주거} 환경, {편의 시설} 등이 있다. 출퇴근하기 편한지, 다른 "
          "지역으로 이동하기 편한지를 고려하는 사람들은 지하철역 주변이나 교통이 편리한 곳을 선호한다. 자녀 교육을 "
          "위한 주변의 여건을 {중시하}는 사람들은 교육 시설이 {발달해|발달하다} 있는 곳에 집을 구한다. 현재의 "
          "{경제적} 상황이나 미래의 계획 등을 고려하여 집을 살 것인지, 전세나 월세 등으로 빌려 쓸 것인지 등을 "
          "살펴보고 자신에게 적합한 방식을 선택하는 것이 좋다."),
        FIGURE("포장 이사 모습"),
        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "부동산에 갈 시간이 없다면? 온라인으로 알아보세요"),
        PARAGRAPH("거주하거나 구매할 집을 찾고자 할 때 부동산을 직접 방문하지 않고도 온라인으로도 알아볼 수 있다. 부동산 "
          "사이트에서 원하는 지역을 선택한 후, 집의 형태(아파트, 빌라, 주택, 오피스텔, 상가 등), 거래 "
          "방식(매매, 전세, 월세, 단기 임대), 가격대 등에 따라 검색해 볼 수 있다. 다만, 온라인 사이트에서 "
          "매물(팔려고 내놓은 물건)을 보고 부동산을 방문했는데 방문 직전에 거래가 완료됐다고 하면서 다른 매물을 "
          "권유하는 경우도 많으므로 주의해야 한다. 또한 계약하기 전에 주택에 문제가 있는지, 계약을 하러 나온 "
          "사람이 진짜 집주인인지 꼭 확인해야 한다. 경우도 있다."),
        SECTION("review", "주요 내용정리"),
        HEADING(3, "한국인이 많이 살고 있는 집의 형태는 무엇일까?"),
        BULLET("한국인들이 살고 있는 주택은 크게 ( 단독 주택 )과 ( 공동 주택 )으로 나뉜다."),
        BULLET("단독 주택에는 일반 주택, ( 다가구 주택 ) 등이 있고 공동 주택에는 다세대 주택, 연립 주택, ( "
          "아파트 ) 등이 포함된다."),
        BULLET("공동 주택에 살고 있는 가구 수가 많아지면서 ( 층간 소음 )으로 인해 이웃 간의 갈등이 심해지는"),
        HEADING(3, "한국에서는 집을 어떻게 구할까?"),
        BULLET("한국에서 집에 거주하는 형태는 자가, ( 전세 ), 월세가 있는데 이중 ( 전세 )는 한국에서만 널리 "
          "활용되는 방식이다."),
        BULLET("집을 사거나 전세 또는 월세를 구할 때는 ( 부동산 중개업소 )를 통해 알아보고 계약서를 작성하는 것이 " "안전하다."),
        BULLET("한국인들이 주거 선택에서 중요하게 여기는 것으로는 편리한 ( 교통 ), 교육 여건, 주변 환경의 쾌적함, "
          "편의 시설 등이 있다."),
        MARGIN("{스세권}", "{학세권}", "{역세권}"),
        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "여러 나라의 다양한 이사 문화"),
        PARAGRAPH("한국에서는 이사를 하고 나면 친척이나 친지들을 초대해 ‘집들이’라는 간단한 잔치를 베풀기도 하고 예전 "
          "에는 ‘이사떡’이라 하여 붉은 팔고물을 묻힌 시루떡을 이웃과 나누어 먹기도 하였다. 집들이에 초대 받은 "
          "사람들은 보통 세제나 화장지를 선물로 사 들고 간다."),
        PARAGRAPH("미국에서는 House warming이라고 하여 이사를 하거나 집을 새로 지었을 경우 친구나 가족들을 "
          "초청하여 파티를 연다."),
        PARAGRAPH("중국에서는 이사를 간 후에 폭죽을 터트리는 풍습이 있다. 짧게는 몇 초에서 길게는 몇 분까지 요란한 "
          "소리의 폭죽을 터트리는데 이는 이웃에게 우리 가족이 이사를 왔다고 알리는 의미이다. 또한 나쁜 것들이 "
          "요란한 소리를 듣고서 다가오지 못하게 하기 위한 목적도 있다. 중국에도 친구나 다른 가족을 초대하여 "
          "집들이 하는 문화가 있다."),
        PARAGRAPH("러시아에서는 고양이가 행운을 가져다주는 존재라고 생각한다. 그래서 이사를 하게 되면 고양이를 데리고 "
          "들어가거나 고양이를 집안에 먼저 들여보내 그 집안의 기운을 살펴보기도 한다."),
        PARAGRAPH("* 자신의 고향 나라의 이사 문화를 한국의 이사 문화와 비교하여 이야기 해 봅시다."),
    ],
    annotations={
        "형태": dict(
            meaning="shape",
        ),
        "세": dict(
            meaning="rent",
        ),
        "단독": dict(
            meaning="single/alone/independent",
            notes=["단독 주택 = a standalone single-family house."],
        ),
        "공동": dict(
            meaning="joint/shared/communal",
            notes=["공동 주택 = jointly-occupied multi-unit housing."],
        ),
        "연립": dict(
            meaning="row/joined together",
            notes=["연립 주택 = row houses/townhouses, units standing side by "
                "side."],
        ),
        "지은": dict(
            meaning="짓다 — to build",
        ),
        "차지하며": dict(
            headword="차지하다",
            meaning="to occupy/take up [space/position]",
            notes=["각각의 독립적인 공간을 차지하며 살다 = \"living while each occupying their "
                "own independent space\""],
        ),
        "다가구": dict(
            meaning="multi-household",
        ),
        "소유권": dict(
            meaning="ownership rights",
        ),
        "거공간": dict(
            meaning="주거공간 — living space/residential space",
        ),
        "면적": dict(
            meaning="area (surface measurement",
        ),
        "수백": dict(
            meaning="several hundred",
        ),
        "수 천": dict(
            headword="수천",
            meaning="several thousand",
        ),
        "대규모": dict(
            meaning="large-scale",
        ),
        "층간 소음": dict(
            meaning="noise between floors",
        ),
        "쾌적": dict(
            meaning="pleasant/comfortable",
        ),
        "한적": dict(
            meaning="quiet/secluded",
        ),
        "전원 주택": dict(
            meaning="country house",
        ),
        "인구": dict(
            meaning="population",
            notes=["인구가 집중되다 = \"population becomes concentrated\""],
        ),
        "대체로": dict(
            meaning="generally/on the whole",
        ),
        "체력 단련실": dict(
            meaning="fitness/exercise room",
            notes=["體力 (physical strength) + 단련 (training/tempering) + 실 "
                "(room)"],
        ),
        "시설": dict(
            meaning="facility",
            notes=["편의 시설 = \"convenience facilities/amenities\""],
        ),
        "갖추어져": dict(
            headword="갖추다",
            meaning="to equip/have prepared",
            notes=["편의 시설이 갖추어져 있다 = \"amenities are equipped/in place\""],
        ),
        "갈등": dict(
            meaning="conflict",
        ),
        "수요": dict(
            meaning="demand (economic term)",
            notes=["공급 — \"supply"],
        ),
        "노년": dict(
            meaning="old age",
            notes=["노년을 준비하다 = \"to prepare for old age.\""],
        ),
        "사회초년생": dict(
            meaning="someone new to working life",
        ),
        "세입자": dict(
            meaning="tenant",
        ),
        "파기": dict(
            meaning="breach/cancellation",
            notes=["annul / cancel"],
        ),
        "확정 일자": dict(
            meaning="fixed date [certification]",
            notes=["an official date-stamp certification from a court or "
                "community service center confirming the date a housing "
                "contract was made (used in Korea to protect a tenant's "
                "deposit priority legally)."],
        ),
        "중개": dict(
            meaning="brokering/mediation",
            notes=["taking on a task between two people so it proceeds "
                "smoothly, i.e., acting as a go-between"],
        ),
        "부동산/중개 업소": dict(
            meaning="real estate/brokerage office",
            notes=["an office that represents or mediates real estate "
                "transactions on someone's behalf in exchange for a "
                "commission (수수료)"],
        ),
        "자가": dict(
            meaning="one's own home",
        ),
        "일정한": dict(
            meaning="fixed/set/certain (amount)",
        ),
        "보증금": dict(
            meaning="security deposit",
        ),
        "맡기": dict(
            headword="맡기다",
            meaning="to entrust/deposit [something with someone]",
            notes=["돈을 맡기다 = \"to entrust/deposit money [with the landlord].\""
                ],
        ),
        "혼합한": dict(
            headword="혼합하다",
            meaning="to mix/combine",
            notes=["전세와 월세를 혼합한 방식 = \"a method that combines jeonse and "
                "monthly rent.\""],
        ),
        "포장 이사": dict(
            meaning="full-service packing move",
        ),
        "여건": dict(
            meaning="conditions/circumstances",
            notes=["與 (to give/provide)",
                "件 (item/matter, same 件 as in 사건 \"incident\")"],
        ),
        "주거": dict(
            meaning="residence/dwelling",
            notes=["a general term for \"housing/residence\" as a concept",
                "주거 환경 = \"residential environment\"",
                "주거 형태 = \"housing form/type\""],
        ),
        "편의 시설": dict(
            meaning="convenience facilities/amenities",
        ),
        "중시하": dict(
            headword="중시하다",
            meaning="to place importance on/value highly",
            notes=["교육 여건을 중시하다 = \"to place importance on educational "
                "conditions.\""],
        ),
        "발달하다": dict(
            meaning="to develop",
            notes=["교육 시설이 발달해 있는 곳 = \"a place where educational facilities "
                "are well-developed.\""],
            surfaces=["발달해"],
        ),
        "경제적": dict(
            meaning="economic",
            notes=["경제적 상황 = \"economic/financial situation.\""],
        ),
    },
    fixes=[
        ("치어지는", "지어지는", "typo — 치 for 지 in 지어지는 “are built”"),
        ("붉은 팔고물", "붉은 팥고물", "typo — 팔 for 팥; 팥고물 is the red-bean topping"),
        ("발생한 소리 가", "발생한 소리가", "spacing"),
        ("느낄 수 있도 록", "느낄 수 있도록", "spacing"),
        ("깨뜨려 무 효로", "깨뜨려 무효로", "spacing"),
        ("이삿침을", "이삿짐을", "typo — 침 for 짐"),
        ("부분 별로", "부분별로", "spacing"),
        ("자연 환경에", "자연환경에", "spacing — the page sets it closed"),
        ("부동산/중개 업소", "부동산 중개 업소",
         "the margin entry runs two words together with a slash"),
        ("예전 에는", "예전에는", "spacing"),
        ("* 자신의", "★ 자신의", "the page uses a star for the discussion prompt"),
    ],
    approved={
        # read against the photos of pp. 32-35 and accepted
        "치어지는", "붉은 팔고물", "발생한 소리 가", "느낄 수 있도 록",
        "깨뜨려 무 효로", "이삿침을", "부분 별로", "자연 환경에",
        "부동산/중개 업소", "예전 에는", "* 자신의",
    },
    headwords={"쾌적한": "쾌적하다", "한적한": "한적하다", "발달해": "발달하다"},

    english={
        "집의 형태": dict(
            title="Kinds of housing",
            paragraphs=[
                "The housing Koreans live in divides broadly into the detached house "
                "(the ordinary house, the multi-household house and so on) and shared "
                "housing (the multi-family house, the row house, the flat and so on). "
                "A detached house is one built on its own, so that a single household "
                "can live independently. It also covers the multi-household house, "
                "built so that several households can each occupy their own separate "
                "space. A multi-household house is a building of three storeys or "
                "fewer; the owner holds title to the whole of it and the other "
                "households live there on a tenancy.",

                "Shared housing means a form in which several households can each "
                "live independently within one building. It includes the multi-family "
                "house, the row house and the flat. Unlike the multi-household house, "
                "a multi-family house has a different owner for each part of the "
                "building. A row house is a dwelling of four storeys or fewer, and "
                "often has living space in the basement as well. A row house has a "
                "greater total floor area than a multi-family house. A flat is shared "
                "housing of five storeys or more, and is often built on a large "
                "scale, from several hundred households to several thousand.",
            ],
        ),
        "주거 문화의 변화": dict(
            title="How the culture of housing has changed",
            paragraphs=[
                "The forms of housing in Korea are changing quickly. In the past most "
                "of it was detached houses, but as the population concentrated in the "
                "cities the number of households living in shared housing came to "
                "exceed those in detached houses. Flats in particular are generally "
                "built where the transport is convenient and come with a range of "
                "amenities — a playground, a gym and so on — so many people prefer to "
                "live in them. Noise between floors, however, can sharpen the "
                "friction between neighbours. Lately, as one- and two-person "
                "households have increased, demand for studio flats and small "
                "dwellings has been growing. People who are retiring and preparing "
                "for old age, or who want to live in a pleasant natural setting, "
                "sometimes build a country house in a quiet area on the edge of a "
                "large city and live there.",
            ],
        ),
        "거주 형태와 집 구하는 방법": dict(
            title="Ways of living somewhere, and ways of finding it",
            paragraphs=[
                "The ways of living in a house in Korea divide into owning it, 전세 "
                "and 월세. Owning means living in a house one owns oneself. 전세 is an "
                "arrangement in which a fixed sum is left with the owner as a deposit "
                "and the house or room is borrowed for the term of the contract; it "
                "is used widely only in Korea. A 전세 contract usually runs in "
                "two-year terms, and the law provides that the owner cannot break it "
                "within those two years unless the tenant wishes it. To get the "
                "deposit back safely once the term is over, it is as well to go to "
                "the administrative welfare centre around the time of moving and have "
                "the date of the contract certified. 월세 is an arrangement in which a "
                "fixed sum is paid to the owner each month for the use of the house "
                "or room. With 월세 too a deposit of some size is often required, but "
                "the amount is small next to 전세. Lately 반전세, which mixes the two, "
                "has become more common; its deposit is smaller than a 전세 deposit "
                "and larger than a 월세 one.",

                "When buying a house or looking for a 전세 or 월세, it is safer to go "
                "through an estate agency — a licensed agent. A licensed agent checks, "
                "on the client's behalf, the things a party to a housing contract must "
                "be sure of, and helps prepare the documents the contract needs, so "
                "the transaction can be made safely and conveniently.",
            ],
        ),
        "주거 선택 기준": dict(
            title="What people weigh in choosing a home",
            paragraphs=[
                "These days most people use a packing removal service when they move. "
                "Among the things held to matter in deciding where to live are "
                "transport, the conditions for education, the residential environment "
                "and the amenities. Those who weigh how easy the commute is, and how "
                "easily one can travel to other areas, prefer somewhere near a subway "
                "station or otherwise well served. Those who put weight on the "
                "surroundings for their children's education look for a house where "
                "educational facilities are well developed. It is as well to weigh "
                "one's present financial situation and future plans, look at whether "
                "to buy or to rent on 전세 or 월세, and choose whichever suits.",
            ],
        ),
    },

    extraAnnotations={
        "단독 주택": dict(
            hanja="單獨住宅", meaning="a detached house",
            characters=[("單", "단", "single — as in 단순 “simple”, 단어 “word”"),
                        ("獨", "독", "alone — as in 독립 “independence”, 독거 “living alone”"),
                        ("住", "주", "to dwell — as in 주거, 주소 “address”"),
                        ("宅", "택", "house — the same 宅 as in 택배 “home delivery”")],
            notes=["One building for one household, as against 공동 주택. The page "
                   "counts the 다가구 주택 as a kind of it, which is the part worth "
                   "remembering: 단독 does not always mean one family."],
        ),
        "공동 주택": dict(
            hanja="共同住宅", meaning="shared housing",
            characters=[("共", "공", "together — as in 공공 “public”, 공유 “sharing”"),
                        ("同", "동", "same — as in 동시 “simultaneous”, 동료 “colleague”")],
            notes=["Several households living independently inside one building: "
                   "다세대 주택, 연립 주택 and 아파트."],
        ),
        "다가구 주택": dict(
            hanja="多家口住宅", meaning="a multi-household house",
            characters=[("多", "다", "many — as in 다양 “various”, 다문화"),
                        ("家", "가", "household"),
                        ("口", "구", "mouth, a person counted — the 口 of 가구, 인구")],
            notes=["Three storeys or fewer, one owner for the whole building and the "
                   "other households renting. Told apart from 다세대 주택 by exactly "
                   "that: who owns what."],
        ),
        "다세대 주택": dict(
            hanja="多世帶住宅", meaning="a multi-family house",
            characters=[("世", "세", "generation, world — as in 세대, 세계"),
                        ("帶", "대", "band, belt — 세대 together meaning a household")],
            notes=["Each part of the building is separately owned, which is what "
                   "distinguishes it from 다가구 주택."],
        ),
        "연립 주택": dict(
            hanja="聯立住宅", meaning="a row house, a low-rise block",
            characters=[("聯", "연", "to join, link — as in 연결 “connection”, 연합"),
                        ("立", "립", "to stand — the same 立 as in 설립 “to establish”")],
            notes=["Four storeys or fewer, with a greater total floor area than a "
                   "다세대 주택, and often living space in the basement."],
        ),
        "소유권": dict(
            hanja="所有權", meaning="title, right of ownership",
            characters=[("所", "소", "place, that which — as in 주소 “address”"),
                        ("有", "유", "to have — as in 유용하다 “useful”, 고유 “inherent”"),
                        ("權", "권", "right, authority — the same 權 as in 권위")],
        ),
        "세": dict(
            hanja="貰", meaning="rent, the money paid for use",
            characters=[("貰", "세", "to hire, rent — as in 전세, 월세, 세입자")],
            notes=["세를 들다 is to take a tenancy, 세를 내다 to pay the rent. Not the "
                   "세 of 세금 “tax”, which is 稅, nor the 세 of 세제 “detergent”, 洗."],
        ),
        "층간 소음": dict(
            hanja="層間騷音", meaning="noise between floors",
            characters=[("層", "층", "storey, layer — as in 1층, 계층 “stratum”"),
                        ("間", "간", "between — the same 間 as in 가족 간, 시간"),
                        ("騷", "소", "clamour, disturbance"),
                        ("音", "음", "sound — the same 音 as in 훈민정음, 발음")],
            notes=["A standing subject of dispute in Korean flats, and the reason the "
                   "passage gives for friction between neighbours."],
        ),
        "쾌적하다": dict(
            hanja="快適", meaning="to be pleasant, agreeable",
            characters=[("快", "쾌", "pleasant, quick — as in 쾌속 “high speed”"),
                        ("適", "적", "to suit — as in 적합하다 “suitable”, 적당하다")],
            notes=["Used of surroundings rather than of people: 쾌적한 자연환경, "
                   "쾌적한 실내."],
        ),
        "한적하다": dict(
            hanja="閑寂", meaning="to be quiet and secluded",
            characters=[("閑", "한", "leisure, idle — as in 한가하다 “to be free”"),
                        ("寂", "적", "still, lonely — as in 적막 “silence”")],
            notes=["Glossed on the page as 한가하고 고요함. A different 한 from the one "
                   "in 한국 or 한글."],
        ),
        "전원 주택": dict(
            hanja="田園住宅", meaning="a country house",
            characters=[("田", "전", "field, paddy — as in 전답"),
                        ("園", "원", "garden — as in 공원 “park”, 유치원")],
            notes=["Built a little away from the city so the feel of nature can be "
                   "had, which is how the page glosses it."],
        ),
        "대규모": dict(
            hanja="大規模", meaning="on a large scale",
            characters=[("規", "규", "rule, standard — as in 규칙 “rule”, 규정"),
                        ("模", "모", "pattern, model — as in 모양 “shape”, 모방하다")],
        ),
        "원룸": dict(
            meaning="a studio flat",
            notes=["From English “one room”, but Korean-made: a single room holding "
                   "the living space, kitchen and bathroom together. Demand for them "
                   "rises with one- and two-person households."],
        ),
        "노년": dict(
            hanja="老年", meaning="old age, one's later years",
            characters=[("老", "노", "old — as in 노인 “an old person”, 독거노인"),
                        ("年", "년", "year — the same 年 as in 연령 “age”, 작년")],
        ),
        "기초생활수급자": dict(
            hanja="基礎生活受給者", meaning="a recipient of basic living support",
            characters=[("基", "기", "foundation — as in 기본 “basic”, 기초"),
                        ("礎", "초", "cornerstone"),
                        ("受", "수", "to receive — as in 수입 “income”"),
                        ("給", "급", "to give, supply — as in 보급 “distribution”, 공급"),
                        ("者", "자", "person — as in 근로자 “worker”, 세입자")],
            notes=["The legal term for a household receiving the state's basic "
                   "livelihood benefit, and the group the page names first among "
                   "those public rental housing is for."],
        ),
        "자가": dict(
            hanja="自家", meaning="owning the home one lives in",
            characters=[("自", "자", "self — the same 自 as in 자가용 “private car”"),
                        ("家", "가", "house, household")],
        ),
        "전세": dict(
            hanja="傳貰", meaning="a lump-sum deposit lease",
            characters=[("傳", "전", "to hand over, pass on — as in 전달, 전통"),
                        ("貰", "세", "to hire, rent — the 貰 of 월세, 세입자")],
            notes=["A large deposit is left with the owner instead of monthly rent "
                   "and returned at the end of the term. The page says it is used "
                   "widely only in Korea, which is why it has no English name.",
                   "Usually two-year terms, and the owner cannot break the contract "
                   "inside them unless the tenant wants it."],
        ),
        "월세": dict(
            hanja="月貰", meaning="monthly rent",
            characters=[("月", "월", "month — as in 월요일, 매월"),
                        ("貰", "세", "to hire, rent — the 貰 of 전세")],
        ),
        "반전세": dict(
            hanja="半傳貰", meaning="a half-전세, part deposit and part monthly rent",
            characters=[("半", "반", "half — as in 반년 “half a year”, 후반")],
            notes=["Its deposit sits between the two: smaller than a 전세 deposit, "
                   "larger than a 월세 one."],
        ),
        "보증금": dict(
            hanja="保證金", meaning="a deposit",
            characters=[("保", "보", "to protect, guarantee — as in 보호, 보험"),
                        ("證", "증", "proof — as in 증명 “proof”, 신분증"),
                        ("金", "금", "money, gold — the same 金 as in 임금 “wages”")],
        ),
        "세입자": dict(
            hanja="貰入者", meaning="a tenant",
            characters=[("貰", "세", "rent"),
                        ("入", "입", "to enter — as in 입구 “entrance”, 수입"),
                        ("者", "자", "person")],
            notes=["Literally the person who has entered on a tenancy — 세를 들어 사는 "
                   "사람, as the passage puts it of the 다가구 주택."],
        ),
        "파기": dict(
            hanja="破棄", meaning="to break off, annul",
            characters=[("破", "파", "to break — as in 파괴 “destruction”"),
                        ("棄", "기", "to discard, abandon — as in 포기 “giving up”")],
            notes=["Used of contracts and promises: 계약을 파기하다."],
        ),
        "확정 일자": dict(
            hanja="確定日字", meaning="a certified date",
            characters=[("確", "확", "certain — the same 確 as in 명확하다, 확인"),
                        ("定", "정", "to fix, settle — as in 결정 “decision”, 정하다"),
                        ("日", "일", "day"),
                        ("字", "자", "character, letter — the 字 of 문자, 한자")],
            notes=["A date stamped on a lease by a court or the 행정복지센터 to prove "
                   "when it was made. It is what protects the deposit's priority if "
                   "the property is later sold or seized, which is why the page says "
                   "to get one around the time of moving."],
        ),
        "중개": dict(
            hanja="仲介", meaning="brokerage, acting between two parties",
            characters=[("仲", "중", "middle, to mediate"),
                        ("介", "개", "to introduce, come between — as in 소개")],
        ),
        "부동산": dict(
            hanja="不動産", meaning="real estate",
            characters=[("不", "부", "not — as in 불편 “inconvenient”"),
                        ("動", "동", "to move — as in 운동 “exercise”, 활동"),
                        ("産", "산", "property, to produce — the same 産 as in 산업")],
            notes=["Literally “immovable property”, against 동산 for movables. In "
                   "speech 부동산 also means the agency itself: 부동산에 가다 is to go to "
                   "the estate agent."],
        ),
        "포장 이사": dict(
            hanja="包裝이사", meaning="a packing removal service",
            characters=[("包", "포", "to wrap — as in 포함 “inclusion”, 소포 “parcel”"),
                        ("裝", "장", "to fit out, equip — as in 장비 “equipment”")],
            notes=["The firm packs everything as well as carrying it, which the page "
                   "says is now what most people use."],
        ),
        "여건": dict(
            hanja="與件", meaning="conditions, the given circumstances",
            characters=[("與", "여", "to give, grant"),
                        ("件", "건", "matter, item — as in 사건 “incident”, 조건")],
            notes=["교육 여건 is the conditions for education in an area — the schools "
                   "and what surrounds them, not the schooling itself."],
        ),
        "매물": dict(
            hanja="賣物", meaning="a property on the market",
            characters=[("賣", "매", "to sell — as in 판매 “sales”, 매매"),
                        ("物", "물", "thing — as in 물건 “article”, 소화물")],
            notes=["Glossed in line on the page as 팔려고 내놓은 물건."],
        ),
        "양옥": dict(
            hanja="洋屋", meaning="a Western-style house",
            characters=[("洋", "양", "ocean, Western — as in 서양 “the West”, 양식"),
                        ("屋", "옥", "house — the same 屋 as in 한옥")],
            notes=["The counterpart of the 한옥: built to a Western plan, of "
                   "brick or concrete, with rooms off a hallway rather than "
                   "around a courtyard. Both are 단독 주택 — one household to "
                   "a building."],
        ),
        "한옥": dict(
            hanja="韓屋", meaning="a Korean traditional house",
            characters=[("韓", "한", "Korea — the same 韓 as in 한국, 대한민국"),
                        ("屋", "옥", "house")],
        ),
        "빌라": dict(
            meaning="a low-rise block of flats",
            notes=["From “villa”, but in Korean it means a small block of a few "
                   "storeys — roughly the 다세대 주택 or 연립 주택 of this chapter, not a "
                   "grand house."],
        ),
        "아파트": dict(
            meaning="a flat, an apartment block",
            notes=["From “apartment”. Five storeys or more, per the page, and usually "
                   "a whole estate rather than a single building."],
        ),
        "스세권": dict(
            meaning="within walking distance of a Starbucks",
            notes=["A joke on 역세권, swapping 역 for the 스 of 스타벅스, and formed the "
                   "same way as 학세권. Your own note in the margin of p. 35."],
        ),
        "학세권": dict(
            hanja="學勢圈", meaning="within easy reach of schools",
            characters=[("學", "학", "to learn — the same 學 as in 학교, 학습")],
            notes=["Built on 역세권 by swapping the first character."],
        ),
        "역세권": dict(
            hanja="驛勢圈", meaning="the catchment of a station",
            characters=[("驛", "역", "station — as in 지하철역, 역장"),
                        ("勢", "세", "force, influence — as in 형세, 기세"),
                        ("圈", "권", "sphere, zone — the same 圈 as in 생활권")],
            notes=["The area close enough to a station to be worth paying for, and "
                   "the original of which 학세권 and 스세권 are jokes."],
        ),
        "친척": dict(
            hanja="親戚", meaning="relatives",
            characters=[("親", "친", "close, kin — the same 親 as in 친사촌, 친밀하다"),
                        ("戚", "척", "kin by marriage")],
        ),
        "친지": dict(
            hanja="親知", meaning="close acquaintances",
            characters=[("親", "친", "close"),
                        ("知", "지", "to know — as in 지식 “knowledge”, 지인")],
            notes=["Not relatives but people one knows well — paired with 친척 in the "
                   "passage to mean everyone one would invite."],
        ),
        "집들이": dict(
            meaning="a housewarming",
            notes=["Native Korean: 집 “house” plus 들이 from 들이다 “to bring in”. Guests "
                   "usually bring detergent or toilet paper, per the page."],
        ),
        "이사떡": dict(
            meaning="moving-day rice cake",
            notes=["시루떡 coated in red bean, shared with the neighbours on moving in. "
                   "The red was thought to keep bad things off — the same reason the "
                   "page gives for the Chinese firecrackers."],
        ),
        "세제": dict(
            hanja="洗劑", meaning="detergent",
            characters=[("洗", "세", "to wash — as in 세수, 세탁 “laundry”"),
                        ("劑", "제", "preparation, agent — as in 약제")],
            notes=["A different 세 from the 貰 of 전세 and 월세 in this same chapter."],
        ),
        "풍습": dict(
            hanja="風習", meaning="a custom",
            characters=[("風", "풍", "wind, manner — as in 풍경 “scenery”, 태풍"),
                        ("習", "습", "to practise — the same 習 as in 학습, 습관")],
        ),
    },

    extraNotes=[
        "The four photos on p. 32 are two 단독 주택 (양옥, 한옥) over two "
        "공동 주택 (빌라, 아파트), which is the division the first article then "
        "explains. The handwriting on the page names the two kinds beside the "
        "rows; here the labels are grouped under them.",
    ],
)
