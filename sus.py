import time
from itertools import count
import random
from match import Match
from amogus import Amogus

class Sus(Amogus):
    counter = 0 #Counter for number of impostors
    
    def __init__(self, name, tasksToDo = None, colour = str):
        super().__init__(name, tasksToDo = None, colour = str)
        visibility = 40
        Sus.counter += 1
        self.id = Sus.counter

    def killTripulant(self):
        print(input("Enter the player you would like to kill, or if you want to cancel the action. "))
        while Amogus.counter != 0:
            print(f"Kill player {Amogus.counter}?\n")
            counter -= 1

        decision = input() 
        if type(decision) == int:
            pass
        if decision == "cancel":
            return

    def sabotage(self):
        visibility -= 30
        countdown(t = 30)
        def countdown(t):
            print("The current sabotage is going to be active for 30 seconds.")
            while t:
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r")
                time.sleep(1)
                t -= 1

    def travelVent(self):
        visibility += 30

    def reportBody(self):        
        Match.meeting()
