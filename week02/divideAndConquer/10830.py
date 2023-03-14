import sys

input = sys.stdin.readline
n, b = map(int, input().strip().split())
matrix = [list(map(int, input().strip().split())) for _ in range(n)]


def matrixSquared(n, matrix1, matrix2):
    result = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= 1000
    return result


def powers(n, matrix, b):
    if b == 1:
        return matrix
    elif b == 2:
        return matrixSquared(n, matrix, matrix)
    else:
        tmp = powers(n, matrix, b // 2)
        if b % 2 == 0:
            return matrixSquared(n, tmp, tmp)
        else:
            return matrixSquared(n, matrixSquared(n, tmp, tmp), matrix)


result = powers(n, matrix, b)
for row in result:
    for num in row:
        print(num % 1000, end=" ")
    print()
