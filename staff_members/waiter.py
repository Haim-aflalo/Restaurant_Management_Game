from customers_and_orders import customer
from customers_and_orders.order import CreateOrder
from menu_and_items.menu import Menu
from staff_members.staff import Staff


class Waiter(Staff):

    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.tips = 0

    @staticmethod
    def take_order(customer,menu):
        order = CreateOrder(customer,0)
        menu.display_menu()
        choice = input("what would you like to eat ?")
        for plat in menu.items:
            if choice == plat.name:
                order.add_item(plat)
        return order

    @staticmethod
    def serve_order(order):
        order.status = "delivered"
        choice1 = input("would you like to increase or decrease satisfaction (i/d)").lower()
        if choice1 == "i":
            choice2 = int(input("how much"))
            customer.increase_satisfaction(choice2)

    def receive_tip(self,amount):
        self.tips += amount

    def get_total_earnings(self):
        return self.salary + self.tips

