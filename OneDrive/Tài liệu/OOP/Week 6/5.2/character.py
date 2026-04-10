class Character:
    def __init__(self, name: str, arrows = 6, is_jumping = False):
        self.__name = name
        self.__arrows = arrows 
        self.__is_jumping = is_jumping
    
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    name = property(get_name, set_name)
    
    def get_arrows(self):
        return self.__arrows
    def set_arrows(self, arrow):
        self.__arrows = arrow
    arrows = property(get_arrows, set_arrows)
    
    def get_is_jump(self):
        return self.__is_jump
    def jump(self):
        self.__is_jumping = True
    jump = property(get_is_jump, jump)
    
    def dodge(self):
        print(f"{self.__name} doge!")
    
    def aim_bow(self):
        print(f"{self.__name} start aiming!")
    
    def shoot_arrow(self):
        if self.__arrows <= 0:
            print("No arrow left!")
            return  
        print(f"{self.__name} is shooting arrow!")
    
    def craft_arrow(self):
        print("Start crafting arrow..")
        self.__arrows += 1
        return 
    
    def display_quiver(self):
        print("Showing quiver..")
    
    
        
        
        
        
        
        
        