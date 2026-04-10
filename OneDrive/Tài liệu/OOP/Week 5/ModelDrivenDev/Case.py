from Motherboard import Motherboard
from PSU import PSU
from CPU import CPU
from GPU import GPU
from RAM import RAM
class Case:
    def __init__(self, make: str, model: str, brand: str):
        self.__make = make 
        self.__model = model
        self.__brand = brand
        self.__motherboard = None
        self.__psu = None
    def get_motherboard(self) -> Motherboard:
        return self.__motherboard
    def get_psu(self) -> PSU:
        return self.__psu
    def install_motherboard(self, motherboard: Motherboard):
        if isinstance(motherboard, Motherboard):
            self.__motherboard = motherboard
    def install_psu(self, psu: PSU):
        if isinstance(psu, PSU):
            self.__psu = psu
    def __str__(self):
        return f" Case: {self.__brand} {self.__model} {self.get_motherboard() if self.__motherboard else "No Motherboard"}{self.get_psu() if self.__psu else "No PSU"}"

case = Case("NZXT", "H510", "NZXT")
psu = PSU("Corsair", "RM750", "Corsair", 750, "80+ Gold")

cpu = CPU("Intel", "i7-12700K", "Intel", "LGA1700", 12)
ram1 = RAM("Corsair", "Vengeance", "Corsair", "DDR4", 16, 3200)
ram2 = RAM("Corsair", "Vengeance", "Corsair", "DDR4", 16, 3200)
gpu = GPU("Nvidia", "RTX 4070", "Nvidia", 12, 25)

motherboard = Motherboard("ASUS", "ROG", "ASUS", "LGA1700", "Z690")
motherboard.install_cpu(cpu)        
motherboard.install_gpu(gpu)
motherboard.install_ram(ram1)
motherboard.install_ram(ram2)

case.install_motherboard(motherboard)
case.install_psu(psu)

print(case)