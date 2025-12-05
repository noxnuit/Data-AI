class MacroScaler:
    def __init__(self, target_calories, target_protein):
        self.target_calories = target_calories
        self.target_protein = target_protein

    def calculate(self, ingredients):
        # 100g 기준 총 칼로리
        total_base = sum(ing['calories_per_100g'] for ing in ingredients)
        
        if total_base == 0:
            return []

        # 목표 칼로리에 맞춰 비율 계산 (Target / Base)
        ratio = self.target_calories / total_base
        # print(f"scaling ratio: {ratio}") # 디버깅용
        
        result = []
        for ing in ingredients:
            result.append({
                "name": ing['name'],
                "grams": round(100 * ratio, 1),
                "calories": round(ing['calories_per_100g'] * ratio, 1),
                "protein": round(ing['protein_per_100g'] * ratio, 1)
            })
            
        return result
