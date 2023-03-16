import sys

input = sys.stdin.readline
brackets = ["(", ")", "[", "]"]
while True:
    sentence = list(input().rstrip())
    temp = []
    if sentence[0] == ".":
        break
    for s in sentence:
        if s in brackets:
            if not temp:
                temp.append(s)
            else:
                if s == "(" or s == "[":
                    temp.append(s)
                elif temp[-1] == "(" and s == ")":
                    temp.pop()
                elif temp[-1] == "[" and s == "]":
                    temp.pop()
                else:
                    temp.append(s)
    if not temp:
        print("yes")
    else:
        print("no")
