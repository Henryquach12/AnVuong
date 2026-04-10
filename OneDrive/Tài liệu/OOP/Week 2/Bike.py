class Bike:
    def __init__(self, Btype, maxGear=6, currentGear=1):
        self.Btype = Btype
        self.maxGear = maxGear
        self.currentGear = currentGear
    def adjustGear(self, adjust):
        if adjust == True and self.currentGear < self.maxGear:
            self.currentGear += 1 
            print(f"The bike is increased the gear. current gear: {self.currentGear}")
        elif adjust == False and self.currentGear > 1:
            self.currentGear -= 1
            print(f"The bike is decreased the gear. current gear: {self.currentGear}")
        else:
            print(f"The current gear is unavailable to adjust")

class Cyclist:
    def __init__(self, name, age, weight, proficiency, protectGear=False):
        self.name = name
        self.age = age
        self.weight = weight
        self.proficiency = proficiency
        self.protectGear = protectGear
    def accelerate(self):
        print("Speed up")
    def brakes(self):
        print("stop")
    def turning(self, turn):
        print(f"you are turning {turn}")
    def wearGear(self):
        self.protectGear = True
        print(f"you are wearing protectGear: {self.protectGear}")

bike1 = Bike("electric", 7, 2)
bike1.adjustGear(True)

cyclist1 = Cyclist("Hao", "18", "100", "Racer", False)

cyclist1.accelerate()
cyclist1.brakes()
cyclist1.turning("right")
cyclist1.wearGear()

    