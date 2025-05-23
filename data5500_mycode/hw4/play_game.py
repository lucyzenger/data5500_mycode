from DeckOfCards import DeckOfCards, Card, deck

#add up the score of the hand
def calculate_score(hand):
    total = 0
    aces = 0
    for card in hand:
        if card.face in ["Jack", "Queen", "King"]:
            total += 10
        elif card.face == "Ace":
            total += 11
            aces += 1
        else:
            total += int(card.face)

    #if total is too high make some aces worth 1 instead of 11
    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total

#print the cards and score
def print_hand(hand, owner="Player"):
    print(f"{owner}'s hand:")
    for card in hand:
        print(f"  {card.face} of {card.suit}")
    print(f"{owner}'s total score is: {calculate_score(hand)}\n")

#start game
print("Welcome to Black Jack!\n")

def play_blackjack():
        print("Deck before shuffled:")
        for card in deck.deck:
            print(f"{card.face} of {card.suit}")
        deck.shuffle_deck()
        print("\nDeck after shuffled:")
        for card in deck.deck:
            print(f"{card.face} of {card.suit}")

        #shuffle the deck
        deck.shuffle_deck()

        #give 2 cards to player and 2 to dealer
        user_hand = [deck.deck.pop(), deck.deck.pop()]
        dealer_hand = [deck.deck.pop(), deck.deck.pop()]

        #show player cards and one dealer card
        print_hand(user_hand, "Player")
        print(f"Dealer's visible card: {dealer_hand[0].face} of {dealer_hand[0].suit}\n")

        #player's turn to hit or stand
        while calculate_score(user_hand) < 21:
            move = input("Do you want to hit or stand? ")
            if move == "hit":
                user_hand.append(deck.deck.pop())
                print_hand(user_hand, "Player")
            elif move == "stand":
                break
            else:
                print("type 'hit' or 'stand'")

        #check if player went over 21
        if calculate_score(user_hand) > 21:
            print("you busted! dealer wins.")
            return

        #dealer's turn. hits until 17 or more
        print_hand(dealer_hand, "Dealer")
        while calculate_score(dealer_hand) < 17:
            dealer_hand.append(deck.deck.pop())
            print_hand(dealer_hand, "Dealer")

        #compare scores and say who won
        player_score = calculate_score(user_hand)
        dealer_score = calculate_score(dealer_hand)

        if dealer_score > 21 or player_score > dealer_score:
            print("you win!")
        elif dealer_score > player_score:
            print("dealer wins!")
        else:
            print("it's a tie!")

#run the game
play_blackjack()