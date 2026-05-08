aa = int(input("아메리카노의 판매 개수를 입력하세요: "))
cl = int(input("카페라떼의 판매 개수를 입력하세요: "))
cp = int(input("카푸치노의 판매 개수를 입력하세요: "))

aa_all = aa * 2000
cl_all = cl * 3000
cp_all = cp * 3500

print("아메리카노 판매 개수:",aa)
print("카페라떼 판매 개수:",cl)
print("카푸치노 판매 개수:",cp)
print("총 매출:",aa_all+cl_all+cp_all,"입니다.")