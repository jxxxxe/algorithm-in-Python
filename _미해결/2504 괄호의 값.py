def check(t,score):
    if type(stack[-1])==int:
        if stack[-2]==t:
            num=stack.pop()
            stack[-1]=score*num
            if type(stack[-2])==int:
                num=stack.pop()
                stack[-1]+=num
            return 1
    if stack[-1]==t:
            stack.pop()
            stack.append(score)
            return 1
    return 0

X,stack=input(),[]

for x in X:
    if x=='(':
        stack.append('(')
    elif x=='[':
        stack.append('[')
    elif x==')':
        if not check('(',2):
            exit()
    elif x==']':
        if not check('[',3):
            exit()

if len(stack)==1 and type(stack[-1])==int:
    print(stack.pop())
else:
    print(0)