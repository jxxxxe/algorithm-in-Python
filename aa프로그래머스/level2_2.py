people=sorted([50,50,50,50,100])
limit=100

people.sort()

count=0
left,right=0,len(people)-1
while left<right:
    if people[left]+people[right]<=limit:
        left+=1
    right-=1
    count+=1

if left==right:
    count+=1

print(count)