word = input()
word = word.lower()
alphabet = list(set(word))
rst={}
for i in alphabet:
    rst[i] = word.count(i)


sort_rst = sorted(rst.items(), key = lambda x:x[1],reverse=True)
if len(word) ==1:
    print(word.upper())
else:
    if sort_rst[0][1] == sort_rst[1][1]:
        print('?')
    else:
        anw = sort_rst[0][0]
        print(anw.upper())