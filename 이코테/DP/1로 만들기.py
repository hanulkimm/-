
n = int(input())
d = [0] * 1000001
for i in range(2, n+1):
    d[i] = d[i-1] + 1 # minus 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 5 ==0:
        d[i] = min(d[i], d[i//5]+1)

print(d[n])


### 백트래킹 ###
n = int(input())
ans = n
def div(n, cnt):
    global ans
    # 가지치기
    if cnt > ans:
        return
    if n==1:
        ans = min(ans, cnt)
        return
    if n%5 == 0:
        div(n//5, cnt+1)
    if n % 3 == 0:
        div(n // 3, cnt + 1)
    if n % 2 == 0:
        div(n // 2, cnt + 1)
    div(n-1, cnt+1)

div(n, 0)
print(ans)