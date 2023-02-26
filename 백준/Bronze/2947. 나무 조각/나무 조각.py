lst = list(map(int, input().split()))
n = len(lst)
while True:
    for i in range(n-1):
        if lst[i] > lst[i+1]:
            lst[i] , lst[i + 1] = lst[i + 1], lst[i]
            print(*lst)
    if lst == [1, 2, 3, 4, 5]:
        break
