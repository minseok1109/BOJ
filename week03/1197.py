import sys

## 사이클론을 형성하는지 체크
# 형성안한다면 n-1까지 담기
# 반복


#부모가 갱신되면 연결되있던 노드들의 부모가 자동으로 한번에 갱신되는게 아니라
# 해당 노드가 다시 부모를 찾을 일이 있으면 부모를 타고타고 가서 확인 후 갱신
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


input = sys.stdin.readline
v, e = map(int, input().strip().split())
graph = []
for _ in range(e):
    a, b, cost = map(int, input().strip().split())
    graph.append((a, b, cost))

parents = [0] * (v + 1)
for i in range(1, v + 1):
    parents[i] = i
graph.sort(key=lambda x: x[2])

total_cost = 0

for i in range(e):
    a, b, cost = graph[i]
    if find_parent(parents, a) != find_parent(parents, b):
        union(parents, a, b)
        total_cost += cost

print(total_cost)
