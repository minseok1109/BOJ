import sys


# 인접한 노드들의 색깔을 체크
# 아직 색이 정해지지 않았다면(None) -> 인접한 노드들의 색깔 반대로 삽입
# 인접한 노들의 색깔과 겹치게 되면 바로 NO 출력
def dfs(start, graph, check):
    for i in graph[start]:
        if check[i] == None:
            if check[start] == 1:
                check[i] = 0
                return
            else:
                check[i] = 1
                return
        dfs(i, graph, check)


input = sys.stdin.readline
k = int(input())
for _ in range(k):
    v, e = map(int, input().strip().split())
    graph = [[] for _ in range(v + 1)]
    check = [None] * (v + 1)

    for i in range(1, v):
        start, end = map(int, input().strip().split())
        graph[start].append(end)
        graph[end].append(start)

    check[1] = 1
    dfs(1, graph, check)
