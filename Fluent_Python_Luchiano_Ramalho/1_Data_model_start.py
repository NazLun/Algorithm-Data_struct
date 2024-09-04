import accessify
import collections
import random
# import traceback        # traceback.format_exc()

# from accessify import protected, private
# from collections import namedtuple


class FrenchDeck:

    # creating a custom datastruct
    Card = collections.namedtuple(
        typename='Card',
        field_names=['rank', 'suit']
    )

    _rank = [i for i in range(2, 11)] + list('JQKA')
    _suit = 'spades diamonds clubs hearts'.split()
    __private_attr = 345

    def __init__(self):
        self._cards = [
            self.Card(rank=rank, suit=suit)
            for rank in self._rank
            for suit in self._suit
        ]

    @accessify.private
    @classmethod
    def __private_meth(cls):
        return 'private!'

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        try:
            return self._cards[position]
        # except KeyError:
        #     raise KeyError('Не найдено значение по переданному ключу')
        except IndexError:
            raise IndexError('Передаваемое значение должно быть в диапазоне 0-51 включительно')
        except TypeError:
            raise TypeError('Допускается вставка только целых чисел')

    def get_random_card(self):
        return random.choice(self._cards)


koloda = FrenchDeck()
print(f'length: {len(koloda)}')
x = 45
print(f'position {x}: {koloda[x]}')

for card in koloda[3:8]:
    print(f'rank: {card.rank}; suit: {card.suit}')

print()
print(f'random card: {koloda.get_random_card()}')
print(dir(koloda))
# print(f'private meth: {koloda._FrenchDeck__private_meth()}')
# EXEPTION: FrenchDeck.__private_meth() is inaccessible due to its protection level

