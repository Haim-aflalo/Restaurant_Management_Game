class MenuItem:

    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
        self.available = True

    def get_infos(self):
        return f"Product: {self.name} ; Category: {self.category} ; Price {self.price}$"

    def set_available(self, status):
        self.available = status

    def is_available(self):
        return self.available
