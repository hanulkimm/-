def solution(s):
    answer = 0
    xi = 0
    while xi < len(s):
        count_x = 1
        count_y = 0
        if xi==len(s)-1:
            answer += 1
            break
        for yi in range(xi+1, len(s)):
            if s[xi]==s[yi]:
                count_x += 1
            else:
                count_y += 1
            if count_x == count_y:
                answer += 1
                xi = yi+1
                break
            if yi == len(s)-1:
                answer += 1
                xi = yi+1

    return answer