from playwright.sync_api import Page

from MenuScraping import getMenu


def test_menuScraping(page: Page):
    menuIdList = [705651, 708962]

    expectedMenuTitle = ['鶏のから揚げ', '鶏胸肉のうま酢煮']
    expectedMenuIngredientItem = ['鶏もも肉・または鶏ももから揚げ用肉', '鶏むね肉']
    expectedMenuIngredientQuantity = ['1枚（250g）', '300g']

    for index, menuId in enumerate(menuIdList):
        menu = getMenu(page, menuId)
        assert menu.title == expectedMenuTitle[index]
        assert menu.Ingredient.item[0] == expectedMenuIngredientItem[index]
        assert menu.Ingredient.quantity[0] == expectedMenuIngredientQuantity[index]
