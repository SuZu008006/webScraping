class MenuStruct:
    def __init__(self, menuBase, menuIngredient):
        self.menuBase = menuBase
        self.menuIngredient = menuIngredient


class Menu:
    def __init__(self, title, ingredient):
        self.title = title
        self.Ingredient = ingredient


class Ingredient:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity
