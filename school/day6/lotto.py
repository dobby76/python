import random
def get_lotto():
    numbers = []
    while len(numbers) < 6:
        n = random.randint(1, 45)

        if n not in numbers:
            # 중복 방지
            numbers.append(n) # 추가
    return numbers # 6개 숫자가 있는 리스트
print(f"로또번호는 {get_lotto()}입니다.")