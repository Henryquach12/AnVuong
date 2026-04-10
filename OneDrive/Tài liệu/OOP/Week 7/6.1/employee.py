from project import Project

class Employee:
    def __init__(self, ID, name, profession, project=None):
        self.__id = ID
        self.__name = name
        self.__profession = profession
        self.__project = project
        self.__project_backlog = []
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_profession(self):
        return self.__profession
    def get_project(self):
        return self.__project
    def assign_project(self, project: Project):
        if isinstance(project, Project):
            self.__project = project
            self.__project_backlog.append(project)
    def swap_project(self, id):
        for project in self.__project_backlog:
            if project.get_id() == id:
                self.__project = project
    def work(self):
        print(f"Current employee is working on {self.__project}")
    def __str__(self):
        return f"Employee: {self.__name}\nProfession: {self.__profession}\nProject: {self.__project.get_title()}"
            
project1 = Project(1, 'Xuat', 'To play with your friend')
project1.set_completed()
print(project1)
 
employee1 = Employee(1, 'Hao', 'Software Dev')
employee1.assign_project(project1)
print(employee1)
        