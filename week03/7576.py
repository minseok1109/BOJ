import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().strip().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
tomatos = [[0 for _ in range(N)] for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]
rip = deque([])
for i in range(M):
    row = list(map(int, input().strip().split()))
    for j in range(N):
        tomatos[i][j] = row[j]
        if row[j] == 1:
            rip.append((i, j))


def isValide(x, y):
    return 0 <= x < M and 0 <= y < N


while rip:
    x, y = rip.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if isValide(nx, ny) and tomatos[nx][ny] == 0:
            if not visited[nx][ny]:
                tomatos[nx][ny] = tomatos[x][y] + 1
                rip.append((nx, ny))

if 0 in sum(tomatos, []):
    print(-1)
else:
    print(max(sum(tomatos, [])) - 1)
