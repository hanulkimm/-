from itertools import combinations
from collections import deque

def bfs(arr):
    q = deque()
    for k in virus:
        q.append(k)
    while q:
        ci, cj = q.popleft()
        v[ci][cj]=1
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<n and 0<=nj<m and arr[ni][nj]==0 and v[ni][nj]==0:
                q.append((ni,nj))

n, m = map(int, input().split())
arr =[list(map(int, input().split())) for _ in range(n)]
ans = 0
tmp = []
virus = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            tmp.append((i,j))
        if arr[i][j]==2:
            virus.append((i,j))

for comb in list(combinations(tmp, 3)):
    v = [[0]*m for _ in range(n)]
    for num in comb:
        a, b = num[0], num[1]
        arr[a][b]=1
    bfs(arr)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if v[i][j]==0 and arr[i][j]==0:
                cnt += 1
    ans = max(ans, cnt)
    for num in comb:
        a, b = num[0], num[1]
        arr[a][b]=0
print(ans)