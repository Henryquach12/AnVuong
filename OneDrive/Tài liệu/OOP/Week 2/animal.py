class Snake:
    def __init__(self, name, nickname, sound):
        self.name = name
        self.nickname = nickname
        self.sound = sound

    def speak(self):
        print(self.sound)

    def coil(self):
        print(f"{self.name} coils up its own body")

snake = Snake("long boi", "lb", "")

class Cat:
    def __init__(self, name, nickname, sound):
        self.name = name
        self.nickname = nickname
        self.sound = sound
        self.location = []

    def speak(self):
        print(self.sound)

    def explore(self, location):
        self.location.append(location)
        print(f"{self.name} is exploring {location}")

cat = Cat('doraemon', 'dorae', 'moew')
cat.speak()
cat.explore("japan")
cat.explore("vietnam")
print(cat.location)

class Mouse:
    def __init__(self, name, nickname, sound, cheese = 0):
        self.name = name
        self.nickname = nickname
        self.sound = sound
        self.cheese = cheese

    def speak(self):
        print(self.sound)
    def collect(self):
        self.cheese += 1
        print(self.cheese)

    def deposit(self):
        self.cheese -= 1
        print(self.cheese)
        
mouse = Mouse('jerry', 'lil j', 'chit')
mouse.speak()
mouse. collect()
mouse. deposit()

class sheep:
    def __init__(self, name, nickname, sound):
        self.name = name
        self.nickname = nickname
        self.sound = sound
        self.min_hunger = 0
        self.max_hunger = 100
        self.current_hunger = 67

    def speak(self):
        print(self.sound)

    def eat(self, nutrition):
        if nutrition < 0:
            print("I cannot eat this non-nutritious meal")
        elif self.current_hunger - nutrition < self.min_hunger:
            print("That is too much food to consume")
        else:
            self.current_hunger -= nutrition 
            print(self.current_hunger) 

sheep1 = sheep("doli", "dl", "bar")
sheep1.speak()
sheep1.eat(20)

class Cow:
    def __init__(self, name, nickname, sound, milk=0):
        self.name = name
        self.nickname = nickname
        self.sound = sound
        self.milk = milk
    def speak(self):
        print(self.sound) 
    def produce(self):
        self.milk += 10
        print(self.milk)
        if self.milk >= 30:
            self.milked()
    def milked(self):
        self.milk = 0

    
cow1 = Cow("trueMilk", "th", "umbo", 0)
cow1.speak()
cow1.produce()
cow1.produce()
cow1.produce()
cow1.produce()
