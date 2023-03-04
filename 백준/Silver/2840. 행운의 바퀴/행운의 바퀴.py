n, k = map(int, input().split()) # 바퀴 칸 수 , 바퀴 돌리는 횟수
lst = [0] * n
st = 0
ans = []
for _ in range(k):
    i, ch = input().split()
    i = int(i)
    new = (st + i) % n
    if lst[new] and lst[new] != ch:
        ans = '!'
    else:
        lst[new] = ch
    st = new

for ch in lst:
    if ch != 0:
        cnt = lst.count(ch)
        if cnt > 1:
            ans = '!'

if ans == '!':
    print(ans)
else:
    for i in range(n):
        if lst[i] == 0:
            lst[i] = '?'
    ans = []
    for i in range(st, -1,-1):
        ans.append(lst[i])
    for j in range(n-1,st,-1):
        ans.append(lst[j])

    print(*ans,sep='')
