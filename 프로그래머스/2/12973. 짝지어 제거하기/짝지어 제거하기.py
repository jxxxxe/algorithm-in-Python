def solution(s):
    stack=[]
    for st in s:
        if stack and stack[-1]==st:
            stack.pop()
        else:
            stack.append(st)

    return 0 if stack else 1