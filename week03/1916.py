import sys
import heapq

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end, cost = map(int, input().strip().split())
    graph[start].append((cost, end))


start, end = map(int, input().strip().split())


def daiksta(graph, start, result_end):
    pq = [(0, start)]
    distances = [float("inf") for _ in range(n + 1)]
    distances[start] = 0

    while pq:
        pre_cost, pre_end = heapq.heappop(pq)

        if distances[pre_end] < pre_cost:
            continue

        for cost, end in graph[pre_end]:
            calc = pre_cost + cost

            if calc < distances[end]:
                distances[end] = calc
                heapq.heappush(pq, (calc, end))
    return distances[result_end]


print((daiksta(graph, start, end)))
