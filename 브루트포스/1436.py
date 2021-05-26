#영화감독 숌

N=int(input())

i=666
count=0
while True:
    if str(i).find("666")!=-1:
        count+=1
        if count==N:
            print(i)
            break
    i+=1