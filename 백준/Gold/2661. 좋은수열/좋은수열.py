def dfs(i, cnt, st):
    global ans
    if int(st) > int(ans[:len(st)]):
        return
    for num in range(2, m+1):
        if len(st)>=2*num:
            if st[len(st)-num:]==st[len(st)-2*num:len(st)-num]:
                return
    if cnt==n:
        if int(ans) > int(st):
            ans = st
        return
    for j in range(1, 4):
        if v[j]==0:
            v[j]=1
            v[i]=0
            dfs(j, cnt+1, st+str(j))
            v[j]=0
            v[i]=1

n = int(input())
m = n//2
v = [0] * 4
v[1]=1
ans = '3'*n

dfs(1, 1, '1') # start, cnt, st
print(ans)