# 단순하게 생각하기
# 어쩌면 당연한 얘기

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
print(lst[(n-1)//2])