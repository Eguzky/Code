import Cards
import KAI
import random

deck = Cards.Deck(hand_size = 7)

valid_input = {'A' : 'A', 'K' : 'K', 'Q' : 'Q', 'J' : 'J', '10' : 'T', '9' : '9',
               '8' : '8', '7' : '7', '6' : '6', '5' : '5', '4' : '4', '3' : '3', 
               '2' : '2'}


def find_card(card:str, player) -> list:
    """It Is Assumed Card Is The Value, Not The Suit"""
    results = []
    count = 0
    for c in deck.players[player].in_hand:
        if c[0] == valid_input[card]:
            results.append(count)
        count += 1
    return results

def take_card(cards : list, player : int, target : int):
    for c in sorted(cards, reverse = True):
        deck.players[player].in_hand.append(deck.players[target].in_hand.pop(c))
    print('You Got {}!'.format(len(cards)))

def count_score(player : int):
    count_hand = {}
    for c in deck.players[player].in_hand:
        val = c[0]
        count_hand.setdefault(val, 0)
        count_hand[val] += 1
    for b in count_hand:
        if count_hand[b] == 4:
            print('You Have A Book of {}s!'.format(deck.values[b]))
            deck.players[player].score += 1
            for i in sorted(find_card(b, player), reverse = True):
                deck.discard(player, i)
    # Check To See If Game Is Over
    if len(deck.players[player].in_hand) == 0:
        # First loop, find everyone's scores. Second loop, call winner or draws
        high_score = 0
        for p in deck.players:
            if deck.players[p].score > high_score:
                high_score = deck.players[p].score
        winner = []
        for p in deck.players:
            if deck.players[p].score == high_score:
                winner.append(p)
        if len(winner) == 1:
            print('{} Has Won With A Score Of {}!'.format(deck.players[winner[0]].name, high_score))
        else:
            print('We Have A Draw With A Score Of {}!'.format(high_score))
            for p in winner:
                print('{} Wins!'.format(deck.players[p].name))




def ask_card(player : int, target : int, guess : str = None):
    if guess == None:
        deck.read_player_hand(player)
    valid_guess = False
    while valid_guess == False:
        if guess == None:
            request = input("Ask For A Card You Have: ")
        else:
            request = guess
            print('{Player} Guessed {guess}'.format(Player = deck.players[player].name, guess = request))
        if request in valid_input:
            have_card = find_card(request, player)
            if len(have_card) > 0:
                valid_guess = True
                target_cards = find_card(request, target)
                if len(target_cards) > 0:
                    take_card(target_cards, player, target)
                    #If Asker Gets A Card(s) Asked For, They Go Again#
                    return True
                else:
                    print('Go Fish!')
                    #Draw Card, Then Check To See If It Was Card Asked For. If So, Asker Goes Again#
                    draw = deck.players[player].drawCard(text_output = True)
                    print(deck.read_card(draw[0]))
                    if draw[0][0] == valid_input[request]:
                        print('Go Again!')
                        return True
                    else:
                        return False
            else:
                print('Pick A Card You Have')
                if guess != None:
                    print('Error: Guess Invalid')
                    return True
        else:
            val_list = sorted(list(valid_input.keys()))
            print('Please Enter A Valid Card Value!')
            print(val_list)

def gameplay_loop():
    playing = True
    while playing:
        for p in deck.players:
            if playing == False:
                break
            turn = True
            while turn:
                players = deck.players.keys()
                players.remove(p)
                if deck.players[p].isAI:
                    target = random.choice(players)
                    turn = ask_card(p, target, deck.players[p].AI_data.guesscard())
                else:
                    input('Pick A Player To Ask: ')

#deck.read_player_hand(1)
#ask_card(0, 1)
deck.players[1].isAI = True
deck.players[1].AI_data = KAI.AI_Gofish(deck.players[1])
deck.players[1].name = 'AI Bob'
ai = deck.players[1].AI_data
ask_card(1, 0, ai.guesscard())