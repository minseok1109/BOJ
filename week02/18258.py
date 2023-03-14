from collections import deque
import sys
input = sys.stdin.readline


n = int(input())

orders = [list(input().strip().split()) for _ in range(n)]

queue = deque([])
for order in orders:
    if order[0] == 'push':
        queue.append((order[1]))
    elif order[0] =='pop':
        if len(queue) == 0:
            print(-1)
        else:
            tmp = queue.popleft()
            print(tmp)
    elif order[0] =='size':
        print(queue.__len__())
    elif order[0] =='empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order[0] =='front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif order[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue)-1])