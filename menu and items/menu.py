class MenuItem:

    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
        self.available = True

    def get_infos(self,name,price,category):
        return f"the product:{self.name} in category: {self.category}, cost {self.price}$"

    def set_available(self, status):
        self.available = status

    def is_available(self):
        return self.available

