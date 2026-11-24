# -*- coding: utf-8 -*-
"""Chapter 40 — The Goryeo period.

Transcribed from the photos of pp. 208-211. The pages carry no handwriting.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, FIGURE, LABELS, TABLE,
               CELL, GLOSSARY)

CHAPTER = dict(
    number=40, slug="40-goryeo",
    unit="역사", title="고려 시대", titleEn="The Goryeo period",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 18세기 프랑스의 지도 {제작자} 장 당빌(Jean D’Anville)이 만든 동아시아 "
                  "지도입니다.",
                  "Below is a map of East Asia made by Jean D’Anville, a "
                  "French mapmaker of the eighteenth century."),
        FIGURE("장 당빌의 동아시아 지도 — 한반도 동쪽 바다에 적힌 ‘COREE’에 빨간색 동그라미가 그려져 있음"),
        HEADING(4, "01 왼쪽 지도의 빨간색 동그라미 부분이 한국을 {가리키는|가리키다} 이름입니다. "
                   "COREE를 어떻게 읽을 수 있습니까?",
                translation="The part ringed in red on the map on the left "
                            "is the name that refers to Korea. How can COREE "
                            "be read?"),
        HEADING(4, "02 한국은 언제부터 COREA(또는 KOREA)라고 {불렸을까요|불리다}?",
                translation="Since when has Korea been called COREA (or "
                            "KOREA)?"),

        SECTION("goals", "학습목표"),
        BULLET("고려의 {성립}과 발전 {과정}을 설명할 수 있다.", ordered=True,
               translation="Explain how 고려 was founded and how it "
                           "developed."),
        BULLET("고려의 사회와 문화에 대해 설명할 수 있다.", ordered=True,
               translation="Explain the society and culture of 고려."),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"],
              [["기본", "역사", "43. 한국의 역사 인물", "서희"]]),

        SECTION("part", "01 고려는 어떻게 발전했을까?"),
        HEADING(2, "고려의 건국과 후삼국 통일", translation=
                "The founding of 고려 and the unification of the Later Three "
                "Kingdoms" "\n\n"
                "At the end of 신라 society was in turmoil and the king’s "
                "power was weak, while in the provinces the power of those "
                "strong in wealth or arms (the 호족) grew. Of the 호족, 견훤, "
                "who was especially powerful, founded 후백제 (900), and 궁예 "
                "founded 후고구려 (901). With this the country was again "
                "divided into three, and this is called the Later Three "
                "Kingdoms period." "\n\n"
                "Meanwhile 왕건, who had been a subject of 궁예, drove 궁예 "
                "out together with other subjects and changed the name of "
                "the country to 고려 (918). This carries the meaning of "
                "succeeding 고구려. After that 고려 fought a fierce war with "
                "후백제, and in the end, after receiving the surrender of 신라 "
                "(935), attacked 후백제 and unified the Later Three Kingdoms "
                "(936)."),
        GLOSSARY(("신하", "왕을 섬기며 벼슬(나랏일)하는 사람", "신하",
                  dict(en="a person who serves the king and holds office (does the work of the state)")),
                 ("계승", "이어 받음", "계승",
                  dict(en="taking over and carrying on"))),
        PARAGRAPH("신라 {말기}에는 사회가 {혼란스러웠고|혼란스럽다} 왕의 힘이 약했던 {반면} 지방에서 "
                  "{경제력}이나 {군사력}이 강한 {세력}({호족})의 힘이 커졌다. 호족 중에서 특히 힘이 "
                  "강했던 견훤은 {후백제}(900년)를, 궁예는 {후고구려}를 세웠다(901년). 이로써 나라가 "
                  "다시 세 개로 나누어졌는데 이를 {후삼국 시대}라고 한다."),
        PARAGRAPH("한편, 궁예의 {신하}였던 왕건은 다른 신하들과 함께 궁예를 {몰아내고|몰아내다} 나라 "
                  "이름을 고려로 바꾸었다(918년). 이것은 고구려를 {계승}한다는 의미를 {띤다|띠다}. 이후 "
                  "고려는 후백제와 {치열한|치열하다} 전쟁을 {벌였는데|벌이다}, 결국 신라의 {항복}을 받은 "
                  "뒤(935년) 후백제를 {공격하여|공격하다} 후삼국을 {통일하였다|통일하다}(936년)."),
        FIGURE("후삼국 시대 — 한반도 지도에 고려, 후백제, 신라의 영역이 색으로 나뉘어 있음(황해, 동해)"),

        HEADING(2, "고려의 발전과 변화", translation=
                "The development of 고려 and its changes" "\n\n"
                "태조 왕건 of 고려 fixed the rate of tax at 10% and allowed no "
                "more than that to be collected, so as to steady the lives "
                "of the people. He also encouraged Buddhism, seeking to "
                "bring together the hearts of a people worn out by the wars "
                "until then." "\n\n"
                "고려, at first an aristocratic society centred on the civil "
                "officials, saw its ruling class change for a time to the "
                "military officials after their revolt (the 무신 정변). The "
                "military officials took more land and more slaves by "
                "unlawful means and collected heavy taxes from the people. "
                "So there were also revolts of farmers resisting this." "\n\n"
                "고려 widened its territory through several wars with the "
                "countries to the north of the Korean peninsula. In the "
                "thirteenth century it was invaded by the Mongols and fought "
                "a war lasting some forty years, going so far as to move the "
                "capital from 개경 (개성) to 강화도. At the end of 고려 the 왜구, "
                "Japanese pirates, and the 홍건적, bands of Chinese robbers, "
                "invaded 고려. In the course of driving them off, a new "
                "military force grew up, 이성계 among them. 이성계 joined "
                "forces with those who wanted to change the society of the "
                "day, which was in turmoil, brought 고려 down and founded 조선 "
                "(1392)."),
        GLOSSARY(("태조", "왕조의 첫 번째 왕", "태조",
                  dict(en="the first king of a dynasty")),
                 ("권장", "무언가를 권하여 하도록 함.", "권장",
                  dict(en="urging someone to do something")),
                 ("문신", "나랏일을 하는 신하 중 군인이 아닌 사람", "문신",
                  dict(en="among the subjects who do the work of the state, one who is not a soldier")),
                 ("무신", "군인으로서 나랏일을 하는 신하", "무신",
                  dict(en="a subject who does the work of the state as a soldier"))),
        PARAGRAPH("고려 {태조} 왕건은 {백성}의 생활을 {안정시키기|안정시키다} 위해 세금의 {비율}을 "
                  "10%로 정해 놓고 그 이상 {거두지|거두다} 못하도록 했다. 또한 {불교}를 {권장}하여 "
                  "그동안 전쟁으로 {지쳐|지치다} 있던 백성의 마음을 모으고자 하였다."),
        PARAGRAPH("원래 {문신} 중심의 {귀족} 사회였던 고려는 {무신}들의 {반란}({무신 정변}) 이후 한동안 "
                  "{지배층}이 무신으로 바뀌었다. 무신들은 {불법적}인 방법으로 땅과 {노비}를 더 많이 "
                  "{차지하였고|차지하다} 백성에게서 많은 세금을 거두었다. 그래서 이에 "
                  "{저항하는|저항하다} {농민}들의 반란이 일어나기도 했다."),
        PARAGRAPH("고려는 한반도 북쪽에 있는 나라들과 여러 차례 전쟁을 {치르면서|치르다} {영토}를 "
                  "{넓혔다|넓히다}. 13세기에는 몽골의 {침략}을 받아 {수도}를 개경(개성)에서 강화도로 옮겨 "
                  "가면서까지 약 40년에 {걸친|걸치다} 전쟁을 벌였다. 고려 말기에는 일본 {해적}인 "
                  "{왜구}와 중국 {도적떼}인 {홍건적}이 고려를 침략하였다. 이들을 {물리치는|물리치다} "
                  "과정에서 이성계 등 새로운 군인 세력이 {성장하였다|성장하다}. 이성계는 {당시} 혼란스럽던 "
                  "사회를 바꾸기를 원했던 사람들과 힘을 합쳐 고려를 {멸망시키고|멸망시키다} 조선을 "
                  "세웠다(1392년)."),
        FIGURE("고려궁터 — 강화도로 도읍을 옮긴 후 1234년에 세운 궁궐과 관아가 있던 곳이다. 지금 남아 "
               "있는 건물은 조선 후기에 복원한 것이다."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "왕건 청동상이 가진 비밀", translation=
                "The secret of the bronze statue of 왕건" "\n\n"
                "In 1992 a bronze statue was found near the tomb of 왕건 "
                "(현릉) in 개성, North Korea. When historians examined it, the "
                "statue, seated and wearing the crown (headgear) that "
                "emperors used, proved to represent 왕건, who founded 고려. "
                "The people of the 고려 period revered 왕건, the founder of "
                "the country, like a god. So they made a statue of him in "
                "bronze and used it at the important ceremonies of the "
                "state." "\n\n"
                "But why is the bronze statue of 왕건 naked? Originally the "
                "statue was thinly coated in gold and dressed over that in "
                "silk clothes. But once 고려 had fallen and the 조선 period "
                "came, it was thought that holding rites to a statue of 왕건 "
                "did not accord with Confucian propriety, and the statue "
                "was buried in the ground. Over the hundreds of years that "
                "followed, the gold peeled off and the clothes rotted away."),
        PARAGRAPH("1992년 북한의 개성에 있는 왕건의 {묘}({현릉}) 근처에서 {청동상}이 "
                  "{발견되었다|발견되다}. {역사학자}들이 조사해 보니 {황제}들이 사용한 {관}(모자)을 쓰고 "
                  "앉아 있는 이 청동상은 고려를 세운 왕건을 나타낸 것이었다. 고려 시대 사람들은 나라를 세운 "
                  "왕건을 신처럼 {모셨다|모시다}. 그래서 청동으로 {동상}을 만들어 국가의 중요한 행사 때 "
                  "사용하였다."),
        PARAGRAPH("그런데, 왕건의 청동상은 왜 {벌거벗은|벌거벗다} 모습을 하고 있을까? 원래는 청동상에 "
                  "얇게 금을 {입히고|입히다}, 그 위에 {비단} 옷을 입혀 놓았다. 그러나 고려가 멸망하고 "
                  "나서 조선 시대가 되자 왕건의 동상에게 {제사}를 지내는 것이 {유교}의 {예절}에 맞지 "
                  "않는다고 생각하여 청동상을 땅속에 {묻어|묻다} 두었다. 이후 수백 년의 시간이 지나면서 "
                  "금이 {벗겨지고|벗겨지다} 옷도 {썩어버린|썩다} 것이다."),
        FIGURE("왕건의 청동상"),

        SECTION("part", "02 고려 시대 사람들은 어떻게 살았을까?"),
        HEADING(2, "고려와 다른 나라의 관계", translation=
                "고려 and its relations with other countries" "\n\n"
                "고려 brought together the varied cultures of the old 고구려, "
                "백제 and 신라, and at the same time developed its culture "
                "through lively exchange with many countries of the world. "
                "In this respect the culture of 고려 can be said to be marked "
                "by openness and diversity." "\n\n"
                "벽란도 in 고려 became widely known as an international "
                "trading port, where Chinese, Japanese and even Arabian "
                "merchants came to buy and sell goods. Through the Arabian "
                "merchants of the day 고려 became known to the world by the "
                "name ‘Korea’. So much so that even when another country "
                "was later founded on the Korean peninsula, it was "
                "remembered abroad by the name ‘고려’."),
        PARAGRAPH("고려는 옛 고구려와 백제, 신라의 다양한 문화를 {통합하면서도|통합하다} 세계 여러 나라와 "
                  "{활발하게|활발하다} {교류하면서|교류하다} 문화를 발전시켰다. 이러한 점에서 고려의 문화는 "
                  "{개방성}과 {다양성}을 띤다고 할 수 있다."),
        PARAGRAPH("고려의 {벽란도}는 중국인, 일본인, 아라비아 {상인}까지 와서 물건을 "
                  "{사고파는|사고팔다} 등 국제적인 {무역항}으로 {널리} 알려졌다. 당시 아라비아 상인들을 "
                  "통해 고려가 ‘코리아’라는 이름으로 세계에 알려졌다. 이후에 한반도에 다른 나라가 세워져도 "
                  "외국에서는 ‘고려’라는 이름으로 기억할 정도였다."),
        FIGURE("고려의 대외무역 — 지도: 거란(요), 여진, 고려, 일본, 황해, 동해; 서경, 개경, 벽란도, "
               "동경, 합포, 탐라, 우산, 덩저우, 밍저우. 화살표와 함께 적힌 물품: ‘금, 은, 인삼, 종이, "
               "화문석, 부채’, ‘약재, 자기, 비단, 차, 향료, 책, 악기’"),

        HEADING(2, "고려의 사회 모습", translation=
                "What 고려 society was like" "\n\n"
                "The aristocratic culture of 고려 was renowned for its "
                "splendour and delicacy. It made, for example, a beautiful "
                "and original pottery called 상감 청자, and on the strength of "
                "its fine craftsmanship it made the world’s first metal "
                "movable type and spread culture." "\n\n"
                "In the 고려 period several religions flourished, with "
                "Buddhism at the centre and Confucianism, Taoism, shamanic "
                "belief and others beside it. Buddhism in particular was "
                "the religion that many people believed in, from the "
                "aristocracy down to the common people; it had a great "
                "influence on the architecture and art of 고려 and left many "
                "Buddhist remains such as temples and statues of the Buddha. "
                "Many Buddhist events were held too, such as 팔관회 and 연등회, "
                "praying for the country’s progress and the happiness of "
                "individuals. During these the whole country became of one "
                "heart and one mind in a festive mood, and many merchants "
                "and officials visited 고려 from China and Japan as well." "\n\n"
                "In the 고려 period monogamy, the union of one husband and "
                "one wife, became the general rule. It is also sometimes "
                "judged to have been considerably progressive, in that men "
                "and women enjoyed rights at almost the same level within "
                "the family."),
        GLOSSARY(("고려의 상감 청자", "상감 청자 특유의 맑고 투명한 색과 부드럽고 생동감 넘치는 모습",
                  "상감 청자",
                  dict(en="the clear, translucent colour peculiar to inlaid celadon, and its soft and lively look")),
                 ("정교", "정확하고 치밀함", "정교",
                  dict(en="being exact and meticulous"))),
        PARAGRAPH("고려의 귀족 문화는 {화려함|화려하다}과 {섬세함|섬세하다}으로 이름이 높았다. 예를 들어, "
                  "{상감 청자}라는 아름답고 {독창적}인 {도자기}를 만들었고 {정교}한 기술을 바탕으로 세계 "
                  "최초의 {금속 활자}를 만들어 문화를 {보급하였다|보급하다}."),
        PARAGRAPH("고려 시대에는 불교를 중심으로 유교, {도교}, {무속 신앙} 등 여러 종교가 발달하였다. "
                  "특히 불교는 귀족부터 백성에 이르기까지 많은 사람들이 믿었던 종교로 고려의 {건축}과 예술 "
                  "등에 많은 영향을 {끼쳤고|끼치다}, {절}이나 {불상}과 같은 불교 {유적}도 많이 남겼다. "
                  "또한, 나라의 발전과 개인의 행복을 {비는|빌다} {팔관회}, {연등회} 등과 같은 불교 행사도 "
                  "많이 열렸다. 이 기간에는 온 나라가 축제 분위기 속에서 {한마음 한뜻}이 되었고, 중국이나 "
                  "일본에서도 많은 상인이나 {관리}들이 고려를 방문하였다."),
        PARAGRAPH("고려 시대에는 남편 1명과 부인 1명이 {결합하는|결합하다} {일부일처}가 일반적으로 자리를 "
                  "잡았다. 또한, 가족 내에서 남녀가 거의 비슷한 수준으로 권리를 {누렸다는|누리다} 점에서 "
                  "{상당히} {진보적}이었다는 {평가}를 받기도 한다."),
        FIGURE("고려의 상감 청자 — 구름과 학 무늬를 새긴 청자 매병"),
        FIGURE("팔관회 모습(상상도)"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "세계 최초의 금속활자로 찍은 책 『직지심체요절』", translation=
                "『직지심체요절』, the book printed with the world’s first metal "
                "movable type" "\n\n"
                "박병선, who left to study in France in 1955, came to work at "
                "the national library in Paris. One day 박병선 found "
                "『직지심체요절』 wedged in a corner of the library’s stacks, "
                "covered in dust. Carrying on her research, she found out "
                "that this was the oldest book in the world printed with "
                "metal movable type. Later, at the ‘exhibition of books "
                "marking International Book Year’ held in Paris, France, in "
                "1972, she presented 『직지심체요절』 for the first time, "
                "together with books from other Asian countries. As a "
                "result it came to be officially recognised as the world’s "
                "first book printed with metal movable type now in "
                "existence (1377). That is as much as 78 years ahead of the "
                "book printed with the metal movable type invented by "
                "Gutenberg of Germany."),
        PARAGRAPH("1955년에 프랑스로 {유학}을 떠난 박병선은 파리 {국립} 도서관에서 일하게 되었다. 어느 "
                  "날 박병선은 도서관 {서고}의 {한구석}에서 {먼지}를 {뒤집어 쓴|뒤집어쓰다} 채 "
                  "{끼여|끼이다} 있던 『{직지심체요절}』을 발견하였다. 연구를 계속한 그녀는 이 책이 세계에서 "
                  "가장 오래된 금속 활자로 찍은 책이라는 것을 알아냈다. 이후 1972년 프랑스 파리에서 열린 "
                  "‘세계 도서의 해 기념 도서 {전시회}’에서 다른 아시아 나라들의 {서적}과 함께 "
                  "『직지심체요절』을 처음으로 소개하였다. 그 결과 현재 {존재하는|존재하다} 세계 최초의 "
                  "금속활자로 찍은 책(1377년)이라는 것을 {공식적}으로 {인정받게|인정받다} 되었다. 이것은 "
                  "독일의 구텐베르크가 {발명한|발명하다} 금속활자로 찍은 책보다 78년이나 {앞선|앞서다} "
                  "것이다."),
        FIGURE("『직지심체요절』과 박병선"),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 고려는 어떻게 발전했을까?"),
        BULLET("고려의 (        )은 신라와 후백제의 항복을 받아 후삼국을 통일하였다."),
        BULLET("고려는 원래 문신 중심의 귀족 사회였는데 (        )들의 반란으로 인해 한동안 지배층이 "
               "(        )으로 바뀌기도 하였다."),
        BULLET("고려는 몽골의 침략에 맞서 수도를 개경에서 (            )로 옮겨 저항하였다."),
        HEADING(3, "02 고려 시대 사람들은 어떻게 살았을까?"),
        BULLET("(            )는 중국인, 일본인뿐만 아니라 아라비아 상인들까지 와서 물건을 사고파는 등 "
               "국제적인 무역항으로 이름이 높았다."),
        BULLET("아라비아 상인들이 부른 고려의 외국식 발음인 (            )가 세계에 알려지게 되었다."),
        BULLET("고려 시대에 (        )는 귀족부터 백성에 이르기까지 많은 사람들이 믿는 종교였다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "[대외 교류(다른 나라와의 교류)로 더욱 풍성해진 고려의 문화]", translation=
                "[The culture of 고려, made richer still by exchange abroad "
                "(exchange with other countries)]" "\n\n"
                "In the 고려 period, as an open policy towards the outside "
                "was pursued, many foreigners from north of the Korean "
                "peninsula, the 거란, the 여진, the Mongols and others, came "
                "into 고려. As they settled and lived in 고려, the make-up of "
                "its population and its culture grew more varied. In late "
                "고려 especially, with the exchange with the Mongols, "
                "Mongol-style clothes came into fashion among the ruling "
                "class, such as the 철릭, made easy to move in by pleating "
                "the lower part of the garment. The 만두, 순대 and 설렁탕 the "
                "Mongols liked to eat, and the way of making drink by "
                "distillation, as with 소주 (heating a liquid into vapour, "
                "then cooling it to make it liquid again), were also passed "
                "on through the Mongols and have come down to today. And "
                "the ‘치’ at the end of a word that marks an occupation, as "
                "in 벼슬아치 (one who holds office) or 장사치 (one who trades), "
                "also comes from Mongolian."),
        PARAGRAPH("고려 시대 때에는 {개방적}인 {대외} 정책을 {펼치면서|펼치다} {거란}, {여진}, 몽골 등 "
                  "한반도 북쪽의 외국인이 고려에 많이 들어왔다. 이들이 고려에 자리를 잡고 살면서 고려의 주민 "
                  "{구성}과 문화가 다양해졌다. 특히 고려 후기에는 몽골과 교류하면서 지배층 사이에서 옷의 "
                  "{아랫도리} 부분에 {주름}을 잡아 활동하기 편하게 만든 {철릭}과 같은 몽골식 옷이 "
                  "{유행하였다|유행하다}. 또한 몽골인이 즐겨 먹던 만두, 순대, 설렁탕, 소주와 같은 {증류} "
                  "방식({액체}에 열을 가해 {증기}로 만든 다음 차갑게 하여 다시 액체로 만드는 방식)으로 "
                  "술을 만드는 방법이 몽골을 통해 {전파되어|전파되다} 오늘날에 이르고 있다. 한편, "
                  "{벼슬아치}(벼슬을 하는 사람)나 {장사치}(장사를 하는 사람)처럼 {말끝}에 직업을 나타내는 "
                  "‘치’도 몽골어에서 {유래하였다|유래하다}."),
        LABELS("철릭", "설렁탕", "소주"),
        FIGURE("철릭, 설렁탕, 소주 사진 세 장"),
        PARAGRAPH("★ 자신의 고향 나라의 {풍속}이나 옷, 음식 등에서 다른 나라로부터 "
                  "{전래된|전래되다} 것은 무엇인지 이야기해 봅시다.",
                  "Talk about what, among the customs, clothes, food and so "
                  "on of your home country, was handed down from another "
                  "country."),
    ],

    extraAnnotations={
        "제작자": dict(
            hanja="製作者", meaning="a maker, a producer",
            characters=[("製", "제", "to make — as in 제품, 제조"),
                        ("作", "작", "to make — as in 작품, 작성"),
                        ("者", "자", "person")],
            notes=["지도 제작자 is a mapmaker, a cartographer."],
        ),
        "가리키다": dict(meaning="to point to, to refer to",
                       surfaces=["가리키는"]),
        "불리다": dict(
            meaning="to be called",
            notes=["The passive of 부르다 “to call”."],
            surfaces=["불렸을까요"],
        ),
        "성립": dict(
            hanja="成立", meaning="coming into being, founding",
            characters=[("成", "성", "to accomplish — as in 성장, 구성"),
                        ("立", "립", "to stand — as in 국립, 설립")],
        ),
        "과정": dict(
            hanja="過程", meaning="a process, a course",
            characters=[("過", "과", "to pass — as in 통과, 과거"),
                        ("程", "정", "a course, a measure — as in 정도, 일정")],
        ),
        "말기": dict(
            hanja="末期", meaning="the closing years, the end of a period",
            characters=[("末", "말", "the end — as in 주말, 연말"),
                        ("期", "기", "a period — as in 후기, 기간")],
            notes=["Against 초기 “the early years” and 후기 “the later "
                   "period”."],
        ),
        "혼란스럽다": dict(
            hanja="混亂스럽다", meaning="to be in turmoil, chaotic",
            characters=[("混", "혼", "to mix — as in 혼합, 혼잡"),
                        ("亂", "란", "disorder — as in 반란, 전란")],
            surfaces=["혼란스러웠고"],
        ),
        "반면": dict(
            hanja="反面", meaning="on the other hand, whereas",
            characters=[("反", "반", "opposite — as in 반대, 위반"),
                        ("面", "면", "a side, a face — as in 방면, 면적")],
            notes=["-던 반면 “whereas …”."],
        ),
        "경제력": dict(
            hanja="經濟力", meaning="economic power, wealth",
            characters=[("經濟", None, "the economy"),
                        ("力", "력", "power — as in 군사력, 능력")],
        ),
        "군사력": dict(
            hanja="軍事力", meaning="military power",
            characters=[("軍事", None, "military affairs — 軍 an army, 事 a matter"),
                        ("力", "력", "power — as in 경제력, 능력")],
        ),
        "세력": dict(
            hanja="勢力", meaning="a force, a power (a group that holds it)",
            characters=[("勢", "세", "force, momentum — as in 자세, 추세"),
                        ("力", "력", "power")],
        ),
        "호족": dict(
            hanja="豪族", meaning="the powerful local clans of late 신라",
            characters=[("豪", "호", "grand, powerful — as in 호화"),
                        ("族", "족", "a clan — as in 귀족, 가족")],
            notes=["The page glosses it itself: 지방에서 경제력이나 군사력이 강한 세력."],
        ),
        "후백제": dict(
            hanja="後百濟", meaning="Later 백제 (900-936)",
            characters=[("後", "후", "later — as in 후기, 이후"),
                        ("百濟", None, "백제, one of the Three Kingdoms")],
        ),
        "후고구려": dict(
            hanja="後高句麗", meaning="Later 고구려 (901-918)",
            characters=[("後", "후", "later"),
                        ("高句麗", None, "고구려, one of the Three Kingdoms")],
        ),
        "후삼국 시대": dict(
            hanja="後三國時代", meaning="the Later Three Kingdoms period",
            characters=[("後", "후", "later"),
                        ("三國", None, "three kingdoms"),
                        ("時代", None, "a period, an age")],
        ),
        "신하": dict(
            hanja="臣下", meaning="a subject, a minister of the king",
            characters=[("臣", "신", "a minister, a subject — as in 문신, 무신"),
                        ("下", "하", "below — as in 지하, 이하")],
        ),
        "몰아내다": dict(meaning="to drive out, to oust",
                       surfaces=["몰아내고"]),
        "계승": dict(
            hanja="繼承", meaning="succession, carrying on",
            characters=[("繼", "계", "to continue — as in 계속"),
                        ("承", "승", "to receive, to take over — as in 승인")],
        ),
        "띠다": dict(
            meaning="to carry, to bear (a meaning, a character)",
            notes=["의미를 띠다 “to carry a meaning”; 다양성을 띠다 “to be marked "
                   "by diversity”."],
            surfaces=["띤다"],
        ),
        "치열하다": dict(
            hanja="熾烈하다", meaning="to be fierce, intense",
            characters=[("熾", "치", "to blaze"),
                        ("烈", "렬", "fierce — as in 강렬, 열렬")],
            surfaces=["치열한"],
        ),
        "벌이다": dict(
            meaning="to wage, to start (a war, an event)",
            notes=["전쟁을 벌이다 “to wage war”."],
            surfaces=["벌였는데"],
        ),
        "항복": dict(
            hanja="降伏", meaning="surrender",
            characters=[("降", "항", "to surrender — read 강 “to descend” in 하강"),
                        ("伏", "복", "to lie prostrate, to submit")],
        ),
        "공격하다": dict(
            hanja="攻擊하다", meaning="to attack",
            characters=[("攻", "공", "to attack — as in 전공, 침공"),
                        ("擊", "격", "to strike — as in 충격, 타격")],
            surfaces=["공격하여"],
        ),
        "통일하다": dict(
            hanja="統一하다", meaning="to unify",
            characters=[("統", "통", "to gather under one rule — as in 통합, 대통령"),
                        ("一", "일", "one")],
            surfaces=["통일하였다"],
        ),
        "태조": dict(
            hanja="太祖", meaning="the founding king of a dynasty",
            characters=[("太", "태", "great, first — as in 태양, 태극"),
                        ("祖", "조", "an ancestor — as in 조상, 조부모")],
            notes=["A temple name: 고려 태조 is 왕건, 조선 태조 is 이성계."],
        ),
        "백성": dict(
            hanja="百姓", meaning="the common people",
            characters=[("百", "백", "a hundred"),
                        ("姓", "성", "a surname — as in 성명")],
        ),
        "안정시키다": dict(
            hanja="安定시키다", meaning="to steady, to stabilise",
            characters=[("安", "안", "peaceful — as in 안전, 안심"),
                        ("定", "정", "to settle — as in 결정, 인정")],
            surfaces=["안정시키기"],
        ),
        "비율": dict(
            hanja="比率", meaning="a rate, a ratio",
            characters=[("比", "비", "to compare — as in 비교, 대비"),
                        ("率", "율", "a rate — as in 확률, 세율")],
        ),
        "거두다": dict(
            meaning="to collect (taxes), to gather in",
            surfaces=["거두지"],
        ),
        "불교": dict(
            hanja="佛敎", meaning="Buddhism",
            characters=[("佛", "불", "the Buddha — as in 불상"),
                        ("敎", "교", "a teaching, a religion — as in 유교, 도교")],
        ),
        "권장": dict(
            hanja="勸獎", meaning="encouragement, urging",
            characters=[("勸", "권", "to urge — as in 권고, 권유"),
                        ("獎", "장", "to encourage — as in 장학금, 장려")],
        ),
        "지치다": dict(meaning="to be worn out, exhausted",
                     surfaces=["지쳐"]),
        "문신": dict(
            hanja="文臣", meaning="a civil official",
            characters=[("文", "문", "letters, civil — as in 문화, 문학"),
                        ("臣", "신", "a minister, a subject — as in 신하")],
        ),
        "귀족": dict(
            hanja="貴族", meaning="the aristocracy, a noble",
            characters=[("貴", "귀", "noble, precious — as in 귀중, 귀하"),
                        ("族", "족", "a clan — as in 호족, 가족")],
        ),
        "무신": dict(
            hanja="武臣", meaning="a military official",
            characters=[("武", "무", "martial — as in 무기, 무술"),
                        ("臣", "신", "a minister, a subject — as in 신하")],
        ),
        "반란": dict(
            hanja="叛亂", meaning="a revolt, a rebellion",
            characters=[("叛", "반", "to rebel — as in 배반"),
                        ("亂", "란", "disorder — as in 혼란")],
        ),
        "무신 정변": dict(
            hanja="武臣政變", meaning="the military officials’ coup (1170)",
            characters=[("武臣", None, "military officials"),
                        ("政變", None, "a coup — 政 government, 變 a change")],
        ),
        "지배층": dict(
            hanja="支配層", meaning="the ruling class",
            characters=[("支", "지", "to hold up, to manage — as in 지원, 지지"),
                        ("配", "배", "to allot — as in 배달, 분배"),
                        ("層", "층", "a layer, a class — as in 계층, 고층")],
        ),
        "불법적": dict(
            hanja="不法的", meaning="unlawful",
            characters=[("不", "불", "not"),
                        ("法", "법", "law"),
                        ("的", "적", "the adjectival suffix")],
        ),
        "노비": dict(
            hanja="奴婢", meaning="slaves, bondsmen and bondswomen",
            characters=[("奴", "노", "a male slave — as in 노예"),
                        ("婢", "비", "a female slave")],
        ),
        "차지하다": dict(meaning="to take, to occupy, to hold",
                       surfaces=["차지하였고"]),
        "저항하다": dict(
            hanja="抵抗하다", meaning="to resist",
            characters=[("抵", "저", "to push against — as in 저촉"),
                        ("抗", "항", "to oppose — as in 항의, 반항")],
            surfaces=["저항하는"],
        ),
        "농민": dict(
            hanja="農民", meaning="a farmer, the peasantry",
            characters=[("農", "농", "farming — as in 농업, 농촌"),
                        ("民", "민", "the people — as in 국민, 주민")],
        ),
        "치르다": dict(
            meaning="to go through, to fight (a war), to hold (an event)",
            surfaces=["치르면서"],
        ),
        "영토": dict(
            hanja="領土", meaning="territory",
            characters=[("領", "령", "to command, a domain — as in 대통령, 영역"),
                        ("土", "토", "land — as in 국토, 토지")],
        ),
        "넓히다": dict(meaning="to widen, to extend", surfaces=["넓혔다"]),
        "침략": dict(
            hanja="侵略", meaning="an invasion",
            characters=[("侵", "침", "to invade — as in 침해, 침입"),
                        ("略", "략", "to seize; a plan — as in 전략, 생략")],
        ),
        "수도": dict(
            hanja="首都", meaning="a capital city",
            characters=[("首", "수", "the head — as in 수석, 수상"),
                        ("都", "도", "a capital, a city — as in 도시, 도읍")],
        ),
        "걸치다": dict(
            meaning="to extend over, to span",
            notes=["약 40년에 걸친 전쟁 “a war lasting some forty years”."],
            surfaces=["걸친"],
        ),
        "해적": dict(
            hanja="海賊", meaning="a pirate",
            characters=[("海", "해", "the sea — as in 해외, 동해"),
                        ("賊", "적", "a robber — as in 도적, 홍건적")],
        ),
        "왜구": dict(
            hanja="倭寇", meaning="the Japanese pirates who raided the coast",
            characters=[("倭", "왜", "the old name for Japan"),
                        ("寇", "구", "a raider, a bandit")],
        ),
        "도적떼": dict(
            hanja="盜賊떼", meaning="a band of robbers",
            characters=[("盜", "도", "to steal — as in 절도, 강도"),
                        ("賊", "적", "a robber — as in 해적")],
            notes=["떼 is a native word for a band, a swarm."],
        ),
        "홍건적": dict(
            hanja="紅巾賊", meaning="the Red Turbans, Chinese rebel bands",
            characters=[("紅", "홍", "red — as in 홍차"),
                        ("巾", "건", "a cloth, a headcloth — as in 수건"),
                        ("賊", "적", "a robber — as in 해적, 도적")],
        ),
        "물리치다": dict(meaning="to drive off, to repel",
                       surfaces=["물리치는"]),
        "성장하다": dict(
            hanja="成長하다", meaning="to grow",
            characters=[("成", "성", "to accomplish — as in 성립, 완성"),
                        ("長", "장", "long, to grow — as in 장점, 사장")],
            surfaces=["성장하였다"],
        ),
        "당시": dict(
            hanja="當時", meaning="at that time, of the day",
            characters=[("當", "당", "the said, that very — as in 당사자, 해당"),
                        ("時", "시", "time — as in 시대, 시간")],
        ),
        "멸망시키다": dict(
            hanja="滅亡시키다", meaning="to bring down, to destroy (a state)",
            characters=[("滅", "멸", "to perish — as in 소멸"),
                        ("亡", "망", "to be ruined, to die — as in 사망, 망하다")],
            surfaces=["멸망시키고"],
        ),
        "묘": dict(
            hanja="墓", meaning="a grave, a tomb",
            characters=[("墓", "묘", "a grave — as in 성묘, 묘지")],
        ),
        "현릉": dict(
            hanja="顯陵", meaning="현릉, the royal tomb of 왕건",
            characters=[("顯", "현", "manifest, illustrious"),
                        ("陵", "릉", "a royal tomb")],
        ),
        "청동상": dict(
            hanja="靑銅像", meaning="a bronze statue",
            characters=[("靑", "청", "blue-green — as in 청자, 청년"),
                        ("銅", "동", "copper — as in 동상, 동전"),
                        ("像", "상", "a figure, an image — as in 불상, 동상")],
        ),
        "발견되다": dict(
            hanja="發見되다", meaning="to be found, discovered",
            characters=[("發", "발", "to send out, to bring out — as in 발명, 발전"),
                        ("見", "견", "to see — as in 의견, 견학")],
            surfaces=["발견되었다"],
        ),
        "역사학자": dict(
            hanja="歷史學者", meaning="a historian",
            characters=[("歷史", None, "history"),
                        ("學者", None, "a scholar")],
        ),
        "황제": dict(
            hanja="皇帝", meaning="an emperor",
            characters=[("皇", "황", "an emperor — as in 황후"),
                        ("帝", "제", "an emperor — as in 제국")],
        ),
        "관": dict(
            hanja="冠", meaning="a crown, formal headgear",
            characters=[("冠", "관", "a cap, a crown — as in 왕관")],
            notes=["The page glosses it 모자."],
        ),
        "모시다": dict(
            meaning="to revere, to attend on (the honorific of 데리다, 받들다)",
            surfaces=["모셨다"],
        ),
        "동상": dict(
            hanja="銅像", meaning="a (bronze) statue",
            characters=[("銅", "동", "copper — as in 청동, 동전"),
                        ("像", "상", "a figure — as in 불상")],
        ),
        "벌거벗다": dict(meaning="to be naked, to strip bare",
                       surfaces=["벌거벗은"]),
        "입히다": dict(
            meaning="to coat, to plate; to dress (someone)",
            notes=["The causative of 입다: 금을 입히다 “to coat in gold”, 옷을 "
                   "입히다 “to dress”."],
            surfaces=["입히고"],
        ),
        "비단": dict(
            hanja="緋緞", meaning="silk",
            characters=[("緋", "비", "scarlet silk"),
                        ("緞", "단", "satin")],
        ),
        "제사": dict(
            hanja="祭祀", meaning="a rite of offering (to ancestors)",
            characters=[("祭", "제", "a rite — as in 축제, 제례"),
                        ("祀", "사", "to offer a rite")],
            notes=["제사를 지내다 “to hold the rite”."],
        ),
        "유교": dict(
            hanja="儒敎", meaning="Confucianism",
            characters=[("儒", "유", "a Confucian scholar — as in 유학"),
                        ("敎", "교", "a teaching — as in 불교, 도교")],
        ),
        "예절": dict(
            hanja="禮節", meaning="propriety, manners",
            characters=[("禮", "예", "rites, courtesy — as in 예의, 혼례"),
                        ("節", "절", "a joint; moderation — as in 절약, 계절")],
        ),
        "묻다": dict(
            meaning="to bury",
            notes=["묻어 두다 “to bury and leave”. Not 묻다 “to ask”, which "
                   "conjugates 물어."],
            surfaces=["묻어"],
        ),
        "벗겨지다": dict(meaning="to peel off, to come off",
                       surfaces=["벗겨지고"]),
        "썩다": dict(
            meaning="to rot",
            notes=["썩어 버리다 “to rot away”; the page prints it closed up, "
                   "썩어버린."],
            surfaces=["썩어버린"],
        ),
        "통합하다": dict(
            hanja="統合하다", meaning="to bring together, to integrate",
            characters=[("統", "통", "to gather under one — as in 통일"),
                        ("合", "합", "to join — as in 결합, 합계")],
            surfaces=["통합하면서도"],
        ),
        "활발하다": dict(
            hanja="活潑하다", meaning="to be lively, active",
            characters=[("活", "활", "to live, lively — as in 생활, 활동"),
                        ("潑", "발", "to splash; vigorous")],
            surfaces=["활발하게"],
        ),
        "교류하다": dict(
            hanja="交流하다", meaning="to exchange, to have dealings with",
            characters=[("交", "교", "to exchange — as in 외교, 교통"),
                        ("流", "류", "to flow — as in 유행, 한류")],
            surfaces=["교류하면서"],
        ),
        "개방성": dict(
            hanja="開放性", meaning="openness",
            characters=[("開", "개", "to open — as in 개발, 공개"),
                        ("放", "방", "to release — as in 방송, 해방"),
                        ("性", "성", "a quality — as in 다양성")],
        ),
        "다양성": dict(
            hanja="多樣性", meaning="diversity",
            characters=[("多", "다", "many — as in 다문화"),
                        ("樣", "양", "a form, a manner — as in 모양"),
                        ("性", "성", "a quality — as in 개방성")],
        ),
        "벽란도": dict(
            hanja="碧瀾渡",
            meaning="벽란도, the trading port of 고려 near 개경",
            characters=[("碧", "벽", "blue-green"),
                        ("瀾", "란", "a wave"),
                        ("渡", "도", "a crossing, a ferry")],
        ),
        "상인": dict(
            hanja="商人", meaning="a merchant",
            characters=[("商", "상", "trade — as in 상업, 상품"),
                        ("人", "인", "person")],
        ),
        "사고팔다": dict(meaning="to buy and sell, to trade",
                       surfaces=["사고파는"]),
        "무역항": dict(
            hanja="貿易港", meaning="a trading port",
            characters=[("貿", "무", "to trade"),
                        ("易", "역", "to exchange"),
                        ("港", "항", "a port — as in 공항, 항구")],
        ),
        "널리": dict(meaning="widely, far and wide"),
        "화려하다": dict(
            hanja="華麗하다", meaning="to be splendid, gorgeous",
            characters=[("華", "화", "flowery, brilliant — as in 호화"),
                        ("麗", "려", "beautiful — the 려 of 고려")],
            notes=["화려함 is the noun made with -ㅁ: “splendour”."],
            surfaces=["화려함"],
        ),
        "섬세하다": dict(
            hanja="纖細하다", meaning="to be delicate, fine",
            characters=[("纖", "섬", "fine, slender — as in 섬유"),
                        ("細", "세", "thin, fine — as in 세부, 상세")],
            notes=["섬세함 is the noun made with -ㅁ: “delicacy”."],
            surfaces=["섬세함"],
        ),
        "상감 청자": dict(
            hanja="象嵌靑瓷", meaning="inlaid celadon",
            characters=[("象嵌", None, "inlay — cutting a pattern into the "
                                      "surface and filling it with another clay"),
                        ("靑", "청", "blue-green — as in 청동"),
                        ("瓷", "자", "porcelain — as in 도자기, 자기")],
        ),
        "독창적": dict(
            hanja="獨創的", meaning="original, creative",
            characters=[("獨", "독", "alone — as in 독립, 독학"),
                        ("創", "창", "to create — as in 창조, 창의"),
                        ("的", "적", "the adjectival suffix")],
        ),
        "도자기": dict(
            hanja="陶瓷器", meaning="pottery, ceramics",
            characters=[("陶", "도", "earthenware"),
                        ("瓷", "자", "porcelain — as in 청자"),
                        ("器", "기", "a vessel — as in 악기, 용기")],
        ),
        "정교": dict(
            hanja="精巧", meaning="fineness, intricacy of workmanship",
            characters=[("精", "정", "refined, fine — as in 정신, 정밀"),
                        ("巧", "교", "skilful — as in 기교")],
            notes=["Used as 정교하다: 정교한 기술 “fine craftsmanship”."],
        ),
        "금속 활자": dict(
            hanja="金屬活字", meaning="metal movable type",
            characters=[("金屬", None, "metal"),
                        ("活字", None, "movable type — 活 live, 字 a character")],
            notes=["The 알아두면 좋아요 box prints it closed up, 금속활자, as "
                   "well as spaced."],
        ),
        "보급하다": dict(
            hanja="普及하다", meaning="to spread, to make widely available",
            characters=[("普", "보", "widespread — as in 보통, 보편"),
                        ("及", "급", "to reach — as in 언급")],
            surfaces=["보급하였다"],
        ),
        "도교": dict(
            hanja="道敎", meaning="Taoism",
            characters=[("道", "도", "the way — as in 도로, 도덕"),
                        ("敎", "교", "a teaching — as in 불교, 유교")],
        ),
        "무속 신앙": dict(
            hanja="巫俗信仰", meaning="shamanic belief",
            characters=[("巫俗", None, "shamanic custom — 巫 a shaman, 俗 custom"),
                        ("信仰", None, "faith — 信 to believe, 仰 to look up to")],
        ),
        "건축": dict(
            hanja="建築", meaning="architecture, building",
            characters=[("建", "건", "to build — as in 건국, 건물"),
                        ("築", "축", "to build up — as in 신축")],
        ),
        "끼치다": dict(
            meaning="to exert, to cause (an influence, trouble)",
            notes=["영향을 끼치다 “to have an influence”."],
            surfaces=["끼쳤고"],
        ),
        "절": dict(meaning="a Buddhist temple"),
        "불상": dict(
            hanja="佛像", meaning="a statue of the Buddha",
            characters=[("佛", "불", "the Buddha — as in 불교"),
                        ("像", "상", "a figure — as in 동상")],
        ),
        "유적": dict(
            hanja="遺跡", meaning="remains, a historic site",
            characters=[("遺", "유", "to leave behind — as in 유산, 유물"),
                        ("跡", "적", "a trace — as in 흔적")],
        ),
        "빌다": dict(
            meaning="to pray for, to wish",
            surfaces=["비는"],
        ),
        "팔관회": dict(
            hanja="八關會",
            meaning="팔관회, a state festival of 고려 with Buddhist rites",
            characters=[("八", "팔", "eight"),
                        ("關", "관", "a barrier, a precept — as in 관계, 세관"),
                        ("會", "회", "a gathering — as in 연등회, 회의")],
        ),
        "연등회": dict(
            hanja="燃燈會", meaning="연등회, the lantern festival",
            characters=[("燃", "연", "to burn — as in 연료"),
                        ("燈", "등", "a lamp — as in 신호등, 전등"),
                        ("會", "회", "a gathering — as in 팔관회")],
        ),
        "한마음 한뜻": dict(
            meaning="one heart and one mind",
            notes=["한 “one” with 마음 “heart” and 뜻 “will, intent”."],
        ),
        "관리": dict(
            hanja="官吏", meaning="an official",
            characters=[("官", "관", "an official — as in 장관, 경찰관"),
                        ("吏", "리", "a petty official")],
            notes=["Not 관리 (管理) “management”."],
        ),
        "결합하다": dict(
            hanja="結合하다", meaning="to unite, to be joined",
            characters=[("結", "결", "to tie — as in 결혼, 결과"),
                        ("合", "합", "to join — as in 통합")],
            surfaces=["결합하는"],
        ),
        "일부일처": dict(
            hanja="一夫一妻", meaning="monogamy",
            characters=[("一", "일", "one"),
                        ("夫", "부", "a husband — as in 부부"),
                        ("一", "일", "one"),
                        ("妻", "처", "a wife")],
        ),
        "누리다": dict(meaning="to enjoy (a right, a benefit)",
                     surfaces=["누렸다는"]),
        "상당히": dict(
            hanja="相當히", meaning="considerably, quite",
            characters=[("相", "상", "mutual — as in 상대, 상담"),
                        ("當", "당", "to match, the said — as in 당시, 해당")],
        ),
        "진보적": dict(
            hanja="進步的", meaning="progressive",
            characters=[("進", "진", "to advance — as in 진행, 진학"),
                        ("步", "보", "a step — as in 도보"),
                        ("的", "적", "the adjectival suffix")],
        ),
        "평가": dict(
            hanja="評價", meaning="an assessment, a judgment",
            characters=[("評", "평", "to judge — as in 비평"),
                        ("價", "가", "value — as in 가격, 물가")],
            notes=["평가를 받다 “to be judged, regarded as”."],
        ),
        "유학": dict(
            hanja="留學", meaning="study abroad",
            characters=[("留", "유", "to stay — as in 체류"),
                        ("學", "학", "to study")],
            notes=["유학을 떠나다 “to leave to study abroad”."],
        ),
        "국립": dict(
            hanja="國立", meaning="national, state-founded",
            characters=[("國", "국", "a country"),
                        ("立", "립", "to stand, to found — as in 성립, 설립")],
        ),
        "서고": dict(
            hanja="書庫", meaning="a library’s stacks, a book store",
            characters=[("書", "서", "a book, writing — as in 서적, 도서관"),
                        ("庫", "고", "a storehouse — as in 창고, 냉장고")],
        ),
        "한구석": dict(meaning="a corner, an out-of-the-way spot"),
        "먼지": dict(meaning="dust"),
        "뒤집어쓰다": dict(
            meaning="to be covered all over in",
            notes=["The page prints it spaced, 뒤집어 쓴."],
            surfaces=["뒤집어 쓴"],
        ),
        "끼이다": dict(
            meaning="to be wedged in, stuck between",
            notes=["The passive of 끼다; 끼여 is 끼이어 contracted."],
            surfaces=["끼여"],
        ),
        "직지심체요절": dict(
            hanja="直指心體要節",
            meaning="직지심체요절, a Buddhist text printed with metal type in "
                    "1377",
            characters=[("直指", None, "pointing straight at"),
                        ("心體", None, "the substance of the mind"),
                        ("要節", None, "essential passages")],
            notes=["Usually shortened to 직지."],
        ),
        "전시회": dict(
            hanja="展示會", meaning="an exhibition",
            characters=[("展", "전", "to unfold — as in 발전, 전망"),
                        ("示", "시", "to show — as in 표시, 지시"),
                        ("會", "회", "a gathering")],
        ),
        "서적": dict(
            hanja="書籍", meaning="books",
            characters=[("書", "서", "a book — as in 서고, 도서"),
                        ("籍", "적", "a register, a book — as in 국적")],
        ),
        "존재하다": dict(
            hanja="存在하다", meaning="to exist",
            characters=[("存", "존", "to exist — as in 보존, 생존"),
                        ("在", "재", "to be at — as in 현재, 재외")],
            surfaces=["존재하는"],
        ),
        "공식적": dict(
            hanja="公式的", meaning="official",
            characters=[("公", "공", "public — as in 공공, 공정"),
                        ("式", "식", "a form, a ceremony — as in 방식, 결혼식"),
                        ("的", "적", "the adjectival suffix")],
        ),
        "인정받다": dict(
            hanja="認定받다", meaning="to be recognised",
            characters=[("認", "인", "to recognise — as in 확인, 인증"),
                        ("定", "정", "to settle — as in 안정, 결정")],
            surfaces=["인정받게"],
        ),
        "발명하다": dict(
            hanja="發明하다", meaning="to invent",
            characters=[("發", "발", "to bring out — as in 발견, 발전"),
                        ("明", "명", "bright, clear — as in 설명, 증명")],
            surfaces=["발명한"],
        ),
        "앞서다": dict(
            meaning="to be ahead of, to come before",
            surfaces=["앞선"],
        ),
        "개방적": dict(
            hanja="開放的", meaning="open",
            characters=[("開", "개", "to open — as in 개방성"),
                        ("放", "방", "to release — as in 방송"),
                        ("的", "적", "the adjectival suffix")],
        ),
        "대외": dict(
            hanja="對外", meaning="towards the outside, foreign",
            characters=[("對", "대", "facing, towards — as in 상대, 대상"),
                        ("外", "외", "outside — as in 외국, 해외")],
            notes=["대외 정책 “foreign policy”, 대외 교류 “exchange abroad”, "
                   "대외무역 “foreign trade”."],
        ),
        "펼치다": dict(
            meaning="to unfold, to pursue (a policy)",
            surfaces=["펼치면서"],
        ),
        "거란": dict(
            hanja="契丹", meaning="the Khitan, who founded the Liao (요) state",
        ),
        "여진": dict(
            hanja="女眞", meaning="the Jurchen",
        ),
        "구성": dict(
            hanja="構成", meaning="make-up, composition",
            characters=[("構", "구", "to construct — as in 구조, 기구"),
                        ("成", "성", "to accomplish — as in 성립, 성장")],
        ),
        "아랫도리": dict(meaning="the lower half of the body, or of a garment"),
        "주름": dict(
            meaning="a pleat, a crease, a wrinkle",
            notes=["주름을 잡다 “to pleat”."],
        ),
        "철릭": dict(
            meaning="철릭, a robe with a pleated skirt sewn to the bodice",
            notes=["The word itself came in from Mongolian."],
        ),
        "유행하다": dict(
            hanja="流行하다", meaning="to be in fashion, to spread",
            characters=[("流", "유", "to flow — as in 교류, 한류"),
                        ("行", "행", "to go — as in 행사, 진행")],
            surfaces=["유행하였다"],
        ),
        "증류": dict(
            hanja="蒸溜", meaning="distillation",
            characters=[("蒸", "증", "to steam — as in 증기, 증발"),
                        ("溜", "류", "to drip, to trickle")],
        ),
        "액체": dict(
            hanja="液體", meaning="a liquid",
            characters=[("液", "액", "liquid — as in 혈액"),
                        ("體", "체", "a body — as in 신체, 단체")],
        ),
        "증기": dict(
            hanja="蒸氣", meaning="vapour, steam",
            characters=[("蒸", "증", "to steam — as in 증류"),
                        ("氣", "기", "air, energy — as in 공기, 분위기")],
        ),
        "전파되다": dict(
            hanja="傳播되다", meaning="to be passed on, to spread",
            characters=[("傳", "전", "to hand on — as in 전래, 전통"),
                        ("播", "파", "to sow, to spread")],
            surfaces=["전파되어"],
        ),
        "벼슬아치": dict(
            meaning="an office-holder, an official",
            notes=["벼슬 “government office” with -아치, which marks a person "
                   "by what they do."],
        ),
        "장사치": dict(
            meaning="a trader, a hawker (slighting)",
            notes=["장사 “trade” with -치."],
        ),
        "말끝": dict(meaning="the end of a word"),
        "유래하다": dict(
            hanja="由來하다", meaning="to come from, to originate in",
            characters=[("由", "유", "from, a cause — as in 이유, 자유"),
                        ("來", "래", "to come — as in 전래, 미래")],
            surfaces=["유래하였다"],
        ),
        "풍속": dict(
            hanja="風俗", meaning="customs",
            characters=[("風", "풍", "wind, a manner — as in 풍습, 태풍"),
                        ("俗", "속", "custom — as in 무속, 민속")],
        ),
        "전래되다": dict(
            hanja="傳來되다", meaning="to be handed down, brought in",
            characters=[("傳", "전", "to hand on — as in 전파, 전통"),
                        ("來", "래", "to come — as in 유래")],
            surfaces=["전래된"],
        ),
    },

    extraNotes=[
        "The margin terms on p. 209 are set beside the article each belongs "
        "to: 신하 and 계승 with the first, 태조, 권장, 문신 and 무신 with the "
        "second. 후삼국 시대 in that margin is a map with no definition, and "
        "is set as a figure.",
        "The maps and photographs on pp. 208-211 are not reproduced; their "
        "captions are, and the place names and goods printed on the 대외무역 "
        "map on p. 210 are listed in its caption.",
        "The review gaps on p. 211 are blank in the book and left blank here.",
    ],
)
