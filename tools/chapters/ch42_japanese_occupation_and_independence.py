# -*- coding: utf-8 -*-
"""Chapter 42 — The Japanese occupation and the independence movement.

Transcribed from the photos of pp. 216-219. There is no handwriting on these
pages.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, FIGURE, VERSE, TABLE,
               CELL, GLOSSARY)

CHAPTER = dict(
    number=42, slug="42-japanese-occupation-and-independence",
    unit="역사", title="일제 강점과 독립운동",
    titleEn="The Japanese occupation and the independence movement",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음 자료는 1896년 서재필을 비롯한 당시 {지식인}(공부를 많이 한 사람)들이 만든 "
                  "신문입니다.",
                  "The material below is a newspaper made in 1896 by 서재필 "
                  "and other intellectuals (people who had studied a great "
                  "deal) of the day."),
        FIGURE("독립신문 1면 사진 — 제호는 오른쪽에서 왼쪽으로 ‘독닙신문’, 본문은 한글 세로쓰기"),
        VERSE("정부에서 하는 일을 {백성}에게 전할 것이요, 백성의 일을 정부에 전할 것이니, 만일 백성이 "
              "정부 일을 자세히 알고, 정부에서 백성의 일을 자세히 알면, 서로에게 "
              "{유익한|유익하다} 일만 있을 것이요, {불평하는|불평하다} 마음과 {의심}하는 생각이 "
              "없어질 것이요.",
              translation=
              "What the government does will be conveyed to the people, and "
              "the people’s affairs conveyed to the government; so if the "
              "people know the government’s business in detail and the "
              "government knows the people’s affairs in detail, there will "
              "be only what is good for each, and discontent and suspicion "
              "will disappear."),
        HEADING(4, "01 이 신문의 이름은 무엇인가요? 오늘날 신문과 다른 점은 무엇인가요?",
                translation="What is this newspaper called? How does it "
                            "differ from a newspaper today?"),
        HEADING(4, "02 이 신문은 한글과 {영문}으로 {발행되었습니다|발행되다}. 그 이유는 "
                   "무엇일까요?",
                translation="This newspaper was published in 한글 and in "
                            "English. Why might that be?"),

        SECTION("goals", "학습목표"),
        BULLET("{개항} 이후 {근대} 국가 {수립} 노력에 대해 설명할 수 있다.", ordered=True,
               translation="Explain the efforts to found a modern state "
                           "after the opening of the ports."),
        BULLET("{일제}의 {식민} {통치}에 {맞선|맞서다} 한국인의 {독립운동}에 대해 설명할 수 있다.",
               ordered=True,
               translation="Explain the independence movement of the Koreans "
                           "who stood against Japanese colonial rule."),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"],
              [["기본", "역사", "43. 한국의 역사 인물", "유관순"]]),

        SECTION("part", "01 근대 국가 수립을 위해 어떤 노력을 펼쳤을까?"),
        GLOSSARY(("척화비(서울 마포)",
                  "“서양 오랑캐가 침범하는데 싸우지 않으면 화친(사이좋게 지내는 것)하는 것이요, 화친을 "
                  "주장하는 일은 나라를 파는 일이다.”라는 글이 새겨져 있다.", "척화비",
                  dict(en="It is inscribed with the words “Western barbarians are invading; not to fight is to make peace (to get along on good terms), and to argue for peace is to sell the country.”")),
                 ("개항", "항구를 열어 외국 배가 드나들 수 있게 함.", "개항",
                  dict(en="opening the ports so that foreign ships can come and go"))),
        HEADING(2, "흥선 대원군의 정책과 개항", translation=
                "The policies of 흥선 대원군 and the opening of the ports" "\n\n"
                "In the latter half of the nineteenth century 흥선 대원군 took "
                "charge of government in place of his son 고종, who had "
                "become king at the young age of twelve. To raise the king’s "
                "authority he rebuilt 경복궁 and pursued policies such as "
                "having taxes paid on a reasonable basis. He also refused the "
                "demands for trade from Western countries such as France and "
                "the United States and, putting up 척화비 and the like, did "
                "not open the country’s doors." "\n\n"
                "After 흥선 대원군 stepped down, a wind of change blew through "
                "조선. Just then Japan demanded that 조선 open its doors, and "
                "조선 opened its ports through the 강화도 Treaty (1876)."),
        PARAGRAPH("19세기 {후반} 12세의 어린 나이로 왕이 된 고종을 대신해 아버지 {흥선 대원군}이 "
                  "정치를 맡았다. 그는 왕의 {권위}를 높이기 위해 {경복궁}을 고쳐 지었고 세금을 "
                  "{합리적}으로 내게 하는 등의 정책을 {펼쳤다|펼치다}. 또한 프랑스, 미국 등 서양 국가의 "
                  "{무역} 요구를 {거절하고|거절하다} {척화비}를 세우는 등 나라의 문을 열지 않았다."),
        PARAGRAPH("흥선 대원군이 {물러난|물러나다} 뒤 조선에 변화의 바람이 불었다. 마침 일본이 조선에 "
                  "나라의 문을 열 것을 요구하였고, 조선은 {강화도 조약}(1876년)을 통해 {개항}을 "
                  "하였다."),
        FIGURE("척화비(서울 마포) — 낱말 풀이에 딸린 비석 사진"),

        GLOSSARY(("문물", "문화의 산물", "문물",
                  dict(en="the products of culture")),
                 ("개혁", "새롭게 뜯어고침", "개혁",
                  dict(en="overhauling something anew")),
                 ("개화", "새로운 사상이나 문물을 받아들여 발전함", "개화",
                  dict(en="taking in new ideas and culture and developing")),
                 ("급진", "급하게 진행함", "급진",
                  dict(en="going ahead in haste")),
                 ("만민 공동회",
                  "독립 협회는 만민 공동회라는 집회를 열어 강대국의 정치적 간섭과 경제 침략을 비판하고, "
                  "나라를 바로잡을 것을 정부에 요구하였다.", "만민 공동회",
                  dict(en="The 독립 협회 held the rallies called 만민 공동회, criticised the great powers’ political interference and economic aggression, and demanded that the government put the country right."))),
        HEADING(2, "근대 국가 수립을 위한 노력과 일본의 침략", translation=
                "Efforts to found a modern state, and Japan’s aggression" "\n\n"
                "After the opening of the ports, efforts unfolded to take in "
                "foreign culture and institutions or to reform the country "
                "and develop it into a modern state. Some people, who thought "
                "조선 had to modernise faster, even attempted radical reform "
                "to change the framework of the whole country to suit the new "
                "age. The peasants who believed in 동학, which stressed human "
                "equality in place of high and low status, called for reform "
                "as they carried out the 동학 Peasant Movement." "\n\n"
                "In 1896 서재필 and other intellectuals made news from inside "
                "and outside the country known to foreigners as well as "
                "Koreans through 독립신문, which was written in 한글 and "
                "English. They also formed the 독립 협회 (Independence Club), "
                "put up 독립문 as an expression of their will to make an "
                "independent country, and held the rally called 만민 공동회 "
                "to criticise foreign aggression." "\n\n"
                "Meanwhile Japan, having won the Russo-Japanese War, began "
                "its aggression against the Korean peninsula in earnest. In "
                "1905 Japan forced the conclusion of a treaty taking away "
                "대한 제국’s diplomatic rights, and interfered in its "
                "politics. Koreans raised 의병 (righteous armies) and fought "
                "against Japan’s aggression, but in the end lost their "
                "sovereignty in 1910."),
        PARAGRAPH("{개항} 이후 외국의 {문물}을 받아들이거나 나라를 {개혁}하여 근대 국가로 발전시키려는 "
                  "노력이 {전개되었다|전개되다}. 조선이 더 빨리 {개화}해야 한다고 생각했던 일부 "
                  "사람들은 나라 전체의 {틀}을 새로운 시대에 맞게 바꾸려고 {급진}적인 개혁을 "
                  "{시도하기도|시도하다} 했다. {신분}의 높낮음 대신 인간 {평등}을 강조한 {동학}을 믿는 "
                  "농민들은 {동학 농민 운동}을 펼치면서 개혁을 요구하였다."),
        PARAGRAPH("1896년에 {서재필}을 비롯한 {지식인}들은 한글과 영어로 된 {독립신문}을 통해 나라 "
                  "{안팎}의 소식을 한국인은 물론 외국인에게도 알렸다. 또한 {독립 협회}를 만들어 "
                  "{자주적}인 나라를 만들겠다는 {의지}를 담아 {독립문}을 세웠고, {만민 공동회}라는 "
                  "{집회}를 열어 외국의 {침략}을 {비판하였다|비판하다}."),
        PARAGRAPH("한편, {러·일 전쟁}에서 이긴 일본은 {한반도}에 대한 침략을 {본격적}으로 시작했다. "
                  "1905년 일본은 {대한 제국}의 {외교권}을 가져가는 {조약}을 {강제}로 {맺게|맺다} "
                  "했고, 대한 제국의 정치에 {간섭하였다|간섭하다}. 한국인들은 {의병}을 일으켜 일본의 "
                  "침략에 맞서 싸웠지만 결국 1910년 {주권}을 {빼앗기고|빼앗기다} 말았다."),
        FIGURE("독립문(서울 서대문구)"),
        FIGURE("만민 공동회 — 낱말 풀이에 딸린 흑백 사진, 깃대 아래 모인 군중"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "조선, {황제} 국가로 {거듭나다}", translation=
                "조선 is reborn as an empire" "\n\n"
                "고종, who had been king of 조선, changed the country’s name "
                "from ‘조선’ to ‘대한 제국’ in 1897 in order to restore the "
                "standing (dignity and trust) of a country that had fallen "
                "low. At that time 고종 built 환구단 (the altar where an "
                "emperor offers rites to heaven) and there ascended to the "
                "position of emperor. During the Japanese occupation 환구단 "
                "was done away with and the 조선 Hotel went up on the site, "
                "so that today only 황궁우 (an annexe of 환구단) remains."),
        PARAGRAPH("조선의 왕이었던 고종은 땅에 떨어진 나라의 {위신}({위엄}과 믿음)을 세우기 위해 "
                  "1897년 나라 이름을 ‘조선’에서 ‘대한 제국’으로 바꾸었다. 당시 고종은 하늘에 "
                  "{제사}를 지내는 {환구단}(황제가 하늘에 제사를 지내는 {제단})을 짓고 이곳에서 황제의 "
                  "자리에 올랐다. {일제 강점기}에 환구단은 없어졌고 그 자리에 조선 호텔이 들어서 오늘날 "
                  "{황궁우}(환구단의 {부속} 건물)만 남아 있다."),
        FIGURE("황궁우(왼쪽)와 환구단(오른쪽)"),

        SECTION("part", "02 한국인은 독립운동을 어떻게 펼쳐 나갔을까?"),
        GLOSSARY(("강압", "강한 힘으로 내리 누름", "강압",
                  dict(en="pressing down with strong force")),
                 ("고문", "몸에 고통을 주면서 질문하는 것", "고문",
                  dict(en="questioning while inflicting pain on the body")),
                 ("물자", "물건이나 자원", "물자",
                  dict(en="goods or resources")),
                 ("일본군 ‘위안부’", "일본 군인을 위해 강제로 성노예 생활을 해야만 했던 여성",
                  "위안부",
                  dict(en="women who were forced to live as sexual slaves for Japanese soldiers"))),
        HEADING(2, "일제(일본 제국)의 강압 통치", translation=
                "The coercive rule of 일제 (the Japanese Empire)" "\n\n"
                "After taking away 대한 제국’s sovereignty, Japan ruled by "
                "coercion. It shut Koreans who opposed Japanese rule in "
                "prison and tortured them. It also sold off land that Koreans "
                "had owned at low prices to Japanese land companies or "
                "Japanese people, and increased rice production in Korea and "
                "sent it to Japan." "\n\n"
                "In the 1930s Japan invaded China (the Sino-Japanese War), "
                "and during the Second World War it attacked Pearl Harbor in "
                "Hawaii in the United States (the Pacific War). When soldiers "
                "and supplies ran short because of the war, Japan dragged off "
                "many young Koreans and put them to work in factories and "
                "mines, and sent them to the battlefield as soldiers. There "
                "were also cases of some Korean women being deceived or taken "
                "by force and made into ‘comfort women’ for the Japanese "
                "army."),
        PARAGRAPH("일본은 대한 제국의 {국권}을 {빼앗은|빼앗다} 뒤 {강압}적으로 {통치}하였다. 일본의 "
                  "{지배}에 반대하는 한국인을 {감옥}에 {가두고|가두다} {고문}을 하였다. 또한 한국인이 "
                  "{소유하고|소유하다} 있던 땅을 일본 {토지} 회사나 일본인에게 {싼값}으로 "
                  "{팔아넘기거나|팔아넘기다} 한국에서 쌀 생산을 늘려 일본으로 보내기도 했다."),
        PARAGRAPH("1930년대에 일본은 중국을 침략하였고({중·일 전쟁}), {제2차 세계 대전} 중에는 미국 "
                  "하와이 {진주만}을 {공격하였다|공격하다}({태평양 전쟁}). 전쟁으로 인해 군인과 "
                  "{물자}가 {부족해지자|부족해지다} 일본은 한국의 많은 청년을 끌고 가 공장이나 "
                  "{탄광}에서 일을 시켰고 {전쟁터}에 {병사}로 보내기도 했다. 또한, 일부 한국 여성들을 "
                  "{속이거나|속이다} 강제로 끌고 가서 일본군 ‘{위안부}’로 삼는 일도 있었다."),
        FIGURE("일본으로 보낼 쌀을 쌓아 놓은 군산항"),
        FIGURE("평화의 소녀상 — 일본군 ‘위안부’ 문제에 대한 진상 규명과 책임 이행 등을 촉구하며 곳곳에 "
               "조각상이 세워졌다."),

        GLOSSARY(("김구(1876~1949)", "대한민국 임시 정부를 이끌며 독립운동을 지도하였다.",
                  "김구",
                  dict(en="He led the Provisional Government of the Republic of Korea and guided the independence movement."))),
        HEADING(2, "일제에 맞서 싸운 한국인의 독립운동", translation=
                "The independence movement of the Koreans who fought 일제" "\n\n"
                "During the Japanese occupation Koreans carried on the "
                "independence movement without cease in order to win back the "
                "country’s sovereignty. In the 3·1 운동 of 1919 millions of "
                "people came out into the streets and demanded independence. "
                "With this as the occasion, 김구 and others took the lead in "
                "setting up the Provisional Government of the Republic of "
                "Korea in Shanghai, China. The Provisional Government led the "
                "independence movement, letting the world know that Korea was "
                "an independent state." "\n\n"
                "From around 1920 the independence army carried on a vigorous "
                "armed struggle against the Japanese army, centred on the "
                "Manchuria region of China. The independence army defeated "
                "the Japanese army in several battles and achieved great "
                "results." "\n\n"
                "Within the country, people sought to build up Koreans’ "
                "abilities through the press, education and economic "
                "activity. The independence movement that continued in this "
                "way at home and abroad was a great help in Korea becoming "
                "independent. At last, on 15 August 1945, Korea regained its "
                "sovereignty."),
        PARAGRAPH("일제 강점기에 한국인들은 나라의 국권을 {되찾기|되찾다} 위해 {끊임없이} 독립운동을 펼쳐 "
                  "나갔다. 1919년 {3·1 운동}에는 수백만 명의 사람들이 거리에 나와 독립을 요구하였다. "
                  "이를 {계기}로 {김구} 등이 중심이 되어 중국 상하이에 {대한민국 임시 정부}를 세웠다. "
                  "임시 정부는 한국이 독립 국가라는 것을 세계에 알리며 독립운동을 이끌었다."),
        PARAGRAPH("1920년 {무렵}부터는 중국 {만주} 지방을 중심으로 {독립군}이 일본군을 상대로 활발한 "
                  "{무장 투쟁}을 {벌여|벌이다} 나갔다. 독립군은 여러 {전투}에서 일본군을 "
                  "{물리쳐|물리치다} 큰 {성과}를 {거두었다|거두다}."),
        PARAGRAPH("국내에서는 {언론}, 교육, 경제 활동을 통해 한국인의 {실력}을 키우고자 하였다. 이처럼 "
                  "{국내외}에서 계속된 독립운동은 한국이 독립하는 데 큰 도움이 되었다. 마침내 1945년 "
                  "8월 15일 한국은 주권을 되찾았다."),
        FIGURE("김구(1876~1949) — 낱말 풀이에 딸린 인물 사진"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "일제 강점기 독립운동을 이끈 대한민국 임시 정부", translation=
                "The Provisional Government of the Republic of Korea, which "
                "led the independence movement under the occupation" "\n\n"
                "The Provisional Government of the Republic of Korea built a "
                "secret network of contacts linked to the homeland, passed "
                "news of itself into the country and received money to be "
                "used for the independence movement. It also set up a "
                "military academy to train soldiers and educated the "
                "independence army, and helped with the publication of "
                "독립신문. And to make known the fact of Japan’s aggression "
                "and the history of Korea it published books, and it sent "
                "diplomats all over the world to show the need for Korea’s "
                "independence and the will for it."),
        PARAGRAPH("대한민국 임시 정부는 국내와 연결되는 {비밀} {연락망}을 만들어 대한민국 임시 정부의 "
                  "소식을 국내에 전했고 독립운동에 쓰일 돈을 {전달받기도|전달받다} 하였다. 또, 군인을 "
                  "{길러내는|길러내다} {무관 학교}를 세워 독립군을 교육하였고 독립신문 {발간}에도 "
                  "도움을 주었다. 그리고 일본의 침략 사실과 한국 역사를 알리기 위해 책을 "
                  "{펴내고|펴내다} 세계 {곳곳}에 {외교관}을 보내 한국 독립의 {필요성}과 의지를 "
                  "보여주었다."),
        FIGURE("대한민국 임시 정부에서 활동한 인물들(1921년)"),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 근대 국가 수립을 위해 어떤 노력을 펼쳤을까?"),
        BULLET("(            )은 서양 국가의 무역 요구를 거절하며 척화비를 세우는 등 나라의 문을 열지 "
               "않았다."),
        BULLET("일본이 조선에 나라의 문을 열 것을 요구하였고 조선은 (        ) 조약을 통해 "
               "개항하였다."),
        BULLET("서재필을 비롯한 지식인들은 한글과 영어로 된 (        )을 통해 나라 안팎의 소식을 알렸고 "
               "독립협회를 만들어 자주적인 나라를 만들기 위해 노력하였다."),
        HEADING(3, "02 한국인은 독립운동을 어떻게 펼쳐 나갔을까?"),
        BULLET("일본은 전쟁으로 인해 물자가 부족해지자 한국에서 많은 사람들을 데려갔다. 일부 한국 여성은 "
               "일본군 ‘(        )’로 끌려 가기도 했다."),
        BULLET("1919년에 일어난 (        )에는 수백만 명의 사람들이 참여하여 독립을 요구하였다."),
        BULLET("중국 상하이에 세워진 (                )는 한국이 독립 국가임을 세계에 알리며 "
               "독립운동을 이끌었다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "[독립을 위해 {목숨}을 {바친|바치다} 사람들: 윤봉길과 남자현]",
                translation="Those who gave their lives for independence: "
                            "윤봉길 and 남자현"),
        BULLET("1932년 4월, 상하이에서 발생한 중국군과 일본군의 {무력 충돌}에서 일본군이 "
               "{승리한|승리하다} 것을 축하하려고 많은 일본인이 홍커우 공원에 모여 있었다. 윤봉길은 그 "
               "공원에 들어가 행사가 {한창} 진행되고 있을 때 {단상}을 향해 {폭탄}을 던졌다. 큰 "
               "{폭발}과 함께 일본군 상하이 {총사령관}을 비롯한 여러 일본인이 쓰러졌다. 윤봉길은 그 "
               "자리에서 {체포되었고|체포되다} 젊은 나이에 목숨을 잃었다.",
               translation=
               "In April 1932 many Japanese had gathered in 홍커우 Park to "
               "celebrate the Japanese army’s victory in the armed clash "
               "between the Chinese and Japanese armies that had broken out "
               "in Shanghai. 윤봉길 went into the park and, when the event "
               "was in full swing, threw a bomb at the platform. With a "
               "great explosion, several Japanese fell, among them the "
               "commander-in-chief of the Japanese army in Shanghai. 윤봉길 "
               "was arrested on the spot and lost his life at a young age."),
        BULLET("한국에서 3·1 운동을 경험한 남자현은 만주로 가서 독립운동에 참여하였다. 그녀는 독립에 "
               "대한 사람들의 {의식}을 높였고 특히 여성에 대한 교육을 강조하였다. 1932년 "
               "{국제 연맹} {조사단}이 중국 하얼빈을 방문했을 때에는 손가락을 잘라 ‘한국의 독립을 "
               "원한다.’라는 {혈서}(피로 쓴 편지)를 보내 독립을 {호소하였다|호소하다}. 그녀가 속한 "
               "독립군 {부대}에서 {유일한|유일하다} 여성 {대원}으로 독립운동을 벌이다가 체포된 그녀는 "
               "고문을 받으면서도 {단식}(식사를 하지 않음)으로 {저항하다가|저항하다} "
               "{사망하였다|사망하다}.",
               translation=
               "남자현, who had lived through the 3·1 운동 in Korea, went to "
               "Manchuria and took part in the independence movement. She "
               "raised people’s awareness of independence and laid "
               "particular stress on education for women. When the League of "
               "Nations commission of inquiry visited Harbin in China in "
               "1932, she cut off a finger and sent a 혈서 (a letter written "
               "in blood) saying ‘I want Korea’s independence’, appealing "
               "for independence. Arrested while working for independence as "
               "the only woman in the independence army unit she belonged "
               "to, she resisted by fasting (not eating) even under torture, "
               "and died."),
        PARAGRAPH("★ 자신의 고향 나라에서 나라를 위해 목숨을 바치거나 큰 {희생}을 한 인물을 소개해 "
                  "봅시다. 그들의 활동을 통해 느낀 점을 이야기해 봅시다.",
                  "Introduce someone from your home country who gave their "
                  "life for the country or made a great sacrifice. Talk about "
                  "what their deeds made you feel."),
    ],

    extraAnnotations={
        "지식인": dict(
            hanja="知識人", meaning="an intellectual, an educated person",
            characters=[("知", "지", "to know — as in 지식, 통지"),
                        ("識", "식", "to recognise — as in 의식, 상식"),
                        ("人", "인", "person")],
            notes=["The page glosses it itself: 공부를 많이 한 사람."],
        ),
        "백성": dict(
            hanja="百姓", meaning="the common people, the subjects of a king",
            characters=[("百", "백", "a hundred"),
                        ("姓", "성", "a surname — as in 성명")],
            notes=["Literally “the hundred surnames”: everyone who is not "
                   "the ruler. The word of a kingdom; a republic says 국민."],
        ),
        "유익하다": dict(
            hanja="有益하다", meaning="to be beneficial, of use",
            characters=[("有", "유", "to have — as in 소유, 유일"),
                        ("益", "익", "benefit — as in 이익, 권익")],
            surfaces=["유익한"],
        ),
        "불평하다": dict(
            hanja="不平하다", meaning="to complain, to be discontented",
            characters=[("不", "불", "not"),
                        ("平", "평", "level, calm — as in 평등, 평화")],
            surfaces=["불평하는"],
        ),
        "의심": dict(
            hanja="疑心", meaning="suspicion, doubt",
            characters=[("疑", "의", "to doubt — as in 용의자, 혐의"),
                        ("心", "심", "heart, mind — as in 중심, 관심")],
        ),
        "영문": dict(
            hanja="英文", meaning="English (writing)",
            characters=[("英", "영", "England, English — as in 영어, 영국"),
                        ("文", "문", "writing — as in 문물, 문화")],
        ),
        "발행되다": dict(
            hanja="發行되다", meaning="to be published, issued",
            characters=[("發", "발", "to send out — as in 발간, 발생"),
                        ("行", "행", "to carry out — as in 행사, 시행")],
            surfaces=["발행되었습니다"],
        ),
        "개항": dict(
            hanja="開港", meaning="the opening of the ports (to foreign trade)",
            characters=[("開", "개", "to open — as in 개화, 전개"),
                        ("港", "항", "a port — as in 항구, 공항")],
            notes=["For 조선 it means 1876, the 강화도 조약 with Japan."],
        ),
        "근대": dict(
            hanja="近代", meaning="the modern age",
            characters=[("近", "근", "near — as in 최근, 접근"),
                        ("代", "대", "an age — as in 시대, 현대")],
            notes=["근대 국가 is “a modern state”. 근대 is the age before "
                   "현대, the present one."],
        ),
        "수립": dict(
            hanja="樹立", meaning="founding, establishing",
            characters=[("樹", "수", "a tree, to plant"),
                        ("立", "립", "to stand — as in 독립, 설립")],
            notes=["Said of a state, a government, a plan: 정부 수립."],
        ),
        "일제": dict(
            hanja="日帝", meaning="Imperial Japan",
            characters=[("日", "일", "Japan, the sun — as in 일본"),
                        ("帝", "제", "an emperor — as in 황제, 제국")],
            notes=["Short for 일본 제국(주의), as the heading on p. 218 "
                   "spells out: 일제(일본 제국)."],
        ),
        "식민": dict(
            hanja="植民", meaning="colonisation, colonial",
            characters=[("植", "식", "to plant — as in 식물"),
                        ("民", "민", "people — as in 국민, 농민")],
            notes=["식민 통치 “colonial rule”, 식민지 “a colony”."],
        ),
        "통치": dict(
            hanja="統治", meaning="rule, government (of a country)",
            characters=[("統", "통", "to command, to unite — as in 대통령, 통일"),
                        ("治", "치", "to govern — as in 정치, 자치")],
        ),
        "맞서다": dict(
            meaning="to stand against, to confront",
            notes=["일본의 침략에 맞서 싸우다 “to fight against Japan’s "
                   "aggression”."],
            surfaces=["맞선"],
        ),
        "독립운동": dict(
            hanja="獨立運動", meaning="the independence movement",
            characters=[("獨立", None, "independence — 獨 alone, 立 to stand"),
                        ("運動", None, "a movement — 運 to carry, 動 to move")],
        ),
        "후반": dict(
            hanja="後半", meaning="the latter half",
            characters=[("後", "후", "after — as in 이후, 오후"),
                        ("半", "반", "half — as in 한반도, 절반")],
            notes=["Its pair is 전반, the first half."],
        ),
        "흥선 대원군": dict(
            hanja="興宣大院君",
            meaning="흥선 대원군 (1820–1898), father of 고종 and regent",
            characters=[("興宣", None, "his title — 興 to rise, 宣 to proclaim"),
                        ("大院君", None, "the title given to a king’s father "
                                         "who was not himself king")],
        ),
        "권위": dict(
            hanja="權威", meaning="authority",
            characters=[("權", "권", "power, right — as in 주권, 국권"),
                        ("威", "위", "might, dignity — as in 위신, 위엄")],
        ),
        "경복궁": dict(
            hanja="景福宮", meaning="경복궁, the main palace of 조선",
            characters=[("景", "경", "bright, a view — as in 경치"),
                        ("福", "복", "good fortune"),
                        ("宮", "궁", "a palace")],
            notes=["Burnt in the invasions of the 1590s and rebuilt under "
                   "흥선 대원군 in the 1860s."],
        ),
        "합리적": dict(
            hanja="合理的", meaning="rational, reasonable",
            characters=[("合", "합", "to fit — as in 합의, 통합"),
                        ("理", "리", "reason — as in 이유, 관리"),
                        ("的", "적", "the suffix “-ic, -al”")],
        ),
        "펼치다": dict(
            meaning="to unfold, to carry out (a policy, a movement)",
            notes=["Both article titles use it: 노력을 펼치다, 독립운동을 "
                   "펼쳐 나가다."],
            surfaces=["펼쳤다"],
        ),
        "무역": dict(
            hanja="貿易", meaning="trade (between countries)",
            characters=[("貿", "무", "to trade"),
                        ("易", "역", "to exchange")],
        ),
        "거절하다": dict(
            hanja="拒絶하다", meaning="to refuse, to turn down",
            characters=[("拒", "거", "to resist — as in 거부"),
                        ("絶", "절", "to cut off — as in 단절")],
            surfaces=["거절하고"],
        ),
        "척화비": dict(
            hanja="斥和碑",
            meaning="the stone tablets 흥선 대원군 set up rejecting peace "
                    "with the West",
            characters=[("斥", "척", "to repel — as in 배척"),
                        ("和", "화", "peace — as in 화친, 평화"),
                        ("碑", "비", "a stone tablet — as in 비석")],
            notes=["Put up across the country in 1871. The one photographed "
                   "is captioned 서울 마포."],
        ),
        "물러나다": dict(
            meaning="to step down, to withdraw",
            surfaces=["물러난"],
        ),
        "강화도 조약": dict(
            hanja="江華島條約", meaning="the Treaty of 강화도 (1876)",
            characters=[("江華島", None, "강화도, the island west of Seoul — "
                                         "島 an island"),
                        ("條約", None, "a treaty — 條 a clause, 約 a promise")],
            notes=["The treaty with Japan by which 조선 opened its ports."],
        ),
        "문물": dict(
            hanja="文物", meaning="the products of a civilisation, culture "
                                  "and institutions",
            characters=[("文", "문", "culture, writing — as in 문화, 영문"),
                        ("物", "물", "a thing — as in 물자, 물건")],
        ),
        "개혁": dict(
            hanja="改革", meaning="reform",
            characters=[("改", "개", "to change — as in 개선, 개정"),
                        ("革", "혁", "to change utterly — as in 혁명")],
        ),
        "전개되다": dict(
            hanja="展開되다", meaning="to unfold, to develop",
            characters=[("展", "전", "to spread out — as in 발전, 전시"),
                        ("開", "개", "to open — as in 개항, 개화")],
            surfaces=["전개되었다"],
        ),
        "개화": dict(
            hanja="開化", meaning="enlightenment, opening up to new ideas",
            characters=[("開", "개", "to open — as in 개항"),
                        ("化", "화", "to change, to become — as in 변화, 문화")],
            notes=["The word of the late 조선 reformers; 개화기 is the "
                   "period."],
        ),
        "틀": dict(
            meaning="a frame, a framework",
            notes=["나라 전체의 틀 “the framework of the whole country”."],
        ),
        "급진": dict(
            hanja="急進", meaning="radical, going ahead fast",
            characters=[("急", "급", "urgent — as in 급히, 응급"),
                        ("進", "진", "to advance — as in 진행, 진출")],
            notes=["급진적 “radical”; its opposite is 점진적 “gradual”."],
        ),
        "시도하다": dict(
            hanja="試圖하다", meaning="to attempt",
            characters=[("試", "시", "to try — as in 시험"),
                        ("圖", "도", "to plan, a drawing — as in 의도, 지도")],
            surfaces=["시도하기도"],
        ),
        "신분": dict(
            hanja="身分", meaning="social status, rank",
            characters=[("身", "신", "the body, oneself — as in 자신"),
                        ("分", "분", "a share, a lot — as in 부분, 구분")],
        ),
        "평등": dict(
            hanja="平等", meaning="equality",
            characters=[("平", "평", "level — as in 불평, 평화"),
                        ("等", "등", "a grade, equal — as in 동등, 등급")],
        ),
        "동학": dict(
            hanja="東學", meaning="동학, “Eastern Learning”",
            characters=[("東", "동", "east — as in 동양"),
                        ("學", "학", "learning — as in 학교")],
            notes=["A religion founded in 1860 by 최제우, named against "
                   "서학, “Western Learning”, which meant Catholicism."],
        ),
        "동학 농민 운동": dict(
            hanja="東學農民運動", meaning="the 동학 Peasant Movement (1894)",
            characters=[("東學", None, "동학"),
                        ("農民", None, "peasants, farmers — 農 farming, "
                                       "民 people"),
                        ("運動", None, "a movement")],
        ),
        "서재필": dict(
            hanja="徐載弼",
            meaning="서재필 (1864–1951), founder of 독립신문 and the "
                    "독립 협회",
        ),
        "독립신문": dict(
            hanja="獨立新聞", meaning="독립신문, “The Independent” (1896)",
            characters=[("獨立", None, "independence"),
                        ("新聞", None, "a newspaper — 新 new, 聞 to hear")],
            notes=["Printed in 한글 with an English edition. The masthead in "
                   "the photograph on p. 216 spells it 독닙신문.",
                   "The Provisional Government’s paper on p. 218 took the "
                   "same name."],
        ),
        "안팎": dict(
            meaning="inside and outside",
            notes=["안 + 밖. 나라 안팎의 소식 “news from home and abroad”."],
        ),
        "독립 협회": dict(
            hanja="獨立協會", meaning="the Independence Club (1896)",
            characters=[("獨立", None, "independence"),
                        ("協會", None, "an association — 協 to join in, "
                                       "會 to meet")],
            notes=["The article spaces it 독립 협회; the review on p. 219 "
                   "prints 독립협회."],
        ),
        "자주적": dict(
            hanja="自主的", meaning="independent, self-reliant",
            characters=[("自", "자", "self — as in 자신, 자발적"),
                        ("主", "주", "master — as in 주권, 주인"),
                        ("的", "적", "the suffix “-ic, -al”")],
        ),
        "의지": dict(
            hanja="意志", meaning="will, resolve",
            characters=[("意", "의", "a thought — as in 의식, 의미"),
                        ("志", "지", "a purpose — as in 지원")],
        ),
        "독립문": dict(
            hanja="獨立門", meaning="독립문, the Independence Gate",
            characters=[("獨立", None, "independence"),
                        ("門", "문", "a gate")],
            notes=["Put up by the 독립 협회 in 서대문구, Seoul."],
        ),
        "만민 공동회": dict(
            hanja="萬民共同會",
            meaning="the 만민 공동회, the mass rallies of the 독립 협회",
            characters=[("萬民", None, "all the people — 萬 ten thousand, "
                                       "民 people"),
                        ("共同", None, "joint, together — 共 together, "
                                       "同 same"),
                        ("會", "회", "a meeting — as in 집회, 협회")],
        ),
        "집회": dict(
            hanja="集會", meaning="a rally, an assembly",
            characters=[("集", "집", "to gather — as in 모집, 집단"),
                        ("會", "회", "to meet — as in 회의, 협회")],
        ),
        "침략": dict(
            hanja="侵略", meaning="aggression, invasion",
            characters=[("侵", "침", "to invade — as in 침해, 침범"),
                        ("略", "략", "to seize, a plan — as in 전략")],
        ),
        "비판하다": dict(
            hanja="批判하다", meaning="to criticise",
            characters=[("批", "비", "to comment on"),
                        ("判", "판", "to judge — as in 판단, 재판")],
            surfaces=["비판하였다"],
        ),
        "러·일 전쟁": dict(
            hanja="露日戰爭", meaning="the Russo-Japanese War (1904–1905)",
            characters=[("露", "로", "Russia — 러 is short for 러시아"),
                        ("日", "일", "Japan"),
                        ("戰爭", None, "a war — 戰 to fight, 爭 to contend")],
        ),
        "한반도": dict(
            hanja="韓半島", meaning="the Korean peninsula",
            characters=[("韓", "한", "Korea"),
                        ("半", "반", "half — as in 후반"),
                        ("島", "도", "an island — as in 강화도")],
        ),
        "본격적": dict(
            hanja="本格的", meaning="in earnest, full-scale",
            characters=[("本", "본", "the root, proper — as in 기본, 본인"),
                        ("格", "격", "a form, a standard — as in 자격, 성격"),
                        ("的", "적", "the suffix “-ic, -al”")],
        ),
        "대한 제국": dict(
            hanja="大韓帝國", meaning="the Korean Empire (1897–1910)",
            characters=[("大韓", None, "Great Korea — as in 대한민국"),
                        ("帝國", None, "an empire — 帝 an emperor, "
                                       "國 a country")],
            notes=["The name 고종 gave the country in 1897; see the "
                   "알아두면 좋아요 on p. 217."],
        ),
        "외교권": dict(
            hanja="外交權", meaning="the right to conduct diplomacy",
            characters=[("外交", None, "diplomacy — 外 outside, 交 to deal "
                                       "with"),
                        ("權", "권", "a right — as in 주권, 국권")],
            notes=["The treaty of 1905 is the one usually called 을사늑약; "
                   "the page does not name it."],
        ),
        "조약": dict(
            hanja="條約", meaning="a treaty",
            characters=[("條", "조", "a clause — as in 조건, 조항"),
                        ("約", "약", "a promise — as in 약속, 계약")],
            notes=["조약을 맺다 “to conclude a treaty”."],
        ),
        "강제": dict(
            hanja="强制", meaning="force, compulsion",
            characters=[("强", "강", "strong — as in 강압, 강조"),
                        ("制", "제", "to control — as in 제도, 규제")],
            notes=["강제로 “by force”."],
        ),
        "맺다": dict(
            meaning="to conclude (a treaty), to tie",
            surfaces=["맺게"],
        ),
        "간섭하다": dict(
            hanja="干涉하다", meaning="to interfere, to meddle",
            characters=[("干", "간", "to meddle with"),
                        ("涉", "섭", "to cross, to be involved — as in 교섭")],
            surfaces=["간섭하였다"],
        ),
        "의병": dict(
            hanja="義兵", meaning="a righteous army, volunteer fighters",
            characters=[("義", "의", "right, just — as in 정의, 의무"),
                        ("兵", "병", "a soldier — as in 병사, 병역")],
            notes=["Ordinary people who took up arms of their own accord "
                   "when the country was invaded."],
        ),
        "주권": dict(
            hanja="主權", meaning="sovereignty",
            characters=[("主", "주", "master — as in 자주적, 주인"),
                        ("權", "권", "power, right — as in 국권, 권위")],
        ),
        "빼앗기다": dict(
            meaning="to be robbed of, to have taken away",
            notes=["The passive of 빼앗다."],
            surfaces=["빼앗기고"],
        ),
        "황제": dict(
            hanja="皇帝", meaning="an emperor",
            characters=[("皇", "황", "an emperor — as in 황궁우"),
                        ("帝", "제", "an emperor — as in 제국, 일제")],
        ),
        "거듭나다": dict(
            meaning="to be born again, to be made anew",
            notes=["거듭 “again” + 나다 “to be born”."],
        ),
        "위신": dict(
            hanja="威信", meaning="prestige, standing",
            characters=[("威", "위", "might, dignity — as in 위엄, 권위"),
                        ("信", "신", "trust — as in 신뢰, 신용")],
            notes=["The page glosses it itself: 위엄과 믿음."],
        ),
        "위엄": dict(
            hanja="威嚴", meaning="dignity, majesty",
            characters=[("威", "위", "might, dignity — as in 위신"),
                        ("嚴", "엄", "strict, solemn — as in 엄격")],
        ),
        "제사": dict(
            hanja="祭祀", meaning="a rite of offering",
            characters=[("祭", "제", "to offer a rite — as in 제단, 축제"),
                        ("祀", "사", "to offer a rite")],
            notes=["Chapter 15 has the family 제사 for ancestors; here it is "
                   "the emperor’s rite to heaven."],
        ),
        "환구단": dict(
            hanja="圜丘壇",
            meaning="환구단, the altar where the emperor offered rites to "
                    "heaven",
            characters=[("圜", "환", "round"),
                        ("丘", "구", "a mound"),
                        ("壇", "단", "an altar, a platform — as in 제단, 단상")],
        ),
        "제단": dict(
            hanja="祭壇", meaning="an altar",
            characters=[("祭", "제", "to offer a rite — as in 제사"),
                        ("壇", "단", "a platform — as in 단상, 환구단")],
        ),
        "일제 강점기": dict(
            hanja="日帝强占期",
            meaning="the period of Japanese occupation (1910–1945)",
            characters=[("日帝", None, "Imperial Japan"),
                        ("强占", None, "seizure by force — 强 strong, "
                                       "占 to occupy"),
                        ("期", "기", "a period — as in 기간, 시기")],
        ),
        "황궁우": dict(
            hanja="皇穹宇",
            meaning="황궁우, the shrine building that stood beside 환구단",
            characters=[("皇", "황", "an emperor — as in 황제"),
                        ("穹", "궁", "the vault of heaven"),
                        ("宇", "우", "a house, the heavens — as in 우주")],
        ),
        "부속": dict(
            hanja="附屬", meaning="attached, annexed",
            characters=[("附", "부", "to attach — as in 부여, 첨부"),
                        ("屬", "속", "to belong — as in 소속")],
            notes=["부속 건물 “an annexe, an outbuilding”."],
        ),
        "국권": dict(
            hanja="國權", meaning="national sovereignty",
            characters=[("國", "국", "a country"),
                        ("權", "권", "power, right — as in 주권, 외교권")],
        ),
        "빼앗다": dict(
            meaning="to take away by force, to rob",
            surfaces=["빼앗은"],
        ),
        "강압": dict(
            hanja="强壓", meaning="coercion, oppression",
            characters=[("强", "강", "strong — as in 강제, 강대국"),
                        ("壓", "압", "to press — as in 압력, 억압")],
        ),
        "지배": dict(
            hanja="支配", meaning="rule, domination",
            characters=[("支", "지", "to hold up, to manage — as in 지원, 지급"),
                        ("配", "배", "to allot — as in 배분, 배달")],
        ),
        "감옥": dict(
            hanja="監獄", meaning="a prison",
            characters=[("監", "감", "to watch over — as in 감독, 감시"),
                        ("獄", "옥", "a gaol")],
        ),
        "가두다": dict(
            meaning="to lock up, to shut in",
            surfaces=["가두고"],
        ),
        "고문": dict(
            hanja="拷問", meaning="torture",
            characters=[("拷", "고", "to beat"),
                        ("問", "문", "to ask — as in 질문, 방문")],
        ),
        "소유하다": dict(
            hanja="所有하다", meaning="to own",
            characters=[("所", "소", "that which — as in 소득, 장소"),
                        ("有", "유", "to have — as in 유익, 유일")],
            surfaces=["소유하고"],
        ),
        "토지": dict(
            hanja="土地", meaning="land",
            characters=[("土", "토", "earth — as in 국토"),
                        ("地", "지", "ground — as in 지방, 지역")],
        ),
        "싼값": dict(
            meaning="a low price",
            notes=["싸다 “cheap” + 값 “price”, written as one word."],
        ),
        "팔아넘기다": dict(
            meaning="to sell off, to make over by sale",
            notes=["팔다 “to sell” + 넘기다 “to hand over”."],
            surfaces=["팔아넘기거나"],
        ),
        "중·일 전쟁": dict(
            hanja="中日戰爭", meaning="the Sino-Japanese War (1937–1945)",
            characters=[("中", "중", "China — as in 중국"),
                        ("日", "일", "Japan"),
                        ("戰爭", None, "a war")],
        ),
        "제2차 세계 대전": dict(
            hanja="第二次世界大戰", meaning="the Second World War",
            characters=[("第二次", None, "the second — 第 the ordinal prefix, "
                                         "次 a time, a turn"),
                        ("世界", None, "the world"),
                        ("大戰", None, "a great war — 大 great, 戰 to fight")],
        ),
        "진주만": dict(
            hanja="眞珠灣", meaning="Pearl Harbor",
            characters=[("眞珠", None, "a pearl"),
                        ("灣", "만", "a bay")],
        ),
        "공격하다": dict(
            hanja="攻擊하다", meaning="to attack",
            characters=[("攻", "공", "to attack — as in 전공"),
                        ("擊", "격", "to strike — as in 충격, 타격")],
            surfaces=["공격하였다"],
        ),
        "태평양 전쟁": dict(
            hanja="太平洋戰爭", meaning="the Pacific War (1941–1945)",
            characters=[("太平洋", None, "the Pacific — 太平 great peace, "
                                         "洋 an ocean"),
                        ("戰爭", None, "a war")],
        ),
        "물자": dict(
            hanja="物資", meaning="supplies, goods and materials",
            characters=[("物", "물", "a thing — as in 문물, 물건"),
                        ("資", "자", "resources — as in 자원, 자금")],
        ),
        "부족해지다": dict(
            hanja="不足해지다", meaning="to run short",
            characters=[("不", "부", "not"),
                        ("足", "족", "enough — as in 만족")],
            surfaces=["부족해지자"],
        ),
        "탄광": dict(
            hanja="炭鑛", meaning="a coal mine",
            characters=[("炭", "탄", "coal — as in 석탄, 연탄"),
                        ("鑛", "광", "a mine, ore — as in 광산")],
        ),
        "전쟁터": dict(
            hanja="戰爭터", meaning="a battlefield",
            characters=[("戰爭", None, "war")],
            notes=["터 is the native word for a site, as in 일터, 놀이터."],
        ),
        "병사": dict(
            hanja="兵士", meaning="a soldier",
            characters=[("兵", "병", "a soldier — as in 의병, 병역"),
                        ("士", "사", "a man of rank — as in 변호사")],
        ),
        "속이다": dict(
            meaning="to deceive",
            notes=["The causative of 속다 “to be deceived”."],
            surfaces=["속이거나"],
        ),
        "위안부": dict(
            hanja="慰安婦",
            meaning="‘comfort women’: women forced into sexual slavery for "
                    "the Japanese army",
            characters=[("慰", "위", "to console — as in 위로"),
                        ("安", "안", "ease — as in 안전, 안녕"),
                        ("婦", "부", "a woman — as in 주부, 부부")],
            notes=["The book always sets the word in quotation marks, "
                   "일본군 ‘위안부’, because it was the army’s own "
                   "euphemism."],
        ),
        "되찾다": dict(
            meaning="to win back, to regain",
            notes=["되- “back, again” + 찾다 “to find”."],
            surfaces=["되찾기"],
        ),
        "끊임없이": dict(
            meaning="without cease, constantly",
            notes=["끊임 “a break” + 없이 “without”."],
        ),
        "3·1 운동": dict(
            hanja="三一運動",
            meaning="the March First Movement (1 March 1919)",
            characters=[("三一", None, "3·1 — the first of March, read 삼일"),
                        ("運動", None, "a movement")],
            notes=["The date is kept as the public holiday 삼일절."],
        ),
        "계기": dict(
            hanja="契機", meaning="an occasion, a turning point",
            characters=[("契", "계", "a bond — as in 계약"),
                        ("機", "기", "an opportunity — as in 기회, 위기")],
            notes=["이를 계기로 “with this as the occasion”."],
        ),
        "김구": dict(
            hanja="金九",
            meaning="김구 (1876–1949), leader of the Provisional Government",
        ),
        "대한민국 임시 정부": dict(
            hanja="大韓民國臨時政府",
            meaning="the Provisional Government of the Republic of Korea "
                    "(1919)",
            characters=[("大韓民國", None, "the Republic of Korea"),
                        ("臨時", None, "provisional — 臨 to face, 時 time"),
                        ("政府", None, "a government")],
        ),
        "무렵": dict(
            meaning="around (a time)",
            notes=["1920년 무렵 “around 1920”."],
        ),
        "만주": dict(
            hanja="滿洲", meaning="Manchuria",
            characters=[("滿", "만", "full — here for the sound"),
                        ("洲", "주", "a continent, a land")],
        ),
        "독립군": dict(
            hanja="獨立軍", meaning="the independence army",
            characters=[("獨立", None, "independence"),
                        ("軍", "군", "an army — as in 군인, 일본군")],
        ),
        "무장 투쟁": dict(
            hanja="武裝鬪爭", meaning="armed struggle",
            characters=[("武裝", None, "arming — 武 military, 裝 to equip"),
                        ("鬪爭", None, "a struggle — 鬪 to fight, "
                                       "爭 to contend")],
        ),
        "벌이다": dict(
            meaning="to wage, to carry on (a struggle, a campaign)",
            surfaces=["벌여"],
        ),
        "전투": dict(
            hanja="戰鬪", meaning="a battle",
            characters=[("戰", "전", "to fight — as in 전쟁"),
                        ("鬪", "투", "to fight — as in 투쟁")],
        ),
        "물리치다": dict(
            meaning="to defeat, to drive back",
            surfaces=["물리쳐"],
        ),
        "성과": dict(
            hanja="成果", meaning="a result, an achievement",
            characters=[("成", "성", "to achieve — as in 성공, 완성"),
                        ("果", "과", "a fruit, a result — as in 결과, 효과")],
            notes=["성과를 거두다 “to achieve results”."],
        ),
        "거두다": dict(
            meaning="to reap, to achieve",
            surfaces=["거두었다"],
        ),
        "언론": dict(
            hanja="言論", meaning="the press, the media",
            characters=[("言", "언", "words — as in 언어, 조언"),
                        ("論", "론", "to discuss — as in 토론, 여론")],
        ),
        "실력": dict(
            hanja="實力", meaning="real ability, strength",
            characters=[("實", "실", "real — as in 사실, 실제"),
                        ("力", "력", "strength — as in 능력, 무력")],
            notes=["실력을 키우다 “to build up one’s ability”."],
        ),
        "국내외": dict(
            hanja="國內外", meaning="at home and abroad",
            characters=[("國", "국", "a country"),
                        ("內", "내", "inside — as in 국내"),
                        ("外", "외", "outside — as in 국외, 외교")],
        ),
        "비밀": dict(
            hanja="祕密", meaning="secret",
            characters=[("祕", "비", "hidden"),
                        ("密", "밀", "close, secret — as in 밀접")],
        ),
        "연락망": dict(
            hanja="連絡網", meaning="a network of contacts",
            characters=[("連", "연", "to link — as in 연결, 관련"),
                        ("絡", "락", "to connect"),
                        ("網", "망", "a net — as in 통신망")],
        ),
        "전달받다": dict(
            hanja="傳達받다", meaning="to have passed on to one, to receive",
            characters=[("傳", "전", "to pass on — as in 전하다, 전통"),
                        ("達", "달", "to reach — as in 배달, 발달")],
            surfaces=["전달받기도"],
        ),
        "길러내다": dict(
            meaning="to train up, to turn out (people)",
            notes=["기르다 “to rear” + 내다 “to bring out”."],
            surfaces=["길러내는"],
        ),
        "무관 학교": dict(
            hanja="武官學校", meaning="a military academy",
            characters=[("武官", None, "a military officer — 武 military, "
                                       "官 an official"),
                        ("學校", None, "a school")],
        ),
        "발간": dict(
            hanja="發刊", meaning="publication",
            characters=[("發", "발", "to send out — as in 발행, 발생"),
                        ("刊", "간", "to print — as in 월간, 출간")],
        ),
        "펴내다": dict(
            meaning="to publish, to bring out (a book)",
            surfaces=["펴내고"],
        ),
        "곳곳": dict(
            meaning="everywhere, place after place",
            notes=["곳 “a place”, doubled."],
        ),
        "외교관": dict(
            hanja="外交官", meaning="a diplomat",
            characters=[("外交", None, "diplomacy"),
                        ("官", "관", "an official — as in 무관, 장관")],
        ),
        "필요성": dict(
            hanja="必要性", meaning="necessity, the need for",
            characters=[("必", "필", "must — as in 필수"),
                        ("要", "요", "to need — as in 중요, 요구"),
                        ("性", "성", "the suffix “-ness, -ity”")],
        ),
        "목숨": dict(
            meaning="one’s life",
            notes=["목숨을 바치다 “to give one’s life”, 목숨을 잃다 “to lose "
                   "one’s life”."],
        ),
        "바치다": dict(
            meaning="to offer up, to devote",
            surfaces=["바친"],
        ),
        "무력 충돌": dict(
            hanja="武力衝突", meaning="an armed clash",
            characters=[("武力", None, "armed force — 武 military, "
                                       "力 strength"),
                        ("衝突", None, "a collision — 衝 to dash against, "
                                       "突 sudden")],
        ),
        "승리하다": dict(
            hanja="勝利하다", meaning="to win, to be victorious",
            characters=[("勝", "승", "to win — as in 우승"),
                        ("利", "리", "advantage — as in 이익, 권리")],
            surfaces=["승리한"],
        ),
        "한창": dict(
            meaning="at its height, in full swing",
        ),
        "단상": dict(
            hanja="壇上", meaning="the platform, the rostrum",
            characters=[("壇", "단", "a platform — as in 제단, 환구단"),
                        ("上", "상", "on, above")],
        ),
        "폭탄": dict(
            hanja="爆彈", meaning="a bomb",
            characters=[("爆", "폭", "to burst — as in 폭발"),
                        ("彈", "탄", "a shell, a bullet")],
        ),
        "폭발": dict(
            hanja="爆發", meaning="an explosion",
            characters=[("爆", "폭", "to burst — as in 폭탄"),
                        ("發", "발", "to go off — as in 발생, 발간")],
        ),
        "총사령관": dict(
            hanja="總司令官", meaning="a commander-in-chief",
            characters=[("總", "총", "overall — as in 총리, 총선"),
                        ("司令", None, "command — 司 to take charge of, "
                                       "令 an order"),
                        ("官", "관", "an officer — as in 외교관")],
        ),
        "체포되다": dict(
            hanja="逮捕되다", meaning="to be arrested",
            characters=[("逮", "체", "to catch up with"),
                        ("捕", "포", "to seize")],
            surfaces=["체포되었고"],
        ),
        "의식": dict(
            hanja="意識", meaning="awareness, consciousness",
            characters=[("意", "의", "a thought — as in 의지, 의미"),
                        ("識", "식", "to recognise — as in 지식인")],
        ),
        "국제 연맹": dict(
            hanja="國際聯盟", meaning="the League of Nations",
            characters=[("國際", None, "international"),
                        ("聯盟", None, "a league — 聯 to link, 盟 an oath")],
        ),
        "조사단": dict(
            hanja="調査團", meaning="a commission of inquiry",
            characters=[("調査", None, "an investigation — 調 to look into, "
                                       "査 to examine"),
                        ("團", "단", "a body of people — as in 단체")],
            notes=["The League’s commission of 1932 is the one known as "
                   "the Lytton Commission."],
        ),
        "혈서": dict(
            hanja="血書", meaning="a letter written in blood",
            characters=[("血", "혈", "blood — as in 혈액, 헌혈"),
                        ("書", "서", "writing — as in 서류, 문서")],
            notes=["The page glosses it itself: 피로 쓴 편지."],
        ),
        "호소하다": dict(
            hanja="呼訴하다", meaning="to appeal, to plead",
            characters=[("呼", "호", "to call out — as in 호흡, 호칭"),
                        ("訴", "소", "to appeal — as in 소송")],
            surfaces=["호소하였다"],
        ),
        "부대": dict(
            hanja="部隊", meaning="a (military) unit",
            characters=[("部", "부", "a section — as in 부분, 일부"),
                        ("隊", "대", "a troop — as in 대원, 군대")],
        ),
        "유일하다": dict(
            hanja="唯一하다", meaning="to be the only one",
            characters=[("唯", "유", "only"),
                        ("一", "일", "one")],
            surfaces=["유일한"],
        ),
        "대원": dict(
            hanja="隊員", meaning="a member of a unit",
            characters=[("隊", "대", "a troop — as in 부대, 군대"),
                        ("員", "원", "a member — as in 직원, 위원")],
        ),
        "단식": dict(
            hanja="斷食", meaning="fasting, a hunger strike",
            characters=[("斷", "단", "to cut off — as in 판단, 차단"),
                        ("食", "식", "to eat — as in 식사, 음식")],
            notes=["The page glosses it itself: 식사를 하지 않음."],
        ),
        "저항하다": dict(
            hanja="抵抗하다", meaning="to resist",
            characters=[("抵", "저", "to push against"),
                        ("抗", "항", "to oppose — as in 반항, 항의")],
            surfaces=["저항하다가"],
        ),
        "사망하다": dict(
            hanja="死亡하다", meaning="to die",
            characters=[("死", "사", "to die — as in 사형"),
                        ("亡", "망", "to perish — as in 망하다")],
            surfaces=["사망하였다"],
        ),
        "희생": dict(
            hanja="犧牲", meaning="a sacrifice",
            characters=[("犧", "희", "a sacrificial animal"),
                        ("牲", "생", "a sacrificial animal")],
            notes=["희생을 하다 “to make a sacrifice”."],
        ),
    },

    extraNotes=[
        "The photograph of 독립신문 on p. 216 is not reproduced. The passage "
        "printed over it on a slip of paper is set as a quotation.",
        "The margin photographs — 척화비 and 만민 공동회 on p. 217, 군산항 "
        "and 김구 on p. 218 — and the photographs of 독립문, 환구단, the "
        "평화의 소녀상 and the Provisional Government are not reproduced; "
        "their captions are. 만민 공동회 and 김구 have no caption of their "
        "own beyond the glossary row they stand under.",
        "개항 is printed once in the margin of p. 217, beside the second "
        "article, though the first article marks the word too; it is set "
        "with the first.",
        "The review gaps on p. 219 are blank in the book and left blank here.",
    ],
)
