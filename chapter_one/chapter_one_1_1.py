import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrechDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                       for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrechDeck()
# 可以用len查看长度
print(len(deck))
# 可以像列表样取得排这是因为__getitem__
print(deck[0])
# 可以随机抽牌
print(choice(deck))
# 可以迭代
for card in deck:  # doctest:+ELLIPSIS
    print(card)
# 反向迭代
for card in reversed(deck):
    print(card)
# deck是一个类，Card('J','hearts')类里__init__元素的一个子集
if Card('J', 'hearts') in deck:
    print("True")

# 排序
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_values = FrechDeck.ranks.index(card.rank)  # 获取类FrechDeck.ranks.index(card.rank)的下标
    return rank_values * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)
