n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
virus = []
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            virus.append([i,j,arr[i][j]])
virus.sort(key=lambda x:x[2])
# print(virus)
from collections import deque
q = deque()
for lst in virus:
    q.append(lst[:2]+[0])

while q:
    ci,cj,time = q.popleft()
    if time==s:
        break
    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni,nj = ci+di, cj+dj
        if 0<=ni<n and 0<=nj<n and arr[ni][nj]==0:
            arr[ni][nj]=arr[ci][cj]
            q.append((ni,nj,time+1))

print(arr[x-1][y-1])