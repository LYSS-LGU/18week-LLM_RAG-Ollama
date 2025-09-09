# Wikipedia 한국어 데이터셋 다운로드 스크립트

from datasets import load_dataset
import os

def download_wikipedia_ko():
    """
    Hugging Face Datasets에서 한국어 Wikipedia 데이터셋을 다운로드합니다.
    """
    print("=== Wikipedia 한국어 데이터셋 다운로드 시작 ===")
    
    try:
        # Wikipedia 한국어 데이터셋 로드
        print("데이터셋 로딩 중...")
        dataset = load_dataset("wikimedia/wikipedia", "20231101.ko")
        
        print(f"✅ 데이터셋 로드 완료!")
        print(f"📊 데이터셋 정보:")
        print(f"   - 훈련 데이터: {len(dataset['train'])}개 문서")
        print(f"   - 컬럼: {dataset['train'].column_names}")
        
        # 샘플 데이터 확인
        print(f"\n📝 샘플 문서 (첫 번째):")
        sample = dataset['train'][0]
        print(f"   - ID: {sample.get('id', 'N/A')}")
        print(f"   - 제목: {sample.get('title', 'N/A')}")
        print(f"   - 텍스트 길이: {len(sample.get('text', ''))}")
        print(f"   - 텍스트 미리보기: {sample.get('text', '')[:200]}...")
        
        return dataset
        
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        return None

def save_sample_data(dataset, num_samples=100):
    """
    샘플 데이터를 로컬에 저장합니다.
    """
    if dataset is None:
        print("❌ 데이터셋이 없습니다.")
        return
    
    print(f"\n=== 샘플 데이터 저장 중 ({num_samples}개) ===")
    
    try:
        # 샘플 데이터 추출
        sample_data = dataset['train'].select(range(min(num_samples, len(dataset['train']))))
        
        # CSV로 저장
        sample_data.to_csv('wikipedia_ko_sample.csv')
        print(f"✅ CSV 파일 저장 완료: wikipedia_ko_sample.csv")
        
        # JSON으로 저장
        sample_data.to_json('wikipedia_ko_sample.json')
        print(f"✅ JSON 파일 저장 완료: wikipedia_ko_sample.json")
        
    except Exception as e:
        print(f"❌ 저장 오류: {e}")

if __name__ == "__main__":
    # 데이터셋 다운로드
    dataset = download_wikipedia_ko()
    
    if dataset:
        # 샘플 데이터 저장
        save_sample_data(dataset, num_samples=1000)
        
        print(f"\n🎉 완료! Wikipedia 한국어 데이터셋이 준비되었습니다.")
        print(f"💡 사용법:")
        print(f"   - 전체 데이터: dataset['train']")
        print(f"   - 특정 문서: dataset['train'][인덱스]")
        print(f"   - 샘플 데이터: wikipedia_ko_sample.csv 또는 .json")
    else:
        print("❌ 데이터셋 다운로드에 실패했습니다.")
