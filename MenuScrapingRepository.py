import re

from MenuClass import MenuTmp


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

            menuImageLocator = self.page.query_selector(".inImage")
            menuImage = menuImageLocator.inner_html()

            pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
            urlList = re.findall(pattern, str(menuImage))

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

            menuMakeListLocator = self.page.locator(
                recipeCardXpath +
                "div[@class ='recipeCardSpOrderWrap']/"
                "div[@class ='wrap820 recipeCardSpOrder4']/"
                "div[@class ='recipeMakeType02']/"
                "div[@class ='makeList']/"
                "ol/li"
            )
            menuMakeList = menuMakeListLocator.all_inner_texts()

            menu.append(
                MenuTmp(
                    menuTitle[len(menuTitle) - 1],
                    urlList[0],
                    MenuTmp.Material(
                        menuIngredientItem,
                        menuIngredientQuantity,
                    ),
                    MenuTmp.Make(
                        menuMakeList,
                    )
                )
            )

        return menu
