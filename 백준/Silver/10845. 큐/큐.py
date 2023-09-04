import sys
from collections import deque
n = int(input())
q = deque([])
for _ in range(n):
    inp = sys.stdin.readline().split()
    if inp[0]=='push':
        q.append(inp[1])
    elif inp[0]=='pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif inp[0]=='size':
        print(len(q))
    elif inp[0]=='empty':
        if q:
            print(0)
        else:
            print(1)
    elif inp[0]=='front':
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)