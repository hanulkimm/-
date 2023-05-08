# [1] 분리하는 기준되는 index 구하기
def split_idx(p):
        cnt = 0
        for i in range(len(p)):
            if p[i]=='(':
                cnt += 1
            else:
                cnt -= 1
            if cnt==0:
                return i
# [2] 올바른 괄호 문자열 판별
def right(st):
    cnt = 0
    for ch in st:
        if ch=='(':
            cnt += 1
        else:
            cnt -=1
        if cnt < 0:
            return False
    return True
    
def solution(p):
    answer = ''
    if p=='':
        return answer
    dct = {"(":")", ")":"("}
    
    idx = split_idx(p)
    u = p[:idx+1]
    v = p[idx+1:]
    if right(u):
        answer += u + solution(v)
    else:
        tmp = '('
        tmp += solution(v)
        tmp += ')'
        for ch in u[1:-1]:
            tmp += dct[ch]
        answer += tmp
    return answer