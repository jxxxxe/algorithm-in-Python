from collections import deque

N=int(input())

cards = deque(range(N,0,-1))

while cards:
    card1 = cards.pop()
    if cards:
        card2 = cards.pop()
        cards.appendleft(card2)

print(card1)