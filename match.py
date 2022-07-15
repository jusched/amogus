class Match:

    def __init__(self, mapa, taskList, players, sus):
        self.mapa = mapa
        self.taskList = taskList
        self.players = players
        self.sus = sus


    def startMatch(self, mapa, players, sus):
        print(f"El juego empezara en el mapa {mapa} con {players} jugadores y {sus} impostores")


    def finishMatch(self, players, sus):
        if sus == 0:
            print(f"Crewmates win")
        
        if sus == players:
            print(f"Impostors win")

        
