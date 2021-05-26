#계차수열~~~~~~~!!!...로 하면 안풀리던데; 사실 계차수열 안써도 됨;;쩝

N=int(input())

count=0
level=1
for n in range(N):
    level+=6*n
    count+=1
    if level>=N:
        break

print(count)