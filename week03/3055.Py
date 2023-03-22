import sys

input = sys.stdin.readline
r, c = map(int, input().strip().split())
Hedgehog = None
water = []
rocks = []
map = []
bibber = None
for i in range(c):
    row = list(input().strip())
    map.append(row)
    for j in range(r):
        if row[j] == "S":
            Hedgehog = (i, j)
        elif row[j] == "*":
            water.append((i, j))
        elif row[j] == "X":
            rocks.append((i, j))
        elif row[j] == "D":
            bibber = (i, j)

print(Hedgehog, water, rocks, bibber)
