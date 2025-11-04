import random

from customers_and_orders.order import CreateOrder
from menu_and_items import menu


class Restaurant:

    def __init__(self,name):
        self.name = name
        self.menu = menu
        self.staff = []
        self.orders = []
        self.money = 1000

    def hire_staff(self,staff_member):
        self.staff.append(staff_member)

    def fire_staff(self,staff_name):
        for member in self.staff:
            if member.name == staff_name:
                self.staff.remove(member)

    def create_order(self,customer):
        num = random.randrange(1, 99999999999)
        order = CreateOrder(customer,num)
        self.orders.append(order)