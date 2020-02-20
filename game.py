import pandas as pd
import numpy as np
import random

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __repr__(self):
        return '{'+str(self.face)+' of '+str(self.suit)+'}'

class Player:
    def __init__(self, name, stack):
        self.name = None
        self.stack = None
        self.cards = []
        self.position = None
        self.bet = None
     def __repr__(self):
        return '{Player ' + str(self.name) + ' with hand ' + str(self.cards) + ' and stack '+ str(self.stack) + '}'



class Deck:
    def __init__(self):
        self.all_cards = None # Turn this into a list of all 52 cards
    def create_cards(self):
        l = []
        for item in ["C", "D", "H", "S"]:
            for i in range(1,14):
                l.append(Card(i, item))
        self.all_cards = l



    def choose_cards(self, val):
        cards = random.sample(self.all_cards, val)
        return cards



class Poker_Game:

    def __init__(self, num_players, pot, small_blind, big_blind):
        self.num_players = num_players
        self.pot = pot
        self.small_blind = small_blind
        self.big_blind = big_blind
        self.cards_on_board = None
        self.players  = None
        self.deck = None

    def make_players(self):
        l = []
        for i in range(self.num_players):
            player = Player(i, pot/num_players)
            l.append(player)
        return l

    def get_deck(self):
        self.deck = Deck()
        self.deck.create_cards()

    def deal(self):
        needed_cards = 5 + 2 * self.num_players
        cards_for_round = self.deck.choose_cards(needed_cards)
        for person in self.players:
            person.cards.append(cards_for_round.pop())
            person.cards.append(cards_for_round.pop())
        self.cards_on_board = cards_for_round

















