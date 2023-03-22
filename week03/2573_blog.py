import sys

sys.setrecursionlimit(10**5)


def dfs(x, y):  # 2가지 경우로 나뉘는걸 체크해주기 위한 함수.
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:
            visited[nx][ny] = False
            if icebergs[nx][ny] != 0:
                dfs(nx, ny)


input = sys.stdin.readline
n, m = map(int, input().split())
icebergs = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False] * m for _ in range(n)]  # 방문 체크
time = 0

while True:
    time += 1
    for x in range(1, n - 1):  # 빙하를 녹이는 함수
        for y in range(1, m - 1):
            if icebergs[x][y] != 0:
                visited[x][y] = True  # 앞서 말한 경우를 방지해주기 위한 작업
                iceberg = icebergs[x][y]
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                        if icebergs[nx][ny] == 0:
                            iceberg -= 1
                            if iceberg == 0:  # 음수가 되면 안 되니 dfs작업을 멈춰준다.
                                break
                icebergs[x][y] = iceberg  # 녹은 빙하를 저장해줌

    ch = 0  # 영역의 개수
    for x in range(1, n - 1):
        for y in range(1, m - 1):  # 방문체크 배열을 재사용하기 위해 True->False로 다 고쳐준다.
            if icebergs[x][y] != 0 and visited[x][y]:
                dfs(x, y)  # 영역을 체크한다.
                ch += 1
            elif icebergs[x][y] == 0 and visited[x][y]:
                visited[x][y] = False

    if ch >= 2:  # 영역이 2개 이상으로 나뉜경우니 출력해주고 반복문을 탈출한다.
        print(time)
        break
    elif ch == 0:  # 한번에 녹았다는 의미이므로 0을 출력해주고 반복문을 탈출한다.
        print(0)
        break
