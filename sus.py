from itertools import count
import random
from match import Match
from amogus import Amogus

class Sus(Amogus):
    counter = 0 #Counter for number of impostors
    
    def __init__(self, name, tasksToDo = None, colour = str):
        super().__init__(name, tasksToDo = None, colour = str)

        Sus.counter += 1
        self.id = Sus.counter

    def killTripulant(self):
        print(input("Enter the player you would like to kill, or if you want to cancel the action. "))
        while Amogus.counter != 0:
            print(f"Kill player {Amogus.counter}\n")
            counter -= 1

        decision = input()

    def sabotage(self):
        visibility += 30
        self.travelVent
        self.killTripulant

    def travelVent(self):
        visibility = 40
        chance = random.randint(0, 100)
        if chance in visibility:
            pass


    def reportBody(self):
        
        self.meeting()
