skill="CBD"
skill_trees=["BACDE", "CBADF", "AECB", "BDA"]
skill_set=set(skill)
answer=len(skill_trees)
for skill_tree in skill_trees:
    skill_stack=list(skill)[::-1]
    for st in skill_tree:
        if st in skill_set:
            if skill_stack and skill_stack[-1]!=st:
                answer-=1
                break
            if skill_stack:
                skill_stack.pop()
print(answer)