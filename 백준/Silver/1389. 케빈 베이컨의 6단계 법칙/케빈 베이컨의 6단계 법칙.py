import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

graph = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][k] and graph[k][j]:
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

sum_list = [sys.maxsize]
for i in range(1, n + 1):
    sum_list.append(sum(graph[i][1:n + 1]))
print(sum_list.index(min(sum_list)))