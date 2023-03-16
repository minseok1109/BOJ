import sys

N,X = map(int,sys.stdin.readline().split())


val = list(map(int,sys.stdin.readline().split(sep=' ',maxsplit=N)))
result = []
for i in val:
    if i < X:
        print(i)

