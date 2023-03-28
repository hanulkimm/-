def dfs(i, cnt, lst):
    if i==n:
        if cnt==6:
            print(*lst)
    else:
        lst.append(num[i])
        dfs(i+1,cnt+1, lst)
        lst.pop()
        dfs(i+1, cnt, lst)


while True:
    n, *num = map(int, input().split())
    if n==0:
        break
    dfs(0,0,[]) # idx, cnt
    print()