#python 시간초과...

from collections import deque
def bfs(start):
    q = deque([start])
    v[start]=0
    while q:
        st = q.popleft()
        for end in adj[st]:
            if v[end]==-1:
                v[end]=v[st]+1
                q.append(end)

n, m, k, x = map(int, input().split()) # 도시의 개수, 도로의 개수, 최단 거리, 출발 도시
adj =[[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)

ans = []
v = [-1] * (n+1)
bfs(x)

flag = True
for i in range(1, n+1):
    if v[i]==k:
        print(i)
        flag = False
if flag:
    print(-1)