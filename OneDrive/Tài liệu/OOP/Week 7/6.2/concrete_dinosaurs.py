class Dinasour: 
    def __init__(self, name, sex, age, egg):
        self.__name = name 
        self.__sex = sex
        self.__age = age
        self.__egg = []
    def set_name(self, name):
        self.__name = name
    def lay_egg(self):
        if self.__sex == "Female":
            if self.__age == 4:
                from egg import Egg
                egg = Egg(self.__class__.__name__)
                self.__egg.append(egg)
    def warm_egg(self):
        if self.__egg:
            print('Hatch')
        else: 
            print('Sit on')
    def name_baby(self, dinasour, name):
        if isinstance(dinasour, Dinasour):
            return dinasour.set_name(name)
    def __str__(self):
        
        