import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
road = []
heap = []
maxi = 0
# 입력 받을 때 큰 수가 오른쪽으로 가게 정렬
for i in range(N):
    h, o = map(int, input().rstrip().split())
    if h > o:
        road.append([o, h])
    else:
        road.append([h, o])


d = int(input())
# 끝지점을 기준으로 오름차순으로 정렬
road.sort(key=lambda x: x[1])


for i in range(len(road)):
    end = road[i][1]
    start = road[i][0]

    # 시작과 끝 차이가 철로 길이보다 작으면 힙에 추가
    if end - start <= d:
        heapq.heappush(heap, start)
    else:
        continue

    while len(heap) != 0:
        tmp = heap[0]
        # 현재 비교하는 끝지점 -  힙에 있는 시작점 <= 철도길이
        if end - tmp <= d:
            break
        else:
            heapq.heappop(heap)

    # 철도길이 안에 제일 많이 포함되어 있는 길을 반환
    maxi = max(maxi, len(heap))


print(maxi)
