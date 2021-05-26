#연속문자열~~~

n=int(input())
list=[]

for i in range(n):
    list.append(input())
  
count=0
for word in list:
    dic=[]
    for i in range(len(word)):
        if not word[i] in dic:
            dic.append(word[i])
        elif word[i]!=word[i-1]:
            count-=1
            break
    count+=1

print(count)