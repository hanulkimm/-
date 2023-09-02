n = int(input())

if n==1:
    print(1)
else:
    tmp = 1
    for i in range(1,n):
        tmp += 6*i
        if n <= tmp:
            print(i+1)
            break