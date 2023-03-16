import sys

input = sys.stdin.readline
n = int(input())
papers = [list(map(int, input().strip().split())) for _ in range(n)]

result1 = 0
result2 = 0
result3 = 0


def cal(x, y, n):
    global result1, result2, result3
    color = papers[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != papers[i][j]:
                next = n // 3
                cal(x, y, next)
                cal(x, y + next, next)
                cal(x, y + (2 * next), next)
                cal(x + next, y, next)
                cal(x + next, y + next, next)
                cal(x + next, y + 2 * (next), next)
                cal(x + (2 * next), y, next)
                cal(x + (2 * next), y + next, next)
                cal(x + (2 * next), y + (2 * next), next)
                return

    if color == -1:
        result1 += 1
        return
    elif color == 0:
        result2 += 1
        return
    else:
        result3 += 1
        return


cal(0, 0, n)

print(result1)
print(result2)
print(result3)
