class Egg: 
    def __init__(self, type):
        self.__type = type
    def __str__(self):
        return f"This egg will hatch into a baby {self.__type}"
    