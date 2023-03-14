import sys
from collections import deque
n, k = map(int, sys.stdin.readline().strip().split())
people = deque([i for i in range(1, n+1)])

answer = []
while people:
    for _ in range(k-1):
        tmp = people.popleft()
        people.append(tmp)
    answer.append(people.popleft())

formatted_list = '<{}>'.format(', '.join(map(str, answer)))
print(formatted_list)









