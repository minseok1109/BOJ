import sys

input = sys.stdin.readline
n, m = map(int, input().strip().split())
icebergs = [list(map(int, input().strip().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
time = 0
while True:
    time += 1

    for x in range(1, n - 1):
        for y in range(1, m - 1):
            tmp_iceberg = icebergs[x][y]
            visited[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    if icebergs[nx][ny] == 0 and not visited[nx][ny]:
                        tmp_iceberg -= 1
                        if tmp_iceberg == 0:
                            break
            icebergs[x][y] = tmp_iceberg
