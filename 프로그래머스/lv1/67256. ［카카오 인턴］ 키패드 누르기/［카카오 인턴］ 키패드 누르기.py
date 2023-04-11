def solution(numbers, hand):
    answer = ''
    def level_w(n):
        if n in [1,4,7,'*']:
            return 1
        elif n in [2,5,8,0]:
            return 2
        elif n in [3,6,9,'#']:
            return 3
    def level_h(n):
        if n in [1,2,3]:
            return 1
        elif n in [4,5,6]:
            return 2
        elif n in [7,8,9]:
            return 3
        else:
            return 4
    current_left = '*'
    current_right = '#'
    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
            current_left = num
        elif num in [3,6,9]:
            answer += 'R'
            current_right = num
        else:
            left = abs(level_h(num)-level_h(current_left)) +abs(level_w(num)-level_w(current_left))
            right = abs(level_h(num)-level_h(current_right))+abs(level_w(num)-level_w(current_right))
            if left < right:
                answer +='L'
                current_left = num
            elif left > right:
                answer += 'R'
                current_right = num
            else:
                if hand=='right':
                    answer += 'R'
                    current_right = num
                else:
                    answer += 'L'
                    current_left = num
    return answer

