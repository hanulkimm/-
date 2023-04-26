def solution(park, routes):
    answer = []
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    dct = {'N':0, 'S':1, 'W':2, 'E':3}
    n = len(park[0])
    for x in range(n):
        for y in range(n):
            if park[x][y]=='S':
                i = x
                j = y
                break
    for route in routes:
        ci,cj = i, j
        flag = False
        dr, amount = route.split()
        amount = int(amount)
        for k in range(1, amount+1):
            ni,nj = i+di[dct[dr]], j+dj[dct[dr]]
            if 0<=ni<n and 0<=nj<n and park[ni][nj]!='X':
                i, j = ni,nj
            else:
                flag = True
                break
        if flag:
            i,j = ci,cj
    answer.append(i)
    answer.append(j)
    return answer