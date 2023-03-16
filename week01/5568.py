import sys
from itertools import permutations 


n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

perList = []

for i in range(n):
    card = str(sys.stdin.readline().rstrip())
    perList.append(card)

print(perList)
result = set()

for i in permutations(perList,k):
    result.add(' '.join(i))

print(len(result))
    



    
