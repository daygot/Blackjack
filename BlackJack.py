import random

# deck to access
deck = {card: 4 for card in range(1, 14)}

# player class for easier data access/storage
class PlayerClass:
	def __init__(self, hand, score=0, bust=False, blackjack=False):
		self.hand = hand
		self.score = score
		self.bust = bust
		self.blackjack = blackjack

def main():
	
	# set up the game state
	dealer, player = PlayerClass(list()), PlayerClass(list());

	deal(dealer)
	deal(dealer)
	deal(player)
	deal(player)

	print("Welcome to the casino, and welcome to the Blackjack table!")
	print("Dealer has: " + better_looking_card(dealer.hand[0]) + " ? = ?")
	print("Player has: " + " ".join(better_looking_card(card) for card in player.hand) + " = " + str(player.score))

	# Handle the Blackjack case (21 on initial deal)
	if player.blackjack:
		print("Player Wins!\nBlackjack!")
		return
	
	while True:
		decision = input("Would you like to (H)it or (S)tand? ")
		# Input validation
		if decision != "H" and decision != "S":
			print("Please only enter H or S.")
			continue
		if decision == "H":
			deal(player)
			print("Player has: " + " ".join(better_looking_card(card) for card in player.hand) + " = " + str(player.score))
			# Handle cases where player busts
			if player.bust:
				print("You have busted! Dealer wins!")
				return
			# Otherwise, return to the top of the loop
			continue
		else:
			print("\nPlayer stands with: " + " ".join(better_looking_card(card) for card in player.hand) + " = " + str(player.score))
			print("Dealer has: " + " ".join(better_looking_card(card) for card in dealer.hand) + " = " + str(dealer.score))
			# Dealer will keep hitting as long as score is below 17
			while dealer.score < 17:
				print("Dealer hits")
				deal(dealer)
				# Handle cases where dealer gets 21 and wins
				if dealer.blackjack:
					print("Dealer has: " + " ".join(better_looking_card(card) for card in dealer.hand) + " = " + str(dealer.score))
					print("Dealer wins! 21!")
					return
				# Handle cases where dealer busts
				elif dealer.bust:
					print("Dealer has: " + " ".join(better_looking_card(card) for card in dealer.hand) + " = " + str(dealer.score))
					print("Dealer has busted! Player wins!")
					return
				print("Dealer has: " + " ".join(better_looking_card(card) for card in dealer.hand) + " = " + str(dealer.score))
			print("Dealer stands")

		# Final tally
		if player.score > dealer.score:
			print("\nPlayer wins!")
		elif player.score == dealer.score:
			print("\nTie!")
		else:
			print("\nDealer wins!")

		print(" ".join(better_looking_card(card) for card in player.hand) + " = " + str(player.score) +
		" to Dealer's " + " ".join(better_looking_card(card) for card in dealer.hand) + " = " + str(dealer.score))
		return

# Cosmetic method to make the cards look neater as they get printed
def better_looking_card(card):
	if card == 1: return "A"
	if card == 11: return "J"
	if card == 12: return "Q"
	if card == 13: return "K"
	return str(card)

# Main method that deals a card to the player/dealer and handles the deck
def deal(player_instance):
	card = random.choice(list(deck.keys()))
	deck[card] -= 1
	if deck[card] == 0: deck.pop(card)
	player_instance.hand.append(card)

	# Recalculates the player's/dealer's score
	calculate_score(player_instance)

# Main method that calculates dealer's/player's optimal score. This runs after each deal
def calculate_score(player_instance):
	
	# Start with just one score candidate (of 0). We will add more if an ace is dealt
	score_candidate = [0]
	
	for card in player_instance.hand:
		if card >= 10:
			for i in range(len(score_candidate)):
				score_candidate[i] += 10
		else:
			for i in range(len(score_candidate)):
				score_candidate[i] += card
		if card == 1:
			for i in range(len(score_candidate)):
				score_candidate += [score_candidate[i] + 10]

	# Iterate backward to find the optimal score
	for score in score_candidate[::-1]:
		if score <= 21:
			player_instance.score = score
			if score == 21:
				player_instance.blackjack = True
			break
	# If at the end of the iteration nothing is less than or equal to 21, we know the person busted
	if score > 21:
		player_instance.score = score
		player_instance.bust = True

if __name__ == '__main__':
	main()