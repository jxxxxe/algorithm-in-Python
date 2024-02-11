S=input()
T=input()

while len(S)<len(T):
    if T[-1]=='A':
        T=T[:-1]
    elif T[-1]=='B':
        T=T[:-1][::-1]

print(1) if S==T else print(0)

#골드5..졸라 easyㅋ