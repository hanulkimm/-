n = int(input())
lst = list(map(int, input().split()))

dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if lst[j] > lst[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(dp)
print(n- max(dp))  # 주의) dp[-1]이 아니라 max(dp)!