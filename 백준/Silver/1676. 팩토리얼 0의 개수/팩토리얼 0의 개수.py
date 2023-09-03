n=int(input())
num = 1
for i in range(1, n+1):
    num *= i

rvs = str(num)[::-1]
ans = 0
for i in range(len(rvs)):
    if rvs[i]=='0':
        ans += 1
    else:
        print(ans)
        break