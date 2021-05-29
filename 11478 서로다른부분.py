S=input()
diff=set()

for i in range(1,len(S)+1):
    for j in range(len(S)-i+1):
        diff.add(S[j:i+j])

print(len(diff))