def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer =''
    for i in range(len(completion)):
        if participant[i]!=completion[i]:
            answer = participant[i]
            break
    if answer:
        pass
    else:
        answer = participant[-1]

    return answer