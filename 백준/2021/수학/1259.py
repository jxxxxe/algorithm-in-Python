#팰린드롬수

N=int(input())
while N!=0:
    list=[]
    x=N
    while x>0:
        list.append(x%10)
        x//=10
    i=0
    while i<=len(list)-1-i:
        if list[i]!=list[len(list)-1-i]:        #if str(num)[:] == str(num)[::-1]:
            print("no")
            break
        i+=1
    if i>=len(list)-1-i:
        print("yes")

    N=int(input())
'''
>> arr [0,1,2,3,4,5,6,7,8,9] 
>> arr[::2] # 처음부터 끝까지 두 칸 간격으로 [0,2,4,6,8] 
>> arr[1::2] # index 1 부터 끝까지 두 칸 간격으로 [1,3,5,7,9] 
>> arr[::-1] # 처음부터 끝까지 -1칸 간격으로 ( == 역순으로) [9,8,7,6,5,4,3,2,1,0] 
>> arr[::-2] # 처음부터 끝까지 -2칸 간격으로 ( == 역순, 두 칸 간격으로) [9,7,5,3,1]
>> arr[3::-1] # index 3 부터 끝까지 -1칸 간격으로 ( == 역순으로) [3,2,1,0] 
>> arr[1:6:2] # index 1 부터 index 6 까지 두 칸 간격으로 [1,3,5]

'''