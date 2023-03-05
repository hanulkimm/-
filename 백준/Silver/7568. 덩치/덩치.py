n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    cnt = 1
    w, h = arr[i][0], arr[i][1]
    if i == 0:
        for j in range(i+1, n):
            if w < arr[j][0] and h < arr[j][1]:
                cnt += 1
        print(cnt, end=' ')
    elif i == n-1:
        for j in range(n):
            if w < arr[j][0] and h < arr[j][1]:
                cnt += 1
        print(cnt, end=' ')
    else:
        for j in range(i):
            if w < arr[j][0] and h < arr[j][1]:
                cnt += 1
        for k in range(i+1, n):
            if w < arr[k][0] and h < arr[k][1]:
                cnt += 1
        print(cnt, end = ' ')
