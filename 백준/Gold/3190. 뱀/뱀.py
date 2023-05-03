n = int(input())
arr = [[0]*n for _ in range(n)]
k = int(input())
for _ in range(k):
    i,j = map(int, input().split())
    arr[i-1][j-1]=2
c = int(input())
change = []
for _ in range(c):
    time, dr = input().split()
    time = int(time)
    change.append((time, dr))

# [1] 사전 작업
stk = [] # 뱀 길이 위치 좌표들
ci,cj = 0,0 # 시작 좌표
t, dr = 0, 0 # 시간, 방향
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
arr[ci][cj] = 1 # 방문 표시
stk.append((ci,cj))

# [2] 이동
while True:
    if change:
        if t == change[0][0]:
            _, chg = change.pop(0)
            if chg=='D':
                dr = (dr+1)%4
            else:
                dr = (dr+3)%4
    ni,nj = ci+di[dr], cj+dj[dr]
    if 0<=ni<n and 0<=nj<n:
        if arr[ni][nj]==2:
            t += 1
            arr[ni][nj]=1
            stk.append((ni,nj))
            ci,cj= ni,nj
        elif arr[ni][nj]==0:
            arr[ni][nj] = 1
            t += 1
            stk.append((ni,nj))
            pi,pj = stk.pop(0)
            arr[pi][pj]=0
            ci,cj = ni,nj
        else:
            t += 1
            break
    else:
        t += 1
        break
print(t)