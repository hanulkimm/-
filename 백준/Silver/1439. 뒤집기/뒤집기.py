lst = list(map(int, input()))
n = len(lst)
match = lst[0]
ans = 0
for i in range(n-1):
    if lst[i]!=lst[i+1] and lst[i+1]!=match:
        ans +=1
print(ans)