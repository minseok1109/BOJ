import sys

input = sys.stdin.readline
word1 = input().rstrip()
word2 = input().rstrip()
len_word1 = len(word1)
len_word2 = len(word2)
dpTable = [[0 for _ in range(len_word1 + 1)] for _ in range(len_word2 + 1)]
Max = -1e9
for i in range(1, len_word2 + 1):
    for j in range(1, len_word1 + 1):
        if word2[i - 1] == word1[j - 1]:
            dpTable[i][j] = dpTable[i - 1][j - 1] + 1
        else:
            dpTable[i][j] = max(dpTable[i - 1][j], dpTable[i][j - 1])
        Max = max(Max, dpTable[i][j])

print(Max)
