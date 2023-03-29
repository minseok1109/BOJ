import sys

input = sys.stdin.readline
find_word = input().rstrip()
word = input().rstrip()
count = 0
k = 0
while k <= len(find_word) - len(word):
    if find_word[k : k + len(word)] == word:
        count += 1
        k += len(word)
    else:
        k += 1
print(count)
