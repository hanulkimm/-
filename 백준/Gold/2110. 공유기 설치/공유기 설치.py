n, c = map(int, input().split())
lst = [int(input()) for _ in range(n)]
lst.sort()
s, e = 1, lst[-1]-lst[0]
ans = 0
while s<=e:
    m = (s+e)//2
    cnt = 1
    start = lst[0]
    for i in range(1, n):
        if lst[i]>=start+m:
            start = lst[i]
            cnt += 1
    if cnt >=c:
        s = m+1
        ans = m
    else:
        e = m-1
print(ans)