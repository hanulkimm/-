def binary_search(s, e):
    if s>e:
        return -1
    m = (s+e)//2
    if lst[m]==m:
        return m
    elif lst[m] < m:
        return binary_search(m+1, e)
    else:
        return binary_search(s,m-1)


n = int(input())
lst = list(map(int, input().split()))
s, e = 0, n-1
ans = binary_search(0,n-1)
print(ans)