N=int(input())

words=list(input() for _ in range(N))
match={}

num=9
words.sort(reverse=True,key=len)
max_len=len(words[0])
for word in words:
    word.rjulst(max_len,'')
print(words)

for i in range(N):
    for j in range(len(words[i])):
        if not words[i][j] in match:
            match[words[i][j]]=num
            num-=1
        words[i][j]=match[words[i][j]]
    print(words[i])
    
sum=0
for w in words:
    sum+=int(''.join(map(str,w)))
print(sum)