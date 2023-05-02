s = input()
n = len(s)
if sum(map(int, s[:int(n/2)]))==sum(map(int, s[int(n/2):])):
    print('LUCKY')
else:
    print('READY')