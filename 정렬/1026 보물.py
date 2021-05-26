N=int(input())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))

arr.sort()
brr.sort()
brr.reverse()

print(sum([arr[i]*brr[i] for i in range(N)]))