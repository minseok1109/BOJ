# 미로만들기 - 다익스트라 <= 시간 초과의 늪에 빠짐...
"""
다익스트라 알고리즘으로 최소 경로를 찾아가면서
검은 방이 몇 개인지 탐색
* 검은 방의 우선순위를 낮게 하여 heap에서 꺼내올 때 가장 나중에 선택되도록
"""
import sys
import heapq

N = int(sys.stdin.readline())
rooms = []
for _ in range(N):
    rooms.append(list(map(int, sys.stdin.readline().rstrip())))

mx = [0, 1, 0, -1]
my = [-1, 0, 1, 0]

"""
visited = [[0] * (N+1)] * (N+1) 
🚨 위의 코드에서 *연산자는 새로운 객체를 생성하지 않고, 기존 객체를 참조
visited[0][0]에 값을 할당하면 visited[1][0], visited[2][0], ...에도 같은 값이 할당됨
"""
visited = [[0] * N for _ in range(N)]


def dijkstra(startx, starty):
    q = []
    heapq.heappush(q, (0, startx, starty))
    while q:
        count, x, y = heapq.heappop(q)
        # print("지금 팝:", count, x, y)
        if x == (N - 1) and y == (N - 1):
            return count

        for i in range(4):
            tempx = x + mx[i]
            tempy = y + my[i]
            if 0 <= tempx < N and 0 <= tempy < N and visited[tempx][tempy] == 0:
                visited[tempx][tempy] = 1
                # print(tempx, tempy, "방 확인:", rooms[tempx][tempy])
                if (rooms[tempx][tempy]) == 1:
                    ## 🚨 최소 경로를 찾기 위해서 count를 저장해줌
                    heapq.heappush(q, (count, tempx, tempy))
                else:
                    ## 🚨 최소 경로를 찾을 때 검은 방은 우선 순위에서 뒤로 가야 하므로 count에 1을 더함
                    heapq.heappush(q, (count + 1, tempx, tempy))


print(dijkstra(0, 0))
