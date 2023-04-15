n,k = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort(reverse=True)
ans = 0
for price in lst:
    ans += k // price
    k %= price
print(ans)