import sys

a, b, c = map(int, input().strip().split())


def cal(a, b, c):
    if b == 1:
        return a % c

    tmp = cal(a, b // 2, c)
    if b % 2 == 0:
        return (tmp * tmp) % c
    else:
        return (tmp * tmp * a) % c


print(cal(a, b, c))
