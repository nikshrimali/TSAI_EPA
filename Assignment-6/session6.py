#Deck of cards without lambda, zip or map functions
def get_my_deck_normally():
    deck = []

    for i in suits:
        for j in vals:
            a = i+'-'+j
            deck.append(a) #zip(i,j)

    # print(deck)
    # print(f'Size of the deck is {len(deck)}')
    return deck

def 

a = list(map(lambda x: list(x), list(map(lambda x: x+"-"+suits[t], vals) for t in range(4))))