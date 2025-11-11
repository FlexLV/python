
class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age=18, job_role="Unknown"):
        super().__init__(name, age)
        self.job_role = job_role

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Job Role:", self.job_role)



a = Employee("Ernests", 20, "DevOps Engineer")


a.display()

