# 먼저, n 이 몇 번 째 줄인지 파악하기
n = int(input())

line = 1
while n > line:
    n -= line
    line += 1

if line % 2 == 0:
    print(f'{n}/{line-n+1}')
else:
    print(f'{line-n+1}/{n}')