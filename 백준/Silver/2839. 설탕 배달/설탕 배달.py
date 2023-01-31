n = int(input())

rst = []          
for i in range(1001):
    for j in range(1667):

        if 5*i + 3*j == n:
            rst.append(i+j)
            
        else:
            continue
if rst == []:
    print(-1)
else:
    print(min(rst))