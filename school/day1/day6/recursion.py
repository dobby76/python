# 재귀 호출(함수 내부에서 자기자신을 호출)
# 5!(팩토리얼) 1*2*3*4*5

def fact(n): # fact: 함수명(매개변수 1개)
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

a = int(input("정수를 입력하세요: "))
res = fact(a) # 함수 호출, 인수 a(정수) 보냄
# 반환 되어서 온 결과값을 res 저장
print(n,"!는",res,"이다")
