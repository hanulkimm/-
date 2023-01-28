num_list = [input() for _ in range(10)]
num_list = map(int, num_list)

left = []
for i in num_list:
    left.append(i % 42)
# print(list(set(left)))
print(len(list(set(left))))