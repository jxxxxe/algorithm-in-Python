selfnum=set(range(1,100))

for cre in range(1,100):
    result=cre
    for c in str(cre):
        result+=int(c)
    if result in selfnum:
        selfnum.remove(result)

for s in selfnum:
    print(s)