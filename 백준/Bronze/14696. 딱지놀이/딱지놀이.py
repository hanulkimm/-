n = int(input())
for _ in range(n):
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    cnt = [0] * 5
    for ch in lst1[1:]:
        cnt[ch] += 1
    for ch in lst2[1:]:
        cnt[ch] -= 1

    ans = 'D'
    for i in range(4,0,-1):
        if cnt[i]!=0:
            if cnt[i]>0:
                ans = 'A'
                break
            else:
                ans = 'B'
                break
        else:
            continue
    print(ans)