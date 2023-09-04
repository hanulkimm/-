n = int(input())
lst_n = sorted(list(map(int, input().split())))
m = int(input())
lst_m = list(map(int, input().split()))
count = {}
for num in lst_n:
    if num in count:
        count[num]+=1
    else:
        count[num] =1

for i in lst_m:
    if i in count:
        print(count[i], end=' ')
    else:
        print(0, end=' ')