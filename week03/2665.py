import sys
import heapq

input = sys.stdin.readline
n = int(input())
map = [list(map(int, input().strip())) for _ in range(n)]
pq = []
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0 for _ in range(n)] for _ in range(n)]
heapq.heappush(pq, [0, 0, 0])
visited[0][0] = 1


def isValid(x, y):
    return 0 <= x < n and 0 <= y < n


while pq:
    count, x, y = heapq.heappop(pq)

    if x == n - 1 and y == n - 1:
        print(count)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if isValid(nx, ny):
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                if map[nx][ny] == 0:
                    map[nx][ny] = count + 1
                    heapq.heappush(pq, [count + 1, nx, ny])
                else:
                    heapq.heappush(pq, [count, nx, ny])
