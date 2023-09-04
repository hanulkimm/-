import sys
n = int(input())
stk = []
for _ in range(n):
    inp = sys.stdin.readline().split()
    if inp[0]=='push':
        stk.append(inp[1])
    elif inp[0]=='pop':
        if stk:
            print(stk.pop())
        else:
            print(-1)
    elif inp[0]=='size':
        print(len(stk))
    elif inp[0]=='empty':
        if stk:
            print(0)
        else:
            print(1)
    elif inp[0]=='top':
        if stk:
            print(stk[-1])
        else:
            print(-1)