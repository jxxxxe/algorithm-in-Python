'''
한조서열정리하고옴ㅋㅋ
'''

N=0
while N<1 or N>30000:
    N=int(input())

people=[] #len(배열) 사용 전에 배열 선언

while len(people)!=N:
    people= list(map(int,input().split())) #파이썬에서 리스트 원소들 한줄로 입력 받기
    if len(people)!=N:
        print("입력한 개수만큼 봉우리 수를 입력하시오")
    # TODO: 원소 중복, 원소값 범위 처리

count=0
max=0
i=0

while i<len(people):
    for j in range(i+1,len(people)): #len(배열)은 배열 원소 개수, 즉 마지막 인덱스+1
        if people[i]<people[j]:
            break
        count+=1
    if count>max:
        max=count
    count=0 #count 초기화 필요
    i+=1

print(max)