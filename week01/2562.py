import sys

max = 0
index = 0
for i in range(9):
    val = int(sys.stdin.readline())
    if max < val:
        max = val 
        index = i+1

print(max)
print(index)