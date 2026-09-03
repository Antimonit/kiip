# -*- coding: utf-8 -*-
"""Chapter 4 — Transport and communication.

Source: 4.html (Google Docs HTML export)
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, LABELS,
               MARGIN, TABLE, CELL, GLOSSARY)

CHAPTER = dict(
    number=4, slug="04-transport-and-communication",
    unit="사회", title="교통과 통신", titleEn="Transport and communication",

    blocks=[
        SECTION("warmup", "생각해 봅시다"),
        LABELS("환승(단말기)", "지하철 앱", "대중교통안 무선인터넷 사용", "버스도착 안내"),
        PARAGRAPH("다음은 한국에서 대중교통수단을 이용할 때 볼 수 있는 모습입니다."),
        HEADING(4, "01 사진에 제시된 기기나 서비스를 이용한 경험이 있습니까? 그 장점은 무엇입니까?"),
        HEADING(4, "02 평소에 자주 이용하는 교통수단은 어떤 것이고 그 이유는 무엇입니까?"),
        SECTION("goals", "학습목표"),
        BULLET("한국에서 사람들이 많이 이용하는 교통수단과 이용 방법을 설명할 수 있다.", ordered=True),
        BULLET("한국에서 많이 사용하는 통신수단과 사용 방법을 설명할 수 있다.", ordered=True),
        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"], [["기본", "지리",
              "46. 수도권 47. 경상 지역 48, 전라 지역 49. 충청 지역 50. 강원, 제주 지역",
              "지역별 특징, 관광 명소와 축제"]]),
        SECTION("part", "01 한국에서 많이 이용하는 교통수단은 무엇일까?"),
        GLOSSARY(("고속버스", "고속도로에서 고속으로 주행 하기에 알맞도록 제작된 대형 버스", None, "express"),
              ("시외버스", "도시 밖 특정 지역까지 운행하 는 버스", None, "intercity")),
        HEADING(2, "교통수단의 종류", translation="Types of Transportation" "\n\n"
          "\"Korea has a variety of well-developed public "
          "transportation options. For nearby trips, people mainly "
          "use buses, subways, taxis, etc., paying with cash or a "
          "transit card. Charging a set amount onto a transit card, "
          "or using a credit card or phone with transit card "
          "functionality built in, can get you a fare discount. By "
          "checking real-time traffic info via the internet or phone "
          "apps, you can find various routes offering the shortest "
          "time or fewest transfers to your destination." "\n\n"
          "For long-distance travel, people use trains, "
          "express/intercity buses, ferries, planes, etc. Trains are "
          "a safe, fast option, including high-speed rail (KTX, SRT), "
          "Saemaul-ho, and Mugunghwa-ho. High-speed rail in "
          "particular connects the whole country into a 2-hour "
          "commuting zone at high speed. Of course, many people also "
          "use private cars besides public transit, but making good "
          "use of public transportation lets you travel conveniently "
          "at low cost.\""),
        PARAGRAPH("한국에는 다양한 대중교통수단이 {발달해|발달하다} 있다. 가까운 곳으로 이동할 때는 주로 버스, 지하철, "
          "택시 등을 이용하는데 이용 요금은 현금이나 교통카드로 {지불한다|지불하다}. 일정한 금액을 교통카드에 "
          "충전해서 사용하거나 신용카드 또는 휴대 전화에 교통카드 기능을 포함해서 사용하면 요금을 할인받을 수 "
          "있다. 인터넷이나 휴대 전화 앱으로 실시간 교통정보를 확인하여 목적지까지 최단 시간이나 최소 환승으로 갈 "
          "수 있는 다양한 방법을 알 수 있다."),
        PARAGRAPH("먼 거리를 이동할 때는 기차, 고속버스나 시외버스, 배, 비행기 등을 이용한다. 기차는 안전하고 빠른 "
          "교통수단으로 고속철도(KTX•SRT), 새마을호, 무궁화호 등이 있다. 특히 고속철도는 빠른 속도로 "
          "전국을 2시간대 {생활권}으로 연결시키는 교통수단이다. 물론 대중교통수단 외에 {자가용}을 이용하는 "
          "사람들도 많지만, 대중교통을 잘 활용하면 적은 비용으로 편리하게 이동할 수 있다."),
        GLOSSARY(("장려", "좋은 일에 힘쓰도록 북돋아 줌", "장려"),
              ("권장", "바람직한 일을 하도록 권하고 격려함", "권장"),
              ("전광판", "그림이나 문자가 나타나도록 만든 판", "전광판"),
              ("혼잡", "여럿이 한데 뒤섞이어 어수선함", "혼잡")),
        HEADING(2, "대중교통 이용을 장려 하는 제도", translation=
          "Systems that encourage the use of public transportation" "\n\n"
          "\"In Korea, systems such as the transfer discount system, "
          "bus arrival information service, and bus-only lane system "
          "are being implemented in order to encourage (권장) the use "
          "of public transportation." "\n\n"
          "The transfer discount system (환승 할인 제도) is a system that "
          "discounts the fare when switching to a different mode of "
          "transportation. Even if you change transportation methods "
          "during your trip, you pay based on the total distance "
          "traveled, which reduces the transportation cost burden for "
          "people using public transit." "\n\n"
          "The bus arrival information service (버스 도착 안내 서비스) informs "
          "people in advance, through electronic display boards (전광판) "
          "at bus stops, of the bus's arrival time and level of "
          "congestion (혼잡), allowing people to use buses more "
          "conveniently. The bus-only lane system (버스 전용 차로제) "
          "designates a lane among the road's lanes that only buses "
          "can use, allowing buses to travel smoothly." "\n\n"
          "Within cities, the center lane or the outermost lane of "
          "the road is often designated as the bus-only lane, while "
          "on highways, lane 1 is operated as the bus-only lane.\""),
        PARAGRAPH("한국에서는 대중교통 이용을 권장하기 위해 환승 할인 {제도}, 버스 도착 안내 서비스, 버스 "
          "{전용}{차로제}와 같은 제도를 시행하고 있다."),
        PARAGRAPH("환승 할인 제도란 다른 교통수단으로 갈아탈 때 요금을 할인해 주는 제도이다. 이동 중에 교통수단을 "
          "변경하더라도 전체 이용 거리에 따라 요금을 내도록 하여 대중교통을 이용하는 사람들의 교통비 부담을 " "덜어준다."),
        PARAGRAPH("버스 도착 안내 서비스는 버스 정류장의 전광판을 통해 버스 도착 시각과 혼잡 정도를 미리 알려 주어서 "
          "버스를 보다 편리하게 이용할 수 있도록 한다. 버스 전용 차로제는 도로의 차로 중 버스만 이용할 수 있는 "
          "전용 차로를 정해 버스가 {원활히|원활하다}{통행할|통행하다} 수 있도록 하는 제도이다."),
        PARAGRAPH("시내에서는 도로의 중앙 부분 또는 가장 바깥쪽 도로를 버스 전용차로로 하는 경우가 많고, 고속도로에서는 "
          "1차로를 버스 전용 차로로 운영하고 있다."),
        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "누구나, 언제나 이용할 수 있는 교통수단, 공공 자전거"),
        PARAGRAPH("주민들의 편의를 도모하고, 교통체증, 대기오염 문제를 해결하기 위해 각 지방자치단체에서는 자전거를 "
          "누구나, 언제나, 어디서나 쉽고 편리하게 이용할 수 있는 무인 대여 시스템을 운영하고 있다. 공공 "
          "자전거의 이름은 따릉이 (선울), 타슈 (대전), '누비자 (창원), '온누리'(순천), '타랑께 "
          "(광주), 어울림'(세종), 여수랑 (여수) 등으로 다양하다. 누리집이나 앱으로 예약해서 이용하거나 "
          "대여소에 가서 직접 이용권을 구매한 뒤 바로 이용할 수 있다."),
        SECTION("part", "02 한국에서 많이 사용하는 통신수단은 무엇일까?"),
        GLOSSARY(("특송", "빠른 시간 안에 물건을 배달함", "특송"),
              ("소화물", "열차나 버스 등을 통해 운반 하는 대체로 작고 가벼운 물품", "소화물"),
              ("보급", "많은 사람들에게 골고루 미치게 하여 누리게 함", "보급")),
        HEADING(2, "통신수단의 종류와 이용", translation=
          "Types and use of communication methods" "\n\n"
          "\"In Korea, people mainly exchange information with those "
          "far away through mail, telephone, the internet, etc. "
          "Through the post office, letters or packages can be sent "
          "domestically or abroad, and besides the post office, "
          "courier services can also be used through delivery "
          "companies or convenience stores. Though more expensive "
          "than regular courier service, 'quick service' (퀵서비스) — "
          "which uses motorcycles or the subway to deliver same-day — "
          "has also developed. When items need to be delivered "
          "quickly to a distant region, KTX express delivery (KTX 특송) "
          "or express bus parcel service can be used.Telephones "
          "include landlines (유선 전화) connected at home or in offices, "
          "and mobile phones (휴대 전화) that people carry around. In "
          "Korea, the majority of people use mobile phones, making "
          "fast communication possible. These days, as smartphones "
          "have become widely distributed (보급), it has become "
          "possible to freely exchange not only voice calls and video "
          "calls but also photos and videos, and to quickly search "
          "for various information.\""),
        PARAGRAPH("한국에서는 주로 우편, 전화, 인터넷 등을 통해 멀리 떨어져 있는 사람과 정보를 주고받는다. 우체국을 "
          "통해 편지나 물건을 국내나 해외에 보낼 수 있고, 우체국 외에도 택배{업체}나 편의점을 통해 택배 "
          "서비스를 이용할 수 있다. 택배보다 가격은 비싸지만 오토바이나 지하철을 이용하여 당일 배송을 해 주는 "
          "퀵서비스도 발달하였다. 멀리 떨어져 있는 지역에 빠르게 물건을 배송해야 할 경우에는 KTX 특송이나 "
          "고속버스 소화물 서비스를 이용할 수 있다."),
        PARAGRAPH("전화는 집이나 사무실에 연결된 {유선} 전화와 사람들이 가지고 다니는 휴대 전화가 있다. 한국에서는 "
          "{대다수}의 사람들이 휴대 전화를 이용하고 있어서 빠르게 연락하는 것이 가능하다. 요즘에는 스마트폰이 "
          "널리 보급되면서 음성 통화나 영상 통화는 물론 사진, 동영상 등도 자유롭게 주고받을 수 있고 다양한 "
          "정보를 {신속하게|신속하다} 검색할 수 있게 되었다."),
        FIGURE("편의점에서도 택배서비스를 신청할 수 있다."),
        GLOSSARY(("통신망", "서로 연결시켜 주는 조직이나 체계", "통신망"),
              ("무선", "전선을 사용하지 않고 전자 기파를 이용하여 주고받는 통신 방식", "무선"),
              ("플랫폼", "누구나 다양하고 방대한 정보 를 쉽게 활용할 수 있도록 제공 하는 기반 서비스", "플랫폼"),
              ("활성화", "기능이나 활동이 활발함", "활성화"),
              ("쟁점", "서로 다투는 중심이 되는 점", "쟁점")),
        HEADING(3, "인터넷을 통한 정보 교환", translation=
          "Information exchange through the internet" "\n\n"
          "\"The internet is a vast communication network connecting "
          "computers worldwide so they can exchange information, and "
          "Korea's wireless internet (5G, LTE) and public Wi-Fi "
          "speeds are at world-class levels. Internet is well "
          "distributed to public institutions and individual "
          "households, and Wi-Fi is easily accessible on buses, "
          "subways, and in places where many people gather. As more "
          "people use smartphones and tablet PCs in addition to "
          "personal computers, it has become easy to conveniently "
          "exchange communication or obtain needed information "
          "anytime, anywhere." "\n\n"
          "Meanwhile, as online video channel platforms like YouTube "
          "have become more active recently, there is high interest "
          "in solo broadcast creators (1인 방송 크리에이터) who achieve "
          "self-realization (자아실현) through broadcasting while also "
          "earning considerable income. Solo broadcasts mainly "
          "provide various kinds of content — interpreting and "
          "organizing issues currently drawing social attention, or "
          "sharing interesting and useful information about specific "
          "fields.\""),
        PARAGRAPH("인터넷은 전 세계의 컴퓨터가 서로 연결되어 정보를 교환할 수 있는 {거대한|거대하다} 통신망으로 한국의 "
          "무선인터넷(SG, LTE), 공공 와이파이(WIFi) 속도는 세계 최고 수준이다. {공공 기관}이나 "
          "{개별 가정}에 인터넷이 잘 {보급}되어 있는 편이며 버스나 지하철, 사람들이 많이 모이는 장소에서도 "
          "와이파이에 쉽게 {접근할|접근하다} 수 있다. 개인용 컴퓨터 외에도 스마트폰이나 태블릿 PC 등을 "
          "사용하는 사람들이 많아지면서 언제 어디서나 편리하게 연락을 주고받거나 필요한 정보를 얻기 쉬워졌다."),
        PARAGRAPH("{한편}, 최근에는 유튜브 등과 같은 온라인 동영상 채널 플랫폼이 활성화 되면서 방송을 통해 "
          "{자아실현}도 하고 {상당한|상당하다}{수입}도 올리는 1인 방송 크리에이터에 대한 관심이 높다. 1인 "
          "방송은 주로 현재 사회의 관심을 받고 있는 쟁점을 해석하고 정리하거나, 특정 분야에 관한 재미있고 "
          "{유용한|유용하다} 정보를 알려 주는 등 다양한 {볼거리}를 제공하고 있다."),
        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "당신의 문자는 안전합니까? (보이스 피싱과 스미싱, 피해 발생 시 대응 방법)"),
        PARAGRAPH("피싱(Phishing)이란 개인 정보(Pivate Data)를 낚는다(Fishing)라는 의미를 가진 "
          "말로 전화, 문자, 메신저, 가짜 사이트 등 통신수단을 이용하여 개인 정보나 금융 정보를 알아낸 후 "
          "현금을 빼 가는 것을 말한다. 이 중 전화를 이용한 것은 보이스 피싱(voice phishing)이라고 "
          "하며, 문자메시지(SIMS)를 통해 악성 앱을 설치하여 현금을 빼 가는 것은 "
          "스미싱(smishing)이라고 한다. 악성 앱 설치가 의심되면 먼저 모바일 백신으로 악성 앱을 삭제하고 "
          "이동통신사에 모바일 결제 내역이 있는지 확인해야 하며 한국인터넷진흥원(KISA) 개인정보침해 "
          "신고센터(국번 없이 118)에 신고한다."),
        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 한국에서 많이 이용하는 교통수단은 무엇일까?"),
        BULLET("한국인들은 대중교통수단으로 주로 버스, 지하철, 택시를 이용하는데 이용 요금은 ( 현금 ) 이나 ( "
          "교통카드 )로 지불한다."),
        BULLET("대중교통 이용을 권장하기 위해 ( 환승 할인 제도 ), 버스 도착 안내 서비스, ( 버스 전용 차로제 "
          ")와 같은 제도를 시행하고 있다."),
        BULLET("( 환승 할인 제도 )란 이동 중 다른 교통수단으로 변경하더라도 전체 ( 거리 )에 따라 요금을 내도록 "
          "하여 교통비 부담을 덜어주는 제도이다."),
        BULLET("( 버스 전용 차로제 )는 도로의 차로 중 버스만 이용할 수 있는 전용 차로를 정해 버스가 원활히 통행할 "
          "수 있도록 하는 제도이다."),
        HEADING(3, "02 한국에서 많이 사용하는 통신수단은 무엇일까?"),
        BULLET("( 우체국 )을 통해 편지나 물건을 국내뿐만 아니라 외국으로 보낼 수 있는데, 우체국 외에도 택배 업체나 "
          "편의점을 통해 ( 택배 ) 서비스를 이용할 수 있다."),
        BULLET("스마트폰이 널리 보급되면서 음성 통화나 영상 통화는 물론 사진, 동영상 등도 자유롭게 주고받을 수 있고 "
          "다양한 ( 정보 )를 신속하고 편리하게 검색할 수 있게 되었다."),
        BULLET("개인용 컴퓨터 외에도 스마트 폰이나 태블릿 PC 등을 사용하는 사람들이 많아지면서 언제 어디서나 편리하게 "
          "연락을 주고받거나 필요한 ( 정보 )를 얻기 쉬워졌다."),
        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "지금은 1인 미디어 전성시대", translation=
          "Now is the golden age of solo media" "\n\n"
          "\"Among the countless genres of solo broadcasts, which "
          "content draws viewers' clicks? On the video platform "
          "YouTube, the most-viewed broadcast content type was "
          "'cover' videos, which recorded 81.98 million views (as of "
          "May 2018). A cover video is content that imitates or "
          "reinterprets a famous singer's song or dance. Second place "
          "went to 'ASMR' videos, which stimulate the brain with "
          "sounds like wind blowing, the sound of writing with a "
          "pencil, or rustling sounds, inducing psychological calm. "
          "Third place is 'HOW TO' videos, which teach 'methods' "
          "related to various fields such as interpersonal "
          "relationships, work, games, romance, and DIY. Fourth place "
          "is 'OOTD' videos — short for 'Outfit Of The Day' (오늘의 의상), "
          "videos introducing the outfit one wore that day. Following "
          "that, 'mukbang' (eating broadcast) and 'beauty' videos "
          "ranked in popularity.\""),
        PARAGRAPH("수많은 {장르}의 1인 방송 중 어떤 콘텐츠가 시청자들의 클릭을 {유도했|유도하다}을까? 동영상 플랫폼인 "
          "유튜브에서 가장 많이 조회된 방송 콘텐츠 유형은 8198만 회를 기록한 ‘커버’ 영상이었다 (2018년 "
          "5월 기준), 커버 영상이란 유명 가수의 노래나 춤을 {모방하|모방하다}거나 {재해석한|재해석하다} "
          "콘텐츠이다. 2위는 바람이 부는 소리, 연필로 글씨를 쓰는 소리, 바스락거리{는} 소리 등으로 뇌를 "
          "자극해 심리적인 안정을 유도하는 ‘ASMR’ 영상이 기록했다. 3위는 ‘HOW TO’ 영상이다. "
          "대인관계, 업무, 게임, 연애, DIY 등 여러 분야와 관련된 ‘방법’을 알려준다. 4위는 ‘OOTD’ "
          "영상이다. ‘Outfit Of The Day(오늘의 {의상})’의 준말로 그날 그날 자신이 입은 패션을 "
          "소개하는 영상이다. 그 다음 은 ‘먹방’, ‘뷰티’ 영상 순으로 인기를 끌었다."),
        SOURCE("[출처] 스포츠경향(2019.05.15)"),
        MARGIN("{백색소음}"),
        PARAGRAPH("★ 본인이 시청한 1인 미디어 중 도움이 되었거나 좋았던 방송을 이야기해 봅시다."),
        PARAGRAPH("(또 본인이 직접 만들어 보고 싶은 방송 분야는 무엇인지 생각해 봅시다.)"),
    ],
    annotations={
        "발달하다": dict(
            meaning="to develop/be developed",
            surfaces=["발달해"],
        ),
        "지불하다": dict(
            meaning="to pay",
            notes=["similar to 결제하다"],
            surfaces=["지불한다"],
        ),
        "생활권": dict(
            meaning="living zone / commuting sphere",
        ),
        "자가용": dict(
            hanja="自家用",
            meaning="private car / one's own car (for personal use)",
            characters=[("自", None, "self/one's own"), ("家", None,
                "home/household"), ("用", None, "use (same 用 as in 전용, 사용, 이용)")
                ],
        ),
        "장려": dict(
            hanja="獎勵",
            meaning="encouragement/promotion",
        ),
        "권장": dict(
            hanja="勸奬",
            meaning="recommendation/encouragement",
        ),
        "전광판": dict(
            hanja="電光板",
            meaning="electronic display board / digital signboard",
            characters=[("電", None, "electricity"), ("光", None, "light"), ("板"
                , None, "board/panel")],
            notes=["Literally \"electric-light-board\" → an electronic sign "
                "that displays images or text using lights — like a stadium "
                "scoreboard, a highway traffic information sign, or a "
                "building's digital billboard."],
        ),
        "혼잡": dict(
            hanja="混雜",
            meaning="congestion/crowdedness/disorder",
            characters=[("混", None, "to mix/mingle"), ("雜", None,
                "mixed/miscellaneous")],
            notes=["Literally \"mixed-mixed\" → a chaotic state where many "
                "things/people are jumbled together — most commonly used "
                "for traffic congestion (교통 혼잡) or crowding (혼잡한 지하철 = a "
                "crowded subway)."],
        ),
        "제도": dict(
            hanja="制度",
            meaning="system / institution",
        ),
        "전용": dict(
            hanja="專用",
            meaning="exclusive use / dedicated (to one purpose)",
            characters=[("專", None,
                "exclusive/sole/specialized (same 專 as in 전공 \"one's "
                "major/field of study\" — \"exclusive specialization,\" 전문 "
                "\"expert/specialized\")"), ("用", None,
                "use (same 用 as in 사용 \"use,\" 이용 \"utilization\")")],
            notes=["전용 주차장 — reserved/dedicated parking (e.g., 장애인 전용 주차장 = "
                "disabled-only parking)", "여성 전용 칸 — women-only subway car",
                "전용 앱 — a dedicated/exclusive app (made for one specific "
                "purpose/service)", "개인 전용 — for personal/private use only"],
        ),
        "차로제": dict(
            meaning="lane system",
            characters=[("制", "제", "suffix form of 제도, meaning \"system\"")],
            notes=["차로 (車路) — lane (of a road)"],
        ),
        "원활하다": dict(
            hanja="圓滑하다",
            meaning="to be smooth/without a hitch",
            surfaces=["원활히"],
        ),
        "통행하다": dict(
            headword="통행",
            hanja="通行",
            meaning="passage/traffic/passing through",
            characters=[("通", None,
                "to pass through/go through (same 通 as in 교통 "
                "\"traffic/transportation,\" 통과 \"passing through\")"), ("行",
                None, "to go/walk/travel (same 行 as in 여행 \"travel,\" 행동 "
                "\"action/behavior\")")],
            notes=["Literally \"pass-through-go\" → the act of vehicles or "
                "people moving through/along a route — refers to traffic "
                "flow or the general passage of people/vehicles on a road."],
            surfaces=["통행할"],
        ),
        "특송": dict(
            meaning="express delivery",
        ),
        "소화물": dict(
            meaning="small parcel/small cargo",
        ),
        "보급": dict(
            hanja="普及",
            meaning="widespread distribution/dissemination",
            characters=[("普", None, "widely/universally"), ("及", None,
                "to reach/extend")],
            notes=["보급 — distribution/spread/dissemination",
                "Literally \"widely-reaching\" → the spread of something so "
                "it becomes widely available/accessible to many people. → "
                "인터넷이 잘 보급되어 있는 편 = \"internet is fairly well "
                "distributed/spread\" — i.e., widely available across "
                "households/institutions.",
                "Common uses: 스마트폰 보급률 (smartphone penetration rate), 백신 보급 "
                "(vaccine distribution)"],
        ),
        "업체": dict(
            meaning="company / business / firm",
        ),
        "유선": dict(
            meaning="무선 전",
            notes=["무선 전화."],
        ),
        "대다수": dict(
            meaning="the great majority / most",
        ),
        "신속하다": dict(
            meaning="to be swift/prompt",
            surfaces=["신속하게"],
        ),
        "통신망": dict(
            hanja="通信網",
            meaning="communication network/a network or system that connects "
                "things to each other",
        ),
        "무선": dict(
            meaning="wireless",
            notes=["유선 — wired", "무료 — free", "유료 — paid"],
        ),
        "플랫폼": dict(
            meaning="platform",
        ),
        "활성화": dict(
            hanja="活性化",
            meaning="activation / vitalization / becoming active",
            characters=[("活", None, "alive/active (from 활발하다, 원활하다)"), ("性",
                None, "nature/property"), ("化", None,
                "-ization/becoming (same 化 as in 산업화 \"industrialization,\" "
                "강화 \"strengthening\")")],
            notes=["Literally \"alive-nature-ization\"",
                "온라인 동영상 채널 플랫폼이 활성화되면서 = \"as online video platforms "
                "became more active/vitalized\""],
        ),
        "쟁점": dict(
            hanja="爭點",
            meaning="controversial issue/the central point of a "
                "dispute/disagreement",
            characters=[("爭", None,
                "to fight/dispute/contend (same 爭 as in 전쟁 \"war,\" 논쟁 "
                "\"debate/argument\")"), ("點", None,
                "point (same 點 as in 관점 \"viewpoint,\" 장점 \"strong "
                "point/advantage\")")],
            notes=["dispute-point",
                "현재 사회의 관심을 받고 있는 쟁점을 해석하고 = \"interpreting contentious "
                "issues/hot topics currently drawing social attention\""],
        ),
        "거대하다": dict(
            hanja="巨大하다",
            meaning="to be huge/enormous/massive",
            characters=[("巨", None,
                "giant/huge (a character specifically meaning \"great in "
                "size\")"), ("大", None, "big/large")],
            surfaces=["거대한"],
        ),
        "공공 기관": dict(
            meaning="public institution",
        ),
        "개별 가정": dict(
            meaning="individual household",
        ),
        "접근하다": dict(
            meaning="to access / approach / draw near",
            surfaces=["접근할"],
        ),
        "한편": dict(
            meaning="meanwhile / on the other hand",
        ),
        "자아실현": dict(
            meaning="self-realization",
        ),
        "상당하다": dict(
            meaning="to be considerable/substantial/respectable/fairly large",
            notes=["상당수 — a considerable number"],
            surfaces=["상당한"],
        ),
        "수입": dict(
            hanja="收入",
            meaning="earnings/income",
            notes=["상당한 수입도 올리는 = \"earning considerable income\"",
                "수입 (輸入) — import"],
        ),
        "유용하다": dict(
            meaning="to be useful",
            characters=[("有", None, "to have/exist"), ("用", None,
                "use (same 用 from 전용, 이용, etc.)")],
            surfaces=["유용한"],
        ),
        "볼거리": dict(
            meaning="something worth watching / a visual attraction / spectacle",
            notes=["보다 (to see/watch) + 거리 (a suffix meaning \"material/stuff "
                "for ~,\" as in 이야깃거리 \"something to talk about,\" 걱정거리 "
                "\"something to worry about\")",
                "다양한 볼거리를 제공하고 있다 = \"providing various things worth "
                "watching\" / \"offering a variety of viewing content\""],
        ),
        "장르": dict(
            meaning="genre",
        ),
        "유도하다": dict(
            hanja="誘導하다",
            meaning="to induce/lead/guide",
            surfaces=["유도했"],
        ),
        "모방하다": dict(
            hanja="模倣하다",
            meaning="to imitate/copy",
            surfaces=["모방하"],
        ),
        "재해석하다": dict(
            hanja="再解釋하다",
            meaning="to reinterpret",
            characters=[("再", None, "again/re-"), ("解釋", None,
                "interpretation (解 = to unravel/explain — same 解 from 해례본! "
                "— 釋 = to explain/release)")],
            surfaces=["재해석한"],
        ),
        "는": dict(
            meaning="바스락거리다 — \"to rustle\" (an onomatopoeic native Korean "
                "verb, mimicking the sound of dry leaves, paper, plastic "
                "wrap rustling)",
            notes=["~거리다 is a common suffix attached to sound-mimicking or "
                "repetitive-action roots to form a verb: \"to make [that "
                "sound/motion] repeatedly\" — e.g., 반짝거리다 (to "
                "sparkle/glitter repeatedly), 흔들거리다 (to sway/wobble "
                "repeatedly)"],
        ),
        "의상": dict(
            hanja="衣裳",
            meaning="\"clothing/attire/costume\" (more formal/stylistic than "
                "the everyday 옷)",
        ),
        "백색소음": dict(
            meaning="white noise",
        ),
    },
    fixes=[
        ("무선인터넷(SG, LTE)", "무선 인터넷(5G, LTE)", "typo — SG for 5G, plus spacing"),
        ("와이파이(WIFi)", "와이파이(WiFi)", "typo — capital I for i"),
        ("문자메시지(SIMS)", "문자메시지(SMS)", "typo"),
        ("(Pivate Data)", "(Private Data)", "typo"),
        ("전자 기파", "전자기파", "spacing"),
        ("정보 를", "정보를", "spacing"),
        ("운반 하는", "운반하는", "spacing"),
        ("운행하 는", "운행하는", "spacing"),
        ("주행 하기에", "주행하기에", "spacing"),
        ("장려 하는", "장려하는", "spacing"),
        ("활성화 되면서", "활성화되면서", "spacing"),
        ("수입도 올리는", " 수입도 올리는", "missing space, lost at an annotation boundary",
         ("상당한수입도", "상당한 수입도")),
        ("=원활히", "원활히 ", "missing space, lost where the two words are annotated separately",
         ("원활히통행할", "원활히 통행할")),
        ("스마트 폰이나", "스마트폰이나", "spacing"),
        ("그 다음 은", "그 다음은", "spacing — the page keeps the space after 그"),
        ("KTX•SRT", "KTX·SRT", "bullet used for a middle dot"),
        ("48, 전라 지역", "48. 전라 지역", "comma for a period in the unit list"),
        ("영상이었다 (2018년 5월 기준),", "영상이었다(2018년 5월 기준).", "spacing and comma for a period"),
        ("따릉이 (선울), 타슈 (대전), '누비자 (창원), '온누리'(순천), '타랑께 (광주), 어울림'(세종), 여수랑 (여수)",
         "‘따릉이’(서울), ‘타슈’(대전), ‘누비자’(창원), ‘온누리’(순천), ‘타랑께’(광주), ‘어울림’(세종), ‘여수랑’(여수)",
         "typo 선울 for 서울, plus unmatched quotes and spacing throughout the list"),
        ("=전용", "전용 ", "missing space, lost where the two words are annotated separately",
         ("전용차로제", "전용 차로제")),
        ("택배서비스", "택배 서비스", "spacing"),
        ("can be used.Telephones", "can be used.\n\nTelephones",
         "the English translation of 통신수단의 종류와 이용 lost a paragraph break "
         "and a space here, which ran two paragraphs together"),
    ],
    approved={
        # read against the photos of pp. 28-31 and accepted
        "48, 전라 지역", "주행 하기에", "운행하 는", "KTX•SRT", "장려 하는",
        "=전용", "=원활히", "운반 하는", "can be used.Telephones", "택배서비스",
        "전자 기파", "정보 를", "무선인터넷(SG, LTE)", "활성화 되면서",
        "문자메시지(SIMS)", "(Pivate Data)", "스마트 폰이나",
        "영상이었다 (2018년 5월 기준),", "수입도 올리는",
        "와이파이(WIFi)", "그 다음 은",
        "따릉이 (선울), 타슈 (대전), '누비자 (창원), '온누리'(순천), '타랑께 (광주), 어울림'(세종), 여수랑 (여수)",
    },
    headwords={"발달해": "발달하다", "지불한다": "지불하다", "유도했": "유도하다",
               "모방하": "모방하다", "재해석한": "재해석하다", "통행할": "통행하다",
               "접근할": "접근하다", "신속하게": "신속하다", "거대한": "거대하다",
               "상당한": "상당하다", "유용한": "유용하다", "원활히": "원활하다",
               "바스락거리는": "바스락거리다"},
    extraAnnotations={
        "고속버스": dict(
            hanja="高速버스", meaning="express coach",
            characters=[("高", "고", "high — as in 고등학교, 고급 “high grade”"),
                        ("速", "속", "speed — as in 속도 “speed”, 신속하다 “prompt”")],
            notes=["Built for motorway running between cities, as against 시외버스, which "
                   "serves particular places outside the city."],
        ),
        "시외버스": dict(
            hanja="市外버스", meaning="intercity bus",
            characters=[("市", "시", "city, market — as in 도시 “city”, 시장 “market”"),
                        ("外", "외", "outside — as in 외국 “foreign country”, 해외 “overseas”")],
            notes=["Literally “outside-the-city bus”. The opposite prefix is 시내(市內), as in "
                   "시내버스, the bus that stays within the city."],
        ),
    },
)
