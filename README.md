<div align="center">

<img src="assets/terminal.svg" width="100%" alt="SON MIN WOO · AI Engineer | Software Developer · since 2023.07"/>

<br/>

<a href="https://solved.ac/smw508/"><img src="http://mazassumnida.wtf/api/mini/generate_badge?boj=smw508" alt="solved.ac tier"/></a>
&nbsp;
<img src="https://komarev.com/ghpvc/?username=minu0508&color=30363D&style=flat-square&label=Profile+Views" alt="profile views"/>

</div>

<br/>


### <img src="assets/prompt.svg" height="22"/> About <sub>소개</sub>

I build AI services end to end: the model, the API around it, and the screen people use. I have been shipping software since July 2023, and most of my work sits where AI meets real business systems.

모델부터 API, 화면까지 AI 서비스를 끝까지 만드는 개발자입니다. 2023년 7월부터 개발을 시작했고, AI를 실제 업무 시스템에 녹여 내는 일을 주로 합니다.

<br/>

### <img src="assets/prompt.svg" height="22"/> What I Can Build <sub>만들 수 있는 것</sub>

<table>
  <tr>
    <td colspan="2" valign="top">
      <h4>LLM Applications &amp; RAG <sub>LLM 애플리케이션 &amp; RAG</sub></h4>
      <img src="https://skillicons.dev/icons?i=py,fastapi&theme=dark" height="40" alt="Python, FastAPI"/>
      <img src="assets/icons/langchain.svg" height="40" alt="LangChain"/>
      <img src="assets/icons/ollama.svg" height="40" alt="Ollama"/>
      <img src="assets/icons/huggingface.svg" height="40" alt="Hugging Face"/>
      <br/><sub>ChromaDB · Reranking · WebSocket</sub>
      <ul>
        <li>Document pipelines that parse PDF and Office files, chunk and embed them, and index them in a vector store<br/><sub>PDF·Office 문서를 파싱하고 잘게 나눠 임베딩한 뒤 벡터 저장소에 색인하는 문서 파이프라인</sub></li>
        <li>Answers grounded in sources, with reranking and citations back to the original file<br/><sub>재순위화를 거쳐 원본 파일 근거를 함께 보여 주는 답변</sub></li>
        <li>Permission-aware retrieval: data separated per tenant, access scoped by department and role<br/><sub>권한을 따르는 검색: 회사별로 데이터를 나누고, 부서와 역할에 맞게 접근을 제한</sub></li>
        <li>Local LLM serving with Ollama, so documents never leave the company network<br/><sub>Ollama로 LLM을 직접 서빙해 문서가 회사 네트워크 밖으로 나가지 않는 구조</sub></li>
        <li>Natural-language chat over a client's own database, kept inside token and time budgets<br/><sub>고객사 자체 DB에 자연어로 묻고 답하는 채팅(토큰·응답 시간 한도 안에서)</sub></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>Machine Learning <sub>머신러닝</sub></h4>
      <img src="https://skillicons.dev/icons?i=py,tensorflow,sklearn&theme=dark" height="40" alt="Python, TensorFlow, scikit-learn"/>
      <br/><sub>Keras · XGBoost · pandas · Flask</sub>
      <ul>
        <li>Anomaly detection on multivariate sensor time series, with regression and autoencoder models that must agree before an alarm<br/><sub>여러 센서의 시계열 데이터 이상탐지: 회귀 모델과 오토인코더가 함께 이상이라고 판단할 때만 알람</sub></li>
        <li>Time-series feature engineering (rolling, lag and diff windows) and per-sensor thresholds learned from training error<br/><sub>시계열 피처 엔지니어링(rolling·lag·diff 구간)과 학습 오차로 정하는 센서별 임계값</sub></li>
        <li>Training and serving pipelines for many small models behind a REST API<br/><sub>작은 모델 여러 개를 학습하고 REST API로 서빙하는 파이프라인</sub></li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h4>Computer Vision <sub>컴퓨터 비전</sub></h4>
      <img src="https://skillicons.dev/icons?i=pytorch,opencv&theme=dark" height="40" alt="PyTorch, OpenCV"/>
      <br/><sub>YOLO · timm</sub>
      <ul>
        <li>Object detection and instance segmentation for recognizing and counting items in photos<br/><sub>사진 속 물건을 알아보고 세는 객체 탐지·인스턴스 세그멘테이션</sub></li>
        <li>Image recognition models served behind REST APIs for web and mobile clients<br/><sub>웹·모바일에서 쓰는 이미지 인식 모델을 REST API로 서빙</sub></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>Full-stack Web &amp; App <sub>풀스택 웹 &amp; 앱</sub></h4>
      <img src="https://skillicons.dev/icons?i=nestjs,ts,react,flutter,docker,nginx&theme=dark" height="40" alt="NestJS, TypeScript, React, Flutter, Docker, Nginx"/>
      <br/><sub>TypeORM · Vite · PostgreSQL · MySQL · Redis</sub>
      <ul>
        <li>REST APIs with NestJS and TypeORM: auth, roles and permissions, organization trees, file handling, licensing<br/><sub>NestJS·TypeORM REST API: 인증, 역할·권한, 조직 트리, 파일 처리, 라이선스</sub></li>
        <li>Admin consoles and service web in React and TypeScript<br/><sub>React·TypeScript로 만드는 관리자 화면과 서비스 웹</sub></li>
        <li>Cross-platform mobile apps in Flutter<br/><sub>Flutter 크로스플랫폼 모바일 앱</sub></li>
        <li>Docker deployment behind Nginx, on PostgreSQL, MySQL and Redis<br/><sub>Nginx 뒤 Docker 배포, PostgreSQL·MySQL·Redis 운영</sub></li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h4>Quality &amp; Security <sub>품질 &amp; 보안</sub></h4>
      <img src="https://skillicons.dev/icons?i=jest,githubactions,linux&theme=dark" height="40" alt="Jest, GitHub Actions, Linux"/>
      <br/><sub>Playwright · pytest · Mutation testing</sub>
      <ul>
        <li>End-to-end test rounds on the real UI with Playwright, split into functional, security and UX passes<br/><sub>Playwright로 실제 화면을 도는 E2E 테스트 회차를 기능·보안·UX로 나눠 진행</sub></li>
        <li>Mutation testing to prove tests can fail, and an evidence file behind every verdict<br/><sub>테스트가 실제로 실패할 수 있는지 뮤테이션 테스트로 확인하고, 판정마다 증거 파일을 남김</sub></li>
        <li>Security designed in from the start: access control, secret handling, keeping data in-house<br/><sub>설계 단계부터 넣는 보안: 접근 제어, 비밀값 관리, 데이터를 사내에 두기</sub></li>
      </ul>
    </td>
  </tr>
</table>

<br/>

<br/>

### <img src="assets/prompt.svg" height="22"/> Stack <sub>기술 스택</sub>

<table>
  <tr>
    <td width="130"><b>AI / ML</b></td>
    <td><img src="assets/stack/ai-ml.svg" alt="Python, PyTorch, TensorFlow, scikit-learn, OpenCV"/></td>
  </tr>
  <tr>
    <td width="130"><b>LLM</b></td>
    <td><img src="assets/stack/llm.svg" alt="LangChain, Ollama, Hugging Face, OpenAI, Anthropic, Claude Code"/></td>
  </tr>
  <tr>
    <td width="130"><b>Backend</b></td>
    <td><img src="assets/stack/backend.svg" alt="NestJS, Node.js, FastAPI, Flask, Django, Java, Spring Boot"/></td>
  </tr>
  <tr>
    <td width="130"><b>Database</b></td>
    <td><img src="assets/stack/database.svg" alt="PostgreSQL, MySQL, Redis"/></td>
  </tr>
  <tr>
    <td width="130"><b>Frontend</b></td>
    <td><img src="assets/stack/frontend.svg" alt="TypeScript, React, Next.js, Vite, JavaScript"/></td>
  </tr>
  <tr>
    <td width="130"><b>Mobile</b></td>
    <td><img src="assets/stack/mobile.svg" alt="Flutter, Dart"/></td>
  </tr>
  <tr>
    <td width="130"><b>Infra / Tools</b></td>
    <td><img src="assets/stack/infra.svg" alt="AWS, Docker, Nginx, Linux, Git, GitHub Actions, Obsidian, VS Code"/></td>
  </tr>
</table>

<br/>

### <img src="assets/prompt.svg" height="22"/> Activity <sub>활동</sub>

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/minu0508/minu0508/output/github-snake-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/minu0508/minu0508/output/github-snake.svg"/>
  <img src="https://raw.githubusercontent.com/minu0508/minu0508/output/github-snake-dark.svg" width="100%" alt="contribution snake"/>
</picture>

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=minu0508&amp;hide_border=true&amp;background=0D1117&amp;ring=39D353&amp;fire=39D353&amp;currStreakLabel=39D353&amp;sideLabels=C9D1D9&amp;currStreakNum=C9D1D9&amp;sideNums=C9D1D9&amp;dates=8B949E&amp;stroke=21262D"/>
  <source media="(prefers-color-scheme: light)" srcset="https://streak-stats.demolab.com?user=minu0508&amp;hide_border=true&amp;background=FFFFFF&amp;ring=1A7F37&amp;fire=1A7F37&amp;currStreakLabel=1A7F37&amp;sideLabels=57606A&amp;currStreakNum=24292F&amp;sideNums=24292F&amp;dates=6E7781&amp;stroke=D0D7DE"/>
  <img src="https://streak-stats.demolab.com?user=minu0508&amp;hide_border=true&amp;background=0D1117&amp;ring=39D353&amp;fire=39D353&amp;currStreakLabel=39D353&amp;sideLabels=C9D1D9&amp;currStreakNum=C9D1D9&amp;sideNums=C9D1D9&amp;dates=8B949E&amp;stroke=21262D" width="62%" alt="streak"/>
</picture>

</div>

<br/>

<div align="center">

<a href="https://github.com/minu0508"><img src="https://img.shields.io/badge/GitHub-0D1117?style=for-the-badge&logo=github&logoColor=white"/></a>
<a href="mailto:devsormoo@gmail.com"><img src="https://img.shields.io/badge/Email-0D1117?style=for-the-badge&logo=gmail&logoColor=EA4335"/></a>
<a href="https://instagram.com/mxxnw_s"><img src="https://img.shields.io/badge/Instagram-0D1117?style=for-the-badge&logo=instagram&logoColor=E4405F"/></a>

<img src="assets/wave.svg" width="100%" alt=""/>

</div>
