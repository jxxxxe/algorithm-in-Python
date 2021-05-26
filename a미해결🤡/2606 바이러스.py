#7=1 1 1 1 1 1 1
#3=>최대2개(7//3), 2=>최대3개
#(3 2개)331 313 133  3*(1+2*3)=21
#(3 0개)1222 2122 2212 2221     4*(1+3+3)+1=29

#set의 add는 한번에 하나씩만 가능
# import sys
# input=sys.stdin.readline

# c=int(input().strip())
# N=int(input().strip())

# worm=set([1])
# for _ in range(N):
#     a,b=map(int,input().split())
#     for w in worm:
#         if a == w or b ==w:
#             worm.add(b)
#             worm.add(a)

# print(len(worm)-1)