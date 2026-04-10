from employee import Employee, employee1

class DigitalArtist(Employee):
    def __init__(self, ID, name, profession, software):
        super().__init__(ID, name, profession)
        self.__software = software 
        self.__suite = [self.__software]
    def get_suite(self):
        for i in self.__suite:
            print(i)
    def work(self):
        super().work()
        print(f"I am a {self.get_profession()} and I am using {self.__software}")
    def learn_software(self, software):
        self.__suite.append(software)

digital_artist = DigitalArtist(1, 'Hao', 'Digital Artist', 'Canva')
digital_artist.learn_software('Capcut')
digital_artist.work()