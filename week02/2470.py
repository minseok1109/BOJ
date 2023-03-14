import sys

input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))

start = 0
end = len(arr) - 1

min = sys.maxsize
while start < end:
    # 두 용액을 합침
    calc = arr[start] + arr[end]
    # 두 용액의 합의 절댓값과 최솟값을 비교
    if abs(calc) < min:
        min = abs(calc)
        answer = arr[start], arr[end]
    if calc == 0:
        break

    # calc값이 음수면 start 1증가
    if calc < 0:
        start += 1
    # calc값이 음수면 end -1 감소
    else:
        end -= 1

print(*answer)
