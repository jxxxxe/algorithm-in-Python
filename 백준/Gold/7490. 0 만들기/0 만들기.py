t=int(input())

answer=[]
for _ in range(t):
    result=[]
    def dfs(cur,n,string):
        if cur==n:
            new_string=string.replace(' ','')
            if eval(new_string)==0:
                result.append(string)
            return   
        dfs(cur+1,n,f'{string}+{cur+1}')
        dfs(cur+1,n,f'{string}-{cur+1}')
        dfs(cur+1,n,f'{string} {cur+1}')

    n=int(input())
    dfs(1,n,'1')
    answer.append('\n'.join(sorted(result)))

print('\n\n'.join(answer))