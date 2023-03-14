import sys

n = int(sys.stdin.readline())

orders = [list(sys.stdin.readline().strip().split()) for _ in range(n)]

stack = []
for order in orders:
    if order[0] =='push':
        stack.append((order[1]))
    elif order[0] =='pop':
        if len(stack) == 0:
            print(-1)
        else:
            tmp = stack.pop()
            print(tmp)
    elif order[0] =='size':
        print(len(stack))
    elif order[0] =='empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order[0] =='top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])