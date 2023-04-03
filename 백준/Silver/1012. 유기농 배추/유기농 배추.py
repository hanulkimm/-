from collections import deque

def bfs(i,j):
    arr[i][j]=0
    q = deque()
    q.append((i,j))

    while q:
        si,sj = q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = si+di, sj+dj
            if 0<=ni<n and 0<=nj<m and arr[ni][nj]:
                arr[ni][nj]=0
                q.append((ni,nj))


t = int(input())
for tc in range(1, t+1):
    n, m, k= map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        arr[a][b]=1
    ans = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                ans += 1
                bfs(i,j)
    print(ans)