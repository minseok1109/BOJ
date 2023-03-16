import sys

T = int(sys.stdin.readline())


for i in range(T):
    data = input()
    data_list = list(data)
    result = 0
    sum = 0
    index = 0
    for j in data_list:
        if data_list[index] == 'O':
            result += 1
            sum += result
        else:
            result = 0
        index += 1
    print(sum)

