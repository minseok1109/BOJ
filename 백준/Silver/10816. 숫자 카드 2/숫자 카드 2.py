import sys
from bisect import bisect_left, bisect_right


def countNumber(li, num):
    rt = bisect_right(li, num)
    lt = bisect_left(li, num)
    return rt - lt


input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().strip().split()))
m = int(input())
numbers = list(map(int, input().strip().split()))
sorted_cards = sorted(cards)
for num in numbers:
    print(countNumber(sorted_cards, num), end=" ")
