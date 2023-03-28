def dfs(i, ans):
    if i==m:
        print(*ans)
    else:
        for j in range(n):
            ans.append(lst[j])
            dfs(i+1, ans)
            ans.pop()


n, m = map(int, input().split())
lst = [i for i in range(1, n+1)]

dfs(0, [])