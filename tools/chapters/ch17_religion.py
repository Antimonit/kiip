# -*- coding: utf-8 -*-
"""Chapter 17 — Religion.

No Google Doc: yours stop at chapter 12. Transcribed from the photos of
pp. 92-95, so the Korean here is my reading of the page rather than yours,
and any error in it is mine.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, MARGIN, LABELS, FIGURE,
               TABLE, CELL, GLOSSARY, CHART)

CHAPTER = dict(
    number=17, slug="17-religion",
    unit="문화", title="종교", titleEn="Religion",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        MARGIN("{무신론자}"),
        PARAGRAPH("다음은 한국에 있는 다양한 {종교단체} 사진입니다."),
        LABELS("{절}", "{교회}", "{성당}", "{모스크}"),
        HEADING(4, "01 사진에 나와 있는 종교단체에 가 보았거나 들어 본 경험이 있습니까?"),
        HEADING(4, "02 출신국과 한국 종교생활의 공통점과 차이점은 무엇입니까?"),

        SECTION("goals", "학습목표"),
        BULLET("한국의 다양한 종교의 특징을 설명할 수 있다.", ordered=True),
        BULLET("다양한 종교를 존중하는 태도를 함양할 수 있다.", ordered=True),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", 2), "제목", "관련 내용"],
              [[CELL("기본", down=2), CELL("문화", down=2), "13. 전통 가치",
                "한국의 효와 예절"],
               ["15. 의례", "한국의 대표적인 의례, 제사"]]),

        SECTION("part", "01 한국에는 어떤 종교가 있을까?"),
        HEADING(2, "전통 신앙"),
        GLOSSARY(("신성", "신과 같이 거룩하고 성스러움", "신성"),
              ("천지신명", "하늘과 땅을 다스리는 거룩한 영적 존재", "천지신명"),
              ("숭배", "우러러 공경함", "숭배")),
        PARAGRAPH("옛날 사람들은 태양, 별, 바다, 나무 등과 같은 자연을 {신성}하게 여기거나 "
          "{천지신명}을 {숭배}하는 경우가 많았다. 이 같은 {전통 신앙}은 오랜 기간 이어졌고 "
          "지금도 일부 남아 있다."),

        HEADING(2, "불교와 유교"),
        GLOSSARY(("삼국 시대", "고구려, 백제, 신라 세 나라가 경쟁하던 시대", "삼국 시대"),
              ("자비", "다른 사람을 사랑하고 가엾게 여김", "자비"),
              ("서민", "신분이 높지 않은 사람이나 나랏일을 맡아 하지 않는 사람", "서민"),
              ("문화유산", "조상이 남긴 문화 중에서 후손에게 물려줄 만한 가치가 있는 것",
               "문화유산")),
        PARAGRAPH("{불교}는 {석가모니}가 만든 종교로, 중국을 거쳐 4세기 무렵 {삼국 시대}에 들어왔다. "
          "{자비}를 강조하는 불교는 왕과 {귀족}은 물론 {서민}의 삶에도 {깊숙이|깊숙하다} "
          "{파고들었다|파고들다}. {절}, {탑}, {불상} 등은 불교와 관련된 {문화유산}이다. "
          "{유교}도 중국을 통해 삼국 시대에 {전파}되었다. 특히 14세기 무렵 이후 한국인의 "
          "생활에 큰 영향을 미쳤다. 부모에 대한 {효도}, 웃어른에 대한 {예의}, 가족의 {결속}, "
          "조상을 위한 {제사} 등 유교의 전통은 현재까지도 남아 있다. 또한 유교 문화를 "
          "{토대}로 만들어진 교육 기관인 {향교}는 지금도 전국 곳곳에서 일부 운영되고 있다."),
        FIGURE("전국 각지에 있는 향교"),

        HEADING(2, "천주교와 개신교"),
        GLOSSARY(("서양", "유럽과 아메리카 지역", "서양")),
        PARAGRAPH("{기독교}는 {예수}의 가르침을 따르고 사랑의 {실천}을 강조하는 종교로, "
          "{천주교}(가톨릭)와 {개신교}로 나뉜다. 천주교는 17세기 무렵에 {서양}의 학문과 함께 "
          "들어왔다. 천주교를 종교가 아니라 학문으로 받아들인 {사례}는 한국이 거의 "
          "{유일하다}. 천주교 {미사}는 {성당}에서 드린다."),
        PARAGRAPH("개신교는 19세기에 서양의 {선교사}를 통해서 한국에 전파되었다. 개신교가 전파되는 "
          "과정에서 {교회}뿐 아니라 많은 학교와 병원이 만들어졌다. 개신교는 한국 {근대} 교육과 "
          "{보건}에 큰 영향을 준 것으로 평가 받는다. 개신교 {예배}는 교회에서 드린다."),

        HEADING(2, "그 밖의 종교"),
        PARAGRAPH("국제 {교류}가 활발해지면서 한국의 종교가 더욱 다양해지고 있다. {이슬람교}, "
          "{힌두교} 등을 종교로 가진 사람도 조금씩 늘고 있다. 한편, {천도교}, {대종교}, "
          "{원불교} 등 한국 {고유}의 종교도 계속 이어져 오고 있다."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "한국에서 창시된 종교 – 천도교, 대종교, 원불교"),
        TABLE(["종교명", "창시자", "창시 연도", "내용"],
              [["천도교", "최제우", "1860",
                "처음에는 동학이라 불렸으며, ‘사람이 곧 하늘’이라는 인내천 사상을 담고 있음"],
               ["대종교", "나철", "1909",
                "한국을 처음 세운 사람인 단군에서 비롯되었으며, 한국인이 단군의 후손임을 강조함"],
               ["원불교", "박중빈", "1916",
                "불교 신앙에서 비롯된 것으로 진리를 깨닫기 위해 노력하는 종교임"]]),

        SECTION("part", "02 종교 간의 배려와 존중이 왜 필요할까?"),
        HEADING(2, "현재 한국의 종교 현황"),
        GLOSSARY(("교리", "종교의 원리나 가르침", "교리")),
        CHART("종교 유형별 인구 비율(%)(통계청, 2015) — 원불교, 유교, 천도교와 기타는 "
              "합쳐도 1%에 미치지 못해 여기서는 생략했다.", "%",
              [("무교", 56.1), ("개신교", 19.7), ("불교", 15.5), ("천주교", 7.9)]),
        PARAGRAPH("한국은 자신이 원하는 종교를 자유롭게 믿을 수 있는 국가이다. 2015년 "
          "{인구통계} 조사에 따르면 한국 국민들 가운데 종교가 있다고 응답한 경우는 43.9%, "
          "종교가 없다고 응답한 ‘{무교}’의 경우는 56.1%이다. 나라에서 정한 종교인 {국교}나 "
          "특별히 {절대 다수}를 차지하고 있는 종교가 없다. 한국에서 종교는 다음과 같은 "
          "{기능}을 하고 있다. 첫째, {개인적} {차원}에서 종교는 {안정감}과 {행복감}을 "
          "제공한다. 둘째, 사회적 차원에서 종교는 공동체의 {유지}와 발전에 도움을 준다. 많은 "
          "종교 {단체}가 각자의 {교리}를 실천하는 과정에서 어려운 이웃을 돕는 활동을 하거나 "
          "외국인을 위한 교육과 문화 서비스를 지원하고 있는 것이 대표적인 예이다."),

        HEADING(2, "종교 간의 상호 배려와 존중"),
        GLOSSARY(("신도", "어떤 종교를 가지고 있는 사람", "신도")),
        PARAGRAPH("현재 한국 사회에서는 다양한 종교가 {공존}하고 있고 그것을 유지하려는 노력도 "
          "계속되고 있다. {신도} 수가 많은 불교와 기독교(천주교, 개신교)의 {기념일}은 각각 "
          "휴일로 지정되어 있다. 음력 4월 8일 불교의 기념일인 ‘{부처님 오신 날}’과 양력 12월 "
          "25일 기독교의 기념일인 ‘{성탄절}’이 그것이다. 최근에는 종교간 {화합} 차원에서 서로 "
          "다른 종교의 기념일을 축하해 주기도 한다."),
        PARAGRAPH("그리고 {대통령}은 종교 {지도자}들과 만남을 가지면서 한국 사회 {통합}에 대한 "
          "{논의}와 함께 {국정} 운영에 대한 {지혜}를 구하기도 한다. 한국의 종교는 앞으로 더욱 "
          "{다양성}을 띨 것으로 예상된다. 이와 함께 종교 간의 {상호} {배려}와 {존중}이 더욱 "
          "강조되어야 한다."),
        PARAGRAPH("한국 사회 {구성원}은 종교가 있든 없든 종교에 대한 {타인}의 생각을 이해하고, "
          "종교라는 것이 각자가 선택한 삶의 방식 중 하나라는 점을 {인식}하는 {태도}를 가져야 "
          "한다."),
        FIGURE("성북동성당에 걸린 부처님 오신 날 축하 현수막 (사진 출처: 〈연합뉴스〉)"),
        FIGURE("조계사에 설치된 성탄절 축하 트리 (사진 출처: 〈연합뉴스〉)"),
        FIGURE("대통령과 종교지도자 간담회 모습"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "종교의 자유는 헌법으로 보장된다"),
        PARAGRAPH("한국의 {헌법}에서는 국민이 누려야 할 {기본권} 중 종교의 자유를 다음과 같이 "
          "{보장}하고 있다."),
        BULLET("[헌법 제11조] 모든 국민은 법 앞에 {평등}하다. 누구든지 {성별}·종교 또는 사회적 "
          "신분에 의하여 정치적·경제적·사회적·문화적·생활의 모든 {영역}에 있어서 {차별}을 받지 "
          "아니한다."),
        BULLET("[헌법 제20조] 모든 국민은 종교의 자유를 가진다. 국교는 {인정}되지 아니하며, 종교와 "
          "정치는 {분리}된다."),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 한국에는 어떤 종교가 있을까?"),
        BULLET("(        )는 석가모니가 만든 종교로서 (        )를 베푸는 것을 강조하였으며, 이와 "
          "관련된 문화유산이 많이 남아 있다."),
        BULLET("기독교는 예수의 가르침을 따르고 사랑의 실천을 강조하는 종교로서 (        )와 "
          "(        )로 나뉜다."),
        BULLET("한국에서 만들어진 고유 종교로는 천도교, (        ), 원불교 등이 있다."),
        HEADING(3, "02 종교 간의 배려와 존중은 왜 필요할까?"),
        BULLET("한국에는 종교의 (        )가 있어서 자신이 원하는 종교를 가질 수 있고 종교를 갖지 "
          "않을 수도 있다."),
        BULLET("종교는 개인에게는 안정감과 행복감을 제공하고, 사회적으로는 (        )를 유지하고 "
          "발전시키는 데 도움을 준다."),
        BULLET("한국에서는 음력 4월 8일을 불교의 기념일인 (        )과 양력 12월 25일을 기독교의 "
          "기념일인 (        )을 휴일로 지정하고 있다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "마을을 지켜주는 장승과 솟대", translation=
          "장승 and 솟대, which keep watch over the village" "\n\n"
          "Leave the city in Korea for the countryside and you can see a "
          "장승 and a 솟대 standing at the entrance to a village. They are "
          "an important example of Korea’s traditional beliefs." "\n\n"
          "A 장승 is a post carved in the shape of a human head. People long "
          "ago believed that from the village entrance it kept the village "
          "safe. It also served to show the way." "\n\n"
          "A 솟대, on the other hand, is a bird made of stone or wood set on "
          "top of a long wooden pole. It was thought of above all as "
          "something that brought a good harvest — a year in which the "
          "farming went well — and good fortune. Like the 장승, it also "
          "carries the sense of protecting the village from misfortune, "
          "disease and natural disaster."),
        PARAGRAPH("한국에서 도시를 벗어나 시골에 가면 마을 {입구}에 있는 {장승}과 {솟대}를 볼 수 있다. "
          "장승과 솟대는 한국의 전통 신앙을 보여주는 중요한 사례이다."),
        PARAGRAPH("장승은 사람 머리 모양의 {기둥}을 가리킨다. 옛날 사람들은 장승이 마을 입구에서 마을을 "
          "안전하게 지켜준다고 믿었다. 장승은 길을 알려주는 기능도 담당했다."),
        PARAGRAPH("한편, 솟대는 긴 나무 {막대기} 위에 돌이나 나무로 만든 새로 올려놓은 것이다. 솟대는 "
          "특히 농사 일이 잘된 것을 가리키는 {풍년}과 {행운}을 가져다주는 {존재}로 여겨졌다. "
          "또한 장승과 마찬가지로 나쁜 일이나 {질병}, {자연재해}로부터 마을을 {보호}한다는 "
          "의미도 담고 있다."),
        FIGURE("장승"),
        FIGURE("솟대"),
        PARAGRAPH("★ 장승이나 솟대와 같이 자신의 고향 나라에서 전통 신앙에 해당하는 것이 있다면 소개해 "
          "봅시다.",
          "If your home country has something belonging to its traditional "
          "beliefs, as 장승 and 솟대 do, introduce it."),
    ],

    english={
        "전통 신앙": dict(
            title="The old beliefs",
            paragraphs=[
                "People long ago often held nature sacred — the sun, the "
                "stars, the sea, the trees — or worshipped the holy spirits "
                "that govern heaven and earth. Beliefs of that kind carried "
                "on for a great while, and some of them remain.",
            ],
        ),
        "불교와 유교": dict(
            title="Buddhism and Confucianism",
            paragraphs=[
                "Buddhism, the religion Sakyamuni founded, came by way of "
                "China around the fourth century, in the Three Kingdoms "
                "period. Stressing compassion, it worked deep into the lives "
                "of common people as well as of kings and nobles. Temples, "
                "pagodas and Buddha images are the cultural heritage it left. "
                "Confucianism too spread into the Three Kingdoms through "
                "China. From the fourteenth century onwards in particular it "
                "bore heavily on how Koreans lived. Its traditions are with us "
                "still: filial duty towards parents, courtesy towards elders, "
                "the solidarity of the family, the rites for the ancestors. "
                "The 향교, the school built on Confucian culture, is still "
                "kept up in places across the country.",
            ],
        ),
        "천주교와 개신교": dict(
            title="Catholicism and Protestantism",
            paragraphs=[
                "Christianity, which follows the teaching of Jesus and "
                "stresses love put into practice, divides into Catholicism "
                "and Protestantism. Catholicism arrived around the "
                "seventeenth century together with Western learning. Korea is "
                "almost the only case of a country that took Catholicism up "
                "as a body of learning rather than as a religion. The "
                "Catholic mass is held in a 성당.",

                "Protestantism was brought to Korea in the nineteenth century "
                "by Western missionaries. As it spread, many schools and "
                "hospitals were founded as well as churches. It is "
                "reckoned to have borne heavily on modern Korean education "
                "and public health. Protestant worship is held in a 교회.",
            ],
        ),
        "그 밖의 종교": dict(
            title="The other religions",
            paragraphs=[
                "As international exchange has grown busier, religion in "
                "Korea has grown more various. The number of people "
                "holding to Islam, to Hinduism and to others is rising a "
                "little at a time. Meanwhile Korea's own religions — 천도교, "
                "대종교, 원불교 — carry on as well.",
            ],
        ),
        "현재 한국의 종교 현황": dict(
            title="Where religion in Korea stands now",
            paragraphs=[
                "Korea is a country in which one may believe freely in "
                "whatever religion one wishes. By the population survey of "
                "2015, 43.9% of Koreans answered that they had a religion and "
                "56.1% answered that they had none. There is no state "
                "religion set by the country, and no religion holding an "
                "outright majority. Religion serves two functions here. "
                "First, for the individual, it offers a sense of steadiness "
                "and of happiness. Second, at the level of society, it helps "
                "hold a community together and carry it forward. The clearest "
                "instance is the many religious bodies that, in putting their "
                "own doctrine into practice, work to help neighbours in "
                "difficulty or support education and cultural services for "
                "foreign residents.",
            ],
        ),
        "종교 간의 상호 배려와 존중": dict(
            title="Care and respect between religions",
            paragraphs=[
                "Many religions live side by side in Korean society today, "
                "and the effort to keep it so goes on. The commemorative days "
                "of Buddhism and of Christianity, Catholic and Protestant, "
                "which have the largest numbers of adherents, are each set as "
                "public holidays. Those are the Buddha's birthday on the "
                "eighth of the fourth lunar month and Christmas on 25 "
                "December. Lately, in "
                "the interest of concord between religions, each has taken to "
                "offering the other congratulations on its day.",

                "The president also meets religious leaders, discussing the "
                "integration of Korean society with them and seeking their "
                "wisdom on the running of the state. Religion in Korea is "
                "expected to grow more various still. With that, care and "
                "respect between religions have all the more to be pressed "
                "for.",

                "Whether or not they hold a religion themselves, members of "
                "Korean society ought to take the attitude of understanding "
                "what others think about religion, and of recognising that a "
                "religion is one among the ways of living that each person "
                "chooses.",
            ],
        ),
    },

    extraAnnotations={
        "종교": dict(
            hanja="宗敎", meaning="religion",
            characters=[("宗", "종", "ancestor, sect — as in 종류 “kind”, 종파"),
                        ("敎", "교", "teaching — as in 교육, 유교, 불교")],
            notes=["The 敎 that ends the name of every religion here: 불교, "
                   "유교, 천주교, 개신교, 이슬람교."],
        ),
        "종교단체": dict(
            hanja="宗敎團體", meaning="a religious body",
            characters=[("團", "단", "group — as in 단체 “organisation”, 집단"),
                        ("體", "체", "body — as in 공동체, 정체성")],
        ),
        "무신론자": dict(
            hanja="無神論者", meaning="an atheist",
            characters=[("無", "무", "without — as in 무료 “free”, 무교"),
                        ("神", "신", "god, spirit — as in 신성, 천지신명"),
                        ("論", "론", "argument — as in 토론 “debate”, 논의"),
                        ("者", "자", "person — as in 신도의 가입자, 근로자")],
            notes=["Literally “one who argues there is no god”. Not the same "
                   "as 무교, which is simply having no religion."],
        ),
        "절": dict(
            meaning="a Buddhist temple",
            notes=["The pure-Korean word; 사(寺) is the Sino-Korean ending on "
                   "temple names, as in 조계사. The same syllable is also 절 "
                   "“a bow”, chapter 13's word."],
        ),
        "교회": dict(
            hanja="敎會", meaning="a Protestant church",
            characters=[("會", "회", "meeting, society — as in 사회, 향우회")],
        ),
        "성당": dict(
            hanja="聖堂", meaning="a Catholic church",
            characters=[("聖", "성", "holy — as in 신성 “sacred”"),
                        ("堂", "당", "hall — as in 식당, 봉안당")],
        ),
        "모스크": dict(
            meaning="a mosque",
            notes=["From the English. Korea's largest is the Seoul Central "
                   "Mosque in Itaewon."],
        ),
        "전통 신앙": dict(
            hanja="傳統信仰", meaning="the old folk beliefs",
            characters=[("信", "신", "to believe — as in 신용 “credit”, 통신"),
                        ("仰", "앙", "to look up to")],
            notes=["What was believed before the great religions arrived, and "
                   "what the 장승 and 솟대 of the last page belong to."],
        ),
        "신성": dict(
            hanja="神聖", meaning="sacred, holy",
            characters=[("神", "신", "god, spirit — as in 신명, 무신론자"),
                        ("聖", "성", "holy — as in 성당 “Catholic church”")],
        ),
        "천지신명": dict(
            hanja="天地神明", meaning="the spirits of heaven and earth",
            characters=[("天", "천", "heaven — as in 천주교, 천도교"),
                        ("地", "지", "earth — as in 지역 “region”, 지위"),
                        ("明", "명", "bright — as in 명당, 설명")],
        ),
        "숭배": dict(
            hanja="崇拜", meaning="worship",
            characters=[("崇", "숭", "to revere, lofty"),
                        ("拜", "배", "to bow — the same 拜 as in 세배")],
        ),
        "불교": dict(
            hanja="佛敎", meaning="Buddhism",
            characters=[("佛", "불", "Buddha — as in 불상 “Buddha image”, 원불교")],
        ),
        "석가모니": dict(
            hanja="釋迦牟尼", meaning="Sakyamuni, the Buddha",
            notes=["The characters transcribe the Sanskrit rather than "
                   "translating it. Shortened to 석가."],
        ),
        "삼국 시대": dict(
            hanja="三國時代", meaning="the Three Kingdoms period",
            characters=[("三", "삼", "three"),
                        ("國", "국", "country — as in 국가, 한국")],
            notes=["Goguryeo, Baekje and Silla, contending until Silla united "
                   "the peninsula in 676."],
        ),
        "자비": dict(
            hanja="慈悲", meaning="compassion, mercy",
            characters=[("慈", "자", "kind, loving"),
                        ("悲", "비", "sorrow — as in 비극 “tragedy”")],
            notes=["A Buddhist term: kindness that suffers along with what it "
                   "pities."],
        ),
        "귀족": dict(
            hanja="貴族", meaning="the nobility",
            characters=[("貴", "귀", "noble, precious — as in 존귀 “dignity”"),
                        ("族", "족", "clan — as in 가족, 친족, 유족")],
        ),
        "서민": dict(
            hanja="庶民", meaning="the common people",
            characters=[("庶", "서", "common, numerous"),
                        ("民", "민", "people — as in 국민, 이주민")],
        ),
        "깊숙하다": dict(meaning="to be deep inside, far in"),
        "파고들다": dict(
            meaning="to burrow into, to work its way in",
            notes=["파다 “to dig” + 들다 “to enter”. Used of an idea getting "
                   "right into something."],
        ),
        "탑": dict(
            hanja="塔", meaning="a pagoda",
            notes=["The stone tower in a temple courtyard, holding a relic. "
                   "Also the ordinary word for a tower."],
        ),
        "불상": dict(
            hanja="佛像", meaning="a Buddha image",
            characters=[("像", "상", "image, statue — as in 영상 “video”, 상징")],
        ),
        "문화유산": dict(
            hanja="文化遺産", meaning="cultural heritage",
            characters=[("遺", "유", "to leave behind — as in 유족, 유골"),
                        ("産", "산", "to produce, property — as in 생산, 재산")],
        ),
        "유교": dict(
            hanja="儒敎", meaning="Confucianism",
            characters=[("儒", "유", "the scholar, the Confucian")],
        ),
        "전파": dict(
            hanja="傳播", meaning="to spread, to propagate",
            characters=[("傳", "전", "to hand on — as in 전통, 전달"),
                        ("播", "파", "to sow, to scatter")],
        ),
        "효도": dict(
            hanja="孝道", meaning="filial duty",
            characters=[("孝", "효", "filial piety — chapter 13's 효"),
                        ("道", "도", "way — as in 도로, 황도")],
        ),
        "예의": dict(
            hanja="禮儀", meaning="manners, courtesy",
            characters=[("禮", "례", "rite, courtesy — as in 예절, 의례"),
                        ("儀", "의", "ceremony — as in 의례, 축의금")],
        ),
        "결속": dict(
            hanja="結束", meaning="solidarity, binding together",
            characters=[("結", "결", "to tie — as in 결혼, 체결"),
                        ("束", "속", "a bundle, to bind — as in 약속 “promise”")],
        ),
        "토대": dict(
            hanja="土臺", meaning="a foundation, a basis",
            characters=[("土", "토", "earth — as in 국토, 토양"),
                        ("臺", "대", "a platform — as in 무대 “stage”")],
        ),
        "향교": dict(
            hanja="鄕校", meaning="hyanggyo, a Confucian district school",
            characters=[("鄕", "향", "home village — as in 고향, 향우회"),
                        ("校", "교", "school — as in 학교, 등교")],
            notes=["The state school of the Joseon period, one to a district, "
                   "teaching the Confucian classics and holding the rites for "
                   "Confucius. Many of the buildings survive."],
        ),
        "기독교": dict(
            hanja="基督敎", meaning="Christianity",
            characters=[("基", "기", "base — as in 기본 “basic”, 기초"),
                        ("督", "독", "to oversee — as in 감독 “director”")],
            notes=["基督 transcribes “Christ”. The word covers both 천주교 and "
                   "개신교, though in everyday Korean it often means the "
                   "Protestant church alone."],
        ),
        "예수": dict(meaning="Jesus"),
        "실천": dict(
            hanja="實踐", meaning="putting into practice",
            characters=[("實", "실", "real — as in 사실 “fact”, 실질적"),
                        ("踐", "천", "to tread, to carry out")],
        ),
        "천주교": dict(
            hanja="天主敎", meaning="Catholicism",
            characters=[("天", "천", "heaven — as in 천지신명"),
                        ("主", "주", "master, lord — as in 주식 “staple”, 집주인")],
            notes=["天主, “the lord of heaven”, is how the Jesuit mission in "
                   "China rendered Deus. Korean Catholics were once called "
                   "천주학쟁이 — students of 천주 learning."],
        ),
        "개신교": dict(
            hanja="改新敎", meaning="Protestantism",
            characters=[("改", "개", "to reform — as in 개조, 개혁"),
                        ("新", "신", "new — as in 신정, 신랑")],
            notes=["Literally “the reformed religion”."],
        ),
        "서양": dict(
            hanja="西洋", meaning="the West",
            characters=[("西", "서", "west — as in 서울의 서, 서부"),
                        ("洋", "양", "ocean — as in 양옥 “Western-style house”")],
        ),
        "유일하다": dict(
            hanja="唯一하다", meaning="to be the only one",
            characters=[("唯", "유", "only, alone"),
                        ("一", "일", "one")],
        ),
        "미사": dict(meaning="the Catholic mass"),
        "예배": dict(
            hanja="禮拜", meaning="Protestant worship, a service",
            characters=[("禮", "례", "rite — as in 예절, 의례"),
                        ("拜", "배", "to bow — as in 세배, 숭배")],
        ),
        "선교사": dict(
            hanja="宣敎師", meaning="a missionary",
            characters=[("宣", "선", "to proclaim — as in 선언 “declaration”"),
                        ("師", "사", "master, teacher — as in 교사 “teacher”")],
        ),
        "근대": dict(
            hanja="近代", meaning="the modern era",
            characters=[("近", "근", "near — as in 최근 “recently”, 근처"),
                        ("代", "대", "generation, age — as in 시대, 현대")],
            notes=["In Korean history the period from the opening of the "
                   "ports in 1876 to liberation in 1945; 현대 is what comes "
                   "after."],
        ),
        "보건": dict(
            hanja="保健", meaning="public health",
            characters=[("保", "보", "to protect — as in 보험, 보건소"),
                        ("健", "건", "healthy — as in 건강 “health”")],
        ),
        "이슬람교": dict(hanja="이슬람敎", meaning="Islam"),
        "힌두교": dict(hanja="힌두敎", meaning="Hinduism"),
        "천도교": dict(
            hanja="天道敎", meaning="Cheondogyo, the Religion of the Heavenly Way",
            notes=["Founded by 최제우 in 1860 and first called 동학, “Eastern "
                   "learning”, against 서학, the Western learning of the "
                   "Catholics. Its doctrine is 인내천 — that a person is "
                   "heaven."],
        ),
        "대종교": dict(
            hanja="大倧敎", meaning="Daejonggyo, the religion of Dangun",
            notes=["Founded by 나철 in 1909, holding that Koreans descend "
                   "from 단군, the founder of the first Korean state. It grew "
                   "under Japanese rule as a nationalist faith."],
        ),
        "원불교": dict(
            hanja="圓佛敎", meaning="Won Buddhism",
            characters=[("圓", "원", "circle, round — as in 원 “a circle”")],
            notes=["Founded by 박중빈 in 1916 out of Buddhist belief. The 圓 "
                   "is the circle that stands for its truth."],
        ),
        "고유": dict(
            hanja="固有", meaning="proper to, native",
            characters=[("固", "고", "firm — as in 고정 “fixed”"),
                        ("有", "유", "to have — as in 특유, 유용하다")],
        ),
        "교류": dict(
            hanja="交流", meaning="exchange",
            characters=[("交", "교", "to cross, exchange — as in 교통, 교환"),
                        ("流", "류", "to flow — as in 유행 “fashion”")],
        ),
        "인구통계": dict(
            hanja="人口統計", meaning="population statistics, a census",
            characters=[("統", "통", "to govern, unify — as in 통합, 전통"),
                        ("計", "계", "to count — as in 계산 “calculation”, 계좌")],
        ),
        "무교": dict(
            hanja="無敎", meaning="having no religion",
            characters=[("無", "무", "without — as in 무료, 무상")],
            notes=["The answer 56.1% of Koreans gave in 2015 — the largest "
                   "single category."],
        ),
        "국교": dict(
            hanja="國敎", meaning="a state religion",
            notes=["Article 20 of the constitution says Korea has none."],
        ),
        "절대 다수": dict(
            hanja="絕對多數", meaning="an outright majority",
            characters=[("絕", "절", "to sever, absolute — as in 단절"),
                        ("對", "대", "against, pair — as in 대비, 반대"),
                        ("多", "다", "many — as in 다양 “various”, 다수")],
        ),
        "기능": dict(
            hanja="機能", meaning="a function",
            characters=[("機", "기", "machine, workings — as in 기관, 계기"),
                        ("能", "능", "ability — as in 가능, 능동적")],
        ),
        "개인적": dict(
            hanja="個人的", meaning="personal, individual",
            characters=[("個", "개", "individual — as in 개수 “number of items”")],
        ),
        "차원": dict(
            hanja="次元", meaning="a level, a dimension",
            characters=[("次", "차", "order, next — as in 차시, 절차"),
                        ("元", "원", "origin, principal — as in 원래 “originally”")],
            notes=["개인적 차원 “at the personal level”, 사회적 차원 “at the "
                   "level of society”. Also “dimension” in the geometric "
                   "sense."],
        ),
        "안정감": dict(
            hanja="安定感", meaning="a sense of steadiness",
            characters=[("安", "안", "peace, safe — as in 안전, 안부"),
                        ("定", "정", "to fix — as in 정착, 지정"),
                        ("感", "감", "to feel — as in 감사 “thanks”, 행복감")],
        ),
        "행복감": dict(hanja="幸福感", meaning="a sense of happiness"),
        "단체": dict(
            hanja="團體", meaning="an organisation, a body",
            characters=[("團", "단", "group — as in 종교단체, 집단")],
        ),
        "교리": dict(
            hanja="敎理", meaning="doctrine",
            characters=[("理", "리", "reason, principle — as in 이유, 관리")],
        ),
        "신도": dict(
            hanja="信徒", meaning="an adherent, a believer",
            characters=[("信", "신", "to believe — as in 신앙, 통신"),
                        ("徒", "도", "follower, disciple")],
        ),
        "공존": dict(
            hanja="共存", meaning="coexistence",
            characters=[("共", "공", "together — as in 공동체, 공공"),
                        ("存", "존", "to exist — as in 존재, 보존")],
        ),
        "기념일": dict(
            hanja="紀念日", meaning="a commemorative day",
            characters=[("紀", "기", "record, era"),
                        ("念", "념", "thought — as in 묵념, 기념")],
        ),
        "부처님 오신 날": dict(
            meaning="the Buddha's birthday",
            notes=["The eighth of the fourth lunar month, a public holiday. "
                   "Once called 석가탄신일; the plainer Korean name is now "
                   "official."],
        ),
        "성탄절": dict(
            hanja="聖誕節", meaning="Christmas",
            characters=[("聖", "성", "holy — as in 성당, 신성"),
                        ("誕", "탄", "to be born — as in 탄생 “birth”"),
                        ("節", "절", "season, festival — as in 명절, 절기")],
        ),
        "화합": dict(
            hanja="和合", meaning="concord, harmony",
            characters=[("和", "화", "harmony, peace — as in 평화 “peace”"),
                        ("合", "합", "to join — as in 통합, 조합원")],
        ),
        "대통령": dict(
            hanja="大統領", meaning="the president",
            characters=[("統", "통", "to govern — as in 통합, 전통"),
                        ("領", "령", "to lead, a territory — as in 영토")],
        ),
        "지도자": dict(
            hanja="指導者", meaning="a leader",
            characters=[("指", "지", "to point — as in 지정, 지시"),
                        ("導", "도", "to guide — as in 유도 “to induce”")],
        ),
        "통합": dict(
            hanja="統合", meaning="integration",
            notes=["The 통합 of 사회통합프로그램 — the course this book teaches."],
        ),
        "논의": dict(
            hanja="論議", meaning="discussion, deliberation",
            characters=[("論", "론", "to argue — as in 토론, 무신론자"),
                        ("議", "의", "to deliberate — as in 회의 “meeting”")],
        ),
        "국정": dict(
            hanja="國政", meaning="the running of the state",
            characters=[("政", "정", "government — as in 정치 “politics”, 정책")],
        ),
        "지혜": dict(
            hanja="智慧", meaning="wisdom",
            characters=[("智", "지", "wisdom, wit"),
                        ("慧", "혜", "bright, wise — as in 혜택 “benefit”'s 惠 "
                                    "is a different character")],
        ),
        "다양성": dict(
            hanja="多樣性", meaning="diversity",
            characters=[("樣", "양", "manner, shape — as in 모양 “shape”"),
                        ("性", "성", "nature, -ness — as in 전문성, 실용성")],
        ),
        "상호": dict(
            hanja="相互", meaning="mutual, each other",
            characters=[("相", "상", "mutual — as in 상부상조"),
                        ("互", "호", "each other")],
        ),
        "배려": dict(
            hanja="配慮", meaning="consideration, care for others",
            characters=[("配", "배", "to distribute, to match — as in 배정, 배달"),
                        ("慮", "려", "to consider — as in 고려 “consideration”")],
        ),
        "존중": dict(
            hanja="尊重", meaning="respect",
            characters=[("尊", "존", "to revere — as in 존경 “respect”, 존귀"),
                        ("重", "중", "heavy, important — as in 중요, 이중")],
        ),
        "구성원": dict(
            hanja="構成員", meaning="a member",
            characters=[("構", "구", "to construct — as in 구조 “structure”"),
                        ("成", "성", "to form — as in 구성, 성장"),
                        ("員", "원", "member — as in 조합원, 공무원")],
        ),
        "타인": dict(
            hanja="他人", meaning="another person, others",
            characters=[("他", "타", "other — as in 기타 “etcetera”")],
        ),
        "인식": dict(
            hanja="認識", meaning="recognition, awareness",
            characters=[("認", "인", "to recognise — as in 인정 “to accept”"),
                        ("識", "식", "to know — as in 지식 “knowledge”, 의식")],
        ),
        "태도": dict(
            hanja="態度", meaning="an attitude",
            characters=[("態", "태", "form, condition — as in 상태, 생태"),
                        ("度", "도", "degree — as in 정도 “degree”, 제도")],
        ),
        "헌법": dict(
            hanja="憲法", meaning="the constitution",
            characters=[("憲", "헌", "law, constitution"),
                        ("法", "법", "law — as in 법무부, 법적")],
        ),
        "기본권": dict(
            hanja="基本權", meaning="a fundamental right",
            characters=[("權", "권", "right, authority — as in 권익, 소유권")],
        ),
        "보장": dict(
            hanja="保障", meaning="to guarantee, to secure",
            characters=[("保", "보", "to protect — as in 보험, 보건"),
                        ("障", "장", "a barrier — as in 장애 “disability”")],
        ),
        "평등": dict(
            hanja="平等", meaning="equality",
            characters=[("平", "평", "flat, even — as in 평생, 평화"),
                        ("等", "등", "rank, equal — as in 등급 “grade”")],
        ),
        "성별": dict(
            hanja="性別", meaning="sex, gender",
            characters=[("別", "별", "to separate, other — as in 특별, 구별")],
        ),
        "영역": dict(
            hanja="領域", meaning="a domain, a sphere",
            characters=[("領", "령", "territory — as in 대통령"),
                        ("域", "역", "region — as in 지역 “region”, 권역")],
            notes=["The same 영역 that heads the 관련 단원 table."],
        ),
        "차별": dict(
            hanja="差別", meaning="discrimination",
            characters=[("差", "차", "difference — as in 차이 “difference”, 격차")],
        ),
        "인정": dict(
            hanja="認定", meaning="recognition; to acknowledge",
            characters=[("認", "인", "to recognise — as in 인식"),
                        ("定", "정", "to fix — as in 지정, 정착")],
        ),
        "분리": dict(
            hanja="分離", meaning="separation",
            characters=[("分", "분", "to divide — as in 부분, 분산"),
                        ("離", "리", "to leave, part — as in 이혼, 이착륙")],
            notes=["종교와 정치는 분리된다 — the separation of church and state, "
                   "in article 20."],
        ),
        "입구": dict(
            hanja="入口", meaning="an entrance",
            characters=[("入", "입", "to enter — as in 입학, 수입"),
                        ("口", "구", "mouth — as in 인구 “population”")],
        ),
        "장승": dict(
            meaning="jangseung, a village guardian post",
            notes=["A wooden or stone post carved with a face, set at the "
                   "entrance to a village to guard it and to mark the road."],
        ),
        "솟대": dict(
            meaning="sotdae, a bird pole",
            notes=["A tall pole with a bird of wood or stone on top, set up "
                   "for a good harvest. From 솟다 “to rise” + 대 “pole”."],
        ),
        "기둥": dict(meaning="a pillar, a post"),
        "막대기": dict(meaning="a stick, a rod"),
        "풍년": dict(
            hanja="豊年", meaning="a year of good harvest",
            characters=[("豊", "풍", "abundant — as in 풍요 “plenty”"),
                        ("年", "년", "year — as in 연령, 미성년자")],
            notes=["Its opposite is 흉년, a year of failed crops."],
        ),
        "행운": dict(
            hanja="幸運", meaning="good fortune",
            characters=[("幸", "행", "fortunate — as in 행복 “happiness”"),
                        ("運", "운", "to carry, fortune — as in 운동, 운영")],
        ),
        "존재": dict(
            hanja="存在", meaning="a being, existence",
            characters=[("存", "존", "to exist — as in 공존, 보존"),
                        ("在", "재", "to be at — as in 재외국민, 현재")],
        ),
        "질병": dict(
            hanja="疾病", meaning="disease",
            characters=[("疾", "질", "illness, swift"),
                        ("病", "병", "illness — as in 병원 “hospital”, 전염병")],
        ),
        "자연재해": dict(
            hanja="自然災害", meaning="a natural disaster",
            characters=[("災", "재", "calamity — as in 재난 “disaster”, 화재"),
                        ("害", "해", "harm — as in 손해 “loss”, 해롭다")],
        ),
        "보호": dict(
            hanja="保護", meaning="protection",
            characters=[("保", "보", "to protect — as in 보장, 보험"),
                        ("護", "호", "to guard — as in 간호 “nursing”")],
        ),
        "유지": dict(
            hanja="維持", meaning="to maintain, to keep up",
            characters=[("維", "유", "to tie, sustain"),
                        ("持", "지", "to hold — as in 지속 “continuation”")],
        ),
        "제사": dict(
            hanja="祭祀", meaning="the memorial rite for an ancestor",
            characters=[("祭", "제", "rite — as in 축제 “festival”"),
                        ("祀", "사", "to offer sacrifice")],
        ),
        "사례": dict(
            hanja="事例", meaning="a case, an instance",
            characters=[("事", "사", "affair — as in 사건, 무사하다"),
                        ("例", "례", "example — as in 예를 들어")],
        ),
    },

    extraNotes=[
        "Chapter 17 has no Google Doc: the Korean is transcribed from the "
        "photos of pp. 92-95 rather than from a transcription of yours, so "
        "mistakes in it are mine and it is worth reading against the pages.",
        "The figure on p. 94 is a pie chart of eight slices. Four of them — "
        "원불교, 유교, 천도교 and 기타 — are too small to read off the page and "
        "together come to under 1%, so only the four large ones are drawn and "
        "the caption says what is missing.",
        "Article 01 has four sub-headings rather than two, and article 02 has "
        "two. All six are translated.",
    ],
)
