n = int(input())
final = []
for _ in range(n):
    final.append(int(input()))
lst = [i for i in range(1, n + 1)]
tmp = []
ans = []
stop = ''
while final or lst:
    if tmp and tmp[-1] == final[0]:
        final.pop(0)
        tmp.pop()
        ans.append('-')

    else:
        if lst:
            tmp.append(lst[0])
            lst.pop(0)
            ans.append('+')
        else:
            ans = 'NO'
            break
if ans !='NO':
    for i in ans:
        print(i)
else:
    print(ans)

