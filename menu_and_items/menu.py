from menu_items import MenuItem

class Menu:

    def __init__(self):
        self.items = []

    def add_items(self, menu_item: MenuItem):
        self.items.append(menu_item)

    def remove_item(self, item_name):
        for i in self.items:
            if i.name == item_name:
                self.items.remove(i)

    def get_item_by_name(self, name):
        for i in self.items:
            if i.name == name:
                return i
        return "not is stock"

    def get_item_by_category(self,category):
        cat_items = []
        for i in self.items:
            if i.category == category:
                cat_items.append(i)
        return cat_items

    def display_menu(self):
        for i in self.items:
            print(f"{i.get_infos()}")


