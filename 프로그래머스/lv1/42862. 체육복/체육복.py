def solution(n, lost, reserve):
    r_lst = set(reserve) - set(lost)
    l_lst = set(lost) - set(reserve)
    for i in r_lst:
        if i-1 in l_lst:
            l_lst.remove(i-1)
        elif i+1 in l_lst:
            l_lst.remove(i+1)
    answer = n-len(l_lst)
    return answer