import sys

n, k = map(int, sys.stdin.readline().strip().split())
numbers = list(sys.stdin.readline().strip())

stack = []
for i in range(len(numbers)):
    now = numbers[i]
    while k > 0 and stack and stack[-1] < now:
        stack.pop()
        k -= 1 #K개만큼 지워야한다.
    stack.append(now) #k개 지우고 난 다음 나머지는 일단 append

stack = stack[:len(stack) - k]#여기서 k개만큼 지운수 출력

print(''.join(stack))
