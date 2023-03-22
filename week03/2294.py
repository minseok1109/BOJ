from collections import deque
import sys

# sys.stdin = open("답체크.txt","r")
input = sys.stdin.readline

n, value = map(int, input().split())
coins = list(set(int(input()) for _ in range(n)))
check = [0 for _ in range(value + 1)]  ### 중복된 조합 filter해서 빼주는 효과가 있음// 없으면 메모리 초과난다 ..!


def bfs(coins, total_value):
    queue = deque()
    for coin in coins:
        if coin < total_value:
            queue.append([coin, 1])
            check[coin] = 1

    while queue:
        now_value, cnt = queue.popleft()
        if total_value == now_value:
            print(cnt)
            break
        for coin in coins:
            check_sum = now_value + coin
            total_cnt = cnt + 1
            if check_sum > total_value:
                continue
            elif check_sum <= total_value and check[check_sum] == 0:
                check[check_sum] = 1
                queue.append([check_sum, total_cnt])

    if now_value != total_value:
        print("-1")


bfs(coins, value)
