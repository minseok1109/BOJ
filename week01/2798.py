import sys
from itertools import combinations

N,M = map(int,sys.stdin.readline().split())

cardList =  list(map(int,sys.stdin.readline().split(sep=' ',maxsplit=N)))

min = 0
idx = 0
result = 0
val = 0
for i in combinations(cardList,3):
    total = sum(i)
    if total <= M:
        comSum = total
        val = M - comSum

        
        if idx == 0:
            min = val
        else:    
            if min > val:
                min = val
                result = comSum
        idx += 1


print(result)
    