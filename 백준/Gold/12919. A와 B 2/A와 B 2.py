s=input()
t=input()

def dfs(str):
    if str == s:
        print(1)
        exit()

    if len(str)==len(s):
        return

    if str[-1]=="A":
        dfs(str[:-1])
    if str[0] == "B":
        dfs(str[:0:-1])

dfs(t)
print(0)