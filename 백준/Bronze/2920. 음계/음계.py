lst = list(map(int, input().split()))

if lst[0] < lst[1]:
    ans = 'ascending'
    for i in range(1,7):
        if lst[i]>lst[i+1]:
            ans = 'mixed'
else:
    ans = 'descending'
    for i in range(1, 7):
        if lst[i] < lst[i+1]:
            ans = 'mixed'
print(ans)