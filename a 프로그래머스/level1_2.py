import re
new_id=input()

answer=new_id.lower()
answer=re.sub('[^a-z0-9_.-]','',answer)
while answer.count('..'):
    answer=answer.replace('..','.')
while answer and answer[0]=='.':
    answer=answer[1:]
while answer and answer[-1]=='.':
    answer=answer[:-1]
if not answer:
    answer='a'
if len(answer)>=16:
    answer=answer[:15]
    if answer[-1]=='.':
        answer=answer[:14]
elif len(answer)<=2:
    new_word=answer[-1]
    answer+=new_word*(3-len(answer))

print(answer)