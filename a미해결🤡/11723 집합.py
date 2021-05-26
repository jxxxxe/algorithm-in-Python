#set() / set(리스트) 
import sys

N=int(input())

jibhab=set()
for _ in range(N):
    line=sys.stdin.readline().strip().split()
    if len(line)==1:    operator=line[0]
    else:    operator,x=line[0],line[1]

    if operator=='add':
        jibhab.add(x)
    elif operator=='remove':
        jibhab.discard(x)
    elif operator=='check':
        print(int(x in jibhab))
    elif operator=='toggle':
        if x in jibhab:
            jibhab.remove(x)
        else:
            jibhab.add(x)
    elif operator=='all':
        jibhab=set([str(i) for i in range(1,21)])
    elif operator=='empty':
        jibhab=set()