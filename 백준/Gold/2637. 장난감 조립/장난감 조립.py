import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
m = int(input())
amounts = [[] for _ in range(n + 1)]
tables = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
starts = []
for _ in range(m):
    start, end, cost = map(int, input().strip().split())
    amounts[end].append((start, cost))
    indegree[start] += 1


def solution():
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            starts.append(i)

    while q:
        now = q.popleft()
        for amount in amounts[now]:
            e, c = amount
            # 기본부품 더하기
            if indegree[now] == 0:
                if now in starts:
                    tables[e][now] = c
                else:
                    for i in range(1, n + 1):
                        tables[e][i] += tables[now][i] * c
                indegree[e] -= 1
                if indegree[e] == 0:
                    q.append(e)


solution()
for i in starts:
    print(i, tables[n][i])
