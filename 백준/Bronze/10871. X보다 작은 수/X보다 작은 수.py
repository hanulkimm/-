import sys
n,x= input().split()
lst = list(map(int,sys.stdin.readline().split()))
rst = []
for num in lst:
    if num < int(x):
        rst.append(num)

print(*rst)