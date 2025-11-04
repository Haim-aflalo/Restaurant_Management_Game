from customer import Customer

class CreateOrder:

    def __init__(self,customer:Customer,order_number):
        self.customer = customer
        self.order_number = order_number
        self.items = []
        self.status = "pending"
        self.total_price = 0

    def add_item(self,menu_item):
        self.items.append(menu_item)
        self.total_price += menu_item.price

    def remove_item(self,menu_item):
        self.items.remove(menu_item)
        self.total_price -= menu_item.price

    def get_total(self):
        return self.total_price

    def new_status(self,new_status):
        self.status = new_status

    def display_order(self):
        print(f"Customer: {self.customer} ; Order Number: {self.order_number}")
        for j in self.items:
            print(j.get_infos())
        print(f"Total Price: {self.total_price} ; Status: {self.status}")

    def is_complete(self):
        return self.status == "delivered"

