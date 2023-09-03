def eight(i, j):
    new_lst = []
    for k in range(8):
        lst = []
        for l in range(8):
            lst.append(arr[i+k][j+l])
        new_lst.append(lst)
    tmp = 0
    for i in range(8):
        if i %2==0: # 짝수
            for j in range(8):
                if j%2==0:
                    if new_lst[i][j]=='W':
                        tmp += 1
                else:
                    if new_lst[i][j]=='B':
                        tmp += 1
        else:
            for j in range(8):
                if j%2==0:
                    if new_lst[i][j]=='B':
                        tmp += 1
                else:
                    if new_lst[i][j]=='W':
                        tmp += 1
    return min(tmp,64-tmp)

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

ans = 64
for i in range(n-8+1):
    for j in range(m-8+1):
        if ans > eight(i,j):
            ans = eight(i,j)

print(ans)