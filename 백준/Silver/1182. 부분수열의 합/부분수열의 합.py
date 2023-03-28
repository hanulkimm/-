def dfs(i, sm, cnt):
    global ans
    if i == n:
        if sm == s and cnt > 0:
            ans += 1
            return
    else:
        dfs(i+1, sm+lst[i], cnt+1)
        dfs(i+1, sm, cnt)


n, s = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
dfs(0,0,0) #idx, sm, cnt
print(ans)