dct = {1:0, 0:1}
n = int(input())
lst = list(map(int, input().split()))
student_n = int(input())
for _ in range(student_n):
    sex, num = map(int, input().split())
    if sex == 1: # 남학생
        for i in range(n):
            if (i+1) % num == 0:
                lst[i] = dct[lst[i]]
    else: # 여학생
        lst[num-1] = dct[lst[num-1]]
        k = 1
        while True:
            if 0 <= num - 1 - k < n and 0 <= num - 1 + k < n:
                if lst[num-1-k] == lst[num-1+k]:
                    lst[num - 1 - k] = dct[lst[num-1-k]]
                    lst[num - 1 + k] = dct[lst[num-1+k]]
                    k += 1
                else:
                    break
            else:
                break
for i in range(1, n+1):
    print(lst[i-1], end = ' ')
    if i % 20 == 0:
        print()