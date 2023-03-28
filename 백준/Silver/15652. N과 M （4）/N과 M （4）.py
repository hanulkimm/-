def dfs(i, ans):
    if ans !=sorted(ans):
        return
    if i==m:
        if ans==sorted(ans):
            print(*ans)
    else:
        for j in range(n):
            ans.append(lst[j])
            dfs(i+1, ans)
            ans.pop()


n, m = map(int, input().split())
lst = [i for i in range(1, n+1)]

dfs(0, [])