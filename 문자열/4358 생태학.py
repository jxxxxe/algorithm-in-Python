#정은이의 첫 골드문제 성공!!!

#첨에 내가 했던 방법!!! eof처리, sorted처리, (print처리)
# import sys
# from collections import Counter

# trees=[]
# while True:               
#     tree=sys.stdin.readline().strip()
#     if not tree:
#         break
#     trees.append(tree)      => eof처리.. 근데 백준에선 read().split('\n')해도 되더라, 즉 4~9라인이 한줄로 됨(밑 참고)

# N=len(trees)
# tree_count=sorted(Counter(trees).items(),key=lambda x:x[0])     
'''
#     #sorted(Counter(trees).keys()) 는 리스트형태가 됨
#     #tree_count=Counter(sys.stdline.read().split('\n')[:-1]) / sum(tree_count.values())
#     #sorted는 밑에 for문에서 for tc in sorted(tree_count.keys())하면 되고 이는 키의 리스트 형태이므로 tree_count[tc]하면 됨.
# for tc in tree_count:
#     print("%s %.4f"%(tc[0], (tc[1]/N)*100))
'''
import sys
from collections import Counter

trees=Counter(sys.stdin.read().split('\n')[:-1])

N=sum(trees.values())

for key in sorted(trees.keys()):
    print(key,"%.4f"%(trees[key]/N*100))