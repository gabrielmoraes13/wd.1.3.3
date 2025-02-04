import random


class Card:
    def __init__(self, card_face, suit):
        self.face = card_face
        match card_face:
            case 'J':
                self.value = 11
            case 'Q':
                self.value = 12
            case 'K':
                self.value = 13
            case 'A':
                self.value = 14
            case _:
                self.value = card_face

        suits = {
            'Spades': '♠',
            'Clubs': '♣',
            'Hearts': '♥',
            'Diamonds': '♦',
        }
        self.suit = suits[suit.capitalize()]

    def __str__(self):
        if self.value != 10:
            return f'''
    ┌─────┐
    |{self.face}    |
    |  {self.suit}  |
    |    {self.face}|
    └─────┘'''
        else:
            return f'''
    ┌─────┐
    |{self.face}   |
    |  {self.suit}  |
    |   {self.face}|
    └─────┘'''

    @property
    def face(self):
        return self._face

    @face.setter
    def face(self, face):
        if face not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']:
            raise ValueError('Invalid card face')
        self._face = face

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value not in range(1, 15):
            raise ValueError('Invalid card value')
        self._value = value

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        if suit not in ['♠', '♣', '♥', '♦']:
            raise ValueError('Invalid suit')
        self._suit = suit


cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']

deck = []

for suit in suits:
    for card in cards:
        card_obj = Card(card, suit)
        deck.append(card_obj)

random.shuffle(deck)
player_one_stack = [card for card in deck[0:26]]
player_two_stack = [card for card in deck[26:]]


def main():
    war_on = False
    game_on = True
    player_one_cards = []
    player_two_cards = []
    while game_on:
        ...


if __name__ == "__main__":
    main()
