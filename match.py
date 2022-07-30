from asyncio import tasks
import time
from tasks import Tasks
from amogus import Amogus

class Match:

    def __init__(self, mapa, taskList, players, sus):
        self.mapa = mapa
        self.taskList = taskList
        self.players = players
        self.sus = sus
        self.tasksWin = Amogus.counter


    def startMatch(self, players, sus):  


        if players + sus <= 10 and players <= 7 and sus >= 1:
            print(f"The game will start on the map {Tasks.giveMap} with {players} players and {sus} impostors")
        else:
            print(f"Select the correct amount of crewmates and impostors to start")
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
    
    def meeting(self, players, sus, timer):
        
        votes = 0

    def tasksCompleted(self):
        tasksWin += 1
        if tasksWin == Amogus.counter * 4:
            self.finishMatch(tasksCompleted=tasksWin)
        else:
            return