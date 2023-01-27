import sys
num = int(input())

lst = list(map(int,sys.stdin.readline().split()))
print(min(lst), max(lst))