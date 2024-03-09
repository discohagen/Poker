from collections import Counter
from typing import List, Tuple
from Card import Card


class Player: #aka Hand
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand: List[Card] = []

    def __lt__(self, hand2: List[Card]) -> bool:
        if self.__get_scoring_hand()[0] < hand2.get_scoring_hand()[0]:
            return True
        elif self.__get_scoring_hand()[0] == hand2.get_scoring_hand()[0]:
            if self.__get_scoring_hand()[1] < hand2.get_scoring_hand()[1]:
                return True
        else:
            return False

    def __gt__(self, hand2: List[Card]) -> bool:
        return not self.__lt__(hand2)

    def __repr__(self) -> str:
        print("---------------")
        print(self.name)
        print(self.hand)
        print(self.__get_scoring_hand())
        return "---------------"
    
    def __get_scoring_hand(self) -> List[int, Card]:
        if self.__is_royal_flush():
            return [9, self.__is_royal_flush()]
        if self.__is_straight_flush():
            return [8, self.__is_straight_flush()]
        if self.__is_quads():
            return [7, self.__is_quads()]
        if self.__is_full_house():
            return [6, self.__is_full_house()]
        if self.__is_flush():
            return [5, self.__is_flush()]
        if self.__is_straight():
            return [4, self.__is_straight()]
        if self.__is_trips():
            return [3, self.__is_trips()]
        if self.__is_two_pairs():
            return [2, self.__is_two_pairs()]
        if self.__is_pair():
            return [1, self.__is_pair()]
        return [0, self.hand.sort(key=lambda card: (card.rank, card.suit))[-1]]

    def __is_royal_flush(self) -> Card | None:
        cards = sorted(card for card in self.hand)
        if all(cards[i].suit == cards[i-1].suit for i in range(1, len(cards))) and all(cards[i].rank == cards[i-1].rank + 1 for i in range(1, len(cards))) and cards[-1].rank == 14:
                return cards[-1]
        return None
    
    def __is_straight_flush(self) -> Card | None:
        cards = sorted(card for card in self.hand)
        if all(cards[i].suit == cards[i-1].suit for i in range(1, len(cards))) and all(cards[i].rank == cards[i-1].rank + 1 for i in range(1, len(cards))):
            return cards[-1]
        return None

    def __is_quads(self) -> Card | None:
        return self.__is_n_of_a_kind(4)
    
    def __is_full_house(self) -> Card | None:
        highest_card_from_pair = self.__is_pair()
        highest_card_from_trips = self.__is_trips()
        if highest_card_from_pair and highest_card_from_trips:
            if highest_card_from_pair > highest_card_from_trips:
                return highest_card_from_pair
            else:
                return highest_card_from_trips
        return None

    def __is_flush(self) -> Card | None:
        cards = sorted(card for card in self.hand)
        if all(cards[i].suit == cards[i-1].suit for i in range(1, len(cards))):
            return cards[-1]
        return None

    def __is_straight(self) -> Card | None:
        cards = sorted(card for card in self.hand)
        if all(cards[i].rank == cards[i-1].rank + 1 for i in range(1, len(cards))):
            return cards[-1]
        return None

    def __is_trips(self) -> Card | None:
        return self.__is_n_of_a_kind(3)

    def __is_two_pairs(self) -> Card | None:
        scoring_cards: List[Card] = []
        grouped_cards = self.__get_cards_with_same_rank_grouped()
        for card_group in grouped_cards:
            if len(card_group) == 2:
                scoring_cards.append(card_group[0])
                scoring_cards.append(card_group[1])
        if len(scoring_cards) == 4:
            scoring_cards.sort(key=lambda card: (card.rank, card.suit))
            return scoring_cards[-1]
        return None

    def __is_pair(self) -> Card | None:
        return self.__is_n_of_a_kind(2)
    
    def __is_n_of_a_kind(self, n: int) -> Card | None:
        grouped_cards = self.__get_cards_with_same_rank_grouped()
        for card_group in grouped_cards:
            if len(card_group) == n:
                card_group.sort(key=lambda card: (card.rank, card.suit))
                return card_group[-1]
        return None
    
    def __get_cards_with_same_rank_grouped(self) -> List[List[Card]]:
        lst: List[List[Card]] = []
        appended = False
        for i in range(5):
            for sub_lst in lst:
                if sub_lst[0].rank == self.hand[i].rank:
                    sub_lst.append(self.hand[i])
                    appended = True
            if not appended:
                lst.append([self.hand[i]])
            appended = False
        return lst