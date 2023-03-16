import sys

input = sys.stdin.readline

n, b = map(int, input().strip().split())
matrix = [list(map(int, input().strip().split())) for _ in range(n)]


def multi(n, matrix1, matrix2):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def cal(n, matrix, b):
    if b == 1:
        return matrix

    # matrix ^ 2
    tmp = cal(n, matrix, b // 2)
    if b % 2 == 0:
        return multi(n, tmp, tmp)
    else:
        return multi(n, multi(n, tmp, tmp), matrix)


result = cal(n, matrix, b)
for row in result:
    for r in row:
        print(r % 1000, end=" ")
    print()
