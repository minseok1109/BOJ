import sys
import heapq

n = int(sys.stdin.readline())
pq = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if not pq and num == 0:
        print(0)
    elif num == 0:
        print(heapq.heappop(pq)[1])
    heapq.heappush(pq, (-num, num))
