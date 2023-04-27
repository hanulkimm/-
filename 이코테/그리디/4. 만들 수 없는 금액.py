import sys
sys.stdin = open('input.txt', 'r')

from itertools import combinations

n = int(input())
lst = list(map(int, input().split()))
set_lst = set([])
for i in range(1, n+1):
    for combination in combinations(lst, i):
        set_lst.add(sum(combination))

for i in range(1, sum(lst)+1):
    if i in set_lst:
        continue
    else:
        print(i)
        break

# 해설 코드 다시 복습
