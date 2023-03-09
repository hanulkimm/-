n, k = map(int, input().split())
dp = [0] * (k+1)
lst = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(k,lst[i][0]-1,-1):
        if dp[j] < dp[j-lst[i][0]] + lst[i][1]:
            dp[j] = dp[j-lst[i][0]] + lst[i][1]

print(dp[-1])
