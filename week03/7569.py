import sys
from collections import deque

input = sys.stdin.readline
M, N, H = map(int, input().split())
Max = 0
# 3차원 배열 초기화
boxes = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
dh = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
# 익은 토마토 위치 초기화
ripe_tomatoes = deque([])

# 입력 받기
for i in range(H):
    for j in range(N):
        row = list(map(int, input().split()))
        for k in range(M):
            boxes[i][j][k] = row[k]
            if row[k] == 1:
                ripe_tomatoes.append((i, j, k))


while ripe_tomatoes:
    h, n, m = ripe_tomatoes.popleft()

    for i in range(6):
        th = h + dh[i]
        ty = n + dy[i]
        tx = m + dx[i]

        if 0 <= th < H and 0 <= ty < N and 0 <= tx < M:
            if boxes[th][ty][tx] == 0:
                boxes[th][ty][tx] = boxes[h][n][m] + 1
                Max = max(Max, boxes[th][ty][tx])
                ripe_tomatoes.append((th, ty, tx))

if 0 in sum(sum(boxes, []), []):
    print(-1)
elif Max == 0:
    print(0)
else:
    print(Max - 1)
