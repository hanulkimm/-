def solution(babbling):
    lst = ["aya", "ye", "woo", "ma"]
    dct = {}
    mx = 0
    for word in babbling:
        dct[word] = 0
        mx = max(mx, len(word))

    def dfs(st, used):  # 문자열, 바로 이전에 사용 문자열
        if len(st) > mx:
            return
        if st in babbling:
            dct[st] = babbling.count(st)
        for word in lst:
            if word != used:
                dfs(st + word, word)

    dfs('', '')
    answer = sum(dct.values())
    return answer