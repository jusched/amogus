from match import Match
def run(player, sus, timer):
    Match.startMatch(sus = int, players = int)

def player_assign():
    players = int(input("Insert how many players do you want. From 3 to 9: "))

    if players == 9 or players == 3:
        sus = 1
    elif players > 5 and players <= 8:
        sus = int(input("Insert how many sus do you want. From 1 to 2: "))
    elif players == 7:
        sus = int(input("Insert how many sus do you want. From 1 to 3: "))
    
    timer = int(input("""Insert the amount of time the meetings will have:
    
    30 seconds, 60 seconds, 90 seconds or 120 seconds. \n"""))
    if timer != 30 or timer != 60 or timer != 90 or timer != 120:
        print("Please select a valid time for the meeting")

    counter = 1
    player_list = []
    while counter != (players + sus):
        player_list = player_list.append(input(f"Ingresa el nombre del jugador {counter}."))
        counter += 1

    run(players, sus, timer)



if __name__ == "__main__":

    player_assign()



