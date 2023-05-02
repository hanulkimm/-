s = input()
num = 0
string = []
for ch in s:
    if ch.isdigit():
        num += int(ch)
    else:
        string.append(ch)

string.sort()
string.append(str(num))
print(''.join(string))
