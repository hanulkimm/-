n = int(input())

rst = 0
for num in range(1,n+1):

    num = str(num)
    dif = []

    if len(num) == 1:
        rst += 1
    elif len(num) ==  2:
        rst += 1
    elif len(num) == 3:
        if int(num[1])-int(num[0]) == int(num[2])-int(num[1]):
            rst += 1
    else:
        pass

print(rst)