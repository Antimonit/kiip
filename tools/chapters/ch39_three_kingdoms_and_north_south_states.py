# -*- coding: utf-8 -*-
"""Chapter 39 — The Three Kingdoms and the North–South States.

Transcribed from the photos of pp. 204-207. Nothing is written on these
pages by hand.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, FIGURE, LABELS,
               TABLE, CELL, GLOSSARY)

CHAPTER = dict(
    number=39, slug="39-three-kingdoms-and-north-south-states",
    unit="역사", title="삼국 시대와 남북국 시대",
    titleEn="The Three Kingdoms and the North–South States",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 고구려, 백제, 신라의 {건국} 이야기입니다.",
                  "Below are the founding stories of 고구려, 백제 and 신라."),
        PARAGRAPH("하늘 신의 아들인 해모수와 물을 {다스리는|다스리다} 신의 딸인 유화 사이에서 한 남자 아이가 "
                  "태어났다. 그는 알을 깨고 나왔는데 어릴 때부터 {활}을 잘 {쏘아|쏘다} 사람들은 그를 "
                  "주몽이라고 불렀다. 다른 왕자들이 주몽을 미워하여 죽이려고 하자 주몽은 자신을 따르는 "
                  "{무리}를 {이끌고|이끌다} 남쪽으로 내려와 졸본에 고구려를 세웠다.",
                  "A boy was born to 해모수, the son of the god of heaven, and "
                  "유화, the daughter of the god who rules the waters. He came "
                  "out by breaking an egg, and because he shot well with a "
                  "bow from childhood people called him 주몽. When the other "
                  "princes hated 주몽 and tried to kill him, he led the band "
                  "that followed him down to the south and founded 고구려 at "
                  "졸본."),
        PARAGRAPH("주몽에게는 부여에서 낳은 아들 유리, 졸본에서 낳은 아들 비류와 온조가 있었다. 유리가 주몽을 "
                  "찾아와 다음 왕의 자리를 {잇게|잇다} 되자 비류와 온조는 고구려를 떠났다. 비류가 죽은 뒤 "
                  "비류를 따르던 사람들은 위례성에 자리 잡은 온조에게 왔다. 온조는 {백성}이 많아지고 나라가 "
                  "커지자 나라 이름을 십제에서 백제로 바꾸었다.",
                  "주몽 had a son, 유리, born in 부여, and two sons, 비류 and 온조, "
                  "born in 졸본. When 유리 came to find 주몽 and was to succeed "
                  "him as the next king, 비류 and 온조 left 고구려. After 비류 "
                  "died, the people who had followed him came to 온조, who had "
                  "settled at 위례성. As his people grew in number and the "
                  "country grew larger, 온조 changed its name from 십제 to 백제."),
        PARAGRAPH("여섯 마을로 이루어진 작은 나라가 있었다. 어느 날, 이 나라의 한 {촌장}이 {우물가}에서 울고 "
                  "있는 흰말과 커다란 알을 발견하였다. 얼마 후 알에서 남자아이가 나왔다. 촌장들은 세상을 밝게 "
                  "한다는 뜻에서 이 아이에게 혁거세라는 이름을 지어 주었다. 사람들은 그를 하늘에서 내려온 "
                  "아이라고 생각하여 사로국(신라의 옛 이름)의 첫 번째 왕으로 {삼았다|삼다}.",
                  "There was a small country made up of six villages. One "
                  "day a village chief of this country found a white horse "
                  "crying beside a well, and a very large egg. A while later "
                  "a boy came out of the egg. The village chiefs gave the "
                  "child the name 혁거세, meaning that he makes the world "
                  "bright. People thought of him as a child come down from "
                  "heaven and made him the first king of 사로국 (the old name "
                  "of 신라)."),
        HEADING(4, "01 이와 같은 건국 이야기는 어떤 역사적인 의미가 담겨 있을까요?",
                translation="What historical meaning might founding stories "
                            "like these carry?"),
        HEADING(4, "02 고구려, 백제, 신라는 각각 어느 지역에서 세워졌을까요?",
                translation="In which region was each of 고구려, 백제 and 신라 "
                            "founded?"),

        SECTION("goals", "학습목표"),
        BULLET("삼국 시대의 {성립}과 발전 과정을 설명할 수 있다.", ordered=True,
               translation="Explain how the Three Kingdoms period came "
                           "about and developed."),
        BULLET("남북국 시대의 발전과 문화에 대해 설명할 수 있다.", ordered=True,
               translation="Explain the development and the culture of the "
                           "North–South States period."),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"],
              [["기본", "문화", "16. 명절", "추석"]]),

        SECTION("part", "01 삼국은 어떻게 발전했을까?"),
        HEADING(2, "삼국의 건국", translation=
                "The founding of the Three Kingdoms" "\n\n"
                "After 고조선, a number of countries were founded on the "
                "Korean peninsula. 주몽 founded 고구려 in the 졸본 area of the "
                "압록강 basin, and 온조, known as the son of 주몽, came down to "
                "the 한강 basin and founded 백제. Meanwhile, 박혁거세 founded "
                "신라 in the 경주 area. These three countries developed, at "
                "times competing and at times exchanging with one another, "
                "in order to hold wider territory. This period is called "
                "the Three Kingdoms period."),
        GLOSSARY(("유역", "강물이 흐르는 지역의 주변", "유역",
                  dict(en="the land around where a river flows"))),
        PARAGRAPH("{고조선} 이후 {한반도}에는 여러 나라가 세워졌다. 주몽은 {압록강} 유역 졸본 지역에 고구려를 "
                  "세웠고, 주몽의 아들로 {알려진|알려지다} 온조는 한강 {유역}으로 내려와 백제를 세웠다. "
                  "{한편}, 박혁거세는 경주 지역에 신라를 세웠다. 이 세 나라는 더 넓은 {영토}를 "
                  "{차지하기|차지하다} 위해 때로는 {경쟁하고|경쟁하다} 때로는 {교류하며|교류하다} "
                  "발전하였다. 이 {시기}를 {삼국 시대}라고 부른다."),

        HEADING(2, "삼국의 발전", translation=
                "The development of the Three Kingdoms" "\n\n"
                "Of the Three Kingdoms, the first to reach its heyday was "
                "백제. In the 4th century 백제 widened its territory not only "
                "over the area north of the 한강 but as far as the south "
                "coast, and traded actively with the regions of China and "
                "Japan as well. In particular it developed a splendid and "
                "delicate culture and passed it on to 왜." "\n\n"
                "고구려 greatly widened its territory in the 5th century. To "
                "the north it held the Manchuria region, and to the south as "
                "far as the central region of the Korean peninsula, "
                "including the 한강 basin. 백제 and 신라 at times formed an "
                "alliance to stand against this. When 왜 invaded 신라, 고구려 "
                "also helped 신라 and drove 왜 back." "\n\n"
                "신라 developed greatly in the 6th century. It built up the "
                "country’s strength on the basis of an organisation called "
                "화랑도, made up of young men of the nobility and the "
                "commoners. As a result it took the 한강 basin and laid the "
                "foundation for unifying the Three Kingdoms."),
        GLOSSARY(("전성기", "가장 발전한 시기", "전성기",
                  dict(en="the period of greatest development")),
                 ("왜", "7세기 말 이전에 일본 또는 일본인을 부르던 호칭. 7세기 말 이후부터 ‘일본’이라고 부름.",
                  "왜",
                  dict(en="the name by which Japan or the Japanese were called before the end of the 7th century. From the end of the 7th century on it is called ‘일본’.")),
                 ("동맹", "둘 이상의 개인이나 단체가 힘을 합치기로 약속함.", "동맹",
                  dict(en="two or more individuals or groups promising to join forces.")),
                 ("충주 고구려비(충북 충주)", "5세기에 고구려가 한반도 중부 지역을 차지했다는 기록이 있다.",
                  "충주 고구려비",
                  dict(en="it carries a record that 고구려 held the central region of the Korean peninsula in the 5th century."))),
        PARAGRAPH("삼국 중 가장 먼저 {전성기}를 {맞이한|맞이하다} 나라는 백제였다. 4세기에 백제는 한강 북쪽 "
                  "지역은 물론 {남해안}까지 영토를 {넓혔고|넓히다} 중국, 일본 지역과도 "
                  "{활발하게|활발하다} {무역}을 하였다. 특히 {화려하고|화려하다} {섬세한|섬세하다} 문화를 "
                  "발전시켜 {왜}에 전해 주었다."),
        PARAGRAPH("고구려는 5세기에 영토를 크게 넓혔다. 북쪽으로 {만주} 지역을, 남쪽으로는 한강 유역을 "
                  "{포함한|포함하다} 한반도 {중부} 지역까지 차지하였다. 백제와 신라는 이에 "
                  "{맞서기|맞서다} 위해 {동맹}을 {맺기도|맺다} 했다. 왜가 신라에 {침입했을|침입하다} 때는 "
                  "신라를 도와 왜를 {물리치기도|물리치다} 하였다."),
        PARAGRAPH("신라는 6세기에 크게 발전하였다. {귀족}과 {평민}의 {청년}들로 {구성된|구성되다} "
                  "{화랑도}라는 {조직}을 {바탕}으로 나라의 힘을 {키웠다|키우다}. 그 결과 한강 유역을 "
                  "차지하면서 삼국 {통일}의 {기반}을 {마련하였다|마련하다}."),
        FIGURE("충주 고구려비(충북 충주) — 글자가 새겨진 돌 비석 사진"),
        LABELS("4세기: 백제의 전성기", "5세기: 고구려의 전성기", "6세기: 신라의 전성기"),
        FIGURE("삼국의 영토를 색으로 나타낸 지도 세 장 — 고구려, 백제, 신라, 가야, 탐라 (6세기 지도에는 "
               "가야가 없다)"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "삼국은 왜 한강 유역을 차지하려고 했을까?", translation=
                "Why did the Three Kingdoms try to take the 한강 basin?" "\n\n"
                "The 한강 basin lies at the centre of the Korean peninsula, "
                "and with its wide plains it is a good place for farming. "
                "It is also a region where goods can easily be carried to "
                "many areas by boat on the 한강, and one well placed for "
                "exchanging directly with China by sea. Because of these "
                "advantages the 한강 basin was regarded as a very important "
                "place not only in the Three Kingdoms period but in the 고려 "
                "and 조선 periods too. What is more, Seoul, the capital of "
                "the Republic of Korea today, also sits in the 한강 basin."),
        PARAGRAPH("한강 유역은 한반도의 중심에 {위치해|위치하다} 있으며, 넓은 {평야}가 있어 "
                  "{농사짓기|농사짓다}에 좋은 곳이다. 또한 한강에서 배를 이용해 물건을 여러 지역으로 쉽게 "
                  "{실어 나를|실어 나르다} 수 있으며, 바다를 통해 중국과 직접 교류하기에도 "
                  "{유리한|유리하다} 지역이다. 이러한 {장점} 때문에 한강 유역은 삼국 시대는 물론 고려, 조선 "
                  "시대에도 매우 중요한 곳으로 {여겨졌다|여겨지다}. 뿐만 아니라 현재 대한민국의 {수도}인 "
                  "서울도 한강 유역에 {자리잡고|자리잡다} 있다."),
        FIGURE("한강 유역의 삼국 시대 유적지 분포 — 한강 주변의 산성과 고분, 유적 발굴 위치를 표시한 지도"),

        SECTION("part", "02 남북국 시대에는 어떤 나라들이 발전했을까?"),
        HEADING(2, "신라의 삼국 통일", translation=
                "신라’s unification of the Three Kingdoms" "\n\n"
                "신라 was the first of the Three Kingdoms to be founded, but "
                "it grew by steadily raising the country’s people of ability "
                "and conducting diplomacy with other countries. After taking "
                "the 한강 basin, the centre of the Korean peninsula, 신라 "
                "joined forces with the 당 dynasty of China and brought down "
                "백제 (660) and 고구려 (668) in turn." "\n\n"
                "But when 당, which had been allied with 신라, tried to rule "
                "even 신라, 신라 stood against 당 and went to war. The 신라 army "
                "won one victory after another over 당 at the battle of 매소성, "
                "the sea battle of 기벌포 and elsewhere, and at last drove 당 "
                "out and unified the Three Kingdoms (676)."),
        GLOSSARY(("인재", "재주가 뛰어난 사람", "인재",
                  dict(en="a person of outstanding ability")),
                 ("연합", "서로 힘을 합쳐 하나가 됨", "연합",
                  dict(en="joining forces with each other and becoming one"))),
        PARAGRAPH("신라는 삼국 중 가장 먼저 세워졌지만 {꾸준히} 나라의 {인재}를 {기르고|기르다} 다른 나라와 "
                  "{외교}를 하면서 {성장하였다|성장하다}. 한반도의 중심인 한강 유역을 차지한 이후 신라는 "
                  "중국의 {당나라}와 힘을 {합쳐|합치다} 백제(660년)와 고구려(668년)를 {차례로} "
                  "{멸망시켰다|멸망시키다}."),
        PARAGRAPH("그런데 신라와 {연합}했던 당이 신라까지 {지배하려고|지배하다} 하자 신라는 당에 맞서 전쟁을 "
                  "{벌였다|벌이다}. 신라군은 매소성 {전투}, 기벌포 {해전} 등에서 {잇달아} 당에 "
                  "{승리하였고|승리하다} {마침내} 당을 {몰아내고|몰아내다} 삼국을 통일하였다(676년)."),

        HEADING(2, "통일 신라와 발해", translation=
                "Unified 신라 and 발해" "\n\n"
                "Having unified the Three Kingdoms, 신라 carried out policies "
                "meant to make all the people living on the Korean peninsula "
                "of one mind. For example, it gave government posts to the "
                "people of the old 백제 and 고구려 as well, or chose them as "
                "soldiers. It also made peace with 당, with which it had once "
                "been at war, and exchanged actively with it. In the Unified "
                "신라 period Buddhist culture such as 석굴암 and 불국사 developed "
                "greatly, and 첨성대, the oldest astronomical observatory in "
                "the East, was built as well." "\n\n"
                "Meanwhile, after 고구려 fell there were efforts to win 고구려 "
                "back. 대조영, who had been a general of 고구려, founded 발해 "
                "together with the displaced people of 고구려 in the northern "
                "region of the Korean peninsula and the Manchuria region of "
                "China (698). 발해 developed its culture on the basis of the "
                "culture of 고구려 while taking in the culture of the "
                "countries around it. From the Buddhist statues and stone "
                "lanterns, the lotus-patterned roof tiles and so on that "
                "remain in the 발해 region, one can gather how high the "
                "Buddhist culture of 발해 was. The period in which Unified "
                "신라 in the south and 발해 in the north existed together is "
                "called the North–South States period."),
        GLOSSARY(("관직", "국가가 맡기는 일", "관직",
                  dict(en="work entrusted by the state")),
                 ("유민", "멸망하여 없어진 나라의 백성", "유민",
                  dict(en="the people of a country that has fallen and ceased to exist")),
                 ("발해의 기와(위)와 고구려의 기와(아래)",
                  "기와의 제작 기법, 모양 등을 통해 발해 문화가 고구려의 문화를 계승하였음을 짐작할 수 있다.",
                  "기와",
                  dict(en="from the way the roof tiles were made, their shape and so on, one can gather that the culture of 발해 carried on the culture of 고구려."))),
        PARAGRAPH("삼국을 통일한 신라는 한반도에 사는 모든 사람이 {한마음}이 되도록 하기 위한 {정책}을 "
                  "{실시하였다|실시하다}. 예를 들어, 옛 백제와 고구려 사람에게도 {관직}을 주거나 그들을 "
                  "{군인}으로 {뽑았다|뽑다}. 또한 {한때} 전쟁을 벌였던 당과도 {화해하고|화해하다} 활발하게 "
                  "교류하였다. 통일 신라 시대에는 {석굴암}, {불국사}와 같은 {불교} 문화가 크게 "
                  "{발달하였고|발달하다} {동양}에서 가장 오래된 {천문대}인 {첨성대}가 만들어지기도 했다."),
        PARAGRAPH("한편, 고구려가 멸망한 후 고구려를 {되찾기|되찾다} 위한 노력이 나타났다. 고구려 {장군} "
                  "{출신}이었던 대조영은 고구려 {유민}들과 함께 한반도 {북부} 지역과 중국 만주 지역에 발해를 "
                  "세웠다(698년). 발해는 고구려 문화를 바탕으로 주변 나라의 문화를 "
                  "{받아들이며|받아들이다} 문화를 발전시켰다. 발해 지역에 남아 있는 {불상}과 {석등}, "
                  "{연꽃무늬} {기와} 등을 통해 발해의 수준 높은 불교문화를 {짐작할|짐작하다} 수 있다. 남쪽의 "
                  "통일신라와 북쪽의 발해가 함께 {존재한|존재하다} 시기를 {남북국 시대}라고 한다."),
        FIGURE("통일 신라와 발해 — 북쪽의 발해와 남쪽의 신라를 색으로 나타낸 지도"),
        FIGURE("발해의 기와(위)와 고구려의 기와(아래) — 연꽃무늬가 새겨진 둥근 기와 사진 두 장"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "남북국은 어떤 나라들을 의미할까?", translation=
                "Which countries does ‘남북국’ mean?" "\n\n"
                "When the 부여 clan (the family name of the 백제 royal house) "
                "fell and the 고 clan (the family name of the 고구려 royal "
                "house) fell, the 김 clan (the family name of the 신라 royal "
                "house) took the land to the south, and the 대 clan (대조영) "
                "took the land to the north and called it 발해. This is "
                "called 남북국, the North and South States. A history of the "
                "North and South States ought by rights to exist, and it is "
                "a fault that 고려 did not compile one. From 『발해고』" "\n\n"
                "Unified 신라 and 발해 existed together for some 220 years, "
                "exchanging and competing with each other. Calling this "
                "period the North–South States period comes from a book "
                "called 『발해고』 written by 유득공, a scholar of the 조선 "
                "period. 유득공 criticised the fact that, because 고려 did not "
                "record the history of 발해 after 발해 fell, it later became "
                "impossible to assert to the other countries that had taken "
                "the territory of 발해 (여진 and 거란) that the land of 발해 was "
                "our land. Accepting this argument, Korea’s history "
                "textbooks today describe the period in which Unified 신라 "
                "and 발해 stood together as the ‘North–South States period’."),
        PARAGRAPH("부여씨(백제 {왕족} {성씨})가 {망하고|망하다} 고씨(고구려 왕족 성씨)가 망하게 되니 김씨(신라 "
                  "왕족 성씨)가 그 남쪽 땅을 차지하고, 대씨(대조영)가 그 북쪽 땅을 차지하여 발해라 하였다. "
                  "이를 남북국이라고 한다. {마땅히} 남북국의 역사가 있어야 했음에도 고려가 이를 "
                  "{편찬하지|편찬하다} 않은 것은 잘못이다. -『발해고』-"),
        PARAGRAPH("통일 신라와 발해는 서로 교류하고 경쟁하며 220여 년을 함께 존재했다. 이 시기를 남북국 "
                  "시대라고 하는 것은 조선 시대의 {학자} 유득공이 쓴 『{발해고}』라는 책에서 "
                  "{비롯된|비롯되다} 것이다. 유득공은 발해가 멸망한 후 고려가 발해의 역사를 "
                  "{기록해|기록하다} 두지 않아서 나중에 발해의 영토를 차지했던 다른 나라({여진}, {거란})에게 "
                  "발해 땅이 우리 땅임을 주장하지 못하게 되었다고 {비판하였다|비판하다}. 이러한 주장을 "
                  "받아들여 오늘날 한국의 역사 {교과서}에서는 통일 신라와 발해가 함께 있던 시기를 ‘남북국 "
                  "시대’라고 {기술하고|기술하다} 있다."),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 삼국은 어떻게 발전했을까?"),
        BULLET("삼국 중 고구려는 (        )이, (        )는 주몽의 아들로 알려진 온조가 세웠다. "
               "(        )를 세운 사람은 박혁거세이다."),
        BULLET("삼국 중 가장 먼저 전성기를 맞이한 나라는 (        )이다."),
        BULLET("고구려, 백제, 신라가 각각 가장 발전했을 때 공통적으로 차지한 지역은 (        ) 유역이다."),
        HEADING(3, "02 남북국 시대에는 어떤 나라들이 발전했을까?"),
        BULLET("신라는 중국의 (        )과 연합하여 백제와 고구려를 멸망시켰다."),
        BULLET("고구려의 장군 출신인 (        )이 고구려 유민을 모아 발해를 세웠다."),
        BULLET("남쪽의 통일 신라, 북쪽의 발해가 함께 존재했던 시기를 가리켜 (        ) 시대라고 한다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "한국의 명절 한가위의 뿌리는 신라 시대의 ‘가배’", translation=
                "The root of 한가위, the Korean festival, is the ‘가배’ of the "
                "신라 period" "\n\n"
                "추석 (the 15th day of the 8th lunar month) is a festival met "
                "just ahead of the harvest (the gathering in of crops that "
                "have fully ripened) of the grain and fruit tended with "
                "devotion from spring to summer. 추석 is also called 한가위, "
                "where ‘한’ means ‘big’ and ‘가위’ means ‘the middle’. That "
                "is, 한가위 means the great day that falls right in the "
                "middle of the 8th month." "\n\n"
                "According to 『삼국사기』, the word ‘가위’ is also one that "
                "came from ‘가배’, a weaving game (a game in which women "
                "gather and weave cloth together) of the 신라 period. King "
                "유리 of 신라 gathered the women who wove hemp cloth (cloth "
                "for clothes) in the palace a month before 한가위, divided "
                "them into two sides and had them weave. The amount of "
                "cloth woven over the month was compared, and the losing "
                "side treated the winning side to food and held a feast "
                "with singing, and this was called ‘가배’. Later ‘가배’ "
                "changed into the word ‘가위’." "\n\n"
                "* 길쌈: a term for the process by which women weave cloth "
                "such as hemp, ramie, silk and cotton at home"),
        PARAGRAPH("추석({음력} 8월 15일)은 봄부터 여름까지 {정성} 들여 {가꾼|가꾸다} {곡식}과 과일 "
                  "{수확}(다 익은 {농작물}을 {거두어 들이는|거두어들이다} 것)을 {앞두고|앞두다} 있을 때 "
                  "맞이하는 명절이다. 추석은 {한가위}라고 하는데, ‘한’은 ‘크다’, ‘가위’는 ‘가운데’라는 "
                  "뜻이다. 즉, 한가위는 8월의 {한가운데} 있는 큰 날이라는 뜻이다."),
        PARAGRAPH("『{삼국사기}』에 따르면 ‘가위’라는 말은 신라 시대 때 {길쌈놀이}(여자들이 함께 모여 "
                  "{옷감}을 {짜며|짜다} 노는 놀이)인 ‘가배’에서 나온 말이기도 하다. 신라의 유리왕이 한가위 "
                  "한 달 전에 {베}(옷감) 짜는 여자들을 {궁궐}에 모아 두 {편}으로 나누어 베를 짜게 하였다. 한 "
                  "달 동안 베를 짠 양을 비교하여 진 편이 이긴 편에게 음식을 {대접하고|대접하다} 노래를 "
                  "부르며 {잔치}를 벌였는데, 이를 ‘가배’라고 하였다. 이후 ‘가배’는 ‘가위’라는 말로 "
                  "변했다."),
        PARAGRAPH("* {길쌈}: 여자들이 가정에서 베, {모시}, {명주}, {무명} 등의 옷감을 짜는 과정을 "
                  "{일컫는|일컫다} {용어}"),
        PARAGRAPH("★ 자신의 고향 나라에 한국의 추석(한가위)과 비슷한 명절이 있는지, 있다면 어떻게 보내는지 "
                  "이야기해 봅시다. 또한 그와 같은 명절의 이름이나 풍습이 어떻게 생겨난 것인지 이야기해 "
                  "봅시다.",
                  "Talk about whether your home country has a festival like "
                  "Korea’s 추석 (한가위) and, if it has, how it is spent. Talk "
                  "too about how the name and the customs of such a festival "
                  "came about."),
    ],

    extraAnnotations={
        "건국": dict(
            hanja="建國", meaning="the founding of a country",
            characters=[("建", "건", "to build — as in 건설, 건물"),
                        ("國", "국", "a country — as in 국가, 삼국")],
        ),
        "다스리다": dict(meaning="to rule, to govern",
                       surfaces=["다스리는"]),
        "활": dict(meaning="a bow (for arrows)",
                  notes=["활을 쏘다 “to shoot a bow”. 주몽 is said to have meant "
                         "“a good archer”."]),
        "쏘다": dict(meaning="to shoot", surfaces=["쏘아"]),
        "무리": dict(meaning="a band, a group of followers"),
        "이끌다": dict(meaning="to lead", surfaces=["이끌고"]),
        "잇다": dict(
            meaning="to succeed to, to carry on",
            notes=["왕의 자리를 잇다 “to succeed to the throne”."],
            surfaces=["잇게"],
        ),
        "백성": dict(
            hanja="百姓", meaning="the people, the subjects of a king",
            characters=[("百", "백", "a hundred — as in 백화점"),
                        ("姓", "성", "a family name — as in 성씨, 성명")],
        ),
        "촌장": dict(
            hanja="村長", meaning="a village chief",
            characters=[("村", "촌", "a village — as in 농촌, 어촌"),
                        ("長", "장", "a head, long — as in 시장, 장점")],
        ),
        "우물가": dict(
            meaning="the side of a well",
            notes=["우물 a well + 가 the edge, as in 강가, 바닷가."],
        ),
        "삼다": dict(
            meaning="to make (someone) into, to take as",
            notes=["왕으로 삼다 “to make someone king”."],
            surfaces=["삼았다"],
        ),
        "성립": dict(
            hanja="成立", meaning="coming into being, establishment",
            characters=[("成", "성", "to become, to achieve — as in 성장, 구성"),
                        ("立", "립", "to stand — as in 설립, 독립")],
        ),
        "고조선": dict(
            hanja="古朝鮮", meaning="고조선, the first Korean state",
            characters=[("古", "고", "old — as in 고대, 고분"),
                        ("朝", "조", "morning, a dynasty — as in 왕조"),
                        ("鮮", "선", "fresh, bright — as in 신선")],
            notes=["古 was added later to tell it from the 조선 of 1392."],
        ),
        "한반도": dict(
            hanja="韓半島", meaning="the Korean peninsula",
            characters=[("韓", "한", "Korea — as in 한국, 대한민국"),
                        ("半", "반", "half — as in 절반, 반년"),
                        ("島", "도", "an island — as in 제주도, 독도")],
        ),
        "압록강": dict(
            hanja="鴨綠江", meaning="the 압록강 (Amnok, or Yalu) river",
            characters=[("鴨", "압", "a duck"),
                        ("綠", "록", "green — as in 녹색, 녹차"),
                        ("江", "강", "a river — as in 한강")],
        ),
        "유역": dict(
            hanja="流域", meaning="a river basin",
            characters=[("流", "류", "to flow — as in 교류, 유행"),
                        ("域", "역", "a region — as in 지역, 영역")],
        ),
        "알려지다": dict(meaning="to be known (as)", surfaces=["알려진"]),
        "한편": dict(
            hanja="한便", meaning="meanwhile, on the other hand",
            characters=[("便", "편", "a side — as in 상대편, 맞은편")],
        ),
        "영토": dict(
            hanja="領土", meaning="territory",
            characters=[("領", "령", "to govern, to hold — as in 대통령, 점령"),
                        ("土", "토", "land, soil — as in 국토, 토지")],
        ),
        "차지하다": dict(meaning="to take, to occupy, to hold",
                       surfaces=["차지하기"]),
        "경쟁하다": dict(
            hanja="競爭하다", meaning="to compete",
            characters=[("競", "경", "to vie — as in 경기, 경매"),
                        ("爭", "쟁", "to contend — as in 전쟁, 분쟁")],
            surfaces=["경쟁하고"],
        ),
        "교류하다": dict(
            hanja="交流하다", meaning="to exchange, to have dealings with",
            characters=[("交", "교", "to cross, to mix — as in 외교, 교통"),
                        ("流", "류", "to flow — as in 유역, 유행")],
            surfaces=["교류하며"],
        ),
        "시기": dict(
            hanja="時期", meaning="a period, a time",
            characters=[("時", "시", "time — as in 시대, 시간"),
                        ("期", "기", "a period — as in 전성기, 기간")],
        ),
        "삼국 시대": dict(
            hanja="三國時代", meaning="the Three Kingdoms period",
            characters=[("三國", None, "the three countries — 三 three, 國 a "
                                      "country"),
                        ("時代", None, "an age — 時 time, 代 a generation")],
            notes=["고구려, 백제 and 신라."],
        ),
        "전성기": dict(
            hanja="全盛期", meaning="a heyday, a golden age",
            characters=[("全", "전", "whole — as in 전체, 안전"),
                        ("盛", "성", "flourishing — as in 번성, 성대"),
                        ("期", "기", "a period — as in 시기, 기간")],
        ),
        "맞이하다": dict(meaning="to meet, to greet, to come to",
                       surfaces=["맞이한"]),
        "남해안": dict(
            hanja="南海岸", meaning="the south coast",
            characters=[("南", "남", "south — as in 남쪽, 남북"),
                        ("海", "해", "the sea — as in 해전, 동해"),
                        ("岸", "안", "a shore — as in 해안, 연안")],
        ),
        "넓히다": dict(meaning="to widen, to extend",
                      surfaces=["넓혔고"]),
        "활발하다": dict(
            hanja="活潑하다", meaning="to be lively, active",
            characters=[("活", "활", "to live — as in 생활, 활동"),
                        ("潑", "발", "to splash, lively")],
            surfaces=["활발하게"],
        ),
        "무역": dict(
            hanja="貿易", meaning="trade",
            characters=[("貿", "무", "to trade"),
                        ("易", "역", "to exchange — as in 교역")],
        ),
        "화려하다": dict(
            hanja="華麗하다", meaning="to be splendid, gorgeous",
            characters=[("華", "화", "brilliant — as in 호화, 중화"),
                        ("麗", "려", "beautiful — as in 고려, 수려")],
            surfaces=["화려하고"],
        ),
        "섬세하다": dict(
            hanja="纖細하다", meaning="to be delicate, fine",
            characters=[("纖", "섬", "fine, a fibre — as in 섬유"),
                        ("細", "세", "thin, detailed — as in 세부, 상세")],
            surfaces=["섬세한"],
        ),
        "왜": dict(
            hanja="倭", meaning="왜, the old name for Japan and the Japanese",
            characters=[("倭", "왜", "the old Chinese and Korean name for "
                                    "Japan")],
            notes=["Not the 왜 that asks “why”."],
        ),
        "충주 고구려비": dict(
            hanja="忠州高句麗碑", meaning="the 고구려 stele at 충주",
            characters=[("忠州", None, "충주, a city in 충청북도"),
                        ("高句麗", None, "고구려"),
                        ("碑", "비", "a stone monument — as in 비석, 기념비")],
        ),
        "만주": dict(
            hanja="滿洲", meaning="Manchuria",
            characters=[("滿", "만", "full — as in 만족, 불만"),
                        ("洲", "주", "a continent, a shoal — as in 아시아주")],
        ),
        "포함하다": dict(
            hanja="包含하다", meaning="to include",
            characters=[("包", "포", "to wrap — as in 포장, 소포"),
                        ("含", "함", "to contain — as in 함량")],
            surfaces=["포함한"],
        ),
        "중부": dict(
            hanja="中部", meaning="the central part",
            characters=[("中", "중", "the middle — as in 중심, 중국"),
                        ("部", "부", "a part — as in 북부, 일부")],
        ),
        "맞서다": dict(meaning="to stand against, to confront",
                      surfaces=["맞서기"]),
        "동맹": dict(
            hanja="同盟", meaning="an alliance",
            characters=[("同", "동", "same, together — as in 공동, 동시"),
                        ("盟", "맹", "an oath — as in 연맹, 맹세")],
            notes=["동맹을 맺다 “to form an alliance”."],
        ),
        "맺다": dict(meaning="to form, to tie (an alliance, a relation)",
                    surfaces=["맺기도"]),
        "침입하다": dict(
            hanja="侵入하다", meaning="to invade, to break into",
            characters=[("侵", "침", "to encroach — as in 침해, 침략"),
                        ("入", "입", "to enter — as in 입국, 수입")],
            surfaces=["침입했을"],
        ),
        "물리치다": dict(meaning="to drive back, to repel",
                       surfaces=["물리치기도"]),
        "귀족": dict(
            hanja="貴族", meaning="the nobility, a noble",
            characters=[("貴", "귀", "precious, high — as in 귀중, 귀하"),
                        ("族", "족", "a clan — as in 가족, 민족, 왕족")],
        ),
        "평민": dict(
            hanja="平民", meaning="a commoner",
            characters=[("平", "평", "level, ordinary — as in 평야, 평등"),
                        ("民", "민", "the people — as in 국민, 유민")],
        ),
        "청년": dict(
            hanja="靑年", meaning="a young person, youth",
            characters=[("靑", "청", "blue, green — as in 청소년"),
                        ("年", "년", "a year — as in 소년, 작년")],
        ),
        "구성되다": dict(
            hanja="構成되다", meaning="to be made up of",
            characters=[("構", "구", "to frame — as in 구조, 기구"),
                        ("成", "성", "to become — as in 성립, 성장")],
            surfaces=["구성된"],
        ),
        "화랑도": dict(
            hanja="花郞徒", meaning="화랑도, the 신라 youth corps",
            characters=[("花", "화", "a flower — as in 화분, 무궁화"),
                        ("郞", "랑", "a young man — as in 신랑"),
                        ("徒", "도", "a band, followers — as in 신도, 학도")],
        ),
        "조직": dict(
            hanja="組織", meaning="an organisation",
            characters=[("組", "조", "to put together — as in 조합, 조립"),
                        ("織", "직", "to weave — as in 직물")],
        ),
        "바탕": dict(
            meaning="a basis, a foundation",
            notes=["…을 바탕으로 “on the basis of …”."],
        ),
        "키우다": dict(meaning="to build up, to raise",
                      surfaces=["키웠다"]),
        "통일": dict(
            hanja="統一", meaning="unification",
            characters=[("統", "통", "to govern, to gather — as in 대통령, 전통"),
                        ("一", "일", "one — as in 일부, 동일")],
        ),
        "기반": dict(
            hanja="基盤", meaning="a foundation, a footing",
            characters=[("基", "기", "a base — as in 기본, 기초"),
                        ("盤", "반", "a slab, a tray — as in 지반")],
        ),
        "마련하다": dict(meaning="to lay, to prepare, to put in place",
                       surfaces=["마련하였다"]),
        "위치하다": dict(
            hanja="位置하다", meaning="to be situated",
            characters=[("位", "위", "a position — as in 지위, 순위"),
                        ("置", "치", "to place — as in 설치, 배치")],
            surfaces=["위치해"],
        ),
        "평야": dict(
            hanja="平野", meaning="a plain",
            characters=[("平", "평", "level — as in 평민, 평등"),
                        ("野", "야", "a field — as in 야외, 분야")],
        ),
        "농사짓다": dict(
            hanja="農事짓다", meaning="to farm",
            characters=[("農", "농", "farming — as in 농촌, 농작물"),
                        ("事", "사", "work, a matter — as in 행사, 사건")],
            surfaces=["농사짓기"],
        ),
        "실어 나르다": dict(
            meaning="to carry (goods) by loading them",
            notes=["싣다 to load + 나르다 to carry."],
            surfaces=["실어 나를"],
        ),
        "유리하다": dict(
            hanja="有利하다", meaning="to be advantageous, favourable",
            characters=[("有", "유", "to have — as in 유효, 소유"),
                        ("利", "리", "benefit — as in 이익, 편리")],
            surfaces=["유리한"],
        ),
        "장점": dict(
            hanja="長點", meaning="an advantage, a strong point",
            characters=[("長", "장", "long, strong — as in 성장, 촌장"),
                        ("點", "점", "a point — as in 단점, 관점")],
        ),
        "여겨지다": dict(meaning="to be regarded as",
                       surfaces=["여겨졌다"]),
        "수도": dict(
            hanja="首都", meaning="a capital city",
            characters=[("首", "수", "the head — as in 수석, 수상"),
                        ("都", "도", "a city — as in 도시, 도심")],
        ),
        "자리잡다": dict(
            meaning="to be settled, to sit (in a place)",
            notes=["The page prints it as one word here, and 자리 잡은 as two "
                   "on p. 204."],
            surfaces=["자리잡고"],
        ),
        "꾸준히": dict(meaning="steadily"),
        "인재": dict(
            hanja="人材", meaning="a person of ability, talent",
            characters=[("人", "인", "a person — as in 군인, 개인"),
                        ("材", "재", "timber, material — as in 재료, 교재")],
        ),
        "기르다": dict(meaning="to raise, to cultivate",
                      surfaces=["기르고"]),
        "외교": dict(
            hanja="外交", meaning="diplomacy",
            characters=[("外", "외", "outside — as in 외국, 해외"),
                        ("交", "교", "to mix, to deal with — as in 교류, 교통")],
        ),
        "성장하다": dict(
            hanja="成長하다", meaning="to grow",
            characters=[("成", "성", "to become — as in 성립, 구성"),
                        ("長", "장", "to grow, long — as in 장점, 촌장")],
            surfaces=["성장하였다"],
        ),
        "당나라": dict(
            hanja="唐나라", meaning="the 당 (Tang) dynasty of China",
            characters=[("唐", "당", "Tang, the Chinese dynasty of 618-907")],
            notes=["The article shortens it to 당 after the first mention."],
        ),
        "합치다": dict(
            hanja="合치다", meaning="to join, to put together",
            characters=[("合", "합", "to join — as in 연합, 합의")],
            notes=["힘을 합치다 “to join forces”."],
            surfaces=["합쳐"],
        ),
        "차례로": dict(
            hanja="次例로", meaning="in turn, one after the other",
            characters=[("次", "차", "next, an order — as in 차남, 목차"),
                        ("例", "례", "an example, a rule — as in 예외, 사례")],
        ),
        "멸망시키다": dict(
            hanja="滅亡시키다", meaning="to bring down, to destroy (a state)",
            characters=[("滅", "멸", "to perish — as in 소멸, 멸종"),
                        ("亡", "망", "to perish, to be lost — as in 사망, 망하다")],
            surfaces=["멸망시켰다"],
        ),
        "연합": dict(
            hanja="聯合", meaning="an alliance, a union",
            characters=[("聯", "련", "to link — as in 연맹, 관련"),
                        ("合", "합", "to join — as in 합치다, 합의")],
        ),
        "지배하다": dict(
            hanja="支配하다", meaning="to rule, to dominate",
            characters=[("支", "지", "to support, a branch — as in 지원, 지점"),
                        ("配", "배", "to distribute — as in 배치, 분배")],
            surfaces=["지배하려고"],
        ),
        "벌이다": dict(
            meaning="to wage (a war), to hold (a feast)",
            notes=["전쟁을 벌이다 here, 잔치를 벌이다 on p. 207."],
            surfaces=["벌였다"],
        ),
        "전투": dict(
            hanja="戰鬪", meaning="a battle",
            characters=[("戰", "전", "war — as in 전쟁, 해전"),
                        ("鬪", "투", "to fight — as in 투쟁")],
        ),
        "해전": dict(
            hanja="海戰", meaning="a sea battle",
            characters=[("海", "해", "the sea — as in 남해안, 동해"),
                        ("戰", "전", "war — as in 전투, 전쟁")],
        ),
        "잇달아": dict(meaning="one after another, in succession"),
        "승리하다": dict(
            hanja="勝利하다", meaning="to win, to be victorious",
            characters=[("勝", "승", "to win — as in 우승, 승부"),
                        ("利", "리", "benefit, gain — as in 유리하다, 이익")],
            surfaces=["승리하였고"],
        ),
        "마침내": dict(meaning="at last, finally"),
        "몰아내다": dict(meaning="to drive out", surfaces=["몰아내고"]),
        "한마음": dict(meaning="one mind, one heart"),
        "정책": dict(
            hanja="政策", meaning="a policy",
            characters=[("政", "정", "government — as in 정치, 행정"),
                        ("策", "책", "a plan — as in 대책, 방책")],
        ),
        "실시하다": dict(
            hanja="實施하다", meaning="to carry out, to put into effect",
            characters=[("實", "실", "real — as in 사실, 실제"),
                        ("施", "시", "to carry out — as in 시행, 시설")],
            surfaces=["실시하였다"],
        ),
        "관직": dict(
            hanja="官職", meaning="a government post",
            characters=[("官", "관", "an official — as in 장관, 경찰관"),
                        ("職", "직", "a post, a job — as in 직업, 직장")],
        ),
        "군인": dict(
            hanja="軍人", meaning="a soldier",
            characters=[("軍", "군", "an army — as in 장군, 신라군"),
                        ("人", "인", "a person — as in 인재, 개인")],
        ),
        "뽑다": dict(meaning="to choose, to pick", surfaces=["뽑았다"]),
        "한때": dict(meaning="once, at one time"),
        "화해하다": dict(
            hanja="和解하다", meaning="to make peace, to be reconciled",
            characters=[("和", "화", "harmony — as in 평화, 조화"),
                        ("解", "해", "to undo, to resolve — as in 해결, 이해")],
            surfaces=["화해하고"],
        ),
        "석굴암": dict(
            hanja="石窟庵", meaning="석굴암, the stone grotto temple at 경주",
            characters=[("石", "석", "stone — as in 석등, 비석"),
                        ("窟", "굴", "a cave — as in 동굴"),
                        ("庵", "암", "a hermitage")],
        ),
        "불국사": dict(
            hanja="佛國寺", meaning="불국사, the temple at 경주",
            characters=[("佛", "불", "Buddha — as in 불교, 불상"),
                        ("國", "국", "a country — as in 건국, 국가"),
                        ("寺", "사", "a temple — as in 사찰")],
        ),
        "불교": dict(
            hanja="佛敎", meaning="Buddhism",
            characters=[("佛", "불", "Buddha — as in 불상, 불국사"),
                        ("敎", "교", "a teaching, a religion — as in 종교, 교과서")],
        ),
        "발달하다": dict(
            hanja="發達하다", meaning="to develop, to advance",
            characters=[("發", "발", "to send out — as in 발전, 발생"),
                        ("達", "달", "to reach — as in 전달, 도달")],
            surfaces=["발달하였고"],
        ),
        "동양": dict(
            hanja="東洋", meaning="the East, Asia",
            characters=[("東", "동", "east — as in 동해, 동쪽"),
                        ("洋", "양", "an ocean — as in 서양, 해양")],
        ),
        "천문대": dict(
            hanja="天文臺", meaning="an astronomical observatory",
            characters=[("天", "천", "heaven, the sky — as in 천국, 천연"),
                        ("文", "문", "a pattern, writing — as in 문화, 문자"),
                        ("臺", "대", "a platform — as in 무대, 첨성대")],
        ),
        "첨성대": dict(
            hanja="瞻星臺", meaning="첨성대, the 신라 observatory at 경주",
            characters=[("瞻", "첨", "to look up at"),
                        ("星", "성", "a star — as in 위성, 행성"),
                        ("臺", "대", "a platform — as in 천문대, 무대")],
        ),
        "되찾다": dict(meaning="to win back, to recover",
                      surfaces=["되찾기"]),
        "장군": dict(
            hanja="將軍", meaning="a general",
            characters=[("將", "장", "a commander — as in 장교, 주장"),
                        ("軍", "군", "an army — as in 군인, 군대")],
        ),
        "출신": dict(
            hanja="出身", meaning="origin, background (where one is from)",
            characters=[("出", "출", "to come out — as in 출입국, 수출"),
                        ("身", "신", "the body — as in 신분, 자신")],
            notes=["장군 출신 “a former general, one who had been a general”."],
        ),
        "유민": dict(
            hanja="遺民", meaning="the people left by a fallen country",
            characters=[("遺", "유", "to leave behind — as in 유적, 유산"),
                        ("民", "민", "the people — as in 평민, 국민")],
        ),
        "북부": dict(
            hanja="北部", meaning="the northern part",
            characters=[("北", "북", "north — as in 북쪽, 남북"),
                        ("部", "부", "a part — as in 중부, 일부")],
        ),
        "받아들이다": dict(meaning="to take in, to accept",
                        surfaces=["받아들이며"]),
        "불상": dict(
            hanja="佛像", meaning="a statue of the Buddha",
            characters=[("佛", "불", "Buddha — as in 불교, 불국사"),
                        ("像", "상", "an image, a statue — as in 동상, 영상")],
        ),
        "석등": dict(
            hanja="石燈", meaning="a stone lantern",
            characters=[("石", "석", "stone — as in 석굴암, 비석"),
                        ("燈", "등", "a lamp — as in 전등, 신호등")],
        ),
        "연꽃무늬": dict(
            hanja="蓮꽃무늬", meaning="a lotus pattern",
            characters=[("蓮", "련", "the lotus")],
            notes=["연꽃 a lotus flower + 무늬 a pattern."],
        ),
        "기와": dict(meaning="a roof tile"),
        "짐작하다": dict(
            hanja="斟酌하다", meaning="to gather, to guess, to infer",
            characters=[("斟", "짐", "to pour, to weigh up"),
                        ("酌", "작", "to pour (a drink), to consider — as in "
                                    "참작")],
            surfaces=["짐작할"],
        ),
        "존재하다": dict(
            hanja="存在하다", meaning="to exist",
            characters=[("存", "존", "to exist, to keep — as in 보존, 생존"),
                        ("在", "재", "to be at — as in 현재, 재외")],
            surfaces=["존재한"],
        ),
        "남북국 시대": dict(
            hanja="南北國時代", meaning="the North–South States period",
            characters=[("南北", None, "south and north — 南 south, 北 north"),
                        ("國", "국", "a country — as in 삼국, 건국"),
                        ("時代", None, "an age — 時 time, 代 a generation")],
            notes=["통일 신라 in the south and 발해 in the north."],
        ),
        "왕족": dict(
            hanja="王族", meaning="a royal family, royalty",
            characters=[("王", "왕", "a king — as in 왕자, 국왕"),
                        ("族", "족", "a clan — as in 귀족, 가족")],
        ),
        "성씨": dict(
            hanja="姓氏", meaning="a family name",
            characters=[("姓", "성", "a family name — as in 백성, 성명"),
                        ("氏", "씨", "a clan — as in 김씨, 씨족")],
        ),
        "망하다": dict(
            hanja="亡하다", meaning="to fall, to be ruined",
            characters=[("亡", "망", "to perish — as in 멸망, 사망")],
            surfaces=["망하고"],
        ),
        "마땅히": dict(meaning="by rights, as it ought to be"),
        "편찬하다": dict(
            hanja="編纂하다", meaning="to compile (a book, a history)",
            characters=[("編", "편", "to compile, to weave — as in 편집, 개편"),
                        ("纂", "찬", "to collect and edit")],
            surfaces=["편찬하지"],
        ),
        "학자": dict(
            hanja="學者", meaning="a scholar",
            characters=[("學", "학", "learning — as in 학교, 과학"),
                        ("者", "자", "a person — as in 기자, 노동자")],
        ),
        "발해고": dict(
            hanja="渤海考", meaning="『발해고』, 유득공’s study of 발해 (1784)",
            characters=[("渤海", None, "발해"),
                        ("考", "고", "to examine — as in 참고, 고려")],
        ),
        "비롯되다": dict(meaning="to come from, to originate in",
                       surfaces=["비롯된"]),
        "기록하다": dict(
            hanja="記錄하다", meaning="to record",
            characters=[("記", "기", "to write down — as in 기술, 일기"),
                        ("錄", "록", "to record — as in 등록, 녹음")],
            surfaces=["기록해"],
        ),
        "여진": dict(
            hanja="女眞", meaning="the Jurchen",
            characters=[("女眞", None, "a people of Manchuria — the two "
                                      "characters write the name by sound")],
        ),
        "거란": dict(
            hanja="契丹", meaning="the Khitan",
            characters=[("契丹", None, "a people of the northern steppe — the "
                                      "two characters write the name by "
                                      "sound")],
            notes=["Written 契丹 but read 거란."],
        ),
        "비판하다": dict(
            hanja="批判하다", meaning="to criticise",
            characters=[("批", "비", "to comment on — as in 비평"),
                        ("判", "판", "to judge — as in 판단, 재판")],
            surfaces=["비판하였다"],
        ),
        "교과서": dict(
            hanja="敎科書", meaning="a textbook",
            characters=[("敎", "교", "to teach — as in 교육, 불교"),
                        ("科", "과", "a subject — as in 과목, 과학"),
                        ("書", "서", "a book, writing — as in 서류, 도서")],
        ),
        "기술하다": dict(
            hanja="記述하다", meaning="to describe, to set down in writing",
            characters=[("記", "기", "to write down — as in 기록, 일기"),
                        ("述", "술", "to state — as in 서술, 진술")],
            notes=["Not 기술 (技術), technology."],
            surfaces=["기술하고"],
        ),
        "음력": dict(
            hanja="陰曆", meaning="the lunar calendar",
            characters=[("陰", "음", "shade, the moon — as in 음지"),
                        ("曆", "력", "a calendar — as in 양력, 달력")],
            notes=["Chapter 16 has its margin definition."],
        ),
        "정성": dict(
            hanja="精誠", meaning="devotion, great care",
            characters=[("精", "정", "fine, the spirit — as in 정신, 정밀"),
                        ("誠", "성", "sincerity — as in 성실")],
            notes=["정성(을) 들이다 “to put one’s heart into”."],
        ),
        "가꾸다": dict(meaning="to tend, to grow (crops, a garden)",
                      surfaces=["가꾼"]),
        "곡식": dict(
            hanja="穀食", meaning="grain, cereals",
            characters=[("穀", "곡", "grain — as in 곡물, 잡곡"),
                        ("食", "식", "food, to eat — as in 음식, 식사")],
        ),
        "수확": dict(
            hanja="收穫", meaning="a harvest",
            characters=[("收", "수", "to gather in — as in 수입, 회수"),
                        ("穫", "확", "to reap")],
        ),
        "농작물": dict(
            hanja="農作物", meaning="crops",
            characters=[("農", "농", "farming — as in 농사, 농촌"),
                        ("作", "작", "to make — as in 제작, 작품"),
                        ("物", "물", "a thing — as in 물건, 식물")],
        ),
        "거두어들이다": dict(
            meaning="to gather in, to harvest",
            notes=["The page prints it with a space, 거두어 들이는."],
            surfaces=["거두어 들이는"],
        ),
        "앞두다": dict(meaning="to have (something) just ahead",
                      surfaces=["앞두고"]),
        "한가위": dict(
            meaning="한가위, another name for 추석",
            notes=["한 big + 가위 the middle, as the page explains."],
        ),
        "한가운데": dict(meaning="the very middle"),
        "삼국사기": dict(
            hanja="三國史記",
            meaning="『삼국사기』, the History of the Three Kingdoms (1145)",
            characters=[("三國", None, "the Three Kingdoms"),
                        ("史", "사", "history — as in 역사"),
                        ("記", "기", "a record — as in 기록, 기술")],
        ),
        "길쌈놀이": dict(
            meaning="a weaving game, a weaving contest",
            notes=["길쌈 weaving + 놀이 a game."],
        ),
        "길쌈": dict(meaning="weaving cloth at home"),
        "옷감": dict(
            meaning="cloth for clothes",
            notes=["옷 clothes + 감 material, as in 장난감, 신랑감."],
        ),
        "짜다": dict(meaning="to weave", surfaces=["짜며"]),
        "베": dict(meaning="hemp cloth"),
        "궁궐": dict(
            hanja="宮闕", meaning="a royal palace",
            characters=[("宮", "궁", "a palace — as in 경복궁"),
                        ("闕", "궐", "a palace gate, the court")],
        ),
        "편": dict(
            hanja="便", meaning="a side, a team",
            characters=[("便", "편", "a side — as in 한편, 상대편")],
            notes=["진 편 the losing side, 이긴 편 the winning side."],
        ),
        "대접하다": dict(
            hanja="待接하다", meaning="to treat (someone to food), to serve",
            characters=[("待", "대", "to wait on, to treat — as in 기대, 초대"),
                        ("接", "접", "to receive — as in 접수, 접대")],
            surfaces=["대접하고"],
        ),
        "잔치": dict(meaning="a feast, a party"),
        "모시": dict(meaning="ramie cloth"),
        "명주": dict(
            hanja="明紬", meaning="silk cloth",
            characters=[("明", "명", "bright — as in 설명, 분명"),
                        ("紬", "주", "silk cloth")],
        ),
        "무명": dict(meaning="cotton cloth"),
        "일컫다": dict(meaning="to call, to refer to",
                      surfaces=["일컫는"]),
        "용어": dict(
            hanja="用語", meaning="a term",
            characters=[("用", "용", "to use — as in 사용, 이용"),
                        ("語", "어", "a word, language — as in 언어, 단어")],
        ),
    },

    extraNotes=[
        "The three maps on p. 205 are set as their printed captions; the "
        "maps themselves, the photograph of the 충주 고구려비 and the small map "
        "of sites in the 한강 basin are not reproduced. The small print on "
        "the 한강 map is too fine to read in the photographs and is not "
        "transcribed.",
        "The 충주 고구려비 note on p. 205 and the roof-tile note on p. 206 sit "
        "in the margin with the glossary and are set as glossary rows, with "
        "a figure line for each photograph.",
        "The map of 통일 신라 and 발해 and the two roof tiles on p. 206 are "
        "not reproduced; their captions are.",
        "The title of 이야기 나누기 on p. 207 is printed in square brackets, "
        "which are left off here.",
        "The review gaps on p. 207 are blank in the book and left blank here.",
    ],
)
