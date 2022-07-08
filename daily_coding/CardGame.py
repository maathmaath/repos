import math
import socket
import random

num = {
    'A': 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    'jack': 11,
    'queen': 12,
    'king': 13
}

suit = {
    'club': 'club',
    'diamond': 'diamond',
    'heart': 'heart',
    'spade': 'spade'
}


class Main(object):
    def shuffle(self, deck, shuffled=[]):
        for i in range(len(deck)):
            ch = random.choice(deck)
            deck.remove(ch)
            shuffled.append(ch)
        return shuffled
        # i = random.choice(deck)
        # shuffled.append(i)
        # deck.remove(i)
        # if deck:
        # return self.shuffle(deck=deck, shuffled=shuffled)
        # else:
        # return shuffled

    def deck(self):
        deck = [('joker', 0)]
        for i in suit:
            for j in num:
                deck.append((i, j))
        return deck

    def play(self):
        Deck = []
        nPlayers = int(input("How many players: "))
        nDecks = math.ceil(nPlayers/2)
        for i in range(nDecks):
            Deck.extend(self.deck())
        Deck = self.shuffle(Deck)
        pCards = []
        for i in range(nPlayers):
            pCards.append([])
        for i in range(len(pCards)*13):
            pCards[i % len(pCards)].append(Deck.pop())
        # hold the deck variable at server end.
        # send the pCards to the client.
        # at every round/after one by one enable client to pick a card.


class Server(object):
    def __init__(self):
        pass

    def create_socket(self):
        server = socket.socket()
        server = server.


if __name__ == '__main__':
    game = Main()
    game.play()
