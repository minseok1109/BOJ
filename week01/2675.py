T = int(input())

for j in range(T):
    P = input().split()
    R = int(P[0])
    S = P[1]
    for i in S:
        print(i*R,end='')
    print()