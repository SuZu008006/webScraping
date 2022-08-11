from playwright.sync_api import Page

from MenuScraping import getMenu, Menu, Ingredient, convertMenu


def test_menuScrapingController(page: Page):
    menuIdList = [705651, 708962]

    expectedMenuTitle = ['鶏のから揚げ', '鶏胸肉のうま酢煮']
    expectedMenuIngredientItem = ['鶏もも肉・または鶏ももから揚げ用肉', '鶏むね肉']
    expectedMenuIngredientQuantity = ['1枚（250g）', '300g']

    menu = getMenu(page, menuIdList)

    for index, menuId in enumerate(menuIdList):
        assert menu[index].title == expectedMenuTitle[index]
        assert menu[index].Ingredient.item[0] == expectedMenuIngredientItem[index]
        assert menu[index].Ingredient.quantity[0] == expectedMenuIngredientQuantity[index]


def test_menuScrapingService():
    # TODO: DIした実装になるようにリファクタリングのこと
    stubMenuList = [
        Menu(
            'menuTitleOne',
            Ingredient(
                ['itemOneOne', 'itemOneTwo'],
                ['11', '12']
            )
        ),
        Menu(
            'menuTitleTwo',
            Ingredient(
                ['itemTwoOne', 'itemTwoTwo', 'itemTwoThree'],
                ['21', '22', '23']
            )
        )
    ]

    actualMenuOutput = convertMenu(stubMenuList)

    expectedMenuBase = [
        [1, 'menuTitleOne'],
        [2, 'menuTitleTwo'],
    ]

    expectedMenuIngredient = [
        [1, 'itemOneOne', '11'],
        [2, 'itemOneTwo', '12'],
        [3, 'itemTwoOne', '21'],
        [4, 'itemTwoTwo', '22'],
        [5, 'itemTwoThree', '23'],
    ]

    assert actualMenuOutput.menuBase == expectedMenuBase
    assert actualMenuOutput.menuIngredient == expectedMenuIngredient
