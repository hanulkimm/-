def solution(X, Y):
    answer = ''
    cntx = [0] * 10  # 0~9
    cnty = [0] * 10 # 0~9
    for i in range(len(X)):
        cntx[int(X[i])] += 1
    for i in range(len(Y)):
        cnty[int(Y[i])] += 1
    for j in range(9, -1, -1):
        if cntx[j] and cnty[j]:
            if j==0 and len(answer)==0:
                answer='0'
            else:
                answer += str(j) * min(cntx[j], cnty[j])
    if len(answer):
        pass
    else:
        answer = "-1"
    return answer
