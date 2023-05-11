from collections import deque
def move(pos,arr):
    candidates = []
    pos = list(pos)
    s,e = pos[0], pos[1]
    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni,nj,nx,ny = s[0]+di,s[1]+dj, e[0]+di,e[1]+dj
        if arr[ni][nj]==0 and arr[nx][ny]==0:
            candidates.append({(ni,nj),(nx,ny)})
    # 가로 방향이면
    if s[0]==e[0]:
        for i in (-1,1): # 아래, 위로 회전
            if arr[s[0] + i][s[1]] == arr[e[0] + i][e[1]] == 0:
                candidates.append({(s[0],s[1]),(s[0]+i,s[1])})
                candidates.append({(e[0],e[1]),(e[0]+i,e[1])})
    # 세로 방향이면
    else: 
        for i in (-1,1): # 왼쪽, 오른쪽으로 회전
            if arr[s[0]][s[1] + i] == arr[e[0]][e[1] + i] == 0:
                candidates.append({(s[0],s[1]),(s[0],s[1]+i)})
                candidates.append({(e[0],e[1]),(e[0],e[1]+i)})
    
    return candidates

def solution(board):
    answer = 0
    n = len(board[0])
    # 벽으로 감싸기
    arr = [[1]*(n+2)]+ [[1]+list+[1] for list in board] + [[1]*(n+2)]
    
    # deque, visited
    q = deque([({(1,1),(1,2)},0)])
    v = [((1,1),(1,2))]

    # bfs
    while q:
        pos,cnt = q.popleft()
        if (n,n) in pos:
            return cnt
        for next in move(pos,arr):
            if next not in v:
                v.append(next)
                q.append((next,cnt+1))
                # q.append((next[0],next[1],cnt+1))
        
    