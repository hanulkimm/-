
n= int(input()) # 26

cnt = 0
key = n
while True:
    a = key // 10 #2
    b = key % 10 #6
    c = (a + b) % 10 #8
    new_num = b * 10 + c

    cnt += 1

    if new_num == n:
        break
    
    key = new_num

print(cnt)
