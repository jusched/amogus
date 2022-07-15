class Match:

    def __init__(self, mapa, taskList, players, sus):
        self.mapa = mapa
        self.taskList = taskList
        self.players = players
        self.sus = sus


    def startMatch(self, mapa, players, sus):

        if players + sus < 10:
            print(f"The game will start on the map {mapa} with {players} players and {sus} impostors")
        else:
            print(f"Select the correc amount of crewmates and impostors to start")


    def finishMatch(self, players, sus, tasksCompleted):
        if sus == 0 or tasksCompleted == int(players * 6):
            print(f"Crewmates win")
        
        elif sus == players:
            print(f"Impostors win")
        


        
