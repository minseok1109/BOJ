import sys
from collections import deque

input = sys.stdin.readline
# 다른 사람의 코드
n, w, l = map(int, input().strip().split())
trucks = deque(list(map(int, input().strip().split())))

bridge = deque([0] * w)
time = 0

while bridge:
    time += 1
    bridge.popleft()
    if trucks:
        if sum(bridge) + trucks[0] <= l:
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)
print(time)
