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
