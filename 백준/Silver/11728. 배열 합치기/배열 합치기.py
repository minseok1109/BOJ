import sys

input = sys.stdin.readline
n, m = map(int, input().strip().split())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

answer = []
i = j = 0

while i < n and j < m:
    if A[i] < B[j]:
        answer.append(A[i])
        i += 1
    else:
        answer.append(B[j])
        j += 1

if i < n:
    answer.extend(A[i:])
else:
    answer.extend(B[j:])

print(*answer)
