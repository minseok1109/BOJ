import sys

input = sys.stdin.readline
n = int(input())
k = int(input())


def makeMatrix(n):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = (i + 1) * (j + 1)
    return sorted(sum(result, []))


b = makeMatrix(n)
