def solution(n, arr1, arr2):
    answer = []
    a1 = []
    a2 = []
    for i in range(n):
        num1 = arr1[i]
        num2 = arr2[i]
        a1.append('0'*(n-len(format(num1,'b')))+ format(num1, 'b'))
        a2.append('0'*(n-len(format(num2,'b')))+ format(num2, 'b'))
    for i in range(n):
        tmp = ''
        for j in range(n):
            if a1[i][j]=='1' or a2[i][j]=='1':
                tmp += '#'
            elif a1[i][j]=='0' and a1[i][j]=='0':
                tmp += ' '
        answer.append(tmp)       
        
    return answer