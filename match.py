import random

class Match:

    def __init__(self, mapa, taskList, players, sus):
        self.mapa = mapa
        self.taskList = taskList
        self.players = players
        self.sus = sus


    def startMatch(self, players, sus, taskList):

        if players + sus < 10:
            print(f"The game will start on the map {map_choice} with {players} players and {sus} impostors")
        else:
            print(f"Select the correc amount of crewmates and impostors to start")

        map_option = ("Skeld", "Mira HQ", "Polus")
        map_choice = random.choice(map_option)

        taskList = {
            "Skeld":("Card swipe", "Reactor", "Navigation",
            "Cables", "02 filter", "Clean Vent", "Electric"
            ),
            "Mira HQ":("ID Code", "Power", "Fuel", "Shields",
            "Process data", "Diagnostics", "Scan"
            ),
            "Polus":("Data", "Artifacts", "Reactor", "Calibrate",
            "Toilet", "Decontaminate", "Keys"
            )

        }

    def finishMatch(self, players, sus, tasksCompleted):
        if sus == 0 or tasksCompleted == int(players * 4):
            print(f"Crewmates win")
        
        elif sus == players:
            print(f"Impostors win")
        


        
