#슬라이싱할 때 사전 key를 복사하걸 조작하면 실제 key의 값도 바뀜; 값을 복사해서 조작해야함. why????
#내 생각엔 dict[key]를 복사하면 같은 key니까 dict에 접근하는 걸로 쳐서 그런거같음
#이산수학 아자아잣 최고닷!!

''' 요건 경우의수를 다 구하는함수
def make_one(n):
    num={1:[[1]],2:[[1,1],[2]],3:[[1,1,1],[2,1],[1,2],[3]]}
    for i in range(4,n+1):
        num[i]=[]
        for j in range(1,4):
            for p in num[i-j]:
                c=p[:]
                c.append(j)
                num[i].append(c)
    return num[n]
'''
def make_one(n):
    num=[1,2,4]
    for i in range(3,n):
        num.append(num[i-1]+num[i-2]+num[i-3])
    return num

T=int(input())
case_count=make_one(11)

for _ in range(T):
    n=int(input())
    print(case_count[n-1])