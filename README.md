<div align="center">

<img src="assets/terminal.svg" width="100%" alt="SON MIN WOO · AI Engineer | Software Developer · since 2023.07"/>

<br/>

<img src="https://img.shields.io/badge/Experience-3%2B%20years%20%C2%B7%20since%202023.07-39D353?style=flat-square&labelColor=0D1117" align="middle" alt="Experience: 3+ years, since 2023.07"/>
&nbsp;&nbsp;
<a href="https://solved.ac/smw508/"><img src="http://mazassumnida.wtf/api/mini/generate_badge?boj=smw508" height="38" align="middle"/></a>
&nbsp;&nbsp;
<img src="https://komarev.com/ghpvc/?username=minu0508&color=39D353&style=flat-square&label=Profile+Views" align="middle" alt="profile views"/>

</div>

<br/>

```python
class MinWoo:
    role    = ["AI Engineer", "Software Developer"]
    since   = "2023.07"
    years   = "3+"  # updated by GitHub Actions
    focus   = ["LLM Application", "RAG", "Agent System",
               "Time-series ML", "Computer Vision", "Full-stack"]
    stack   = ["Python", "TypeScript", "NestJS", "React", "Flutter", "Docker"]
    motto   = "Slow is fine. Quitting isn't. Keep growing."
```

### <img src="assets/prompt.svg" height="22"/> About

I build AI services end to end: the model, the API around it, and the screen people use. I have been shipping software since July 2023, and most of my work sits where AI meets real business systems.

모델부터 API, 화면까지 AI 서비스를 끝까지 만드는 개발자입니다. 2023년 7월부터 개발을 시작했고, AI를 실제 업무 시스템에 녹여 내는 일을 주로 합니다.

<br/>

### <img src="assets/prompt.svg" height="22"/> What I Can Build

<table>
  <tr>
    <td colspan="2" valign="top">
      <h4>LLM Applications &amp; RAG</h4>
      <img src="https://skillicons.dev/icons?i=py,fastapi&theme=dark" height="40" alt="Python, FastAPI"/>
      <img src="assets/icons/langchain.svg" height="40" alt="LangChain"/>
      <img src="assets/icons/ollama.svg" height="40" alt="Ollama"/>
      <img src="assets/icons/huggingface.svg" height="40" alt="Hugging Face"/>
      <br/><sub>ChromaDB · Reranking · WebSocket</sub>
      <ul>
        <li>Document pipelines that parse PDF and Office files, chunk and embed them, and index them in a vector store</li>
        <li>Answers grounded in sources, with reranking and citations back to the original file</li>
        <li>Permission-aware retrieval: data separated per tenant, access scoped by department and role</li>
        <li>Local LLM serving with Ollama, so documents never leave the company network</li>
        <li>Natural-language chat over a client's own database, kept inside token and time budgets</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>Machine Learning</h4>
      <img src="https://skillicons.dev/icons?i=py,tensorflow,sklearn&theme=dark" height="40" alt="Python, TensorFlow, scikit-learn"/>
      <br/><sub>Keras · XGBoost · pandas · Flask</sub>
      <ul>
        <li>Anomaly detection on multivariate sensor time series, with regression and autoencoder models that must agree before an alarm</li>
        <li>Time-series feature engineering (rolling, lag and diff windows) and per-sensor thresholds learned from training error</li>
        <li>Training and serving pipelines for many small models behind a REST API</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h4>Computer Vision</h4>
      <img src="https://skillicons.dev/icons?i=pytorch,opencv&theme=dark" height="40" alt="PyTorch, OpenCV"/>
      <br/><sub>YOLO · timm</sub>
      <ul>
        <li>Object detection and instance segmentation for recognizing and counting items in photos</li>
        <li>Image recognition models served behind REST APIs for web and mobile clients</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>Full-stack Web &amp; App</h4>
      <img src="https://skillicons.dev/icons?i=nestjs,ts,react,flutter,docker,nginx&theme=dark" height="40" alt="NestJS, TypeScript, React, Flutter, Docker, Nginx"/>
      <br/><sub>TypeORM · Vite · PostgreSQL · MySQL · Redis</sub>
      <ul>
        <li>REST APIs with NestJS and TypeORM: auth, roles and permissions, organization trees, file handling, licensing</li>
        <li>Admin consoles and service web in React and TypeScript</li>
        <li>Cross-platform mobile apps in Flutter</li>
        <li>Docker deployment behind Nginx, on PostgreSQL, MySQL and Redis</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h4>Quality &amp; Security</h4>
      <img src="https://skillicons.dev/icons?i=jest,githubactions,linux&theme=dark" height="40" alt="Jest, GitHub Actions, Linux"/>
      <br/><sub>Playwright · pytest · Mutation testing</sub>
      <ul>
        <li>End-to-end test rounds on the real UI with Playwright, split into functional, security and UX passes</li>
        <li>Mutation testing to prove tests can fail, and an evidence file behind every verdict</li>
        <li>Security designed in from the start: access control, secret handling, keeping data in-house</li>
      </ul>
    </td>
  </tr>
</table>

<br/>

### <img src="assets/prompt.svg" height="22"/> How I Build

- **Agents as teammates.** Claude Code and Codex work as a pair: one plans and implements, the other reviews the plan and the diff.
- **Design factory.** A 10-stage agent pipeline that turns one sentence into a brief, an ERD with executable DDL, screen flows, an API spec, UI components and a scaffolded repo. Each stage is planned, reviewed, run and verified.
- **LLM Wiki.** A personal knowledge base in Obsidian that an LLM maintains: 100+ linked pages on AI tooling, with claims checked against primary sources.
- **Second brain for code.** Coding sessions are collected into the vault, summarized and indexed with gbrain, so past decisions, and who made them, stay searchable.

<details>
<summary><b>See the design factory pipeline</b></summary>
<br/>

```mermaid
%%{init: {"theme": "base", "themeVariables": {"background": "transparent", "primaryColor": "#161B22", "primaryTextColor": "#C9D1D9", "primaryBorderColor": "#39D353", "lineColor": "#39D353", "clusterBkg": "transparent", "clusterBorder": "#30363D", "titleColor": "#8B949E", "fontFamily": "monospace", "fontSize": "15px"}}}%%
flowchart TB
    subgraph design ["design"]
        direction LR
        A([One-line idea]) --> B[Brief] --> C[Interview] --> D[ERD + DDL]
    end
    subgraph build ["build"]
        direction LR
        E[Screen flows] --> F[API spec] --> G[UI] --> H{Verify} --> I[(Repo)]
    end
    design --> build
```

<sub>Every stage runs plan → review → execute → verify before the next one starts.</sub>

</details>

<br/>

### <img src="assets/prompt.svg" height="22"/> Stack

<table>
  <tr>
    <td width="130"><b>AI / ML</b></td>
    <td><img src="https://skillicons.dev/icons?i=py,pytorch,tensorflow,sklearn,opencv&theme=dark" height="40" alt="Python, PyTorch, TensorFlow, scikit-learn, OpenCV"/></td>
  </tr>
  <tr>
    <td width="130"><b>LLM</b></td>
    <td><img src="assets/icons/langchain.svg" height="40" alt="LangChain"/> <img src="assets/icons/ollama.svg" height="40" alt="Ollama"/> <img src="assets/icons/huggingface.svg" height="40" alt="Hugging Face"/> <img src="assets/icons/openai.svg" height="40" alt="OpenAI"/> <img src="assets/icons/anthropic.svg" height="40" alt="Anthropic"/> <img src="assets/icons/claude.svg" height="40" alt="Claude Code"/></td>
  </tr>
  <tr>
    <td width="130"><b>Backend</b></td>
    <td><img src="https://skillicons.dev/icons?i=nestjs,nodejs,fastapi,flask,django,java,spring&theme=dark" height="40" alt="NestJS, Node.js, FastAPI, Flask, Django, Java, Spring Boot"/></td>
  </tr>
  <tr>
    <td width="130"><b>Database</b></td>
    <td><img src="https://skillicons.dev/icons?i=postgres,mysql,redis&theme=dark" height="40" alt="PostgreSQL, MySQL, Redis"/></td>
  </tr>
  <tr>
    <td width="130"><b>Frontend</b></td>
    <td><img src="https://skillicons.dev/icons?i=ts,react,nextjs,vite,js&theme=dark" height="40" alt="TypeScript, React, Next.js, Vite, JavaScript"/></td>
  </tr>
  <tr>
    <td width="130"><b>Mobile</b></td>
    <td><img src="https://skillicons.dev/icons?i=flutter,dart&theme=dark" height="40" alt="Flutter, Dart"/></td>
  </tr>
  <tr>
    <td width="130"><b>Infra / Tools</b></td>
    <td><img src="https://skillicons.dev/icons?i=aws,docker,nginx,linux,git,githubactions,obsidian,vscode&theme=dark" height="40" alt="AWS, Docker, Nginx, Linux, Git, GitHub Actions, Obsidian, VS Code"/></td>
  </tr>
</table>

<br/>

### <img src="assets/prompt.svg" height="22"/> Activity

<div align="center">

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
