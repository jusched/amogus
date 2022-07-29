from itertools import count
from match import Match
import time
import random
from tasks import Tasks

class Amogus():
    counter = 0

    def __init__(self, name, colour):
        self.name = name
        self.colour = colour    
        Amogus.counter += 1
        self.id = Amogus.counter

    def doTask(self):
        task_del = input("Type the task you want to do.")
        if task_del in Tasks.giveTask:
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
        vote_options = []

    def reportBody(self):
        pass

    #Random in order to calculate if another crewmate has seen the killing