import sys

input = sys.stdin.readline

N,M = map(int,input().split())
keywords=set()

for _ in range(N):
    keywords.add(input().strip())

for _ in range(M):
    words=set(input().strip().split(','))
    keywords-=words
    print(len(keywords))