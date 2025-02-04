# wd.1.3.3

War game - Turing College WD.1.3.3

At the start of the game, the deck is generated from a dictionary containing all 13 different cards as keys and their strength as values.

Then that dictionary is looped through 4 times so the full deck can be generated and saved as a list with only the cards' names.

That list is then shuffled randomly and the halves are given to the players.

Then the players decide when to reveal the first card of their stacks.

If there's no 'war', the winning player adds both cards to the bottom of their stack and the game continues once the players decide to reveal the next card.

If there's a war, 2 additional cards are drawn from each player's stack, but only one of them is revealed.

If one of the revealed cards is stronger than the other, the 'war' is over and the winning player takes all cards that are not in the stacks. Otherwise, the war continues.

If a player is out of cards during a war, that player loses the game. AAAAAAAAAAA
