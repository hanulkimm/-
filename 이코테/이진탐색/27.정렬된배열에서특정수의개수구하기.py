from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
lst = list(map(int, input().split()))
right = bisect_right(lst, x)
left = bisect_left(lst, x)
if right-left:
    print(right-left)
else:
    print(-1)
