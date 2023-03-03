n = int(input())
arr = [[0] * 100 for _ in range(100)]
for _ in range(n):
    si, sj = map(int, input().split())
    for i in range(si,si+10):
        for j in range(sj,sj+10):
            arr[i][j] = 1
ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] ==0:
            if 0<=i-1<100:
                if arr[i - 1][j] == 1:
                    ans += 1
            if 0<=i+1<100:
                if arr[i + 1][j] == 1:
                    ans += 1
            if 0<=j-1<100:
                if arr[i][j - 1] == 1:
                    ans += 1
            if 0<=j+1<100:
                if arr[i][j+1]==1:
                    ans += 1
for ch in arr[0]:
    if ch == 1:
        ans += 1
for ch in arr[99]:
    if ch == 1:
        ans += 1
for i in range(100):
    if arr[i][0] == 1:
        ans += 1
    if arr[i][99] == 1:
        ans += 1
print(ans)