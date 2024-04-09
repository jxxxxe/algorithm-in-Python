string=input().strip()
target=input().strip()
len_target=len(target)

stack=[]
for s in string:
    stack.append(s)
    while len(stack)>=len_target and stack[-1]==target[-1] and ''.join(stack[-len_target:])==target:
        for _ in range(len_target):
            stack.pop()

print(''.join(stack) if stack else "FRULA")