from collections import deque
def bfs(n, cnt):
    global ans
    q = deque()
    q.append((n, cnt))
    while q:
        n, cnt = q.popleft()
        if n==k:
            ans = cnt
            break
        for new in [(n-1), (n+1), (n*2)]:
            if 0<=new<=100000 and v[new]==0:
                v[new]=1
                q.append((new, cnt+1))


n, k = map(int, input().split())
v = [0] * 100001
v[n]=1
ans = 0
bfs(n, 0)
print(ans)