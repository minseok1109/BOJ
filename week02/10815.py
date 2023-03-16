import sys
from bisect import bisect_left, bisect_right


def countNumber(li, n):
    rt = bisect_right(li, n)
    lt = bisect_left(li, n)
    return rt - lt


input = sys.stdin.readline
n = int(input())
cards = sorted(list(map(int, input().strip().split())))
m = int(input())
numbers = list(map(int, input().strip().split()))

for num in numbers:
    print(countNumber(cards, num), end=" ")
