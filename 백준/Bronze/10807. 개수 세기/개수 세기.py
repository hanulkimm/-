import sys
n = int(input())
lst = list(map(int,sys.stdin.readline().split()))

find_num = int(input())
print(lst.count(find_num))