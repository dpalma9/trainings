#/usr/bin/python
# -*- coding: utf-8 -*-

class Card(object):
    def __init__(self,card):
        self._check(card)
        self.value=card[0]
        self.suit=card[1]

    def __repr__(self):
        return '<Card: {{ value: {}, suit: {} }}>'.format(self.value, self.suit)

    def _check(self, raw_card):
        values = '23456789JQKA'
        suits = 'SHCD'
        if len(raw_card) != 2:
            raise ValueError()
        elif not (raw_card[0] in values and raw_card[1] in suits):
            raise ValueError()