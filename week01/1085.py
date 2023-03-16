import sys

a,b,c,d = map(int,sys.stdin.readline().split())
# a = x , b = y , c = w , d = h

#1) x축 기준
R1 = c - a
R2 = a

#2) y축 기준
R3 = d - b
R4 = b

result = min(R1,R2,R3,R4)

print(result)