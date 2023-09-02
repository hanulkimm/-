while True:
    n = int(input())
    if n==0:
        break
    lst = list(str(n))
    if lst==lst[::-1]:
        print('yes')
    else:
        print('no')