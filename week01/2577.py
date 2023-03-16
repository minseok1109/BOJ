import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

result = A * B * C
a = str(result)
b = list(a)

idx = 0
while idx < 10:
    cnt = 0
    for i in b:
       idx_ = int(i)
       if idx_ == idx:
            cnt += 1

    idx += 1
    print(cnt)

