class Ingredient:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity


class Menu:
    def __init__(self, title, ingredient):
        self.title = title
        self.Ingredient = ingredient


def getMenu(page, menuIdList):
    menu = []

    for index, menuId in enumerate(menuIdList):
        page.goto(f"https://park.ajinomoto.co.jp/recipe/card/{menuId}/")

        recipeCardXpath = (
            "xpath="
            "html/body/"
            "div[@class='chFixed']/"
            "div[@class='searchView']/"
            "div[@id='content']/"
            "article[@id='recipeCard']/"
        )

        menuTitleLocator = page.locator(
            recipeCardXpath +
            "div[@class='recipeArea']/"
            "div[@class='recipeTitleAreaType02']/"
            "div[@class='wrap1160']/"
            "div[@class='in_table']/"
            "h1[@class='recipeTitle']/"
            "span"
        )
        menuTitle = menuTitleLocator.all_inner_texts()

        menuIngredientItemLocator = page.locator(
            recipeCardXpath +
            "div[@class ='recipeCardSpOrderWrap']/"
            "div[@class ='wrap820 recipeCardSpOrder1']/"
            "div[@class ='recipeMaterialType02']/"
            "div[@class ='recipeMaterialList']/"
            "dl/dt"
        )
        menuIngredientItem = menuIngredientItemLocator.all_inner_texts()

        menuIngredientQuantityLocator = page.locator(
            recipeCardXpath +
            "div[@class ='recipeCardSpOrderWrap']/"
            "div[@class ='wrap820 recipeCardSpOrder1']/"
            "div[@class ='recipeMaterialType02']/"
            "div[@class ='recipeMaterialList']/"
            "dl/dd"
        )
        menuIngredientQuantity = menuIngredientQuantityLocator.all_inner_texts()

        menu.append(
            Menu(
                menuTitle[len(menuTitle) - 1],
                Ingredient(
                    menuIngredientItem,
                    menuIngredientQuantity,
                )
            )
        )

    return menu


class MenuStruct:
    def __init__(self, menuBase, menuIngredient):
        self.menuBase = menuBase
        self.menuIngredient = menuIngredient


def convertMenu(menuList):
    menuBase = []
    menuIngredient = []
    ingredientMasterIndex = 0

    for menuIndex, menu in enumerate(menuList):
        menuBase.append(
            [
                menuIndex+1,
                menu.title,
            ]
        )
        for ingredientIndex, ingredient in enumerate(menu.Ingredient.item):
            menuIngredient.append(
                [
                    ingredientMasterIndex+1,
                    menu.Ingredient.item[ingredientIndex],
                    menu.Ingredient.quantity[ingredientIndex],
                ]
            )
            ingredientMasterIndex = ingredientMasterIndex+1

    return MenuStruct(
        menuBase,
        menuIngredient,
    )
