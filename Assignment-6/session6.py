#Deck of cards without lambda, zip or map functions

vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

# Deck generated Normally
def get_my_deck_normally()->list:
    '''Returns a deck of 52 cards when function is called which is generated in a normal fashion'''
    deck = []

    for i in suits:
        for j in vals:
            a = i+'-'+j
            deck.append(a)
    return deck

# Deck generated in one-line
def get_deck_oneline() -> list:
    '''Single expression includes lambda, zip, and map function to create 52 cards in a deck'''
    return sorted(list(map(lambda x: x[0]+'-'+x[1], list(zip(suits*len(vals), vals*len(suits))))))


# Poker Function
value_dict = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'jack':11, 'queen':12, 'king':13, 'ace':14, 'spades':1, 'clubs':1, 'hearts':1, 'diamonds':1}
suits = ['spades', 'clubs', 'hearts', 'diamonds']

def get_player_score(a:list) -> dict:
    '''Checks the cards, identifies and computes a score of user's deck'''
    correct_value = False
    vals_score = []
    rank = 0
    deck_type = ""

    for cont in a:

        for _ in cont.split("-"):

            if str(_).lower() in value_dict:
                pass

            else:
                raise ValueError('Incorrect Values supplied')
    # Dict of Vals
    in_vals = [x.split("-")[0] for x in a] # Count of the vals received in the function
    vals_count_dict = {i:in_vals.count(i) for i in in_vals}

    # Dict of suits
    in_suits = [x.split("-")[1] for x in a] # Count of the suits received in the function

    # Score of suit cards
    vals_score = sorted([value_dict[t] for t in in_vals], reverse=True)
    suits_dict = {i:in_suits.count(i) for i in in_suits} # Counting elements of suits dict++
    suits_list = sorted(suits_dict, reverse=True) # Sorting the Suits dict

    # Test cases
    # 1 Royal Flush
    if sum([(t-s) for t,s in(zip(vals_score,vals_score[1:]))])  == len(a)-1 and sum(vals_score) > len(a)*10 and len(suits_dict) == 1:
        rank = 1
        deck_type = "Royal Flush"
        print(f'Royal Flush {rank}')

    # 2 Straight Flush
    elif sum([(t-s) for t,s in(zip(vals_score,vals_score[1:]))])  == len(a)-1 and sum(vals_score) < len(a)*10 and len(suits_dict) == 1:
        rank = 2
        deck_type = "Straight Flush"
        print(f'Straight Flush {rank}')

    # 6 Straight
    elif sum([(t-s) for t,s in(zip(vals_score,vals_score[1:]))])  == len(a)-1:
        rank = 6
        deck_type = "Straight"
        print(f'Straight - Rank {rank}')

    # 3 Four of a kind
    elif any(v == 4 for v in vals_count_dict.values()):
        rank = 3
        deck_type = "Four of a kind"
        print(f'Four of a kind {rank}')

    # 4 Full House

    elif any(v == 3 for v in vals_count_dict.values()) and list(v == 2 for v in vals_count_dict.values()).count(True) == 1:
        rank = 4
        deck_type = "Full House"
        print(f'Full house {rank}')

    # 7 Three of a kind
    elif any(v == 3 for v in vals_count_dict.values()):
        rank = 7
        deck_type = "Three of a kind"
        print(f'Three of a kind {rank}')

    # 8 Two pairs
    elif list(v == 2 for v in vals_count_dict.values()).count(True) == 2:
        rank = 8
        deck_type = "Two pairs"
        print(f'Two pairs {rank}')

    # 9 One pair
    elif list(v == 2 for v in vals_count_dict.values()).count(True) == 1:
        rank = 9
        deck_type = "One pair"
        print(f'One pair {rank}')

    # 5 Flush
    elif len(suits_dict) == 1:
        rank = 5
        deck_type = "Flush"
        print('Flush')

    # 10 High Card
    else:
        rank = 10
        deck_type = "High Card"
        print(f'High card {rank}')


    return {'rank': rank, 'score':sum(vals_score), 'deck_type':deck_type}


def kinda_poker(a:list, b:list) -> list:
    '''If you don't have any money and currently going through a Quater life crisis, then playing this game is perfect for you.
    kinda_poker(list1, list2) -> winner_list - Checks the type of cards and computes a score to predict who wins'''

    winner = None

    if (len(a) in range(3,6)) and (len(b) in range(3,6)) and len(a) == len(b):
        score_a = get_player_score(a)
        score_b = get_player_score(b)

        if score_a['rank'] < score_b['rank']:
            winner = a
        elif score_a['rank'] == score_b['rank']:
            if score_a['score'] > score_b['score']:
                winner = a
            else:
                winner = b
        elif score_a['rank'] > score_b['rank']:
            winner = b

        return winner

    else: # Cards check
        raise ValueError('Only players between 3 and 5 are allowed and size of lists must be equal')
