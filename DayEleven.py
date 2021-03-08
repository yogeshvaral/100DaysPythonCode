## BlackJack Rule

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    import random
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw :)"
    elif computer_score == 0:
        return "You loose .Opponent has blackjack"
    elif user_score == 0:
        return "You win with Blackjack"
    elif user_score > 21:
        return "you went over You loose"
    elif computer_score > 21:
        return "Opponent went over you loose"
    elif user_score > computer_score:
        return "you win"
    else:
        return "You loose"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cars are {user_cards} your score is {user_score}")
        print(f"Computer First cards is {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card or Type 'n' to pass")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand {user_cards} Your final score {user_score}")
    print(f"Computer final hand {computer_cards} computer final score {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of blackjack Type 'y' for yes or 'n' for No") == 'y':
    play_game()
