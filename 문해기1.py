N=float(input())

binary_int=[]
binary_flo=[]
integer=int(N)
flo=N-integer

while integer>0:
    binary_int.append(integer%2)
    integer//=2

binary_int.reverse()

for _ in range(10):
    flo*=2
    if flo>1:
        binary_flo.append(1)
        flo-=1
    else:
        binary_flo.append(0)

print(''.join(list(map(str,binary_int)))+'.'+''.join(list(map(str,binary_flo))))