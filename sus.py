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
        pass

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
