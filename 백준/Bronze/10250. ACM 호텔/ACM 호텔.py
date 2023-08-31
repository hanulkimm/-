t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    # n%h==0 일때 아닐때
    if n%h==0:
        floor = h
        room = n//h
    else:
        floor = n%h
        room = n//h+1
    
    if room<10:
        ans = str(floor) + str('0') + str(room)
    else:
        ans = str(floor) + str(room)
    print(ans)
