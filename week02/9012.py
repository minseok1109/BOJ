import sys

n = int(sys.stdin.readline())
ps = [list(sys.stdin.readline().strip()) for _ in range(n)]


for item in ps:
    stack = []
    for string in item:
        if string == '(':
            stack.append(string)
        elif string == ')' and len(stack) == 0:
            stack.append(string)
            break
        else:
            stack.pop()
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')