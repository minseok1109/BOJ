import sys

input = sys.stdin.readline
n = int(input())
classrooms = sorted(
    [tuple(map(int, input().split())) for _ in range(n)], key=lambda x: (x[1], x[0])
)


result = [classrooms[0]]

for i in range(1, n):
    if result[-1][1] <= classrooms[i][0]:
        result.append(classrooms[i])

print(len(result))
