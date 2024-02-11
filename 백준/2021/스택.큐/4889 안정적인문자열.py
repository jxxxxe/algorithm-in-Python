import sys

for i in range(1,sys.maxsize):
    line=sys.stdin.readline().strip()
    if '-' in line:
        break
    stack,count=[],0
    for l in line:
        if l=='}':
            if not stack:
                stack.append("{")
                count+=1
            else:
                stack.pop()
        if l=='{':
            stack.append("{")
    count+=len(stack)//2
    print("%d. %d"%(i,count))