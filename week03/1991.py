import sys

input = sys.stdin.readline
n = int(input())
trees = {}
for i in range(n):
    root, left, right = input().strip().split()
    trees[root] = [left, right]


def preorder(start):
    if start != ".":
        print(start, end="")
        preorder(trees[start][0])
        preorder(trees[start][1])


def medianOrder(start):
    if start != ".":
        medianOrder(trees[start][0])
        print(start, end="")
        medianOrder(trees[start][1])


def lastOrder(start):
    if start != ".":
        lastOrder(trees[start][0])
        lastOrder(trees[start][1])
        print(start, end="")


preorder("A")
print()
medianOrder("A")
print()
lastOrder("A")
