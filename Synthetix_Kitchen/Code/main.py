import json
from macro_calculator import MacroScaler

# 데이터 불러오기
def load_db():
    # 경로 설정 (상대경로)
    path = "../Data/ingredient_db.json"
    
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    print("=== 다이어트 레시피 생성기 ===")
    
    # DB 로딩
    db_data = load_db()
    
    # ID로 찾기 쉽게 딕셔너리로 변환
    db_map = {item['id']: item for item in db_data}
    
    menu = input("먹고 싶은 메뉴: ")
    
    print("재료 ID 입력 (콤마로 구분, 예: 1, 2)")
    # 공백 제거하고 리스트로 만듦
    user_input = input("> ").split(",")
    
    my_list = []
    for uid in user_input:
        uid = uid.strip()
        if uid in db_map:
            data = db_map[uid]
            my_list.append({
                "name": data['name'],
                "calories_per_100g": data['nutrition_per_100g']['calories'],
                "protein_per_100g": data['nutrition_per_100g']['protein']
            })
    
    if len(my_list) == 0:
        print("재료가 없어요.")
        return

    # 목표치 (일단 300으로 고정)
    target_cal = 300
    target_prot = 20
    
    scaler = MacroScaler(target_cal, target_prot)
    
    # result = scaler.calc(selected_ingredients)
    result = scaler.calculate(my_list)
    
    print(f"\n=== 결과: {menu} ({target_cal}kcal) ===")
    print("아래 정량대로 조리하세요:\n")
    
    for item in result:
        print(f"- {item['name']}: {item['grams']}g (Cal: {item['calories']})")
        
    print("\n끝!")

if __name__ == "__main__":
    main()
