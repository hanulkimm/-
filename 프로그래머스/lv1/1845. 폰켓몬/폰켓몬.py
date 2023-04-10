def solution(nums):
    ans = 0
    total = len(nums)
    m = total/2
    cnt = [0] * 200001 # 0~200000
    for i in nums:
        cnt[i] += 1
    select = 0
    for j in cnt:
        if j>0:
            select += 1
    if select >= m:
        ans = m
    else:
        ans = select
    return ans