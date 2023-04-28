from heapq import heappush, heappop
def solution(food_times, k):
    answer = 0
    if sum(food_times)<=k:
        return -1
    
    hq = []
    length = len(food_times)
    for i in range(length):
        heappush(hq, (food_times[i],i+1))
    time = 0
    while (hq[0][0]-time)*length<=k:
        k -= (hq[0][0]-time)*length
        time += (hq[0][0]-time)
        length -= 1
        heappop(hq)
    result = sorted(hq, key = lambda x:x[1])
    answer = result[k%length][1]
    return answer