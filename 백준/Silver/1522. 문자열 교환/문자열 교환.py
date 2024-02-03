abs = list(input())
length=len(abs)
a_count=abs.count('a')
abs.extend(abs)

result=length

for i in range(length):
    result = min(result, abs[i:i+a_count].count('b'))

print(result)