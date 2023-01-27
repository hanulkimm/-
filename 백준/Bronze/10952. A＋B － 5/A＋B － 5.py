import sys
while True:
    try:
        n,m = map(int, sys.stdin.readline().split())
        if n+m == 0:
            pass
        else:
            print(n+m)
    except:
        break