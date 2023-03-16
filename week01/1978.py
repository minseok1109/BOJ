import sys

N = int(sys.stdin.readline())

primeNumber = list(map(int,sys.stdin.readline().split(maxsplit=N)))
cnt = 0
for i in primeNumber:
    if i != 1:
        resultCnt = 0

        for j in range(1,i):
            if i % j == 0:
                resultCnt += 1
        if resultCnt < 2:
            cnt += 1

print(cnt)
            
            
            