# boj 2493 탑
# stack
import sys

N = int(sys.stdin.readline())  # 탑의 개수
top_list = list(map(int, sys.stdin.readline().strip().split()))  # 탑 리스트
stack = []
answer = []

for i in range(N):
    while stack:
        if stack[-1][1] > top_list[i]:  # 수신 가능한 상황
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:  # 스택이 비면 레이저를 수신할 탑이 없다.
        answer.append(0)
    stack.append([i, top_list[i]])  # 인덱스, 값

print(*answer)