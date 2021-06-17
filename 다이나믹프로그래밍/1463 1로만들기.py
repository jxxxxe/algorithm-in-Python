def make_one(n):
    num,i=set([n]),0
    while 1 not in num:
        new=set()
        for x in num:
            if x%3==0:
                new.add(x//3)
            if x%2==0:
                new.add(x//2)
            new.add(x-1)
        num=new
        i+=1
    return i

N=int(input())
print(make_one(N))