while True:
    lst = list(map(int, input().split()))
    if lst[0]==0:
        break
    else:
        lst.sort()
        a,b,c = lst[0],lst[1],lst[2]
        if a*a+b*b==c*c:
            print('right')
        else:
            print('wrong')