import sys

input = sys.stdin.readline
s = input().rstrip()
tokens = s.split("-")
result = 0
for i in range(len(tokens)):
    if "+" in tokens[i]:
        tokens[i] = "(" + "+".join(list(map(str, map(int, tokens[i].split("+"))))) + ")"
    else:
        tokens[i] = str(int(tokens[i]))


temp = "-".join(tokens)
result = eval(temp)
print(result)
