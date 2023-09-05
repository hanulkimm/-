import sys
n = int(sys.stdin.readline())
dct = {}
lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))
lst.sort()
for i in lst:
    if i in dct:
        dct[i]+=1
    else:
        dct[i]=1
print(round(sum(lst)/len(lst)))
print(lst[(n-1)//2])
tmp = []
for num, cnt in dct.items():
    if cnt==max(dct.values()):
        tmp.append(num)
if len(tmp)==1:
    print(tmp[0])
else:
    tmp.sort()
    print(tmp[1])

print(max(lst)-min(lst))
