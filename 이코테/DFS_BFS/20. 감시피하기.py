from itertools import combinations
n = int(input())
arr = [list(input().split()) for _ in range(n)]
possible = []
t_lst = []
for i in range(n):
    for j in range(n):
        if arr[i][j]=='X':
            possible.append((i,j))
        elif arr[i][j]=='T':
            t_lst.append((i,j))

choose_lst = list(combinations(possible,3))
flag = True
for choose in choose_lst:

    cnt = 0
    for ci,cj in choose:
        arr[ci][cj]='O'
    for ti,tj in t_lst:
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            for k in range(1, n):
                ni,nj = ti+di*k, tj+dj*k
                if 0<=ni<n and 0<=nj<n:
                    if arr[ni][nj]=='O':
                        break
                    elif arr[ni][nj]=='S':
                        cnt += 1
                        break
                else:
                    break

    for ci,cj in choose:
        arr[ci][cj]='X'

    if cnt == 0:
        print("YES")
        flag = False
        break
if flag:
    print('NO')