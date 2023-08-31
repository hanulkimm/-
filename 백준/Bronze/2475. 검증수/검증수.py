lst = list(map(int, input().split()))
ans = 0
for i in lst:
    ans += i*i
print(ans%10)