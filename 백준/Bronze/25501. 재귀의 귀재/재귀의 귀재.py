
N=int(input())

for _ in range(N):
    word = input()
    if word == word[::-1]:
        print(1, len(word)//2+1)
        continue
    for i in range(len(word)//2+1):
        if word[i]!=word[-i-1]:
            print(0, i+1)
            break