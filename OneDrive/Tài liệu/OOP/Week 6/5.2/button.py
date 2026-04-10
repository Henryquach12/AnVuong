from character import Character
class Button:
    def __init__(self, mapping: str):
        self.__mapping = mapping
        
    def get_mapping(self)-> str:
        return self.__mapping
    
    def set_mapping(self, new_map)-> str:
        self.__mapping = new_map
        
    mapping = property(set_mapping, set_mapping)
    
    def __eq__(self)
    
    def on_press(self, character):
        if self.__mapping.strip() == 'A':
            character.jump()
        elif self.__mapping.strip() == 'B':
            character.dodge()
        elif self.__mapping.strip() == 'LT':
            character.aim_bow()
        elif self.__mapping.strip() == 'RT':
            character.shoot_arrow()
        elif self.__mapping.strip() == 'LB':
            character.craft_arrowr()
        elif self.__mapping.strip() == ''
    