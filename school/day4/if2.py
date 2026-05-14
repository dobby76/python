jumin = input("주민번호를 입력하세요: ")
 #081212-321111

# num = jumin.split("-")
# 081212 -> [0]
# 3211111 -> [1] -> num
# if num[0] == "1" or num[1] == '3':
#     print("남자")
# elif num[0] == '2' or num[1] == '4':
#     print("여자")

if jumin[7] == "1" or jumin[7] == "3":
    print("남자")
elif jumin[7] == "2" or jumin[7] == "4":
    print("여자")

number = int(input("첫번째 숫자를 입력하세요: "))
number2 = int(input("두번째 숫자를 입력하세요: "))
number3 = int(input("세번째 숫자를 입력하세요: "))

if number > number2 and number > number3:
    print("큰수는: ",number)

elif number2 > number and number2 > number3:
    print("큰 수는: ",number2)

else:
    print("큰 수는: ",number3)