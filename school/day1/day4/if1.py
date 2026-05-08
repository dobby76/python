eg = input("영어 한 글자만 입력하세요: ")
if eg.isupper():
    print(eg.lower)
else:
    print(eg.upper)

score = int(input("점수를 입력하세요: "))

if score >= 81:
    print("A")
elif score >= 61:
    print("B")
elif score >= 41:
    print("C")
elif score >= 21:
    print("D")
else:
    print("E")