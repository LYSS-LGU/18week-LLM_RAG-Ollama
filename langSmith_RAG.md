# LangSmith와 RAG 시스템 구축 가이드

## 📋 개요

이 문서는 2025년 9월 10일 교육자료를 바탕으로 LangSmith 모니터링, 검색효율 개선, 소득세법 RAG 구축에 대한 핵심 내용을 정리한 것입니다.

---

## 1. LangSmith 모니터링 및 평가 🔍

### 1.1 LangSmith 플랫폼 소개

- **개발사**: LangChain에서 개발한 LLM 애플리케이션 전용 플랫폼
- **주요 기능**: 테스트, 모니터링, 디버깅, LangChain Hub 포함
- **특징**: 원래 LangChain 일부였으나 독립된 플랫폼으로 분리

### 1.2 요금 체계 💰

| 플랜       | 월 요금 | Traces 한도    |
| ---------- | ------- | -------------- |
| 무료       | $0      | 5,000 traces   |
| Plus       | $39     | 50,000 traces  |
| Pro        | $199    | 500,000 traces |
| Enterprise | 커스텀  | 무제한         |

### 1.3 RAG 시스템 평가 방법론 📊

#### 데이터셋 구성

- **주제**: 소득세법 관련 질문-답변
- **규모**: 20개 데이터셋
- **목적**: 도메인 특화 RAG 성능 측정

#### 핵심 평가 지표 3가지

1. **answer_evaluator**: 기준 답변과의 정확성 비교
2. **answer_helpfulness_evaluator**: 답변의 유용성 평가
3. **answer_hallucination_evaluator**: 환각(거짓 정보) 여부 검사

#### 실제 구현 코드

```python
# RagBot 클래스 - @traceable() 데코레이터로 추적 가능
class RagBot:
    def __init__(self, retriever, model="gpt-4o"):
        self._client = wrap_openai(openai.Client())  # LangSmith 래핑

# 평가 실행
experiment_results = evaluate(
    predict_rag_answer_with_context,
    data="income_tax_dataset",
    evaluators=[
        answer_evaluator,
        answer_helpfulness_evaluator,
        answer_hallucination_evaluator
    ],
    experiment_prefix="tax-evaluator-hallucination"
)
```

---

## 2. 검색 효율 개선을 위한 데이터 전처리 🎯

### 2.1 핵심 문제점

- **현상**: 이미지로 된 표(예: 세법 제55조 누진세율표)가 검색되지 않음
- **원인**: GPT가 이미지 테이블을 텍스트로 인식하지 못함
- **영향**: 구체적인 세율 계산 질문에 정확한 답변 불가

### 2.2 해결 전략 📈

#### 표 형식 변환 프로세스

1. **이미지 표** → **Word 표** → **마크다운 표**
2. **이유**: GPT가 마크다운 형식의 표를 더 잘 인식하고 처리

#### 쿼리 정규화 기법

```python
def normalize_query(q: str) -> str:
    # 숫자 표기 통일
    q = q.replace("5천만원","5,000만원")

    # 용어 정규화
    q = q.replace("연봉", "과세표준")

    # 계산 컨텍스트 추가 (핵심!)
    if "계산" not in q:
        q = q + " 계산 기준과 누진공제를 적용해 계산"

    return q
```

#### 키워드 사전 활용

```python
# 용어 매핑 사전
dictionary = ["사람을 나타내는 표현 -> 거주자"]

# LCEL 파이프라인 구성
dictionary_chain = prompt | llm | StrOutputParser()
tax_chain = {"query": dictionary_chain} | qa_chain
```

### 2.3 핵심 인사이트 💡

- **단순한 변화로 큰 효과**: "얼마인가요?" → "계산하면 얼마인가요?"
- **임베딩 특성**: 계산/세율/누진공제 같은 "계산 컨텍스트" 신호에 강하게 반응
- **검색 성능 향상**: 쿼리에 계산 관련 키워드만 추가해도 검색 정확도 대폭 상승

---

## 3. 소득세법 RAG 구축 접근법 🏗️

### 3.1 시스템 아키텍처

#### 문서 분할 (Text Splitting)

```python
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,    # 한 덩어리 최대 글자 수
    chunk_overlap=200,  # 앞뒤 청크 겹침으로 문맥 보존
)
```

#### 임베딩 및 벡터 저장

```python
# 멀티링구어 지원 임베딩 모델 사용
embedding = OpenAIEmbeddings(model='text-embedding-3-large')

# ChromaDB를 활용한 영구 저장
database = Chroma.from_documents(
    documents=document_list,
    embedding=embedding,
    collection_name='chroma-tax',
    persist_directory="./chroma"  # 로컬 영구 저장
)
```

#### 리트리버 최적화

```python
# MMR(Maximal Marginal Relevance) 활용으로 다양성과 관련성 균형
retriever = database.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 8,           # 최종 반환 문서 수
        "fetch_k": 24,    # 초기 검색 문서 수
        "lambda_mult": 0.5 # 관련성 vs 다양성 균형 (0~1)
    }
)
```

### 3.2 프롬프트 전략 🔧

1. **단순 프롬프트**: 컨텍스트 직접 삽입
2. **범용 프롬프트**: `hub.pull("rlm/rag-prompt")` 활용
3. **RetrievalQA Chain**: 자동화된 워크플로우 체인

---

## 4. 실무 적용 베스트 프랙티스 🎓

### 4.1 검색 성능 향상 핵심 요소

1. **데이터 전처리**: 이미지 표를 마크다운 형식으로 변환
2. **쿼리 최적화**: 용어 정규화 + 계산 컨텍스트 신호 강화
3. **평가 체계**: LangSmith를 통한 정량적 성능 측정
4. **리트리버 튜닝**: MMR로 관련성과 다양성 균형 조정

### 4.2 추천 도구 및 라이브러리 🛠️

#### 이미지 처리

- **pyzerox**: 이미지에서 텍스트 추출
- **Upstage Document Parser**: 문서 파싱 전문 도구

#### 모니터링 및 평가

- **LangSmith**: LLM 애플리케이션 전용 모니터링 플랫폼
- **평가 지표**: 정확성, 유용성, 환각 여부 3대 지표

#### 벡터 데이터베이스

- **ChromaDB**: 로컬 개발 및 프로토타이핑용
- **Pinecone**: 프로덕션 환경용 클라우드 벡터DB

### 4.3 성공 요인 분석 📈

1. **체계적 평가**: LangSmith를 통한 정량적 성능 측정
2. **도메인 최적화**: 소득세법 전용 용어 사전 및 쿼리 정규화
3. **데이터 품질**: 이미지 표의 텍스트 변환으로 검색 품질 향상
4. **지속적 개선**: 실험 결과를 바탕으로 한 반복적 최적화

---

## 5. 결론 및 다음 단계 🚀

### 5.1 핵심 학습 내용

- LangSmith를 활용한 체계적인 RAG 시스템 모니터링 방법 습득
- 도메인 특화(소득세법) 데이터 전처리 및 검색 최적화 기법 이해
- 실무에서 바로 적용 가능한 구체적인 코드 및 전략 확보

### 5.2 적용 권장사항

1. **단계별 접근**: 기본 RAG 구축 → 검색 최적화 → 평가 체계 도입
2. **도메인 특화**: 각 분야별 전문 용어 사전 및 쿼리 패턴 분석
3. **지속적 평가**: LangSmith를 통한 정기적 성능 측정 및 개선

이러한 체계적 접근법을 통해 석이가 고품질의 도메인 특화 RAG 시스템을 성공적으로 구축하실 수 있을 것입니다! 🎯
