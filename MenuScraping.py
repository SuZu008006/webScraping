import re
from playwright.sync_api import Page


def test_homepage_has_Playwright_in_title_and_get_started_link_linking_to_the_intro_page(page: Page):
    menuIdList = [705651, 708962]

    for menuId in menuIdList:
        getMenu(page, menuId)


def getMenu(page, menuId):
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

    print("\n")
    print("------------------------------------------")
    print(menuTitle)
    print("------------------------------------------")

    menuIngredientItemLocator = page.locator(
        recipeCardXpath +
        "div[@class ='recipeCardSpOrderWrap']/"
        "div[@class ='wrap820 recipeCardSpOrder1']/"
        "div[@class ='recipeMaterialType02']/"
        "div[@class ='recipeMaterialList']/"
        "dl/dt"
    )
    menuIngredientItem = menuIngredientItemLocator.all_inner_texts()

    print("\n")
    print("------------------------------------------")
    print(menuIngredientItem)
    print("------------------------------------------")

    menuIngredientQuantityLocator = page.locator(
        recipeCardXpath +
        "div[@class ='recipeCardSpOrderWrap']/"
        "div[@class ='wrap820 recipeCardSpOrder1']/"
        "div[@class ='recipeMaterialType02']/"
        "div[@class ='recipeMaterialList']/"
        "dl/dd"
    )
    menuIngredientQuantity = menuIngredientQuantityLocator.all_inner_texts()

    print("\n")
    print("------------------------------------------")
    print(menuIngredientQuantity)
    print("------------------------------------------")
