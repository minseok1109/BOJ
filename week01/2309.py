import sys
from itertools import combinations

nan = []
sum = 0
substract = 0

idx = 1
while(1):
    val = int(sys.stdin.readline().rstrip())
    if val < 100:
        nan.append(val)
        sum += val
        idx += 1

    if idx == 10:
        break

substract = sum - 100

for i in combinations(nan,2):
    sum = i[0] + i[1]
    if sum == substract:
        nan.remove(i[0])
        nan.remove(i[1])
        break


nan.sort()

for i in nan:
    print(i)



