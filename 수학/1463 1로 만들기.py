# N=int(input())

count=0
while True:
    count=0
    N=int(input())

    k=1
    n=1
    while N>=k*3:
        count+=1
        k*=3
    print(k)
    while N>=k:
        count+=1
        k*=2
    print(k)
    print(count+k-N)


'''
3으로 나눌 수 있으면 3,없으면 2로 나눔
2,3의 배수가 아닌 수-> 1을 빼고 -> 3/2로 나눔 (반복)
'''