from match import Match
from amogus import Amogus

class Sus(Amogus):
    counter = 0 #Counter for number of impostors
    
    def __init__(self, name, tasksToDo = None, colour = str):
        super().__init__(name, tasksToDo = None, colour = str)
        self.visibility = 1
        Sus.counter += 1
        self.id = Sus.counter

    def killTripulant(self):
        input("Enter the player you would like to kill, or if you want to cancel the action. \n")

        decision = input() 
        for i in self.player_list:
            print(i)
        if decision in self.player_list:
            del self.player_list[decision]
            self.visibility += 60
            t = 10
            Match.timer(self, t,text=(f"You will be more visible for {t} seconds. "))
            
        elif decision == "cancel":
            return
        else:
            print("Enter a valid name or the 'cancel' word correctly. ")

    def sabotage(self):
        self.visibility -= 35
        t = 30
        Match.timer(self, t, text=(f"The sabotage will be active for {t} seconds. "))
        return

    def travelVent(self):
        self.visibility += 25
        t = 5
        Match.timer(self, t, text=(f"You will be more visible for {t} seconds. "))
        return
