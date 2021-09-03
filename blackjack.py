import random
import time
import doctest


def BLACKJACK_21() -> int:
    """Return the upperbound number of valid card values.

    :return: an integer, 21
    """
    return 21


def DEALER_LIMIT() -> int:
    """Return the upperbound number to which the dealer is allowed to raise to.

    :return: an integer, 14
    """
    return 14


def STARTING_MONEY() -> int:
    """Return the starting amount of money the player has.

    :return: an integer, 100
    """
    return 100


def MIN_BET() -> int:
    """Return the minimum bet the player can make.

    :return: an integer, 10
    """
    return 10


def WIN_BET_RETURN() -> int:
    """Return the amount the player's bet will be multiplied by if they win the round.

    :return: an integer, 2.
    """
    return 2


def MAX_ACE_11() -> int:
    """Return the upperbound number that the player's hand can be before Ace values drop to 1.

    :return: an integer, 11.
    """
    return 11


def GREEN() -> str:
    """Return string to color text green.

    :return: a string to color text green
    """
    return "\033[32m"


def RED() -> str:
    """Return string to color text red.

    :return:  string to color text red
    """
    return "\033[31m"


def END() -> str:
    """Return string to end the text color.

    :return: a string that denotes an end to the text color
    """
    return "\033[0m"


class Card:
    """Create a card.

    This class creates an instance of a playing card.
    """

    def __init__(self, name, value, suit):
        """Initialize instance variables of Card.

        :param name: a string.
        :param value: a positive integer.
        :param suit: a string.
        :postcondition: correctly assign instance variables.
        """
        self.name = name
        self.value = value
        self.suit = suit

    def __repr__(self):
        """Define dunder method __repr__ of Card.

        :postcondition: correctly assign the output of __repr__
        :return: a string representation of how to initialize Card.

        >>> test_card = Card("queen", 10, "hearts")
        >>> print(repr(test_card))
        Card('queen', 'hearts', 10)
        """
        return "Card('{}', '{}', {})".format(self.name, self.suit, self.value)

    def __str__(self):
        """Define dunder method __str__ of Card.

        :postcondition: correctly assign the output of __str__
        :return: a formatted string representation of Card's information.

        >>> test_card = Card("queen", 10, "hearts")
        >>> print(str(test_card))
        This is a(n) queen of hearts, with the value 10
        """
        return "This is a(n) {} of {}, with the value {}".format(self.name, self.suit, self.value)


def make_cards(suit: str) -> list:
    """Create cards from a suit.

    This function will create all the cards Ace to King from a card suit.

    :param suit: a string.
    :precondition: all the conditions to create a Card object with the Card class must be met.
    :postcondition: correctly create all the cards from a specified suit.
    :return: a list of all the cards in the specified suit.

    >>> hearts = make_cards("hearts")
    >>> print(hearts)
    [Card('2', 'hearts', 2), Card('3', 'hearts', 3), Card('4', 'hearts', 4), Card('5', 'hearts', 5), Card('6', \
'hearts', 6), Card('7', 'hearts', 7), Card('8', 'hearts', 8), Card('9', 'hearts', 9), Card('10', 'hearts', 10), \
Card('ace', 'hearts', 1), Card('queen', 'hearts', 10), Card('king', 'hearts', 10), Card('jack', 'hearts', 10)]
    """
    suit_cards = [Card(str(y), y, suit) for y in range(2, 11)]
    face_cards = [Card("ace", 1, suit), Card("queen", 10, suit), Card("king", 10, suit), Card("jack", 10, suit)]
    for card in face_cards:
        suit_cards.append(card)
    return suit_cards


def make_deck() -> list:
    """Make a deck of 52 Cards.

    :precondition: all the conditions to successfully execute make_cards function must be met.
    :postcondition: creates a deck with 52 Cards, 13 from each suit.
    :return: a list representing a deck of cards.

    >>> my_deck = make_deck()
    >>> print(my_deck)  # this is obviously going to be very long...
    [Card('2', 'hearts', 2), Card('3', 'hearts', 3), Card('4', 'hearts', 4), Card('5', 'hearts', 5), Card('6', \
'hearts', 6), Card('7', 'hearts', 7), Card('8', 'hearts', 8), Card('9', 'hearts', 9), Card('10', 'hearts', 10), \
Card('ace', 'hearts', 1), Card('queen', 'hearts', 10), Card('king', 'hearts', 10), Card('jack', 'hearts', 10), \
Card('2', 'spades', 2), Card('3', 'spades', 3), Card('4', 'spades', 4), Card('5', 'spades', 5), \
Card('6', 'spades', 6), Card('7', 'spades', 7), Card('8', 'spades', 8), Card('9', 'spades', 9), \
Card('10', 'spades', 10), Card('ace', 'spades', 1), Card('queen', 'spades', 10), Card('king', 'spades', 10), \
Card('jack', 'spades', 10), Card('2', 'diamonds', 2), Card('3', 'diamonds', 3), Card('4', 'diamonds', 4), \
Card('5', 'diamonds', 5), Card('6', 'diamonds', 6), Card('7', 'diamonds', 7), Card('8', 'diamonds', 8), \
Card('9', 'diamonds', 9), Card('10', 'diamonds', 10), Card('ace', 'diamonds', 1), Card('queen', 'diamonds', 10), \
Card('king', 'diamonds', 10), Card('jack', 'diamonds', 10), Card('2', 'clubs', 2), Card('3', 'clubs', 3), \
Card('4', 'clubs', 4), Card('5', 'clubs', 5), Card('6', 'clubs', 6), Card('7', 'clubs', 7), Card('8', 'clubs', 8), \
Card('9', 'clubs', 9), Card('10', 'clubs', 10), Card('ace', 'clubs', 1), Card('queen', 'clubs', 10), \
Card('king', 'clubs', 10), Card('jack', 'clubs', 10)]
    >>> print(len(my_deck))
    52
    """
    deck_list = []
    for card in make_cards("hearts"):
        deck_list.append(card)
    for card in make_cards("spades"):
        deck_list.append(card)
    for card in make_cards("diamonds"):
        deck_list.append(card)
    for card in make_cards("clubs"):
        deck_list.append(card)
    return deck_list


def make_player() -> dict:
    """Make the player.

    :postcondition: correctly makes a player dictionary with the keys name, money, hand, hand_value, and bet.
    :return: a dictionary representing the player.

    >>> me = make_player()
    >>> print(me)
    {'name': 'the Player', 'money': 100, 'hand': [], 'hand_value': 0, 'bet': 0}
    """
    player = {"name": "the Player", "money": STARTING_MONEY(), "hand": [], "hand_value": 0, "bet": 0}
    return player


def make_dealer() -> dict:
    """Make the dealer.

    :postcondition: correctly makes a dealer dictionary with the keys name, hand, and hand_value.
    :return: a dictionary representing the dealer.

    >>> cpu = make_dealer()
    >>> print(cpu)
    {'name': 'the Dealer', 'hand': [], 'hand_value': 0}
    """
    dealer = {"name": "the Dealer", "hand": [], "hand_value": 0}
    return dealer


def deal_cards(deck: list, person: dict):
    """Deal 2 cards to the person at the start of a round.

    :param deck: a list.
    :param person: a dictionary.
    :precondition: deck must be a list which only contains Card objects.
    :precondition: person must be a dictionary containing the key "hand", which is a list.
    :postcondition: correctly deals 2 cards to the person at the beginning of the round.
    :postcondition: prints out which cards were dealt.

    >>> me = make_player()
    >>> test_deck = make_deck()
    >>> deal_cards(test_deck, me)  # due to time.sleep there is some lag in execution
    <BLANKLINE>
    The card 2 of hearts was dealt to the Player.
    <BLANKLINE>
    The card 3 of hearts was dealt to the Player.
    <BLANKLINE>
    The current value of \033[32mthe Player\033[0m's hand is \033[32m5\033[0m.
    """
    time.sleep(1)
    print(f"\nThe card {deck[0].name} of {deck[0].suit} was dealt to {person['name']}.")
    time.sleep(1)
    print(f"\nThe card {deck[1].name} of {deck[1].suit} was dealt to {person['name']}.")
    person["hand"].append(deck.pop(0))
    person["hand"].append(deck.pop(0))
    time.sleep(1)
    check_hand_value(person)


def hit(deck: list, person: dict):
    """Deal a card to the person that choose to hit during a round.

    :param deck: a list.
    :param person: a dictionary.
    :precondition: deck must be a list with 52 Card objects.
    :precondition: person must be a dictionary containing the key "hand", which is a list.
    :postcondition: correctly deals a card to the person at the beginning of the round.
    :postcondition: prints out which card was dealt.

    >>> me = make_player()
    >>> test_deck = make_deck()
    >>> hit(test_deck, me)  # due to time.sleep there is some lag in execution
    <BLANKLINE>
    The card 2 of hearts was dealt to the Player.
    <BLANKLINE>
    The current value of \033[32mthe Player\033[0m's hand is \033[32m2\033[0m.
    """
    time.sleep(1)
    print(f"\nThe card {deck[0].name} of {deck[0].suit} was dealt to {person['name']}.")
    person["hand"].append(deck.pop(0))
    time.sleep(1)
    check_hand_value(person)


def check_hand_value(person: dict):
    """Calculate the value of the person's hand.

    Aces will be worth 11, unless the total value of the person's hand exceeds 10. If so, Aces are worth 1.

    :param person: a dictionary.
    :precondition: person must be a dictionary containing the key "hand", which is a list.
    :precondition: the key "hand" can only have a list, which can either be empty or only contain Card objects.
    :postcondition: correctly calculates the value of the person's hand.
    :return: an integer that corresponds to the value of the cards in the person's hand.

    >>> me = make_player()
    >>> me["hand"].append(Card('2', 2, 'hearts'))
    >>> check_hand_value(me)
    <BLANKLINE>
    The current value of \033[32mthe Player\033[0m's hand is \033[32m2\033[0m.
    >>> me["hand"].append(Card('ace', 1, 'hearts'))
    >>> check_hand_value(me)
    <BLANKLINE>
    The current value of \033[32mthe Player\033[0m's hand is \033[32m13\033[0m.
    >>> me["hand"].append(Card('10', 10, 'hearts'))
    >>> check_hand_value(me)  # due to time.sleep there is some lag in execution
    <BLANKLINE>
    The current value of \033[32mthe Player\033[0m's hand is \033[32m13\033[0m.
    """
    value = 0
    aces = 0
    for card in person["hand"]:
        value += card.value
        if card.name == "ace":
            aces += 1
    if aces >= 1 and value <= MAX_ACE_11():
        value += 10
    person["hand_value"] = value
    if person["name"] == "the Dealer":
        print(f"\nThe current value of {RED() + person['name'] + END()}'s hand is "
              f"{RED() + str(person['hand_value']) + END()}.")
    if person["name"] == "the Player":
        print(f"\nThe current value of {GREEN() + person['name'] + END()}'s hand is "
              f"{GREEN() + str(person['hand_value']) + END()}.")


def reset_round(player: dict, dealer: dict):
    """Reset the values of player and dealer after each round concludes.

    The hands of both the player and the dealer will be reset, and the player's bet value will be changed back to 0.

    :param player: a dictionary.
    :param dealer: a dictionary.
    :precondition: player must be a dictionary containing the keys "name", "money", "hand", "hand_value", and "bet".
    :precondition: dealer must be a dictionary containing the keys "name, "hand", and "hand_value".
    :postcondition: correctly resets the player and dealer's hands, as well as the player's bet.

    >>> me = make_player()
    >>> me["hand"].append(Card('2', 2, 'hearts'))
    >>> me["bet"] = 50
    >>> me["hand_value"] = 2
    >>> cpu = make_dealer()
    >>> cpu["hand"].append(Card('10', 10, 'hearts'))
    >>> cpu["hand_value"] = 10
    >>> print(me)
    {'name': 'the Player', 'money': 100, 'hand': [Card('2', 'hearts', 2)], 'hand_value': 2, 'bet': 50}
    >>> print(cpu)
    {'name': 'the Dealer', 'hand': [Card('10', 'hearts', 10)], 'hand_value': 10}
    >>> reset_round(me, cpu)
    >>> print(me)
    {'name': 'the Player', 'money': 100, 'hand': [], 'hand_value': 0, 'bet': 0}
    >>> print(cpu)
    {'name': 'the Dealer', 'hand': [], 'hand_value': 0}
    """
    player["hand"].clear()
    dealer["hand"].clear()
    player["hand_value"] = 0
    dealer["hand_value"] = 0
    player["bet"] = 0


def make_bet(player: dict):
    """Make a bet.

    :param player: a dictionary.
    :precondition: player must be a dictionary containing the keys "name", "money", "hand", "hand_value", and "bet".
    :precondition: only positive integers are accepted for bets.
    :precondition: bets must be >= 10.
    :raise: ValueError if player input is not a value which can be converted to an integer.
    :postcondition: makes a bet for the player and removes the value from the money they currently have.
    """
    while True:
        try:
            bet_value = int(input("\nHow many dollars do you wish to bet? "))
        except ValueError:
            print("\nYou must enter a whole dollar amount with no decimal point or trailing zeroes.")
        else:
            if bet_value > player["money"]:
                print("\nYou don't have that much money, try again.")
            if bet_value < MIN_BET():
                print("\nYou must make a bet of at least 10 dollars.")
            if player["money"] >= bet_value >= MIN_BET():
                player["money"] -= bet_value
                player["bet"] += bet_value
                print(f"\nYou have bet {player['bet']} dollars and you have {player['money']} dollars remaining.")
                break


def win_round(player: dict):
    """Add the money won to the player's total amount of money if they win a round.

    :param player: a dictionary.
    :precondition: player must be a dictionary containing the keys "name", "money", "hand", "hand_value", and "bet".
    :postcondition: correctly increases the player's total amount of money.

    >>> me = make_player()
    >>> me["bet"] = 10
    >>> win_round(me)  # due to time.sleep there is some lag in execution
    <BLANKLINE>
    You have won this round!
    <BLANKLINE>
    You have won 20 dollars! You have 120 dollars now.
    >>> print(me["money"])
    120
    """
    time.sleep(1)
    print("\nYou have won this round!")
    player["money"] += player["bet"] * WIN_BET_RETURN()
    print(f"\nYou have won {player['bet'] * WIN_BET_RETURN()} dollars! You have {player['money']} dollars now.")
    time.sleep(1)


def lose_round(player: dict):
    """Subtract the money lost from the player's total amount of money if they lose a round.

    :param player: a dictionary.
    :precondition: player must be a dictionary containing the keys "name", "money", "hand", "hand_value", and "bet".
    :postcondition: correctly decreases the player's total amount of money.

    >>> me = make_player()
    >>> me["money"] = 90
    >>> me["bet"] = 10
    >>> lose_round(me)  # due to time.sleep there is some lag in execution
    <BLANKLINE>
    You have lost 10 dollars. You have 90 dollars remaining.
    >>> print(me["money"])
    90
    """
    time.sleep(1)
    print(f"\nYou have lost {player['bet']} dollars. You have {player['money']} dollars remaining.")
    time.sleep(1)


def tie_round(player: dict):
    """Return the money the player bet to the player's total amount of money if the round results in a tie.

    :param player: a dictionary.
    :precondition: player must be a dictionary containing the keys "name", "money", "hand", "hand_value", and "bet".
    :postcondition: correctly returns the amount bet to the player's total amount of money.

    >>> me = make_player()
    >>> me["money"] = 90
    >>> me["bet"] = 10
    >>> tie_round(me)  # due to time.sleep there is some lag in execution
    <BLANKLINE>
    This round resulted in a draw.
    <BLANKLINE>
    10 dollars was refunded to you. You have 100 dollars.
    >>> print(me["money"])
    100
    """
    time.sleep(1)
    print("\nThis round resulted in a draw.")
    player["money"] += player["bet"]
    print(f"\n{player['bet']} dollars was refunded to you. You have {player['money']} dollars.")
    time.sleep(1)


def make_selection() -> str:
    """Prompt player to make a selection.

    :postcondition: correctly returns the player's choice.
    :return: a string representing the player's choice from an enumerated list.
    """
    time.sleep(1)
    print("\nWhat will you do?\n")
    choices = ["Hit", "Stand"]
    for number, choice in enumerate(choices, 1):
        print(number, "-", choice)
    valid_inputs = str([number for number, choice in enumerate(choices, 1)])
    chosen = False
    while not chosen:
        user_input = str(input("\nEnter a selection: "))
        if user_input not in valid_inputs:
            print("\nYou must make a valid selection.")
        else:
            return user_input


def player_round(player: dict, deck: list):
    """Simulate the player's turn during a round.

    The player's turns will end if the player decides to stand, or if their hand busts.

    :param player: a dictionary.
    :param deck: a list.
    :precondition: player must be a dictionary containing the keys "name", "money", "hand", "hand_value", and "bet".
    :precondition: deck must be a list of Card objects.
    :postcondition: correctly simulate a player's turn during a round.
    """
    while True:
        player_input = make_selection()
        if player_input == "1" and len(deck) > 0:
            hit(deck, player)
            if player["hand_value"] > BLACKJACK_21():
                print("\nBust! You lose this round.")
                break
        if player_input == "1" and len(deck) == 0:
            print("\nThere are no more cards to be dealt, so the game will end now.")
            break
        if player_input == "2":
            check_hand_value(player)
            print("\nYou have ended your turn.")
            break


def dealer_round(dealer: dict, deck: list):
    """Simulate the dealer's turn during a round.

    The dealer's turns will end if the dealer's hand exceeds 14, or if their hand busts.

    :param dealer: a dictionary.
    :param deck: a list.
    :precondition: dealer must be a dictionary containing the keys "name, "hand", and "hand_value".
    :precondition: deck must be a list of Card objects.
    :postcondition: correctly simulate a dealer's turn during a round.
    """
    while True:
        if dealer["hand_value"] < DEALER_LIMIT() and len(deck) > 0:
            hit(deck, dealer)
            if dealer["hand_value"] > BLACKJACK_21():
                print("\nBust! The Dealer loses this round.")
                break
        if dealer["hand_value"] < DEALER_LIMIT() and len(deck) == 0:
            print("\nThere are no more cards to be dealt, so the game will end now.")
            break
        if DEALER_LIMIT() <= dealer["hand_value"] <= BLACKJACK_21():
            print("\nThe Dealer will stand now.")
            break


def end_round(player: dict, dealer: dict, stats: dict, deck: list):
    """Wrap up the current round of the game.

    :param player: a dictionary.
    :param dealer: a dictionary.
    :param stats: a dictionary.
    :param deck: a list.
    :precondition: player must be a dictionary containing the keys "name", "money", "hand", "hand_value", and "bet".
    :precondition: dealer must be a dictionary containing the keys "name, "hand", and "hand_value".
    :precondition: stats must be a list with 3 indices, which must all be positive integers.
    :postcondition: correctly executes conditions based on if the round was evaluated to be a win, a loss, or a tie
    :postcondition: resets the player's and dealer's hands, as well as the bet amount to the next round can start.
    for the player.

    >>> me = make_player()
    >>> cpu = make_dealer()
    >>> test_deck = make_deck()
    >>> test_stats = {"win": 0, "lose": 0, "tie": 0}
    >>> me["hand_value"] = 10
    >>> me["bet"] = 10
    >>> cpu["hand_value"] = 8
    >>> end_round(me, cpu, test_stats, test_deck)  # due to time.sleep there is some lag in execution
    <BLANKLINE>
    You have won this round!
    <BLANKLINE>
    You have won 20 dollars! You have 120 dollars now.
    >>> print(test_stats)
    {'win': 1, 'lose': 0, 'tie': 0}

    >>> me = make_player()
    >>> cpu = make_dealer()
    >>> test_deck = make_deck()
    >>> test_stats = {"win": 0, "lose": 0, "tie": 0}
    >>> me["hand_value"] = 25
    >>> me["money"] = 90
    >>> me["bet"] = 10
    >>> cpu["hand_value"] = 8
    >>> end_round(me, cpu, test_stats, test_deck)  # due to time.sleep there is some lag in execution
    <BLANKLINE>
    You have lost 10 dollars. You have 90 dollars remaining.
    >>> print(test_stats)
    {'win': 0, 'lose': 1, 'tie': 0}

    >>> me = make_player()
    >>> cpu = make_dealer()
    >>> test_deck = make_deck()
    >>> test_stats = {"win": 0, "lose": 0, "tie": 0}
    >>> me["hand_value"] = 21
    >>> me["bet"] = 10
    >>> me["money"] = 90
    >>> cpu["hand_value"] = 21
    >>> end_round(me, cpu, test_stats, test_deck)  # due to time.sleep there is some lag in execution
    <BLANKLINE>
    This round resulted in a draw.
    <BLANKLINE>
    10 dollars was refunded to you. You have 100 dollars.
    >>> print(test_stats)
    {'win': 0, 'lose': 0, 'tie': 1}
    """
    if player["hand_value"] > BLACKJACK_21() or (player["hand_value"] < dealer["hand_value"] <= BLACKJACK_21()):
        lose_round(player)
        stats["lose"] += 1
    if dealer["hand_value"] > BLACKJACK_21() or (dealer["hand_value"] < player["hand_value"] <= BLACKJACK_21()):
        win_round(player)
        stats["win"] += 1
    if player["hand_value"] == dealer["hand_value"] or (len(deck) == 0 and len(player["hand"]) == 0):
        tie_round(player)
        stats["tie"] += 1
    reset_round(player, dealer)


def game_loop(stats: dict, deck: list, player: dict, dealer: dict):
    """Simulate the main game loop of the game of Blackjack.

    :param stats: a dictionary.
    :param deck: a list.
    :param player: a dictionary.
    :param dealer: a dictionary.
    :precondition: player must be a dictionary containing the keys "name", "money", "hand", "hand_value", and "bet".
    :precondition: dealer must be a dictionary containing the keys "name, "hand", and "hand_value".
    :precondition: stats must be a list with 3 indices, which must all be positive integers.
    :postcondition: successfully executes the main game loop of the game of blackjack.
    """
    while len(deck) > 0:
        if player["money"] >= 10:
            make_bet(player)
        else:
            print("\nYou can't make the minimum bet of 10 dollars. Better luck next time.")
            break
        if len(deck) >= 4:
            deal_cards(deck, dealer)
            deal_cards(deck, player)
        else:
            print("\nThere are not enough cards to deal. The game is over.")
            break
        dealer_round(dealer, deck)
        player_round(player, deck) if dealer["hand_value"] <= 21 and len(deck) > 0 else None
        end_round(player, dealer, stats, deck)


def game():
    """Initiate a game of Blackjack.

    :precondition: all functions needed for the game to run has their conditions met and are executed correctly
    :postcondition: correctly simulates a modified game of Blackjack.
    """
    stats = {"win": 0, "lose": 0, "tie": 0}
    deck = make_deck()
    random.shuffle(deck)
    player = make_player()
    dealer = make_dealer()
    print(f"{GREEN()}SUSAN'S BLACKJACK SIMULATOR - GOOD LUCK!{END()}")
    game_loop(stats, deck, player, dealer)
    time.sleep(1)
    print(f"\nYou have won {stats['win']} times, lost {stats['lose']} times, and drew {stats['tie']} times.\n\n"
          f"Your total money right now is {player['money']} dollars.")
    time.sleep(1)
    print(f"\n{GREEN()}THANK YOU FOR PLAYING!{END()}")


def main():
    """Drive the program."""
    doctest.testmod(verbose=True)
    game()


if __name__ == '__main__':
    main()
