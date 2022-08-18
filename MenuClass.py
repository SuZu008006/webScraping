

class MenuStructTmp:
    def __init__(self, menu, ingredient, seasoning):
        self.menu = menu
        self.menu = ingredient
        self.menu = seasoning

class MenuTmp:
    def __init__(self, title, material):
        self.title = title
        self.Material = material


class Material:
    def __init__(self, item, content):
        self.item = item
        self.content = content


class MenuStruct:
    def __init__(self, menuRecord, ingredientRecord, seasoningRecord):
        self.menuRecord = menuRecord
        self.ingredientRecord = ingredientRecord
        self.seasoningRecord = seasoningRecord

    class Menu:
        def __init__(self, title):
            self.title = title
    class Ingredient:
        def __init__(self, item, quantity, scale):
            self.item = item
            self.quantity = quantity
            self.scale = scale
    class Seasoning:
        def __init__(self, item, quantity, scale):
            self.item = item
            self.quantity = quantity
            self.scale = scale
