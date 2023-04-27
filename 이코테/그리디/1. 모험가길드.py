import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
ans = 0

cnt = 0
for num in lst:
    cnt += 1
    if cnt >= num: # 최신 num 기준으로 이전까지의 cnt 고려해주기
        ans += 1
        cnt = 0
print(ans)