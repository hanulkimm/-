n = int(input())

nums, count = 1,1
while n > nums:
    nums += 6 * count
    count += 1

print(count)