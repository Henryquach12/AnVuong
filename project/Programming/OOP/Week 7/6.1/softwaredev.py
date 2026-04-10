from employee import Employee, employee1

class SoftwareDev(Employee):
    def __init__(self, ID, name, profession, language):
        super().__init__(ID, name, profession)
        self.__language = language
        self.__programming_languages = [self.__language]
    def get_language(self):
        for i in self.__programming_languages:
            print(i)
    def work(self):
        super().work()
        print(f"I am doing {self.get_profession()} and I use {self.__language}")
    def add_language(self, language):
        self.__programming_languages.append(language)
        
software = SoftwareDev(2, 'Quach', 'soft dev', 'Python')
software.add_language('Java')
print(software.work())