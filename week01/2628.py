import sys

n = list(map(int,sys.stdin.readline().split()))

# 가로
row = int(n[0])

# 세로
column = int(n[1])

# 잘라야하는 점선의 개수
T = int(sys.stdin.readline())
r = [0,row]
c = [0,column]

# 각 리스트에 값 넣기
for i in range(T):
    area = list(map(int,sys.stdin.readline().split()))
    if(area[0] == 0):
        n = int(area[1])
        c.append(n)
    else:
        m = int(area[1])
        r.append(m)

# 각 리스트 내의 중복 값 제거
rowList = list(dict.fromkeys(r))
columnList = list(dict.fromkeys(c))



# 오름차순으로 정렬
rowList.sort()
columnList.sort()
resultList = []

for i in range(len(rowList)-1):
    rL = rowList[i:i+2]
    for j in range(len(columnList)-1):
        cL = columnList[j:j+2]
        n = (rL[1]-rL[0])*(cL[1]-cL[0])
        resultList.append(n)
result = max(resultList)
        

print(result)
        

