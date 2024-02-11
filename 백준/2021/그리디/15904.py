#UCPC!!
#TODO: 문자열 1000자 제한, 맨앞뒤 공백&연속공백 없어야하는거 처리하기...ㅇㅅㅇ
string=input()
UCPC="UCPC"

i=0
j=0
while i!=len(string) and j!=len(UCPC):
    if string[i]==UCPC[j]:
        j+=1
    i+=1

if j==len(UCPC):
    print("I love UCPC")
else:
    print("I hate UCPC")