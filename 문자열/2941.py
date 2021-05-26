#크로아티아 문자
#index가 i+1 이상이면 인덱스의 범위를 벗어날 수 있다.
chro=input()

count=0
for i in range(len(chro)):
    if chro[i]=='-' or chro[i]=='=':
        count-=1
    elif i+2<len(chro) and chro[i]=='d' and chro[i+1]=='z' and chro[i+2]=='=':
        count-=1
    elif i+1<len(chro) and (chro[i]=='l' or chro[i]=='n') and chro[i+1]=='j':
        count-=1

    count+=1

print(count)