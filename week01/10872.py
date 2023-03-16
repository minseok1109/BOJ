import sys

def fac(n):
    
    if n>0:
       return n * fac(n-1)
    else:
        return 1





N = int(sys.stdin.readline())
print(fac(N))
