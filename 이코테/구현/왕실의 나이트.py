s = input()
i = int(s[1])-1
j = int(ord(s[0])-ord('a'))
ans = 0
for di,dj in ((1, 2), (1, -2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)):
    ni,nj = i+di, j+dj
    if 0<=ni<8 and 0<=nj<8:
        ans += 1
print(ans)