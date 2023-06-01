n = int(input())
lst = list(map(int, input().split()))
d = [0] * n
d[0], d[1] = lst[0], lst[1]
for i in range(2, n):
    d[i] = lst[i] + max(d[:i-1])
print(max(d))

## 최대값만 저장
n = int(input())
lst = list(map(int, input().split()))
d = [0] * n
d[0], d[1] = lst[0], max(lst[0], lst[1])
for i in range(2, n):
    d[i] = max(d[i-2], d[i-1]) + lst[i]
print(d[n-1])