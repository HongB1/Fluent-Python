import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])  # 개별 카를 나타내는 클래스


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')  # 인스턴스로 생성되지 않아도 접근 가능 (ex) FrenchDeck.ranks
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    beer_card = Card('7', 'diamonds')
    print("``beer_card``: ", beer_card)
    
    deck = FrenchDeck()
    print("The length of ``deck``: ", len(deck))
    print("The first card in ``deck``: ", deck[0])
    print("The last card in ``deck``: ", deck[-1])
    
    print("")
    print("The first three cards: ", deck[:3])
    print("Cards drawn at intervals of 13, starting with index 12: ", deck[12::13])
    
    print("")
    print("Print cards")
    for card in deck:
        print(card)
        
    print("")
    print("Print cards in reverse order")
    for card in reversed(deck):
        print(card)
        
    print("")
    print("``Card('Q', 'hearts')`` in ``deck``? ", Card('Q', 'hearts') in deck)
    print("``Card('7', 'beasts')`` in ``deck``? ", Card('7', 'beasts') in deck)

    print("")
    suit_values = dict(spades=3, hearts=2, diamonds=2, clubs=1)

    
    def spades_high(card):
        """
        1st: Spade Ace
        2nd: Heart Ace 
        3rd: Diamond Ace 
        4th: Club Ace
        5th: Spade 2
        6th: Heart 2
        """
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]
    
    print("Rank of cards")
    for card in sorted(deck, key=spades_high):
        print(card)
