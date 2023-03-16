
a = list(map(str,input().split()))

A = a[0]
B = a[1]
A_ = list(A)
B_ = list(B)

str1 = ""
str2 = ""
for i in reversed(A_):
    str1 += i
    
for i in reversed(B_):
    str2 += i

int1 = int(str1)
int2 = int(str2)

if int1 > int2:
    print(int1)
else:
    print(int2)