import sys
N = int(input())

for _ in range(N):
    str = sys.stdin.readline().strip()
    stack = 0
    for s in str:
        if s == "(":
            stack += 1
        elif s == ")" and stack:
            stack -= 1
        else:
            print("NO")
            break
    else:
        print("NO") if stack else print("YES")