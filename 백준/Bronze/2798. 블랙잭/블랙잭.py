
from itertools import combinations
n,m = map(int, input().split())
lst = list(map(int, input().split()))
comb = combinations(lst,3)
mx = 0
for i in comb:
    if sum(i)<=m and mx<sum(i):
        mx=sum(i)
print(mx)