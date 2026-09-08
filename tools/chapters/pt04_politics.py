# -*- coding: utf-8 -*-
"""제4편 정치 — the spread that closes the part, pp. 130-133.

Not a chapter: every 편 ends with four pages of its own — 대단원 정리 and a
가로세로 퀴즈, then 단원 종합 평가, then two illustrated features. Transcribed
from the photos.

The answers to the crossword and to the 종합 평가 are mine, worked out from
the chapters. The book keeps its own in 정답보기 on p. 262, which is not
photographed, so if one of mine is wrong the book is not to blame.
"""

from . import SECTION, HEADING, PARAGRAPH, BULLET, FIGURE, TABLE, VERSE

PART = dict(
    number=4, slug="part-4", part=True,
    unit="정치", title="대단원 마무리", titleEn="Closing the part",

    append=[
        SECTION("summary", "대단원 정리"),
        TABLE([["한국의 민주 정치", "정치와 민주주의 의미, 주권, 권력 분립"],
               ["입법부",
                "국회의 구성, 국회의원의 특권과 의무, 국회가 하는 일(입법, 국가 재정, 국정)"],
               ["행정부", "정부의 구성, 국무회의, 대통령의 권한, 정부가 하는 일"],
               ["사법부",
                "법원의 구성, 재판을 통한 권리 보호와 질서 유지, 공정한 재판을 위한 제도, "
                "재판의 종류"],
               ["선거와 지방자치",
                "선거의 의미, 선거의 4대 원칙, 선거의 종류, 지방자치제의 의미, "
                "지방자치의 모습"]]),
        HEADING(4, "찾아볼 곳"),
        BULLET("정부24 — www.gov.kr"),
        BULLET("청와대 — www.president.go.kr"),
        BULLET("대한민국 국회 — www.assembly.go.kr"),
        BULLET("중앙선거관리위원회 — www.nec.go.kr"),

        SECTION("quiz", "가로 세로 퀴즈"),
        FIGURE("일곱 칸씩 가로세로로 짜인 낱말 퍼즐 판. 가로 열쇠 ㉮~㉲와 세로 열쇠 ①~④가 "
            "시작하는 칸에 번호가 적혀 있다."),
        HEADING(4, "가로 열쇠"),
        BULLET("㉮ 주인으로서의 권리, 한국 국민은 국가의 주인으로서 이것을 가지고 있음 ( 주권 )"),
        BULLET("㉯ 국민의 기본권을 규정하고 있는 국가 최고의 법 ( 헌법 )"),
        BULLET("㉰ 국민에게 필요한 정책을 직접 집행하면서 나라의 살림을 하는 기관 ( 행정부 )"),
        BULLET("㉱ 대한민국 대통령이 일하는 곳 ( 청와대 )"),
        BULLET("㉲ 국민을 대표하는 기관인 국회의 구성원 ( 국회의원 )"),
        HEADING(4, "세로 열쇠"),
        BULLET("① 국민이 권력을 가지고 스스로 다스린다는 것을 의미하는 정치 제도 ( 민주주의 )"),
        BULLET("② 법을 적용하여 재판을 담당하는 기관 ( 사법부 )"),
        BULLET("③ 국회에서 필요한 경우에 당사자, 증인, 참고인 등을 불러 질문하고 사실이나 의견을 "
          "듣는 제도 ( 청문회 )"),
        BULLET("④ 공정한 재판을 위해 한 사건에 대하여 세 번 심판을 받을 수 있는 제도 ( 삼심제 )"),

        SECTION("exam", "단원 종합 평가"),
        HEADING(4, "01 한국의 민주주의 발전과 관계없는 것은?"),
        BULLET("① 4·19혁명"),
        BULLET("② 6월 항쟁"),
        BULLET("③ 6·25전쟁"),
        BULLET("④ 5·18 민주화 운동"),
        PARAGRAPH("정답 ( ③ )"),

        HEADING(4, "02 다음 중 선거의 기본 원칙에 속하지 않는 것은?"),
        BULLET("① 간접 선거"),
        BULLET("② 보통 선거"),
        BULLET("③ 평등 선거"),
        BULLET("④ 비밀 선거"),
        PARAGRAPH("정답 ( ① )"),

        HEADING(4, "03 다음 중 민주주의 국가의 특징에 해당하지 않는 것은?"),
        BULLET("① 국민의 대표를 국민이 직접 선출한다."),
        BULLET("② 권력을 가진 한 사람이 모든 것을 결정한다."),
        BULLET("③ 모든 국민이 나라의 주인으로서 권리를 갖는다."),
        BULLET("④ 국가 권력을 여러 기관에서 나누어 견제와 균형을 이룬다."),
        PARAGRAPH("정답 ( ② )"),

        HEADING(4, "04 〈보기〉의 ㉠, ㉡에서 설명하는 용어로 옳은 것은?"),
        VERSE("ㄱ. 지역 주민이 스스로 자기 지역의 대표자를 뽑아서 지역의 정치를 담당하도록 "
              "하는 제도.",
              "ㄴ. 공정한 재판을 위해 같은 사건에 대해 세 번까지 재판을 받을 수 있도록 한 제도."),
        BULLET("① 지방자치제 / 삼권분립"),
        BULLET("② 지방자치제 / 삼심제"),
        BULLET("③ 의원내각제 / 삼권분립"),
        BULLET("④ 의원내각제 / 삼심제"),
        PARAGRAPH("정답 ( ② )"),

        HEADING(4, "05 다음 〈보기〉에서 설명하는 기관으로 알맞은 곳은?"),
        VERSE("국무회의를 통해 국가의 주요 정책을 의논하고 결정한다.",
              "대통령이 최고 책임자이며, 국무총리, 장관 등이 속해 있는 기관이다."),
        BULLET("① 법무부"),
        BULLET("② 사법부"),
        BULLET("③ 입법부"),
        BULLET("④ 행정부"),
        PARAGRAPH("정답 ( ④ )"),

        HEADING(4, "06 다음 〈보기〉에서 선거에 대한 옳은 설명을 모두 고른 것은?"),
        VERSE("ㄱ. 친한 사람끼리는 비밀 선거의 원칙을 지킬 필요 없다.",
              "ㄴ. 선거는 국민이 자신을 대표할 사람을 직접 뽑는 것을 말한다.",
              "ㄷ. 보통 선거는 만 17세가 되면 국민 누구나 참여할 수 있는 것이다.",
              "ㄹ. 평등 선거는 조건에 관계없이 공평하게 1인 1표씩 투표하는 것이다."),
        BULLET("① ㄱ, ㄴ"),
        BULLET("② ㄱ, ㄷ"),
        BULLET("③ ㄷ, ㄹ"),
        BULLET("④ ㄴ, ㄹ"),
        PARAGRAPH("정답 ( ④ )"),

        SECTION("feature", "일상생활과 민주주의"),
        HEADING(3, "다수결"),
        PARAGRAPH("다양한 의견을 하나로 모으기 위해 많은 사람들의 의견에 따라 결정하는 것."),
        PARAGRAPH("{다수결} 결정 방식으로는 선거와 같은 대표자 선출, 학급 회장 선출, 학급에서 소풍 장소 "
          "결정 등이 있다."),
        FIGURE("교실에서 손을 들어 소풍 장소를 정하는 아이들 — 칠판에 ‘제12회 봄소풍 장소 투표’"),
        HEADING(3, "관용"),
        PARAGRAPH("자신의 신념만을 절대시하지 않고 다른 사람의 이익과 신념, 가치도 인정하고 {포용}하는 "
          "생각과 태도."),
        PARAGRAPH("{관용}은 민주주의의 {다양성}의 {전제}이며 {소수자}들이 어떠한 {탄압}이나 {소외} 없이 "
          "{더불어} 살아가는 것을 {보장}하는 데 있어 중요한 {요소}이다."),
        FIGURE("길에서 서로 다른 주장을 든 사람들이 마주 선 모습"),
        HEADING(3, "토론"),
        PARAGRAPH("어떤 문제에 대해 찬성과 반대의 의견을 말하며 {논의}하는 것."),
        PARAGRAPH("{토론}은 찬성하는 쪽과 반대하는 쪽이 있어서 서로 자기의 주장이 {옳음}을 "
          "{내세우며|내세우다} 각각 자기 쪽의 주장을 {받아들이도록|받아들이다} {상대방} 또는 "
          "{제3자}를 {설득}하는 것이다."),
        FIGURE("‘제2회 □△ 토론 대회’ — 찬성과 반대 표지를 놓고 마주 앉은 학생들"),
        HEADING(3, "타협"),
        PARAGRAPH("어떤 일을 서로 {양보}해서 {협의}하는 것."),
        PARAGRAPH("{타협}은 민주주의 {의사 결정} 과정에서 {합의}를 이끌어 내는 하나의 방식이다. 서로 "
          "다른 주장이 있을 때 서로의 {입장}에서 조금씩 {물러나|물러나다} 양보와 타협을 하게 "
          "되면 더 많은 사람이 {만족}할 만한 결과를 얻을 수도 있다."),
        FIGURE("돈주머니와 임금 인상을 놓고 악수하는 두 사람 — “올라간 게 조금이겠”, “네!”"),

        SECTION("feature", "한국 대통령과 만난 정상들"),
        PARAGRAPH("2020년 3월 G20 특별 {정상회의}는 주요 20개국 {협의체} 정상들이 {화상}으로 한자리에 "
          "모였다. 코로나19 {대응}을 위한 G20 특별 정상회의에서 한국은 {선제적}이고 {투명}한 "
          "{방역조치} 활동을 국제사회와 {공유}했다."),
        FIGURE("화상으로 열린 G20 특별 정상회의 (사진 출처: 청와대)"),
        PARAGRAPH("2019 한-{아세안} 특별 정상회의에 {참석}한 정상들과 {기념촬영} 모습이다. 2019 한-아세안 "
          "특별 정상회의 {공동 의장} {성명}에서 정상들은 1988년 한-아세안 {대화 관계} {수립} "
          "이후의 다양한 분야에서의 협력 {성과}를 높이 평가하면서 {안보}·{교역}·{첨단 산업}·"
          "{인적 교류} 등의 분야에서 협력을 {확대}하기로 했다. 기념촬영은 왼쪽부터 말레이시아 "
          "총리, 미얀마 {국가고문}, 필리핀 대통령, 싱가포르 총리, 태국 총리, 한국의 문재인 "
          "대통령, 베트남 총리, 브루나이 국왕, 캄보디아 {외교장관}, 인도네시아 대통령, 라오스 "
          "총리이다."),
        FIGURE("2019 한-아세안 특별 정상회의 기념촬영 (사진 출처: 청와대)"),
        PARAGRAPH("2017년 11월 제25차 APEC 정상회의는 베트남 다낭에서 {개최}되었다. 이번 정상회의에는 "
          "한국의 문재인 대통령과 미국 트럼프 대통령, 중국 시진핑 {국가주석}, 일본 아베 신조 "
          "총리, 러시아 블라디미르 푸틴 대통령 등 21개 {회원국} 정상이 모두 참석했다. 이들 정상은 "
          "‘새로운 {역동성} {창조}, 함께하는 미래만들기’를 {주제}로 {지속가능}하고 {혁신적}이며 "
          "{포용적} {성장} {증진}과 {역내} {경제통합} 등을 {집중적}으로 논의했다."),
        FIGURE("제25차 APEC 정상회의 (사진 출처: 청와대)"),
    ],

    english={
        "다수결": dict(
            title="Majority rule",
            paragraphs=[
                "Deciding a matter by the view of the greater number, so as to "
                "gather many views into one.",

                "Choosing representatives at an election, electing a class "
                "president, settling where a class will go on an outing are "
                "all decisions taken by majority.",
            ],
        ),
        "관용": dict(
            title="Tolerance",
            paragraphs=[
                "A cast of mind that does not hold one's own convictions to be "
                "absolute, but acknowledges and makes room for the interests, "
                "convictions and values of others.",

                "Tolerance is the premise of democracy's plurality, and an "
                "important part of guaranteeing that minorities may live "
                "alongside everyone else without oppression or exclusion of "
                "any kind.",
            ],
        ),
        "토론": dict(
            title="Debate",
            paragraphs=[
                "Talking a question over, with views stated for and against.",

                "In a debate there is a side in favour and a side against, "
                "each asserting that its own claim is the right one and each "
                "trying to persuade the other side, or a third party, to "
                "accept it.",
            ],
        ),
        "타협": dict(
            title="Compromise",
            paragraphs=[
                "Coming to terms on something, each side giving ground.",

                "Compromise is one of the ways agreement is reached in "
                "democratic decision-making. Where two claims differ, drawing "
                "back a little from each position and giving and taking may "
                "reach a result that more people can be satisfied with.",
            ],
        ),
    },

    extraAnnotations={
        "다수결": dict(
            hanja="多數決", meaning="a decision by majority",
            characters=[("多", "다", "many — as in 다양, 다문화"),
                        ("數", "수", "number — as in 과반수, 횟수"),
                        ("決", "결", "to decide — as in 결정, 판결")],
        ),
        "포용": dict(
            hanja="包容", meaning="embracing, accepting",
            characters=[("包", "포", "to wrap, to include — as in 포함"),
                        ("容", "용", "to contain, to allow — as in 허용, 내용")],
        ),
        "관용": dict(
            hanja="寬容", meaning="tolerance",
            characters=[("寬", "관", "broad, lenient"),
                        ("容", "용", "to allow — the same 容 as in 포용")],
        ),
        "다양성": dict(hanja="多樣性", meaning="diversity, plurality"),
        "전제": dict(
            hanja="前提", meaning="a premise, a precondition",
            characters=[("前", "전", "before — as in 사전 투표, 전주"),
                        ("提", "제", "to put forward — as in 제시, 제출")],
        ),
        "소수자": dict(
            hanja="少數者", meaning="a member of a minority",
            characters=[("少", "소", "few — as in 소년, 감소")],
        ),
        "탄압": dict(
            hanja="彈壓", meaning="oppression, suppression",
            characters=[("彈", "탄", "to flick, a bullet — as in 폭탄"),
                        ("壓", "압", "to press — as in 압력, 압수")],
        ),
        "소외": dict(
            hanja="疏外", meaning="exclusion, alienation",
            characters=[("疏", "소", "sparse, distant — as in 의사소통"),
                        ("外", "외", "outside — as in 외국, 제외")],
        ),
        "더불어": dict(
            meaning="together with, alongside",
            notes=["더불어 살다 “to live alongside others” — the phrase the "
                   "textbook keeps returning to. Also the 더불어 of "
                   "더불어민주당."],
        ),
        "보장": dict(hanja="保障", meaning="guarantee"),
        "요소": dict(
            hanja="要素", meaning="an element, a factor",
            characters=[("要", "요", "necessary — as in 중요, 필요"),
                        ("素", "소", "element, plain — as in 소재")],
        ),
        "논의": dict(hanja="論議", meaning="discussion"),
        "토론": dict(
            hanja="討論", meaning="debate",
            characters=[("討", "토", "to discuss, to attack — as in 검토"),
                        ("論", "론", "to argue — as in 논의, 이론")],
        ),
        "옳음": dict(meaning="being right, rightness"),
        "내세우다": dict(meaning="to put forward, to assert"),
        "받아들이다": dict(meaning="to accept, to take in"),
        "상대방": dict(
            hanja="相對方", meaning="the other party",
            characters=[("相", "상", "mutual — as in 상속, 수상"),
                        ("對", "대", "against, facing — as in 대비, 반대"),
                        ("方", "방", "side, direction — as in 방법, 지방")],
        ),
        "제3자": dict(hanja="第三者", meaning="a third party"),
        "설득": dict(
            hanja="說得", meaning="persuasion",
            characters=[("說", "설", "to explain — as in 설명, 소설"),
                        ("得", "득", "to obtain — as in 득표율, 소득")],
        ),
        "양보": dict(
            hanja="讓步", meaning="yielding, giving way",
            characters=[("讓", "양", "to yield, to concede"),
                        ("步", "보", "a step — as in 산책's 보행, 진보")],
            notes=["The word on the priority-seat signs: 양보해 주세요."],
        ),
        "협의": dict(
            hanja="協議", meaning="consultation, coming to terms",
            characters=[("協", "협", "to cooperate — as in 협력, 협의체"),
                        ("議", "의", "to deliberate — as in 회의, 의논")],
        ),
        "타협": dict(
            hanja="妥協", meaning="compromise",
            characters=[("妥", "타", "peaceful, settled"),
                        ("協", "협", "to cooperate — the same 協 as in 협의")],
        ),
        "의사 결정": dict(hanja="意思決定", meaning="decision-making"),
        "합의": dict(
            hanja="合意", meaning="agreement, consensus",
            characters=[("合", "합", "to join — as in 결합, 통합"),
                        ("意", "의", "intention — as in 동의, 의견")],
        ),
        "입장": dict(
            hanja="立場", meaning="a position, a standpoint",
            characters=[("立", "립", "to stand — as in 입법, 독립"),
                        ("場", "장", "place — as in 장면, 시장")],
            notes=["Not the 입장 “entry” (入場) of 입장료."],
        ),
        "물러나다": dict(meaning="to step back, to withdraw"),
        "만족": dict(
            hanja="滿足", meaning="satisfaction",
            characters=[("滿", "만", "full — as in 만원, 만점"),
                        ("足", "족", "foot, enough — as in 부족, 충족")],
        ),
        "정상회의": dict(
            hanja="頂上會議", meaning="a summit",
            characters=[("頂", "정", "summit, top"),
                        ("上", "상", "above — as in 상원, 이상")],
            notes=["정상 here is the peak, hence the heads of state — not the "
                   "정상 “normal” (正常) of 정상적."],
        ),
        "협의체": dict(hanja="協議體", meaning="a consultative body"),
        "화상": dict(
            hanja="畫像", meaning="video, a screen image",
            notes=["화상 회의 is a video conference. A different 화상 (火傷) is a "
                   "burn."],
        ),
        "대응": dict(
            hanja="對應", meaning="a response, countermeasures",
            characters=[("應", "응", "to respond — as in 응답, 적응")],
        ),
        "선제적": dict(
            hanja="先制的", meaning="pre-emptive",
            characters=[("先", "선", "first — as in 선생, 우선"),
                        ("制", "제", "to control — as in 제도, 통제")],
        ),
        "투명": dict(
            hanja="透明", meaning="transparency",
            characters=[("透", "투", "to penetrate — as in 투과"),
                        ("明", "명", "bright, clear — as in 설명, 분명")],
        ),
        "방역조치": dict(
            hanja="防疫措置", meaning="disease-control measures",
            characters=[("防", "방", "to defend — as in 예방, 방지"),
                        ("疫", "역", "epidemic — as in 검역, 면역"),
                        ("措", "조", "to arrange, to take (a step)"),
                        ("置", "치", "to place — as in 설치, 위치")],
        ),
        "공유": dict(
            hanja="共有", meaning="sharing",
            characters=[("共", "공", "together — as in 공동, 공공"),
                        ("有", "유", "to have — as in 유권자, 소유")],
        ),
        "아세안": dict(
            meaning="ASEAN",
            notes=["동남아시아국가연합 — the ten states of Southeast Asia. Korea "
                   "opened dialogue relations with them in 1988."],
        ),
        "참석": dict(hanja="參席", meaning="attendance, taking part"),
        "기념촬영": dict(
            hanja="紀念撮影", meaning="a commemorative photograph",
            characters=[("紀", "기", "record, era — as in 세기"),
                        ("念", "념", "thought — as in 개념, 이념")],
        ),
        "공동 의장": dict(hanja="共同議長", meaning="a co-chair"),
        "성명": dict(
            hanja="聲明", meaning="a statement, a declaration",
            characters=[("聲", "성", "voice, sound — as in 음성"),
                        ("明", "명", "to make clear — as in 투명, 설명")],
        ),
        "대화 관계": dict(hanja="對話關係", meaning="dialogue relations"),
        "수립": dict(
            hanja="樹立", meaning="establishment (of relations, a plan)",
            characters=[("樹", "수", "tree, to plant"),
                        ("立", "립", "to set up — as in 입장, 설립")],
        ),
        "성과": dict(
            hanja="成果", meaning="an achievement, results",
            characters=[("成", "성", "to accomplish — as in 성장, 구성"),
                        ("果", "과", "fruit, result — as in 결과, 효과")],
        ),
        "안보": dict(
            hanja="安保", meaning="security",
            notes=["Short for 안전 보장. 국가 안보 is national security."],
        ),
        "교역": dict(
            hanja="交易", meaning="trade",
            characters=[("交", "교", "to exchange — as in 외교, 교통"),
                        ("易", "역", "to trade, easy — as in 무역")],
        ),
        "첨단 산업": dict(
            hanja="尖端産業", meaning="high-technology industry",
            characters=[("尖", "첨", "pointed, sharp"),
                        ("端", "단", "end, tip — as in 단서")],
            notes=["첨단 is literally the sharp tip — the leading edge."],
        ),
        "인적 교류": dict(
            hanja="人的交流", meaning="people-to-people exchange",
        ),
        "확대": dict(hanja="擴大", meaning="expansion"),
        "국가고문": dict(
            hanja="國家顧問", meaning="State Counsellor",
            notes=["Myanmar's office held by Aung San Suu Kyi at the time; "
                   "abolished after the 2021 coup."],
        ),
        "외교장관": dict(hanja="外交長官", meaning="a foreign minister"),
        "개최": dict(
            hanja="開催", meaning="holding (an event)",
            characters=[("開", "개", "to open — as in 공개, 개방"),
                        ("催", "최", "to urge, to hold")],
        ),
        "국가주석": dict(
            hanja="國家主席", meaning="the President of China",
            characters=[("主", "주", "main — as in 주권, 주인"),
                        ("席", "석", "seat — as in 출석, 좌석")],
        ),
        "회원국": dict(hanja="會員國", meaning="a member state"),
        "역동성": dict(
            hanja="力動性", meaning="dynamism",
            characters=[("力", "력", "force — as in 능력, 권력"),
                        ("動", "동", "to move — as in 운동, 활동")],
        ),
        "창조": dict(
            hanja="創造", meaning="creation",
            characters=[("創", "창", "to originate — as in 창의, 창업"),
                        ("造", "조", "to make — as in 제조, 구조")],
        ),
        "주제": dict(hanja="主題", meaning="a theme, a subject"),
        "지속가능": dict(
            hanja="持續可能", meaning="sustainable",
            characters=[("持", "지", "to hold — as in 유지, 지지"),
                        ("續", "속", "to continue — as in 계속, 상속")],
        ),
        "혁신적": dict(
            hanja="革新的", meaning="innovative",
            characters=[("革", "혁", "leather, to reform — as in 개혁"),
                        ("新", "신", "new — as in 신문, 최신")],
        ),
        "포용적": dict(hanja="包容的", meaning="inclusive"),
        "성장": dict(hanja="成長", meaning="growth"),
        "증진": dict(
            hanja="增進", meaning="promotion, furthering",
            characters=[("增", "증", "to increase — as in 증가"),
                        ("進", "진", "to advance — as in 진행, 진출")],
        ),
        "역내": dict(
            hanja="域內", meaning="within the region",
            characters=[("域", "역", "region — as in 지역, 광역")],
        ),
        "경제통합": dict(hanja="經濟統合", meaning="economic integration"),
        "집중적": dict(
            hanja="集中的", meaning="intensive, concentrated",
            characters=[("集", "집", "to gather — as in 집회 “a rally”"),
                        ("中", "중", "middle — as in 중심, 집중")],
        ),
    },

    extraNotes=[
        "The crossword grid is not reproduced; its clues are, with the "
        "answers covered. Those answers, and the answers to the 종합 평가, are "
        "mine — worked out from the chapters. The book keeps its own in "
        "정답보기 on p. 262, which is not photographed.",
        "The 〈보기〉 boxes of questions 04 to 06 are set as quoted lines, "
        "which is how the book boxes them. Question 04's stem names ㉠ and ㉡ "
        "while its box is labelled ㄱ and ㄴ; that is the book's own slip and "
        "stands as printed.",
        "The three summit notes on p. 133 are left untranslated, as the "
        "알아두면 좋아요 boxes are.",
    ],
)
