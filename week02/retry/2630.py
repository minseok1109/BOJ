import sys

input = sys.stdin.readline
n = int(input())
papers = [list(map(int, input().strip().split())) for _ in range(n)]
blue = 0
white = 0


def countColor(x, y, n):
    global blue, white
    color = papers[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != papers[i][j]:
                countColor(x, y, n // 2)
                countColor(x, y + n // 2, n // 2)
                countColor(x + n // 2, y, n // 2)
                countColor(x + n // 2, y + n // 2, n // 2)
                return

    if color == 1:
        blue += 1
    else:
        white += 1


countColor(0, 0, n)
print(white)
print(blue)
