# from the back ##
import sys
n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)][::-1]

cnt = 0
ans = 0
for lst in arr:
    if len(lst) == 1:
        cnt += 1
    else:
        cnt += 1
        if lst[2] <= cnt:
            ans += lst[1]
            cnt -= lst[2]
        else:
            cnt = 0
print(ans)