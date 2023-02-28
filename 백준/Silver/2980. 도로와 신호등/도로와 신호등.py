n, l = map(int, input().split())
arr = [[] for _ in range(l+1)]
for _ in range(n):
    d, r, g = map(int, input().split())
    arr[d].append(r)
    arr[d].append(g)

ans = 0
for i in range(1, l+1):
    if arr[i]:
        ans += 1
        sm = 0
        for num in arr[i]:
            sm += num

        if ans % sm <= arr[i][0]:
            ans += arr[i][0] - ans % sm

    else:
        ans += 1

print(ans)
