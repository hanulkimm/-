dct = {'(':')'}
n = int(input())
for _ in range(n):
    stk = []
    ans = 'YES'
    st = input()
    for i in st:
        if i=='(':
            stk.append(dct[i])
        else:
            if stk and stk[-1]==i:
                stk.pop()
            else:
                ans = 'NO'
    if stk:
        ans = 'NO'
    print(ans)