class Project:
    def __init__(self, id, title, description, completed=False):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__completed = completed
    def get_id(self):
        return self.__id
    def get_title(self):
        return self.__title
    def get_description(self):
        return self.__description
    def get_completed(self):
        return self.__completed
    def set_completed(self):
        self.__completed = True
    def __str__(self):
        return f"Project: {self.__title}\nDescription: {self.__description}\nStatus: {self.__completed}"
    


        