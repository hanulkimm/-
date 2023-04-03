from collections import deque

def bfs(i,j) :
    q = deque()
    q.append((i,j))
    v[i][j]=1
    while q:
        si,sj = q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)):
            ni,nj = si+di, sj+dj
            if 0<=ni<n and 0<=nj<m and v[ni][nj]==0 and arr[ni][nj]==1:
                arr[ni][nj]=-1
                v[ni][nj]=1
                q.append((ni,nj))

while True:
    m, n = map(int,input().split())
    if m==0:
        break
    else:
        arr = [list(map(int, input().split())) for _ in range(n)]
        v = [[0]*m for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j]==1:
                    ans += 1
                    bfs(i,j)
        print(ans)