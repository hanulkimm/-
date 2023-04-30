def solution(dartResult):
    answer = 0
    stk = []
    dct = {'S':1, 'D':2, 'T':3}
    i = 0
    while i < len(dartResult):
    # for i in range(len(dartResult)):
        ch = dartResult[i]
        if ch in list(map(str,range(11))):
            if dartResult[i+1] in list(map(str,range(11))):
                ch += dartResult[i+1]
                i += 1
            stk.append(int(ch))
        elif ch in ('S', 'D', 'T'):
            stk[-1] **= dct[ch]
            
        else:
            if ch=='*':
                if len(stk)>1:
                    stk[-2] *= 2
                    stk[-1] *= 2 
                else:
                    stk[-1] *= 2
            else:
                
                stk[-1] *= (-1)
        i += 1

    return sum(stk)