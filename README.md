# Wine RAG Embedding 실습 가이드 🍷

## 📖 개요

AI 소믈리에 서비스를 위한 와인 RAG(Retrieval-Augmented Generation) 시스템 구축 실습입니다. 
와인 이미지와 텍스트를 분석하여 개인화된 와인 추천과 페어링을 제공하는 시스템을 만들어봅시다.

## 🎯 학습 목표

1. **멀티모달 AI 이해**: 이미지와 텍스트를 함께 처리하는 AI 시스템 구축
2. **벡터 임베딩**: 와인 데이터를 벡터로 변환하여 유사도 검색 구현
3. **RAG 시스템**: Pinecone을 활용한 효율적인 정보 검색 및 생성
4. **LangChain 활용**: 프롬프트 엔지니어링과 체인 구성

## 🏗️ 시스템 아키텍처

```
[와인 이미지] → [Gemini Vision] → [텍스트 분석] → [임베딩] → [Pinecone DB]
                                                           ↓
[사용자 질의] → [임베딩] → [유사도 검색] → [RAG 생성] → [개인화 추천]
```

## 📊 데이터 구조

### Pinecone 벡터 DB 현황
- **총 벡터 수**: 390,273개
- **차원**: 1536 (OpenAI embedding)
- **네임스페이스**:
  - `wine-reviews-ns1`: 259,942개 (와인 리뷰 데이터)
  - `wine_description_only`: 130,331개 (와인 설명 데이터)

## 🔧 핵심 구성 요소

### 1. AI 소믈리에 페르소나
```
전문 소믈리에로서 와인 선정, 음식 페어링, 와인 서비스에 대한 깊은 지식을 보유
- 다양한 와인 지역과 포도 품종에 대한 이해
- 미묘한 풍미와 특성을 구분하는 정교한 미각
- 사용자 맞춤형 추천 제공
```

### 2. 주요 기능들

#### A. 와인 이미지 기반 요리 추천 (`recommend_dishes_chain`)
- **입력**: 와인 이미지 + 질의 텍스트
- **출력**: 해당 와인과 어울리는 요리 추천
- **활용**: LangChain 프롬프트 템플릿

#### B. 요리 이미지 기반 풍미 분석 (`describe_dish_flavor_chain`)
- **입력**: 요리 이미지
- **출력**: 요리의 풍미 프로필 분석
- **특징**: 맛, 질감, 향 등 종합적 분석

### 3. 기술 스택
- **LLM**: Gemini API (멀티모달 지원)
- **벡터 DB**: Pinecone
- **프레임워크**: LangChain
- **임베딩**: OpenAI text-embedding-ada-002
- **언어**: Python + Jupyter Notebook

## 🔑 핵심 개념

### 멀티모달 AI (LMM)
- **LLM**: text → model → text
- **LMM**: image → model → text
- Gemini와 같은 옴니 모델은 LLM과 LMM을 모두 지원

### RAG 시스템의 장점
1. **실시간 정보**: 최신 와인 데이터 반영
2. **정확성**: 벡터 검색을 통한 관련성 높은 정보 제공
3. **개인화**: 사용자 선호도 기반 맞춤 추천
4. **확장성**: 새로운 와인 데이터 쉽게 추가

## 📝 실습 과정

### 1단계: 환경 설정
- Gemini API 키 설정
- Pinecone 연결 확인
- 필요 라이브러리 설치

### 2단계: 데이터 탐색
- Pinecone 인덱스 상태 확인
- 와인 데이터 구조 분석

### 3단계: 체인 구성
- 프롬프트 템플릿 설계
- LangChain 체인 구축
- 멀티모달 입력 처리

### 4단계: 테스트 및 최적화
- 다양한 와인 이미지로 테스트
- 응답 품질 평가 및 개선

## 🎨 예시 시나리오

### 시나리오 1: 와인 → 요리 추천
```
입력: Primitivo 와인 이미지
출력: 
- 그릴드 스테이크
- 바비큐 립
- 라자냐
- 양고기 요리
- 숙성 치즈 플래터
```

### 시나리오 2: 요리 → 풍미 분석
```
입력: 그래놀라 바 이미지
출력: "견과류와 귀리가 들어간 그래놀라 바로, 고소하고 달콤한 맛이 특징입니다."
```

## 🔍 실습 포인트

1. **프롬프트 엔지니어링**: 소믈리에 페르소나를 잘 표현하는 프롬프트 작성
2. **이미지 처리**: 멀티모달 입력을 위한 적절한 이미지 URL 포맷
3. **체인 최적화**: LangChain을 활용한 효율적인 처리 파이프라인
4. **벡터 검색**: Pinecone을 통한 관련 와인 정보 검색

## 💡 확장 아이디어

1. **개인화 강화**: 사용자 히스토리 기반 추천
2. **실시간 재고**: 와인샵 재고와 연동
3. **소셜 기능**: 와인 리뷰 및 평점 시스템
4. **AR 통합**: 와인 라벨 스캔 기능

## 📚 참고 자료

- [LangChain 공식 문서](https://python.langchain.com/)
- [Pinecone 벡터 DB 가이드](https://www.pinecone.io/learn/)
- [Gemini API 문서](https://ai.google.dev/tutorials)
- 와인 소믈리에 전문 지식 베이스

---

*"와인은 단순한 음료가 아니라, 문화와 예술이 담긴 경험입니다. AI와 함께 그 깊이를 탐험해보세요!"*

---

# LLM_RAG-Ollama

18주차 LLM, RAG, Ollama 관련 학습 내용을 정리한 저장소입니다.

## 📚 학습 내용 개요

이 저장소는 LLM(Large Language Model), RAG(Retrieval-Augmented Generation), 그리고 Ollama를 활용한 다양한 실습과 프로젝트를 포함합니다.

## 📁 파일 구조 및 내용

### 🔧 메인 애플리케이션 파일

#### `app.py`

- **Streamlit 기반 투자 보고서 생성 서비스**
- 회사명 검색을 통한 주식 정보 조회
- Meilisearch를 활용한 종목 검색
- yfinance를 통한 실시간 주가 정보 수집
- LangChain을 활용한 투자 보고서 자동 생성

#### `search.py`

- **Meilisearch 클라이언트 설정**
- NASDAQ 종목 데이터 검색 기능
- 주식 심볼 기반 검색 API

#### `stock_info.py`

- **yfinance를 활용한 주식 정보 수집 클래스**
- 기본 정보 (회사명, 산업, 부문, 시가총액 등)
- 재무제표 (손익계산서, 대차대조표, 현금흐름표)
- 분기별 재무 데이터 제공

#### `report_service.py`

- **LangChain을 활용한 투자 보고서 생성 서비스**
- ChatPromptTemplate을 통한 구조화된 프롬프트 관리
- 주식 기본정보와 재무제표를 기반으로 한 투자 분석 보고서 생성
- 마크다운 형식의 한글 보고서 출력

### 📓 Jupyter 노트북 학습 자료

#### `01_hello_openai.ipynb`

- **OpenAI API 기본 사용법**
- 환경 변수 설정 및 API 키 관리
- Chat Completions API 활용
- JSON 형식 응답 처리
- CoT(Chain of Thought) 프롬프트 기법
- Self-consistency 기법
- Reflexion(자기 피드백) 프롬프트 설계

#### `02_prompt.ipynb`

- **프롬프트 엔지니어링 기법**
- 출력 형식 지정 (JSON 객체)
- CoT 프롬프트를 통한 단계별 사고 과정
- Self-consistency를 통한 다중 응답 검증
- Reflexion 기법을 활용한 반복적 개선

#### `03_langchain_test.ipynb`

- **LangChain 기본 사용법**
- ChatOpenAI 모델 초기화
- invoke(), batch(), stream() 메서드 활용
- 비동기 처리 (async/await)
- 병렬 처리 성능 비교

#### `04_search_engine_setting.ipynb`

- **Meilisearch 검색 엔진 설정**
- NASDAQ 주식 데이터 CSV 로드
- 검색 인덱스 생성 및 데이터 삽입
- 주식 심볼 기반 검색 기능 구현

#### `05_stock_info_test.ipynb`

- **yfinance를 활용한 주식 정보 수집**
- Microsoft(MSFT) 주식 정보 예제
- 기본 정보 추출 (회사명, 산업, 부문, 시가총액 등)
- 재무제표 데이터 수집 및 분석

#### `06_langchain_caching.ipynb`

- **LangChain 캐싱 시스템**
- InMemoryCache를 통한 메모리 캐싱
- Redis를 활용한 분산 캐싱
- 캐시 성능 최적화

#### `07_prompt template.ipynb`

- **프롬프트 템플릿 관리**
- PromptTemplate을 통한 템플릿 생성
- 템플릿 저장 및 로드 (JSON 형식)
- ChatPromptTemplate을 활용한 대화형 프롬프트
- 프롬프트 연결 및 조합

#### `08_outputparser.ipynb`

- **출력 파서 활용**
- JsonOutputParser를 통한 구조화된 출력
- Pydantic 모델을 활용한 데이터 검증
- 이메일 정보 추출 예제

#### `09_chain_LCEL.ipynb`

- **LangChain Expression Language (LCEL)**
- 파이프라인 구성을 통한 체인 생성
- SequentialChain을 활용한 순차 처리
- 체인 연결 및 실행

#### `11_LLM환경설정.ipynb`

- **다양한 LLM 환경 설정**
- OpenAI API 설정
- Upstage Solar Pro 2 모델 활용
- Ollama Gemma2 모델 로컬 실행

#### `12_임베딩비교.ipynb`

- **다양한 임베딩 모델 비교 분석**
- OpenAI Embeddings (text-embedding-3-small) vs Upstage Solar Embeddings
- 코사인 유사도를 통한 벡터 성능 비교
- 다국어 임베딩 성능 평가 (영어-한국어 간 유사도 측정)
- Sentence Transformers 활용 (multilingual MiniLM 모델)
- GPU 기반 허깅페이스 임베딩 모델 실습

#### `13_허깅페이스의활용.ipynb`

- **Hugging Face Transformers 활용**
- 다양한 NLP 태스크 (감성분석, 분류, 번역, 요약 등)
- Pipeline을 통한 간편한 모델 사용
- AutoTokenizer, AutoModel 활용
- 모델 파인튜닝 및 저장/로드

#### `13_벡터DB_test.ipynb`

- **Pinecone 벡터 데이터베이스 활용 실습**
- AWS Serverless 환경에서 벡터 인덱스 생성 및 관리
- 3차원 벡터 데이터 저장 및 검색 (영화 장르 분류 예제)
- 메타데이터 필터링을 통한 장르별 검색 기능
- 코사인 유사도 기반 유사 벡터 검색 및 랭킹
- Namespace를 통한 데이터 분리 관리
- 벡터 데이터 업서트(upsert) 및 인덱스 통계 조회
- Fetch API를 활용한 벡터 데이터 조회
- Matplotlib을 활용한 3D 벡터 공간 시각화
- 임베딩 미션: 한국어 텍스트 데이터의 벡터화 및 유사도 검색

#### `13_1_벡터DB_trial.ipynb`

- **한국어 텍스트 벡터화 실습**
- Gemini API를 활용한 한국어 임베딩 생성
- Pinecone 벡터 데이터베이스에 한국어 텍스트 저장
- 의미적 유사도 기반 검색 및 랭킹
- 실제 한국어 문장 데이터를 활용한 RAG 시스템 구현

#### `13_Gemini_embedding_mission.ipynb` & `13_Gemini_embedding_mission.py`

- **Google Gemini 임베딩 API 활용**
- text-embedding-004 모델을 통한 고품질 임베딩 생성
- 한국어 텍스트의 의미적 유사도 측정
- 사과(과일) vs 애플(기업) 구분을 통한 임베딩 품질 검증
- 코사인 유사도 기반 벡터 검색 및 분석

#### `14_위키인덱스.ipynb`

- **Wikipedia 한국어 데이터셋 다운로드 및 벡터 인덱싱**
- Hugging Face Datasets를 활용한 대규모 한국어 텍스트 데이터 수집
- 2023년 11월 기준 한국어 Wikipedia 전체 데이터셋
- OpenAI 임베딩을 활용한 텍스트 벡터화
- Pinecone 벡터 데이터베이스에 한국어 문서 인덱싱
- 의미적 유사도 기반 검색 및 RAG 시스템 구축
- 샘플 데이터 추출 및 로컬 저장 (CSV, JSON)
- 특정 주제별 문서 필터링 및 검색 기능

### 🍷 AI 소믈리에 & 와인 RAG 시스템

#### `21_와인이미지_질의.ipynb`

- **멀티모달 와인 분석 시스템**
- OpenAI GPT-4o-mini를 활용한 와인 이미지 분석
- AI 소믈리에 페르소나 프롬프트 설계
- 와인 이미지 기반 요리 추천 기능
- 이미지 URL과 텍스트 질의를 결합한 멀티모달 처리

#### `22_와인이미지_랭체인프롬프트.ipynb`

- **LangChain을 활용한 와인 추천 체인**
- ChatPromptTemplate을 통한 구조화된 프롬프트 관리
- `recommend_dishes_chain`: 와인 → 요리 추천 체인
- `describe_dish_flavor_chain`: 요리 → 풍미 분석 체인
- RunnableLambda를 활용한 체인 실행 및 최적화
- 시스템/휴먼 메시지 구조화 및 이미지 URL 처리

#### `23_와인매거진_임베딩벡터구성.ipynb`

- **Pinecone 와인 벡터 데이터베이스 활용**
- 총 390,273개 와인 관련 벡터 데이터 관리
- 네임스페이스별 데이터 분리 (`wine-reviews-ns1`, `wine_description_only`)
- 1536차원 OpenAI 임베딩 기반 코사인 유사도 검색
- 와인 리뷰 및 설명 데이터를 활용한 RAG 시스템 구축

### 📄 설정 및 데이터 파일

#### `restaurant_tour_prompt.json`

- **프롬프트 템플릿 저장 파일**
- 레스토랑 투어 관련 프롬프트 템플릿
- JSON 형식으로 저장된 템플릿 메타데이터

#### `nasdaq_screener_1755789601709.csv`

- **NASDAQ 주식 데이터**
- 7,008개 종목의 기본 정보
- 심볼, 회사명, 가격, 시가총액, 부문, 산업 등 포함

## 🚀 주요 기능

1. **투자 보고서 자동 생성**: 주식 정보를 기반으로 한 AI 투자 분석 보고서
2. **실시간 주가 정보 수집**: yfinance를 통한 최신 주식 데이터
3. **검색 엔진 통합**: Meilisearch를 활용한 빠른 종목 검색
4. **벡터 데이터베이스**: Pinecone을 활용한 고차원 벡터 검색
5. **다양한 LLM 모델 지원**: OpenAI, Upstage, Ollama 등
6. **프롬프트 엔지니어링**: 다양한 프롬프트 기법 실습
7. **RAG 시스템 구현**: 검색과 생성의 결합
8. **🍷 AI 소믈리에 시스템**: 멀티모달 와인 분석 및 개인화 추천
9. **와인 이미지 분석**: 와인 라벨 인식 및 특성 분석
10. **음식 페어링 추천**: 와인과 어울리는 요리 자동 추천

## 🛠️ 기술 스택

- **Python 3.x**
- **Streamlit**: 웹 애플리케이션 프레임워크
- **LangChain**: LLM 애플리케이션 개발 프레임워크
- **OpenAI API**: GPT 모델 활용
- **Google Gemini**: 임베딩 및 생성 모델
- **Upstage Solar Pro 2**: 한국형 대규모 언어 모델
- **Ollama**: 로컬 LLM 실행 환경
- **yfinance**: 주식 데이터 수집
- **Meilisearch**: 검색 엔진
- **Pinecone**: 벡터 데이터베이스
- **Hugging Face Transformers**: 다양한 NLP 모델
- **Redis**: 캐싱 시스템

## 📋 설치 및 실행

1. 필요한 패키지 설치:

```bash
pip install streamlit langchain openai yfinance meilisearch redis sentence-transformers
pip install langchain-upstage langchain-ollama pinecone-client google-generativeai
```

2. Ollama 설치 및 모델 다운로드:

```bash
# Ollama 설치 (Windows)
# https://ollama.ai/download 에서 다운로드

# 모델 다운로드
ollama pull gemma2
ollama pull llama2
ollama pull mistral
```

3. 환경 변수 설정 (.env 파일):

```
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
UPSTAGE_API_KEY=your_upstage_api_key
HF_TOKEN=your_huggingface_token
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=your_pinecone_index_name
```

4. Streamlit 앱 실행:

```bash
streamlit run app.py
```

## 🤖 지원 LLM 모델

### OpenAI GPT

- **모델**: GPT-4o-mini
- **특징**: 빠른 응답 속도, 높은 정확도
- **용도**: 일반적인 텍스트 생성, 대화형 AI

### Upstage Solar Pro 2

- **모델**: Solar Pro 2 (30.9B 파라미터)
- **특징**: 한국어 최적화, 높은 추론 능력
- **용도**: 한국어 텍스트 생성, 복잡한 추론 작업
- **장점**: 한국어 이해도가 뛰어나고 비용 효율적

### Ollama (로컬 실행)

- **지원 모델**: Gemma2, Llama2, Mistral 등
- **특징**: 로컬 실행, 개인정보 보호, 오프라인 사용 가능
- **용도**: 프라이버시가 중요한 작업, 로컬 개발 환경
- **장점**: API 비용 없음, 완전한 데이터 제어

### Hugging Face Transformers

- **다양한 모델**: BERT, DistilBERT, T5 등
- **특징**: 특화된 태스크용 모델
- **용도**: 감성분석, 번역, 요약, 분류 등

## 📊 모델 비교

| 모델                | 언어 지원     | 실행 환경     | 비용      | 특징                   |
| ------------------- | ------------- | ------------- | --------- | ---------------------- |
| OpenAI GPT-4o-mini  | 다국어        | 클라우드      | 유료      | 빠른 응답, 높은 정확도 |
| Upstage Solar Pro 2 | 한국어 최적화 | 클라우드      | 유료      | 한국어 특화, 추론 능력 |
| Ollama Gemma2       | 다국어        | 로컬          | 무료      | 오프라인, 프라이버시   |
| Hugging Face        | 다국어        | 로컬/클라우드 | 무료/유료 | 특화 태스크            |

## 📖 학습 목표

- LLM의 기본 개념과 활용법 이해
- RAG 시스템의 구현과 최적화
- 프롬프트 엔지니어링 기법 습득
- 다양한 LLM 모델의 비교 분석
- 로컬 LLM과 클라우드 LLM의 장단점 이해
- 실무에서 활용 가능한 AI 애플리케이션 개발
- **멀티모달 AI 시스템 구축** (이미지 + 텍스트 처리)
- **벡터 임베딩과 유사도 검색** 시스템 이해
- **AI 소믈리에 서비스** 실습을 통한 실전 경험

## 🍷 Wine RAG 실습 가이드

상세한 와인 RAG 시스템 구축 가이드는 [WineRAG_Guide.md](./WineRAG_Guide.md)를 참고하세요.

### 핵심 학습 포인트
- **멀티모달 AI**: 와인 이미지와 텍스트를 함께 처리
- **Pinecone 벡터 DB**: 390,273개 와인 데이터 벡터 검색
- **LangChain 체인**: 구조화된 프롬프트 및 워크플로우 관리
- **AI 페르소나**: 전문 소믈리에 역할 구현
