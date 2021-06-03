A,B=map(int,input().split())

if A>B:
    B,A=A,B

jari=B%A if B%A!=0 else A

for _ in range(jari):
    print(1,end='')