from MenuClass import MenuTmp, Material


class MenuScrapingRepository:
    def __init__(self, page):
        self.page = page


    def getMenu(self, menuIdList):
        menu = []

        for index, menuId in enumerate(menuIdList):
            self.page.goto(f"https://park.ajinomoto.co.jp/recipe/card/{menuId}/")

            recipeCardXpath = (
                "xpath="
                "html/body/"
                "div[@class='chFixed']/"
                "div[@class='searchView']/"
                "div[@id='content']/"
                "article[@id='recipeCard']/"
            )

            menuTitleLocator = self.page.locator(
                recipeCardXpath +
                "div[@class='recipeArea']/"
                "div[@class='recipeTitleAreaType02']/"
                "div[@class='wrap1160']/"
                "div[@class='in_table']/"
                "h1[@class='recipeTitle']/"
                "span"
            )
            menuTitle = menuTitleLocator.all_inner_texts()

            menuIngredientItemLocator = self.page.locator(
                recipeCardXpath +
                "div[@class ='recipeCardSpOrderWrap']/"
                "div[@class ='wrap820 recipeCardSpOrder1']/"
                "div[@class ='recipeMaterialType02']/"
                "div[@class ='recipeMaterialList']/"
                "dl/dt"
            )
            menuIngredientItem = menuIngredientItemLocator.all_inner_texts()

            menuIngredientQuantityLocator = self.page.locator(
                recipeCardXpath +
                "div[@class ='recipeCardSpOrderWrap']/"
                "div[@class ='wrap820 recipeCardSpOrder1']/"
                "div[@class ='recipeMaterialType02']/"
                "div[@class ='recipeMaterialList']/"
                "dl/dd"
            )
            menuIngredientQuantity = menuIngredientQuantityLocator.all_inner_texts()

            menu.append(
                MenuTmp(
                    menuTitle[len(menuTitle) - 1],
                    Material(
                        menuIngredientItem,
                        menuIngredientQuantity,
                    )
                )
            )

        return menu
