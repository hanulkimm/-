t = int(input())
for _ in range(t):
    h,w,n= (map(int, input().split()))

    floor = n % h
    num = n // h + 1
    if n % h == 0:
        num = n//h
        floor = h

    print(num + floor * 100)
          