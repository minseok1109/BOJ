import sys

input = sys.stdin.readline

n, k = map(int, input().split())
levels = [int(input()) for _ in range(n)]

start = min(levels)
end = start + k

res = 0
while start <= end:
    mid = (start + end) // 2

    total = 0
    # mid값과 레벨의 차이를 다 더함
    for level in levels:
        if mid > level:
            total += mid - level

    if total <= k:
        # mid가 찾는 최댓값
        start = mid + 1
        res = max(mid, res)
    else:
        end = mid - 1


print(res)
