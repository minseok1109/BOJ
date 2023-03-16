import sys

N = int(sys.stdin.readline())

alphabet = [str(sys.stdin.readline().strip()) for i in range(N)]
alphabet.sort()
alphabet.sort(key=len)
result = dict.fromkeys(alphabet)

for i in result:
    print(i)