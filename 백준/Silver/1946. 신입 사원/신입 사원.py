import sys

input = sys.stdin.readline
answer = []
T = int(input())
for _ in range(T):
    result = 1
    n = int(input())
    scores = sorted(
        [tuple(map(int, input().split())) for _ in range(n)], key=lambda x: x[0]
    )

    top = scores[0]
    for i in range(1, n):
        if (top[0] < scores[i][0]) ^ (top[1] < scores[i][1]):
            result += 1
            top = scores[i]
            continue

    answer.append(result)

for i in answer:
    print(i)
