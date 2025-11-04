class Staff:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        self.energy = 100

    def work(self):
        self.energy -= 10
        print("Working...")

    def rest(self):
        self.energy += 20
        if self.energy > 100:
            self.energy = 100

    def is_tired(self):
        return self.energy < 30

    def get_info(self):
        return f"Name: {self.name} ; Salary: {self.salary} ; Energy: {self.energy}"

