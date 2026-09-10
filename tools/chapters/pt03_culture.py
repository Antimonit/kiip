# -*- coding: utf-8 -*-
"""제3편 문화 — the spread that closes the part, pp. 104-107.

Not a chapter: every 편 ends with four pages of its own — 대단원 정리 and a
가로세로 퀴즈, then 단원 종합 평가, then two illustrated features. Transcribed
from the photos.

Your worked answers on p. 105 are carried: ④ for question 3 and ② for
question 5, which you marked. The rest of the 종합 평가 answers and the
crossword answers are mine, worked out from chapters 13-19. The book keeps
its own in 정답보기 on p. 262, which is not photographed, so if one of mine is
wrong the book is not to blame.
"""

from . import SECTION, HEADING, PARAGRAPH, BULLET, FIGURE, TABLE

PART = dict(
    number=3, slug="part-3", part=True,
    unit="문화", title="대단원 마무리", titleEn="Closing the part",

    append=[
        SECTION("summary", "대단원 정리"),
        TABLE([["전통 가치",
                "효와 예절: 높임말, 웃어른 공경 / 공동체와 연고 중시: ‘우리, 함께’를 중요시함"],
               ["전통 의식주",
                "한국 음식: 밥, 국, 반찬이 기본 식단 / 한복: 바지와 저고리(남자), 치마와 "
                "저고리(여자) / 한옥: 기와집과 초가집"],
               ["의례", "결혼식: 부부가 되는 의례 / 장례식: 사람이 죽었을 때 치르는 의례"],
               ["명절",
                "설날: 음력 1월 1일, 떡국을 먹으며 건강과 장수를 기원 / 추석: 음력 8월 15일, "
                "한 해 농사에 감사하는 전통에서 유래"],
               ["종교", "한국은 불교와 유교, 천주교와 개신교 등과 같은 종교를 누구나 자유롭게 가질 수 있음"],
               ["대중문화",
                "한국의 인기 있는 대중문화: 드라마, 음악과 노래(K-POP), 영화, 스포츠, 예능 프로그램 등"],
               ["여가문화", "일과 생활이 균형 잡힌 삶을 살아가기 위해서는 여가활동이 필요함"]]),
        HEADING(4, "찾아볼 곳"),
        BULLET("문화체육관광부 — www.mcst.go.kr"),
        BULLET("남산골한옥마을 — www.hanokmaeul.or.kr"),
        BULLET("전통문화포털 — www.kculture.or.kr"),
        BULLET("한식포털 — www.hansik.or.kr"),
        BULLET("한국예절문화원 — www.etiquette.or.kr"),
        BULLET("대한민국 구석구석 — korean.visitkorea.or.kr"),

        SECTION("quiz", "가로 세로 퀴즈"),
        FIGURE("일곱 칸씩 가로세로로 짜인 낱말 퍼즐 판. 가로 열쇠 ㉮~㉱와 세로 열쇠 ①~④가 시작하는 "
               "칸에 번호가 적혀 있다."),
        HEADING(4, "가로 열쇠"),
        BULLET("㉮ 한옥의 중요한 특징으로 아궁이에 불을 때어 방을 따뜻하게 하는 난방 장치 ( 온돌 )"),
        BULLET("㉯ 추석은 ○○○ 또는 가배라고도 불림 ( 한가위 )"),
        BULLET("㉰ 석가모니가 만든 종교로 중국을 거쳐 4세기 무렵 삼국 시대에 들어옴 ( 불교 )"),
        BULLET("㉱ 사람이 죽었을 때, 예를 갖추어 돌아가신 분을 보내는 의례 ( 장례식 )"),
        HEADING(4, "세로 열쇠"),
        BULLET("① 아이가 태어난 지 1년이 되는 첫 번째 생일 ( 돌 )"),
        BULLET("② 한국의 대중문화가 여러 나라로 확산되면서 대중적 인기를 끌게 된 현상 ( 한류 )"),
        BULLET("③ 개신교 예배는 ○○에서 드림 ( 교회 )"),
        BULLET("④ 남자와 여자가 부부가 되기로 서약하는 의례 ( 결혼식 )"),

        SECTION("exam", "단원 종합 평가"),
        HEADING(4, "01 〈보기〉의 설날에 먹는 음식에 대한 설명 중 ㉠과 ㉡에 들어갈 용어로 적합한 것은?"),
        PARAGRAPH("차례와 세배를 마친 후에는 떡국을 먹는다. 떡국은 흰 가래떡을 얇게 썰어 끓인 것으로 "
                  "설날의 대표적인 음식이다. 흰 가래떡은 ㉠와과 ㉡을/를 상징하며, 떡국 한 그릇을 먹으면 "
                  "나이도 한 살 더 먹는다는 의미가 담겨 있다."),
        BULLET("① 건강 — 장수"),
        BULLET("② 장수 — 희망"),
        BULLET("③ 장수 — 기쁨"),
        BULLET("④ 건강 — 기쁨"),
        PARAGRAPH("정답 ( ① )"),

        HEADING(4, "02 〈보기〉의 빈 칸에 공통으로 들어갈 알맞은 말은?"),
        PARAGRAPH("설날 아침에는 {조상}에게 감사하는 의식인 {차례}를 지낸다. 그리고 부모님 또는 "
                  "{조부모님} 등 집안의 {윗사람}에게 (   )를 한다. (   )를 받은 윗사람은 자녀 등 "
                  "아랫사람에게 한 해 동안 건강하고 잘 지내라고 {덕담}을 한다."),
        BULLET("① {성묘}"),
        BULLET("② {세배}"),
        BULLET("③ {벌초}"),
        BULLET("④ {연날리기}"),
        PARAGRAPH("정답 ( ② )"),

        HEADING(4, "03 다음 중 한국의 식사 예절로 옳은 것을 〈보기〉에서 모두 고른 것은?"),
        BULLET("ㄱ. 숟가락과 젓가락을 동시에 들고 사용한다."),
        BULLET("ㄴ. 밥그릇이나 국그릇을 손으로 들고 먹는다."),
        BULLET("ㄷ. {웃어른}이 먼저 {수저}를 들 때까지 기다린다."),
        BULLET("ㄹ. 입안에 음식이 있을 때에는 {가급적} 말하지 않는다."),
        BULLET("① ㄱ, ㄴ"),
        BULLET("② ㄱ, ㄹ"),
        BULLET("③ ㄴ, ㄷ"),
        BULLET("④ ㄷ, ㄹ"),
        PARAGRAPH("정답 ( ④ )"),

        HEADING(4, "04 다음 중 한국에서 창시된 종교가 아닌 것은?"),
        BULLET("① {유교}"),
        BULLET("② {원불교}"),
        BULLET("③ {대종교}"),
        BULLET("④ {천도교}"),
        PARAGRAPH("정답 ( ① )"),

        HEADING(4, "05 한국의 여가문화에 대한 설명으로 옳은 것은?"),
        BULLET("① 영화 관람의 경우 반드시 영화관에 직접 가서 표를 구매해야 한다."),
        BULLET("② 주 52시간 근무제가 {도입되면서|도입되다} 여가의 중요성이 더욱 높아졌다."),
        BULLET("③ 행정복지센터나 평생학습관에서 운영하는 여가 프로그램은 모두 무료이다."),
        BULLET("④ 자신이 좋아하거나 배우고 싶은 것을 다른 사람들과 함께 공유하기는 불가능하다."),
        PARAGRAPH("정답 ( ② )"),

        HEADING(4, "06 〈보기〉의 빈 칸에 공통으로 들어갈 알맞은 말은?"),
        PARAGRAPH("제사를 지낼 때 가족이 함께 모여 {추모하는|추모하다} 마음으로 제사 음식 앞에서 조상에게 "
                  "절을 두 번 한다. 제사를 마친 후에는 가족들이 함께 모여 제사 음식을 나누어 먹는다. 이를 "
                  "(   )이라고 한다. (   )은 조상이 주는 복을 나누어 받는다는 의미가 담겨 있다."),
        BULLET("① 절"),
        BULLET("② 화장"),
        BULLET("③ {음복}"),
        BULLET("④ {문상}"),
        PARAGRAPH("정답 ( ③ )"),

        SECTION("feature", "한국의 세시풍속 이야기: 절기"),
        PARAGRAPH("기후 변화가 뚜렷한 한국은 예로부터 1년을 봄, 여름, 가을, 겨울 네 계절로 나누고 다시 "
                  "4계절을 24절기로 나누어 놓았다. 보통 한 절기와 다음 절기 사이에서는 평균 15일 가량의 "
                  "차이가 있고, 보통 한 달에 두 번 가량 절기가 들어있게 된다. 또한 계절에 따라 의미 있는 "
                  "날을 정해 놓고 기념하였는데 이러한 날들을 명절이라 한다. 이러한 절기나 명절에 따라 연례 "
                  "행사를 진행하였는데 이를 세시풍속이라 한다. 절기와 명절의 대표적인 예는 다음과 같다.",
                  "Korea, where the change of climate is marked, has long "
                  "divided the year into four seasons — spring, summer, "
                  "autumn, winter — and divided those four again into 24 "
                  "solar terms. There are about 15 days on average between "
                  "one term and the next, so about two terms fall in a month. "
                  "Days of significance were also set by the season and "
                  "marked, and those days are called 명절. Annual events were "
                  "held according to these terms and festivals, and that is "
                  "what 세시풍속 means. Here are the best-known of the terms "
                  "and the festivals."),
        HEADING(4, "[입춘] 양력 2월 4일"),
        PARAGRAPH("1년의 시작을 알리는 봄을 대표하는 절기인 입춘. 이날은 콩을 문이나 마루에 뿌려 악귀를 "
                  "쫓고 좋은 글귀를 써서 천장에 붙이곤 하였다. 봄이면 흔히 보이는 ‘입춘대길 立春大吉’이 "
                  "대표적인 예이다.",
                  "입춘, the term that stands for the spring announcing the "
                  "year’s beginning. On this day people would scatter beans "
                  "at the door or on the floor to drive off evil spirits, and "
                  "write a good phrase and paste it to the ceiling. The "
                  "‘입춘대길 立春大吉’ commonly seen in spring is the best-known "
                  "example."),
        HEADING(4, "[소서] 양력 7월 7일"),
        PARAGRAPH("소서. 즉 작은 여름이라 하는데, 이때부터 본격적인 무더위가 시작되며 각종 채소나 과일이 "
                  "풍성해진다. 특히 단오때부터 즐기기 시작하는 ‘국수’와 ‘수제비’ 등이 이 시기에 가장 맛이 "
                  "좋다고 한다.",
                  "소서 — the ‘lesser heat’. From this point the real heat "
                  "begins and vegetables and fruit of every kind grow "
                  "plentiful. ‘국수’ and ‘수제비’, which people begin to enjoy "
                  "from 단오, are said to taste best at this time."),
        HEADING(4, "[처서] 양력 8월 23일"),
        PARAGRAPH("여름이 지나 더위도 가시고 선선한 가을을 맞이하게 된다고 하여 처서라 불렀다. 처서가 "
                  "지나면 따가운 햇볕이 누그러져 풀이 더 자라지 않기 때문에 산소의 풀을 깎아 벌초를 한다.",
                  "It was called 처서 because summer passes, the heat goes and "
                  "a cool autumn is met. Once 처서 is past, the fierce sun "
                  "softens and the grass grows no further, so the grass on "
                  "the graves is cut in 벌초."),
        HEADING(4, "[동지] 양력 12월 22일"),
        PARAGRAPH("1년 중 밤이 가장 길고, 낮이 가장 짧은 날이다. 붉은 색의 팥죽을 먹어 귀신을 쫓는 풍습이 "
                  "지금까지 이어져 오고 있다. 팥죽에는 나이만큼 새알이라 불리는 떡을 넣었다.",
                  "The day with the longest night and the shortest day of the "
                  "year. The custom of eating red 팥죽 to drive off spirits has "
                  "carried on to this day. Into the 팥죽 went rice cakes called "
                  "새알, as many as one’s years."),
        FIGURE("네 절기 사진 — 입춘의 문에 붙인 입춘대길, 소서의 수제비, 처서의 들녘, 동지의 팥죽"),

        SECTION("feature", "한국의 세시풍속 이야기: 명절"),
        HEADING(4, "[설날] 음력 1월 1일"),
        PARAGRAPH("음력으로 한 해가 시작되는 새해 첫 달의 첫날, 서로에게 ‘새해 복 많이 받으세요.’라고 "
                  "인사하며 덕담을 나누는 풍습이 있는 명절",
                  "The first day of the first month of the new year on the "
                  "lunar calendar, the festival with the custom of greeting "
                  "one another with ‘새해 복 많이 받으세요’ and exchanging good "
                  "wishes."),
        HEADING(4, "[정월대보름] 음력 1월 15일"),
        PARAGRAPH("음력 정월보름날을 말하며 나쁜 일을 물리치고 좋은 일이 오기를 바라는 마음에서 부럼 "
                  "깨물기, 더위팔기, 귀밝이술 마시기, 줄다리기, 다리밟기, 고싸움, 돌싸움, 쥐불놀이 등을 "
                  "하는 명절",
                  "The fifteenth of the first lunar month: the festival at "
                  "which, in the hope of driving off ill fortune and drawing "
                  "in good, people crack nuts, ‘sell the heat’, drink "
                  "귀밝이술, hold tug-of-war, walk the bridges, and hold 고싸움, "
                  "돌싸움 and 쥐불놀이."),
        HEADING(4, "[삼짇날] 음력 3월 3일"),
        PARAGRAPH("다시 새로운 농사일을 시작할 시점에 겨울 동안 움츠렸던 몸과 마음을 펴고 한 해의 건강과 "
                  "평화를 비는 명절",
                  "The festival at which, as the new farming year is about to "
                  "begin, people stretch out the body and mind that had drawn "
                  "in over the winter and pray for health and peace for the "
                  "year."),
        HEADING(4, "[단오] 음력 5월 5일"),
        PARAGRAPH("모내기를 끝내고 풍년을 기원하는 제사이기도 한 단오는 단오떡을 해먹고 여자는 창포물에 "
                  "머리를 감고 그네를 뛰며 남자는 씨름을 하면서 하루를 보내는 명절",
                  "단오, which is also the rite praying for a good harvest "
                  "once the rice planting is done: the festival where people "
                  "make and eat 단오떡, the women wash their hair in iris water "
                  "and ride the swings, and the men wrestle 씨름, spending the "
                  "day so."),
        HEADING(4, "[유두] 음력 6월 15일"),
        PARAGRAPH("신라 때부터 유래한 것으로, 나쁜 일을 떨어 버리기 위하여 동쪽으로 흐르는 물에 머리를 "
                  "감는 풍습이 있는 명절",
                  "Dating from the Silla period, the festival with the custom "
                  "of washing one’s hair in east-flowing water to shake off "
                  "ill fortune."),
        HEADING(4, "[추석] 음력 8월 15일"),
        PARAGRAPH("음력 팔월 보름을 일컫는 말로 가을의 한가운데 달이며 또한 팔월의 한가운데 날이라는 뜻을 "
                  "지니고 있는 연중 으뜸인 명절",
                  "The name for the fifteenth of the eighth lunar month: the "
                  "middle month of autumn and the middle day of the eighth "
                  "month, and the foremost festival of the year."),
        FIGURE("여섯 명절 사진 — 설날의 세배, 정월대보름의 부럼, 삼짇날의 화전, 단오의 그네, 유두, "
               "추석의 달과 토끼"),
    ],

    extraAnnotations={
        "조상": dict(
            hanja="祖上", meaning="an ancestor",
            characters=[("祖", "조", "ancestor — as in 조부모, 조상"),
                        ("上", "상", "above — as in 이상, 상급")],
        ),
        "차례": dict(
            hanja="茶禮", meaning="the ancestral rite held on a festival day",
            characters=[("茶", "차", "tea — as in 차, 다도"),
                        ("禮", "례", "rite, courtesy — as in 예절, 의례")],
            notes=["Held on the morning of 설날 and 추석; 제사 is the rite on "
                   "the anniversary of a death."],
        ),
        "조부모님": dict(
            hanja="祖父母님", meaning="grandparents",
            characters=[("祖", "조", "ancestor — the same 祖 as in 조상"),
                        ("父母", None, "parents")],
        ),
        "윗사람": dict(
            meaning="a senior, someone above one in age or standing",
        ),
        "덕담": dict(
            hanja="德談", meaning="words of blessing, a kind wish",
            characters=[("德", "덕", "virtue — as in 덕분, 미덕"),
                        ("談", "담", "to talk — as in 상담, 회담")],
        ),
        "성묘": dict(
            hanja="省墓", meaning="visiting an ancestor’s grave",
            characters=[("省", "성", "to reflect, to visit"),
                        ("墓", "묘", "a grave — as in 묘지, 성묘")],
        ),
        "세배": dict(
            hanja="歲拜", meaning="the new year bow",
            characters=[("歲", "세", "year, age — as in 만 65세, 세월"),
                        ("拜", "배", "to bow — as in 예배, 참배")],
        ),
        "벌초": dict(
            hanja="伐草", meaning="cutting the grass on a grave",
            characters=[("伐", "벌", "to cut down, to fell"),
                        ("草", "초", "grass — as in 초가집, 잡초")],
        ),
        "연날리기": dict(meaning="kite flying"),
        "웃어른": dict(meaning="an elder, one’s senior"),
        "수저": dict(meaning="spoon and chopsticks"),
        "가급적": dict(
            hanja="可及的", meaning="as far as possible, if possible",
            characters=[("可", "가", "possible — as in 가능, 허가"),
                        ("及", "급", "to reach — as in 보급, 급하다")],
        ),
        "유교": dict(
            hanja="儒敎", meaning="Confucianism",
            characters=[("儒", "유", "a Confucian scholar"),
                        ("敎", "교", "teaching, religion — as in 종교, 불교")],
            notes=["Not founded in Korea, which is what question 4 turns on."],
        ),
        "원불교": dict(
            hanja="圓佛敎", meaning="Won Buddhism",
            notes=["Founded by 박중빈 in 1916 — chapter 17’s table."],
        ),
        "대종교": dict(
            hanja="大倧敎", meaning="Daejonggyo",
            notes=["Founded by 나철 in 1909, tracing itself to 단군."],
        ),
        "천도교": dict(
            hanja="天道敎", meaning="Cheondogyo",
            notes=["Founded by 최제우 in 1860, first called 동학."],
        ),
        "도입되다": dict(
            hanja="導入되다", meaning="to be introduced, brought in",
            characters=[("導", "도", "to guide — as in 지도, 인도적"),
                        ("入", "입", "to enter — as in 입국, 수입")],
            surfaces=["도입되면서"],
        ),
        "추모하다": dict(
            hanja="追慕하다", meaning="to remember, to cherish the memory of",
            characters=[("追", "추", "to chase, to follow — as in 추구, 추적"),
                        ("慕", "모", "to long for, to admire")],
            notes=["The page prints 추모; 추모 and 추도 both appear for this, "
                   "추모 being the older form."],
            surfaces=["추모하는"],
        ),
        "음복": dict(
            hanja="飮福", meaning="sharing the food from an ancestral rite",
            characters=[("飮", "음", "to drink — as in 음식, 음주"),
                        ("福", "복", "blessing, fortune — as in 복, 축복")],
            notes=["Literally drinking the blessing: the family shares what "
                   "was offered, and so shares the ancestors’ blessing."],
        ),
        "문상": dict(
            hanja="問喪", meaning="paying a condolence call",
            characters=[("問", "문", "to ask — as in 질문, 문의"),
                        ("喪", "상", "mourning — as in 장례, 상주")],
        ),
    },

    extraNotes=[
        "제3편's closing spread runs pp. 104-107.",
        "The crossword grid is not reproduced; its clues are, with the "
        "answers covered. Those answers are mine, worked out from chapters "
        "13-19.",
        "The 종합 평가 answers to questions 3 and 5 are the ones you marked on "
        "p. 105; the rest are mine, since 정답보기 on p. 262 is not "
        "photographed. Your English glosses on that page are the entries for "
        "조상, 차례, 조부모님, 윗사람, 덕담, 성묘, 세배, 벌초, 연날리기, 웃어른, 수저, "
        "가급적, 유교, 원불교, 대종교, 천도교 and 도입되다.",
        "The photographs on pp. 106-107 are not reproduced; their captions "
        "and the text beside them are.",
    ],
)
