lst = []
for _ in range(10):
    lst.append(int(input()))
ans = 0
for ch in lst:
    if abs(100-ans) >= abs(100-ans-ch):
        ans += ch
    else:
        break
print(ans)