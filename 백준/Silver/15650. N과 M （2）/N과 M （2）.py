def dfs(i, ans):
    if i==m:
        if ans==sorted(ans):
            print(*ans)
    else:
        for j in range(n):
            if v[j]==0:
                ans.append(lst[j])
                v[j]=1
                dfs(i+1, ans)
                ans.pop()
                v[j]=0

n, m = map(int, input().split())
lst = [i for i in range(1, n+1)]
v = [0]*n
dfs(0, [])