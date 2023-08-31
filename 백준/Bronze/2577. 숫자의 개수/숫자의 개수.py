a = int(input())
b = int(input())
c = int(input())

num = a*b*c
lst = [0] * 10
for i in str(num):
    lst[int(i)] += 1
for i in lst:
    print(i)
