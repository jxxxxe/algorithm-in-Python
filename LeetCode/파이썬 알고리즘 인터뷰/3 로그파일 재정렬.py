def reorderLogFiles(logs):
        eng,num=[],[]                   #한줄로 선언 하기!!
        for l in logs:
            # sep=l.index(" ")
            # if l[sep+1].isalpha():
            if l.split()[1].isalpha():  #첫 공백문자 이후 첫글자가(위 두줄을 이렇게 간편하게 할 수 있음)
                print(l.split()[1])
                eng.append(l)
            else:
                num.append(l)
        eng=sorted(eng,key=lambda x:(x.split()[1:],x.split()[0]))
        
        # eng.extend(num)
        return eng+num  #extend보다 훠얼씬 빠르다;

list=[]
for _ in range(10):
    list.append(input())
print(reorderLogFiles(list))