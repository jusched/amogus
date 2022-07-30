from itertools import count
from match import Match
import time
import random
from tasks import Tasks

class Amogus():
    counter = 0

    def __init__(self, name):
        #After initializing the class, the players must have a name. 
        # Also, the counter is to check if the criteria for win/lose is met.

        self.name = name
        Amogus.counter += 1
        self.id = Amogus.counter

    def doTask(self):
        #Does tasks for each player 
        task_del = input("Type the task you want to do.")
        if task_del in Tasks.giveTask():
            countdown(t = 10)
        else:
            return
        def countdown(t):
            while t:
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r")
                time.sleep(1)
                t -= 1
                print(f"Doing task, {t} seconds remaining")
            

    def callMeeting(self, players, sus, timer):
        self.meeting(players, sus, timer)


    def vote(self):
        vote_options = list(Match.player_list)
        for i in vote_options:
            print(i)
        print("Type the person you want to give your vote to, even yourself: ")

    def reportBody(self):
        self.callMeeting()

    #Random in order to calculate if another crewmate has seen the killing