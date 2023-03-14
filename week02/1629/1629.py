import sys

input = sys.stdin.readline
a, b, c = map(int, input().strip().split())


def powers(a, n):
    if n == 1:
        return a % c
    else:
        tmp = powers(a, n // 2)
        if n % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c


print(powers(a, b))
