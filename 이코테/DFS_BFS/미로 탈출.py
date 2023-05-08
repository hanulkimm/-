from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

def bfs(i,j,cnt):
    q = deque([(i,j,cnt)])
    v[i][j]=cnt
    while q:
        ci,cj,cnt = q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<n and 0<=nj<m and arr[ni][nj]==1:
                if cnt+1 < v[ni][nj]:
                    v[ni][nj] = min(v[ni][nj], cnt+1)
                    q.append((ni,nj,cnt+1))
    return v[n-1][m-1]


INF = 1e9

v = [[INF] * m for _ in range(n)]
print(bfs(0,0,1))