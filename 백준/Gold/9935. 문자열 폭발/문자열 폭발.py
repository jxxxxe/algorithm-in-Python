string=input().strip()
target=input().strip()
len_target=len(target)

stack=[]
for s in string:
    stack.append(s)
    if s==target[-1] and stack[-len_target:]==list(target):
        for _ in range(len_target):
            stack.pop()

print(''.join(stack) if stack else "FRULA")