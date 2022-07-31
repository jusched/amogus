import time
import random
from match import Match
from amogus import Amogus

class Sus(Amogus):
    counter = 0 #Counter for number of impostors
    
    def __init__(self, name, tasksToDo = None, colour = str):
        super().__init__(name, tasksToDo = None, colour = str)
        self.visibility = 40
        Sus.counter += 1
        self.id = Sus.counter

    def killTripulant(self):
        input("Enter the player you would like to kill, or if you want to cancel the action. \n")

        decision = input() 
        for i in self.player_list:
            print(i)
        if decision in self.player_list:
            del self.player_list[decision]
            self.visibility += 40
            countdown(t = 5)
            def countdown(t):
                print("You will be more visible for 5 seconds. ")
                while t:
                    mins, secs = divmod(t, 60)
                    timer = '{:02d}:{:02d}'.format(mins, secs)
                    print(timer, end="\r")
                    time.sleep(1)
                    t -= 1
            return
            
        elif decision == "cancel":
            return
        else:
            print("Enter a valid name or the 'cancel' word correctly. ")

        

    def sabotage(self):
        self.visibility -= 35
        countdown(t = 30)
        def countdown(t):
            print("The current sabotage is going to be active for 30 seconds.")
            while t:
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r")
                time.sleep(1)
                t -= 1
            return

    def travelVent(self):
        self.visibility += 30
        countdown(t = 5)
        def countdown(t):
            print("You will be more visible for 5 seconds. ")
            while t:
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r")
                time.sleep(1)
                t -= 1
        return

    def reportBody(self):        
        Match.meeting()
