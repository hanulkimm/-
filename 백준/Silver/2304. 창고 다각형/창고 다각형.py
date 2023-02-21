n = int(input())
arr = [0] * 1001 # 0~1001
mx_i = 0
mx = 0
for _ in range(n):
    l, h = map(int, input().split())
    arr[l] = h
    if mx < h:
        mx = h
        mx_i = l

ans = 0
stk = []
for ch in arr[:mx_i+1]:
    if stk:
        if stk[-1] < ch:
            stk.append(ch)
        ans += stk[-1]
    else:
        stk.append(ch)
        ans += stk[-1]
stk = []
for ch in arr[mx_i+1:][::-1]:
    if stk:
        if stk[-1] < ch:
            stk.append(ch)
        ans += stk[-1]
    else:
        stk.append(ch)
        ans += stk[-1]
print(ans)