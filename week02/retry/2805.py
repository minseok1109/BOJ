import sys

input = sys.stdin.readline
n, m = map(int, input().strip().split())
trees = sorted(list(map(int, input().strip().split())))

start = trees[0]
end = trees[-1]

while start <= end:
    mid = (start + end) // 2

    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid

    if total >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
