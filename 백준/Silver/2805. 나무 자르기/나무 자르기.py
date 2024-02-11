def cut(tree,center):
    sum=0
    for t in tree:
        sum+=t-center if t-center>0 else 0
    return sum
N,M=map(int,input().split())
tree=list(map(int,input().split()))
left,right=0,max(tree)

while left<=right:
    center=(left+right)//2
    sum=cut(tree,center)
    if sum>=M:
        left=center+1
    else:
        right=center-1

print(right)