import sys
sys.stdin = open('input.txt', 'r')

lst = list(map(int, input()))
ans = lst[0]
for num in lst[1:]:
    if ans <=1 or num<=1: # 곱하는 것보다 더하는 것이 더 큰 결과
        ans += num
    else:
        ans *= num
print(ans)
