N=int(input())

whoo=input()
stack=[]
dict={}

for w in whoo:
    if w.isupper():
        if w in dict:
            stack.append(dict[w])
        else:
            dict[w]=int(input())
            stack.append(dict[w])
        continue
    b,a=stack.pop(),stack.pop()
    if w=='+': stack.append(a+b)
    elif w=='-': stack.append(a-b)
    elif w=='*': stack.append(a*b)
    elif w=='/': stack.append(a/b)

print("%.2f"%stack[0])