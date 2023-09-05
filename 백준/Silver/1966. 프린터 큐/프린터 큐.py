def max_one(lst):
    n = lst[0][1]
    for idx, num in lst[1:]:
        if num>n:
            return False
    return True

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    lst = list(map(int, input().split()))

    target_idx, target_num = m, lst[m]
    idx_lst = []
    for idx, num in enumerate(lst):
        idx_lst.append((idx,num))

    turn = 0
    while idx_lst:
        if len(idx_lst)==1 or max_one(idx_lst):
            turn += 1
            x,y = idx_lst.pop(0)
            if x==target_idx and y==target_num:
                print(turn)
                break
        else:
            idx_lst.append(idx_lst.pop(0))