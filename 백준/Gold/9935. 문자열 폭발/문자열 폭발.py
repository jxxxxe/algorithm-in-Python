string=input().strip()
target=input().strip()
len_target=len(target)

stack=[]
for s in string:
    stack.append(s)
    if s==target[-1] and stack[-len_target:]==list(target):
        del stack[-len_target:]

print(''.join(stack) if stack else "FRULA")