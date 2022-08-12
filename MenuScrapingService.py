from MenuClass import MenuStruct


class MenuScrapingService:
    def __init__(self, menuScrapingRepository):
        self.menuBase = []
        self.menuIngredient = []
        self.ingredientMasterIndex = 0
        self.menuScrapingRepository = menuScrapingRepository

    def convertMenu(self, menuIdList):
        menuList = self.menuScrapingRepository.getMenu(menuIdList)
        for menuIndex, menu in enumerate(menuList):
            self.menuBase.append(
                [
                    menuIndex + 1,
                    menu.title,
                ]
            )
            for ingredientIndex, ingredient in enumerate(menu.Ingredient.item):
                self.menuIngredient.append(
                    [
                        self.ingredientMasterIndex + 1,
                        menuIndex + 1,
                        menu.Ingredient.item[ingredientIndex],
                        menu.Ingredient.quantity[ingredientIndex],
                    ]
                )
                self.ingredientMasterIndex = self.ingredientMasterIndex + 1

        return MenuStruct(
            self.menuBase,
            self.menuIngredient,
        )

