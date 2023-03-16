import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

list = []
for i in str(b):
    list.append(i)
    
one = int(list[2])
tens = int(list[1])
hundred = int(list[0])

three = a * one
four = a * tens
five = a * hundred

result = a * b



print(three)
print(four)
print(five)
print(result)






