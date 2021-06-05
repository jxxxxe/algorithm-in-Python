N,k=map(int,input().split())

jari,sum_jari=1,0
while True:
    sum_jari+=jari*(9*10**jari-1)
    jari+=1
    if sum_jari+(jari)*(9*10**(jari-1))>k:
        break
print(jari,sum_jari)

new_k = k-sum_jari
num,index = new_k//jari, new_k%jari
num=str(10**(jari-1)+num)
print(num)
# print(-1)