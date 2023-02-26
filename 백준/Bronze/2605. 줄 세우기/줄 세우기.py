n =int(input())
move = list(map(int, input().split()))
lst = [i for i in range(1, n+1)]
for i in range(n):
    mv = move[i]
    if mv ==0:
        continue
    else:
        tmp = lst[i]
        for j in range(i, i-mv, -1):
            lst[j] = lst[j-1]
        lst[i-mv] = tmp
print(*lst)
