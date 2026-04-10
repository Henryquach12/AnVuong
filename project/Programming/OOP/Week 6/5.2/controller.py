from character import Character
class Controller:
    def __init__(self, character: Character):
        self.__triggers = []
        self.__action_buttons = []
        self.__directional_buttons = []
        self.__character = character 