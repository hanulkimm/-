from statistics import mean
n = int(input())
nums = list(map(int, input().split()))
max_num = max(nums)
rst = []
for i in nums:
    rst.append(i/max_num*100)
print(mean(rst))