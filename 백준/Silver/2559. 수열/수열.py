n, k = map(int, input().split())
lst = list(map(int, input().split()))
ans = []
ans.append(sum(lst[:k]))
for i in range(n-k):
    ans.append(ans[i]-lst[i]+lst[i+k])
print(max(ans))