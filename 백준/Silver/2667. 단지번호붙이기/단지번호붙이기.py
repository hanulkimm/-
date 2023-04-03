
from collections import deque

def bfs(i,j):
    tmp = 1
    q = deque()
    q.append((i,j))
    arr[i][j]=0
    while q:
        si,sj = q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = si+di, sj+dj
            if 0<=ni<n and 0<=nj<n and arr[ni][nj]==1:
                arr[ni][nj]=0
                tmp += 1
                q.append((ni,nj))
    cnt.append(tmp)

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
ans = 0
cnt = []
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            ans += 1
            bfs(i,j)
print(ans)
cnt.sort()
for num in cnt:
    print(num)