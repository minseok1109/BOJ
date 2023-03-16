import sys

a = int(sys.stdin.readline())

if a % 4 == 0 and a % 100 !=0:
    print('1')
elif a % 400 == 0:
    print('1')
else:
    print('0')