def binary_search(s,e,lst,target):
    if s > e :
        return False
    m = (s+e)//2
    if lst[m]==target:
        return True
    elif lst[m] < target:
        return binary_search(m+1,e,lst,target)
    else:
        return binary_search(s, m-1, lst, target)

n = int(input())
lst_n = list(map(int, input().split()))
m = int(input())
lst_m = list(map(int, input().split()))
lst_n.sort()

for i in lst_m:
    if binary_search(0,n-1, lst_n, i):
        print(1)
    else:
        print(0)