from GPU import GPU
from CPU import CPU
from RAM import RAM
class Motherboard:
    def __init__(self, make: str, model: str, brand: str, socket: str, chipset: str):
        self.__make = make
        self.__model = model
        self.__brand = brand 
        self.__socket = socket
        self.__chipset = chipset
        self.__cpu = None
        self.__gpu = None
        self.__ram = []
    def get_name(self) -> str:
        return self.__model 
    def get_gpu(self) -> GPU:
        return self.__gpu
    def get_cpu(self) -> CPU: 
        return self.__cpu
    def install_cpu(self, cpu: CPU):
        if isinstance(cpu, CPU):
            self.__cpu = cpu
    def install_gpu(self, gpu: GPU):
        if isinstance(gpu, GPU):
            self.__gpu = gpu
    def install_ram(self, ram: RAM):
        if isinstance(ram, RAM):
            self.__ram.append(ram)
    def __str__(self):
        return f"{self.__brand} {self.__model} {self.__socket} ({self.__chipset}) | CPU: {self.get_cpu()} | GPU: {self.get_gpu()} | RAM: {self.__ram}"
