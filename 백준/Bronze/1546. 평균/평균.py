n = int(input())
lst = list(map(int, input().split()))
m = max(lst)
new_lst = []
for num in lst:
    new_lst.append(num/m*100)
print(sum(new_lst)/len(new_lst))