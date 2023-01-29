word = input()
alphabet = list(map(chr,range(97,123)))
rst = []
for i in alphabet:
    rst.append(word.find(i))
print(*rst)