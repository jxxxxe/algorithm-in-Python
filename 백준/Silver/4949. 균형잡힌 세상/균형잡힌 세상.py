import sys

while True:
    line = sys.stdin.readline().rstrip()
    if line == ".":
        break

    stack = []

    for l in line:
        if l == "(":
            stack.append(')')
        elif l == "[":
            stack.append(']')
        elif l == ")" or l == "]":
            if stack and stack[-1] == l:
                stack.pop()
            else:
                print("no")
                break
    else:
        print("no") if stack else print("yes")