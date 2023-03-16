import sys

b = list(map(int,sys.stdin.readline().split()))
# b = list(map(int,input().split()))

def solve(a):
    ans = 0
    for i in a:
        val = int(i)
        ans += val
    return ans

print(solve(b))