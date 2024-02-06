n=input()
rb=input()

#오른쪽으로 모을 때
i=len(rb)-1
while i>0 and rb[i]==rb[i-1]:
    i-=1

right=min(rb[:i].count('R'),rb[:i].count('B'))

#왼쪽으로 모을 때
j=0
while j<len(rb)-1 and rb[j]==rb[j+1]:
    j+=1

left=min(rb[j+1:].count('R'),rb[j+1:].count('B'))

print(min(left,right))