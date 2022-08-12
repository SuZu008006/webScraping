import os

from playwright.sync_api import Page

from MenuScrapingRepository import Menu, Ingredient, MenuScrapingRepository
from MenuScrapingController import MenuScrapingController
from MenuScrapingService import MenuScrapingService
from SpyStubMenuScrapingService import SpyStubMenuScrapingService
from SpyStubMenuScrapingRepository import SpyStubMenuScrapingRepository


def test_menuScrapingRepository(page: Page):
    menuScrapingRepository = MenuScrapingRepository(page)
    menuIdList = [705651, 708962]

    expectedMenuTitle = ['鶏のから揚げ', '鶏胸肉のうま酢煮']
    expectedMenuIngredientItem = ['鶏もも肉・または鶏ももから揚げ用肉', '鶏むね肉']
    expectedMenuIngredientQuantity = ['1枚（250g）', '300g']


    menu = menuScrapingRepository.getMenu(menuIdList)


    for index, menuId in enumerate(menuIdList):
        assert menu[index].title == expectedMenuTitle[index]
        assert menu[index].Ingredient.item[0] == expectedMenuIngredientItem[index]
        assert menu[index].Ingredient.quantity[0] == expectedMenuIngredientQuantity[index]


def test_menuScrapingService():
    menuIdList = [111111, 222222]

    spyStubMenuScrapingRepository = SpyStubMenuScrapingRepository()

    menuList = [
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
    spyStubMenuScrapingRepository.menuList_returnValue = menuList

    menuScrapingService = MenuScrapingService(spyStubMenuScrapingRepository)


    actualMenuOutput = menuScrapingService.convertMenu(menuIdList)


    expectedMenuBase = [
        [1, 'menuTitleOne'],
        [2, 'menuTitleTwo'],
    ]

    expectedMenuIngredient = [
        [1, 1, 'itemOneOne', '11'],
        [2, 1, 'itemOneTwo', '12'],
        [3, 2, 'itemTwoOne', '21'],
        [4, 2, 'itemTwoTwo', '22'],
        [5, 2, 'itemTwoThree', '23'],
    ]

    assert actualMenuOutput.menuBase == expectedMenuBase
    assert actualMenuOutput.menuIngredient == expectedMenuIngredient


def test_menuScrapingController_menuBaseCsv():
    menuIdList = [111111, 222222]
    spyStubMenuScrapingService = SpyStubMenuScrapingService([])

    menuBaseList_returnValue = [
        [1, 'menuTitleOne'],
        [2, 'menuTitleTwo'],
    ]
    spyStubMenuScrapingService.menuBaseList_returnValue = menuBaseList_returnValue

    menuScrapingController = MenuScrapingController(spyStubMenuScrapingService)


    menuScrapingController.saveMenu(menuIdList)


    with open(f'{os.getcwd()}/csvContainer/menuBase.csv', 'r') as csvMenuBase:
        actualMenuBase = csvMenuBase.read()

        assert len(actualMenuBase.splitlines()) == 3
        assert actualMenuBase.splitlines()[0].split(',') == ['id', 'title']
        assert actualMenuBase.splitlines()[1].split(',') == ['1', 'menuTitleOne']


def test_menuScrapingController_menuIngredientCsv():
    menuIdList = [111111, 222222]
    spyStubMenuScrapingService = SpyStubMenuScrapingService(menuIdList)

    menuIngredientList_returnValue = [
        [1, 1, 'itemOneOne', '11'],
        [2, 1, 'itemOneTwo', '12'],
        [3, 2, 'itemTwoOne', '21'],
        [4, 2, 'itemTwoTwo', '22'],
        [5, 2, 'itemTwoThree', '23'],
    ]
    spyStubMenuScrapingService.menuIngredientList_returnValue = menuIngredientList_returnValue

    menuScrapingController = MenuScrapingController(spyStubMenuScrapingService)


    menuScrapingController.saveIngredient(menuIdList)


    with open(f'{os.getcwd()}/csvContainer/menuIngredient.csv', 'r') as csvMenuBase:
        actualMenuBase = csvMenuBase.read()

        assert len(actualMenuBase.splitlines()) == 6
        assert actualMenuBase.splitlines()[0].split(',') == ['ingredient_id', 'id', 'item', 'quantity']
        assert actualMenuBase.splitlines()[1].split(',') == ['1', '1', 'itemOneOne', '11']
