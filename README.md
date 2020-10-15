# Blackjack
Simple Blackjack game implemented in Python

1. This program is runnable straight from the command line. No dependencies are required as the only import is random, which is part of the Python standard library.

2. Some key assumptions
  a. A standard deck of 52 cards is to be used
  b. The dealer will always hit as long as their score is  17 (for instance, if the player stands with a score of 10 and the dealer has a hand of 12, they will still hit even though they already won)
  c. There are no hand limits (there is a variant of the game where the player wins if they have 5 cards without busting)
  d. There is no splitting after the player is initially dealt the two cards
  e. The player can still hit even after reaching 21 (not sure if the rule permits this)

3. Things I did well
  a. Utilizing a PlayerClass class to represent the data contained. This made for easier data retrievalstorage and better readability
  b. Coded the game process sequentially to maximize readability
  c. Wrote individual methods for key features which allows for more flexible debugging
  d. Close adherence to project requirements
  e. Handled input validation where necessary

4. Design choices: 
I opted to use a PlayerClass class to handle basically all of the game's core data as it relates to the two parties in the game (dealer and player). The reason was to make class-reliant methods easier to write. For example, deal(player_instance) is a method that takes in a PlayerClass object, deals a card (and removes it from the deck), and calculates the score appropriately. This would have been messy to implement without a proper data structure containing all of the key info neatly. The one challenging algorithmic decision to made was how to properly calculate a hand's optimal score. My implementation re-calculates the score upon every successful deal which is not ideal, but I thought doing it this way was easier to implementunderstand, and the data processing overhead isn't super punishing.

5. Programming trade-offs: 
In terms of a space-time tradeoff, I used more than just an integer to calculate the score of any given hand (due to the fact that an ace throws off the linear score calculation). I used an array which records possible scores of a hand. There should be an algorithm that can handle this without the use of an array, such as comparing each possible candidate to 21 and taking the largest one.

6. Improvements to be made:
   a. Improving the runtime of the calculate_score method
   b. Implementing another method that handles printing hands for dealerplayer
   c. Implementing an option to start a new game
   d. Implementing record tracking
   e. Implementing chipssome sort of betting system

7. Ways to test:
   a. Manually assigning hands to the playerdealer and checking score calculation
   b. Checking manual inputs other than H and S
   c. Checking that games ends and records results successfully upon player or dealer busting
   d. Checking that an initial Blackjack (21 points) ends the game and results in a win for the player
   e. Checking that the dealer's behavior is as expected (hitting until 17)
