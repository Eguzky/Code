import CardsEnhanced as Cards
import KAI
import random
import time
import NameGenK as NameGen



def game_setup() -> Cards.Deck:
    def toInt(num) -> int:
        inum = -1
        try:
            inum =  int(num)
            
        except ValueError:
            print("Not a valid number, try again")
        
        finally:
            return inum

    goodtotal = False
    while goodtotal == False:    
        humans = -1
        bots = -1

        while humans <= -1:
            humans = toInt(input('How Many Human Players? '))
        
        while bots <= -1:
            bots = toInt(input('How Many AI Players? '))
        
        if humans + bots > 6:
            print("Please play with no more than 6 players.")
        elif humans + bots < 2:
            print("There needs to be at least 2 players.")
        else:
            goodtotal = True
    
    if humans + bots == 2:
        deck = Cards.Deck(hand_size=7)
    else:
        deck = Cards.Deck(players = humans + bots, hand_size= 5)

    count = 0
    for player in deck.players:
        pid = deck.players[player]
        count += 1
        if count <= humans:
            pid.set_name()
        else:
            pid.isAI = True
            pid.AI_data = KAI.AI_Gofish(pid, 1)
            pid.name = "AI {}".format(NameGen.namegen())

    return deck


deck = game_setup()
    

valid_input = {'A': 'A', 'K': 'K', 'Q': 'Q', 'J': 'J', '10': 'T', '9': '9',
               '8': '8', '7': '7', '6': '6', '5': '5', '4': '4', '3': '3',
               '2': '2', 'T': 'T'}

game_over = False

players = deck.players


def find_card(card: str, player) -> list:
    """It Is Assumed Card Is The Value, Not The Suit"""
    results = []
    count = 0
    for c in players[player].in_hand:
        if c.value == valid_input[card]:
            results.append(count)
        count += 1
    return results


def take_card(cards: list, player: int, target: int):
    for c in sorted(cards, reverse=True):
        players[player].in_hand.append(players[target].in_hand.pop(c))
    print('{name} Got {cards}!'.format(
        cards=len(cards), name=players[player].name))


def count_score(player: int):
    count_hand = {}
    global game_over
    for c in players[player].in_hand:
        val = c.value
        count_hand.setdefault(val, 0)
        count_hand[val] += 1
    for b in count_hand:
        if count_hand[b] == 4:
            players[player].score += 1
            print('{name} Has A Book of {value}s!  Score is now {score}!'.format(
                value=deck.values[b], name=players[player].name, score=players[player].score))
            for i in sorted(find_card(b, player), reverse=True):
                deck.discard(player, i)
    # Check To See If Game Is Over
    if len(players[player].in_hand) == 0:
        # First loop, find everyone's scores. Second loop, call winner or draws
        high_score = 0
        for p in players:
            if players[p].score > high_score:
                high_score = players[p].score
        winner = []
        for p in players:
            if players[p].score == high_score:
                winner.append(p)
        if len(winner) == 1:
            print('{} Has Won With A Score Of {}!'.format(
                players[winner[0]].name, high_score))
        else:
            print('We Have A Draw With A Score Of {}!'.format(high_score))
            for p in winner:
                print('{} Wins!'.format(players[p].name))
        game_over = True


def ask_card(player: int, target: int, guess: str = None):
    playguess = players[player].guesses
    playguess.setdefault(target, [])
    if guess is None:
        deck.read_player_hand(player)
    valid_guess = False
    while valid_guess is False:
        if guess is None:
            if len(playguess[target]) > 0:
                print("Previous Guesses: {}".format(
                    list(reversed(playguess[target]))))
            request = input("Ask For A Card You Have: ")
        else:
            request = guess

        if request in valid_input:
            print('{Player} Guessed {guess} from {target}'.format(
                Player=players[player].name, guess=request, target=players[target].name))

            playguess[target].append(request)
            if len(playguess[target]) > 3:
                del playguess[target][0]
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
                    draw = players[player].drawCard(text_output=True)
                    if len(draw) == 0:
                        return False
                    if players[player].isAI == False:
                        print(deck.read_card(draw[0]))
                    if draw[0].value == valid_input[request]:
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
    for p in players:
        players[p].guesses = {}  # initialize a guessing dictionary

    while playing:
        for p in players:
            if playing is False:
                break
            turn = True
            print("{}'s turn!".format(players[p].name))
            while turn:
                if len(players[p].in_hand) > 0:
                    gameplayers = list(players.keys())
                    gameplayers.remove(p)
                    if players[p].isAI:
                        target = random.choice(gameplayers)
                        turn = ask_card(
                            p, target, players[p].AI_data.guesscard())
                    else:
                        p_dict = {}
                        count = 0
                        for i in gameplayers:
                            count += 1
                            p_dict[str(count)] = i
                            print('{}. {}'.format(count, players[i].name))
                        target = input('Pick A Player To Ask: ')
                        if target not in p_dict:
                            print('Please Pick A Valid Number')
                            continue
                        turn = ask_card(p, p_dict[target])
                else:
                    print("Player out of cards, game over!")
                count_score(p)
                time.sleep(1)
                if game_over:
                    playing = False
                    break


gameplay_loop()
