import random
#from replit import clear
from art import logo


# the functions

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# nextfunc
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


# nextfunc
def compare(user_score, comp_score):
    if user_score > 21 and comp_score > 21:
        return "Both went over. You lose 🙃"

    if user_score == comp_score:
        return "Itssss a draw 😤"
    elif comp_score == 0:
        return "You lost the game, computer got a blackjack 😱"
    elif user_score == 0:
        return "You won the game!!You got a blackjack 😎"
    elif user_score > 21:
        return "You lost, you went over 😭"
    elif comp_score > 21:
        return " Oh my goodnessss,you won!!😃"
    elif user_score > comp_score:
        return "Got the higher score,you won😁!"
    else:
        return "You lost😭😭😭"


# each pack getting 2 cards
def play_game():
    print(logo)

    user_pack = []
    computer_pack = []
    game_over = False

    for _ in range(2):
        user_pack.append(deal_card())
        computer_pack.append(deal_card())

    # two while loops
    while not game_over:
        user_score = calculate_score(user_pack)
        comp_score = calculate_score(computer_pack)

        print(f"  Your cards: {user_pack}, current score: {user_score}")
        print(f"  computers first card : {computer_pack[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            hit = input("Would you like to continue? if yes type 'y'or if no type 'n': ")
            if hit == 'y':
                user_pack.append(deal_card())
            else:
                game_over = True

    while comp_score != 0 and comp_score < 17:
        computer_pack.append(deal_card())
        comp_score = calculate_score(computer_pack)

    print(f"  your final hand: {user_pack}, final score: {user_score}")
    print(f"  computers final hand: {computer_pack}, final score: {comp_score}")
    print(compare(user_score, comp_score))


while input("Would you like to play a game of blackjack? if yes type 'y' or if no type 'n': ") == 'y':
    #clear()
    play_game()