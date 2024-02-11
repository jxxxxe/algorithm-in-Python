N,S=map(int,input().split())
num=list(map(int,input().split()))
left,right=0,0
total,l,m_l=0,0,N+1
while right<len(num):
    total+=num[right]
    l+=1
    if total>=S:
        while total-num[left]>=S and left<right:
            total-=num[left]
            left+=1
            l-=1
        m_l=min(l,m_l)
    right+=1
print(m_l if m_l<N+1 else 0)