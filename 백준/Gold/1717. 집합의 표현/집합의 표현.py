import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def find_set(x):
    if x == parent[x]:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]

def union(x,y):
    x, y = find_set(x), find_set(y)

    if x < y: # 값이 더 작은 쪽이 부모가 되도록
        parent[y] = x
    else:
        parent[x] = y


n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    i, a, b = map(int, input().split())
    if i==0:
        union(a,b)
    else:
        if find_set(a)==find_set(b):
            print('yes')
        else:
            print('no')