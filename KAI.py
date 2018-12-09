from Cards import Deck
import random
class AI:
    class Memory:
        def __init__(self, outer):
            self._outer = outer
            self.havesets = {}

    def __init__(self, playerfile : Deck.Hand):
        self.playerfile = playerfile
        self.memory = self.Memory(self)
        



class AI_Gofish(AI):
    def setscheck(self):
        self.memory.setscheck()
    
    def guesscard(self) -> str:
        self.setscheck()
        hand = self.memory.havesets

        sort = sorted(hand.items(), key= lambda kv: kv[0])
        highval = hand[sort[0][0]]
        
        choices = []
        for key in hand:
            if hand[key] == highval:
                choices.append(key)
        selected = random.choice(choices)
        if selected == "T":
            selected = "10"
        return selected



    class Memory(AI.Memory):
        def setscheck(self):
            self.havesets = {}
            for card in self._outer.playerfile.in_hand:
                self.havesets.setdefault(card[0], 0)
                self.havesets[card[0]] += 1
        
        def __init__(self, outer):
            super().__init__(outer)
            self.setscheck()
        


    
