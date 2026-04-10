class Number:
    def square(self, number):
        square_num = number**2
        return square_num
    def parity(self, number):
        if number % 2 == 0:
            print("even")
        else:
            print("odd")
    def average(self, list_num):
        total = 0
        for num in list_num:
            total += num
        average = total / 2
        return average
number = Number()
print(number.square(5))
l = [1,2,3,4]
print(number.average(l))

class Temperature:
    def __init__(self):
        self.celcius = 1.0
    def convert_to_fahrenheit(self):
        fahrenheit = (self.celcius * 9/5) + 32
        return fahrenheit
    def check_is_freezing(self):
        if self.celcius <= 0:
            print("brrrr it's freezing.")
        else:
            print("At least it isn't freezing.")
    def check_weather(self):
        if self.celcius <= 0:
            print("Super Cold.")
        elif self.celcius > 0 and self.celcius < 10:
            print("Cold")
        elif self.celcius > 10 and self.celcius < 18:
            print("slightly cold")
        elif self.celcius > 18 and self.celcius < 25:
            print("Getting warm")
        elif self.celcius > 25 and self.celcius < 35:
            print("Vietname")
        else:
            print("Sunny")
temperature = Temperature()
temperature.convert_to_fahrenheit()
temperature.check_is_freezing()
temperature.check_weather()        
        
    