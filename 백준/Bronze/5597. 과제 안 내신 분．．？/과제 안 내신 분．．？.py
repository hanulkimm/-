num_list = [input() for _ in range(28)]
num_list = map(int, num_list)
full = list(range(1,31))


for i in num_list:
    full.remove(i)
full.sort()
print(full[0])
print(full[1])