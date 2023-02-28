def max_idx(lst):
    mx = 0
    mx_idx = -1
    for i in range(n):
        if mx <= lst[i]:
            mx = lst[i]
            mx_idx = i
    return mx_idx
n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
if len(lst) == 1:
    ans = 0
else:
    ans = 0

    while True:
        idx = max_idx(lst)
        if idx == 0:
            break
        else:
            lst[idx] -= 1
            lst[0] += 1
            ans += 1

print(ans)