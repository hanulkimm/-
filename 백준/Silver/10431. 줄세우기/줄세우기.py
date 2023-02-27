t = int(input())
for _ in range(t):
    tc, *lst = map(int, input().split())
    cnt = 0

    for i in range(1, 20):
        s = -1
        for j in range(i-1, -1, -1):
            if lst[j] > lst[i]:
                s = j
        if s == -1:
            continue
        tmp = lst[i]
        for k in range(i,s,-1):
            cnt += 1
            lst[k] = lst[k-1]
        lst[s]=tmp

    print(tc, cnt)