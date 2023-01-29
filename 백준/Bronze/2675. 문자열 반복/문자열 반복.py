n = int(input())
cases = [input().split() for _ in range(n)]
for case in cases:
    num = int(case[0])
    rst = []
    for i in case[1]:
        rst.append(i*num)
    print(''.join(rst))
