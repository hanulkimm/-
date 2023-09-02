l = int(input())
lst = list(input())
sm = 0
for i in range(len(lst)):
    sm += (ord(lst[i])-96) * (31 ** i)
print(sm%1234567891)