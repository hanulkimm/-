dct = {'(':')', '[':']'}
while True:
    st = input()
    if len(st)==1 and st=='.':
        break
    ans = 'yes'
    stk = []
    for i in st:
        if i in ('(','['):
            stk.append(dct[i])
        elif i in (')', ']'):
            if stk and stk[-1]==i:
                stk.pop()
            else:
                ans='no'
    if stk:
        ans = 'no'
    print(ans)