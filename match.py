import random

class Match:

    def __init__(self, mapa, taskList, players, sus):
        self.mapa = mapa
        self.taskList = taskList
        self.players = players
        self.sus = sus


    def startMatch(self, players, sus):        

        taskList = {
            "Skeld":["Card swipe", "Reactor", "Navigation",
            "Cables", "02 filter", "Clean Vent", "Electric"
            ],
            "Mira HQ":("ID Code", "Power", "Fuel", "Shields",
            "Process data", "Diagnostics", "Scan"
            ),
            "Polus":("Data", "Artifacts", "Reactor", "Calibrate",
            "Toilet", "Decontaminate", "Keys"
            )
        }
        
        map_option = random.choice(taskList.value)
        taskList = tuple(taskList.keys)

        if players + sus < 10:
            print(f"The game will start on the map {map_option} with {players} players and {sus} impostors")
        else:
            print(f"Select the correc amount of crewmates and impostors to start")

    def finishMatch(self, players, sus, tasksCompleted):
        if sus == 0 or tasksCompleted == int(players * 4):
            print(f"Crewmates win")
        
        elif sus == players:
            print(f"Impostors win")
        


        
