def solution(number, limit, power):
    answer = 1
    for num in range(2, number + 1):
        tmp = 0
        for i in range(1, int(num ** (1 / 2)) + 1):
            if num / i == i:
                tmp += 1
            elif num % i == 0:
                tmp += 2


        if tmp > limit:
            answer += power
        else:
            answer += tmp

    return answer