# 1 ~ 100 까지 합과 개수
sum = 0
cnt = 0

while cnt < 101:
    sum = sum + cnt # 합을 누적
    cnt = cnt +1 # 1씩 증가

print("개수는: ", cnt)
print("합계는: ", sum)