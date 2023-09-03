n = int(input())
lst = []
for _ in range(n):
    lst.append(tuple(map(int, input().split())))
ans = []
for i in range(n):
    tmp = 1
    for j in range(n):
        if lst[i][0]<lst[j][0] and lst[i][1]<lst[j][1]:
           tmp += 1
    ans.append(tmp)
for i in ans:
    print(i, end=' ')