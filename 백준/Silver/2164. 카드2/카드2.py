from collections import deque

N=int(input())

cards = deque(range(1,N+1))

while cards:
    card1 = cards.popleft()
    if cards:
        card2 = cards.popleft()
        cards.append(card2)

print(card1)