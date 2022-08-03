import random

class Tasks:

    def __init__(self):
        #Has the maps and assigned task for each map in order to make the 
        #Assignation at the start of the game
        self.map_options = {
            "Skeld":("Card swipe", "Reactor", "Navigation",
            "Cables", "02 filter", "Clean Vent", "Electric"
            ),
            "Mira HQ":("ID Code", "Power", "Fuel", "Shields",
            "Process data", "Diagnostics", "Scan"
            ),
            "Polus":("Data", "Artifacts", "Reactor", "Calibrate",
            "Toilet", "Decontaminate", "Key turn"
            )
        }

    def giveMap(self, map_option):
        #This method selects a random map then stores the 
        #tasks assigned to that map
        map_choice = random.choice(map_option.keys)
        task_list = map_option[map_choice]
        self.giveTask(task_list)
        #calls giveTask method using the task_list from the dictionary


    def giveTask(self, task_list):
         
        max_tasks = 1
        while max_tasks <= 4:
            tasksToDo = tasksToDo.append(random.choice(task_list))
            max_tasks += 1
            if tasksToDo[max_tasks] in tasksToDo:
                tasksToDo.pop(max_tasks)
                max_tasks -= 1
        #Assigns tasks from task_list until 4 are choosen. 
        #If a task is going to be repeated, it repeats the process
        # in order to avoid the same task twice on the same player. 