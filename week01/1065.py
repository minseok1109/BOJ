import sys

X = int(sys.stdin.readline())
result = 0
if X < 100:
    result = X
    print(result)
else:
    # 최종적으로 result + 99하면 될듯
    result = 99
    # X_list = result
    
    X_list = []
    for i in range(100,X+1):
        X_list.append(str(i))
    
    for i in X_list:
        number_list = []
        for j in i:
            val = int(j)
            number_list.append(val)
        if(len(number_list) == 3):
           a = number_list[1] - number_list[0]  
           b = number_list[2] - number_list[1]
           if(a == b):
               result += 1
        elif(len(number_list)== 4):
            a = number_list[3] - number_list[2]
            b = number_list[2] - number_list[1]
            c = number_list[1] - number_list[0]
            if(a==b and b==c):
                result+=1
                
                
    print(result)















