from Bars import Bar
from Ore import *
class Forge:
    def __init__(self):
        self.__bars = [] 
    
    def get_bars(self):
        return self.__bars
    
    bars = property(get_bars)
    
    def smelting(self, ore1, ore2):
        if not isinstance(ore1, Ore) or not isinstance(ore2, Ore):
            return False
        forge = {
            (Tin, Copper): 'Bronze Bar',
            (Iron, Iron): 'Iron Bar',
            (Iron, Coal): 'Steel Bar',
            (Mithril, Coal): 'Mithril Bar',
            (Adamantite, Luminite): 'Steel Bar',
            (Adamantite, Luminite): 'Rune Bar'
            }
        bar = forge.get((type(ore2), type(ore1))) or forge.get((type(ore1), type(ore2)))
        if bar:
            new_bar = Bar(bar, ore1, ore2)
            self.__bars.append(new_bar)
        else:
            return False
        
    def __str__(self):
        description = "A forge containing:\n"
        if len(self.__bars) == 0:
            description += "- No bars smelted.\n"
        else:
            for bar in self.__bars:
                description += "- " + str(bar) + "\n"
        return description
        
tin = Tin()
copper = Copper()
forge = Forge()

forge.smelting(copper, tin)


print(forge)