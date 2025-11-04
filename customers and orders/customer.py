class Customer:

    def __init__(self,name):
        self.name = name
        self.satisfaction = 50

    def increase_satisfaction(self,amount):
        if  self.satisfaction + amount <= 100:
            self.satisfaction += amount
        else:
            print("the satisfaction cannot exceed 100")

    def decrease_satisfaction(self,amount):
        if self.satisfaction - amount >= 0:
            self.satisfaction -= amount
        else:
            print("the satisfaction cannot be under 0")

    def is_happy(self):
        return self.satisfaction > 70

    def get_info(self):
        return f"the satisfaction of {self.name} is {self.satisfaction}"


