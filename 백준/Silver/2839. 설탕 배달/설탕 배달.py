n = int(input())
ans = n
for i in range(n//5,-1,-1):
    if (n-i*5)%3==0:
       if ans > i + (n-i*5)//3:
           ans = i + (n-i*5)//3
if ans ==n:
    ans = -1
print(ans)