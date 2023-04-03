from collections import deque
def bfs(i,j):
    q = deque()
    q.append((i,j))
    v[i][j]=1
    while q:
        si,sj = q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = si+di,sj+dj
            if 0<=ni<n and 0<=nj<m and arr[ni][nj]:
                if v[ni][nj]==0 or v[ni][nj]>v[si][sj]+1:
                    v[ni][nj]=v[si][sj]+1
                    q.append((ni,nj))

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
v = [[0]*m for _ in range(n)]
bfs(0,0) # 좌표
print(v[n-1][m-1])