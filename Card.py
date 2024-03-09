class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]
    ranks = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, rank: int, suit: int) -> None:
        self.rank = rank
        self.suit = suit

    def __lt__(self, card2: 'Card') -> bool:
        return self.rank > card2.rank or (self.rank == card2.rank and self.suit < card2.suit)
    
    def __gt__(self, card2: 'Card') -> bool:
        return (card2 < self)

    def __repr__(self) -> str:
        return self.ranks[self.rank] + " of " + self.suits[self.suit]