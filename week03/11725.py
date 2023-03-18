import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
parents = [0] * (n + 1)
for _ in range(1, n):
    start, end = map(int, input().strip().split())
    graph[start].append(end)
    graph[end].append(start)


# visited배열 대신 parents 배열이 그 역할을 대신함
# true를 삽입하는 게 아니라 그 해당 재귀를 시작한 start를 삽입
def dfs(start, graph, parents):
    for i in graph[start]:
        if not parents[i]:
            parents[i] = start
            dfs(i, graph, parents)


dfs(1, graph, parents)
for i in range(2, n + 1):
    print(parents[i])
