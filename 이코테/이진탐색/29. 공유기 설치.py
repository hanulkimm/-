# 공유기 사이의 거리를 조절하면서 찾기!!

n, c = map(int, input().split())
lst = [int(input()) for _ in range(n)]
lst.sort()
s, e = 1, lst[-1]-lst[0] # 최소 거리, 최대 거리
ans = 0
while s<=e:
    m = (s+e)//2
    cnt = 1
    start = lst[0]
    for i in range(1, n):
        if lst[i]>=start+m:
            start = lst[i]
            cnt += 1
    if cnt >=c: # 주어진 공유기 개수보다 많이 설치할 수 있다면
        s = m+1 # 거리 증가
        ans = m
    else:
        e = m-1 # 거리 줄이기
print(ans)