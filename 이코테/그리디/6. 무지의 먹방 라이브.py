from heapq import heappush, heappop
def solution(food_times, k):
    answer = 0
    if sum(food_times)<=k:
        return -1
    
    hq = []
    length = len(food_times)
    for i in range(length):
        heappush(hq, (food_times[i],i+1))
    time = 0 # 직전에 다 먹은 음식 시간
    while (hq[0][0]-time)*length<=k: # 한 바퀴 다 돌릴 수 있다면
        k -= (hq[0][0]-time)*length # 시간 빼주고
        time += (hq[0][0]-time) # 다 먹은 음식 시간 더해주고
        length -= 1 # 전체 길이 줄이고
        heappop(hq) # 다 먹은 음식 빼주기
    result = sorted(hq, key = lambda x:x[1]) # index 기준으로 정렬
    answer = result[k%length][1] 
    return answer