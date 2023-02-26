n,m = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i!=j and j!=k and k!=i:
                cnt = lst[i]+lst[j]+lst[k]
                if m-cnt>=0 and (m-ans >= m-cnt):
                    ans = cnt
print(ans)