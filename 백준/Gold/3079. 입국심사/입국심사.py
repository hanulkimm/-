n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
s, e = 0 , max(arr)*m
ans = e
while s<=e:
    total = 0 # 사람 수
    mid = (s+e)//2

    for i in range(n):
        total += mid//arr[i] # 한 심사대에서 심사할 수 있는 사람

    if total >= m: # 충분히 심사 할 수 있다면
        e = mid - 1
        if ans > mid:
            ans = mid
    else:
        s = mid +1
print(ans)