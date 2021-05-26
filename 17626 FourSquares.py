#다이나믹프로그래밍이 아닌 브루트포스를 사용했다는! 점~~~
N = int(input())

root = N**0.5
if root == int(root):
    print(1)
else:
    is3=0
    max=int(50000**0.5)
    list=[i*i for i in range(1,max+1)]
    for i in range(len(list)):
        if N-list[i] in set(list):
            print(2)
            exit()
        else:
            for j in range(i,len(list)):
                if N-list[i]-list[j] in set(list):
                    is3=1
                    break
    if is3==1:
        print(3)
    else:            
        print(4)
