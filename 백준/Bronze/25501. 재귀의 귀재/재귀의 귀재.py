N=int(input())
def is_palindrome(word, left, right, count=1):
    if left>=right:
        return [1, count]
    
    if word[left] != word[right]:
        return [0, count]
    
    return is_palindrome(word, left+1, right-1, count+1)

for _ in range(N):
    word = input()
    print(*is_palindrome(word, 0, len(word)-1))