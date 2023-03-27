from collections import deque

t = int(input())
for tc in range(1, t + 1):
    m, n = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    v = [[0] * m for _ in range(n)]
    fire_q = deque()
    q = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '@':
                q.append((i, j, 0))
                v[i][j]=1
            if arr[i][j] == '*':
                fire_q.append((i, j, 0))
    ans = 0
    flag = False
    while True:
        while fire_q and fire_q[0][2] == ans:
            flag2 = False
            fi, fj, _ = fire_q.popleft()
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nfi, nfj = fi + di, fj + dj
                if 0 <= nfi < n and 0 <= nfj < m and (arr[nfi][nfj] == '.' or arr[nfi][nfj] == '@'):
                    arr[nfi][nfj] = '*'
                    fire_q.append((nfi, nfj, ans + 1))
        while q and q[0][2] == ans:
            ci, cj, _ = q.popleft()
            if ci == 0 or cj == 0 or ci == n - 1 or cj == m - 1:
                print(ans + 1)
                flag = True
                break
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = ci + di, cj + dj
                if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == '.' and v[ni][nj]==0:
                    arr[ni][nj] = '@'
                    if arr[ci][cj]!='*':
                        arr[ci][cj] = '.'
                    v[ni][nj]=1
                    q.append((ni, nj, ans + 1))
        ans += 1
        if flag:
            break
        if not q:
            print("IMPOSSIBLE")
            break