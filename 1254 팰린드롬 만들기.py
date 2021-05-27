N=input()

for i in range(len(N)):
    if N[i:][::-1]==N[i:]:       #N[::-1][:len(N)-i]==N[i:] 는 N[i:][::-1]==N[i:]
        print(len(N)+i)
        # exit()
        break

# print(2*len(N)-1)                 #차피 팰린드롬이 아니더라도 맨 끝자리 하나는 무조건 팰린드롬이기 때문에 위 조건은 무조건 성립