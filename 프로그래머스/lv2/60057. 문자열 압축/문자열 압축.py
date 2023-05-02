def solution(s):
    n = len(s)
    answer = n
    m = n//2
    for length in range(1, m+1):
        lst = []
        for i in range(n//length):
            lst.append(s[i*length:i*length+length])
        # return lst
        stk = []
        for check in lst:
            if stk:
                if check==stk[-1][0]:
                    stk[-1][1]+=1
                else:
                    stk.append([check,1])
            else:
                stk.append([check, 1])
        # return stk
        tmp = n%length
        for lst2 in stk:
            if lst2[1]>1:
                tmp += len(lst2[0]) + len(str(lst2[1]))
            else:
                tmp += len(lst2[0])
        # return tmp
        answer = min(tmp, answer)
    return answer
    