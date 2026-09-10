# -*- coding: utf-8 -*-
"""Chapter 30 — Foreigners and the law.

Transcribed from the photos of pp. 162-165. Your English glosses on p. 163
and p. 164 are carried as the entries for the words they sit over.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, TABLE,
               CELL, GLOSSARY)

CHAPTER = dict(
    number=30, slug="30-foreigners-and-law",
    unit="법", title="외국인과 법", titleEn="Foreigners and the law",

    append=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 한국에서 쓰레기 및 재활용품을 분리하여 배출한 모습입니다.",
                  "Below is what separating rubbish and recyclables for "
                  "collection looks like in Korea."),
        FIGURE("길가에 놓인 분리배출 자루 넷 — 일반쓰레기, 플라스틱/비닐류, 유리병류, 캔/고철류"),
        HEADING(4, "01 사진을 통해 한국에서 쓰레기와 재활용품을 어떻게 분리배출하는지 말해봅시다.",
                translation="From the photograph, say how rubbish and "
                            "recyclables are separated for collection in "
                            "Korea."),
        HEADING(4, "02 세계 많은 나라 중에서 유독 한국은 쓰레기와 재활용품 분리배출이 잘 이뤄지고 "
                   "있습니다. 그 이유는 무엇일까요?",
                translation="Of all the countries in the world, Korea "
                            "separates its rubbish and recyclables "
                            "particularly well. Why might that be?"),

        SECTION("goals", "학습목표"),
        BULLET("한국 사회에서 법이 얼마나 중요한 것인지 설명할 수 있다.", ordered=True,
               translation="Explain how important the law is in Korean "
                           "society."),
        BULLET("법에 정해진 외국인의 {권리}와 {의무}를 설명할 수 있다.", ordered=True,
               translation="Explain the rights and duties the law sets out "
                           "for foreigners."),

        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"],
              [[CELL("기본", down=2), "법", "31. 한국 체류와 법", "외국인에게 적용되는 법률"],
               ["법", "32. 한국 국적과 법", "국적의 의미와 한국 국민의 기준"]]),

        SECTION("part", "01 한국에서 법은 어떤 의미를 가지고 있을까?"),
        GLOSSARY(("규범", "인간이 마땅히 따르고 지켜야 할 공동의 기준", "규범",
                  "norm, law, standard"),
                 ("정치인", "정치에 활발히 참여하거나 매우 밀접한 관련을 갖는 직업을 가진 사람. "
                            "주로 국회의원을 가리키는 경우가 많다.", "정치인", "politician"),
                 ("준법 정신", "법률이나 규칙 등을 잘 지키는 정신", "준법 정신",
                  "law-abiding spirit, respect for law")),
        HEADING(2, "법의 목적과 역할", translation=
                "What the law is for, and what it does" "\n\n"
                "The law is a norm made through the wisdom and the agreement "
                "of the members of a society. Its purpose is to realise "
                "justice. Justice means judging right and wrong and giving "
                "each person the proper share they are due. It gives the "
                "reward that is due to someone who has worked hard, and "
                "gives a punishment to fit to someone who has done wrong or "
                "harmed another. Through this each person’s freedom and "
                "rights are protected and social order too can be kept "
                "stable." "\n\n"
                "Because the law does such an important job, Korean society "
                "today works constantly at making better law. Where a law "
                "does not fit the times or contains something wrong, "
                "politicians — members of the National Assembly among them — "
                "and citizens raise the matter and put it right."),
        PARAGRAPH("법은 사회 {구성원}의 {지혜}와 {합의}를 통해 만들어진 {규범}이다. 법의 목적은 "
                  "{정의}를 {실현하는|실현하다} 것이다. 정의란 {옳고|옳다} {그름}을 {판단하여|판단하다} "
                  "각자가 받아야 할 {정당한|정당하다} 몫을 주는 것을 말한다. 열심히 노력한 사람에게는 "
                  "그에 따른 {보상}을 주고, 잘못을 {저지르거나|저지르다} 다른 사람에게 피해를 준 "
                  "사람에게는 그에 맞는 벌을 주는 것이다. 이를 통해서 각 개인의 자유와 {권리}를 "
                  "보호하고 사회 {질서}도 안정적으로 유지할 수 있다."),
        PARAGRAPH("이처럼 법이 중요한 역할을 하고 있기 때문에 오늘날 한국 사회에서는 더 좋은 법을 만들기 "
                  "위해 {끊임없이} 노력하고 있다. 법이 시대에 맞지 않거나 잘못된 내용을 포함하고 있을 "
                  "때는 {국회의원}을 비롯한 {정치인}과 시민들이 그에 대해 문제를 {제기하고|제기하다} "
                  "{고쳐|고치다} 나가고 있다."),
        FIGURE("한국의 대법원 앞 정의의 여신상"),

        HEADING(2, "준법의 중요성", translation=
                "Why keeping the law matters" "\n\n"
                "To protect people’s rights and keep order in society "
                "through the law, a law-abiding spirit is needed alongside "
                "the effort of making good law. However good a law may be, "
                "it is of no use if people do not keep it. In Korea, "
                "keeping the law and not harming others or society is held "
                "to matter. Foreigners living in Korea, as well as Korean "
                "citizens, can understand and keep the law and so protect "
                "their own rights and those of others, and live more "
                "safely."),
        PARAGRAPH("법을 통해 사람들의 {권리}를 보호하고 사회 질서를 유지하기 위해서는 좋은 법을 만드는 "
                  "노력과 함께 {준법 정신}이 필요하다. 아무리 좋은 법이 있어도 사람들이 그것을 지키지 "
                  "않는다면 소용이 없다. 한국에서는 법을 지키고 다른 사람이나 사회에 피해를 주지 않는 "
                  "것을 중요하게 생각한다. 대한민국 국민뿐만 아니라 한국에서 생활하는 외국인 또한 법을 "
                  "잘 이해하고 지킴으로써 자신과 타인의 권리를 보호하며 더욱 안전하게 생활할 수 있다."),
        TABLE(["연도", "체류외국인 수(명)", "외국인 피의자 수(명)"],
              [["2014", "1,797,618", "28,456"],
               ["2015", "1,899,519", "35,443"],
               ["2016", "2,049,441", "41,044"],
               ["2017", "2,180,498", "33,905"],
               ["2018", "2,367,607", "32,313"]]),
        SOURCE("▶ 경찰청 범죄 통계"),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "순천의 외국인 유학생 자율방범대", translation=
                "Suncheon’s international student neighbourhood watch" "\n\n"
                "In June 2019 an international student neighbourhood watch "
                "began work in Suncheon to help prevent crime involving "
                "foreigners. Its members go out on group patrol at least "
                "once a month, mainly in the areas where foreigners live "
                "closely together and around the university, and work for "
                "the safety of the area. All over Korea, in the same way, "
                "foreigners are forming watches of their own accord and "
                "working with the local police on crime prevention. Their "
                "work is improving safety in these areas and winning the "
                "support of many residents, and it helps to resolve the "
                "difficulties foreigners face as well."),
        PARAGRAPH("2019년 6월 순천에서는 외국인 {범죄} {예방}을 위한 외국인 유학생 {자율 방범대} "
                  "활동이 시작되었다. 이들은 외국인이 {밀집}되어 있는 지역과 대학교 주변을 중심으로 한 "
                  "달에 한 번 이상 {집중} {순찰}에 나서며 지역 안전을 위해 노력하고 있다. 이처럼 "
                  "대한민국 지역 곳곳에서 외국인들이 {자율적}으로 방범대를 꾸리고 지역 경찰과 "
                  "{협력하여|협력하다} 범죄 예방 활동에 나서고 있다. 이들의 활동은 지역의 {치안}을 "
                  "{개선하여|개선하다} 많은 주민들의 {호응}을 얻고 있으며, 외국인들의 어려움을 해결하는 "
                  "데도 도움을 주고 있다."),
        FIGURE("순천경찰서, 외국인 유학생 자율방범대 발대식"),

        SECTION("part", "02 외국인에게는 어떤 법적 권리와 의무가 있을까?"),
        GLOSSARY(("인권", "사람으로서 당연히 누려야 할 인간답게 살 권리", "인권", "human rights"),
                 ("국제법", "국가들 간의 관계를 정해놓은 법", "국제법", "international law"),
                 ("출입국관리법",
                  "한국에 입국하거나 한국에서 출국하는 사람들의 출입국 관리 및 한국에 체류하는 외국인 "
                  "등록 등을 정해 놓은 법", "출입국관리법"),
                 ("강제퇴거",
                  "한국에 체류하는 외국인이 질서를 어지럽히거나 안전을 위협할 경우 강제로 본국이나 "
                  "제3국으로 추방하는 것", "강제퇴거")),
        HEADING(2, "외국인의 권리", translation=
                "The rights of foreigners" "\n\n"
                "Korea guarantees human rights — the basic rights everyone "
                "is to enjoy as a human being — to anyone, whatever their "
                "nationality. It also guarantees foreigners’ basic standing "
                "and rights in accordance with international law. So in "
                "Korea a foreigner can pursue a happy life without their "
                "life or property being threatened, and must not be "
                "discriminated against on unjust grounds in wages or "
                "working conditions." "\n\n"
                "Korea guarantees certain rights in political participation "
                "and social life as well. A foreigner who has held "
                "permanent residence for three years, for instance, may "
                "take part in the elections that choose local "
                "representatives where certain conditions are met. "
                "Foreigners’ children also have the right to primary and "
                "secondary education, and a foreigner staying six months or "
                "more can receive medical services through health "
                "insurance. Korea also supports the treatment costs of "
                "foreign patients with infectious diseases under the "
                "Infectious Disease Control and Prevention Act, protecting "
                "the health of foreign visitors and preventing the spread "
                "of infection."),
        PARAGRAPH("한국은 국적과 상관없이 누구에게나 인간으로서 누려야 할 기본적인 권리인 {인권}을 "
                  "{보장한다|보장하다}. 또한 {국제법}에 따라 외국인의 기본적인 {지위}와 권리를 보장하고 "
                  "있다. 따라서 한국에서 외국인은 생명이나 재산 등을 {위협받지|위협받다} 않고 행복한 "
                  "삶을 {추구할|추구하다} 수 있으며, 임금이나 {노동조건} 등에서도 {부당한|부당하다} "
                  "이유로 {차별받아서는|차별받다} 안 된다."),
        PARAGRAPH("한국은 외국인의 정치 참여나 사회생활 등에서도 일정한 권리를 보장하고 있다. 예를 들어, "
                  "{영주권}을 얻고 나서 3년이 지난 외국인 중 일정 {조건}을 갖춘 경우에는 지역 주민의 "
                  "대표를 뽑는 선거에 참여할 수 있다. 또한, 외국인의 자녀도 초·중등교육을 받을 권리가 "
                  "있으며, 6개월 이상 체류하는 외국인은 건강보험을 통한 의료 서비스를 받을 수 있다. 또한 "
                  "한국에서는 {감염병} 예방법에 따라 외국인 감염병 환자의 치료 비용 등을 지원하여 국내 "
                  "방문 외국인의 건강을 보호하고 감염병 {확산}을 {방지하고|방지하다} 있다."),
        FIGURE("국내 외국인의 지방선거 참여 모습 — 해외문화홍보원(kocis.go.kr) (사진 출처: 〈연합뉴스〉)"),

        HEADING(2, "외국인의 의무", translation=
                "The duties of foreigners" "\n\n"
                "In Korea the law lays down not only foreigners’ rights but "
                "their duties. Basically a foreigner too must keep Korea’s "
                "laws and public order and pay the taxes the law sets. In "
                "particular, under the Immigration Act a foreigner who "
                "might harm the interests of the Republic of Korea, public "
                "safety or social order may be refused entry or deported. "
                "In 2020, for instance, Korea imposed fines on foreigners "
                "who did not follow the advice to self-isolate despite "
                "symptoms suggesting COVID-19, and had them leave the "
                "country."),
        PARAGRAPH("한국에서는 법을 통해 외국인의 권리뿐만 아니라 {의무}도 {규정하고|규정하다} 있다. "
                  "기본적으로 외국인도 한국의 법과 {공공질서}를 잘 지키고 법이 정하는 세금을 내야 한다. "
                  "특히 {출입국관리법}에 따라 대한민국의 이익, {공공안전}, 사회질서 등을 "
                  "{해칠|해치다} {우려}가 있는 외국인은 입국이 {금지되거나|금지되다} "
                  "{강제퇴거}될 수도 있다. 예를 들어, 2020년 한국에서는 코로나19 의심 증상으로 "
                  "{자가 격리} 권고를 받고도 이를 따르지 않은 외국인에 대해 {범칙금}을 "
                  "{부과하고|부과하다} 출국하도록 하였다."),
        TABLE(["연도", "외국인 세금 납부액(억 원)"],
              [["2015년", "11,909"],
               ["2016년", "12,399"],
               ["2017년", "13,178"]]),
        SOURCE("▲ 외국인의 근로소득세/종합소득세 금액 — 세금 납부는 기본적인 의무이며 외국인도 한국의 법에 "
               "따라 세금을 내고 있다."),

        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "외국인 자녀의 교육받을 권리를 보장하고 있어요", translation=
                "The right of a foreigner’s child to an education is "
                "guaranteed" "\n\n"
                "Under the UN Convention on the Rights of the Child, Korea "
                "guarantees a child’s right to education whatever their "
                "residence status or nationality, including the children of "
                "unregistered foreigners. Where there are no official "
                "papers, enrolment in primary, middle or high school can be "
                "applied for with nothing more than a document confirming "
                "residence, such as a tenancy agreement. Where a child "
                "cannot prove the education they have had, enrolment is "
                "possible after asking the office of education and going "
                "through an assessment of prior learning. Where a child "
                "does not know Korean, Korean lessons are also supported, "
                "through preparatory schools and the like."),
        PARAGRAPH("한국은 {유엔아동권리협약}에 따라 {미등록외국인}의 자녀를 포함하여 체류 자격이나 국적과 "
                  "관계없이 아동의 교육받을 권리를 보장하고 있다. 공식적인 서류가 없는 경우 "
                  "{임대차계약서} 등 거주 사실을 확인할 수 있는 서류만으로도 초중고 입학을 신청할 수 "
                  "있다. 아동이 기존 {학력}을 {증명하기|증명하다} 어려운 경우에는 교육청에 문의하여 학력 "
                  "{심의}를 거친 후에 입학이 가능하다. 아동이 한국어를 모르는 경우 {예비학교} 등을 통해 "
                  "한국어 교육을 지원하기도 한다."),
        FIGURE("‘대한민국의 학교는 모두에게 열려 있습니다!’ 안내 포스터"),

        SECTION("review", "주요 내용정리"),
        HEADING(3, "01 한국에서 법은 어떤 의미를 가지고 있을까?"),
        BULLET("법은 사회 구성원의 지혜와 합의를 통해 만들어진 규범으로 (        )를 실현하는 것을 "
               "목적으로 한다."),
        BULLET("법을 통해 각 사람의 자유와 (        )를 보호할 수 있고 사회 (        )도 "
               "안정적으로 유지할 수 있다."),
        BULLET("법이 본래의 목적과 역할을 잘 수행하도록 하기 위해서는 좋은 법을 만드는 노력과 함께 "
               "(        ) 정신이 필요하다."),
        HEADING(3, "02 외국인에게는 어떤 법적 권리와 의무가 있을까?"),
        BULLET("한국에서 외국인은 인간으로서 누려야 할 기본적 권리인 (        )을 보장받으며, "
               "(        )에 따라 외국인의 기본적 지위와 권리를 보장받는다."),
        BULLET("한국에서 (        )을 얻고 나서 3년이 지난 외국인 중 일정 조건을 갖춘 경우에는 "
               "지역 주민의 대표를 뽑는 선거에 참여할 수 있다."),
        BULLET("한국에 입국하거나 한국에서 출국하는 외국인이 주의해야 할 사항이나 외국인 등록에 관한 "
               "내용 등을 정해 놓은 (            )은 한국에 체류하는 외국인이라면 특히 잘 "
               "알아두어야 하는 법이다."),

        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "한국에 거주하는 외국인도 국민연금에 가입해야 합니다", translation=
                "Foreigners living in Korea must join the national pension "
                "too" "\n\n"
                "A foreigner living in Korea must join the national "
                "pension. A foreigner aged between 18 and 60 who works as "
                "an employee at a workplace joins as a workplace "
                "subscriber, and one who is self-employed as a regional "
                "subscriber, and can enjoy the benefits. It can be called a "
                "policy that gives foreigners the same rights and duties as "
                "Korean workers. It does not apply, however, where the "
                "foreigner’s own country does not guarantee pension "
                "membership to Korean citizens, or where there is a "
                "separate agreement on pensions between Korea and that "
                "country."),
        PARAGRAPH("한국에 거주하고 있는 외국인도 {국민연금}에 가입해야 한다. 18세 이상 60세 미만의 "
                  "외국인의 경우 {사업장}에서 근로자로 일하면 사업장 {가입자}로서, {자영업자}인 경우에는 "
                  "{지역가입자}로서 국민연금에 가입하여 혜택도 누릴 수 있다. 이는 외국인들에게도 한국인 "
                  "근로자와 {동등한|동등하다} 권리와 의무를 누리게 하는 정책이라고 할 수 있다. 다만, "
                  "외국인의 {본국}에서 대한민국 국민에게 연금 가입을 보장하지 않을 경우 또는 한국과 "
                  "외국인의 본국 사이에 연금과 관련한 별도의 {협정}이 있는 경우에는 해당되지 않는다."),
        FIGURE("‘외국인 근로자도 국민연금 가입이 의무입니다!’ 안내 그림"),
        PARAGRAPH("★ 한국에서 외국인에게 제공하는 권리에는 어떤 것이 있는지, 어떤 권리를 더 제공해야 "
                  "한다고 생각하는지 이야기해 봅시다.",
                  "Talk about what rights Korea provides to foreigners, and "
                  "what rights you think it should provide as well."),
    ],

    extraAnnotations={
        "구성원": dict(
            hanja="構成員", meaning="a member (of a body), one who makes it up",
            characters=[("構", "구", "to build — as in 구조 “structure”, 구성"),
                        ("成", "성", "to form, achieve — as in 성장, 완성"),
                        ("員", "원", "a member — as in 회원, 직원")],
        ),
        "지혜": dict(
            hanja="智慧", meaning="wisdom",
            characters=[("智", "지", "wisdom, wit — as in 지능 “intelligence”"),
                        ("慧", "혜", "bright, wise")],
        ),
        "합의": dict(
            hanja="合意", meaning="agreement, consent, a meeting of minds",
            characters=[("合", "합", "to join, agree — as in 합격, 결합"),
                        ("意", "의", "intention, meaning — as in 의견, 의미")],
        ),
        "규범": dict(
            hanja="規範", meaning="a norm, a standard people are to keep to",
            characters=[("規", "규", "rule — as in 규칙, 규제"),
                        ("範", "범", "a model, an example — as in 모범 “model”")],
            notes=["The page glosses it as 인간이 마땅히 따르고 지켜야 할 공동의 기준 — "
                   "a shared standard people ought to follow."],
        ),
        "정의": dict(
            hanja="正義", meaning="justice",
            characters=[("正", "정", "right, correct — as in 정당, 정확"),
                        ("義", "의", "righteousness — as in 의무 “duty”, 정의")],
        ),
        "실현하다": dict(
            hanja="實現하다", meaning="to realise, to bring about",
            characters=[("實", "실", "actual, real — as in 실제, 사실"),
                        ("現", "현", "to appear — as in 현재, 표현")],
            surfaces=["실현하는"],
        ),
        "옳다": dict(meaning="to be right, to be correct", surfaces=["옳고"]),
        "그름": dict(meaning="being wrong; 옳고 그름 = right and wrong"),
        "판단하다": dict(
            hanja="判斷하다", meaning="to judge, to decide",
            characters=[("判", "판", "to judge — as in 판결, 재판"),
                        ("斷", "단", "to cut off, decide — as in 단절, 결단")],
            surfaces=["판단하여"],
        ),
        "정당하다": dict(
            hanja="正當하다", meaning="to be right, proper, justified",
            characters=[("正", "정", "right — the same 正 as in 정의"),
                        ("當", "당", "fitting, due — as in 당연 “natural”")],
            surfaces=["정당한"],
        ),
        "보상": dict(
            hanja="補償", meaning="a reward; compensation",
            characters=[("補", "보", "to make up for — as in 보충, 보완"),
                        ("償", "상", "to compensate — as in 배상")],
            notes=["Chapter 7 has the 보상 of 산업재해보상보험, where it is "
                   "compensation for harm; here it is the reward that is due."],
        ),
        "저지르다": dict(
            meaning="to commit (a wrong), to do (something bad)",
            surfaces=["저지르거나"],
        ),
        "질서": dict(
            hanja="秩序", meaning="order",
            characters=[("秩", "질", "order, rank"),
                        ("序", "서", "sequence — as in 순서 “order, sequence”")],
            notes=["사회 질서 = social order; 공공질서 = public order."],
        ),
        "끊임없이": dict(
            meaning="constantly, without a break",
            notes=["From 끊이다 “to be cut off” — literally without ceasing."],
        ),
        "국회의원": dict(
            hanja="國會議員", meaning="a member of the National Assembly",
            characters=[("國會", None, "the National Assembly — chapter 21"),
                        ("議員", None, "an elected member (議 to deliberate, "
                                       "員 member)")],
        ),
        "제기하다": dict(
            hanja="提起하다", meaning="to raise (an issue), to bring up",
            characters=[("提", "제", "to present, put forward — as in 제출, 제안"),
                        ("起", "기", "to rise — as in 기상, 起")],
            surfaces=["제기하고"],
        ),
        "고치다": dict(meaning="to fix, to mend, to amend", surfaces=["고쳐"]),
        "준법 정신": dict(
            hanja="遵法精神", meaning="a law-abiding spirit, respect for the law",
            characters=[("遵", "준", "to obey, comply — as in 준수 “compliance”"),
                        ("法", "법", "law"),
                        ("精神", None, "spirit, mind")],
        ),
        "정치인": dict(
            hanja="政治人", meaning="a politician",
            characters=[("政治", None, "politics — chapter 20’s subject"),
                        ("人", "인", "person")],
        ),
        "권리": dict(
            hanja="權利", meaning="a right, a claim one may make",
            characters=[("權", "권", "power, right — as in 권력, 인권"),
                        ("利", "리", "benefit — as in 이익, 이해관계")],
            notes=["권리 is a right one may claim; 권력 is power over others."],
        ),
        "의무": dict(
            hanja="義務", meaning="a duty, an obligation",
            characters=[("義", "의", "righteousness — the same 義 as in 정의"),
                        ("務", "무", "task, duty — as in 업무, 공무원")],
        ),
        "범죄": dict(
            hanja="犯罪", meaning="a crime",
            characters=[("犯", "범", "to violate — as in 위반, 범인"),
                        ("罪", "죄", "guilt, sin — as in 유죄, 무죄")],
        ),
        "예방": dict(
            hanja="豫防", meaning="prevention",
            characters=[("豫", "예", "in advance — as in 예약, 예상"),
                        ("防", "방", "to guard against — as in 방지, 국방")],
        ),
        "자율 방범대": dict(
            hanja="自律防犯隊", meaning="a voluntary neighbourhood watch",
            characters=[("自律", None, "of one’s own accord, self-governing"),
                        ("防犯", None, "crime prevention"),
                        ("隊", "대", "a squad, a team — as in 부대, 대원")],
        ),
        "밀집": dict(
            hanja="密集", meaning="being densely gathered",
            characters=[("密", "밀", "dense, close — as in 밀접, 비밀"),
                        ("集", "집", "to gather — as in 집중, 모집")],
        ),
        "집중": dict(
            hanja="集中", meaning="concentration; here, concentrated (patrol)",
            characters=[("集", "집", "to gather — as in 밀집, 수집"),
                        ("中", "중", "middle, centre")],
        ),
        "순찰": dict(
            hanja="巡察", meaning="a patrol",
            characters=[("巡", "순", "to go round — as in 순회"),
                        ("察", "찰", "to observe — as in 경찰 “police”, 관찰")],
        ),
        "자율적": dict(
            hanja="自律的", meaning="of one’s own accord, voluntary",
        ),
        "협력하다": dict(
            hanja="協力하다", meaning="to co-operate",
            characters=[("協", "협", "to join in — as in 협약, 협정"),
                        ("力", "력", "strength — as in 노력, 능력")],
            surfaces=["협력하여"],
        ),
        "치안": dict(
            hanja="治安", meaning="public safety, law and order",
            characters=[("治", "치", "to govern — as in 정치, 통치"),
                        ("安", "안", "peace, safety — as in 안전, 안정")],
        ),
        "개선하다": dict(
            hanja="改善하다", meaning="to improve",
            characters=[("改", "개", "to change, reform — as in 개정, 개혁"),
                        ("善", "선", "good — as in 최선 “one’s best”")],
            surfaces=["개선하여"],
        ),
        "호응": dict(
            hanja="呼應", meaning="a favourable response, support",
            characters=[("呼", "호", "to call — as in 호칭, 호출"),
                        ("應", "응", "to answer — as in 응답, 응시")],
        ),
        "인권": dict(
            hanja="人權", meaning="human rights",
            characters=[("人", "인", "person"),
                        ("權", "권", "right — the same 權 as in 권리")],
        ),
        "국제법": dict(
            hanja="國際法", meaning="international law",
            characters=[("國際", None, "international — as in 국제화, 국제적"),
                        ("法", "법", "law")],
        ),
        "보장하다": dict(
            hanja="保障하다", meaning="to guarantee, to secure",
            characters=[("保", "보", "to protect — as in 보호, 보험"),
                        ("障", "장", "a barrier, to shield — as in 장애")],
            surfaces=["보장한다"],
        ),
        "지위": dict(
            hanja="地位", meaning="standing, status",
            characters=[("地", "지", "ground, place — as in 지역, 지방"),
                        ("位", "위", "position — as in 순위, 학위")],
        ),
        "위협받다": dict(
            hanja="威脅받다", meaning="to be threatened",
            characters=[("威", "위", "authority, might — as in 위력"),
                        ("脅", "협", "to threaten")],
            surfaces=["위협받지"],
        ),
        "추구하다": dict(
            hanja="追求하다", meaning="to pursue",
            characters=[("追", "추", "to chase — as in 추적, 추가"),
                        ("求", "구", "to seek — as in 요구, 구직")],
            surfaces=["추구할"],
        ),
        "노동조건": dict(
            hanja="勞動條件", meaning="working conditions",
            characters=[("勞動", None, "labour — as in 노동자, 노동부"),
                        ("條件", None, "conditions, terms")],
        ),
        "부당하다": dict(
            hanja="不當하다", meaning="to be unjust, unreasonable",
            characters=[("不", "부", "not — as in 부적합, 불법"),
                        ("當", "당", "fitting, due — the same 當 as in 정당하다")],
            surfaces=["부당한"],
        ),
        "차별받다": dict(
            hanja="差別받다", meaning="to be discriminated against",
            characters=[("差", "차", "difference — as in 차이, 격차"),
                        ("別", "별", "to separate, distinguish — as in 구별, 특별")],
            surfaces=["차별받아서는"],
        ),
        "영주권": dict(
            hanja="永住權", meaning="permanent residence (the right to stay)",
            characters=[("永", "영", "eternal, permanent — as in 영원"),
                        ("住", "주", "to dwell — as in 주거, 거주"),
                        ("權", "권", "right")],
        ),
        "조건": dict(
            hanja="條件", meaning="a condition, a requirement",
            characters=[("條", "조", "an article, a clause — as in 조항, 조약"),
                        ("件", "건", "a case, an item — as in 사건, 물건")],
        ),
        "감염병": dict(
            hanja="感染病", meaning="an infectious disease",
            characters=[("感染", None, "infection — 感 to feel, 染 to be dyed"),
                        ("病", "병", "illness — as in 질병, 병원")],
        ),
        "확산": dict(
            hanja="擴散", meaning="spread, diffusion",
            characters=[("擴", "확", "to expand — as in 확대, 확장"),
                        ("散", "산", "to scatter — as in 분산, 산책")],
        ),
        "방지하다": dict(
            hanja="防止하다", meaning="to prevent, to keep from happening",
            characters=[("防", "방", "to guard against — the same 防 as in 예방"),
                        ("止", "지", "to stop — as in 정지, 금지")],
            surfaces=["방지하고"],
        ),
        "규정하다": dict(
            hanja="規定하다", meaning="to lay down, to stipulate",
            characters=[("規", "규", "rule — the same 規 as in 규범"),
                        ("定", "정", "to fix — as in 지정, 제정")],
            surfaces=["규정하고"],
        ),
        "공공질서": dict(
            hanja="公共秩序", meaning="public order",
            characters=[("公共", None, "public — as in 공공기관, 공공장소"),
                        ("秩序", None, "order — the 질서 of this chapter")],
        ),
        "출입국관리법": dict(
            hanja="出入國管理法", meaning="the Immigration Act",
            characters=[("出入國", None, "leaving and entering a country"),
                        ("管理", None, "management, control"),
                        ("法", "법", "law")],
            notes=["Chapter 31’s subject: what it says about staying in "
                   "Korea."],
        ),
        "공공안전": dict(hanja="公共安全", meaning="public safety"),
        "해치다": dict(
            meaning="to harm, to damage",
            notes=["Chapter 8’s word — 안전을 해치다 “to endanger safety”."],
            surfaces=["해칠"],
        ),
        "우려": dict(
            hanja="憂慮", meaning="concern, apprehension",
            characters=[("憂", "우", "to worry, grieve"),
                        ("慮", "려", "to consider, be anxious — as in 고려")],
        ),
        "금지되다": dict(
            hanja="禁止되다", meaning="to be prohibited",
            characters=[("禁", "금", "to forbid — as in 금연, 금지"),
                        ("止", "지", "to stop — the same 止 as in 방지")],
            surfaces=["금지되거나"],
        ),
        "강제퇴거": dict(
            hanja="強制退去", meaning="deportation, forced removal",
            characters=[("強制", None, "by force, compulsory — as in 강제적"),
                        ("退去", None, "to withdraw, leave — 退 to retreat, "
                                       "去 to go")],
        ),
        "자가 격리": dict(
            hanja="自家隔離", meaning="self-isolation",
            characters=[("自家", None, "one’s own home"),
                        ("隔離", None, "isolation — 隔 to separate, 離 to part")],
        ),
        "범칙금": dict(
            hanja="犯則金", meaning="a fine (for a minor offence)",
            characters=[("犯", "범", "to violate — the same 犯 as in 범죄"),
                        ("則", "칙", "rule — as in 원칙, 규칙"),
                        ("金", "금", "money")],
        ),
        "부과하다": dict(
            hanja="賦課하다", meaning="to impose (a tax, a fine)",
            characters=[("賦", "부", "to levy, bestow"),
                        ("課", "과", "to assign, a lesson — as in 과제, 과정")],
            surfaces=["부과하고"],
        ),
        "유엔아동권리협약": dict(
            meaning="the UN Convention on the Rights of the Child",
            notes=["아동 “child”, 권리 “rights”, 협약 “convention, "
                   "agreement”."],
        ),
        "미등록외국인": dict(
            hanja="未登錄外國人", meaning="an unregistered foreigner",
            characters=[("未", "미", "not yet — as in 미혼, 미성년"),
                        ("登錄", None, "registration — as in 외국인 등록")],
        ),
        "임대차계약서": dict(
            hanja="賃貸借契約書", meaning="a tenancy agreement",
            characters=[("賃貸", None, "letting, lease — as in 임대 주택"),
                        ("借", "차", "to borrow, rent"),
                        ("契約書", None, "a written contract — chapter 5’s 계약")],
        ),
        "학력": dict(
            hanja="學歷", meaning="educational background, prior schooling",
            characters=[("學", "학", "learning — as in 학교, 학위"),
                        ("歷", "력", "a record, history — as in 경력, 역사")],
        ),
        "증명하다": dict(
            hanja="證明하다", meaning="to prove, to certify",
            characters=[("證", "증", "evidence — as in 증인, 영수증"),
                        ("明", "명", "clear — as in 명확하다, 설명")],
            surfaces=["증명하기"],
        ),
        "심의": dict(
            hanja="審議", meaning="deliberation, review (by a body)",
            characters=[("審", "심", "to examine — as in 심사, 심판"),
                        ("議", "의", "to deliberate — as in 회의, 국회의원")],
        ),
        "예비학교": dict(
            hanja="豫備學校", meaning="a preparatory school",
            characters=[("豫備", None, "preparation, reserve — 豫 in advance, "
                                       "備 to provide")],
            notes=["For children who arrive without Korean, before they "
                   "join an ordinary class."],
        ),
        "국민연금": dict(
            hanja="國民年金", meaning="the national pension",
            characters=[("國民", None, "the people, citizens"),
                        ("年金", None, "a pension — 年 year, 金 money")],
            notes=["Chapter 7’s 사회보험 lists it among the four."],
        ),
        "사업장": dict(
            hanja="事業場", meaning="a workplace, a business premises",
            characters=[("事業", None, "a business, an undertaking"),
                        ("場", "장", "a place — as in 시장, 공장")],
        ),
        "가입자": dict(
            hanja="加入者", meaning="a subscriber, a member of a scheme",
            characters=[("加入", None, "to join — as in 가입하다"),
                        ("者", "자", "a person — as in 소비자, 근로자")],
        ),
        "자영업자": dict(
            hanja="自營業者", meaning="a self-employed person",
            characters=[("自營", None, "running one’s own"),
                        ("業", "업", "business — as in 취업, 기업"),
                        ("者", "자", "person")],
        ),
        "지역가입자": dict(
            hanja="地域加入者", meaning="a regional subscriber",
            notes=["The category for those not covered through a workplace "
                   "— chapter 8 has the same split for health insurance."],
        ),
        "동등하다": dict(
            hanja="同等하다", meaning="to be equal, on the same footing",
            characters=[("同", "동", "same — as in 동일, 공동"),
                        ("等", "등", "rank, class — as in 평등, 고등")],
            surfaces=["동등한"],
        ),
        "본국": dict(
            hanja="本國", meaning="one’s own country, the home country",
            characters=[("本", "본", "origin, main — as in 기본, 본관"),
                        ("國", "국", "country")],
        ),
        "협정": dict(
            hanja="協定", meaning="an agreement between states",
            characters=[("協", "협", "to join in — the same 協 as in 협력"),
                        ("定", "정", "to fix — as in 규정, 제정")],
        ),
    },

    extraNotes=[
        "The 정의의 여신상 photograph on p. 163 and the 순천 자율방범대 group "
        "photograph are not reproduced; their captions are.",
        "The 경찰청 범죄 통계 table on p. 163 and the 외국인 세금 납부액 table on "
        "p. 164 are set as tables, with the note under each as a source line.",
        "The review gaps on p. 165 are blank in the book and left blank here.",
    ],
)
