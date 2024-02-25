import sys

input = sys.stdin.readline

h,w = map(int, input().split())
blocks = list(map(int, input().split()))
left,right = 0, w-1
lmax,rmax = blocks[left], blocks[right]

answer=0

while left<right:
    if blocks[left]<=blocks[right]:
       lmax=max(lmax, blocks[left])
       answer+=lmax-blocks[left]
       left+=1
    if blocks[left]>blocks[right]:
       rmax=max(rmax, blocks[right])
       answer+=rmax-blocks[right]
       right-=1

print(answer)