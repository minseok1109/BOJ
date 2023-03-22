import sys

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
print(graph)
