import sys

input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().strip().split())))
m = int(input())
numbers = list(map(int, input().strip().split()))


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # 타겟이 없는 경우


for num in numbers:
    result = binary_search(a, num)
    if result == -1:
        print(0)
    else:
        print(1)
