# PriorityQueue
from queue import PriorityQueue
n = int(input())
q = PriorityQueue()
for _ in range(n):
    q.put(int(input()))
ans = 0
while q.qsize()>=2:
    a = q.get()
    b = q.get()
    q.put(a+b)
    ans += a+b
print(ans)

# heap
from heapq import heappush, heappop
n = int(input())
heap = []
for _ in range(n):
    heappush(heap, int(input()))
ans = 0
if len(heap)==1:
    print(ans)
else:
    while len(heap)>=2:
        a = heappop(heap)
        b = heappop(heap)
        ans += (a+b)
        heappush(heap, a+b)
    print(ans)