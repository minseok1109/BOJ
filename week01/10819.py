import sys
from itertools import permutations

N = int(sys.stdin.readline())

A = list(map(int,sys.stdin.readline().split(sep=' ',maxsplit=N)))

ans = 0
for perm in permutations(A,N):
    sum = 0
    for i in range(1,N):
        sum += abs(perm[i]-perm[i-1])
    ans = max(ans,sum)

print(ans)