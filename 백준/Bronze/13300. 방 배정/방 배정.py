n, k = map(int, input().split())
arr = [[0]*2 for _ in range(7)]
for _ in range(n):
    sex, grade = map(int, input().split())
    arr[grade][sex] += 1

ans = 0
for lst in arr:
    for num in lst:
        if num:
            ans += num//(k+1) +1
print(ans)