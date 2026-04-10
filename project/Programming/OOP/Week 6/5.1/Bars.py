from Ore import Ore
class Bar:
    def __init__(self, Type, primary_ore=None, secondary_ore=None):
        self.__type = Type
        self.__primary_ore = primary_ore
        self.__secondary_ore = secondary_ore
        self.
    def __eq__(self, bar):
        if isinstance(bar, Bar):
            if bar.__type != self.__type:
                return False
            return (
                bar.__type == self.__type and
                bar.__primary_ore == self.__primary_ore and
                bar.__secondary_ore == self.__secondary_ore)
        return False
    def __str__(self):
        return f"type: {self.__type}, primary ore: {self.__primary_ore}, secondary ore: {self.__secondary_ore}"
    
class Bronze_bar(Bar):
    pass
class Iron_bar(Bar):
    pass
class Steel_bar(Bar):
    pass
class Mithril_bar(Bar):
    pass
class Adamant_bar(Bar):
    pass
class Luminite_bar(Bar):
    pass
class Runite(Bar):
    pass