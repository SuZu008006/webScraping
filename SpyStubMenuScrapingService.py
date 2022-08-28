from MenuClass import MenuStruct


class SpyStubMenuScrapingService:
    def __init__(self, _):
        self.menu_returnValue = ["", ""]
        self.ingredient_returnValue = 0

    def convertMenu(self, _):
        return [
            MenuStruct(
                MenuStruct.Menu(
                    title=self.menu_returnValue[0],
                    image=self.menu_returnValue[1],
                ).__dict__,
                [
                    MenuStruct.Ingredient(
                        item="test1",
                        quantity=self.ingredient_returnValue,
                        scale="test1",
                    ).__dict__,
                    MenuStruct.Ingredient(
                        item="test2",
                        quantity=self.ingredient_returnValue,
                        scale="test2",
                    ).__dict__,
                ],
                [
                    MenuStruct.Seasoning(
                        item="test3",
                        quantity=self.ingredient_returnValue,
                        scale="test3",
                    ).__dict__,
                ]
            ).__dict__,
        ]
