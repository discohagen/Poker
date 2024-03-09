from random import shuffle
from typing import List
from Card import Card


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def draw(self) -> Card | None:
        if len(self.cards) == 0:
            return
        return self.cards.pop()
    