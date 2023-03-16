import sys

n = int(sys.stdin.readline().rstrip())
result = []

for i in range(n):
    val = int(sys.stdin.readline().rstrip())
    result.append(val)

result.sort()

for i in result:
    print(i)
    