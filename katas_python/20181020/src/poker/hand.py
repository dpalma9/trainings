# -*- coding: utf-8 -*-
from poker.card import Card
from poker.exceptions import DuplicatedCardError

class Hand(object):

    def __init__(self,hand):
       hand=hand.split(" ")
       self.hand=hand
       self.check_cards_in_hand()
       self.rank()

    def rank(self):
       self.check_if_rep_cards()
       self.high_card()

    def check_cards_in_hand(self):
       for card in self.hand:
        card=Card(card)

    def check_if_rep_cards(self):
       hand_=[]
       rep_hand=[]

       for i in self.hand:
           if i not in hand_:
               hand_.append(i)
           else:
               if i not in rep_hand:
                   rep_hand.append(i)

       if len(rep_hand) > 0:
           raise DuplicatedCardError()

    def high_card(self):
        order=['2','3','4','5','6','7','8','9','J','Q','K','A']
        #suits=['S','H','C','D']
        new=[]

        #hand=hand[0].split(" ")
        for i in self.hand:
            new.append(i[0])

        ordenado=sorted(new, key=lambda new: order.index(new[0]))
        high=ordenado[len(ordenado)-1]

        for i in self.hand:
            if high == i[0]:
                highC=i
    
        return highC


# class DuplicatedError(Exception):
#     pass

# def Hand(hand):

#     # TO DO
#     #for i in len(hand):
#     #    Check_card(hand[i].split(" "))
        
#     hand1=hand[0].split(" ")
#     hand2=hand[1].split(" ")

#     Check_card(hand1)
#     Check_card(hand2)
#     #print ("Hand1: " + str(hand1))
#     #print ("Hand2: " + str(hand2))

#     if card_rep(hand1,hand2):
#         print ("Jugada válida")
#         print ("High Card: " + str(highCard(hand1)))
#     else:
#         print ("Mierda pa' ti, tramposo")

# def Check_card(hand):

#     for card in hand:
#         Card(card)

# def card_rep(hand1, hand2):
    
#     rep=[i for i, j in zip(hand1,hand2) if i == j]
#     hand_1=[]
#     rep_hand_1=[]
#     hand_2=[]
#     rep_hand_2=[]
    
#     for i in hand1:
#         if i not in hand_1:
#             hand_1.append(i)
#         else:
#             if i not in rep_hand_1:
#                 rep_hand_1.append(i)
    
#     for i in hand2:
#         if i not in hand_2:
#             hand_2.append(i)
#         else:
#             if i not in rep_hand_2:
#                 rep_hand_2.append(i)
    
#     if not rep_hand_1 and not rep_hand_2 and not rep:
#         return True
#     else:
#         return False
    
# def highCard(hand):
#     order=['2','3','4','5','6','7','8','9','J','Q','K','A']
#     #suits=['S','H','C','D']
#     new=[]

#     #hand=hand[0].split(" ")
#     for i in hand:
#         new.append(i[0])

#     ordenado=sorted(new, key=lambda new: order.index(new[0]))
#     high=ordenado[len(ordenado)-1]

#     for i in hand:
#         if high == i[0]:
#             highC=i
    
#     return highC


#hand=['2D 2S 4Q 4K 4K','2D 2S 4Q 6K 4Q']
#Hand(hand)
#hand=["2S 3D 4D KH QD", "2H 4S 3H 7D 8D"]
#Hand(hand)