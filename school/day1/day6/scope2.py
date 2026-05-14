# 스코프(scope)
# 파이썬은 변수를 찾을 때 가까운 영역부터 찾음
# LEGB 규칙(Local -> Enclosing -> Global -> Bulit-in)
# Local -> 함수 내부 변수
# Enclosing -> 바깥 함수 변수
# Global -> 함수 밖 변수
# Bulit-in -> pytion이 기본 제공하는 이름(print, input, len)
a = '홍길동'
b = 99

def function1(): # 함수1
    a = '이순신'
    c = [1 ,2 ,3]
    
    def function2(): # 함수1안에 함수2
        d = (1, 2, 3)
        print('Local a =',a) # 이순신
        print('Local b =',b) # 99
        print('Local c =',c) # [1,2,3]
        print('Local d =',d) # (1,2,3)
        
    
    function2()
    print('Enclosing a =',a)
    print('Enclosing b =',b)
    print('Enclosing c =',c)
    print('Enclosing d =',d) 
function1()
print('Global a =',a)
print('Global b =',b)
print('Global c =',c) 
print('Global d =',d) 