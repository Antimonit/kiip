# -*- coding: utf-8 -*-
"""Chapter 43 — Korea's historical figures.

Transcribed from the photos of pp. 220-223. The pages carry no handwriting.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, FIGURE, LABELS, VERSE,
               TABLE, CELL, GLOSSARY)

CHAPTER = dict(
    number=43, slug="43-historical-figures",
    unit="역사", title="한국의 역사 인물", titleEn="Korea’s historical figures",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 서울 광화문 사거리에 있는 어떤 인물의 {동상}과 그가 {지휘했던|지휘하다} 배의 "
                  "{모형}입니다.",
                  "Below are the statue of a certain figure that stands at "
                  "the Gwanghwamun crossroads in Seoul, and a model of the "
                  "ship he commanded."),
        FIGURE("갑옷을 입고 칼을 짚고 선 장군의 동상 사진 · 지붕을 덮은 배의 모형 사진"),
        HEADING(4, "01 이 인물의 직업은 무엇이었을까요? 그가 지휘했던 배는 어떤 동물의 모양을 "
                   "{본떠|본뜨다} 만든 것일까요?",
                translation="What was this figure’s occupation? The ship he "
                            "commanded was modelled on the shape of which "
                            "animal?"),
        HEADING(4, "02 동상의 인물은 이 배를 이용해 어떤 일을 했을까요?",
                translation="What did the figure of the statue do with this "
                            "ship?"),

        SECTION("goals", "학습목표"),
        BULLET("한국을 {위기}에서 {구한|구하다} 사람들에 대해 설명할 수 있다.", ordered=True,
               translation="Explain who the people were who saved Korea "
                           "from crisis."),
        BULLET("한국 역사에서 여성들의 활동에 대해 설명할 수 있다.", ordered=True,
               translation="Explain what women did in Korean history."),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"],
              [["기본", "역사", "41. 조선의 건국과 발전", "임진왜란"]]),

        SECTION("part", "01 국가를 위기에서 구한 사람들에는 누가 있을까?"),
        HEADING(2, "수나라 대군을 물리친 고구려의 을지문덕", translation=
                "을지문덕 of 고구려, who drove off the great army of Sui" "\n\n"
                "China’s Sui invaded 고구려 at the head of a great army of "
                "1,130,000 men. When it picked 300,000 of them and set out "
                "to attack Pyongyang, the capital of 고구려, the 고구려 general "
                "을지문덕 drew the Sui army in close to Pyongyang by pretending "
                "on purpose to be losing. The 고구려 army, which had waited "
                "until the Sui army was crossing the middle of the 살수 (the "
                "Cheongcheon river), burst all at once the dam it had put "
                "across the river beforehand and routed the Sui army."),
        PARAGRAPH("중국의 {수나라}가 113만 명의 큰 {군대}를 {이끌고|이끌다} 고구려에 "
                  "{쳐들어왔다|쳐들어오다}. 그중 30만 명을 뽑아 고구려의 수도 평양을 "
                  "{공격하려고|공격하다} 하자 고구려의 {장군} {을지문덕}은 {일부러} {패하는|패하다} "
                  "{척하며|척하다} 수나라 군대를 평양 가까이로 {끌어들였다|끌어들이다}. 수나라 군대가 "
                  "{살수}(청천강)의 가운데를 건너갈 때까지 기다리던 고구려군은 미리 막아 두었던 강의 "
                  "{둑}을 {한꺼번에} {터뜨려|터뜨리다} 수나라 군대를 크게 {물리쳤다|물리치다}."),
        FIGURE("살수 대첩(민족 기록화, 전쟁 기념관)"),

        HEADING(2, "외교로 나라를 구한 고려의 서희", translation=
                "서희 of 고려, who saved the country by diplomacy" "\n\n"
                "The 거란 (Khitan), who were to the north of the Korean "
                "peninsula, came down and demanded that 고려 give up its "
                "northern land and that it have no dealings with China’s "
                "Song. The officials of 고려 said that, as the 거란 army was "
                "very strong, they should cede the land and avoid a war. At "
                "this point 서희 came forward and met the 거란 general. 서희 "
                "knew that the 거란 had a war with Song ahead of them and so "
                "could not put their whole strength into invading 고려. "
                "Without fighting, 서희 was able to stave off the war through "
                "diplomacy, and what is more to take the land as far as the "
                "east of the Amnok river."),
        PARAGRAPH("{한반도} 북쪽에 있던 {거란}이 내려와서 고려의 북쪽 땅을 {내놓을|내놓다} 것, 중국의 "
                  "{송나라}와 {교류하지|교류하다} 말 것을 요구하였다. 고려의 {관리}들은 거란의 군대가 "
                  "매우 강하니 땅을 {떼어 주어|떼어 주다} 전쟁을 피하자고 하였다. 이때 {서희}가 "
                  "{나서서|나서다} 거란의 장군을 만났다. 서희는 거란이 송나라와 전쟁을 "
                  "{앞두고|앞두다} 있어서 고려 {침략}에 온 힘을 {쏟을|쏟다} 수 없다는 것을 알고 "
                  "있었다. 서희는 싸우지 않고도 {외교}를 통해 전쟁을 {막아냈고|막아내다} {오히려} "
                  "{압록강} 동쪽 땅까지 {차지할|차지하다} 수 있었다."),
        FIGURE("거란의 침입과 서희의 외교 담판으로 얻은 지역 (지도)"),
        LABELS("거란(요)", "여진", "고려", "서희의 외교 담판으로 얻은 지역", "흥화진", "용주",
               "철주", "통주", "귀주", "곽주", "서희의 외교 담판 (993)",
               "강감찬의 귀주 대첩 (1019)"),
        VERSE("서희: 고려는 고구려의 {후손}이라는 뜻에서 나라 이름을 고려라 하였소. 거란이 옛 고구려 "
              "땅에 살고 있으니 그 땅을 우리에게 내놓아야 할 것이오.",
              "거란의 장군: 그런데 고려는 왜 가까이 있는 우리 거란은 멀리하면서 바다 건너에 있는 "
              "송나라하고 {사귀는|사귀다} 것이오?",
              "서희: 그것은 {여진족}이 {가로막고|가로막다} 있기 때문이오. 거란이 압록강 동쪽의 땅을 "
              "고려에 준다면 거란과 고려가 쉽게 교류할 수 있소.",
              translation=
              "서희: 고려 took the name 고려 to mean that it is the descendant "
              "of 고구려. As the 거란 are living on the old land of 고구려, it is "
              "you who ought to give that land up to us." "\n\n"
              "The 거란 general: Then why does 고려 keep us 거란, who are close "
              "by, at a distance, while it befriends Song across the sea?"
              "\n\n"
              "서희: That is because the 여진 people stand in the way. If the "
              "거란 give 고려 the land east of the Amnok river, the 거란 and 고려 "
              "can easily have dealings with each other."),

        HEADING(2, "일본군을 물리친 조선의 이순신", translation=
                "이순신 of 조선, who drove off the Japanese army" "\n\n"
                "Early in the 임진왜란 the army of 조선 was heavily defeated in "
                "a number of battles. The navy of 조선 led by 이순신, on the "
                "other hand, won great victories in place after place. The "
                "Japanese navy meant to carry weapons and provisions to the "
                "Japanese army, but 이순신, using outstanding tactics and "
                "weapons such as the 거북선 (turtle ship) and cannon, brought "
                "every battle fought with the Japanese forces at sea to "
                "victory. What 이순신 did changed the mood of a war that was "
                "going against 조선 at the time of the 임진왜란, and played a "
                "great part in making the Japanese forces withdraw at last."),
        PARAGRAPH("{임진왜란} 초기에 조선의 {육군}은 여러 {전투}에서 크게 패하였다. 반면 {이순신}이 "
                  "이끈 조선 {수군}({해군})은 {곳곳}에서 큰 {승리}를 {거두었다|거두다}. 일본 수군은 "
                  "일본 육군에게 {무기}와 {식량}을 전해 주려고 했으나 이순신은 {뛰어난|뛰어나다} "
                  "{전술}과 {거북선}, {화포} 등의 무기를 사용하여 일본군과 바다에서 {벌인|벌이다} "
                  "전투를 모두 승리로 이끌었다. 이순신의 {활약}은 임진왜란 당시 조선에게 "
                  "{불리했던|불리하다} 전쟁 분위기를 바꾸고 {마침내} 일본군이 "
                  "{물러나도록|물러나다} 하는데 큰 역할을 하였다."),
        FIGURE("거북선(복원 모형)"),

        SECTION("part", "02 한국 역사에서 여성들은 어떤 활동을 했을까?"),
        HEADING(2, "조선을 대표하는 여성 시인, 허난설헌", translation=
                "허난설헌, the woman poet who stands for 조선" "\n\n"
                "허난설헌 was the elder sister of 허균, who wrote the novel in "
                "한글 『홍길동전』, and from an early age she had a fine gift for "
                "writing and composed poetry well. But the people of 조선 at "
                "the time did not look kindly on women of outstanding talent "
                "being active in society. Her husband and her mother-in-law "
                "were the same. 허난설헌, sick at heart from an unhappy married "
                "life and from the deaths of her own father and her two "
                "children among other things, died at the age of 27. "
                "Afterwards 허균, who felt his sister’s talent had gone to "
                "waste, gathered her poems and made them into a book. Her "
                "poems were highly thought of in China and Japan and became "
                "very popular."),
        PARAGRAPH("{허난설헌}은 한글 소설 『{홍길동전}』을 지은 {허균}의 누나로, 어려서부터 {글재주}가 "
                  "훌륭해서 {시}를 잘 지었다. 그러나 당시 조선 사람들은 {재능}이 뛰어난 여성들이 "
                  "{사회활동}을 하는 것을 좋게 {여기지|여기다} 않았다. 남편과 시어머니도 "
                  "{마찬가지}였다. {불행한|불행하다} 결혼 생활, {친정} 아버지와 두 자녀의 죽음 "
                  "등으로 마음의 병을 얻은 허난설헌은 27세에 {세상을 떠났다|세상을 떠나다}. 이후 "
                  "누나의 재능을 {아까워한|아까워하다} 허균은 누나의 시를 모아 책으로 만들었다. "
                  "그녀의 시는 중국과 일본에서 높은 {평가}를 받고 큰 인기를 얻었다."),
        FIGURE("허난설헌 초상"),
        FIGURE("『난설헌집』(오죽헌 시립 박물관) — 허난설헌의 시를 모아 만든 책이다."),

        HEADING(2, "재산을 모아 제주도 백성을 구한 상인, 김만덕", translation=
                "김만덕, the merchant who built a fortune and saved the people "
                "of Jeju" "\n\n"
                "김만덕, born on Jeju in the 조선 period, lost her parents young "
                "and had a hard life. Later 김만덕 went into trade and made a "
                "great deal of money. Then a severe famine year came to Jeju "
                "and many people were on the point of starving to death, so "
                "김만덕 bought rice with the money she had saved until then "
                "and shared it out among the people. Word that 김만덕 had "
                "saved the people of Jeju reached even 정조. 정조 praised her "
                "good deed and asked what she wished for. 김만덕, who was of "
                "low status, answered, “I should like to go to Seoul and look "
                "upon the place where the king is, and to go to 금강산, which "
                "boasts such outstanding scenery,” and with 정조’s help she "
                "had her wish. Even now Jeju has set up the ‘만덕상’ and gives "
                "a prize every year to people who, like 김만덕, have done much "
                "good for others."),
        GLOSSARY(("흉년", "농사가 잘 되지 않은 해", "흉년",
                  dict(en="a year in which the farming has not gone well"))),
        PARAGRAPH("조선 시대 제주도에서 태어난 {김만덕}은 어려서 부모를 잃고 힘들게 살았다. 이후 "
                  "김만덕은 장사를 하여 {큰돈}을 모았다. 그러던 중 제주도에 심한 {흉년}이 들어 많은 "
                  "사람이 {굶어|굶다} 죽게 되자 김만덕은 그동안 모은 돈으로 쌀을 사서 사람들에게 "
                  "나누어 주었다. 김만덕이 제주도 {백성}을 구한 일은 {정조}에게까지 알려졌다. 정조는 "
                  "그녀의 착한 행동을 칭찬하며 {소원}을 물어보았다. 낮은 {신분}이었던 김만덕은 "
                  "“서울에 가서 {임금}이 계신 곳을 바라보고, {빼어난|빼어나다} {경치}를 자랑하는 "
                  "{금강산}에 가보고 싶습니다.”라고 답했고 정조의 도움으로 소원을 "
                  "{이루었다|이루다}. 지금도 제주도에서는 ‘{만덕상}’을 만들어 김만덕처럼 {선행}을 "
                  "많이 {베푼|베풀다} 사람들에게 {해마다} 상을 주고 있다."),
        FIGURE("김만덕의 선행을 기념하는 행사 포스터 — ‘김만덕주간 나눔 큰잔치’"),

        HEADING(2, "3·1 운동 당시 한국의 독립을 외친 독립운동가, 유관순", translation=
                "유관순, the independence activist who cried out for Korea’s "
                "independence at the time of the 3·1 운동" "\n\n"
                "When the 3·1 운동 calling for Korea’s independence broke out "
                "in 1919, 유관순, then a student at 이화학당, took part in the "
                "movement with her friends. To stop the students taking part, "
                "the Japanese authorities shut the school’s gates. 유관순 then "
                "went down to her home town (Cheonan) and started a 만세 "
                "demonstration, and many people joined it. Arrested by the "
                "Japanese police in the end, 유관순 spoke out boldly to the "
                "Japanese judge in the courtroom. “You killed my father and "
                "my mother, so it is you who have committed the crime. You "
                "have no standing to try us.” Afterwards 유관순 carried on the "
                "만세 demonstrations even while shut up in 서대문 형무소, and met "
                "her death at the age of 19 from the violence of the Japanese "
                "police and from malnutrition."),
        PARAGRAPH("1919년 한국의 {독립}을 {외치는|외치다} {3·1 운동}이 일어나자 당시 {이화학당} "
                  "학생이었던 유관순은 친구들과 함께 운동에 {참여하였다|참여하다}. {일제}는 학생들의 "
                  "참여를 막기 위해 학교의 문을 닫아 버렸다. 그러자 유관순은 고향(천안)에 내려가 "
                  "{만세 운동}을 벌였고 많은 사람들이 여기에 참여하였다. 결국 일본 경찰에 "
                  "{체포된|체포되다} 유관순은 {재판정}에서 일본 판사에게 {당당하게|당당하다} 말했다. "
                  "“너희가 내 아버지와 어머니를 죽였으니 {죄}를 지은 사람은 바로 너희다. 너희는 "
                  "우리를 재판할 {자격}이 없다.” 이후 유관순은 {서대문 형무소}에서 "
                  "{갇혀|갇히다} 있으면서도 만세 운동을 {펼치다가|펼치다} 일본 경찰의 {폭행}과 "
                  "{영양 부족}으로 19세의 나이에 죽음을 {맞이하였다|맞이하다}."),
        FIGURE("유관순 — 서대문 형무소에 갇혀 있을 때의 모습"),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 국가를 위기에서 구한 사람들에는 누가 있을까?"),
        BULLET("고구려의 (        )은 중국 수나라의 침입을 살수(청천강)에서 크게 물리쳤다."),
        BULLET("(        )는 서희의 외교 덕분에 거란의 침입을 물리치고 압록강 동쪽의 땅까지 "
               "차지하였다."),
        BULLET("조선의 (        )은 임진왜란 당시 수군을 이끌고 일본의 침입을 막아냈다."),
        HEADING(3, "02 한국 역사에서 여성들은 어떤 활동을 했을까?"),
        BULLET("조선 시대 허균의 누나인 (        )의 시를 모은 책은 중국과 일본에서 큰 인기를 "
               "얻었다."),
        BULLET("(        )은 자신이 모은 재산을 내놓아 큰 흉년으로 어려움을 겪던 제주도의 백성을 "
               "구했다."),
        BULLET("3·1 운동 당시 이화학당 학생이었던 (        )은 고향에 내려가 만세 운동을 벌였다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "[한국의 지폐에 있는 여러 인물들]", translation=
                "[The figures on Korea’s banknotes]" "\n\n"
                "The figures who appear on Korea’s banknotes are, "
                "respectively, 이황 (the 1,000-won note), 이이 (the 5,000-won "
                "note), 세종 (the 10,000-won note) and 신사임당 (the 50,000-won "
                "note). 이황 and 이이 were outstanding scholars of 조선 who "
                "contributed to the development of Confucian learning. 세종, "
                "the fourth king of 조선, made 훈민정음, which is called 한글 "
                "today, and put his efforts into the advance of culture, "
                "having various scientific instruments made and so on. 신사임당 "
                "had a talent for painting from an early age and, being "
                "steadily educated, was a woman of great learning. After her "
                "marriage she brought her children up admirably, and 이이 is "
                "one of them."),
        FIGURE("천원 · 오천원 · 만원 · 오만원 지폐"),
        PARAGRAPH("한국의 {지폐}에 {등장하는|등장하다} 인물은 각각 {이황}(1,000원권), "
                  "{이이}(5,000원권), {세종}(10,000원권), {신사임당}(50,000원권)이다. 이황과 "
                  "이이는 조선의 뛰어난 {학자}로 {유학}의 {발달}에 {기여하였다|기여하다}. 세종은 "
                  "조선의 네 번째 왕으로 오늘날 한글이라고 불리는 {훈민정음}을 만들었으며, 여러 과학 "
                  "{기구}를 만드는 등 문화 발전에 힘을 쏟았다. 신사임당은 어려서부터 그림에 재능이 "
                  "있었고 {꾸준히} 교육을 받아 {학식}이 높았다. 결혼 후에는 자녀들을 훌륭하게 "
                  "키웠는데 이이도 그중 한 명이다."),
        PARAGRAPH("★ 자신의 고향 나라에서 사용되는 {화폐} 속 인물에 대해 이야기해 봅시다. 그들의 "
                  "{업적}과 활동을 소개해 봅시다.",
                  "Talk about the figures on the money used in your home "
                  "country. Introduce what they achieved and what they did."),
    ],

    extraAnnotations={
        "동상": dict(
            hanja="銅像", meaning="a bronze statue",
            characters=[("銅", "동", "copper, bronze — as in 동메달"),
                        ("像", "상", "an image, a figure — as in 초상, 영상")],
        ),
        "지휘하다": dict(
            hanja="指揮하다", meaning="to command, to direct",
            characters=[("指", "지", "a finger, to point — as in 지시, 지도"),
                        ("揮", "휘", "to wave, to wield — as in 발휘")],
            surfaces=["지휘했던"],
        ),
        "모형": dict(
            hanja="模型", meaning="a model, a replica",
            characters=[("模", "모", "a pattern, to copy — as in 모양, 규모"),
                        ("型", "형", "a mould, a type — as in 유형, 대형")],
        ),
        "본뜨다": dict(
            meaning="to model on, to copy the form of",
            notes=["본 (本) “a pattern” + 뜨다 “to take off, to copy”."],
            surfaces=["본떠"],
        ),
        "위기": dict(
            hanja="危機", meaning="a crisis",
            characters=[("危", "위", "dangerous — as in 위험"),
                        ("機", "기", "a moment, a mechanism — as in 기회, 계기")],
        ),
        "구하다": dict(
            hanja="救하다", meaning="to save, to rescue",
            characters=[("救", "구", "to save — as in 구조, 구제")],
            notes=["Not 구하다 (求) “to look for”, as in 일자리를 구하다."],
            surfaces=["구한"],
        ),
        "수나라": dict(
            hanja="隋나라", meaning="Sui, the Chinese dynasty (581–618)",
            characters=[("隋", "수", "Sui, the name of the dynasty")],
            notes=["A Chinese dynasty takes 나라 after its one-syllable name: "
                   "수나라, 당나라, 송나라."],
        ),
        "군대": dict(
            hanja="軍隊", meaning="an army, the armed forces",
            characters=[("軍", "군", "an army — as in 장군, 육군"),
                        ("隊", "대", "a troop, a unit — as in 부대, 대원")],
        ),
        "이끌다": dict(
            meaning="to lead",
            notes=["승리로 이끌다 “to lead to victory” comes further down."],
            surfaces=["이끌고"],
        ),
        "쳐들어오다": dict(
            meaning="to invade, to storm in",
            notes=["치다 “to strike” + 들어오다 “to come in”."],
            surfaces=["쳐들어왔다"],
        ),
        "공격하다": dict(
            hanja="攻擊하다", meaning="to attack",
            characters=[("攻", "공", "to attack — as in 전공, 침공"),
                        ("擊", "격", "to strike — as in 충격, 타격")],
            surfaces=["공격하려고"],
        ),
        "장군": dict(
            hanja="將軍", meaning="a general",
            characters=[("將", "장", "a commander; about to — as in 장래"),
                        ("軍", "군", "an army")],
        ),
        "을지문덕": dict(
            hanja="乙支文德",
            meaning="을지문덕, the 고구려 general who won the battle of the 살수 "
                    "in 612",
            characters=[("乙支", None, "을지, the family name"),
                        ("文德", None, "문덕, the given name — 文 letters, "
                                       "德 virtue")],
        ),
        "일부러": dict(meaning="on purpose, deliberately"),
        "패하다": dict(
            hanja="敗하다", meaning="to be defeated, to lose",
            characters=[("敗", "패", "to be defeated — as in 실패, 부패")],
            surfaces=["패하는"],
        ),
        "척하다": dict(
            meaning="to pretend to",
            notes=["After -는/-(으)ㄴ: 패하는 척하다 “to pretend to be losing”."],
            surfaces=["척하며"],
        ),
        "끌어들이다": dict(
            meaning="to draw in, to lure in",
            surfaces=["끌어들였다"],
        ),
        "살수": dict(
            hanja="薩水",
            meaning="the 살수, the old name of the Cheongcheon river",
            characters=[("薩", "살", "used for its sound"),
                        ("水", "수", "water, a river")],
            notes=["The victory there is the 살수 대첩 (大捷, a great victory) "
                   "of the picture’s caption."],
        ),
        "둑": dict(meaning="a dam, an embankment"),
        "한꺼번에": dict(meaning="all at once, in one go"),
        "터뜨리다": dict(
            meaning="to burst, to break open",
            surfaces=["터뜨려"],
        ),
        "물리치다": dict(
            meaning="to drive off, to repel",
            surfaces=["물리쳤다"],
        ),
        "한반도": dict(
            hanja="韓半島", meaning="the Korean peninsula",
            characters=[("韓", "한", "Korea"),
                        ("半", "반", "half — as in 절반"),
                        ("島", "도", "an island — as in 제주도, 독도")],
        ),
        "거란": dict(
            hanja="契丹",
            meaning="the Khitan, the people who founded the Liao state (요) "
                    "north of 고려",
            characters=[("契丹", None, "Khitan — the characters are read 거란 "
                                       "for this name only")],
        ),
        "내놓다": dict(
            meaning="to give up, to hand over; to put out",
            surfaces=["내놓을"],
        ),
        "송나라": dict(
            hanja="宋나라", meaning="Song, the Chinese dynasty (960–1279)",
            characters=[("宋", "송", "Song, the name of the dynasty")],
        ),
        "교류하다": dict(
            hanja="交流하다", meaning="to have dealings with, to exchange",
            characters=[("交", "교", "to cross, to exchange — as in 외교, 교통"),
                        ("流", "류", "to flow — as in 유행, 한류")],
            surfaces=["교류하지"],
        ),
        "관리": dict(
            hanja="官吏", meaning="an official",
            characters=[("官", "관", "an office, an official — as in 장관, 경찰관"),
                        ("吏", "리", "a clerk, a minor official")],
            notes=["Not 관리 (管理) “management”."],
        ),
        "떼어 주다": dict(
            meaning="to cut off a part and give it",
            notes=["떼다 “to detach” + 주다."],
            surfaces=["떼어 주어"],
        ),
        "서희": dict(
            hanja="徐熙",
            meaning="서희, the 고려 official who negotiated with the 거란 in 993",
            characters=[("徐", "서", "서, the family name"),
                        ("熙", "희", "bright — the given name")],
        ),
        "나서다": dict(
            meaning="to come forward, to step in",
            surfaces=["나서서"],
        ),
        "앞두다": dict(
            meaning="to have (something) ahead of one",
            notes=["전쟁을 앞두고 “with a war ahead”, 시험을 앞두고 “with the exam "
                   "coming”."],
            surfaces=["앞두고"],
        ),
        "침략": dict(
            hanja="侵略", meaning="an invasion, aggression",
            characters=[("侵", "침", "to invade — as in 침입, 침해"),
                        ("略", "략", "to seize; a plan — as in 전략, 생략")],
            notes=["The review on p. 223 says 침입 (侵入) for the same thing."],
        ),
        "쏟다": dict(
            meaning="to pour (out)",
            notes=["힘을 쏟다 “to put one’s strength into”."],
            surfaces=["쏟을"],
        ),
        "외교": dict(
            hanja="外交", meaning="diplomacy",
            characters=[("外", "외", "outside — as in 외국, 해외"),
                        ("交", "교", "to exchange — as in 교류, 교환")],
            notes=["The map’s 외교 담판 (談判) is a diplomatic negotiation that "
                   "settles a matter."],
        ),
        "막아내다": dict(
            meaning="to stave off, to hold back",
            surfaces=["막아냈고"],
        ),
        "오히려": dict(meaning="on the contrary, what is more"),
        "압록강": dict(
            hanja="鴨綠江", meaning="the Amnok (Yalu) river",
            characters=[("鴨", "압", "a duck"),
                        ("綠", "록", "green — as in 녹색, 녹차"),
                        ("江", "강", "a river — as in 한강")],
        ),
        "차지하다": dict(
            meaning="to take, to occupy",
            surfaces=["차지할"],
        ),
        "후손": dict(
            hanja="後孫", meaning="a descendant",
            characters=[("後", "후", "after — as in 이후, 오후"),
                        ("孫", "손", "a grandchild — as in 손자, 자손")],
        ),
        "사귀다": dict(
            meaning="to befriend, to keep company with",
            surfaces=["사귀는"],
        ),
        "여진족": dict(
            hanja="女眞族", meaning="the Jurchen people",
            characters=[("女眞", None, "Jurchen — written for its sound"),
                        ("族", "족", "a people, a clan — as in 민족, 가족")],
        ),
        "가로막다": dict(
            meaning="to block, to stand in the way",
            surfaces=["가로막고"],
        ),
        "임진왜란": dict(
            hanja="壬辰倭亂",
            meaning="the Japanese invasions that began in 1592",
            characters=[("壬辰", None, "the 임진 year of the sixty-year cycle, "
                                       "1592"),
                        ("倭", "왜", "Japan (an old name)"),
                        ("亂", "란", "a disturbance, a war — as in 혼란, 반란")],
        ),
        "육군": dict(
            hanja="陸軍", meaning="the army, land forces",
            characters=[("陸", "육", "land — as in 육지, 대륙"),
                        ("軍", "군", "an army")],
        ),
        "전투": dict(
            hanja="戰鬪", meaning="a battle",
            characters=[("戰", "전", "war — as in 전쟁, 전술"),
                        ("鬪", "투", "to fight — as in 투쟁")],
        ),
        "이순신": dict(
            hanja="李舜臣",
            meaning="이순신, the admiral of 조선 in the 임진왜란",
            characters=[("李", "이", "이, the family name"),
                        ("舜臣", None, "순신, the given name — 舜 the sage "
                                       "king Shun, 臣 a minister")],
        ),
        "수군": dict(
            hanja="水軍", meaning="the navy (the old word)",
            characters=[("水", "수", "water — as in 수영, 수도"),
                        ("軍", "군", "an army")],
            notes=["The book glosses it with today’s word, 해군."],
        ),
        "해군": dict(
            hanja="海軍", meaning="the navy",
            characters=[("海", "해", "the sea — as in 해외, 동해"),
                        ("軍", "군", "an army")],
        ),
        "곳곳": dict(meaning="place after place, everywhere"),
        "승리": dict(
            hanja="勝利", meaning="a victory",
            characters=[("勝", "승", "to win — as in 우승, 승부"),
                        ("利", "리", "advantage, benefit — as in 이익, 유리")],
        ),
        "거두다": dict(
            meaning="to win, to reap; to gather in",
            notes=["승리를 거두다 “to win a victory”."],
            surfaces=["거두었다"],
        ),
        "무기": dict(
            hanja="武器", meaning="a weapon, arms",
            characters=[("武", "무", "military — as in 무술, 무력"),
                        ("器", "기", "a tool, a vessel — as in 기구, 악기")],
        ),
        "식량": dict(
            hanja="食糧", meaning="provisions, food supplies",
            characters=[("食", "식", "to eat, food — as in 음식, 식사"),
                        ("糧", "량", "grain, rations — as in 양식")],
        ),
        "뛰어나다": dict(
            meaning="to be outstanding",
            surfaces=["뛰어난"],
        ),
        "전술": dict(
            hanja="戰術", meaning="tactics",
            characters=[("戰", "전", "war — as in 전투, 전쟁"),
                        ("術", "술", "a skill, an art — as in 기술, 미술")],
        ),
        "거북선": dict(
            hanja="거북船", meaning="the turtle ship",
            characters=[("船", "선", "a ship — as in 선박, 어선")],
            notes=["거북 “a turtle” + 船: the roofed warship the opening "
                   "page’s first question asks about."],
        ),
        "화포": dict(
            hanja="火砲", meaning="a cannon, artillery",
            characters=[("火", "화", "fire — as in 화재, 소화기"),
                        ("砲", "포", "a gun, a cannon — as in 대포")],
        ),
        "벌이다": dict(
            meaning="to wage, to start, to stage",
            notes=["전투를 벌이다 “to fight a battle”; the 유관순 article has "
                   "만세 운동을 벌였고."],
            surfaces=["벌인"],
        ),
        "활약": dict(
            hanja="活躍", meaning="an active part, exploits",
            characters=[("活", "활", "to live, lively — as in 활동, 생활"),
                        ("躍", "약", "to leap — as in 도약")],
        ),
        "불리하다": dict(
            hanja="不利하다", meaning="to be unfavourable, to go against one",
            characters=[("不", "불", "not — as in 불행, 부족"),
                        ("利", "리", "advantage — as in 승리, 유리")],
            surfaces=["불리했던"],
        ),
        "마침내": dict(meaning="at last, in the end"),
        "물러나다": dict(
            meaning="to withdraw, to step back",
            surfaces=["물러나도록"],
        ),
        "허난설헌": dict(
            hanja="許蘭雪軒",
            meaning="허난설헌 (1563–1589), a poet of 조선",
            characters=[("許", "허", "허, the family name"),
                        ("蘭雪軒", None, "난설헌, her pen name — 蘭 an orchid, "
                                         "雪 snow, 軒 a house")],
        ),
        "홍길동전": dict(
            hanja="洪吉童傳",
            meaning="The Tale of 홍길동, the novel in 한글",
            characters=[("洪吉童", None, "홍길동, the hero’s name"),
                        ("傳", "전", "a tale, a life — as in 전기, 전통")],
        ),
        "허균": dict(
            hanja="許筠",
            meaning="허균 (1569–1618), the writer, 허난설헌’s younger brother",
            characters=[("許", "허", "허, the family name"),
                        ("筠", "균", "bamboo — the given name")],
        ),
        "글재주": dict(
            meaning="a gift for writing",
            notes=["글 “writing” + 재주 “a talent, a knack”."],
        ),
        "시": dict(
            hanja="詩", meaning="a poem, poetry",
            characters=[("詩", "시", "poetry — as in 시인")],
            notes=["시를 짓다 “to compose a poem”; the heading’s 시인 (詩人) is "
                   "a poet."],
        ),
        "재능": dict(
            hanja="才能", meaning="talent",
            characters=[("才", "재", "talent — as in 천재, 인재"),
                        ("能", "능", "ability — as in 능력, 가능")],
        ),
        "사회활동": dict(
            hanja="社會活動", meaning="activity in society, public life",
            characters=[("社會", None, "society — 社 a gathering, 會 to meet"),
                        ("活動", None, "activity — 活 lively, 動 to move")],
        ),
        "여기다": dict(
            meaning="to regard, to consider",
            notes=["좋게 여기지 않다 “not to look kindly on”."],
            surfaces=["여기지"],
        ),
        "마찬가지": dict(meaning="the same, just alike"),
        "불행하다": dict(
            hanja="不幸하다", meaning="to be unhappy, unfortunate",
            characters=[("不", "불", "not — as in 불리, 불편"),
                        ("幸", "행", "good fortune — as in 행복, 다행")],
            surfaces=["불행한"],
        ),
        "친정": dict(
            hanja="親庭", meaning="a married woman’s own parents’ home",
            characters=[("親", "친", "parents, close — as in 부친, 친척"),
                        ("庭", "정", "a garden, a household — as in 가정")],
            notes=["친정 아버지 is the wife’s own father, against 시아버지, her "
                   "husband’s."],
        ),
        "세상을 떠나다": dict(
            hanja="世上을 떠나다", meaning="to pass away",
            characters=[("世", "세", "the world, an age — as in 세계, 세대"),
                        ("上", "상", "on, above — as in 이상, 지상")],
            notes=["Literally “to leave the world”."],
            surfaces=["세상을 떠났다"],
        ),
        "아까워하다": dict(
            meaning="to feel (something) is too good to lose, to begrudge "
                    "its loss",
            notes=["From 아깝다 “to be a waste, a pity”."],
            surfaces=["아까워한"],
        ),
        "평가": dict(
            hanja="評價", meaning="an assessment, esteem",
            characters=[("評", "평", "to comment, to judge — as in 평판, 비평"),
                        ("價", "가", "value, price — as in 가격, 물가")],
            notes=["높은 평가를 받다 “to be highly thought of”."],
        ),
        "김만덕": dict(
            hanja="金萬德",
            meaning="김만덕 (1739–1812), a merchant of Jeju",
            characters=[("金", "김", "김, the family name"),
                        ("萬德", None, "만덕, the given name — 萬 ten thousand, "
                                       "德 virtue")],
        ),
        "큰돈": dict(meaning="a large sum of money, a fortune"),
        "흉년": dict(
            hanja="凶年", meaning="a year of bad harvest, a famine year",
            characters=[("凶", "흉", "ill-omened, bad — as in 흉기"),
                        ("年", "년", "a year")],
            notes=["흉년이 들다 “a bad year sets in”. Its opposite is 풍년 "
                   "(豊年), a year of plenty."],
        ),
        "굶다": dict(
            meaning="to go hungry, to starve",
            notes=["굶어 죽다 “to starve to death”."],
            surfaces=["굶어"],
        ),
        "백성": dict(
            hanja="百姓", meaning="the common people, a king’s subjects",
            characters=[("百", "백", "a hundred — as in 백화점"),
                        ("姓", "성", "a family name — as in 성명")],
            notes=["Literally “the hundred surnames”."],
        ),
        "정조": dict(
            hanja="正祖",
            meaning="정조, the twenty-second king of 조선 (r. 1776–1800)",
            characters=[("正", "정", "right — as in 정의, 공정"),
                        ("祖", "조", "an ancestor — as in 조상; closes a "
                                     "king’s temple name")],
        ),
        "소원": dict(
            hanja="所願", meaning="a wish",
            characters=[("所", "소", "that which; a place — as in 장소, 소득"),
                        ("願", "원", "to wish — as in 원하다, 지원")],
            notes=["소원을 이루다 “to have one’s wish come true”."],
        ),
        "신분": dict(
            hanja="身分", meaning="social status, standing",
            characters=[("身", "신", "the body, oneself — as in 신체, 자신"),
                        ("分", "분", "a share, a part — as in 부분, 분야")],
        ),
        "임금": dict(
            meaning="a king",
            notes=["The native word. Not 임금 (賃金) “wages”."],
        ),
        "빼어나다": dict(
            meaning="to be outstanding, exceptionally fine",
            surfaces=["빼어난"],
        ),
        "경치": dict(
            hanja="景致", meaning="scenery",
            characters=[("景", "경", "a view — as in 풍경, 배경"),
                        ("致", "치", "to reach; an air, a charm")],
        ),
        "금강산": dict(
            hanja="金剛山", meaning="금강산, Mount Kumgang",
            characters=[("金剛", None, "diamond — 金 metal, 剛 hard"),
                        ("山", "산", "a mountain")],
        ),
        "이루다": dict(
            meaning="to achieve, to fulfil",
            surfaces=["이루었다"],
        ),
        "만덕상": dict(
            hanja="萬德賞", meaning="the 만덕 prize",
            characters=[("萬德", None, "만덕, 김만덕’s given name"),
                        ("賞", "상", "a prize — as in 상금, 수상")],
        ),
        "선행": dict(
            hanja="善行", meaning="a good deed",
            characters=[("善", "선", "good — as in 최선, 개선"),
                        ("行", "행", "to act — as in 행동, 행위")],
            notes=["선행을 베풀다 “to do good to others”."],
        ),
        "베풀다": dict(
            meaning="to bestow, to do (a kindness)",
            surfaces=["베푼"],
        ),
        "해마다": dict(meaning="every year"),
        "독립": dict(
            hanja="獨立", meaning="independence",
            characters=[("獨", "독", "alone — as in 독신, 독학"),
                        ("立", "립", "to stand — as in 설립, 국립")],
        ),
        "외치다": dict(
            meaning="to cry out, to call for",
            surfaces=["외치는"],
        ),
        "3·1 운동": dict(
            hanja="三一運動",
            meaning="the March First Movement of 1919",
            characters=[("三一", None, "three-one: 1 March"),
                        ("運動", None, "a movement — 運 to carry, 動 to move")],
        ),
        "이화학당": dict(
            hanja="梨花學堂",
            meaning="이화학당, the girls’ school in Seoul founded in 1886",
            characters=[("梨花", None, "pear blossom — 梨 a pear, 花 a flower"),
                        ("學堂", None, "a school — 學 to learn, 堂 a hall")],
        ),
        "참여하다": dict(
            hanja="參與하다", meaning="to take part",
            characters=[("參", "참", "to take part — as in 참가, 참석"),
                        ("與", "여", "to give, to join — as in 기여, 수여")],
            surfaces=["참여하였다"],
        ),
        "일제": dict(
            hanja="日帝", meaning="imperial Japan",
            characters=[("日", "일", "Japan; the sun, a day"),
                        ("帝", "제", "an emperor — as in 제국, 황제")],
            notes=["Short for 일본 제국주의, Japanese imperialism."],
        ),
        "만세 운동": dict(
            hanja="萬歲運動",
            meaning="a 만세 demonstration, the crowds shouting 대한 독립 만세",
            characters=[("萬歲", None, "ten thousand years, “long live” — "
                                       "萬 ten thousand, 歲 a year"),
                        ("運動", None, "a movement")],
        ),
        "체포되다": dict(
            hanja="逮捕되다", meaning="to be arrested",
            characters=[("逮", "체", "to catch up with, to seize"),
                        ("捕", "포", "to catch — as in 포획")],
            surfaces=["체포된"],
        ),
        "재판정": dict(
            hanja="裁判廷", meaning="a courtroom",
            characters=[("裁判", None, "a trial — 裁 to judge, 判 to judge"),
                        ("廷", "정", "a court, a hall — as in 법정")],
        ),
        "당당하다": dict(
            hanja="堂堂하다", meaning="to be bold, unabashed, dignified",
            characters=[("堂", "당", "a hall; imposing — as in 식당, 학당")],
            notes=["The character is said twice."],
            surfaces=["당당하게"],
        ),
        "죄": dict(
            hanja="罪", meaning="a crime, a sin",
            characters=[("罪", "죄", "a crime — as in 범죄, 무죄")],
            notes=["죄를 짓다 “to commit a crime”."],
        ),
        "자격": dict(
            hanja="資格", meaning="a qualification, standing",
            characters=[("資", "자", "resources, a basis — as in 자료, 투자"),
                        ("格", "격", "a standard, a rank — as in 합격, 성격")],
        ),
        "서대문 형무소": dict(
            hanja="西大門刑務所", meaning="Seodaemun Prison",
            characters=[("西大門", None, "the West Gate — 西 west, 大 great, "
                                         "門 a gate"),
                        ("刑務所", None, "a prison — 刑 punishment, 務 duties, "
                                         "所 a place")],
            notes=["형무소 is the old word; a prison is 교도소 today."],
        ),
        "갇히다": dict(
            meaning="to be shut up, to be confined",
            notes=["The passive of 가두다 “to lock up”."],
            surfaces=["갇혀"],
        ),
        "펼치다": dict(
            meaning="to carry on, to unfold",
            surfaces=["펼치다가"],
        ),
        "폭행": dict(
            hanja="暴行", meaning="violence, assault",
            characters=[("暴", "폭", "violent — as in 폭력, 폭우"),
                        ("行", "행", "to act — as in 행위, 선행")],
        ),
        "영양 부족": dict(
            hanja="營養不足", meaning="malnutrition",
            characters=[("營養", None, "nutrition — 營 to manage, 養 to "
                                       "nourish"),
                        ("不足", None, "a lack — 不 not, 足 enough")],
        ),
        "맞이하다": dict(
            meaning="to meet, to greet",
            notes=["죽음을 맞이하다 “to meet one’s death”."],
            surfaces=["맞이하였다"],
        ),
        "지폐": dict(
            hanja="紙幣", meaning="a banknote, paper money",
            characters=[("紙", "지", "paper — as in 휴지, 편지"),
                        ("幣", "폐", "money — as in 화폐")],
        ),
        "등장하다": dict(
            hanja="登場하다", meaning="to appear, to come on the scene",
            characters=[("登", "등", "to climb, to enter — as in 등록, 등산"),
                        ("場", "장", "a place — as in 시장, 현장")],
            surfaces=["등장하는"],
        ),
        "이황": dict(
            hanja="李滉",
            meaning="이황 (1501–1570), a Confucian scholar of 조선, pen name 퇴계",
            characters=[("李", "이", "이, the family name"),
                        ("滉", "황", "deep and wide (of water) — the given "
                                     "name")],
        ),
        "이이": dict(
            hanja="李珥",
            meaning="이이 (1536–1584), a Confucian scholar of 조선, pen name 율곡",
            characters=[("李", "이", "이, the family name"),
                        ("珥", "이", "an ear ornament of jade — the given "
                                     "name")],
        ),
        "세종": dict(
            hanja="世宗",
            meaning="세종, the fourth king of 조선 (r. 1418–1450)",
            characters=[("世", "세", "an age, the world — as in 세계, 세상"),
                        ("宗", "종", "an ancestor, a line — as in 종교; closes "
                                     "a king’s temple name")],
        ),
        "신사임당": dict(
            hanja="申師任堂",
            meaning="신사임당 (1504–1551), a painter of 조선, the mother of 이이",
            characters=[("申", "신", "신, the family name"),
                        ("師任堂", None, "사임당, her pen name — 師 to take as "
                                         "a teacher, 任 태임, the mother of "
                                         "King Wen of Zhou, 堂 a hall")],
        ),
        "학자": dict(
            hanja="學者", meaning="a scholar",
            characters=[("學", "학", "to learn — as in 학교, 학식"),
                        ("者", "자", "a person — as in 기자, 당사자")],
        ),
        "유학": dict(
            hanja="儒學", meaning="Confucian learning",
            characters=[("儒", "유", "a Confucian scholar — as in 유교"),
                        ("學", "학", "learning")],
            notes=["Not 유학 (留學) “studying abroad”."],
        ),
        "발달": dict(
            hanja="發達", meaning="development, advance",
            characters=[("發", "발", "to send out, to arise — as in 발전, 발생"),
                        ("達", "달", "to reach — as in 전달, 도달")],
        ),
        "기여하다": dict(
            hanja="寄與하다", meaning="to contribute",
            characters=[("寄", "기", "to entrust, to send — as in 기부, 기숙사"),
                        ("與", "여", "to give — as in 참여, 수여")],
            surfaces=["기여하였다"],
        ),
        "훈민정음": dict(
            hanja="訓民正音",
            meaning="훈민정음, “the right sounds for teaching the people”: "
                    "the alphabet 세종 made, now called 한글",
            characters=[("訓", "훈", "to teach — as in 훈련, 교훈"),
                        ("民", "민", "the people — as in 국민, 시민"),
                        ("正", "정", "right — as in 정확, 공정"),
                        ("音", "음", "a sound — as in 발음, 음악")],
        ),
        "기구": dict(
            hanja="器具", meaning="an instrument, an implement",
            characters=[("器", "기", "a tool, a vessel — as in 무기, 악기"),
                        ("具", "구", "to be equipped; a tool — as in 도구, 가구")],
            notes=["Not 기구 (機構) “an organisation”."],
        ),
        "꾸준히": dict(meaning="steadily, without a break"),
        "학식": dict(
            hanja="學識", meaning="learning, scholarship",
            characters=[("學", "학", "to learn — as in 학자, 학교"),
                        ("識", "식", "to know — as in 지식, 상식")],
            notes=["학식이 높다 “to be of great learning”."],
        ),
        "화폐": dict(
            hanja="貨幣", meaning="money, currency",
            characters=[("貨", "화", "goods, money — as in 화물, 외화"),
                        ("幣", "폐", "money — as in 지폐")],
        ),
        "업적": dict(
            hanja="業績", meaning="an achievement, a record of work done",
            characters=[("業", "업", "work — as in 직업, 사업"),
                        ("績", "적", "to spin; results — as in 성적, 실적")],
        ),
    },

    extraNotes=[
        "The two photographs on p. 220 carry no caption; they are described, "
        "not reproduced.",
        "The painting, the map and the turtle ship on p. 221, the portrait, "
        "the book, the poster and the photograph on p. 222 and the four "
        "banknotes on p. 223 are not reproduced; their captions are. The "
        "words printed on the map are set as labels.",
        "The exchange between 서희 and the 거란 general, printed in small type "
        "beside the article on p. 221, is set line by line after it.",
        "On p. 222 허난설헌 초상 and 유관순 are printed in the margin with the "
        "red dot of a glossary term, but they caption the two portraits and "
        "are set as captions. 흉년 is the page’s one glossary term.",
        "The review gaps on p. 223 are blank in the book and left blank here.",
    ],
)
