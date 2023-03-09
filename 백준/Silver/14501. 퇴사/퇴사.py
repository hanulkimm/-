n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n+1) # 0~n
for i in range(n):
    for j in range(i+lst[i][0], n+1): # 상담 끝나는 날부터 끝까지
        if dp[j] < dp[i] + lst[i][1]: # 상담 추가 될 때마다 중복되지 않게 할 수 있는 이전 상담 금액 추가
            dp[j] = dp[i] + lst[i][1]

print(dp[-1])