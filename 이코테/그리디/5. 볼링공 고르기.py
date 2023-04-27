# dct 사용
n, m = map(int, input().split())
lst = list(map(int, input().split()))
dct = {i:0 for i in set(lst)}
for num in lst:
    dct[num] += 1
ans = 0
for key1, value1 in dct.items():
    for key2, value2 in dct.items():
        if key1 != key2:
            ans += value1 * value2
print(ans//2)

# cnt list 사용
n, m = map(int, input().split())
lst = list(map(int, input().split()))
cnt = [0] * 11
for num in lst:
    cnt[num] += 1
ans = 0
for i in range(1, m+1):
    if cnt[i]:
        ans += sum(cnt[i+1:])*cnt[i]
print(ans)