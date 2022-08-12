from MenuClass import MenuStruct


class SpyStubMenuScrapingService:
    def __init__(self, _):
        self.menuBaseList_returnValue = []
        self.menuIngredientList_returnValue = []

    def convertMenu(self, _):
        return MenuStruct(
            self.menuBaseList_returnValue,
            self.menuIngredientList_returnValue,
        )
