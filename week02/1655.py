import heapq
import sys

N = int(sys.stdin.readline())

leftHeap = [] #최대 힙
rightHeap = [] #최소 힙
answer = []
for i in range(N):
    inputNum = int(sys.stdin.readline())

    if len(leftHeap) == len(rightHeap): #길이가 같으면 최대힙으로
        heapq.heappush(leftHeap, (-inputNum, inputNum))
    else: #다르다면 최소힙으로
        heapq.heappush(rightHeap, (inputNum, inputNum))

    #최대힙의 루트값이 최소힙의 루트값보다 크다면 둘이 교환
    if rightHeap and leftHeap[0][1] > rightHeap[0][1]:
        min_ = heapq.heappop(rightHeap)[1]
        max_ = heapq.heappop(leftHeap)[1]
        heapq.heappush(leftHeap, (-min_, min_))
        heapq.heappush(rightHeap, (max_, max_))

    answer.append(leftHeap[0][1])

print(*answer)