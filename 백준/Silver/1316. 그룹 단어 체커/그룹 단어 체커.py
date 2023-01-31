n = int(input())
lst = [input() for _ in range(n)]
cnt = n
for word in lst:
    for i in range(0,len(word)-1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+2:]:
            cnt -= 1
            break
print(cnt)