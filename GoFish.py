import Cards

deck = Cards.Deck(hand_size = 7)

valid_input = {'A' : 'A', 'K' : 'K', 'Q' : 'Q', 'J' : 'J', '10' : 'T', '9' : '9',
               '8' : '8', '7' : '7', '6' : '6', '5' : '5', '4' : '4', '3' : '3', 
               '2' : '2'}

def find_card(card:str, player) -> list:
    """It Is Assumed Card Is The Value, Not The Suit"""
    results = []
    for c in deck.players[player].in_hand:
        if c[0] == valid_input[card]:
            results.append(c)
    return results

def take_card(cards : list, player : int, target : int):
    pass


def ask_card(player : int, target : int):
    deck.read_player_hand(player)
    valid_guess = False
    while valid_guess == False:
        request = input("Ask For A Card You Have: ")
        if request in valid_input:
            have_card = find_card(request, player)
            if len(have_card) > 0:
                valid_guess = True
                target_cards = find_card(request, target)
                if len(target_cards) > 0:
                    take_card(target_cards, player, target)
                    #If Asker Gets A Card(s) Asked For, They Go Again#
                else:
                    print('Go Fish!')
                    #Draw Card, Then Check To See If It Was Card Asked For. If So, Asker Goes Again#
            else:
                print('Pick A Card You Have')
        else:
            val_list = sorted(list(valid_input.keys()))
            print('Please Enter A Valid Card Value!')
            print(val_list)