class MenuStruct:
    def __init__(self, menuBase, menuIngredient, menuSeasoning):
        self.menuBase = menuBase
        self.menuIngredient = menuIngredient
        self.menuSeasoning = menuSeasoning


class Menu:
    def __init__(self, title, material):
        self.title = title
        self.Material = material


class Material:
    def __init__(self, item, content):
        self.item = item
        self.content = content
