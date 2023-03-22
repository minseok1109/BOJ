import sys


def dfs(arr, n):
    global count
    for i in arr[n]:
        if not visited[i]:
            visited[i] = True
            count += 1
            dfs(arr, i)


input = sys.stdin.readline
n, m = map(int, input().split())
big = [[] for _ in range(n + 1)]
small = [[] for _ in range(n + 1)]
# 전체 개수의 반을 중간으로 설정
mid = (n + 1) / 2

# 자기보다 크고 작은것을 인접리스트를 활용해 나타냄
for _ in range(m):
    bigger, smaller = map(int, input().split())
    big[bigger].append(smaller)
    small[smaller].append(bigger)


answer = 0
# 전체 다 반복문을 돌면서 자기 보다 큰 거, 작은거, 개수를 세서 중간값보다 크거나 같으면
# 정답에 1추가
for i in range(1, n + 1):
    visited = [False for _ in range(n + 1)]
    count = 0
    dfs(big, i)
    if count >= mid:
        answer += 1
    count = 0
    dfs(small, i)
    if count >= mid:
        answer += 1

print(answer)
