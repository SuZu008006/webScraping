

class MenuTmp:
    def __init__(self, title, image, material, make):
        self.title = title
        self.image = image
        self.material = material
        self.make = make

    class Material:
        def __init__(self, item, content):
            self.item = item
            self.content = content
    class Make:
        def __init__(self, content):
            self.content = content

class MenuStruct:
    def __init__(self, menuRecord, ingredientRecord, seasoningRecord, makeRecord):
        self.menuRecord = menuRecord
        self.ingredientRecord = ingredientRecord
        self.seasoningRecord = seasoningRecord
        self.makeRecord = makeRecord

    class Menu:
        def __init__(self, title, image):
            self.title = title
            self.image = image
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
    class Make:
        def __init__(self, content):
            self.content = content
