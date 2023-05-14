def solution(N, stages):
    answer = []
    total = len(stages)
    tmp = []
    for i in range(N+1):
        tmp.append((i, stages.count(i)/total))
        total -= stages.count(i) # 다음 스테이지 도전 인원 계산
        if total==0: # 더 이상 참여할 사람 없다면
            for j in range(i+1, N+1): # 나머지 스테이지의 실패율은 0 (도전 사람 없으니)
                tmp.append((j,0))
            break
    tmp = tmp[1:]
    tmp.sort(key=lambda x:x[1], reverse=True)
    for lst in tmp:
        answer.append(lst[0])
    return answer