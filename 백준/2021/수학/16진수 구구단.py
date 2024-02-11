#정수 n을 접두어 없이 16진수로 변환: format(n,'x')

h=input("16진수 입력 : ")
if h=='A' or h=='a':
    h10=10
elif h=='B' or h=='b':
    h10=11
elif h=='C' or h=='c':
    h10=12
elif h=='D' or h=='d':
    h10=13
elif h=='E' or h=='e':
    h10=14
elif h=='F' or h=='f':
    h10=15

for i in range(1,16):
    print("%s*%s = %s"%(h,format(i,'x'),format(h10*i,'x')))