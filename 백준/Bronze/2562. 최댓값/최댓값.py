import sys
rst = []
for i in range(9):
    rst.append(int(sys.stdin.readline()))

for info in enumerate(rst):
    if info[1] == max(rst):
        print(info[1])
        print(info[0]+1)