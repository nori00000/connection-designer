# Project Metadata / 프로젝트 메타데이터

## Overview / 개요

Connection Designer is a static presentation and portfolio page. It explains a personal work narrative around AI-assisted operations, public-interest projects, gardening/landscape work, and project connections.

Connection Designer는 정적 발표/포트폴리오 페이지입니다. AI 기반 운영, 공익 프로젝트, 조경·정원 작업, 프로젝트 간 연결성을 설명하는 개인 발표 자료입니다.

## Purpose / 목적

- Present a portfolio narrative in a browser-friendly static HTML format.
- Help people understand the relationship between multiple projects and domains.
- Help AI tools identify this repository as presentation content, not a reusable product codebase.

- 브라우저에서 볼 수 있는 정적 HTML 형식으로 포트폴리오 서사를 보여줍니다.
- 여러 프로젝트와 도메인 사이의 관계를 사람이 쉽게 이해하게 합니다.
- AI 도구가 이 레포를 재사용 가능한 제품 코드가 아니라 발표/콘텐츠 레포로 인식하게 합니다.

## Keywords / 키워드

- Korean / 한국어: 발표자료, 포트폴리오, AI 운영, 조경, 쇼가든, 사회혁신, 공공 데이터, 프로젝트 연결, 정적 HTML
- English: presentation, portfolio, AI operations, landscaping, show garden, social innovation, public data, project connections, static HTML
- Technical / 기술: HTML, CSS, Reveal.js presentation (reveal.js@5.1.0 via jsdelivr CDN), static site, GitHub Pages <!-- DOC-SYNC: 2026-08-10 재검증 — GitHub Pages 실배포 status=built/public=true 유지 확인(`gh api repos/nori00000/connection-designer/pages`). "Reveal.js-style"을 "Reveal.js"로 정정: presentation.html이 reveal.js@5.1.0 라이브러리를 CDN에서 직접 로드해 사용 중(자체 CSS 모사가 아님, presentation.html:8-9,1106 `<script src=".../reveal.js@5.1.0/dist/reveal.js">` 실측). -->

## Repository Contents / 레포 내용

- `index.html`: overview page / 개요 페이지
- `presentation.html`: slide-style presentation / 슬라이드형 발표 자료
- `msf-showgarden.jpg`: neutral placeholder image replacing a rights-unclear binary image / 권리 출처가 불명확했던 이미지를 대체한 중립 placeholder 이미지
- `NOTICE.md`: presentation asset and trademark notice / 발표 자산과 상표 고지
- `PROJECT.md`: this file — bilingual project metadata, keywords, and reuse boundaries / 이 문서 — 이중언어 프로젝트 메타데이터, 키워드, 재사용 범위
- `README.md`: entry-point summary linking to this file and NOTICE.md / 이 문서와 NOTICE.md로 연결되는 진입점 요약
<!-- DOC-SYNC: 2026-08-15 재검증 — README.md는 PROJECT.md·NOTICE.md 목록에 있으나 PROJECT.md 자신은 이 목록에서 누락되어 있었음(UNDOCUMENTED gap). 자기참조 항목 추가로 현행화. -->

## Copyright And Reuse / 저작권과 재사용

The source structure and simple static page code may be reused where applicable, but the presentation text, personal biography, project descriptions, organization names, event references, images, screenshots, and visual assets are not automatically licensed for reuse.

정적 페이지 구조와 간단한 소스 코드는 필요한 경우 재사용할 수 있지만, 발표 텍스트, 개인 약력, 프로젝트 설명, 기관명, 행사 참조, 이미지, 스크린샷, 시각 자산은 자동으로 재사용 허가되는 것이 아닙니다.

Third-party organization names and service names are used for factual context only. No affiliation, sponsorship, or endorsement is implied.

제3자 기관명과 서비스명은 사실 맥락 설명을 위해서만 사용됩니다. 제휴, 후원, 보증을 의미하지 않습니다.

See `NOTICE.md` before reusing any content or assets from this repository.

이 레포의 콘텐츠나 자산을 재사용하기 전에는 `NOTICE.md`를 확인하세요.
