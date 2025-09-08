# 18week-LLM_RAG-Ollama

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

- **임베딩 모델 비교 분석**
- OpenAI Embeddings vs Upstage Embeddings
- 코사인 유사도를 통한 벡터 비교
- 다국어 임베딩 성능 평가
- Sentence Transformers 활용

#### `13_허깅페이스의활용.ipynb`

- **Hugging Face Transformers 활용**
- 다양한 NLP 태스크 (감성분석, 분류, 번역, 요약 등)
- Pipeline을 통한 간편한 모델 사용
- AutoTokenizer, AutoModel 활용
- 모델 파인튜닝 및 저장/로드

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
4. **다양한 LLM 모델 지원**: OpenAI, Upstage, Ollama 등
5. **프롬프트 엔지니어링**: 다양한 프롬프트 기법 실습
6. **RAG 시스템 구현**: 검색과 생성의 결합

## 🛠️ 기술 스택

- **Python 3.x**
- **Streamlit**: 웹 애플리케이션 프레임워크
- **LangChain**: LLM 애플리케이션 개발 프레임워크
- **OpenAI API**: GPT 모델 활용
- **Upstage Solar Pro 2**: 한국형 대규모 언어 모델
- **Ollama**: 로컬 LLM 실행 환경
- **yfinance**: 주식 데이터 수집
- **Meilisearch**: 검색 엔진
- **Hugging Face Transformers**: 다양한 NLP 모델
- **Redis**: 캐싱 시스템

## 📋 설치 및 실행

1. 필요한 패키지 설치:

```bash
pip install streamlit langchain openai yfinance meilisearch redis sentence-transformers
pip install langchain-upstage langchain-ollama
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
UPSTAGE_API_KEY=your_upstage_api_key
HF_TOKEN=your_huggingface_token
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

| 모델 | 언어 지원 | 실행 환경 | 비용 | 특징 |
|------|-----------|-----------|------|------|
| OpenAI GPT-4o-mini | 다국어 | 클라우드 | 유료 | 빠른 응답, 높은 정확도 |
| Upstage Solar Pro 2 | 한국어 최적화 | 클라우드 | 유료 | 한국어 특화, 추론 능력 |
| Ollama Gemma2 | 다국어 | 로컬 | 무료 | 오프라인, 프라이버시 |
| Hugging Face | 다국어 | 로컬/클라우드 | 무료/유료 | 특화 태스크 |

## 📖 학습 목표

- LLM의 기본 개념과 활용법 이해
- RAG 시스템의 구현과 최적화
- 프롬프트 엔지니어링 기법 습득
- 다양한 LLM 모델의 비교 분석
- 로컬 LLM과 클라우드 LLM의 장단점 이해
- 실무에서 활용 가능한 AI 애플리케이션 개발
