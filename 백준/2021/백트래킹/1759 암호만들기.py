#set에 들어있는 값들은 해쉬가능해야 함. => 리스트는 해쉬 불가능, 튜플로 변환
#튜플도 join할 수 있음
#함수 외부에 있는 list를 함수 외부에 있는 또 다른 list에 함수내에서 append하더라도 함수 외부에 가면 소멸됨;싹아지
def make_pwd(L,alpah):
    return coperate(alpah,L)

def coperate(list,r):
    picked,start,result=[],0,[]
    def recur(start):
        if len(picked)==r and vow_count(picked,r):
            result.append(tuple(picked))
            return
        for i in range(start,len(list)):
            picked.append(list[i])
            start+=1
            recur(start)
            picked.pop()
    recur(start)
    return result

def vow_count(list,r):
    count=0
    for vow in ['a','e','i','o','u']:
        count+=list.count(vow)
    return (count>=1 and count<=r-2)


L,C=map(int,input().split())
alpha=sorted(input().split())
for pwd in make_pwd(L,alpha):
    print(''.join(pwd))