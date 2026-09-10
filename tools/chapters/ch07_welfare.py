# -*- coding: utf-8 -*-
"""Chapter 7 — Welfare.

Transcribed in your Google Doc (7.html), whose text is carried in `blocks`
below as the Doc had it. First transcribed from the photos of pp. 40-43; the
two readings were compared line by line when your Doc arrived, and every
difference proved to be a slip in the Doc, listed as fixes below.
"""

from . import (SECTION, HEADING, PARAGRAPH, BULLET, SOURCE, FIGURE, MARGIN,
               TABLE, CELL, GLOSSARY)

CHAPTER = dict(
    number=7, slug="07-welfare",
    unit="사회", title="복지", titleEn="Welfare",

    blocks=[
        SECTION("warmup", "생각해 봅시다"),
        PARAGRAPH("다음은 한국에서 생활하면서 겪을 수 있는 상황을 나타낸 것입니다"),
        FIGURE("일하다가 다친 모습 · 회사에서 해고된 모습 · 장애가 있는 사람의 모습 · 나이가 들어 걷기 어려운 " "모습"),
        HEADING(4, "01 자신의 고향 나라에서는 이런 경우 어떻게 대응합니까?"),
        HEADING(4, "02 본인은 한국에서 이와 같은 상황에 대비하여 무엇을 준비하고 있습니까?"),
        SECTION("goals", "학습목표"),
        BULLET("최소한의 인간다운 삶을 보장하는 한국의 사회 복지 제도를 설명할 수 있다.", ordered=True),
        BULLET("외국인 대상 복지 서비스를 이해하고 이용할 수 있다.", ordered=True),
        SECTION("related", "관련 단원 확인하기"),
        TABLE([CELL("영역", columns=2), "제목", "관련 내용"], [["심화", "국민",
              "4. 대한민국 국민을 위한 복지", "사회보험, 공공부조"]]),
        SECTION("part", "01 한국의 사회 복지 제도에는 어떤 것들이 있을까?"),
        MARGIN("{4대 보험}"),
        HEADING(2, "사회보험", translation="Social Insurance" "\n\n"
          "In Korea, various social welfare systems are established "
          "so that citizens can enjoy at least a minimally human "
          "standard of living. Korea's social welfare system can "
          "broadly be divided into social insurance (사회보험) and public "
          "assistance (공공부조)." "\n\n"
          "Social insurance is a system requiring citizens to enroll, "
          "by law, in preparation for future risks. This includes "
          "health insurance, employment insurance, national pension, "
          "and industrial accident compensation insurance." "\n\n"
          "Health Insurance (건강보험)" "\n\n"
          "When you go to the hospital because you're sick, you can "
          "receive support covering part of your medical costs." "\n\n"
          "Employment Insurance (고용보험)" "\n\n"
          "When you're laid off from a company, you can receive "
          "financial support for a set period." "\n\n" "National Pension (국민연금)"
          "\n\n" "When you get older and it becomes difficult to earn money "
          "anymore, you can receive a set amount each month as living "
          "expenses." "\n\n"
          "Industrial Accident Compensation Insurance (산업재해보상보험)" "\n\n"
          "If you're injured in an accident while working at your "
          "company, you can receive compensation for damages such as "
          "hospital costs."),
        PARAGRAPH("한국에서는 국민이 {최소한}의 {인간다운} 삶을 {누릴} 수 있도록 다양한 사회 복지 제도를 {마련해} "
          "두고 있다. 한국의 사회 복지 제도는 크게 사회보험과 {공공부조}로 나눌 수 있다."),
        PARAGRAPH("사회보험은 미래의 위험에 {대비하여} 법에 따라 국민들이 가입하도록 하고 있는 제도이다. 여기에는 "
          "건강보험, 고용보험, 국민연금, 산업재해보상보험이 있다."),
        TABLE(["건강보험", "아파서 병원에 갈 때 의료비의 {일부}를 지원 받을 수 있다."], [["고용보험",
              "회사에서 {해고되었을|해고} 때 일정 기간 {금전적} 지원을 받을 수 있다"],
              ["국민연금", "나이가 들어 더 이상 돈을 벌기 어려울 때 매달 일정 금액을 생활비로 {지급} 받을 수 있다."],
              ["산업재해보상보험", "회사에서 일하다가 사고로 다쳤을 때 병원비 등 피해에 대해 {보상}을 받을 수 있다."]]),
        BULLET("개인보험"),
        BULLET("생명보험", level=2),
        BULLET("손해보험", level=2),
        BULLET("교육보험", level=2),
        BULLET("사회보험"),
        BULLET("연금보험", level=2),
        BULLET("국민건강보험", level=2),
        BULLET("고용보험", level=2),
        BULLET("산재", level=2),
        MARGIN("국민연금공단", "국민연금 업무를 담당하는 기관", "문의:1355, www.nps.or.kr"),
        HEADING(2, "공공부조"),
        GLOSSARY(("최저 생계비", "생활에 필요한 최소한의 비용"),
              ("저소득층", "소득이 낮아 경제적 지원이 필요한 사람들"),
              ("생계", "살아 나가는 형편"),
              ("긴급", "중요하고 급함")),
        PARAGRAPH("공공부조는 생활이 어려운 사람들의 기본적인 생활 수준을 보장해주기 위해 국가나 지방자치단체에서 생활비, "
          "교육비, 의료비 등을 지원해 주는 제도이다. 소득이 최저 생계비보다 적은 저소득층은 국민 기초생활보장 "
          "제도를 통해 생활비를 지원 받을 수 있다."),
        PARAGRAPH("갑작스럽게 어려운 일을 당해 생계 유지가 곤란한 저소득층 가구를 지원하는 긴급 복지 지원 제도도 있다. "
          "예를 들어 돈을 주로 벌어오는 사람이 크게 다치거나 큰 병을 앓게 되어 일을 할 수 없게 된 경우, 화재 "
          "등으로 인해 살고 있던 집이나 건물에서 생활하기 어려운 경우 등이 발생하면 지방자치단체의 담당 부서나 "
          "보건복지부 콜센터로 전화하여 도움을 받을 수 있다."),
        MARGIN("보건복지부", "상담센터(☎ 129)",
               "본인과 가족에게 필요한 복지 정보와 상담을 원할 때는 129로 전화하면 된다.",
               "특히 보건복지부에서는 각종 의료보장제도에 의해 의료혜택을 받을 수 없는 국내에 거주하는 외국인에게도 "
               "심의를 통해 의료비를 지원하고 있다."),
        FIGURE("복지로 누리집에서 복지 관련 정보를 얻을 수 있다. (http://www.bokjiro.go.kr/)"),
        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "태풍, 지진, 전염병 등의 재난상황에서도 도움을 받을 수 있는 방법이 있을까?", translation=
          "Is there help to be had in a disaster — a typhoon, an "
          "earthquake, an epidemic?" "\n\n"
          "In a disaster such as a typhoon, an earthquake or the spread of "
          "an infectious disease, there is disaster relief money that the "
          "government or a local authority pays for a limited time. The "
          "best-known case in Korea was in 2020, when COVID-19 spread and "
          "disaster relief money was paid to support those affected and to "
          "stimulate the economy. The government’s emergency disaster "
          "payment went to vulnerable households, such as recipients of "
          "basic livelihood support, in cash and without a separate "
          "application; the remaining households applied and were paid in "
          "card points, consumption vouchers or local gift certificates."),
        PARAGRAPH("태풍, 지진, 전염병 확산 등 재난상황에서 정부나 지방자치단체 등이 한시적으로 지급하는 재난관련 지원금이 "
          "있다. 대표적으로 한국에서는 2020년 코로나바이러스 감염증-19가 확산됨에 따라 재난 피해자의 지원과 "
          "경기활성화를 위한 방법으로 재난관련 지원금이 지급되었다. 정부의 긴급재난지원금은 기초생활수급자 등 "
          "취약가정에는 별도 신청과정 없이 현금으로 지급되었으며, 나머지 가구는 신청을 받아 카드 포인트, "
          "소비쿠폰, 지역사랑 상품권 등으로 지급되었다."),
        SECTION("part", "02 다문화 가족 및 외국인을 위한 기관과 지원 서비스에는 어떤 것들이 있을까?"),
        TABLE([CELL("생계급여 대상자선정 기준(월 소득액)", columns=2)], [["1인가구", "527,158"],
              ["2인가구", "897,594"],
              ["3인가구", "1,161,173"],
              ["4인가구", "1,424,752"]]),
        SOURCE("(보건복지부, 2020)"),
        HEADING(2, "외국인 대상 지원 서비스", translation="Support Services for Foreigners"
          "\n\n" "Among Korea's social welfare systems, public assistance "
          "(공공부조) in principle applies only to Korean citizens. "
          "However, among foreigners living in Korea, those who are "
          "married to a Korean citizen, those caring for a parent or "
          "child holding Korean nationality, and those legally "
          "recognized as refugees can, if their income is below the "
          "minimum cost of living (최저 생계비), receive support such as "
          "minimum living expenses, medical costs, and emergency "
          "welfare. Beyond this, programs are also being run offering "
          "free Korean language and Korean culture classes to help "
          "people adapt well to life in Korea and live "
          "independently/on their own terms. In addition, female "
          "marriage immigrants who are pregnant or about to give "
          "birth can receive health management services for "
          "themselves and their newborn baby."),
        GLOSSARY(("신생아", "갓 태어난 아기", "신생아")),
        PARAGRAPH("사회 복지 제도 중 공공부조는 원칙적으로 한국 국민에게만 적용된다. 그러나 한국에 살고 있는 외국인 중 "
          "대한민국 국민과 혼인한 사람, 대한민국 국적을 가진 부모나 자녀를 돌보고 있는 사람, 법에 따라 난민으로 "
          "인정된 사람 등은 소득이 최저 생계비보다 적은 경우 최저 생계비, 의료비, 긴급 복지 등을 지원받을 수 "
          "있다. 이외에도 한국 생활에 잘 적응하고 한국에서 주체적으로 살아갈 수 있도록 무료로 한국어와 한국 "
          "문화를 배울 수 있는 프로그램도 운영되고 있다. 또한 임신을 한 상태이거나 출산을 앞둔 여성 결혼 "
          "이민자는 자신과 신생아의 건강 관리 서비스를 받을 수 있다."),
        HEADING(2, "다문화 가족·외국인 지원 기관", translation=
          "Multicultural Family and Foreigner Support Agencies" "\n\n"
          "Agencies that support multicultural families and "
          "foreigners include: the Ministry of Justice's Foreigner "
          "Comprehensive Information Center, the Ministry of Gender "
          "Equality and Family's Danuri Call Center, Multicultural "
          "Family Support Centers, and the Ministry of Employment and "
          "Labor's Foreign Worker Support Centers." "\n\n"
          "The Foreigner Comprehensive Information Center (1345) "
          "provides multilingual support and consultation for "
          "immigration-related civil affairs matters for foreigners "
          "living in Korea — including ID-related matters, stay "
          "permit matters, and nationality matters. The Danuri Call "
          "Center (1577-1366) provides multicultural families and "
          "migrant women living in Korea with the information they "
          "need for life in Korea, and supports crisis counseling and "
          "emergency assistance, allowing people to speak with "
          "professional counselors in their native language. "
          "Multicultural Family Support Centers provide education to "
          "help multicultural families adapt to Korean society, and "
          "services supporting children's language development. "
          "Foreign Worker Support Centers provide Korean language "
          "education for foreign workers and support the protection "
          "of foreign workers' rights and interests (권익)."),
        GLOSSARY(("다국어", "여러 나라의 언어", "다국어"),
              ("이주", "다른 나라나 지역으로 옮겨 가서 사는 것", "이주"),
              ("권익", "권리와 이익", "권익")),
        PARAGRAPH("다문화 가족과 외국인을 지원하는 기관으로는 {법무부}의 외국인 종합 안내 센터, {여성가족부}의 "
          "{다누리}콜센터, 다문화 가족 지원 센터, {고용노동부}의 외국인 근로자 지원센터 등이 있다."),
        PARAGRAPH("외국인 종합 안내센터(1345)는 {신분증} 관련 업무, {체류}{허가} 관련 업무, 국적 관련 업무 등 "
          "한국에 거주하는 외국인의 출입국 {행정}{민원} 상담과 정보를 다국어로 지원한다. "
          "다누리콜센터(1577-1366)는 국내에 거주하는 다문화 가족·이주 여성에게 필요한 한국 생활 정보를 "
          "제공하고, 위기 상담 및 긴급 지원 등 전문 상담원과 자국 언어로 통화할 수 있도록 지원한다. 다문화 "
          "가족 지원센터는 다문화 가족의 한국 사회 적응을 돕는 교육, 자녀 언어발달 지원 서비스 등을 제공한다. "
          "외국인 근로자 지원센터는 외국인 근로자들을 대상으로 한국어 교육을 실시하고, 외국인 근로자의 권익 보호를 " "지원한다."),
        FIGURE("외국인 종합 안내센터(법무부, 1345) — 1345 + 국가번호 + * 로 20개 언어 상담이 " "가능하다."),
        SECTION("aside", "알아두면 좋아요"),
        HEADING(3, "자신의 고향 나라 언어로 법률 상담을 받을 수 있는 방법은?", translation=
          "How can you get legal advice in your own language?" "\n\n"
          "A, an overseas Korean, was working at a company and caring for "
          "an elderly widowed mother. Some five million won of wages had "
          "been owed for several months, and A, unable to get the money "
          "from the owner and in difficulty, took legal advice through the "
          "free interpreting service between the ‘village lawyer’ and a "
          "foreigner, provided by the foreigner information centre — the "
          "1345 call centre. As a result, all the unpaid wages were "
          "recovered." "\n\n"
          "At the foreigner information centre (1345), a lawyer appointed "
          "by the Ministry of Justice gives legal advice, with interpreting "
          "help from a centre counsellor, to foreigners who find legal "
          "services hard to use because of the language barrier and a lack "
          "of information."),
        PARAGRAPH("재외 동포 A씨는 회사에 다니며 나이가 많은 홀어머니를 모시고 있었다. 수개월 간 약 500만원의 임금이 "
          "밀렸지만 사장으로부터 돈을 받지 못해 A씨는 생활에 어려움을 겪던 중 외국인 종합 안내센터(1345 "
          "콜센터)가 제공하는 ‘마을변호사-외국인’ 간 무료 통역 서비스를 통해 법률 자문을 받았다. 그 결과 "
          "그동안 밀린 임금을 모두 받을 수 있었다."),
        PARAGRAPH("외국인 종합 안내센터(1345)에서는 법무부가 지정한 변호사가 1345센터 상담사의 통역 지원을 받아 "
          "언어 장벽과 정보 부족으로 법률 서비스를 이용하기 어려운 외국인에게 법률 상담을 제공하고 있다."),
        MARGIN("상담시간: 평일 09:00 ~ 22:00 (1345-④마을변호사 법률 상담)"),
        SECTION("review", "주요 내용정리"),
        HEADING(2, "01 한국의 사회 복지 제도에는 어떤 것들이 있을까?"),
        BULLET("미래의 위험에 대비하여 법에 따라 국민들이 가입하도록 하고 있는 사회보험에는 ( 건강 보험 ), ( 고용 "
          "보험 ), (   ), (   )이 있다."),
        BULLET("(   )는 소득이 최저 생계비보다 적은 저소득층의 기본적인 생활 수준을 보장해주기 위해 국가나 "
          "지방자치단체에서 생활비와 교육비, 의료비 등을 지원해주는 제도이다."),
        BULLET("(   ) 지원 제도는 갑작스럽게 어려운 일을 당해 생계 유지가 곤란한 저소득층 가구를 지원하는 " "제도이다."),
        HEADING(2, "02 다문화 가족·외국인 지원 서비스와 기관에는 어떤 것들이 있을까?"),
        BULLET("한국에 체류하고 있는 외국인 중 대한민국 국민과 (   )한 사람, 대한민국 (   )을 가진 부모나 "
          "자녀를 돌보고 있는 사람, 법에 따라 (   )으로 인정된 사람 등은 최저 (   ) 지원, 의료비 "
          "지원, 긴급 복지 지원을 받을 수 있다."),
        BULLET("외국인이 한국에 잘 적응하고 주체적으로 살아갈 수 있도록 무료로 (   )와 한국 ( 언어 ) 교육, "
          "임신 및 출산 지원 서비스, 상담 서비스 등을 제공하고 있다."),
        BULLET("다문화 가족과 외국인을 지원하는 기관으로는 (   ) 종합 안내센터, 다누리 콜센터, 다문화 가족 "
          "지원센터, 외국인 근로자 지원센터 등이 있다."),
        SECTION("discuss", "이야기 나누기"),
        HEADING(3, "네팔 출신 1호 의사의 꿈", translation=
          "The dream of the first doctor from Nepal" "\n\n"
          "Jeong Je-han, the first Korean doctor of Nepalese origin, has "
          "countless brothers to look after besides his own family. They are "
          "the migrant workers staying in the country. He puts a great deal of "
          "effort into helping migrant workers whose Korean is halting and "
          "who cannot properly say what they mean." "\n\n"
          "He has become the foreign member of the Daegu regional 법사랑 "
          "committee, where he speaks for migrants in their place. With "
          "fellow doctors he has also opened a mobile community that helps "
          "Nepalese people and migrant workers having a hard time in Korea."),
        PARAGRAPH("네팔 출신 한국인 1호 의사인 정제한씨는 가족 외에도 챙겨야 할 수많은 형제가 있다. 바로 국내에 체류 "
          "중인 이주노동자들이다. 정제한씨는 한국말이 서툴러 자신의 의견을 제대로 표현하지 못하는 이주 노동자들을 "
          "돕기 위해 여러 노력을 기울이고 있다."),
        PARAGRAPH("정제한씨는 대구 지역 법사랑 위원회의 외국인 위원이 되어 이주민의 목소리를 대신 전해 주기도 한다. 또한, "
          "동료 의사들과 함께 모바일 커뮤니티를 열어 한국에서 어려움을 겪는 네팔인들과 이주 노동자들을 돕고 있다."),
        SOURCE("[출처] 다문화 가족과 함께 만드는 정보 매거진 레인보우 웹진, 2016 가을 호, 여성가족부"),
        PARAGRAPH("★ 본인이 한국에서 지원받은 복지 제도나 서비스, 본인에게 도움을 주었던 사람이나 기관에 대해 이야기해 " "봅시다.",
          "Talk about a welfare scheme or service you have been supported by "
          "in Korea, or a person or an organisation that helped you."),
    ],
    annotations={
        "최소한": dict(
            meaning="at least/minimum",
            notes=["最 (most, same 最 as in 최근 \"recently\")", "小 (small)",
                "限 (limit, same 限 as in 제한 \"restriction\")",
                "literally \"smallest limit\"",
                "최소한의 삶 = \"a minimal standard of living\"."],
        ),
        "인간다운": dict(
            headword="인간답다",
            meaning="to be human-like/befitting a human",
            notes=["인간 (human)",
                "답다 (a suffix meaning \"to be worthy of/befitting\")",
                "인간다운 삶 = \"a life befitting a human/humane life\""],
        ),
        "누릴": dict(
            headword="누리다",
            meaning="to enjoy/partake of",
            notes=["a slightly more formal word than 즐기다",
                "삶을 누리다 = \"to enjoy life\""],
        ),
        "마련해": dict(
            headword="마련하다",
            meaning="to prepare/set up/arrange",
            notes=["제도를 마련하다 = \"to establish/set up a system\""],
        ),
        "공공부조": dict(
            meaning="public assistance",
            notes=["government welfare aid given directly based on need (as "
                "opposed to insurance-based 사회보험)"],
        ),
        "대비하여": dict(
            headword="대비하다",
            meaning="to prepare for/provide against",
            notes=["對 (facing/against, same 對 as in 반대 \"opposition\")",
                "備 (to prepare, same 備 as in 준비 \"preparation\")",
                "미래의 위험에 대비하다 = \"to prepare against future risks\""],
        ),
        "일부": dict(
            meaning="a part/portion",
            notes=["一 (one)", "部 (part, same 部 as in 법무부's ministry suffix)",
                "의료비의 일부 = \"a portion of medical costs\""],
        ),
        "해고": dict(
            meaning="dismissal/layoff",
            notes=["解 (to release/undo, same 解 as in 해례본, 이해)",
                "雇 (to hire, same 雇 as in 고용)", "literally \"release-hiring\""
                , "to be fired/laid off from a job"],
        ),
        "금전적": dict(
            meaning="financial/monetary",
            notes=["金錢 (money, 金 = gold/money + 錢 = coin/money)",
                "적 (adjective suffix)", "금전적 지원 = \"financial support\""],
        ),
        "지급": dict(
            meaning="payment/disbursement",
            notes=["支 (to pay/support, same 支 as in 지불하다 \"to pay\")",
                "給 (to give, same 給 as in 공급 \"supply\")",
                "생활비로 지급받다 = \"to be paid/disbursed as living expenses\""],
        ),
        "보상": dict(
            meaning="compensation",
            notes=["補 (to supplement/repair, same 補 as in 보완 "
                "\"supplementation\")", "償 (to compensate/repay)",
                "피해에 대해 보상을 받다 = \"to receive compensation for damages\""],
        ),
        "신생아": dict(
            meaning="newborn baby",
            notes=["新 (new, same 新 as in 신도시, 신용카드)",
                "生 (birth/life, same 生 as in 학생 \"student\", 생산 "
                "\"production\")", "兒 (child, same 兒 as in 유아 \"infant\")",
                "literally \"newly-born child\", a baby that has just been "
                "born."],
        ),
        "다국어": dict(
            meaning="multilingual/multiple languages",
            notes=["多 (many, same 多 as in 다가구, 다양하다)",
                "國語 (national language, 國 = nation, 語 = language)",
                "다국어 서비스 = \"multilingual service\""],
        ),
        "이주": dict(
            meaning="migration/relocation",
            notes=["移 (to move/shift, same 移 as in 이사 \"moving house\")",
                "住 (to reside, same 住 as in 주택, 거주)",
                "moving to and living in a different country or region.",
                "이주민 = \"migrant\""],
        ),
        "권익": dict(
            meaning="rights and interests",
            notes=["權 (right/authority, same 權 as in 권위)",
                "益 (benefit, same 益 as in 이익)",
                "a combined term covering both one's legal rights and "
                "practical interests/benefits",
                "이주민의 권익 보호 = \"protecting the rights and interests of "
                "migrants\""],
        ),
        "법무부": dict(
            meaning="Ministry of Justice",
            notes=["法 (law, same 法 as in 법률)",
                "務 (affairs/duty, same 務 as in 업무 \"work/duties\")",
                "部 (ministry/department, same 部 as in 부분 \"part\" — here "
                "used for a government ministry)",
                "the government ministry handling legal/justice affairs"],
        ),
        "여성가족부": dict(
            meaning="Ministry of Gender Equality and Family",
            notes=["女性 (women, 女 = female, 性 = gender/nature)", "家族 (family)",
                "部 (ministry)",
                "the ministry handling women's and family policy"],
        ),
        "다누리": dict(
            meaning="다 (\"all/every\") + 누리 (an old/poetic native word for "
                "\"world\"), meaning roughly \"everyone's world\"",
            notes=["used as a branded name for the call center, not a regular "
                "vocabulary word you'd use elsewhere"],
        ),
        "고용노동부": dict(
            meaning="Ministry of Employment and Labor",
            notes=["雇傭 (employment, 雇 = to hire + 傭 = to hire/employ)",
                "勞動 (labor, 勞 = labor + 動 = to move/act)", "部 (ministry)",
                "the ministry handling employment and labor policy"],
        ),
        "신분증": dict(
            meaning="identification card",
        ),
        "체류": dict(
            meaning="stay/sojourn",
            notes=["滯 (to stay/detain, same 滯 as in 정체 "
                "\"congestion/stagnation\")",
                "留 (to stay/remain, same 留 as in 정류장)",
                "체류 허가 = \"stay permit\"", "체류 기간 = \"period of stay\""],
        ),
        "허가": dict(
            meaning="permission/permit",
            notes=["許 (to allow/permit)",
                "可 (permissible/possible, same 可 as in 불가능 \"impossible\")",
                "체류 허가 = \"residence/stay permit\""],
        ),
        "행정": dict(
            meaning="administration",
            notes=["行 (to act/go, same 行 as in 여행 \"travel\", 통행)",
                "政 (governance/politics, same 政 as in 정책 \"policy\")",
                "출입국 행정 = \"immigration administration\""],
        ),
        "민원": dict(
            meaning="civil complaint/petition",
            notes=["民 (people/citizen, same 民 as in 국민, 훈민정음)",
                "願 (wish/request, same 願 as in 소원 \"wish\")",
                "a request or complaint a citizen files with a government "
                "office", "민원 상담 = \"civil affairs consultation\"."],
        ),
    },
    headwords={"밀렸지만": "밀리다", "곤란한": "곤란하다", "앓게": "앓다"},
    english={
        "사회보험": dict(
            title="Social insurance",
            paragraphs=[
                "Korea has put in place a range of social welfare arrangements so "
                "that its people may enjoy at least a life fit for a human being. "
                "They divide broadly into social insurance and public assistance.",

                "Social insurance is a system the people are required by law to join, "
                "against the risks of the future. It comprises health insurance, "
                "employment insurance, the national pension and industrial accident "
                "compensation insurance.",
            ],
        ),
        "공공부조": dict(
            title="Public assistance",
            paragraphs=[
                "Public assistance is a system under which the state or a local "
                "authority supports living costs, education costs and medical costs, "
                "so as to guarantee a basic standard of living to people whose "
                "circumstances are hard. Those on low incomes, whose income is below "
                "the minimum cost of living, can have their living costs supported "
                "through the National Basic Livelihood Security scheme.",

                "There is also emergency welfare support, for low-income households "
                "that have suddenly met with hardship and cannot keep themselves. If, "
                "for instance, the main earner is badly injured or falls seriously ill "
                "and can no longer work, or a fire makes the house or building they "
                "were living in unfit to live in, one can telephone the responsible "
                "department of the local authority, or the Ministry of Health and "
                "Welfare call centre, and get help.",
            ],
        ),
        "외국인 대상 지원 서비스": dict(
            title="Support services for foreign residents",
            paragraphs=[
                "Of the social welfare arrangements, public assistance applies in "
                "principle only to Korean nationals. But among foreigners living in "
                "Korea, those married to a Korean national, those caring for a parent "
                "or child who holds Korean nationality, and those recognised as "
                "refugees under the law can, if their income is below the minimum cost "
                "of living, receive support for that minimum, for medical costs and "
                "for emergency welfare. Beyond this, programmes are run in which "
                "Korean and Korean culture can be learned free of charge, so that one "
                "may settle into life in Korea and live here on one's own terms. A "
                "female marriage immigrant who is pregnant or about to give birth can "
                "also receive health care services for herself and her newborn.",
            ],
        ),
        "다문화 가족·외국인 지원 기관": dict(
            title="The bodies that support multicultural families and foreigners",
            paragraphs=[
                "Among the bodies supporting multicultural families and foreigners "
                "are the Immigration Contact Center of the Ministry of Justice, the "
                "Danuri Call Center and the Multicultural Family Support Centers of "
                "the Ministry of Gender Equality and Family, and the Foreign Workers' "
                "Support Centers of the Ministry of Employment and Labor.",

                "The Immigration Contact Center (1345) handles enquiries and gives "
                "information in many languages on the immigration administration of "
                "foreigners living in Korea — matters of identification, of residence "
                "permits, of nationality. The Danuri Call Center (1577-1366) provides "
                "the information about life in Korea that multicultural families and "
                "migrant women living here need, and makes it possible to speak with a "
                "specialist counsellor in one's own language for crisis counselling "
                "and emergency support. The Multicultural Family Support Centers "
                "provide education to help such families settle into Korean society, "
                "and services supporting children's language development. The Foreign "
                "Workers' Support Centers provide Korean-language teaching for foreign "
                "workers and support the protection of their rights and interests.",
            ],
        ),
    },

    extraAnnotations={
        "4대 보험": dict(
            hanja="四大保險", meaning="the four major insurances",
            characters=[("四", "사", "four"),
                        ("大", "대", "great, major")],
            notes=["The four the law requires: 국민연금, 건강보험, 고용보험 and 산재보험. "
                   "Your note at the top of p. 41 names them, and every Korean "
                   "employment contract turns on them.",
                   "Set against 개인 보험, the private policies one takes out by "
                   "choice — 생명 보험, 손해 보험, 교육 보험."],
        ),
        "사회보험": dict(
            hanja="社會保險", meaning="social insurance",
            characters=[("社", "사", "society, company — the same 社 as in 회사, 퇴사"),
                        ("會", "회", "to gather — the same 會 as in 회식, 회사"),
                        ("保", "보", "to protect — the same 保 as in 보증금, 보호"),
                        ("險", "험", "risk — as in 위험 “danger”, 산재보험")],
            notes=["Compulsory and contributory: one pays in against a future risk. "
                   "That is what separates it from 공공부조, which is paid out of tax "
                   "to those who need it."],
        ),
        "공공부조": dict(
            hanja="公共扶助", meaning="public assistance",
            characters=[("公", "공", "public — the same 公 as in 공기업, 공공"),
                        ("共", "공", "together — the same 共 as in 공동 주택"),
                        ("扶", "부", "to help, support"),
                        ("助", "조", "to assist — as in 도움, 원조, 보조")],
            notes=["Paid for out of tax and given according to need, with nothing "
                   "contributed by the recipient — the other half of the pair with "
                   "사회보험. In principle for nationals only, which is what part 02 "
                   "of the chapter qualifies."],
        ),
        "가입": dict(
            hanja="加入", meaning="joining, enrolling",
            characters=[("加", "가", "to add — as in 추가 “addition”, 참가"),
                        ("入", "입", "to enter — the same 入 as in 세입자, 수입")],
            notes=["The word for signing up to anything with membership: insurance, a "
                   "union, a website. 산재보험에 가입하다."],
        ),
        "건강보험": dict(
            hanja="健康保險", meaning="health insurance",
            characters=[("健", "건", "healthy — as in 건강, 건전"),
                        ("康", "강", "at ease, healthy")],
        ),
        "고용보험": dict(
            hanja="雇用保險", meaning="employment insurance",
            characters=[("雇", "고", "to hire — as in 고용 “employment”, 해고"),
                        ("用", "용", "to use — the same 用 as in 전용, 이용")],
            notes=["What pays out on being dismissed. Its counterpart 해고 “dismissal” "
                   "uses the same 雇."],
        ),
        "국민연금": dict(
            hanja="國民年金", meaning="the national pension",
            characters=[("國", "국", "country"),
                        ("民", "민", "people — the same 民 as in 훈민정음, 결혼이민자"),
                        ("年", "년", "year — the same 年 as in 연령, 노년"),
                        ("金", "금", "money — the same 金 as in 보증금, 임금")],
        ),
        "산업재해보상보험": dict(
            hanja="産業災害補償保險", meaning="industrial accident compensation insurance",
            characters=[("災", "재", "disaster — the same 災 as in 재난"),
                        ("害", "해", "harm — as in 피해 “damage”, 해로운"),
                        ("補", "보", "to supplement, make up — as in 보충, 보완"),
                        ("償", "상", "to compensate — as in 보상, 배상")],
            notes=["Shortened to 산재보험, and to 산재 in speech — which is how your "
                   "note on p. 41 writes it. Chapter 6's article on seasonal workers "
                   "turns on who may join it."],
        ),
        "국민연금공단": dict(
            hanja="國民年金公團", meaning="the National Pension Service",
            characters=[("公", "공", "public"),
                        ("團", "단", "group, body — as in 단체 “organisation”, 집단")],
            notes=["공단 is the word for a public corporation run at arm's length from "
                   "a ministry. Enquiries on 1355."],
        ),
        "보건복지부": dict(
            hanja="保健福祉部", meaning="the Ministry of Health and Welfare",
            characters=[("保", "보", "to protect — the same 保 as in 보험, 보장"),
                        ("健", "건", "healthy — the same 健 as in 건강보험"),
                        ("福", "복", "blessing, welfare — the 福 of 복지"),
                        ("祉", "지", "welfare, blessing"),
                        ("部", "부", "ministry — the same 部 as in 법무부, 여성가족부")],
            notes=["보건 is public health and 복지 is welfare; the ministry covers both. "
                   "Its counselling line is 129, and the box on p. 41 notes that it "
                   "supports medical costs even for foreign residents who fall outside "
                   "the medical insurance schemes."],
        ),
        "최저 생계비": dict(
            hanja="最低生計費", meaning="the minimum cost of living",
            characters=[("最", "최", "most — as in 최고 “highest”, 최근 “recently”"),
                        ("低", "저", "low — the same 低 as in 저소득층"),
                        ("生", "생", "life"),
                        ("計", "계", "to reckon, plan — as in 계획 “plan”, 통계"),
                        ("費", "비", "expense — as in 의료비, 생활비, 교통비")],
            notes=["The threshold the whole of 공공부조 is measured against: fall below "
                   "it and the support applies."],
        ),
        "저소득층": dict(
            hanja="低所得層", meaning="the low-income bracket",
            characters=[("低", "저", "low"),
                        ("所", "소", "that which — the same 所 as in 소유권, 주소"),
                        ("得", "득", "to obtain — as in 획득, 소득"),
                        ("層", "층", "layer, stratum — the same 層 as in 층간 소음, 계층")],
            notes=["층 is the same character as a storey of a building, used here of a "
                   "stratum of society. 소득 is income."],
        ),
        "생계": dict(
            hanja="生計", meaning="livelihood, making a living",
            characters=[("生", "생", "life"),
                        ("計", "계", "to reckon, plan")],
            notes=["생계 유지 is keeping oneself; 생계급여 is the livelihood benefit whose "
                   "thresholds are tabled on p. 42."],
        ),
        "긴급": dict(
            hanja="緊急", meaning="urgent, emergency",
            characters=[("緊", "긴", "tight, tense — as in 긴장 “tension”"),
                        ("急", "급", "urgent, hurried — as in 급하다, 응급")],
        ),
        "수준": dict(
            hanja="水準", meaning="level, standard",
            characters=[("水", "수", "water — the same 水 as in 수로, 수질"),
                        ("準", "준", "standard, to prepare — as in 준비, 기준")],
            notes=["From the water level of a builder's level: the line something is "
                   "measured against. 세계 최고 수준 in chapter 4, 생활 수준 here."],
        ),
        "보장": dict(
            hanja="保障", meaning="to guarantee, secure",
            characters=[("保", "보", "to protect"),
                        ("障", "장", "to obstruct, shield — as in 장애 “disability”, 고장")],
            notes=["Of a right or a standard the state undertakes to hold up: "
                   "기초생활보장, 사회보장. The 학습목표 uses it of 인간다운 삶."],
        ),
        "소득": dict(
            hanja="所得", meaning="income",
            characters=[("所", "소", "that which"),
                        ("得", "득", "to obtain, gain")],
            notes=["Literally what one gets. Distinct from 수입, which is also income "
                   "but can mean imports too."],
        ),
        "기초생활보장": dict(
            hanja="基礎生活保障", meaning="basic livelihood security",
            characters=[("基", "기", "foundation — the same 基 as in 기초생활수급자"),
                        ("礎", "초", "cornerstone")],
            notes=["The scheme; 기초생활수급자, met in chapter 5, is the person on it."],
        ),
        "화재": dict(
            hanja="火災", meaning="a fire",
            characters=[("火", "화", "fire — as in 화요일, 소화기"),
                        ("災", "재", "disaster — the same 災 as in 재난, 산재")],
            notes=["A different 화 from the 化 of 도시화 or the 和 of 화합."],
        ),
        "담당": dict(
            hanja="擔當", meaning="being in charge of",
            characters=[("擔", "담", "to bear, shoulder — as in 부담 “burden”, 분담"),
                        ("當", "당", "to correspond to — as in 당시, 상당하다")],
            notes=["담당 부서 is the department responsible; 담당자 the person handling "
                   "your case — the word you want at any Korean counter."],
        ),
        "재난": dict(
            hanja="災難", meaning="a disaster",
            characters=[("災", "재", "disaster"),
                        ("難", "난", "difficulty — the same 難 as in 취업난")],
        ),
        "한시적": dict(
            hanja="限時的", meaning="for a limited time",
            characters=[("限", "한", "limit — as in 제한 “restriction”, 한계"),
                        ("時", "시", "time — as in 시간, 당시"),
                        ("的", "적", "-ic, -al")],
            notes=["Of a measure with an end date built in, which is how the "
                   "pandemic payments were framed."],
        ),
        "취약가정": dict(
            hanja="脆弱家庭", meaning="a vulnerable household",
            characters=[("脆", "취", "brittle, fragile"),
                        ("弱", "약", "weak — as in 약하다, 강약")],
            notes=["취약계층 is the wider term for vulnerable groups. These households "
                   "were paid in cash without having to apply."],
        ),
        "원칙적": dict(
            hanja="原則的", meaning="in principle, as a general rule",
            characters=[("原", "원", "origin — the same 原 as in 원리, 원인"),
                        ("則", "칙", "rule — as in 규칙 “rule”, 법칙"),
                        ("的", "적", "-ic, -al")],
            notes=["Carries the same implication as the English: what follows is the "
                   "rule, and exceptions are about to be named. Here they are — the "
                   "sentence after it lists who does qualify."],
        ),
        "혼인": dict(
            hanja="婚姻", meaning="marriage",
            characters=[("婚", "혼", "marriage — the same 婚 as in 결혼, 미혼, 기혼"),
                        ("姻", "인", "marriage tie, affinity")],
            notes=["The legal word where 결혼 is the everyday one: 혼인신고 is "
                   "registering a marriage."],
        ),
        "국적": dict(
            hanja="國籍", meaning="nationality",
            characters=[("國", "국", "country"),
                        ("籍", "적", "register, record — as in 호적, 학적")],
        ),
        "난민": dict(
            hanja="難民", meaning="a refugee",
            characters=[("難", "난", "difficulty — the same 難 as in 재난, 취업난"),
                        ("民", "민", "people")],
            notes=["Literally people in hardship. 난민 인정 is recognition of refugee "
                   "status, which is what the passage means by 법에 따라 난민으로 인정된."],
        ),
        "주체적": dict(
            hanja="主體的", meaning="on one's own terms, as an agent",
            characters=[("主", "주", "master, main — as in 주인 “owner”, 주로"),
                        ("體", "체", "body — as in 신체, 업체"),
                        ("的", "적", "-ic, -al")],
            notes=["주체 is the subject that acts, against 대상, the object acted on — "
                   "and 대상 is the very word in this chapter's other heading, "
                   "외국인 대상 지원 서비스. The two sit oddly close together."],
        ),
        "임신": dict(
            hanja="妊娠", meaning="pregnancy",
            characters=[("妊", "임", "to conceive"),
                        ("娠", "신", "to be with child")],
        ),
        "신생아": dict(
            hanja="新生兒", meaning="a newborn",
            characters=[("新", "신", "new — as in 신도시, 신설"),
                        ("生", "생", "to be born"),
                        ("兒", "아", "child — the same 兒 as in 육아 “childcare”")],
        ),
        "법무부": dict(
            hanja="法務部", meaning="the Ministry of Justice",
            characters=[("法", "법", "law — as in 법률, 법원"),
                        ("務", "무", "duty — the same 務 as in 업무협약, 공무원"),
                        ("部", "부", "ministry, part — as in 보건복지부, 부서")],
            notes=["Runs the 외국인 종합 안내센터 on 1345, and immigration generally."],
        ),
        "여성가족부": dict(
            hanja="女性家族部", meaning="the Ministry of Gender Equality and Family",
            characters=[("女", "여", "woman — as in 여성, 자녀"),
                        ("性", "성", "sex, nature — the same 性 as in 양성평등")],
            notes=["Runs the 다누리 콜센터 and the 다문화 가족 지원센터."],
        ),
        "고용노동부": dict(
            hanja="雇用勞動部", meaning="the Ministry of Employment and Labor",
            characters=[("雇", "고", "to hire — the same 雇 as in 고용보험"),
                        ("勞", "로", "to labour — the same 勞 as in 근로자"),
                        ("動", "동", "to move — the same 動 as in 활동, 부동산")],
        ),
        "신분증": dict(
            hanja="身分證", meaning="an identity document",
            characters=[("身", "신", "body, self — as in 신체, 자신"),
                        ("分", "분", "to divide, status — the same 分 as in 분산, 분리수거"),
                        ("證", "증", "proof — the same 證 as in 보증금, 증명")],
            notes=["For a foreign resident this means the 외국인등록증."],
        ),
        "체류": dict(
            hanja="滯留", meaning="staying, residing in a country",
            characters=[("滯", "체", "to be held up, stagnate"),
                        ("留", "류", "to remain")],
            notes=["Also in chapter 6, of the seasonal worker's period of stay. "
                   "체류 허가 is the residence permit this centre advises on."],
        ),
        "출입국": dict(
            hanja="出入國", meaning="immigration and emigration",
            characters=[("出", "출", "to go out — the same 出 as in 진출, 출산"),
                        ("入", "입", "to enter"),
                        ("國", "국", "country")],
            notes=["Going out and coming in, taken together — the Korean name for what "
                   "English calls immigration: 출입국·외국인청."],
        ),
        "민원": dict(
            hanja="民願", meaning="a citizen's request to an office",
            characters=[("民", "민", "people"),
                        ("願", "원", "to wish, request — as in 지원, 소원")],
            notes=["Anything a member of the public asks an administrative office to "
                   "do — a certificate, a registration, a complaint. 민원을 넣다 is to "
                   "file one."],
        ),
        "다국어": dict(
            hanja="多國語", meaning="multiple languages",
            characters=[("多", "다", "many — the same 多 as in 다문화, 다세대"),
                        ("國", "국", "country"),
                        ("語", "어", "language — as in 한국어, 언어")],
            notes=["The 1345 centre works in twenty of them, per the figure on p. 42."],
        ),
        "이주": dict(
            hanja="移住", meaning="migration, moving to live elsewhere",
            characters=[("移", "이", "to move — the same 移 as in 이직, 이사"),
                        ("住", "주", "to dwell — the same 住 as in 주거, 주택")],
            notes=["이주 여성 and 이주 노동자 are the terms the chapter and the discussion "
                   "use, and are preferred to older words for the same people."],
        ),
        "권익": dict(
            hanja="權益", meaning="rights and interests",
            characters=[("權", "권", "right — the same 權 as in 권위, 소유권"),
                        ("益", "익", "benefit, profit — as in 이익 “profit”, 유익하다")],
        ),
        "재외 동포": dict(
            hanja="在外同胞", meaning="an overseas Korean",
            characters=[("在", "재", "to exist, be at — as in 현재 “the present”, 재학"),
                        ("外", "외", "outside — the same 外 as in 시외버스, 외국"),
                        ("同", "동", "same — the same 同 as in 공동, 동료"),
                        ("胞", "포", "womb, kin")],
            notes=["동포 is literally from the same womb — a person of Korean descent "
                   "living abroad, or returned. A different legal footing again from "
                   "결혼이민자 or 난민."],
        ),
        "자문": dict(
            hanja="諮問", meaning="professional advice",
            characters=[("諮", "자", "to consult"),
                        ("問", "문", "to ask — as in 질문 “question”, 문의")],
            notes=["Of expert counsel sought from outside: 법률 자문, 자문위원. Not the "
                   "자 of 자기 or 자신."],
        ),
        "형제": dict(
            hanja="兄弟", meaning="brothers, siblings",
            characters=[("兄", "형", "elder brother — as in 형, 형님"),
                        ("弟", "제", "younger brother — as in 제자, 사제")],
            notes=["Used figuratively in the article: the migrant workers the doctor "
                   "counts as family besides his own."],
        ),
        "서툴러": dict(
            headword="서투르다", meaning="to be clumsy, unpractised",
            notes=["Native Korean, of a skill not yet mastered — here of Korean not "
                   "well enough to say what one means. 서툴다 is the shortened form."],
        ),
    },

    extraNotes=[
        "The 사회보험 table on p. 41 and the 생계급여 thresholds on p. 42 are set as "
        "tables. The four photographs in 생각해 봅시다 are described in one caption "
        "rather than four, since the page gives them no labels.",
        "Your bracketed taxonomy at the top of p. 41 — 개인 보험 over 사회 보험, with "
        "three and four under them — is set as a two-level list. 4대 보험 names the "
        "four under 사회 보험.",
    ],
)
