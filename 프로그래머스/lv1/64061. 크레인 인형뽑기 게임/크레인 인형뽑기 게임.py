def solution(board, moves):
    answer = 0
    stk = []
    n = len(board)
    for move in moves:
        j = move -1
        for i in range(n):
            if board[i][j]:
                stk.append(board[i][j])
                board[i][j]=0
                break
        if len(stk)>=2:
            if stk[-1]==stk[-2]:
                stk.pop()
                stk.pop()
                answer += 2
    return answer