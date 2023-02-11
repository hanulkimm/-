width, height = map(int, input().split())
n = int(input())

lst_garo = []
lst_sero = []
for _ in range(n):
    dr, num = map(int, input().split())
    if dr == 0: #가로로 자르는 경우
        lst_garo.append(num)
    else: # 세로로 자르는 경우
        lst_sero.append(num)

# 오름차순 정렬하기
for i in range(len(lst_garo)-1, 0, -1):
    for j in range(i):
        if lst_garo[j] > lst_garo[j+1]:
            lst_garo[j] , lst_garo[j + 1] = lst_garo[j+1], lst_garo[j]

for i in range(len(lst_sero)-1,0,-1):
    for j in range(i):
        if lst_sero[j] > lst_sero[j+1]:
            lst_sero[j] , lst_sero[j + 1] = lst_sero[j+1], lst_sero[j]

length_garo = []
length_sero = []
st = 0
for i in lst_garo:
    length_garo.append(i-st)
    st = i
length_garo.append(height-st)

st = 0
for i in lst_sero:
    length_sero.append(i-st)
    st = i
length_sero.append(width-st)

ans = 0
for i in length_garo:
    for j in length_sero:
        if ans < i * j:
            ans = i * j
print(ans)