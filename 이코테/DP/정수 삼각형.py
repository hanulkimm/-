n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

if n==1:
    print(arr[0][0])
else:
    arr[1][0] += arr[0][0]
    arr[1][1] += arr[0][0]
    if n==2:
        print(max(arr[1][0], arr[1][1]))
    else:
        for i in range(2, n):
            for j in range(i+1):
                if j==0:
                    arr[i][j] += arr[i-1][j]
                elif j==i:
                    arr[i][j] += arr[i-1][j-1]
                else:
                    arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])
    print(max(arr[n-1]))