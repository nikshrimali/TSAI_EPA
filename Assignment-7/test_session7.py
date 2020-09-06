import pytest
import random
import session6
from session6 import *
import os
import inspect
import re
import cmath
import math



README_CONTENT_CHECK_FOR = ['get_my_deck_normally', 'get_deck_oneline', 'get_player_score', 'kinda_poker']

ACTUAL_DECK = ['spades-2', 'spades-3', 'spades-4', 'spades-5', 'spades-6', 'spades-7', 'spades-8', 'spades-9', 'spades-10', 'spades-jack', 'spades-queen', 'spades-king', 'spades-ace', 'clubs-2', 'clubs-3', 'clubs-4', 'clubs-5', 'clubs-6', 'clubs-7', 'clubs-8', 'clubs-9', 'clubs-10', 'clubs-jack', 'clubs-queen', 'clubs-king', 'clubs-ace', 'hearts-2', 'hearts-3', 'hearts-4', 'hearts-5', 'hearts-6', 'hearts-7', 'hearts-8', 'hearts-9', 'hearts-10', 'hearts-jack', 'hearts-queen', 'hearts-king', 'hearts-ace', 'diamonds-2', 'diamonds-3', 'diamonds-4', 'diamonds-5', 'diamonds-6', 'diamonds-7', 'diamonds-8', 'diamonds-9', 'diamonds-10', 'diamonds-jack', 'diamonds-queen', 'diamonds-king', 'diamonds-ace']


def test_readme_exists():
    '''Checks if README.md exists'''
    assert os.path.isfile("README.md", ), "README.md file missing!"


def test_readme_contents():
    '''Contents of readme file has been properly written or not'''
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 100 words"


def test_readme_proper_description():
    '''Checks for the functions implemented has proper description or not'''
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    '''Checks for Readme File formatting'''
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_function_name_had_cap_letter():
    '''Raises error if Functions has capital letter'''
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_incorrect_value():
    '''Sends an invalid input as cards to check if code is raising error'''
    with pytest.raises(ValueError):
        kinda_poker(['queen-hearts', 'queen-clubs', 'sdf-clubs'], ['ace-clubs','ace-clubs','ace-clubs'])

def test_3_players():
    '''Checks the code behaviour when 3 values are sent as inputs instead of 2'''
    with pytest.raises(TypeError):
        kinda_poker(['queen-hearts', 'queen-clubs', 'sdf-clubs'], ['ace-clubs','ace-clubs','ace-clubs'],[])

def test_6_cards():
    '''Checks the code behaviour when 6 cards are sent as inputs instead of range(3,6)'''
    with pytest.raises(TypeError):
        kinda_poker(['queen-hearts', 'queen-clubs', 'sdf-clubs','ace-clubs','ace-clubs','ace-clubs'])


def test_poker_doc():
    '''Checks if the poker function has docstrings or not'''
    assert kinda_poker.__doc__ != None, "The Poker code is unworthy, can't hold Mjölnir"

def test_poker_annotations():
    '''Checks if the poker function has annotations or not'''
    assert kinda_poker.__annotations__ !=  None, "The Poker code is unworthy, can't hold Mjölnir"

def test_sattebaazi():
    '''Sends two inputs as lists of different decks 21 times,
    and validates the output from the scoring function'''

    # 1 Four  of a kind vs 
    a = ['queen-hearts', 'queen-clubs', 'queen-diamonds', 'queen-spades']
    b = ['10-hearts', 'queen-hearts', 'king-hearts', 'king-spades']
    assert kinda_poker(a,b) == a, "Four of a kind works"

    # 2 Three of a kind vs Straight flush
    a = ['queen-hearts', 'queen-clubs', 'queen-diamonds']
    b = ['10-hearts', '9-hearts', '8-hearts']
    assert kinda_poker(a, b) == b, "Three of a kind works"

    # 3 Royal Flush vs Royal Flush
    a = ['ace-hearts', 'queen-hearts', 'king-hearts']
    b = ['jack-hearts', 'queen-hearts', '10-hearts']
    assert kinda_poker(a, b) == a, "Higher order royal flush works"

    # 4 Two pair vs one pair
    a = ['queen-hearts', 'queen-clubs', 'jack-diamonds', 'jack-diamonds', 'king-diamonds']
    b = ['10-hearts', 'queen-hearts', 'king-hearts', 'king-spades', '2-hearts']
    assert kinda_poker(a, b) == a, "Two pair works"

    # 5 Full House vs one pair
    a = ['queen-hearts', 'ace-hearts', 'queen-diamonds', 'jack-diamonds', 'jack-clubs']
    b = ['queen-spades', 'queen-hearts', 'king-hearts', 'king-spades', '2-hearts']
    assert kinda_poker(a, b) == a, "Full house should win"

    # 6 Flush vs High card
    a = ['king-hearts', '8-hearts', '6-hearts', '4-hearts', '2-hearts']
    b = ['10-spades', 'queen-hearts', 'king-hearts', '8-spades', '2-hearts']
    assert kinda_poker(a, b) == a, "Flush should win"

    # 7 Straight vs Straight
    a = ['ace-hearts', 'queen-hearts', 'king-diamonds']
    b = ['8-hearts', '7-spades', '6-diamonds']
    assert kinda_poker(a, b) == a, "a is a bigger straight"

    # 8 Three of a kind vs Straight flush
    a = ['queen-hearts', 'queen-clubs', 'queen-diamonds']
    b = ['9-hearts', '8-hearts', '7-hearts']
    assert kinda_poker(a, b) == b

    # 9 Three of a kind vs flush
    a = ['queen-hearts', 'queen-clubs', 'queen-diamonds']
    b = ['10-hearts', '2-hearts', '8-hearts']
    assert kinda_poker(a, b) == b
    
    # 10 Three of a kind vs High card
    a = ['queen-hearts', 'queen-clubs', 'queen-diamonds']
    b = ['10-hearts', '2-spades', '8-hearts']
    assert kinda_poker(a, b) == a

    # 11 Royal Flush vs Straight

    a = ['ace-hearts', 'queen-hearts', 'king-hearts']
    b = ['jack-spades', 'queen-hearts', '10-hearts']
    assert kinda_poker(a, b) == a

    # 12 Royal Flush vs High Card
    a = ['ace-hearts', 'queen-hearts', 'king-hearts']
    b = ['jack-spades', 'queen-hearts', '2-hearts']
    assert kinda_poker(a, b) == a

    # 13 Royal Flush vs 3 of a kind
    a = ['ace-hearts', 'queen-hearts', 'king-hearts']
    b = ['jack-spades', 'jack-hearts', 'jack-diamonds']
    assert kinda_poker(a, b) == a

    # 14 Two pairs vs High card
    a = ['queen-hearts', 'ace-hearts', 'queen-diamonds', 'jack-diamonds', 'jack-clubs']
    b = ['ace-spades', 'queen-hearts', 'king-hearts', '10-spades', '9-diamonds']
    assert kinda_poker(a, b) == a, "Full house should win"

    # 5 Two pairs vs Full House
    a = ['queen-hearts', 'ace-hearts', 'queen-diamonds', 'jack-diamonds', 'jack-clubs']
    b = ['ace-spades', 'ace-hearts', 'king-hearts', '10-spades', 'ace-diamonds']
    assert kinda_poker(a, b) == b, "Full house should win"

    # 16 Royal flush vs Straight Flush
    a = ['king-clubs', 'queen-clubs', 'ace-clubs']
    b = ['10-hearts', '9-hearts', '8-hearts']
    assert kinda_poker(a, b) == a, "Three of a kind works"

    # 17 Two pair vs High card
    a = ['queen-hearts', 'queen-clubs', 'jack-diamonds', 'jack-diamonds', 'king-diamonds']
    b = ['10-hearts', 'ace-hearts', 'king-hearts', '9-spades', '2-hearts']
    assert kinda_poker(a, b) == a, "Two pair works"

    # 18 Two pair vs Royal Flush
    a = ['queen-hearts', 'queen-clubs', 'jack-diamonds', 'jack-diamonds', 'king-diamonds']
    b = ['ace-hearts', 'king-hearts', 'queen-hearts', '10-hearts', 'jack-hearts']
    assert kinda_poker(a, b) == b, "Royal Flush wins here"

    # 19 Two pair vs Flush
    a = ['queen-hearts', 'queen-clubs', 'jack-diamonds', 'jack-diamonds', 'king-diamonds']
    b = ['ace-hearts', '8-hearts', '2-hearts', '10-hearts', 'jack-hearts']
    assert kinda_poker(a, b) == b, "Flush wins here"

    # 20 Two pair vs Three of a kind
    a = ['queen-hearts', 'queen-clubs', 'jack-diamonds', 'jack-diamonds', 'king-diamonds']
    b = ['ace-hearts', 'ace-spades', 'ace-diamonds', '10-hearts', 'jack-hearts']
    assert kinda_poker(a, b) == b, "Three of a kind wins here"
    
    # 21 Two pair vs Straight Flush
    a = ['queen-hearts', 'queen-clubs', 'jack-diamonds', 'jack-diamonds', 'king-diamonds']
    b = ['10-hearts', '9-hearts', '8-hearts', '7-hearts', '6-hearts']
    assert kinda_poker(a, b) == b, "Straight Flush wins here"

# 12
def test_royalflush():
    ''' Tests the properties when RoyalFlush is sent as Input'''
    a = ['ace-hearts', 'queen-hearts', 'king-hearts']
    score = get_player_score(a)
    assert score['rank'] == 1, "RoyalFlush is ranked 1"
    assert score['deck_type'] == "Royal Flush"

# 13
def test_straightflush():
    '''Tests the properties when StraightFlush is sent as Input'''
    a = ['10-hearts', '9-hearts', '8-hearts', '7-hearts']
    score = get_player_score(a)
    assert score['rank'] == 2, "RoyalFlush is ranked 1"
    assert score['deck_type'] == "Straight Flush"


# 14
def test_fourkind():
    '''Tests the properties when Four of a kind is sent as Input'''
    a = ['queen-hearts', 'queen-spades', 'queen-diamonds', 'queen-clubs', '5-clubs']
    score = get_player_score(a)
    assert score['rank'] == 3, "RoyalFlush is ranked 1"
    assert score['deck_type'] == "Four of a kind"

# 15

def test_fullhouse():
    '''Tests the properties when Full House is sent as Input'''
    a = ['ace-hearts', 'ace-spades', 'ace-diamonds', 'king-clubs', 'king-hearts']
    score = get_player_score(a)
    assert score['rank'] == 4
    assert score['deck_type'] == "Full House"


# 16

def test_flush():
    '''Tests the properties when Flush is sent as Input'''
    a = ['king-hearts', '8-hearts','6-hearts','4-hearts','2-hearts',]
    score = get_player_score(a)
    assert score['rank'] == 5
    assert score['deck_type'] == "Flush"


# 17

def test_straight():
    '''Tests the properties when straight is sent as Input'''
    a = ['8-hearts','7-clubs','6-hearts','5-diamonds', '4-spades']
    score = get_player_score(a)
    assert score['rank'] == 6
    assert score['deck_type'] == "Straight"


# 18
def test_three_kind():
    '''Tests the properties when three of a kind is sent as Input'''
    a = ['queen-hearts','queen-clubs','7-hearts','queen-diamonds', '4-spades']
    score = get_player_score(a)
    assert score['rank'] == 7
    assert score['deck_type'] == "Three of a kind"


# 19
def test_two_pair():
    '''Tests the properties when two_pair is sent as Input'''
    a = ['queen-hearts','queen-clubs','9-hearts','9-diamonds', '4-spades']
    score = get_player_score(a)
    assert score['rank'] == 8
    assert score['deck_type'] == "Two pairs"


# 20
def test_one_pair():
    '''Tests the properties when one_pair is sent as Input'''
    a = ['queen-hearts','queen-clubs','9-hearts','8-diamonds', '4-spades']
    score = get_player_score(a)
    assert score['rank'] == 9
    assert score['deck_type'] == "One pair"


# 21
def test_high_card():
    '''Tests the properties when high_card is sent as Input'''
    a = ['ace-hearts','queen-clubs','10-hearts','9-diamonds', '4-spades']
    score = get_player_score(a)
    assert score['rank'] == 10
    assert score['deck_type'] == "High Card"

# 22
def test_score_doc():
    '''Checks if the score function has docstrings or not'''
    assert get_player_score.__doc__ != None, "The Score code is also unworthy, can't hold Mjölnir"


# 23
def test_score_annotations():
    '''Checks if the score function has annotations or not'''
    assert get_player_score.__annotations__ !=  None, "The Score code is also unworthy, can't hold Mjölnir"

# 24
def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically
    significant indenting.'''
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

# 25
def test_normal_deck():
    '''Checks the deck generated by one line is correct or not'''
    boring_deck = get_my_deck_normally()
    assert sorted(boring_deck) == sorted(ACTUAL_DECK), "Free to to kuch bhi code likhoge kya!!!"

# 26
def test_oneliner_deck():
    '''Checks the deck generated by one line is correct or not'''
    awesome_deck = get_deck_oneline()
    assert sorted(awesome_deck) == sorted(ACTUAL_DECK), "Free to to kuch bhi code likhoge kya!!!"

# 27
def test_match_decks():
    '''Checks the  output matches of both decks'''
    boring_deck = get_my_deck_normally()
    awesome_deck = get_deck_oneline()

    assert sorted(boring_deck) == sorted(awesome_deck), "Gangadhar hi Shaktimaan hai bhai"

# 28
def test_oneliner_doc():
    '''Checks if the oneliner function has docstrings or not'''
    assert kinda_poker.__doc__ != None, "The Poker code is unworthy, can't hold Mjölnir"

# 29
def test_oneliner_annotations():
    '''Checks if the oneliner function has annotations or not'''
    assert kinda_poker.__annotations__ !=  None, "The Poker code is unworthy, can't hold Mjölnir"

# 30
def test_normal_deck_doc():
    '''Checks if the normal_deck function has docstrings or not'''
    assert kinda_poker.__doc__ != None, "The Poker code is unworthy, can't hold Mjölnir"

# 31
def test_normal_deck_annotations():
    '''Checks if the normal_deck function has annotations or not'''
    assert kinda_poker.__annotations__ !=  None, "The Poker code is unworthy, can't hold Mjölnir"