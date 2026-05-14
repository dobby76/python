def calc(r1):
    result = 3.14*r1**2 # r1 반지름
    return result

r = float(input("원의 반지름 입력: "))
area = calc(r)
print(area)

############################################

def calc(r2):
    global a
    a = 3.14*r2**2 # r1 반지름
    return a # 지녁 변수
a = 0 # 전역 변수
rr= float(input("원의 반지름 입력: "))
calc(rr)
print(a) # 0 전역변수