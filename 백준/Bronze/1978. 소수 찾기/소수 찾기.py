import math

def prime_num(x):
    for i in range(2, int(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True

n = int(input())
lst = list(map(int, input().split()))
# 소수 판별하기
ans = 0
for num in lst:
    if num==1:
        continue
    elif num==2 or num==3:
        ans += 1
    else:
        if prime_num(num):
            ans += 1

print(ans)