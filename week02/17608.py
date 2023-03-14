import sys

n = int(sys.stdin.readline())
sticks = [int(sys.stdin.readline()) for _ in range(n)]
cnt = 1
Max = sticks[-1]
for i in range(len(sticks)-1,-1,-1):
    if sticks[i] > Max:
        Max = sticks[i]
        cnt += 1


print(cnt)
