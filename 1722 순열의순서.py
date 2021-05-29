N=int(input())

line=input()
case=line.split()[0]

if case=='1':
    k=int(line.split()[1])
elif case=='2':
    soon=list(map(int,line.split()[1:]))

