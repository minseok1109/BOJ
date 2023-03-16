import sys
import math
C = int(sys.stdin.readline())

for i in range(C):
    N = list(map(int,input().split()))
    result = 0
    total = 0
    first = int(N[0])
    for j in N:
        total += j
    total_ = total - first
    avg = total_ / first
    #print('avg : ',avg)
    
    cnt = 0
    idx = 0
    for k in N:
        if idx != 0:
            if k > avg:
                cnt += 1 
        idx += 1
    
    result = (cnt/first*100.0)
    #print(result)
    
    real_result = '%.3f%%'%result
    print(real_result)