from collections import Counter

S=input()

counts = Counter(S)

count0,count1= counts['0']//2,counts['1']//2

print("0"*count0+"1"*count1)