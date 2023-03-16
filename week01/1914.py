import sys
import math


def diskPrint(start,to):
    print(start,to)
    
def disk(N,start,to,via):
    if(N==1):
        diskPrint(start,to)
        return
    else:
        disk(N-1,start,via,to)
        diskPrint(start,to)
        disk(N-1,via,to,start)
        
        
N = int(sys.stdin.readline().rstrip())

num = int(math.pow(2,N))-1
if(N>20):
    print(num)
else:
    print(num)
    disk(N,1,3,2)
