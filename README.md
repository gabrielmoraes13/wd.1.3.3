# War game - Turing College WD.1.3.3

- Simple card game developed as a pair programming exercise

# Game steps

- At the start of the game, the deck is generated from a dictionary containing all 13 different cards as keys and their strength as values.

- Then that dictionary is looped through 4 times so each card name can be used 4 times to generate a card object from the Class card, which will take the card's value as an attribute with the same name. Every time an object is generated it is appended to a list.

- That list is then shuffled with the help of the random module and the cards from index 0 to index 25 are put into a list named player_one and the cards from index 26 to 51 in a list named player_two.

- The players can then decide when to reveal the first card of their stacks, which is the card in the first index position of their stacks, by inputting 'go'.

  - If the input is not 'go' (case insensitive), an error message is displayed.

- If one card is greater than the other, based on the card object's value attribute, the winning player adds both cards to the bottom of their stack and the game continues once the players decide to reveal the next card.

- If there's a 'war' (a tie):

  - 2 additional cards are drawn from each player's stack, but only one of them is revealed.

  - If one of the revealed cards is stronger than the other, the 'war' is over and the winning player takes all cards that are not in the stacks. Otherwise, the war continues.

  - If a player is out of cards during a war, that player loses the game.

- The game also ends if one of the players has all 52 cards, in which case that player wins.
