#https://www.acmicpc.net/problem/1790
#아따마 헷갈리네 마
N,k=map(int,input().split())

sum_jari=0
first_count=list((10**i,9*(10**i)) for i in range(9))
for f in first_count:
    sum_jari+=f[1]*len(str(f[0]))
    first,count,jari=f[0],f[1],len(str(f[0]))
    if sum_jari>=k:
        new_k=k-(sum_jari-f[1]*len(str(f[0])))
        num=f[0]+(new_k-1)//jari
        if num<=N:
            print(str(num)[(new_k-1)%jari])
            exit()
        break

print(-1)