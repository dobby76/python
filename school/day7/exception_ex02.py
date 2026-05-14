fruits = ["사과", "배", "오렌지"] # 리스트 0 ~ 2

try:
    index = int(input("번호 입력(0 ~ 2): "))
    if index < 0 or index >= len(fruits):
        raise IndexError # 강제로 예외를 발생시킴

except IndexError:
    print("없는 인덱스입니다.")

except ValueError:
    print("숫자를 입력하세요.")

else:
    print(fruits[index])