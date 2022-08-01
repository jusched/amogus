import time
from tasks import Tasks
from amogus import Amogus

class Match:

    def __init__(self, mapa, taskList, players, sus, meet_time):
        self.mapa = mapa
        self.taskList = taskList
        self.players = players
        self.sus = sus
        self.tasksWin = Amogus.counter
        self.meet_time = meet_time


    def startMatch(self, players, sus):  


        if players + sus <= 10 and players <= 7 and sus >= 1:
            print(f"The game will start on the map {Tasks.giveMap} with {players} players and {sus} impostors")
            return
        else:
            print(f"Select the correct amount of crewmates and impostors to start")
            return
        #checks if the number of players is enough to start the match


    def finishMatch(self, tasksCompleted, players, sus):
        if sus == 0 or tasksCompleted == int(players * 4):
            print(f"Crewmates win")
    #after every death, ejection or vote, this method will be run in
    #order to check if the requirements for the end are met
        elif sus == players:
            print(f"Impostors win")
        else:
            return
    
    def meeting(self, players, sus, meet_time):
        self.timer(t=meet_time, text=(f"The meeting will be active for {meet_time} seconds. "))
        votes = {}

    def tasksCompleted(self):
        #Counts the tasks based on the crewmates on the match and verifies 
        # If there are enough tasks in order to finsh the match with victory by
        # Tasks completed
        tasksWin += 1
        if tasksWin == Amogus.counter * 4:
            self.finishMatch(tasksCompleted=tasksWin)
        else:
            return

    def timer(self, t, text):
        print(text)
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        return