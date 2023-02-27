lst = []
for _ in range(9):
    lst.append(int(input()))
sm = sum(lst)
dlt = []
for i in range(9):
    for j in range(9):
        if dlt:
            break
        if i != j:
            if sm - lst[i]- lst[j] == 100:
                dlt.append(lst[i])
                dlt.append(lst[j])
                break
alst = []
for ch in lst:
    if ch not in dlt:
        alst.append(ch)
alst.sort()
for ch in alst:
    print(ch)
