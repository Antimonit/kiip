# Open questions

Things I decided on my own and would rather you confirmed, and things I could
not resolve. Newest first. Delete a line once it is settled.

## Where things stand

Chapters 1 to 29 are built — 제1편 사회, 제2편 교육, 제3편 문화, 제4편 정치 and
제5편 경제 complete, with the spreads that close 제4편 and 제5편. Chapters 1 to
12 come from your Google Docs, with chapter 10 as the exception — its Doc
carries no comments and six typos, so it stays as I transcribed it. Chapters
13 to 29 have no Doc at all: your transcriptions stop at chapter 12, so their
Korean is my reading of the pages.

Every chapter now carries its own text. The Docs were read one last time and
written into the modules, so the build needs nothing outside the repository,
and no payload changed by a byte in the process.

| ch | title | annotations | articles | rows | gaps | corrections open |
|----|-------|------------:|---------:|-----:|-----:|-----------------:|
| 1 | 한국의 상징 | 53 | 5 | 26 | – | – |
| 2 | 가족 | 32 | 4 | 26 | 10 | – |
| 3 | 일터 | 51 | 4 | 27 | 9 | 1 |
| 4 | 교통과 통신 | 58 | 5 | 27 | 11 | – |
| 5 | 주거 | 80 | 4 | 31 | 9 | – |
| 6 | 도시와 농촌 | 94 | 5 | 33 | 8 | – |
| 7 | 복지 | 60 | 4 | 17 | 13 | – |
| 8 | 의료와 안전 | 97 | 4 | 26 | 11 | 22 |
| 9 | 보육 제도 | 75 | 5 | 28 | 9 | 13 |
| 10 | 초·중등 교육 | 79 | 4 | 25 | 12 | – |
| 11 | 고등 교육과 입시 | 53 | 4 | 26 | 11 | 14 |
| 12 | 평생 교육 | 36 | 4 | 19 | 9 | 21 |
| 13 | 전통 가치 | 91 | 4 | 37 | 6 | – |
| 14 | 전통 의식주 | 112 | 4 | 36 | 13 | – |
| 15 | 의례 | 110 | 5 | 32 | 6 | – |
| 16 | 명절 | 91 | 4 | 29 | 6 | – |
| 17 | 종교 | 115 | 6 | 35 | 9 | – |
| 18 | 대중문화 | 134 | 4 | 31 | 6 | – |
| 19 | 여가문화 | 112 | 4 | 24 | 6 | – |
| 20 | 한국의 민주 정치 | 115 | 4 | 28 | 11 | – |
| 21 | 입법부 | 113 | 6 | 29 | 6 | – |
| 22 | 행정부 | 129 | 5 | 25 | 6 | – |
| 23 | 사법부 | 122 | 5 | 34 | 7 | – |
| 24 | 선거와 지방자치 | 60 | 5 | 13 | 8 | – |
| 25 | 일상생활과 경제 활동 | 103 | 4 | 27 | 9 | – |
| 26 | 경제 성장 | 130 | 4 | 28 | 7 | – |
| 27 | 장보기와 소비자 보호 | 97 | 4 | 28 | 7 | – |
| 28 | 금융기관 이용하기 | 110 | 4 | 33 | 7 | – |
| 29 | 취업하기 | 96 | 4 | 26 | 5 | – |

Chapters 10 and 13 to 29 have no corrections column because there was no
transcription to correct. Errors there are in the text itself, and they are
mine.

## The whole book

The 교재 구성 (pp. 6-11) and 차례 (pp. 12-13) give the plan: fifty chapters in
eight 편, and they are now transcribed into `tools/chapters/contents.py` and
listed on the index page.

| 편 | chapters | pages |
|----|----------|-------|
| 1 사회 | 1-8 | 16-47 |
| 2 교육 | 9-12 | 54-69 |
| 3 문화 | 13-19 | 76-103 |
| 4 정치 | 20-24 | 110-129 |
| 5 경제 | 25-29 | 136-155 |
| 6 법 | 30-37 | 162-193 |
| 7 역사 | 38-44 | 200-227 |
| 8 지리 | 45-50 | 234-257 |

Then 정답보기 at 262 and 찾아보기 at 272.

- **The topic tags are gone.** They were a stand-in for structure I did not
  have when the site started: three per chapter, invented. With the book's
  own 편 on the page they earned nothing — of 31 tags, 20 sat on a single
  chapter, and 문화 and 교육 only restated the part. Only 제도, 생활, 가족 and
  외국인 지원 crossed a part at all. The 편 are the grouping now, and each
  wears the colour the book gives it.
- **The part colours are a step deeper than print.** The book sets white on
  them, which needs more depth at screen sizes; the hues are the book's and
  every chip clears 4.5:1. Dark mode lifts them again so a part reads the
  same against either ground.
- **The missing pages are the part openers.** Every gap in the photo folders
  falls between one 편's last chapter and the next 편's first: 48-53, 70-75,
  104-109, 130-135, 156-161, 194-199, 228-233, and 258-261 before 정답보기.
  Six pages each. So the intermezzos you mentioned are one per part, and
  none of them is a chapter.
- **Chapter 20 starts on p. 110, not 104.** The empty `Chapter 20` folder
  wants pp. 110-113.
- **All nineteen built chapters check out against 교재 구성.** Their titles and
  both article headings match the book's own 본문 column exactly, which is an
  independent check on the transcriptions — including the seven read off the
  photos with no Doc.

## Source material

- **A margin-glossary word is now clickable in the prose as well.** The
  textbook glosses a word in the margin and then uses it a line or two later;
  only the gloss carried the annotation unless the Doc happened to comment on
  the prose too. The first place the article says it is now marked, headings
  included, which is where 장려, 무선 and 활성화 came from in chapter 4. It
  added 60-odd clickable words across the fifteen chapters.
- **A correction whose two sides look identical** is a correction that
  falls on an annotation boundary: what changes is a space at the edge of a
  run. Give such a fix its fourth element, the pair to display, and it reads
  properly. Chapter 1's 강조 하고 was the case that showed this up.
- **Chapters 11 and 12 have Docs with almost no comments** — four on chapter
  11 and none on chapter 12 — so the annotations there are nearly all mine,
  as in chapter 10. The Korean is yours and was checked against the pages.
- **Chapter 11's Doc stops after the 유학생 table.** 주요 내용정리 and
  이야기 나누기 are transcribed from the photo of p. 65 and appended.
- **Chapter 11's chart plots one series of three.** The graph on p. 63 tracks
  progression to middle school, to high school and to higher education. The
  first two sit flat at about 100% and would flatten the third, so only the
  third is drawn and the caption gives the other two.
- **The sketch at the top of chapter 12's p. 66 is not on the page.** You drew
  평생 교육 as a line running past 학교 on both sides. I did not want to put
  words in your mouth, so nothing stands in for it — say what it should read
  and I will add it.
- **The Doc exports are no longer on disk.** `~/Downloads` has none of
  1.html–12.html any more, so chapters 1–9, 11 and 12 cannot be rebuilt: the
  build skips them with a warning and keeps the files they generated last
  time. Those files are checked in, so the site is unaffected — but a change
  to one of those chapters' modules will silently not take effect. The fix is
  to keep the exports in the repo under `source/`; say the word next time you
  have them and I will move them there.
- **Chapters 13 to 19 have no Doc**, since yours stop at chapter 12. Their
  Korean is transcribed from the photos by me, which inverts the usual
  direction: the photos are the only source, so everything in them is worth a
  closer read than usual, and their `fixes` lists are empty because there was
  no transcription to correct.
- **Chapter 15's 장례식 article is hard to read on p. 86.** The sentences
  about the third day appear twice over, once faintly. I took the fainter run
  as show-through from the facing page and kept the darker one, but that
  paragraph is worth checking against the book.
- **Two chapters have more than four prose articles.** Chapter 15 has five —
  the first part runs 결혼식, 돌잔치, 성년식 and the second 장례식, 제사 — and
  chapter 17 has six, four under the first part and two under the second. All
  of them are translated.
- **Two figures in chapter 19 are not drawn as charts.** The 여가시간 및
  여가비용 추이 graph on p. 101 layers three series over eight years, and its
  numbers cannot be read reliably off the photograph, so it is described
  rather than reproduced with invented values. The 여가활동 목적 figure on
  p. 103 gives 2015 against 2018, which one bar chart cannot show, so it is
  set as a table.
- **Chapter 18's warm-up is a four-panel comic.** The speech bubbles are too
  small to read off the photograph, so the panels are described in one caption
  and only the four words you wrote beside them are set as labels.
- **Chapter 17's pie chart is drawn short.** The figure on p. 94 has eight
  slices; 원불교, 유교, 천도교 and 기타 are too small to read off the page and
  come to under 1% between them, so the four large ones are drawn and the
  caption says what is left out.
- **Chapter 16's 24절기 box** is a table of four seasons against six terms
  each. The terms are set one cell to a season, which is how the page prints
  them.
- **Pages 48–53 are missing.** The photo folders run 16–19 (ch. 1) through
  44–47 (ch. 8), then jump to 54–57 (ch. 9). Six pages are unaccounted for
  between chapters 8 and 9 — most likely an intermezzo, since you mentioned
  those exist. Chapters 9 and 10 are built from the photos that are there.
- **Chapter 1's folder holds eight files**: `16.jpg`–`19.jpg` plus four
  `PXL_*.jpg`. I used the numbered four; the PXL ones look like a second pass
  over the same pages. Worth deleting one set.
- **Chapter 9 is where the unit changes** from 사회 to 교육 — the page header
  reads `9 교육` and the footer `02 교육`. Chapters 9 and 10 are set to 교육.
- **Chapters 5–10 were built from the photos first, then rebuilt from your
  Docs.** Before rebuilding, the two readings were compared line by line. All
  sixteen differences were slips in the Doc and none were misreadings of the
  page — 치어지는 for 지어지는, 팔고물 for 팥고물, 위생 도시 for 위성 도시,
  농사 for 농가, 근로게약서, 화공말, 공공 7관, 물래, 해지고, 이간보육, 수입이
  for 수업이, 초등하교, 100만 월, 껵거나, 방지될, 보와이. Those and the
  spacing slips are now `fixes` for you to accept or reject.
- **Chapter 10 is still built from the photos.** Its Doc has no comments at
  all, so there is nothing to gain from it, and it carries six typos my
  reading does not. Add comments to that Doc and I will switch it over.
- **Chapter 10's title differs between the two.** The Doc reads
  초·중등 학교, the page reads 초·중등 교육. The page wins.
- **Chapter 7's 사회보험 translation is left whole.** Your comment there also
  translates the four rows of the 건강보험/고용보험 table, so it cannot be cut
  to the shape of the two Korean paragraphs. It reads fine as one block.
- **Chapter 5's 거주 형태와 집 구하는 방법 translation stops part-way**, at
  확정 일자, leaving 월세 and 반전세 and the second paragraph untranslated. The
  page falls back to the English I wrote for that section.
- **Chapter 9's Doc has two stray English words** left in the 이야기 나누기
  section (`prenatal education`, `behavior`). They are dropped.
- **Chapter 8's Doc has no 학습목표 or 관련 단원 확인하기 section.** Both are
  inserted from the photos of p. 44.

## Decisions I made without asking

- **Two figures were split in two** because their halves are counted in
  different units and one bar chart would flatten the smaller series to
  nothing: chapter 6's 농가인구 / 고령인구, and chapter 8's total casualties
  against deaths. Chapter 6 and 8's notes say so on the page.
- **A bracketed diagram is a two-level list, not a merged table.** Your
  개인 보험 / 사회 보험 taxonomy at the top of chapter 7's p. 41 could be set
  either way now that merged cells work. It stays a list: it is a hierarchy
  rather than a grid, nine words would carry fourteen cell borders, and it is
  marginalia, which should read lighter than the book's own tables. Merged
  cells are for the tables that really are tables.
- **The unit table is set centred**, as the book sets it. It is the only
  table that is: the tables inside an article run to the left with their
  prose. The section carries a `--cell-align` token for it.
- **The “this chapter has no Google Doc” note was stale in four chapters.**
  Chapters 5, 7, 8 and 9 kept it after they were rebuilt from your Docs, so
  the page was telling the reader the opposite of the truth. It is gone from
  those four. Chapter 10's now says what is actually the case: the Doc exists
  but has no comments and six typos, so the photos are used instead.
- **Chapter 5's warm-up is now grouped, not tagged.** The four photos on
  p. 32 are two 단독 주택 (양옥, 한옥) over two 공동 주택 (빌라, 아파트) — the
  division the first article then explains. The words written beside the rows
  on the page name those two kinds; I had read them as notes on the two
  questions and put them in the margin. They are now the headings the labels
  sit under. The first label is 양옥, settled with your colleagues.
- **Row-spanning table cells work now.** Chapter 10's 학사 일정 groups its
  rows under 1학기 / 2학기 with a merged cell, and the 관련 단원 tables in
  chapters 13 and 15 merge 기본 and 문화 across their two rows; all three used
  to repeat the value on every row. `SPAN(text, down=n)` is the row-wise
  counterpart of `SPAN(text, n)`.
- **Two tables were reshaped to read on a narrow screen.** Chapter 15's table
  of age names is printed four age-and-name pairs across, three rows deep; it
  is set here as one two-column table of twelve rows. Chapter 13's warm-up
  puts two lines of dialogue in a cell; they are run onto one line.
- **Chapter 14's warm-up is a world map**, with a bubble over each region and
  a small bar chart of 2009, 2014 and 2017 beside it. Only the 2017 totals
  are drawn, one bar per region, and the China and Japan figures are given in
  the caption.
- **"All four articles" read as the main prose articles** of each chapter —
  the two under each numbered part. The 알아두면 좋아요 boxes, 생각해 봅시다,
  주요 내용정리 and 이야기 나누기 are left untranslated. Say the word and I
  will do those too.
- **Translations are mine, not the textbook's**, except where a Doc comment
  supplies one. Chapters 3 to 9 now carry translations you wrote; where a
  section has none, or where yours does not divide the same way as the
  Korean, mine stands in. Chapter 10's are all mine.
- **An annotation written in a chapter module now attaches itself** to the
  first place its word is said, so an entry no longer has to wait for a Docs
  comment to become clickable. This is why chapters 1, 3 and 4 gained a few
  annotations without their content changing.
- Chapter 1's 한국의 국가 and chapter 3's 직장 근무 시간과 근무 유형 are each
  one paragraph the Doc broke in two mid-sentence. They are rejoined, which
  changes the paragraph count against the Doc.

## The part-closing spreads

Pages 130 to 133 are not a chapter. They close 제4편 with 대단원 정리 (a table
of what each chapter covered, and four government web addresses), a
가로세로 퀴즈 crossword, 단원 종합 평가 — multiple-choice questions over the whole
part — and two illustrated features, 일상생활과 민주주의 and
한국 대통령과 만난 정상들. The page gaps I had put down to part openers are
these: every 편 ends with such a spread.

제4편's and 제5편's are built, at `lesson.html?ch=part-4` and `?ch=part-5`,
linked from each part's header on the contents. They are built and read
exactly as a chapter is; only what the page calls itself differs. The other
six wait on photographs.

제5편's closing pages run to four as well, the last two being 화폐 이야기 — the
coins and the notes, with what is pictured on each. Those two tables are the
book's own words; the coins and notes themselves are not reproduced.

Two things in it are mine rather than the book's. The crossword grid is not
reproduced — only its clues, with the answers covered — and every answer,
crossword and 종합 평가 alike, is worked out from the chapters, because the
book's own key is in 정답보기 on p. 262 and that page is not photographed. If
one of them is wrong the book is not to blame. Two slips in them are the
book's own and stand as printed: 제4편's question 04 asks about ㉠ and ㉡ while
its 〈보기〉 box is labelled ㄱ and ㄴ, and 제5편's clue ㉲ prints 반듯이 where
반드시 is the word.

Chapter 21's review gaps hold your own pencilled answers — 입법부, 300, 법,
예산, 감사 — since the book leaves them blank and you filled them in. The one
you left blank, 국회의원, is blank here too. Chapters 22 to 24 are blank
throughout, as the book has them.

## Still to review

- Chapters 1, 2, 4, 5, 6 and 7 have been all the way through you. What was
  rejected and reverted: 이 때 in chapter 1; 대중교통안 and 버스도착 in chapter
  4; and in chapter 5, 어떤 것 입니까, 수 천, 초대 받은 and 이야기 해 봅시다, all
  four because the book really does set the space. That last one was accepted
  in chapter 1 and rejected here, so the two pages differ — worth remembering
  that spacing is a per-page judgement and not a rule. Chapter 6's thirteen
  and chapter 7's twelve were all accepted.
- Chapters 11 and 12: 14 and 21 corrections, all found by reading the Doc
  against the pages, none of them checked by you.
- Chapters 13 to 29: no corrections to review, but the Korean itself is my
  transcription and has been read by nobody else.
- Chapter 25's 공공 요금 gloss prints 목적하는 하는, with 하는 twice over. That
  is the book's own slip and stands as printed.
- Chapter 26's margin heads its OECD entry 경제협력기구, one word short of
  경제협력개발기구, which is how the article itself writes it. Both stand as
  printed, and the entry is filed under the full name.
- Four figures in 제5편 are not reproduced — chapter 25's 소비자물가 추이 line
  chart and 간편 결제 chart, chapter 27's 모바일쇼핑 거래액 graphic and
  오프라인·온라인 쇼핑 현황 chart. Their figures are too small to read off the
  photographs with any confidence. Every other chart in the part is drawn.
- Chapter 28's ATM gloss is my own wording: the book heads the entry
  ATM(현금자동입출금기) and leaves the definition to the article.
- Chapter 21's 국정 감사 article prints 궁금한, which is how the book spells it
  in chapter 8 too, so it stands.
- Chapter 22's aside on 청와대 is left as the book has it. The president's
  office moved to 용산 in 2022, two years after this printing, and the grounds
  are open to visitors now.
- Three tables are set as lists because the book prints them with no header
  row: chapter 23's three principles of a suspect's rights, and chapter 24's
  four principles of an election and their opposites. Each names itself in
  bold instead.
- Chapter 18's p. 98 reads 뛰어난 춤 실력을 뽑을 수 있다 as far as I can make
  out, which would be a slip for 꼽을; the book writes 꼽을 수 있다 elsewhere,
  so it is set that way. Its 기생충 box says 4개 부분 where 부문 is the word,
  and p. 102 prints 워라벨 where the standard is 워라밸 — both set as printed,
  since they are the book's own.
- Chapter 16's p. 90 prints ‘경칩,’ with the comma inside the closing
  quotation mark. That is the book's own slip and is set as printed.
- Chapter 3: the 남녀 경제 활동 참가율 figure needs better formatting — the page
  has a line chart of two series over time and it is drawn as one bar a year.
- Chapter 2's review gaps: the book prints `( 호칭 )로`, but 호칭 ends in a
  consonant and wants `으로`. It is the textbook's own slip, so it stands.
- The margin memos still show their English inline (`세계기록 world record`).
  I read those as your marginalia presented as marginalia, unlike the
  handwriting that sat inside the textbook's own text.
