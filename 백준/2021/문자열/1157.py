#가장 많이 나온 문자는?
#사전 이용할거지롱

string=input()
Cabinet={}

for i in range(len(string)):
    alpha=string[i].upper()
    if alpha in Cabinet:
        Cabinet[alpha] +=1
    else:
        Cabinet[alpha]=1

max=0
for alpha in Cabinet.keys():
    if Cabinet[alpha]>max:
        max=Cabinet[alpha]
        maxalpha=alpha
    elif Cabinet[alpha]==max:
        maxalpha="?"

print(maxalpha)