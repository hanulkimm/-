from collections import deque
def dfs(i):

    dfs_lst.append(i)
    v[i] = 1
    for j in adj[i]:
        if v[j]==0:
            dfs(j)

def bfs(i):
    v = [0] * (n+1)
    q = deque()
    q.append(i)
    bfs_lst.append(i)
    v[i]=1
    while q:
        s = q.popleft()
        for j in adj[s]:
            if v[j]==0:
                v[j]=1
                q.append(j)
                bfs_lst.append(j)


n, m, V = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
for lst in adj:
    lst.sort()
dfs_lst = []
bfs_lst = []
v = [0] * (n + 1)
dfs(V)
bfs(V)
print(*dfs_lst)
print(*bfs_lst)