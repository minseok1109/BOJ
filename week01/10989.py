import sys

N = int(sys.stdin.readline())

Nlist = [0]*10001

for i in range(N):
    a = int(sys.stdin.readline())
    Nlist[a] = Nlist[a] + 1

for i in range(10001):
    if Nlist[i] != 0:
        for j in range(Nlist[i]):
            print(i)