import random

class Tasks:

    def __init__(self):
        self.map_option = {
            "Skeld":["Card swipe", "Reactor", "Navigation",
            "Cables", "02 filter", "Clean Vent", "Electric"
            ],
            "Mira HQ":("ID Code", "Power", "Fuel", "Shields",
            "Process data", "Diagnostics", "Scan"
            ),
            "Polus":("Data", "Artifacts", "Reactor", "Calibrate",
            "Toilet", "Decontaminate", "Key turn"
            )
        }

    def giveMap(self, map_option):
        map_choice = random.choice(map_option.keys)
        task_list = map_option[map_choice]
        self.giveTask(task_list)


    def giveTask(self, task_list):
         
        counter = 0
        while counter != 4:
            tasksToDo = tasksToDo.append(random.choice(task_list))
            counter += 1
