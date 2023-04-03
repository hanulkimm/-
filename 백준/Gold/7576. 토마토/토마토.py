from collections import deque

def imp(arr):
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                return True

def bfs(lst):
    q = deque()
    for a in lst:
        q.append(a)

    while q:
        si,sj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = si + di, sj + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0:
                arr[ni][nj] = arr[si][sj] + 1
                q.append((ni, nj))


m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
tomato = []
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            tomato.append((i,j))

bfs(tomato)
ans = -1

if not imp(arr):
    for lst in arr:
        ans = max(ans, max(lst))
if ans !=-1:
    ans -= 1
print(ans)