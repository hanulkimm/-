def solution(n, weak, dist):
    from itertools import permutations
    answer = len(dist) + 1
    weak_num = len(weak)
    
    for i in range(weak_num):
        weak.append(weak[i]+n) # 선형으로 표현하기
    dist_lst = list(permutations(dist, len(dist)))
    # return dist_lst
    for i in range(weak_num):
        weak_tmp = [weak[j] for j in range(i,i+weak_num)]
        for dist_tmp in dist_lst:
            tmp = 1 
            ppl = 0
            move = weak_tmp[0] + dist_tmp[ppl]
            for k in range(1,weak_num):
                if weak_tmp[k] > move:
                    tmp += 1
                    if tmp>len(dist_tmp):
                        break
                    ppl += 1
                    move = weak_tmp[k] + dist_tmp[ppl]
            answer = min(answer, tmp)
    if answer > len(dist):
        answer  =-1
            
            
    return answer