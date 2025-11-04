from menu import MenuItem


class Menu:

    def __init__(self):
        self.items = []

    def add_items(self,menu_item:MenuItem):
        self.items.append(menu_item)

    def remove_item