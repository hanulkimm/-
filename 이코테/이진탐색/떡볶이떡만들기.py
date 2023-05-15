def total(height):
    tmp = 0
    for num in lst:
        if height<num:
            tmp += (num-height)
    return tmp

def binary_search(start, end, target):
    while start<=end:
        mid = (start+end)//2
        if total(mid)==target:
            return mid
        elif total(mid) < target:
            end -= 1
        else:
            start += 1


n, m = map(int, input().split())
lst = list(map(int, input().split()))
print(binary_search(0, max(lst),m))