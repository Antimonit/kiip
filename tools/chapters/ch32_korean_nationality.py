# -*- coding: utf-8 -*-
"""Chapter 32 — Korean nationality and the law.

Transcribed from the photos of pp. 170-173. Your English glosses on pp. 170,
171, 172 and 173 are carried as the entries for the words they sit over.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, TABLE,
               CELL, GLOSSARY)

CHAPTER = dict(
    number=32, slug="32-korean-nationality",
    unit="법", title="한국 국적과 법", titleEn="Korean nationality and the law",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 {귀화}를 통해 한국 국적을 갖게 된 사례입니다.",
                  "Below is the case of someone who came to hold Korean "
                  "nationality through naturalisation."),
        FIGURE("MBC 뉴스 화면 — 팜티프엉 중앙경찰학교 교육생: “국적 포기하는 것도 마음이 좀 아프긴 하지만, "
               "조금 더 내가 큰 보람이 되는 일을 하고 싶었습니다.”"),
        SOURCE("▲ 베트남 출신 팜티프엉 씨는 지난 2007년 한국인 남편과 함께 충청북도 음성에 자리를 잡았다. "
               "그녀는 경찰이 되고 싶었지만 한국 국적이 없었기 때문에 경찰학교에 도전할 수 없었다. 그래서 "
               "귀화를 결심했고 2016년 결국 꿈을 이루게 되었다. 팜티프엉 씨는 한국의 경찰로서 한국에 와 "
               "있는 결혼이민자, 외국인 근로자, 유학생 등을 돕는 일을 하고 싶다고 말했다."),
        HEADING(4, "01 팜티프엉 씨가 한국 경찰이 되기 어려웠던 이유는 무엇입니까?",
                translation="Why was it hard for Pham Thi Phuong to become a "
                            "Korean police officer?"),
        HEADING(4, "02 한국 국적을 얻으면 한국에서 생활할 때 어떤 점이 좋은지 말해 볼까요?",
                translation="Shall we say what is good about living in Korea "
                            "once one holds Korean nationality?"),

        SECTION("goals", "학습목표"),
        BULLET("한국 국적을 얻는 것의 의미와 {기준}을 설명할 수 있다.", ordered=True,
               translation="Explain what obtaining Korean nationality means, "
                           "and on what basis it is granted."),
        BULLET("귀화의 {유형}과 절차를 설명할 수 있다.", ordered=True,
               translation="Explain the kinds of naturalisation and the "
                           "procedure."),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"],
              [["기본", "법", "30. 외국인과 법", "국적과 관계 없이 보장되는 외국인의 권리"]]),

        SECTION("part", "01 한국 국적은 어떤 의미를 가지며 어떤 기준으로 결정될까?"),
        GLOSSARY(("영주권", "일정한 요건을 갖춘 외국인에게 주는, 그 나라에서 영구적으로 오랫동안 거주할 수 "
                            "있는 권리", "영주권", "permanent residency (F-5)"),
                 ("입대", "군에 들어가 군인이 되는 것", "입대", "to join the army")),
        HEADING(2, "국적의 의미", translation=
                "What nationality means" "\n\n"
                "Nationality means the standing by which a person is "
                "recognised as a national of some country. A Korean national "
                "is therefore someone holding the nationality of the "
                "Republic of Korea, who can enjoy the freedoms and rights "
                "the Constitution guarantees and must also carry out certain "
                "duties." "\n\n"
                "A permanent resident generally holds a good many rights and "
                "duties too, but not quite the same ones as a national who "
                "has obtained nationality. A permanent resident, unlike a "
                "national, has no right to take part in a presidential "
                "election, and an adult man holding Korean permanent "
                "residence has no duty to join the Korean army." "\n\n"
                "Unlike Korea, countries such as the United States, Canada "
                "and Australia operate a system of citizenship rather than "
                "of nationality. In those countries a citizen is thereby a "
                "national of that country and the bearer of every kind of "
                "right and duty."),
        PARAGRAPH("{국적}이란 한 사람이 어느 {국가}의 국민으로서 {인정받는|인정받다} {자격}을 가리킨다. "
                  "그러므로 한국 국민은 대한민국 국적을 갖고 있는 사람으로서 대한민국 {헌법}이 "
                  "{보장하는|보장하다} 자유와 {권리}를 누릴 수 있고 {일정한|일정하다} {의무}도 "
                  "{수행해야|수행하다} 한다."),
        PARAGRAPH("일반적으로 {영주권}자도 {상당히} 많은 권리와 의무를 가지고 있지만 국적을 얻은 국민과 "
                  "똑같지는 않다. 예를 들어 영주권자는 국민과 달리 대통령 선거에 참여할 수 있는 권리가 "
                  "없으며, 한국 영주권을 가진 {성인} 남자의 경우에는 한국 군대에 {입대}할 의무가 없다."),
        PARAGRAPH("한국과 달리 미국, 캐나다, 호주 등의 국가는 {국적 제도}가 아니라 {시민권} 제도를 "
                  "{운영한다|운영하다}. 이들 나라에서는 시민권자가 곧 그 나라의 국민으로서 {각종} 권리와 "
                  "의무의 {주체}가 된다."),
        FIGURE("대한민국 영주증의 모습 — 체류자격 영주(F-5)"),

        GLOSSARY(("출생지주의(속지주의)", "아이가 태어난 장소(국가)를 기준으로 아이의 국적을 결정하는 것",
                  "출생지주의", "the territorial principle"),
                 ("혈통주의(속인주의)", "태어난 아이의 부모가 가진 국적을 기준으로 아이의 국적을 결정하는 것",
                  "혈통주의", "the personal nationality principle"),
                 ("국적법", "한국 국민이 되는 요건을 정하는 법", "국적법",
                  "the Nationality Act"),
                 ("무국적자", "국적이 없는 사람", "무국적자", "a stateless person")),
        HEADING(2, "국적을 결정하는 방법", translation=
                "How nationality is decided" "\n\n"
                "How nationality is decided differs from country to country. "
                "The United States and Canada treat the place — the country "
                "— of birth as what matters. A child born in the United "
                "States can therefore hold American nationality. This is "
                "called the birthplace principle, or 속지주의. Countries such "
                "as China and Australia give weight to the nationality of "
                "the child’s parents. This is called the bloodline "
                "principle, or 속인주의." "\n\n"
                "Korea’s Nationality Act follows the bloodline principle. "
                "That is, a child’s nationality is decided by where the "
                "parents’ nationality lies. If the father or the mother, or "
                "both, are Korean nationals, the child can become a Korean "
                "national. Where it is not clear who the parents of a child "
                "born in Korea are, however, or where the parents or the "
                "child are stateless, being born in Korea is by itself "
                "enough to become a Korean national."),
        PARAGRAPH("국적을 결정하는 방법은 나라마다 차이가 있다. 미국이나 캐나다에서는 태어난 장소(국가)를 "
                  "중요하게 여긴다. 그래서 미국에서 태어난 아이는 미국 국적을 가질 수 있다. 이를 "
                  "{출생지주의}(속지주의)라고 한다. 중국이나 호주 같은 경우에는 태어난 아이의 부모의 국적을 "
                  "{중시한다|중시하다}. 이를 {혈통주의}(속인주의)라고 한다."),
        PARAGRAPH("한국의 {국적법}은 혈통주의를 따른다. 즉, 태어난 아이의 부모 국적이 어디인가에 따라 "
                  "아이의 국적이 결정된다. 태어난 아이의 아버지나 어머니 중 한 명 또는 두 사람이 모두 한국 "
                  "국민이라면 그 아이는 한국 국민이 될 수 있다. 다만, 한국에서 태어난 아이의 부모가 누구인지 "
                  "{분명하지|분명하다} 않거나 아이의 부모나 아이 본인이 {무국적자}인 경우에는 한국에서 "
                  "태어난 것만으로도 한국 국민이 될 수 있다."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "보편적 출생등록 제도", translation=
                "Universal birth registration" "\n\n"
                "In Korea, where a child of foreign nationality is born in "
                "the country, the birth is to be registered through the "
                "embassy of the parents’ own country. But the child of an "
                "unregistered foreigner is left stateless, under the "
                "protection of no country at all. To solve this the UN "
                "Committee on the Rights of the Child and others are asking "
                "Korea to protect such children through ‘universal birth "
                "registration’. The National Assembly is accordingly "
                "discussing a bill that would let a foreigner register in "
                "Korea the birth of a child born here."),
        PARAGRAPH("한국에서는 국내에서 태어난 외국 국적 아동의 경우 {본국} {대사관}을 통해 출생 신고를 "
                  "하도록 하고 있다. 하지만 {미등록 외국인}의 자녀는 어느 국가의 보호도 받지 못하는 "
                  "{무국적} 상태에 놓이게 된다. 이런 문제를 해결하기 위해 {유엔아동권리위원회} 등은 한국에 "
                  "‘{보편적 출생 등록 제도}’를 통해 그와 같은 아동을 보호하도록 {요청하고|요청하다} 있다. "
                  "이에 따라 한국 국회는 외국인이 국내에서 낳은 자녀를 한국에서 출생신고를 할 수 있도록 하는 "
                  "{법률안}을 {논의하고|논의하다} 있다."),

        SECTION("part", "02 귀화는 어떤 절차로 이루어질까?"),
        GLOSSARY(("허가", "허락하여 할 수 있도록 함", "허가", "permission"),
                 ("배우자", "남편에게는 아내가, 아내에게는 남편이 각각 배우자임", "배우자", "spouse"),
                 ("가족관계등록부",
                  "한국 국민 개개인이 등록한 주소, 성명, 생년월일 등 신분에 관한 사항과 가족관계에 관한 "
                  "사항 등을 기록한 문서", "가족관계등록부")),
        HEADING(2, "귀화의 유형과 절차", translation=
                "The kinds of naturalisation, and the procedure" "\n\n"
                "A foreigner can become a Korean national by meeting the "
                "requirements through their own will and effort and then "
                "obtaining permission from the Minister of Justice. This is "
                "called naturalisation. There are three kinds: general, "
                "simplified and special." "\n\n"
                "General naturalisation is the way a foreigner with no ties "
                "of blood or of place to Korea obtains Korean nationality. "
                "To apply for it one must have lived in Korea continuously "
                "for five years or more with an address and hold permanent "
                "residence (F-5) status, and must be an adult of 19 or over "
                "at the time of applying. One must also be of good conduct "
                "and able to maintain a livelihood, and have the basic "
                "attainments of a national, such as ability in Korean." "\n\n"
                "Simplified naturalisation is the way a foreigner with a "
                "certain connection to Korea obtains Korean nationality. For "
                "instance, a foreigner who has lived continuously in Korea "
                "for three years or more and one of whose parents was a "
                "Korean national may apply for it. Naturalisation through "
                "marriage also counts as simplified naturalisation. A "
                "foreigner who is or was the spouse of a Korean national may "
                "generally apply for simplified naturalisation where they "
                "have lived continuously in Korea for two years or more." "\n\n"
                "Special naturalisation is simpler in procedure than general "
                "or simplified naturalisation. A foreigner one of whose "
                "parents is currently a Korean national, a foreigner who has "
                "rendered special service to Korea, and a foreigner with "
                "outstanding ability in a particular field who is judged "
                "likely to serve the national interest may apply for special "
                "naturalisation."),
        PARAGRAPH("외국인은 자신의 {의지}와 노력을 통해 {요건}을 {갖춘|갖추다} 후, 법무부 {장관}으로부터 "
                  "{허가}를 받아 한국 국민이 될 수 있다. 이를 {귀화}라고 한다. 귀화에는 {일반귀화}, "
                  "{간이귀화}, {특별귀화}의 3가지 {유형}이 있다."),
        PARAGRAPH("일반귀화는 한국과 {혈연적}, {지연적} 관계가 없는 외국인이 한국 국적을 얻는 방법이다. "
                  "일반귀화를 신청하려면 한국에서 5년 이상 계속 생활한 주소, 영주(F-5) 자격을 가지고 있어야 "
                  "하며 귀화 신청 당시에 만 19세 이상의 {성인}이어야 한다. 또한, {품행}이 "
                  "{단정하고|단정하다} {생계유지} 능력이 있어야 하며 한국어 능력 등 국민으로서 기본적인 "
                  "{소양}을 갖추어야 한다."),
        PARAGRAPH("{간이귀화}는 대한민국과 일정한 관계가 있는 외국인이 한국 국적을 얻는 방법이다. 예를 "
                  "들어, 외국인이 한국에서 3년 이상 계속 생활했고 그의 부모 중 어느 한쪽이 한국 국민이었다면 "
                  "그는 간이귀화를 신청할 수 있다. {혼인}을 통한 귀화도 간이귀화에 {해당한다|해당하다}. "
                  "한국 국민의 {배우자}이거나 배우자였던 외국인의 경우 일반적으로 한국에 2년 이상 계속 "
                  "거주하는 경우 간이귀화를 신청할 수 있다."),
        PARAGRAPH("{특별귀화}는 일반귀화나 간이귀화에 비해 절차가 더 간단하다. 부모 중 어느 한쪽이 현재 "
                  "한국 국민인 외국인, 한국에 특별한 {공로}가 있는 외국인, {특정} 분야에서 매우 "
                  "{우수한|우수하다} 능력을 {보유}한 사람으로서 한국 {국익}에 도움을 줄 것으로 인정되는 "
                  "외국인은 특별귀화를 신청할 수 있다."),
        BULLET("귀화 신청 및 접수 → 귀화시험 및 요건 심사 → 범죄 경력 및 신원조회 후 심사 결정 → "
               "{국민선서} → 법무부가 귀화허가를 받은 사람이 정한 등록기준지의 시·읍·면의 장에게 통보하면 "
               "{가족관계등록부} 생성 → 허가 후 1년 내 외국 국적 포기 또는 외국 국적 불행사 서약 → "
               "주소지 행정복지센터에서 주민등록 및 외국인 등록증 반납",
               translation="Applying for naturalisation and the application "
                           "being received → the naturalisation test and the "
                           "examination of requirements → the decision after "
                           "checks on criminal record and identity → the "
                           "national oath → the Ministry of Justice notifies "
                           "the head of the city, town or township of the "
                           "registration base the person has chosen, and a "
                           "family relation register is created → within a "
                           "year of permission, renouncing the foreign "
                           "nationality or pledging not to exercise it → "
                           "resident registration at the community service "
                           "centre for the address, and returning the alien "
                           "registration card."),
        SOURCE("▲ 귀화 절차"),
        TABLE(["", "인원(명)"],
              [["일반귀화", "1,037"],
               ["간이귀화", "7,953"],
               ["특별귀화", "2,064"],
               ["기타", "502"],
               ["합계", "11,556"]]),
        SOURCE("▲ 귀화에 의한 국적 취득 현황(법무부 2019)"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "국적법 개정에 따라 ‘국민선서’를 해야 합니다", translation=
                "Under the amended Nationality Act, the national oath must "
                "be taken" "\n\n"
                "The amended Nationality Act took effect on 20 December "
                "2018. Under it, someone granted naturalisation or the "
                "restoration of nationality must attend the ceremony where "
                "the certificate of nationality is conferred and take the "
                "national oath in order to hold Korean nationality. The oath "
                "runs as follows." "\n\n"
                "The oath: “I solemnly swear that, as a proud national of the "
                "Republic of Korea, I will abide by the Constitution and the "
                "laws of the Republic of Korea and fulfil the "
                "responsibilities and duties of a national.”" "\n\n"
                "After the oath, when the Ministry of Justice notifies the "
                "head of the city, town or township of the registration base "
                "chosen by the person granted naturalisation that they have "
                "become a Korean national, a family relation register is "
                "created."),
        PARAGRAPH("2018년 12월 20일부터 {개정}된 {국적법}이 {시행되었다|시행되다}. 이 법에 따르면 귀화나 "
                  "국적 {회복} 허가를 받은 사람이 한국 국적을 갖기 위해서는 {국적증서} {수여식}에 "
                  "참여하여 {국민선서}를 해야 한다. 국민선서 내용은 다음과 같다."),
        PARAGRAPH("“나는 자랑스러운 대한민국의 국민으로서 대한민국의 헌법과 법률을 {준수하고|준수하다} "
                  "국민의 {책임}과 의무를 다할 것을 {엄숙히} {선서합니다|선서하다}.”"),
        PARAGRAPH("국민선서 이후에 한국 국민이 되었다는 사실을 법무부가 귀화허가를 받은 사람이 정한 "
                  "{등록기준지}의 시·읍·면의 장에게 {통보하면|통보하다} {가족관계등록부}가 만들어진다."),
        FIGURE("귀화자 국민선서 모습 (사진 출처: 〈연합뉴스〉)"),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 한국 국적은 어떤 의미를 가지며 어떤 기준으로 결정될까?"),
        BULLET("한국 국민은 대한민국 (        )을 가진 사람을 말한다. 한국 국적을 가지고 있는 사람은 "
               "대한민국 (        )이 보장하는 자유와 권리를 누릴 수 있고 일정한 의무도 수행해야 한다."),
        BULLET("(        )은 외국인이 어떤 나라에 영구적으로 거주할 수 있는 권리를 의미한다."),
        BULLET("한국은 아이가 태어난 장소보다 아이 부모의 국적이 어디인가를 중시한다. 이것을 "
               "(        ) 또는 혈통주의라고 한다."),
        HEADING(3, "02 귀화란 무엇일까?"),
        BULLET("외국인은 본인의 의지와 노력에 의해 요건을 갖춘 후, (            )으로부터 허가를 받아 "
               "한국 국민이 될 수 있다."),
        BULLET("일반귀화를 신청하려면 한국에서 (        ) 이상 생활한 주소가 있어야 하고 "
               "(        ) 자격을 가지고 있어야 한다. 또한, 귀화 신청 당시 만 (        ) 이상의 "
               "성인으로서 품행이 단정하고 생계유지 능력과 국민으로서 기본적인 소양을 갖추어야 한다."),
        BULLET("혼인을 통한 귀화는 (        )에 해당한다. 한국 국민의 배우자이거나 배우자였던 외국인의 "
               "경우 일반적으로 한국에 (        )년 이상 계속 거주하는 경우 (        )를 신청할 수 "
               "있다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "당신에게 국적은 어떤 의미인가요?", translation=
                "What does nationality mean to you?" "\n\n"
                "The documentary 〈귀화〉 tells the stories of people who came "
                "to hold Korean nationality for various reasons. Kim "
                "Ju-hyeon, from Bangladesh, says that without Korean "
                "nationality even buying a mobile phone was hard, and that "
                "it is wonderful now, as a Korean, not to have to go to the "
                "immigration office again. Choi Mu-bin, from Pakistan, says "
                "that holding Korean nationality has made moving in and out "
                "of the country easier while running a business. Being able "
                "to take part in presidential and Assembly elections in "
                "particular, he says he has now become completely Korean. "
                "Through their stories we can think about what nationality "
                "means to us, and what it does."),
        PARAGRAPH("{다큐멘터리} 〈귀화〉는 여러 가지 이유로 대한민국 국적을 갖게 된 사람들의 이야기를 다루고 "
                  "있다. 김주현(방글라데시 출신)씨는 한국 국적이 없을 때는 휴대폰 하나 구입하기도 힘들었다고 "
                  "하며 이제 한국인이 되어 다시 {출입국사무소}를 가지 않아서 너무 좋다고 한다. "
                  "최무빈(파키스탄 출신)씨는 한국 국적을 갖고 나니 사업을 하면서 국내외 {이동}이 "
                  "편리해졌다고 한다. 특히 대통령 선거나 국회의원 선거에도 참여하게 되면서 {스스로} 이제는 "
                  "완전히 한국인이 되었다고 말한다. 이들의 이야기를 통해 우리 자신에게 국적이란 어떤 의미를 "
                  "가지고 있는지, 어떤 역할을 하는지 생각해볼 수 있다."),
        FIGURE("다큐멘터리 ‘귀화’의 한 장면 — ‘귀화, 돌아오다’"),
        PARAGRAPH("★ 자신에게 한국 국적이 생긴다면 어떤 변화가 생길까요? 자신이 한국 국적을 필요로 한다면 "
                  "어떤 점에서 그러한지 말해 봅시다.",
                  "What would change if you came to hold Korean nationality? "
                  "If you need Korean nationality, say in what respects."),
    ],

    extraAnnotations={
        "귀화": dict(
            hanja="歸化", meaning="naturalisation, taking on a nationality",
            characters=[("歸", "귀", "to return, to belong to — as in 귀국, 귀가"),
                        ("化", "화", "to become, -isation — as in 산업화, 고령화")],
            notes=["Literally to return and become one of. 귀화자 is a "
                   "naturalised citizen."],
        ),
        "국적": dict(
            hanja="國籍", meaning="nationality",
            characters=[("國", "국", "country — as in 국가, 국민"),
                        ("籍", "적", "a register — as in 호적, 본적")],
            notes=["The standing by which one is recognised as a national "
                   "of a country. Korea grants 국적; some countries grant "
                   "시민권 instead."],
        ),
        "권리": dict(
            hanja="權利", meaning="a right, a claim one may make",
            characters=[("權", "권", "power, right — as in 권력, 인권"),
                        ("利", "리", "benefit — as in 이익, 국익")],
        ),
        "의무": dict(
            hanja="義務", meaning="a duty, an obligation",
            characters=[("義", "의", "righteousness — as in 정의, 의무"),
                        ("務", "무", "task, duty — as in 업무, 공무원")],
        ),
        "기준": dict(
            hanja="基準", meaning="a standard, the basis for a decision",
            characters=[("基", "기", "a base — as in 기본, 기초"),
                        ("準", "준", "a level, a rule — as in 준비, 표준")],
        ),
        "유형": dict(
            hanja="類型", meaning="a kind, a type",
            characters=[("類", "류", "a kind, class — as in 종류, 인류"),
                        ("型", "형", "a form, mould — as in 형태, 모형")],
        ),
        "국가": dict(
            hanja="國家", meaning="a nation, a state",
            characters=[("國", "국", "country — as in 국적, 국민"),
                        ("家", "가", "house, family — as in 가족, 가정")],
        ),
        "인정받다": dict(
            hanja="認定받다", meaning="to be recognised (as)",
            characters=[("認", "인", "to acknowledge — as in 인식, 승인"),
                        ("定", "정", "to fix, settle — as in 결정, 지정")],
            surfaces=["인정받는"],
        ),
        "자격": dict(
            hanja="資格", meaning="standing, qualification, status",
            characters=[("資", "자", "resources, means — as in 자원, 투자"),
                        ("格", "격", "standard, rank — as in 성격, 합격")],
        ),
        "헌법": dict(
            hanja="憲法", meaning="the Constitution",
            characters=[("憲", "헌", "a constitution, a statute — as in 헌장"),
                        ("法", "법", "law")],
        ),
        "보장하다": dict(
            hanja="保障하다", meaning="to guarantee",
            characters=[("保", "보", "to protect — as in 보호, 보험"),
                        ("障", "장", "a barrier, to shield — as in 장애")],
            surfaces=["보장하는"],
        ),
        "일정하다": dict(
            hanja="一定하다", meaning="to be certain, fixed, regular",
            characters=[("一", "일", "one"),
                        ("定", "정", "to fix — the same 定 as in 인정")],
            surfaces=["일정한"],
        ),
        "수행하다": dict(
            hanja="遂行하다", meaning="to carry out, to fulfil",
            characters=[("遂", "수", "to accomplish"),
                        ("行", "행", "to act, go — as in 시행, 집행")],
            surfaces=["수행해야"],
        ),
        "영주권": dict(
            hanja="永住權", meaning="permanent residence (F-5)",
            characters=[("永", "영", "eternal, permanent — as in 영원"),
                        ("住", "주", "to dwell — as in 거주, 주거"),
                        ("權", "권", "right")],
        ),
        "상당히": dict(
            hanja="相當히", meaning="considerably, quite a lot",
            characters=[("相當", None, "considerable, fitting — 相 mutual, "
                                       "當 to be due")],
        ),
        "성인": dict(
            hanja="成人", meaning="an adult",
            characters=[("成", "성", "to become, complete — as in 성장, 구성원"),
                        ("人", "인", "person")],
            notes=["만 19세 이상 in Korean law."],
        ),
        "입대": dict(
            hanja="入隊", meaning="joining the army",
            characters=[("入", "입", "to enter — as in 입국, 입원"),
                        ("隊", "대", "a unit, a troop — as in 부대, 방범대")],
        ),
        "국적 제도": dict(
            meaning="a system of nationality",
            notes=["Korea grants 국적; the United States, Canada and "
                   "Australia grant 시민권, citizenship."],
        ),
        "시민권": dict(
            hanja="市民權", meaning="citizenship",
            characters=[("市民", None, "a citizen — 市 city, 民 people"),
                        ("權", "권", "right")],
        ),
        "운영하다": dict(
            hanja="運營하다", meaning="to run, to operate (a system)",
            characters=[("運", "운", "to move, carry — as in 운전, 운동"),
                        ("營", "영", "to manage — as in 경영, 자영업")],
            surfaces=["운영한다"],
        ),
        "각종": dict(
            hanja="各種", meaning="every kind of, various",
            characters=[("各", "각", "each — as in 각자, 각국"),
                        ("種", "종", "a kind — as in 종류, 품종")],
        ),
        "주체": dict(
            hanja="主體", meaning="the bearer, the agent (of a right or duty)",
            characters=[("主", "주", "main, master — as in 주인, 주권"),
                        ("體", "체", "body — as in 신체, 단체")],
        ),
        "출생지주의": dict(
            hanja="出生地主義", meaning="the birthplace principle (jus soli)",
            characters=[("出生地", None, "place of birth"),
                        ("主義", None, "-ism, principle")],
            notes=["Also called 속지주의 — the territorial principle."],
        ),
        "중시하다": dict(
            hanja="重視하다", meaning="to give weight to, to regard as important",
            characters=[("重", "중", "heavy, important — as in 중요, 존중"),
                        ("視", "시", "to look at — as in 시청, 무시")],
            surfaces=["중시한다"],
        ),
        "혈통주의": dict(
            hanja="血統主義", meaning="the bloodline principle (jus sanguinis)",
            characters=[("血統", None, "bloodline — 血 blood, 統 lineage"),
                        ("主義", None, "-ism, principle")],
            notes=["Also called 속인주의 — the personal nationality principle. "
                   "Korea follows it."],
        ),
        "국적법": dict(
            hanja="國籍法", meaning="the Nationality Act",
            notes=["Sets out what makes someone a Korean national. Amended "
                   "in December 2018 to require the national oath."],
        ),
        "분명하다": dict(
            hanja="分明하다", meaning="to be clear, evident",
            characters=[("分", "분", "to divide — as in 구분, 신분"),
                        ("明", "명", "bright, clear — as in 명확, 설명")],
            surfaces=["분명하지"],
        ),
        "무국적자": dict(
            hanja="無國籍者", meaning="a stateless person",
            characters=[("無", "무", "without — as in 무료, 무비자"),
                        ("國籍", None, "nationality"),
                        ("者", "자", "person")],
        ),
        "본국": dict(
            hanja="本國", meaning="one’s own country",
            characters=[("本", "본", "origin, main — as in 기본, 본인"),
                        ("國", "국", "country")],
        ),
        "대사관": dict(
            hanja="大使館", meaning="an embassy",
            characters=[("大使", None, "an ambassador — 大 great, 使 envoy"),
                        ("館", "관", "a hall, an establishment — as in 도서관")],
        ),
        "미등록 외국인": dict(
            hanja="未登錄外國人", meaning="an unregistered foreigner",
            characters=[("未", "미", "not yet — as in 미혼, 미성년"),
                        ("登錄", None, "registration")],
        ),
        "무국적": dict(
            hanja="無國籍", meaning="statelessness, having no nationality",
        ),
        "유엔아동권리위원회": dict(
            meaning="the UN Committee on the Rights of the Child",
        ),
        "보편적 출생 등록 제도": dict(
            hanja="普遍的出生登錄制度", meaning="universal birth registration",
            characters=[("普遍的", None, "universal — 普 widespread, 遍 all over"),
                        ("出生", None, "birth"),
                        ("登錄", None, "registration")],
        ),
        "요청하다": dict(
            hanja="要請하다", meaning="to request, to call on",
            characters=[("要", "요", "to need, require — as in 요건, 요구"),
                        ("請", "청", "to ask — as in 신청, 청문회")],
            surfaces=["요청하고"],
        ),
        "법률안": dict(
            hanja="法律案", meaning="a bill (a proposed law)",
            characters=[("法律", None, "law, legislation"),
                        ("案", "안", "a plan, a draft — as in 법안, 방안")],
        ),
        "논의하다": dict(
            hanja="論議하다", meaning="to discuss, to deliberate",
            characters=[("論", "론", "to argue — as in 논쟁, 이론"),
                        ("議", "의", "to deliberate — as in 회의, 국회의원")],
            surfaces=["논의하고"],
        ),
        "의지": dict(
            hanja="意志", meaning="will, determination",
            characters=[("意", "의", "intention — as in 의견, 합의"),
                        ("志", "지", "aspiration, purpose — as in 지원, 의지")],
        ),
        "요건": dict(
            hanja="要件", meaning="a requirement, a condition to be met",
            characters=[("要", "요", "to require — the same 要 as in 요청"),
                        ("件", "건", "a case, an item — as in 조건, 사건")],
        ),
        "갖추다": dict(
            meaning="to have ready, to meet (a requirement)",
            surfaces=["갖춘"],
        ),
        "장관": dict(
            hanja="長官", meaning="a minister (head of a ministry)",
            characters=[("長", "장", "head, long — as in 장기, 시장"),
                        ("官", "관", "an official — as in 관공서, 관할")],
            notes=["법무부 장관 — the Minister of Justice, who grants "
                   "naturalisation."],
        ),
        "허가": dict(
            hanja="許可", meaning="permission, leave",
            characters=[("許", "허", "to allow — as in 허락, 특허"),
                        ("可", "가", "possible — as in 가능")],
        ),
        "일반귀화": dict(
            hanja="一般歸化", meaning="general naturalisation",
            notes=["Five years’ continuous residence, F-5 status, 19 or "
                   "over, good conduct, a livelihood, basic Korean."],
        ),
        "간이귀화": dict(
            hanja="簡易歸化", meaning="simplified naturalisation",
            characters=[("簡易", None, "simple, easy — 簡 brief, 易 easy")],
            notes=["For a foreigner with a connection to Korea — a Korean "
                   "parent, or marriage to a Korean national."],
        ),
        "특별귀화": dict(
            hanja="特別歸化", meaning="special naturalisation",
            notes=["For a foreigner with a Korean parent, one who has "
                   "rendered special service, or one of outstanding "
                   "ability."],
        ),
        "혈연적": dict(
            hanja="血緣的", meaning="of blood, related by blood",
            characters=[("血緣", None, "blood ties — 血 blood, 緣 connection")],
        ),
        "지연적": dict(
            hanja="地緣的", meaning="of place, connected by locality",
            characters=[("地緣", None, "ties of place — 地 land, 緣 connection")],
        ),
        "품행": dict(
            hanja="品行", meaning="conduct, behaviour",
            characters=[("品", "품", "quality, article — as in 품질, 상품"),
                        ("行", "행", "to act — as in 행동, 수행")],
        ),
        "단정하다": dict(
            hanja="端正하다", meaning="to be neat, proper, well-conducted",
            characters=[("端", "단", "an end, upright — as in 단정"),
                        ("正", "정", "right, correct — as in 정의, 정당")],
            surfaces=["단정하고"],
        ),
        "생계유지": dict(
            hanja="生計維持", meaning="maintaining a livelihood",
            characters=[("生計", None, "livelihood — as in 생계비"),
                        ("維持", None, "maintenance — 維 to hold, 持 to keep")],
        ),
        "소양": dict(
            hanja="素養", meaning="attainments, the grounding one has",
            characters=[("素", "소", "plain, basic — as in 소재, 요소"),
                        ("養", "양", "to nurture — as in 양육, 교양")],
        ),
        "혼인": dict(
            hanja="婚姻", meaning="marriage (the legal act)",
            characters=[("婚", "혼", "marriage — as in 결혼, 기혼"),
                        ("姻", "인", "marriage ties")],
        ),
        "해당하다": dict(
            hanja="該當하다", meaning="to fall under, to be applicable",
            characters=[("該", "해", "that, the said"),
                        ("當", "당", "to be due, fitting — as in 정당, 상당")],
            surfaces=["해당한다"],
        ),
        "배우자": dict(
            hanja="配偶者", meaning="a spouse",
            characters=[("配", "배", "to match, distribute — as in 배송, 택배"),
                        ("偶", "우", "a pair, a mate"),
                        ("者", "자", "person")],
        ),
        "공로": dict(
            hanja="功勞", meaning="service, meritorious contribution",
            characters=[("功", "공", "merit, achievement — as in 성공, 공적"),
                        ("勞", "로", "labour — as in 노동, 근로")],
        ),
        "특정": dict(
            hanja="特定", meaning="particular, specified",
            characters=[("特", "특", "special — as in 특별, 특징"),
                        ("定", "정", "to fix — as in 지정, 결정")],
        ),
        "우수하다": dict(
            hanja="優秀하다", meaning="to be outstanding, excellent",
            characters=[("優", "우", "superior — as in 우선, 우대"),
                        ("秀", "수", "excellent, elegant")],
            surfaces=["우수한"],
        ),
        "보유": dict(
            hanja="保有", meaning="holding, possessing",
            characters=[("保", "보", "to keep — as in 보호, 보장"),
                        ("有", "유", "to have — as in 유효, 소유")],
        ),
        "국익": dict(
            hanja="國益", meaning="the national interest",
            characters=[("國", "국", "country"),
                        ("益", "익", "benefit — as in 이익, 유익")],
        ),
        "국민선서": dict(
            hanja="國民宣誓", meaning="the national oath",
            characters=[("國民", None, "the people, a national"),
                        ("宣誓", None, "an oath — 宣 to proclaim, 誓 to swear")],
            notes=["Required since the Nationality Act was amended in "
                   "December 2018."],
        ),
        "가족관계등록부": dict(
            hanja="家族關係登錄簿", meaning="the family relation register",
            characters=[("家族關係", None, "family relations"),
                        ("登錄簿", None, "a register — 簿 a ledger")],
            notes=["Created once a naturalised person has taken the oath; "
                   "it records identity and family relations."],
        ),
        "개정": dict(
            hanja="改正", meaning="amendment (of a law)",
            characters=[("改", "개", "to change, reform — as in 개선, 개혁"),
                        ("正", "정", "right, correct")],
        ),
        "시행되다": dict(
            hanja="施行되다", meaning="to take effect, to be put into force",
            characters=[("施", "시", "to carry out — as in 시설, 실시"),
                        ("行", "행", "to act")],
            surfaces=["시행되었다"],
        ),
        "회복": dict(
            hanja="回復", meaning="restoration, recovery",
            characters=[("回", "회", "to turn, return — as in 회의, 회식"),
                        ("復", "복", "to restore — as in 복구, 복지")],
            notes=["국적 회복 is regaining a nationality once held."],
        ),
        "국적증서": dict(
            hanja="國籍證書", meaning="the certificate of nationality",
        ),
        "수여식": dict(
            hanja="授與式", meaning="a conferment ceremony",
            characters=[("授與", None, "to confer, award — 授 to give, 與 to grant"),
                        ("式", "식", "a ceremony — as in 결혼식, 형식")],
        ),
        "준수하다": dict(
            hanja="遵守하다", meaning="to abide by, to observe (a law)",
            characters=[("遵", "준", "to obey — the same 遵 as in 준법 정신"),
                        ("守", "수", "to guard, keep — as in 수호, 보수")],
            surfaces=["준수하고"],
        ),
        "책임": dict(
            hanja="責任", meaning="responsibility",
            characters=[("責", "책", "to hold to account — as in 책임감"),
                        ("任", "임", "a duty, to entrust — as in 임명, 담임")],
        ),
        "엄숙히": dict(
            hanja="嚴肅히", meaning="solemnly",
            characters=[("嚴", "엄", "strict, stern — as in 엄격"),
                        ("肅", "숙", "solemn, quiet")],
        ),
        "선서하다": dict(
            hanja="宣誓하다", meaning="to swear, to take an oath",
            surfaces=["선서합니다"],
        ),
        "등록기준지": dict(
            hanja="登錄基準地", meaning="the registration base (place of record)",
            notes=["The place a Korean national’s family register is kept — "
                   "the successor to the old 본적."],
        ),
        "통보하다": dict(
            hanja="通報하다", meaning="to notify",
            characters=[("通", "통", "to pass, communicate — as in 통과, 통역"),
                        ("報", "보", "to report — as in 보고, 정보")],
            surfaces=["통보하면"],
        ),
        "다큐멘터리": dict(meaning="a documentary"),
        "출입국사무소": dict(
            hanja="出入國事務所", meaning="the immigration office",
            notes=["Now called 출입국·외국인청 — chapter 31."],
        ),
        "이동": dict(
            hanja="移動", meaning="movement, moving about",
            characters=[("移", "이", "to move — as in 이주, 이사"),
                        ("動", "동", "to move — as in 활동, 운동")],
        ),
        "스스로": dict(meaning="oneself, of one’s own accord"),
    },

    extraNotes=[
        "The MBC news still on p. 170, the permanent resident card on p. 171, "
        "the hands photograph on p. 171 and the oath ceremony photograph on "
        "p. 172 are not reproduced; their captions are. The 팜티프엉 caption "
        "under the news still is set as a source line.",
        "The eight steps of the 귀화 절차 on p. 172 are printed as one box with "
        "arrows between them; they are set here as a single item with the "
        "arrows kept. The book numbers them 1-8 but prints no 6.",
        "The review gaps on p. 173 are blank in the book and left blank here.",
    ],
)
