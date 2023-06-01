## 냅색 알고리즘...?
## 그리디 문제와 살짝 다름

n, m = map(int, input().split())
money = list(int(input()) for _ in range(n))
# money.sort(reverse=True)
INF = 1e9
d = [INF] * (m+1)
d[0] = 0
for num in money:
    for i in range(num, m+1):
        d[i] = min(d[i], d[i-num]+1) # num을 더해주기 이전의 경우의 수에 +1
if d[m]==INF:
    print(-1)
else:
    print(d[m])
# while m>0:
#     flag = True
#     for i in money:
#         if m%i==0:
#             flag = False
#             ans += m//i
#             m = m%i
#             break
#     if flag:
#         ans = -1
#         break
# print(ans)
