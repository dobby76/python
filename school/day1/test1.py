name = input("상품 이름 입력: ")
price = int(input("가격 입력: "))
num = int(input("수량 입력: "))

total = price * num

#print(name+"총 금액은"+total+"원 입니다")
print(name,"총 금액은",total,"원입니다")
print(f"{name} 총 금액은 {total} 원입니다")