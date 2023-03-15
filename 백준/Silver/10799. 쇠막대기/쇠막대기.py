import sys

input = sys.stdin.readline
brackets = list(input().strip())


stack = []
answer = 0
for i in range(len(brackets)):
    if brackets[i] == "(":
        stack.append(brackets[i])
    else:
        stack.pop()
        if brackets[i - 1] == "(":
            answer += len(stack)
        else:
            answer += 1

print(answer)
