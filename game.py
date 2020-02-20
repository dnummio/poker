import pandas as pd
import numpy as np

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

def main():
    c1 = Card("A", "H")
    print(c1.face)

main()

class Player:
    def __init__(self, name, stack, position, cards, bet):
        self.name = name
        self.stack = stack
        self.cards = cards
        self.position = position
        self.bet = bet

def main():
    p1 = Player(100)
    print(p1.stack)

main()

class Deck:
    def __init__(self):
        self.all_cards = None # Turn this into a list of all 52 cards
    def create_cards(self):
        
    def deal_cards(self, cards):



class Game:
	def __init__(self, num_players, pot, small_blind, big_blind):
		self.num_players = num_players
		self.pot = pot
		self.small_blind = small_blind
		self.big_blind = big_blind
		self.players  = None
		self.deck = None

	def make_players(self, num_players):
		l = []
		for i in range(num_players):
			player = Player()
			player.name = i 
		    l.append(player)
		return l












