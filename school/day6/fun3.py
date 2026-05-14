def dis_price(price,rate):  # 함수명 (가격, 할인율)
    discount = price * (rate/100) 
    final_price = price - discount
    return final_price

price_a = dis_price(10000,10)
print(f"상품은 {price_a}입니다.")

price_b = dis_price(50000,20)
print(f"상품은 {price_b}입니다.")