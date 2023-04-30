def solution(N, stages):
    answer = []
    total = len(stages)
    tmp = []
    for i in range(N+1):
        tmp.append((i, stages.count(i)/total))
        total -= stages.count(i)
        if total==0:
            for j in range(i+1, N+1):
                tmp.append((j,0))
            break
    tmp = tmp[1:]
    tmp.sort(key=lambda x:x[1], reverse=True)
    for lst in tmp:
        answer.append(lst[0])
    return answer