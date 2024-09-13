import random,itertools

deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
random.shuffle(deck)

for i in range(1,5):
    print(deck[i][0],'of',deck[i][1])
