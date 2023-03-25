import sys

input = sys.stdin.readline
N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (1 << N - 1) for _ in range(N)]


def solution(i, route):
    if dp[i][route] != 0:
        return dp[i][route]

    # 현재까지 방문한 도시의 집합(route)이 모든 도시를 방문한 집합(2^(N-1) - 1)과 같은지를 판별하는 조건문
    if route == (1 << (N - 1)) - 1:
        if W[i][0]:
            return W[i][0]
        else:
            return float("inf")

    min_dist = float("inf")
    for j in range(1, N):
        if not W[i][j]:
            continue
        # 비트마스크(route)를 활용하여 j번째 도시를 방문했으면 1
        # 안했으면 0
        if route & (1 << j - 1):
            continue
        dist = W[i][j] + solution(j, route | (1 << (j - 1)))
        if min_dist > dist:
            min_dist = dist
    dp[i][route] = min_dist

    return min_dist


print(solution(0, 0))
