def solution(key, lock):
    answer = False
    m = len(key)
    n = len(lock)
    lock_cnt = 0
    for i in range(n):
        for j in range(n):
            if lock[i][j]==0:
                lock_cnt += 1
    p = n + (m-1)*2
    arr = [[2]*p for _ in range(p)]
    for i in range(m-1, m-1+n):
        for j in range(m-1, m-1+n):
            arr[i][j] = lock[i-(m-1)][j-(m-1)]
    # return arr
    for _ in range(4):
        new_key = [[key[j][i] for j in range(m-1,-1,-1)] for i in range(m)]
        # return new_key
        for i in range(p-m+1):
            for j in range(p-m+1):
                cnt = 0
                for ci in range(m):
                    for cj in range(m):
                        if arr[i+ci][j+cj]!=2 and arr[i+ci][j+cj]==0 and new_key[ci][cj]!=arr[i+ci][j+cj] :
                            cnt += 1
                        elif arr[i+ci][j+cj]!=2 and new_key[ci][cj]==arr[i+ci][j+cj]:
                            cnt = 1e9
                if cnt == lock_cnt:
                    answer = True
        key=new_key
    return answer