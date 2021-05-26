#arr[b:a:-1] => (b>a) arr 끝에서 a+1~b까지 역순으로
#ex. arr='12345', arr[:3:-1]=5, arr[4:0:-1]=5432
import sys

N=int(input())

pattern=input()
starindex=pattern.index("*")

for _ in range(N):
    string=sys.stdin.readline().strip()
    if string[:starindex]==pattern[:starindex]:
        ppattern=pattern[:starindex:-1]
        pstring=string[:starindex-1:-1]
        if len(pstring)<len(ppattern) or pstring[:len(ppattern)]!=ppattern:
            print("NE")
        else:
            print("DA")  
    else:
        print("NE")