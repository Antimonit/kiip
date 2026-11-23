# -*- coding: utf-8 -*-
"""Chapter 41 — The founding and development of 조선.

Transcribed from the photos of pp. 212-215. Nothing is written on these
pages by hand.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, LABELS,
               TABLE, CELL, VERSE, GLOSSARY)

CHAPTER = dict(
    number=41, slug="41-joseon",
    unit="역사", title="조선의 건국과 발전",
    titleEn="The founding and development of 조선",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 서울 광화문에 세워져 있는 한 왕의 {동상}입니다.",
                  "Below is the statue of a king that stands at 광화문 in "
                  "Seoul."),
        FIGURE("세종대왕 동상 — 받침돌에 ‘세종대왕’이라고 새겨져 있다"),
        HEADING(4, "01 이 왕은 한국의 어느 {화폐}에 들어 있습니까? 이 왕을 ‘{대왕}’이라고 부르는 "
                   "이유는 무엇일까요?",
                translation="Which Korean note or coin is this king on? Why "
                            "is this king called ‘the Great’?"),
        HEADING(4, "02 자신의 고향 나라에서 가장 {존경}을 많이 받는 왕이나 인물을 한 사람씩 소개해 "
                   "봅시다.",
                translation="Each introduce one king or figure who is most "
                            "respected in your home country."),

        SECTION("goals", "학습목표"),
        BULLET("조선의 {성립}과 발전 과정을 설명할 수 있다.", ordered=True,
               translation="Explain how 조선 came into being and developed."),
        BULLET("조선 시대 사회와 문화에 대해 설명할 수 있다.", ordered=True,
               translation="Explain the society and culture of the 조선 "
                           "period."),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"],
              [["기본", "역사", "44. 한국의 문화유산", "유교문화의 발전, 조선의 과학 기술"]]),

        SECTION("part", "01 조선은 나라의 기틀을 어떻게 마련하였을까?"),
        GLOSSARY(("성곽", "성과 성의 둘레", "성곽",
                  dict(en="a fortress and the wall around it"))),
        HEADING(2, "조선의 {건국}", translation=
                "The founding of 조선" "\n\n"
                "태조 이성계, who founded 조선 in 1392, moved the capital from "
                "개경 (개성) to 한양 (한성, today’s Seoul) to give the country a "
                "new look and a new mood. He also built 경복궁 and 종묘, as "
                "well as the four great gates, 숭례문 (남대문) and 동대문 among "
                "them, and the fortress walls." "\n\n"
                "조선 was governed on the basis of Confucian ideas. "
                "Accordingly it stressed closeness between parents and "
                "children, loyalty and duty between king and subject, "
                "distinction between husband and wife (respect for their "
                "different roles), order between old and young (elders "
                "treated first), trust between friends, and so on. These "
                "ideas have changed little by little as the times have "
                "changed, but they still influence Korea today."),
        PARAGRAPH("1392년 조선을 세운 {태조} 이성계는 나라의 모습과 {분위기}를 새롭게 하기 위해 "
                  "{수도}를 개경(개성)에서 한양(한성, 오늘의 서울)으로 옮겼다. 또한 {경복궁}과 "
                  "{종묘}를 {비롯해|비롯하다} {숭례문}(남대문), 동대문 등 {4대문}과 {성곽}도 세웠다."),
        PARAGRAPH("조선은 {유교}의 {이념}을 {바탕}으로 나라를 {다스렸다|다스리다}. 이에 따라 부모와 "
                  "자녀 사이의 {친밀한|친밀하다} 관계, 왕과 {신하} 사이의 {의리}, 남편과 아내 사이의 "
                  "{구별}(서로 다른 역할 존중), 어른과 아이 사이의 순서(어른을 먼저 {대우}), 친구 "
                  "사이의 믿음 등을 강조하였다. 이러한 내용은 시대가 변하면서 조금씩 달라지기는 했지만 "
                  "오늘날에도 한국에 여전히 영향을 주고 있다."),
        FIGURE("조선의 지방 행정 조직(8도) — 도마다 색을 달리한 한반도 지도"),
        LABELS("함길도(함경도)", "평안도", "황해도", "한성", "강원도", "경기도", "충청도",
               "경상도", "전라도"),

        GLOSSARY(("호패",
                  "호패에는 신분에 따라 조금씩 다르다. 이름, 출생 연도, 주소, 얼굴빛, 키 등이 적혀 "
                  "있었다.", "호패",
                  dict(en="호패 differed a little according to status. The name, year of birth, address, complexion, height and so on were written on them."))),
        HEADING(2, "조선의 발전", translation=
                "The development of 조선" "\n\n"
                "태종, the son of 이성계, greatly strengthened the king’s power "
                "and laid the foundation on which 조선 could develop. He also "
                "brought in a law making every man aged sixteen or over "
                "carry a 호패 (an identity tag), and so kept an exact record "
                "of the people’s lives, their births, movements and the "
                "like." "\n\n"
                "세종, the son of 태종, is regarded as the greatest king of "
                "조선. Culture, science and technology developed greatly in "
                "this period. Together with outstanding scholars and "
                "officials, 세종 published many books on history, geography, "
                "etiquette and other subjects. To help farming, he also had "
                "the rain gauge, the sundial, the water clock and other "
                "instruments made. And so that the people could read and "
                "write easily, he created 훈민정음 (“the correct sounds for "
                "teaching the people”, today’s 한글)." "\n\n"
                "In the reign of 성종 the 『경국대전』, the basic code of law "
                "for governing the country, was completed. The 『경국대전』 "
                "contains provisions on life as a whole: what the king and "
                "the officials must do, taxes, the buying and selling of "
                "goods, etiquette, military affairs, punishments and so on. "
                "This code shows that 조선 was a state under the rule of law, "
                "governed according to the law and not by the king’s word."),
        PARAGRAPH("이성계의 아들 태종은 왕의 {권력}을 크게 {강화시켜|강화시키다} 조선이 발전할 수 있는 "
                  "{기틀}을 마련하였다. 또한, 16살 이상의 남자는 모두 {호패}({신분증})를 "
                  "{차고|차다} 다니도록 하는 법을 실시하여 {백성}의 출생, 이동 등과 같은 생활을 "
                  "정확하게 관리하였다."),
        PARAGRAPH("태종의 아들 세종은 조선의 가장 {위대한|위대하다} 왕으로 평가 받는다. 이 시기에 "
                  "문화와 과학 기술이 크게 발달하였다. 세종은 우수한 학자와 {관리}들과 함께 역사, 지리, "
                  "예절 등과 관련한 많은 책을 {펴냈다|펴내다}. 또한, 농사에 도움을 주기 위해 "
                  "{측우기}, {해시계}, {물시계} 등을 만들었다. 그리고 백성이 쉽게 글을 읽고 쓸 수 "
                  "있도록 하기 위해 {훈민정음}(백성을 가르치는 바른 소리, 오늘의 한글)을 만들었다."),
        PARAGRAPH("성종 때에는 나라를 다스리는 기본 {법전}인 『{경국대전}』을 완성하였다. 『경국대전』에는 "
                  "왕과 관리가 해야 할 일, 세금, 물건 거래, 예절, {군사}, {형벌} 등 생활 {전반}에 "
                  "관한 내용이 {담겨|담기다} 있다. 이 법은 조선이 왕의 말이 아닌 법에 따라 나라를 "
                  "다스리는 {법치국가}임을 보여준다."),
        FIGURE("호패 여덟 점 (출처: 국립중앙박물관)"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "『경국대전』을 통해 살펴본 백성의 삶", translation=
                "The people’s lives as seen through the 『경국대전』" "\n\n"
                "The 《경국대전》 was long the basis of government in 조선, and "
                "it had a great influence on the lives of the people too. "
                "Some of its provisions that bore on the people’s daily "
                "lives are as follows."),
        PARAGRAPH("《경국대전》은 오랫동안 조선 {통치}의 기본이 되었으며 백성의 생활에도 많은 영향을 "
                  "미쳤다. 그중에서 백성의 일상생활과 관련되었던 일부 내용을 살펴보면 다음과 같다."),
        BULLET("땅과 집을 사면 100일 안에 국가 기관에 보고해야 한다.",
               translation="Anyone who buys land or a house must report it "
                           "to a state office within 100 days."),
        BULLET("부모가 많이 아프거나 부모의 나이가 70세 이상이면 그 아들은 군대에 가지 않아도 된다.",
               translation="If a parent is very ill, or aged 70 or over, the "
                           "son need not go into the army."),
        BULLET("{노비}인 여성이 아이를 낳으면 {출산 휴가} 기간은 90일이다. 필요한 경우에는 남편도 "
               "출산 휴가를 신청할 수 있다.",
               translation="When a woman who is a 노비 has a child, her "
                           "maternity leave is 90 days. Where necessary her "
                           "husband can apply for maternity leave too."),
        FIGURE("『경국대전』 (출처: 서울역사박물관)"),

        SECTION("part", "02 조선 후기에는 어떤 변화가 나타났을까?"),
        GLOSSARY(("임진왜란", "임진년(1592년)에 왜(일본)가 일으킨 전란", "임진왜란",
                  dict(en="the war started by 왜 (Japan) in the 임진 year (1592)")),
                 ("의병", "백성들이 자발적으로 조직한 군대", "의병",
                  dict(en="an army organised by the people of their own accord")),
                 ("병자호란", "병자년(1636년)에 호(청나라)가 일으킨 전란", "병자호란",
                  dict(en="the war started by 호 (the Qing) in the 병자 year (1636)")),
                 ("남한산성", "병자호란 당시 마지막까지 청의 군대에 맞서 싸운 곳", "남한산성",
                  dict(en="the place where the Qing army was fought to the last during the 병자호란"))),
        HEADING(2, "두 차례의 큰 전쟁을 극복한 조선", translation=
                "조선 overcomes two great wars" "\n\n"
                "Japan’s invasion of 조선 in 1592 is called the 임진왜란. The "
                "수군 (navy) of 조선, under 이순신 and others, held off the "
                "attacks of the Japanese forces well, and the people formed "
                "righteous armies and fought against the Japanese. As a "
                "result of these efforts the country was defended against "
                "the Japanese forces. In 1636 came the 병자호란, in which the "
                "Qing dynasty of China invaded 조선. 조선 fought to the end at "
                "남한산성, but in the end it accepted the demands of the Qing "
                "and brought the war to a close." "\n\n"
                "The two great wars left the farmland ruined and made the "
                "people’s lives hard. 영조 and 정조, kings of 조선, worked to "
                "overcome this crisis. They lightened taxes to steady the "
                "people’s livelihood, and developed not only farming but the "
                "fields the people needed, such as commerce and industry. "
                "Together with scholars who argued that 조선 should take in "
                "what it needed from other countries, they also contributed "
                "to the advance of learning. It was in 정조’s reign, too, "
                "that 수원 화성 was built, a UNESCO World Heritage site "
                "regarded as an outstanding piece of architecture."),
        PARAGRAPH("1592년 일본이 조선을 {침략한|침략하다} 사건을 {임진왜란}이라고 한다. 이순신 등 "
                  "조선의 {수군}(해군)이 일본군의 공격을 잘 {막아냈고|막아내다} 백성들은 {의병}을 "
                  "{조직하여|조직하다} 일본군에 {맞서|맞서다} 싸웠다. 이러한 노력의 결과 일본군으로부터 "
                  "나라를 지켜 냈다. 1636년에는 중국의 {청나라}가 조선을 침략한 {병자호란}이 일어났다. "
                  "조선은 {남한산성}에서 끝까지 싸웠지만 결국 청의 요구를 들어주고 전쟁을 끝냈다."),
        PARAGRAPH("두 차례의 큰 전쟁으로 {농토}는 {망가졌고|망가지다} 백성들의 삶도 힘들어졌다. 조선의 "
                  "왕이었던 영조와 정조는 이러한 위기를 {극복하기|극복하다} 위해 노력하였다. 세금을 줄여 "
                  "주어 백성의 생활을 {안정시켰고|안정시키다} 농업뿐 아니라 {상업}, {공업} 등 백성이 "
                  "필요로 하는 분야를 발전시켰다. 또한 다른 나라로부터 조선에 필요한 것을 받아들여야 "
                  "한다고 주장하는 학자들과 함께 {학문} 발전에도 {기여하였다|기여하다}. 유네스코 "
                  "{세계유산}의 하나로 뛰어난 {건축물}로 평가 받는 {수원 화성}이 건축된 것도 정조 "
                  "때이다."),
        FIGURE("남한산성의 성문과 성벽 사진"),

        GLOSSARY(("과거", "국가 관리를 뽑기 위해 보는 시험", "과거",
                  dict(en="the examination held to select state officials")),
                 ("백정", "소, 돼지 등을 잡는 사람", "백정",
                  dict(en="a person who slaughters cattle, pigs and the like")),
                 ("판소리", "소리꾼이 북 장단에 맞추어 들려주는 긴 이야기", "판소리",
                  dict(en="a long story a singer tells to the rhythm of a drum")),
                 ("탈놀이", "머리에 탈을 쓰고 노는 놀이", "탈놀이",
                  dict(en="a performance played wearing a mask on the head")),
                 ("민화", "백성의 생활 모습을 주로 비전문가가 그린 평범한 그림", "민화",
                  dict(en="ordinary pictures of the people's life, painted mostly by non-professionals"))),
        HEADING(2, "조선 후기의 사회와 문화", translation=
                "Society and culture in late 조선" "\n\n"
                "Status in 조선 was divided broadly into 양반, 중인, 상민 and "
                "천민. The 양반 were the ruling class, and devoted themselves "
                "to study in order to pass the 과거. The 중인 were technical "
                "officials such as interpreters and physicians. 상민 refers "
                "to farmers, craftsmen, merchants and the like. The 천민 were "
                "노비, 백정 and others, and did work that was held to be mean "
                "and low." "\n\n"
                "In late 조선 the status system was shaken: the 양반 grew in "
                "number, and the 상민 and 천민 grew fewer. This social change "
                "is regarded as a movement towards doing away with status "
                "and gradually becoming an equal society. And unlike early "
                "조선, which centred on the culture of the 양반, late 조선 also "
                "saw a great flowering of the culture of ordinary people, in "
                "한글 novels, 판소리, 탈놀이, 민화 and the like."),
        PARAGRAPH("조선의 {신분}은 크게 {양반}, {중인}, {상민}, {천민}으로 나누어져 있었다. 양반은 "
                  "{지배층}으로 {과거} 합격을 위해 {글공부}에 {힘썼다|힘쓰다}. 중인은 통역관이나 의사 "
                  "등과 같은 기술 관리였다. 상민은 농민·{수공업자}·상인 등을 가리킨다. 천민은 노비나 "
                  "{백정} 등으로 {천하고|천하다} 낮은 일을 담당하였다."),
        PARAGRAPH("조선 {후기}에는 {신분제}가 흔들리면서 양반이 많아지고 상민과 천민의 수가 줄어들었다. "
                  "이러한 사회 변화는 신분을 없애고 {점차} {평등한|평등하다} 사회로 나아가고자 하는 "
                  "움직임으로 평가받는다. 또한, 양반 문화 중심이었던 조선 {전기}와 달리 조선 후기에는 "
                  "한글 소설, {판소리}, {탈놀이}, {민화} 등 {서민} 문화도 크게 발달하였다."),
        FIGURE("안동 하회 별신굿 탈놀이 (사진 출처: 〈연합뉴스〉)"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "수원 화성의 공사 기간이 대폭 줄어든 이유는?", translation=
                "Why was the building of 수원 화성 cut so much shorter?" "\n\n"
                "수원 화성, built by 정조, was originally expected to take ten "
                "years to build. Yet the work actually took less than three "
                "years, and the secret was as follows. 조선 had always put "
                "the people to work without giving anything in return, but "
                "when 화성 was built, workers were recruited and paid wages "
                "(품삯). When the weather was sweltering, moreover, the "
                "workers were given medicine to protect their bodies, and "
                "wages were paid even for the time they could not work "
                "because they were being treated. They were also paid "
                "allowances (money given separately, on top of wages) "
                "according to the results of their work, and now and then a "
                "feast was held to encourage them. The workers then took "
                "part in the building of 화성 all the more diligently. On top "
                "of that, the 거중기, which applied the principle of the "
                "pulley, was used to lift heavy loads, and this science and "
                "technology too did much to shorten the building time."),
        PARAGRAPH("정조가 세운 수원 화성은 원래 {예상} {공사} 기간이 10년이었다. 그러나 실제 공사 "
                  "시간은 3년도 걸리지 않았는데 그 {비결}은 다음과 같다. 원래 조선은 아무런 {대가}를 "
                  "주지 않고 백성에게 일을 시켰는데 화성을 세울 때는 {일꾼}을 {모집하여|모집하다} "
                  "{임금}({품삯})을 {지급하였다|지급하다}. 또한, 날이 {무더울|무덥다} 때는 일하는 "
                  "사람들에게 몸을 보호하는 약을 주었고, 치료를 받느라 일하지 못하는 기간에도 임금을 "
                  "줬다. 또한 일의 {성과}에 따라 {수당}(임금 이외에 따로 주는 돈)을 지급하였고 가끔 "
                  "{잔치}를 열어 {격려}도 해 주었다. 그러자 일꾼들이 더욱 열심히 화성 건축에 "
                  "참여하였다. 뿐만 아니라 무거운 짐을 들어올리기 위해 {도르래}의 {원리}를 이용한 "
                  "{거중기}를 사용하였는데 이 같은 과학기술도 공사 기간 {단축}에 큰 도움을 주었다."),
        FIGURE("수원 화성과 거중기"),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 조선은 나라의 기틀을 어떻게 마련하였을까?"),
        BULLET("조선을 세운 태조 이성계는 나라의 모습과 분위기를 새롭게 하기 위해 수도를 개경에서 "
               "(        )으로 옮겼다."),
        BULLET("(        )은 농사에 도움을 주기 위해 측우기, 해시계, 물시계 등을 만들었고 백성이 글을 "
               "쉽게 배울 수 있도록 훈민정음을 만들었다."),
        BULLET("성종 때에는 나라를 다스리는 기본 법전인 (            )을 완성하였다."),
        HEADING(3, "02 조선 후기에는 어떤 변화가 나타났을까?"),
        BULLET("조선 시대에 일본이 조선을 침략한 사건을 (            )이라고 하고, 중국 청나라가 "
               "조선을 침략한 사건을 병자호란이라고 한다."),
        BULLET("정조가 왕이던 시기에 지어진 수원 (        )은 유네스코 세계문화유산의 하나로, 뛰어난 "
               "건축물로 평가 받는다."),
        BULLET("조선 후기에 신분제가 흔들리면서 (        )이 많아지고 상민과 천민이 줄어들었다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "[조선 후기에 유행한 판소리]", translation=
                "판소리, popular in late 조선" "\n\n"
                "판소리 is music in which a singer, keeping to the rhythm of "
                "the 고수 (the drummer), weaves a story by mixing 창 (song), "
                "아니리 (speech) and 너름새 (gesture). The 판 of 판소리, as in "
                "‘씨름판’ and ‘장사판’, refers to a place where many people "
                "have gathered. 판소리, then, means a performance of song "
                "held where many people have gathered." "\n\n"
                "판소리 can be called a performance that the singer and the "
                "audience make together. Following the 추임새 of the drummer, "
                "who keeps the rhythm to the singer’s song and speech, the "
                "audience too add to the excitement with calls such as "
                "‘얼씨구’ and ‘좋지’."),
        VERSE("토끼가 해변가에 도착하여 {산천}으로 쭉 기어 올라가니, {별주부}가 "
              "{기가 막혀|기가 막히다},",
              "“아, 여보시오, 토 선생. 죽겠다 하고 업어다 놓으니까 그렇게 모르는 {체하고|체하다} "
              "가신단 말이오? {간}이나 좀 갖고 오시오.”",
              "토끼가 뒤돌아보더니 욕을 마구 {퍼붓는데|퍼붓다}, “이런 {미련한|미련하다} 놈아, 뱃속에 "
              "달린 간을 어찌 내고 들인단 말이냐? 바다 속 병든 {용왕} 살리자고 {성한|성하다} 토끼 "
              "내가 죽을쏘냐?”",
              translation=
              "When the rabbit reached the shore and went crawling straight "
              "up into the hills, 별주부 was dumbfounded:" "\n\n"
              "“Hey, look here, Mr Rabbit. I carried you here on my back "
              "saying it would kill me, and you mean to go off like that as "
              "if you knew nothing about it? Bring me the liver, at least.”"
              "\n\n"
              "The rabbit looked back and poured out abuse: “You dim-witted "
              "wretch, how do you suppose a liver fixed inside the belly is "
              "taken out and put back in? Am I, a healthy rabbit, to die so "
              "that a sick Dragon King under the sea may live?”"),
        SOURCE("- ‘수궁가’ 중에서 -"),
        FIGURE("병풍 앞에서 부채를 든 소리꾼이 서서 소리를 하고 고수가 돗자리에 앉아 북을 치는 그림"),
        PARAGRAPH("판소리는 {소리꾼}이 {고수}(북 치는 사람)의 {장단}에 맞추어 {창}(노래)과 "
                  "{아니리}(말)과 {너름새}(몸짓)를 섞어 이야기를 {엮어|엮다} 가는 음악이다. 또한 "
                  "판소리의 판이란 ‘{씨름판}’, ‘장사판’과 같이 사람이 많이 모인 곳을 가리킨다. 판소리는 "
                  "많은 사람이 모인 곳에서 열리는 노래 공연을 뜻한다."),
        PARAGRAPH("판소리는 소리꾼과 {청중}이 함께 만들어가는 공연이라고 할 수 있다. 소리꾼의 창과 말에 "
                  "장단을 맞추는 고수의 {추임새}에 따라 청중들도 ‘얼씨구’, ‘좋지’ 등을 하며 {흥}을 "
                  "더한다."),
        PARAGRAPH("★ 자신의 고향 나라에서 {전해 내려오는|전해 내려오다} 전통 공연에 대해 이야기해 "
                  "봅시다. 한국의 판소리와 어떤 점이 비슷하고 어떤 점이 다른지 말해 봅시다.",
                  "Talk about a traditional performance handed down in your "
                  "home country. Say in what ways it is like Korea’s 판소리 "
                  "and in what ways it differs."),
    ],

    extraAnnotations={
        "동상": dict(
            hanja="銅像", meaning="a bronze statue",
            characters=[("銅", "동", "copper, bronze — as in 동메달"),
                        ("像", "상", "an image, a figure — as in 영상, 불상")],
        ),
        "화폐": dict(
            hanja="貨幣", meaning="money, currency (notes and coins)",
            characters=[("貨", "화", "goods, money — as in 화물, 외화"),
                        ("幣", "폐", "currency — as in 지폐")],
            notes=["세종 is on the 10,000-won note."],
        ),
        "대왕": dict(
            hanja="大王", meaning="a great king, “the Great”",
            characters=[("大", "대", "great"),
                        ("王", "왕", "a king")],
        ),
        "존경": dict(
            hanja="尊敬", meaning="respect, esteem",
            characters=[("尊", "존", "to honour — as in 존중, 존댓말"),
                        ("敬", "경", "to respect — as in 경로, 공경")],
        ),
        "성립": dict(
            hanja="成立", meaning="coming into being, establishment",
            characters=[("成", "성", "to become, to achieve — as in 성공, 완성"),
                        ("立", "립", "to stand, to set up — as in 설립, 독립")],
        ),
        "건국": dict(
            hanja="建國", meaning="the founding of a country",
            characters=[("建", "건", "to build — as in 건축, 건설"),
                        ("國", "국", "a country")],
        ),
        "태조": dict(
            hanja="太祖", meaning="태조, “Grand Progenitor”: the title of a "
                                  "dynasty’s founding king",
            characters=[("太", "태", "great, first — as in 태양, 태극"),
                        ("祖", "조", "an ancestor — as in 조상, 조부모")],
            notes=["Here 이성계, who founded 조선. 고려’s founder 왕건 is also "
                   "called 태조."],
        ),
        "분위기": dict(
            hanja="雰圍氣", meaning="atmosphere, mood",
            characters=[("雰", "분", "mist, air"),
                        ("圍", "위", "to surround — as in 주위, 범위"),
                        ("氣", "기", "air, spirit — as in 공기, 기분")],
        ),
        "수도": dict(
            hanja="首都", meaning="a capital city",
            characters=[("首", "수", "head, chief — as in 수석, 수상"),
                        ("都", "도", "a city, a capital — as in 도시")],
        ),
        "경복궁": dict(
            hanja="景福宮", meaning="경복궁, the main royal palace of 조선",
            characters=[("景", "경", "bright, a view — as in 경치, 풍경"),
                        ("福", "복", "blessing — as in 행복, 복지"),
                        ("宮", "궁", "a palace — as in 궁궐")],
        ),
        "종묘": dict(
            hanja="宗廟", meaning="종묘, the royal ancestral shrine of 조선",
            characters=[("宗", "종", "an ancestor, a main line — as in 종교, 세종"),
                        ("廟", "묘", "a shrine")],
        ),
        "비롯하다": dict(
            meaning="to begin with, to include",
            notes=["A를 비롯해 B “B, starting with A”, “A and also B”."],
            surfaces=["비롯해"],
        ),
        "숭례문": dict(
            hanja="崇禮門", meaning="숭례문, the south gate of 한양 (남대문)",
            characters=[("崇", "숭", "to revere — as in 숭배"),
                        ("禮", "례", "propriety, rites — as in 예절, 장례"),
                        ("門", "문", "a gate")],
        ),
        "4대문": dict(
            hanja="四大門", meaning="the four great gates (of 한양)",
            characters=[("四", "사", "four"),
                        ("大", "대", "great"),
                        ("門", "문", "a gate — as in 남대문, 동대문")],
        ),
        "성곽": dict(
            hanja="城郭", meaning="a fortress wall, a walled fortress",
            characters=[("城", "성", "a fortress, a walled town — as in 남한산성"),
                        ("郭", "곽", "an outer wall")],
        ),
        "유교": dict(
            hanja="儒敎", meaning="Confucianism",
            characters=[("儒", "유", "a scholar, Confucian — as in 유학"),
                        ("敎", "교", "teaching — as in 종교, 교육")],
        ),
        "이념": dict(
            hanja="理念", meaning="an ideology, guiding ideas",
            characters=[("理", "이", "reason, principle — as in 이유, 원리"),
                        ("念", "념", "a thought — as in 개념, 기념")],
        ),
        "바탕": dict(
            meaning="a basis, a foundation",
            notes=["…을 바탕으로 “on the basis of …”."],
        ),
        "다스리다": dict(
            meaning="to rule, to govern",
            surfaces=["다스렸다"],
        ),
        "친밀하다": dict(
            hanja="親密하다", meaning="to be close, intimate",
            characters=[("親", "친", "close, a parent — as in 친구, 부친"),
                        ("密", "밀", "dense, close — as in 비밀, 밀접")],
            notes=["The five relations listed here are Confucianism’s 오륜 "
                   "(五倫)."],
            surfaces=["친밀한"],
        ),
        "신하": dict(
            hanja="臣下", meaning="a subject, a minister of the king",
            characters=[("臣", "신", "a minister, a subject"),
                        ("下", "하", "below")],
        ),
        "의리": dict(
            hanja="義理", meaning="loyalty, what one owes in duty",
            characters=[("義", "의", "right, duty — as in 정의, 의무"),
                        ("理", "리", "principle — as in 이념, 원리")],
        ),
        "구별": dict(
            hanja="區別", meaning="distinction",
            characters=[("區", "구", "to divide, a district — as in 구분, 구청"),
                        ("別", "별", "separate — as in 차별, 특별")],
        ),
        "대우": dict(
            hanja="待遇", meaning="treatment (of a person)",
            characters=[("待", "대", "to treat, to wait — as in 기대, 접대"),
                        ("遇", "우", "to meet, to treat — as in 우대")],
        ),
        "권력": dict(
            hanja="權力", meaning="power, authority",
            characters=[("權", "권", "authority, a right — as in 권리, 인권"),
                        ("力", "력", "strength — as in 노력, 능력")],
        ),
        "강화시키다": dict(
            hanja="强化시키다", meaning="to strengthen",
            characters=[("强", "강", "strong — as in 강조, 강제"),
                        ("化", "화", "to become, -isation — as in 변화, 문화")],
            surfaces=["강화시켜"],
        ),
        "기틀": dict(
            meaning="a foundation, a framework",
            notes=["기틀을 마련하다 “to lay the foundation”, as in the "
                   "article’s title."],
        ),
        "호패": dict(
            hanja="號牌", meaning="호패, the identity tag men carried in 조선",
            characters=[("號", "호", "a name, a number — as in 번호, 신호"),
                        ("牌", "패", "a tag, a tablet — as in 명패")],
        ),
        "신분증": dict(
            hanja="身分證", meaning="an identity card",
            characters=[("身", "신", "the body, oneself — as in 신체, 자신"),
                        ("分", "분", "a share, one’s station — as in 부분, 분야"),
                        ("證", "증", "proof, a certificate — as in 증명, 영수증")],
        ),
        "차다": dict(
            meaning="to wear (at the waist or wrist), to carry on one",
            notes=["시계를 차다 “to wear a watch”."],
            surfaces=["차고"],
        ),
        "백성": dict(
            hanja="百姓", meaning="the common people, the king’s subjects",
            characters=[("百", "백", "a hundred"),
                        ("姓", "성", "a family name — as in 성명")],
            notes=["Literally “the hundred surnames”."],
        ),
        "위대하다": dict(
            hanja="偉大하다", meaning="to be great",
            characters=[("偉", "위", "great — as in 위인"),
                        ("大", "대", "great")],
            surfaces=["위대한"],
        ),
        "관리": dict(
            hanja="官吏", meaning="a government official",
            characters=[("官", "관", "an official, office — as in 장관, 경찰관"),
                        ("吏", "리", "a clerk, an official")],
            notes=["Not the 관리 (管理) of 관리하다 “to manage”, which closes "
                   "the paragraph before."],
        ),
        "펴내다": dict(
            meaning="to publish, to bring out (a book)",
            surfaces=["펴냈다"],
        ),
        "측우기": dict(
            hanja="測雨器", meaning="a rain gauge",
            characters=[("測", "측", "to measure — as in 측정, 예측"),
                        ("雨", "우", "rain — as in 우산, 폭우"),
                        ("器", "기", "an instrument — as in 악기, 무기")],
        ),
        "해시계": dict(
            hanja="해時計", meaning="a sundial",
            characters=[("時", "시", "time"),
                        ("計", "계", "to measure, to count — as in 계산, 체온계")],
            notes=["해 “the sun” + 시계 “a clock”."],
        ),
        "물시계": dict(
            hanja="물時計", meaning="a water clock",
            characters=[("時", "시", "time"),
                        ("計", "계", "to measure, to count — as in 계산, 통계")],
        ),
        "훈민정음": dict(
            hanja="訓民正音",
            meaning="훈민정음, “the correct sounds for teaching the people”: "
                    "the original name of 한글",
            characters=[("訓", "훈", "to teach — as in 훈련, 교훈"),
                        ("民", "민", "the people — as in 국민, 서민"),
                        ("正", "정", "correct — as in 정확, 공정"),
                        ("音", "음", "a sound — as in 음악, 발음")],
        ),
        "법전": dict(
            hanja="法典", meaning="a code of law",
            characters=[("法", "법", "law"),
                        ("典", "전", "a canon, a standard work — as in 사전, 고전")],
        ),
        "경국대전": dict(
            hanja="經國大典",
            meaning="경국대전, the basic code of law of 조선",
            characters=[("經", "경", "to manage, to pass through — as in 경제, 경영"),
                        ("國", "국", "a country"),
                        ("大", "대", "great"),
                        ("典", "전", "a canon — as in 법전, 사전")],
            notes=["“The great code for governing the country”."],
        ),
        "군사": dict(
            hanja="軍事", meaning="military affairs",
            characters=[("軍", "군", "an army — as in 군대, 수군"),
                        ("事", "사", "a matter — as in 사건, 행사")],
        ),
        "형벌": dict(
            hanja="刑罰", meaning="punishment, a penalty",
            characters=[("刑", "형", "punishment — as in 형사, 사형"),
                        ("罰", "벌", "a penalty — as in 처벌, 벌금")],
        ),
        "전반": dict(
            hanja="全般", meaning="the whole, every part of",
            characters=[("全", "전", "whole — as in 전체, 안전"),
                        ("般", "반", "a kind, in general — as in 일반")],
        ),
        "담기다": dict(
            meaning="to be contained, to be set down in",
            notes=["The passive of 담다 “to put in”."],
            surfaces=["담겨"],
        ),
        "법치국가": dict(
            hanja="法治國家", meaning="a state under the rule of law",
            characters=[("法", "법", "law"),
                        ("治", "치", "to govern — as in 정치, 통치"),
                        ("國家", None, "a state")],
        ),
        "통치": dict(
            hanja="統治", meaning="rule, government",
            characters=[("統", "통", "to command, to unite — as in 대통령, 통일"),
                        ("治", "치", "to govern — as in 정치, 법치")],
        ),
        "노비": dict(
            hanja="奴婢", meaning="노비, people held in bondage: slaves and "
                                  "servants",
            characters=[("奴", "노", "a male slave"),
                        ("婢", "비", "a female slave")],
        ),
        "출산 휴가": dict(
            hanja="出産休暇", meaning="maternity leave",
            characters=[("出産", None, "childbirth — 出 to come out, 産 to bear"),
                        ("休暇", None, "leave, a holiday — 休 to rest, 暇 free "
                                       "time")],
        ),
        "침략하다": dict(
            hanja="侵略하다", meaning="to invade",
            characters=[("侵", "침", "to encroach — as in 침해, 침입"),
                        ("略", "략", "to seize, to abridge — as in 전략, 생략")],
            surfaces=["침략한"],
        ),
        "임진왜란": dict(
            hanja="壬辰倭亂",
            meaning="the 임진왜란, the Japanese invasion of 1592",
            characters=[("壬辰", None, "임진, the name of the year 1592 in the "
                                       "sixty-year cycle"),
                        ("倭", "왜", "the old name for Japan"),
                        ("亂", "란", "a disturbance, a war — as in 혼란, 전란")],
        ),
        "수군": dict(
            hanja="水軍", meaning="a navy (the old word)",
            characters=[("水", "수", "water"),
                        ("軍", "군", "an army — as in 해군, 군대")],
        ),
        "막아내다": dict(
            meaning="to hold off, to fend off",
            surfaces=["막아냈고"],
        ),
        "의병": dict(
            hanja="義兵", meaning="a righteous army, volunteers who rise to "
                                  "defend the country",
            characters=[("義", "의", "right, duty — as in 의리, 정의"),
                        ("兵", "병", "a soldier — as in 병사, 병역")],
        ),
        "조직하다": dict(
            hanja="組織하다", meaning="to organise, to form",
            characters=[("組", "조", "to put together — as in 조합"),
                        ("織", "직", "to weave — as in 직물")],
            surfaces=["조직하여"],
        ),
        "맞서다": dict(
            meaning="to stand against, to confront",
            surfaces=["맞서"],
        ),
        "청나라": dict(
            hanja="淸나라", meaning="the Qing dynasty of China",
            characters=[("淸", "청", "clear, pure — as in 청소, 청결")],
        ),
        "병자호란": dict(
            hanja="丙子胡亂",
            meaning="the 병자호란, the Qing invasion of 1636",
            characters=[("丙子", None, "병자, the name of the year 1636 in the "
                                       "sixty-year cycle"),
                        ("胡", "호", "the northern peoples; here the Qing"),
                        ("亂", "란", "a disturbance, a war — as in 임진왜란")],
        ),
        "남한산성": dict(
            hanja="南漢山城",
            meaning="남한산성, the mountain fortress south-east of Seoul",
            characters=[("南", "남", "south"),
                        ("漢", "한", "한, as in 한강, 한양"),
                        ("山", "산", "a mountain"),
                        ("城", "성", "a fortress — as in 성곽, 화성")],
        ),
        "농토": dict(
            hanja="農土", meaning="farmland",
            characters=[("農", "농", "farming — as in 농사, 농업"),
                        ("土", "토", "soil, land — as in 토지, 국토")],
        ),
        "망가지다": dict(
            meaning="to be ruined, to be wrecked",
            surfaces=["망가졌고"],
        ),
        "극복하다": dict(
            hanja="克服하다", meaning="to overcome",
            characters=[("克", "극", "to overcome"),
                        ("服", "복", "to submit; clothes — as in 복종, 한복")],
            surfaces=["극복하기"],
        ),
        "안정시키다": dict(
            hanja="安定시키다", meaning="to steady, to stabilise",
            characters=[("安", "안", "peaceful — as in 안전, 안심"),
                        ("定", "정", "to settle — as in 결정, 일정")],
            surfaces=["안정시켰고"],
        ),
        "상업": dict(
            hanja="商業", meaning="commerce, trade",
            characters=[("商", "상", "trade — as in 상인, 상품"),
                        ("業", "업", "work, an industry — as in 농업, 직업")],
        ),
        "공업": dict(
            hanja="工業", meaning="industry, manufacture",
            characters=[("工", "공", "to make, a craft — as in 공장, 공사"),
                        ("業", "업", "work, an industry — as in 상업, 농업")],
        ),
        "학문": dict(
            hanja="學問", meaning="learning, scholarship",
            characters=[("學", "학", "to learn — as in 학교, 학자"),
                        ("問", "문", "to ask — as in 질문, 문의")],
            notes=["The scholars meant are those of 실학 (實學), “practical "
                   "learning”."],
        ),
        "기여하다": dict(
            hanja="寄與하다", meaning="to contribute",
            characters=[("寄", "기", "to entrust, to send — as in 기부, 기숙사"),
                        ("與", "여", "to give — as in 참여, 수여")],
            surfaces=["기여하였다"],
        ),
        "세계유산": dict(
            hanja="世界遺産", meaning="World Heritage",
            characters=[("世界", None, "the world"),
                        ("遺", "유", "to leave behind — as in 유물, 유언"),
                        ("産", "산", "property, to produce — as in 재산, 생산")],
        ),
        "건축물": dict(
            hanja="建築物", meaning="a building, a piece of architecture",
            characters=[("建", "건", "to build — as in 건국, 건설"),
                        ("築", "축", "to construct — as in 신축"),
                        ("物", "물", "a thing — as in 물건, 건물")],
        ),
        "수원 화성": dict(
            hanja="水原華城",
            meaning="수원 화성, the fortress 정조 built at 수원",
            characters=[("水原", None, "수원, the city south of Seoul"),
                        ("華", "화", "splendid, flowering — as in 화려"),
                        ("城", "성", "a fortress — as in 성곽, 남한산성")],
        ),
        "신분": dict(
            hanja="身分", meaning="social status, one’s station",
            characters=[("身", "신", "the body, oneself — as in 신체, 자신"),
                        ("分", "분", "a share, one’s station — as in 부분, 분야")],
        ),
        "양반": dict(
            hanja="兩班", meaning="양반, the ruling class of 조선",
            characters=[("兩", "양", "both, two — as in 양쪽, 양국"),
                        ("班", "반", "a rank, a group — as in 반장")],
            notes=["Literally “the two ranks”: the civil and the military "
                   "officials."],
        ),
        "중인": dict(
            hanja="中人", meaning="중인, the “middle people”: technical "
                                  "officials",
            characters=[("中", "중", "middle"),
                        ("人", "인", "a person")],
        ),
        "상민": dict(
            hanja="常民", meaning="상민, commoners",
            characters=[("常", "상", "ordinary, usual — as in 일상, 정상"),
                        ("民", "민", "the people — as in 국민, 서민")],
        ),
        "천민": dict(
            hanja="賤民", meaning="천민, the lowest class",
            characters=[("賤", "천", "lowly, mean — as in 천하다"),
                        ("民", "민", "the people — as in 상민, 국민")],
        ),
        "지배층": dict(
            hanja="支配層", meaning="the ruling class",
            characters=[("支", "지", "to hold up, to control — as in 지원, 지지"),
                        ("配", "배", "to allot — as in 배달, 분배"),
                        ("層", "층", "a layer, a class — as in 계층, 고층")],
        ),
        "과거": dict(
            hanja="科擧", meaning="과거, the state examination for officials",
            characters=[("科", "과", "a subject, a branch — as in 과목, 과학"),
                        ("擧", "거", "to raise, to select — as in 선거")],
            notes=["Not 과거 (過去) “the past”."],
        ),
        "글공부": dict(
            hanja="글工夫", meaning="book learning, study of letters",
            characters=[("工", "공", "work, a craft — as in 공업, 공사"),
                        ("夫", "부", "a man — as in 부부, 농부")],
            notes=["글 “writing” + 공부 “study”."],
        ),
        "힘쓰다": dict(
            meaning="to devote oneself to, to work hard at",
            surfaces=["힘썼다"],
        ),
        "수공업자": dict(
            hanja="手工業者", meaning="a craftsman, an artisan",
            characters=[("手", "수", "the hand — as in 수건, 수당"),
                        ("工業", None, "industry, manufacture"),
                        ("者", "자", "a person")],
        ),
        "백정": dict(
            hanja="白丁", meaning="백정, a butcher (of the lowest class)",
            characters=[("白", "백", "white"),
                        ("丁", "정", "an adult man")],
        ),
        "천하다": dict(
            hanja="賤하다", meaning="to be lowly, mean",
            characters=[("賤", "천", "lowly, mean — as in 천민")],
            surfaces=["천하고"],
        ),
        "후기": dict(
            hanja="後期", meaning="the later period",
            characters=[("後", "후", "after — as in 오후, 이후"),
                        ("期", "기", "a period — as in 기간, 시기")],
        ),
        "신분제": dict(
            hanja="身分制", meaning="the status system",
            characters=[("身", "신", "the body, oneself"),
                        ("分", "분", "a share, one’s station"),
                        ("制", "제", "a system — as in 제도, 규제")],
        ),
        "점차": dict(
            hanja="漸次", meaning="gradually",
            characters=[("漸", "점", "little by little — as in 점점"),
                        ("次", "차", "next, an order — as in 차례, 목차")],
        ),
        "평등하다": dict(
            hanja="平等하다", meaning="to be equal",
            characters=[("平", "평", "level, even — as in 평화, 공평"),
                        ("等", "등", "a grade, equal — as in 등급, 동등")],
            surfaces=["평등한"],
        ),
        "전기": dict(
            hanja="前期", meaning="the earlier period",
            characters=[("前", "전", "before — as in 오전, 이전"),
                        ("期", "기", "a period — as in 후기, 기간")],
            notes=["Not 전기 (電氣) “electricity”."],
        ),
        "판소리": dict(
            meaning="판소리, a long story sung by one singer to a drum",
            notes=["판 “a place where people gather” + 소리 “sound, song”, as "
                   "the 이야기 나누기 explains."],
        ),
        "탈놀이": dict(
            meaning="a masked dance-drama",
            notes=["탈 “a mask” + 놀이 “play”."],
        ),
        "민화": dict(
            hanja="民畫", meaning="folk painting",
            characters=[("民", "민", "the people — as in 서민, 국민"),
                        ("畫", "화", "a picture — as in 화가, 영화")],
        ),
        "서민": dict(
            hanja="庶民", meaning="ordinary people, the common people",
            characters=[("庶", "서", "many, common"),
                        ("民", "민", "the people — as in 국민, 민화")],
        ),
        "예상": dict(
            hanja="豫想", meaning="expectation, an estimate",
            characters=[("豫", "예", "beforehand — as in 예약, 예방"),
                        ("想", "상", "to think — as in 상상, 사상")],
        ),
        "공사": dict(
            hanja="工事", meaning="building work, construction",
            characters=[("工", "공", "to make, a craft — as in 공업, 공장"),
                        ("事", "사", "a matter, work — as in 군사, 행사")],
        ),
        "비결": dict(
            hanja="祕訣", meaning="a secret, the key (to doing something)",
            characters=[("祕", "비", "secret — as in 비밀, 신비"),
                        ("訣", "결", "a knack, a parting")],
        ),
        "대가": dict(
            hanja="代價", meaning="payment in return, a price",
            characters=[("代", "대", "in place of — as in 대신, 대리"),
                        ("價", "가", "a price — as in 가격, 물가")],
        ),
        "일꾼": dict(
            meaning="a worker, a labourer",
            notes=["일 “work” + 꾼, one who does it — as in 소리꾼."],
        ),
        "모집하다": dict(
            hanja="募集하다", meaning="to recruit",
            characters=[("募", "모", "to call for — as in 공모, 모금"),
                        ("集", "집", "to gather — as in 집단, 수집")],
            surfaces=["모집하여"],
        ),
        "임금": dict(
            hanja="賃金", meaning="wages",
            characters=[("賃", "임", "hire, rent — as in 임대"),
                        ("金", "금", "money — as in 요금, 세금")],
            notes=["Not the native word 임금 “a king”."],
        ),
        "품삯": dict(
            meaning="pay for a day’s labour, wages",
            notes=["품 “labour” + 삯 “a fee”."],
        ),
        "지급하다": dict(
            hanja="支給하다", meaning="to pay out, to provide",
            characters=[("支", "지", "to pay out, to hold up — as in 지출, 지원"),
                        ("給", "급", "to give — as in 월급, 공급")],
            surfaces=["지급하였다"],
        ),
        "무덥다": dict(
            meaning="to be sweltering, hot and humid",
            surfaces=["무더울"],
        ),
        "성과": dict(
            hanja="成果", meaning="results, an achievement",
            characters=[("成", "성", "to achieve — as in 성립, 성공"),
                        ("果", "과", "fruit, a result — as in 결과, 효과")],
        ),
        "수당": dict(
            hanja="手當", meaning="an allowance (on top of wages)",
            characters=[("手", "수", "the hand — as in 수공업"),
                        ("當", "당", "to fall to, fitting — as in 당연, 해당")],
        ),
        "잔치": dict(meaning="a feast, a party"),
        "격려": dict(
            hanja="激勵", meaning="encouragement",
            characters=[("激", "격", "fierce, to stir — as in 감격, 급격"),
                        ("勵", "려", "to urge on — as in 장려")],
        ),
        "도르래": dict(meaning="a pulley"),
        "원리": dict(
            hanja="原理", meaning="a principle",
            characters=[("原", "원", "origin — as in 원래, 원인"),
                        ("理", "리", "reason, principle — as in 이념, 의리")],
        ),
        "거중기": dict(
            hanja="擧重機", meaning="거중기, the crane used to build 화성",
            characters=[("擧", "거", "to raise — as in 과거, 선거"),
                        ("重", "중", "heavy — as in 중요, 체중"),
                        ("機", "기", "a machine — as in 기계, 비행기")],
            notes=["“The machine that lifts heavy things”."],
        ),
        "단축": dict(
            hanja="短縮", meaning="shortening",
            characters=[("短", "단", "short — as in 장단, 단점"),
                        ("縮", "축", "to shrink — as in 축소, 압축")],
        ),
        "산천": dict(
            hanja="山川", meaning="hills and streams, the land",
            characters=[("山", "산", "a mountain"),
                        ("川", "천", "a stream — as in 하천")],
        ),
        "별주부": dict(
            hanja="鼈主簿", meaning="별주부, “Clerk Terrapin”: the terrapin of "
                                    "the tale",
            characters=[("鼈", "별", "a terrapin"),
                        ("主簿", None, "주부, the title of a minor official")],
            notes=["In 수궁가 the terrapin is sent to fetch a rabbit’s liver "
                   "to cure the Dragon King."],
        ),
        "기가 막히다": dict(
            hanja="氣가 막히다", meaning="to be dumbfounded, at a loss for words",
            characters=[("氣", "기", "breath, spirit — as in 분위기, 공기")],
            notes=["Literally “one’s breath is blocked”."],
            surfaces=["기가 막혀"],
        ),
        "체하다": dict(
            meaning="to pretend, to make as if",
            notes=["모르는 체하다 “to pretend not to know”."],
            surfaces=["체하고"],
        ),
        "간": dict(
            hanja="肝", meaning="the liver",
            characters=[("肝", "간", "the liver")],
        ),
        "퍼붓다": dict(
            meaning="to pour down, to heap (abuse) on",
            notes=["욕을 퍼붓다 “to heap abuse on someone”."],
            surfaces=["퍼붓는데"],
        ),
        "미련하다": dict(
            meaning="to be dim-witted, foolish",
            surfaces=["미련한"],
        ),
        "용왕": dict(
            hanja="龍王", meaning="the Dragon King (ruler of the sea)",
            characters=[("龍", "용", "a dragon"),
                        ("王", "왕", "a king")],
        ),
        "성하다": dict(
            meaning="to be sound, healthy, undamaged",
            surfaces=["성한"],
        ),
        "소리꾼": dict(
            meaning="a singer (of 판소리)",
            notes=["소리 “song” + 꾼, one who does it."],
        ),
        "고수": dict(
            hanja="鼓手", meaning="a drummer",
            characters=[("鼓", "고", "a drum"),
                        ("手", "수", "the hand; one who does — as in 가수, 선수")],
        ),
        "장단": dict(
            hanja="長短", meaning="rhythm, a rhythmic pattern",
            characters=[("長", "장", "long — as in 성장, 장점"),
                        ("短", "단", "short — as in 단축, 단점")],
            notes=["Literally “long and short”."],
        ),
        "창": dict(
            hanja="唱", meaning="song, the sung part of 판소리",
            characters=[("唱", "창", "to sing — as in 합창")],
        ),
        "아니리": dict(meaning="the spoken part of 판소리"),
        "너름새": dict(meaning="the singer’s gestures in 판소리"),
        "엮다": dict(
            meaning="to weave, to put together",
            surfaces=["엮어"],
        ),
        "씨름판": dict(
            meaning="a 씨름 (wrestling) ground, with its crowd",
        ),
        "청중": dict(
            hanja="聽衆", meaning="an audience",
            characters=[("聽", "청", "to listen — as in 시청, 청취"),
                        ("衆", "중", "a crowd — as in 대중, 관중")],
        ),
        "추임새": dict(
            meaning="the calls of encouragement the drummer puts in",
            notes=["얼씨구 and 좋지 are such calls."],
        ),
        "흥": dict(
            hanja="興", meaning="excitement, high spirits",
            characters=[("興", "흥", "to rise, delight — as in 흥미")],
        ),
        "전해 내려오다": dict(
            hanja="傳해 내려오다", meaning="to be handed down",
            characters=[("傳", "전", "to hand on — as in 전통, 전달")],
            surfaces=["전해 내려오는"],
        ),
    },

    extraNotes=[
        "The statue photograph on p. 212, the 호패 and 『경국대전』 photographs "
        "on p. 213, the 남한산성, 탈놀이, 수원 화성 and 거중기 photographs on "
        "p. 214 and the 판소리 painting on p. 215 are not reproduced; their "
        "captions are. The 남한산성 photograph and the painting have none in "
        "the book.",
        "The map of the eight provinces on p. 213 is set as its caption and "
        "the names printed on it.",
        "The three provisions of the 『경국대전』 on p. 213 are printed with a "
        "middle dot before each; they are set as a list.",
        "The 수궁가 passage on p. 215 is set by speaker, three lines, where "
        "the book runs it over five.",
        "The review gaps on p. 215 are blank in the book and left blank here.",
    ],
)
