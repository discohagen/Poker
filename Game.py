from Card import Card
from Deck import Deck
from Player import Player


class Game:
    def __init__(self) -> None:
        #name = input("Player name: ")
        name = "test"
        self.deck = Deck()
        self.player = Player(name)

    def play_game(self) -> None:
        self.__give_player_cards(5)
        self.player.hand = [Card(6, 1), Card(12, 3), Card(3, 3), Card(12, 2), Card(3, 0)]
        print(self.player)
        
    def __give_player_cards(self, num: int) -> None:
        for _ in range(num):
            self.player.hand.append(self.deck.draw())