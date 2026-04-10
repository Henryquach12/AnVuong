from Motherboard import Motherboard
from GPU import GPU
class PSU:
    def __init__(self, make: str, model: str, brand: str, wattage: int, efficiency_rating: str):
        self.__make = make
        self.__model = model
        self.__brand = brand
        self.__wattage = wattage
        self.__efficiency_rating = efficiency_rating 
        self.__is_on = False
    def get_on(self) -> bool: 
        return self.__is_on 
    def set_on(self, on):
        self.__is_on = on
    def power_motherboard(motherboard: Motherboard):
        if isinstance(motherboard, Motherboard):
            print("Motherboard power is on")
    def power_gpu(gpu: GPU):
        if isinstance(gpu, GPU):
            print("GPU power is on")
    def __str__(self):
        return f"{self.__brand} {self.__model} {self.__wattage} {self.__efficiency_rating}"
    