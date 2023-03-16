import sys

input = sys.stdin.readline
brackets = list(input().strip())
stack = []
for b in brackets:
    if not stack:
        stack.append(b)
    else:
        if b == "(":
            stack.append(b)
        else:
            if stack[-1] == "(":
                stack.pop()
            else:
                stack.append(b)

print(len(stack))
