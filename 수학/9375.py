import math

def binomial(num):  #이항계수 구하는 함수
    count=0
    for i in range(1,num+1):
        count+=math.factorial(num)//(math.factorial(i)*math.factorial(num-i))
    return count

case=int(input())   #케이스의 수

for i in range(case):
    list={}     #의상 리스트
    closet=[]   #중복 제거한 의상리스트
    count=0     #경우의 수
    dupli=0     #중복 의상의 수

    n=int(input()) #의상 개수 입력
    for j in range(n):  #의상 입력
        name,sort=input().split()
        list[name]=sort
    for k in list:      # 중복 확인하기
        if list[k] in closet:     
            dupli+=1
        else: 
            closet.append(k)

    print("중복 개수: {}".format(dupli))
    count+=binomial(len(closet))  # 중복 제거한 경우의 수
    count+=(count-len(closet))*binomial(dupli)  #중복 의상으로 대체한 경우의 수
 
    print("최종 count: {}".format(count))
