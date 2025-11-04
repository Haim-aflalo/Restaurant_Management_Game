
from staff_members.staff import Staff


class Chef(Staff):

    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.speciality = "French"

    def cook_order(self,order):
        order.status = "cooking"
        self.work()
        order.status = "ready"

    def override_work(self):
        self.energy -= 15