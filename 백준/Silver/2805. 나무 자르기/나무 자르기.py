n, M = map(int, input().split())
lst = list(map(int, input().split()))
h = max(lst)
s = 0
e = h
while s <= e:
    m = (s+e)//2
    cnt = 0
    for ch in lst:
        if ch > m:
            cnt += ch - m
    if cnt >= M:
        s = m+1
    elif cnt < M:
        e = m-1

print(e)