# 알고리즘 개쉽게 했는데 입력처리 땜에 몇번이고 틀렸던 ㅡㅡ
# 이문제에선 테스트케이스가 한꺼번에 몰려온다.
# 끝은 나야함!! 입력한 문장이 올바르지 않을 때 끝이 난다
# 여기에선 먼저 문장을 하나 받고 그 문장이 올바른지 검사한 후, 그문장을 split하여 s,t에 나눠준다.
import sys

while True:
    line = sys.stdin.readline().strip() 
    if not line:
        break

    s, t = line.split()
    i=0
    j=0

    while i<len(s) and j<len(t):
        if s[i]==t[j]:
            i+=1
        j+=1

    if i==len(s):
        print("Yes")
    else:
        print("No")