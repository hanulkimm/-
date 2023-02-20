V = int(input())
n = int(input())
adj = [[] for _ in range(V+1)]
for _ in range(n):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

v =[0]*(V+1) 
stk = []
s = 1
v[s] = 1
alst = []

while True:
    for e in adj[s]:
        if v[e] == 0:
            stk.append(s)
            s = e
            v[s] = 1
            alst.append(s)
            break
    else:
        if stk:
            s = stk.pop()
        else:
            break

print(len(set(alst)))