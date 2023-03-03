def cnt(arr):
    mx = 0
    for i in range(n): # 행 기준
        cnt1 = 1
        for j in range(n-1):
            if arr[i][j]==arr[i][j+1]:
                cnt1 += 1
            else:
                cnt1 = 1
            if mx <= cnt1:
                mx = cnt1
    for j in range(n): # 열 기준
        cnt2 = 1
        for i in range(n-1):
            if arr[i][j] == arr[i+1][j]:
                cnt2 += 1
            else:
                cnt2 = 1
            if mx <= cnt2:
                mx = cnt2
    return mx

n = int(input())
arr = [list(input()) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)): # 상하좌우
            ni,nj = i+di,j+dj
            if 0<=ni<n and 0<=nj<n and arr[ni][nj]!=arr[i][j]: # 범위 내이고 다른 색
                arr[i][j],arr[ni][nj] = arr[ni][nj], arr[i][j] # 바꿔주기
                if ans < cnt(arr):
                    ans = cnt(arr)
                arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j] # 되돌리고
print(ans)