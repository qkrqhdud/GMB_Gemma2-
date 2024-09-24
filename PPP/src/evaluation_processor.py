import json

def load_evaluation_data(filepath):
    """JSON 파일에서 평가 데이터를 로드합니다."""
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def process_evaluation_results(data):
    """평가 결과를 처리하여 카테고리, 점수, 설명 및 개선 사항을 반환합니다."""
    categories = [result["category"] for result in data["evaluation_results"]]
    scores = [result["score"] for result in data["evaluation_results"]]
    explanations = [result["explanation"] for result in data["evaluation_results"]]
    suggestions = [result["improvement_suggestion"] for result in data["evaluation_results"]]
    
    additional_analysis = data["additional_analysis"]

    return {
        "categories": categories,
        "scores": scores,
        "explanations": explanations,
        "suggestions": suggestions,
        "additional_analysis": additional_analysis
    }
