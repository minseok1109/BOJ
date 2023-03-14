import sys

n = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().strip().split()))

answer = []

while towers:
    flag = 0  # 자기보다 큰 탑 찾았는지 표시용
    tower = towers.pop()  # 뒤에 있는 탑을 하나 빼와서
    # 뒤에서부터 큰 탑 있는지 비교
    for t in range(len(towers) - 1, -1, -1):
        # 큰 탑을 찾으면 그 탑의 인덱스 + 1 출력하고 break
        if towers[t] > tower:
            print(t + 1, end=' ')
            flag = 1
            break
    ## 큰 건물을 하나도 못찾으면 0출력 하고 break
    if flag == 0:
        print(0, end=' ')

##문제는 이거를 어떻게 거꾸로 출력하지??
