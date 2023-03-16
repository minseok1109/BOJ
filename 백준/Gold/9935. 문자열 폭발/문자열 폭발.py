import sys

inputs = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

stack = []

for i in range(len(inputs)):
    stack.append(inputs[i])
    if ''.join(stack[-len(bomb):]) == bomb:
        for i in range(len(bomb)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')