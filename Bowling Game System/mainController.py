from Player import Player
from Game import Game

p1 = Player("A")
p2 = Player("B")
p3 = Player("C")
p4 = Player("D")

players = []
players.extend([p1,p2,p3,p4])

g = Game()
index = g.createSession(players)
s1= []
s2= []
s3= []
s4= []
score = 0
import random

for i in range(0, 20):
    score = random.randint(0,9)
    s1.append(score)
    g.roll(index, p1,score)

    score = random.randint(0,9)
    s2.append(score)
    g.roll(index, p2,score)

    score = random.randint(0,9)
    s3.append(score)
    g.roll(index, p3,score)

    score = random.randint(0,9)
    s4.append(score)
    g.roll(index, p4,score)


print("Player 1 scores: ", s1)
print("Player 2 scores: ", s2)
print("Player 3 scores: ", s3)
print("Player 4 scores: ", s4)

g.declareWinner(index)

g.createSession(players)
g.createSession(players)
g.createSession(players)
g.createSession(players)


