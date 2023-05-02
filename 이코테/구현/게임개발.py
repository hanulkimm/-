def dfs(i,j,dr):
    global ans
    ci,cj,dr = i, j, dr
    while True:
        flag = True
        for _ in range(4):
            dr = (dr+3)%4
            ni,nj=ci+di[dr],cj+dj[dr]
            if 0<=ni<n and 0<=nj<m and arr[ni][nj]==0 and v[ni][nj]==0:
                ans += 1
                v[ni][nj]=1
                ci,cj = ni,nj
                flag = False
                break
        if flag:
            ni,nj = ci-di[dr],cj-dj[dr]
            if 0<=ni<n and 0<=nj<m and arr[ni][nj]==1:
                break
            else:
                ci,cj = ni,nj

n, m = map(int, input().split())
i, j, dr = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
v = [[0]*m for _ in range(n)]
v[i][j]=1
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
ans = 0
dfs(i,j,dr)
print(ans)