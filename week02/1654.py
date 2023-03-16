import sys

input = sys.stdin.readline
k, n = map(int, input().strip().split())
lans = [int(input().strip()) for _ in range(k)]
start = 0
end = max(lans)

result = 0
while start < end:
    mid = (start + end) // 2

    count = 0
    for lan in lans:
        if mid <= lan:
            count += lan // mid

    if count >= n:
        result = max(mid, result)
        start = mid + 1
    else:
        end = mid - 1

print(result)
