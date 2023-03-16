import sys

A,B,V = map(int,sys.stdin.readline().split())
x = (V-B)/(A-B)
if x == int(x):
    print(int(x))
else:
    print(int(x) + 1)