import sys


# 인접한 노드들의 색깔을 체크
# 아직 색이 정해지지 않았다면(None) -> 인접한 노드들의 색깔 반대로 삽입
def dfs(start, group):
    global error
    if not error:
        return

    visited[start] = group
    for i in graph[start]:
        if not visited[i]:
            dfs(i, -group)
        elif visited[start] == visited[i]:
            error = True
            return


input = sys.stdin.readline
k = int(input())
for _ in range(k):
    v, e = map(int, input().strip().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)
    error = False

    for i in range(1, v):
        start, end = map(int, input().strip().split())
        graph[start].append(end)
        graph[end].append(start)

    for i in range(1, v + 1):
        if not visited[i]:
            dfs(i, 1)
            if error:
                break

    if error:
        print("NO")
    else:
        print("YES")
