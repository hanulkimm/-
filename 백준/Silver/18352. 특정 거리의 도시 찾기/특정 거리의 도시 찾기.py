from collections import deque
def bfs(start,time):
    q = deque([(start, time)])
    v[start]=1
    while q:
        st, time = q.popleft()
        if time > k:
            break
        if time==k:
            ans.append(st)
            continue
        for end in adj[st]:
            if v[end]==0:
                v[end]=1
                q.append((end, time +1))

n, m, k, x = map(int, input().split()) # 도시의 개수, 도로의 개수, 최단 거리, 출발 도시
adj =[[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)

ans = []
v = [0] * (n+1)
bfs(x,0)
if ans:
    ans.sort()
    for num in ans:
        print(num)
else:
    print(-1)