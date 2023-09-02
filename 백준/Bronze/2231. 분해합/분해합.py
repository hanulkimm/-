n = int(input())
for i in range(1, n+1):
    sm = sum(map(int, str(i)))
    if i + sm == n:
        print(i)
        break
    if i==n:
        print(0)