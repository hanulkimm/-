# 재귀 이용
def binary_search(start, end, target):
    if start>end:
        return False
    middle = (start+end)//2
    if lst[middle] == target:
        return True
    elif target < lst[middle]:
        return binary_search(start, middle-1, target)
    else:
        return binary_search(middle+1, end, target)

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
m = int(input())
numbers = list(map(int, input().split()))
for num in numbers:
    if binary_search(0,len(lst),num):
        print('yes', end=' ')
    else:
        print('no', end=' ')


# 반복문 이용
def binary_search(start, end, target):
    while start<=end:
        mid = (start+end)//2
        if lst[mid]==target:
            return True
        elif target < lst[mid] :
            start = mid + 1
        else:
            end = mid - 1
    return False