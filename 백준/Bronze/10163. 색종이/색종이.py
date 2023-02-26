n = int(input())
ans  =0
arr = [[0]*1001 for _ in range(1001)]
for num in range(1,n+1):
    x, y, w, h = map(int, input().split())
    for i in range(x,x+w):
        for j in range(y, y+h):
            arr[i][j]=num

for i in range(1,n+1):
    cnt = 0
    for lst in arr:
        for ch in lst:
            if ch == i:
                cnt += 1
    print(cnt)
