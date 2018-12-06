## Card Shuffling ##

import random

suits = {'H' : 'Hearts', 'D' : 'Diamonds', 'C' : 'Clubs', 'S' : 'Spades'}

values = {'A' : 'Ace', 'K' : 'King', 'Q' : 'Queen', 'J' : 'Jack', 'T' : 'Ten',
          '9' : 'Nine', '8' : 'Eight', '7' : 'Seven', '6' : 'Six', '5' : 'Five',
           '4' : 'Four', '3' : 'Three', '2' : 'Two'}

#TODO: Make a Dictionary to store ranking for card power. Use a float: suit ranking.card ranking.
# S = 4, H = 3, D = 2, C = 1

class Deck:

    @staticmethod
    def build_deck() -> list:
        deck = []
        for s in suits:
            for v in values:
                deck.append(v + s) # Example: 2H, Two of Hearts

        return deck

    def shuffle(self) -> None:
        for i in range(100):
            random.shuffle(self.cards)

    @staticmethod
    def read_card(card:str) -> str:
        return '{} of {}'.format(values[card[0]], suits[card[1]])


    class Hand:
        def drawCard(self, numCard : int = 1, text_output : bool = False) -> list:
            drawn = []
            for i in range(numCard):
                if self._outer.hand_limit == None or self._outer.hand_limit > len(self.in_hand):
                    card = self._outer.cards.pop()
                    drawn.append(card)
                    self.in_hand.append(card)
                else:
                    print("Hand At Maximum Size! Was Only Able To Draw {}".format(i))
                    break
            if text_output:
                return drawn
            else:
                return []
            

        def __init__(self, outer, hand_size : int = 5):
            self._outer = outer
            self.in_hand = []
            self.drawCard(hand_size)
        
        def see_hand(self):
            print('Cards In Hand')
            for i in self.in_hand:
                print(self._outer.read_card(i))

    def __init__(self, players : int = 2, hand_limit : int = None, hand_size : int = 5):
        Deck.cards = self.build_deck()
        self.shuffle()
        self.discards = []
        self.players = {}
        self.hand_limit = hand_limit
        for i in range(players):
            self.players[i] = self.Hand(self, hand_size = hand_size)


    def read_player_hand(self, player : int):
        if player not in self.players:
            print("Player Not Found")
        else:
            self.players[player].see_hand()

    def __repr__(self):
        return super().__repr__()




# test = Deck(hand_limit = 5)