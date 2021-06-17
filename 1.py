N=int(input("학생 수 입력: "))
input_list,rank=[],{}

for i in range(N):
    name,k,m,s=input("이름: "),int(input("국어 점수: ")),int(input("수학 점수: ")),int(input("과학 점수: "))
    input_list.append([name,k,m,s,k+m+s,i])

for i in range(N-1,-1,-1):
    for j in range(i):
        if input_list[j][4]>input_list[j+1][4]:
            input_list[j],input_list[j+1]=input_list[j+1],input_list[j]
    order,input_list[i][5]=input_list[i][5],i+1
    rank[order]=input_list[i]

for i in range(N):
    print(rank[i])