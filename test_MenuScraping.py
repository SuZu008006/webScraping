import os

from playwright.sync_api import Page

from MenuScrapingRepository import Menu, Ingredient, MenuScrapingRepository
from MenuScrapingController import MenuScrapingController
from MenuScrapingService import MenuScrapingService
from SpyStubMenuScrapingService import SpyStubMenuScrapingService
from SpyStubMenuScrapingRepository import SpyStubMenuScrapingRepository


def test_menuScraping(page: Page):
    menuIdList = [
        705651,
        708962,
        705645,
        707841,
        708846,
        702969,
        705346,
        700595,
        706594,
        800030,
    ]

    menuScrapingRepository = MenuScrapingRepository(page)

    menuScrapingService = MenuScrapingService(menuScrapingRepository)

    menuScrapingController = MenuScrapingController(menuScrapingService, menuIdList)
    menuScrapingController.saveMenu()
    menuScrapingController.saveIngredient()


def test_menuScrapingRepository(page: Page):
    menuScrapingRepository = MenuScrapingRepository(page)
    menuIdList = [705651, 708962]

    expectedMenuTitle = ['鶏のから揚げ', '鶏胸肉のうま酢煮']
    expectedMenuIngredientItem = ['鶏もも肉・または鶏ももから揚げ用肉', '鶏むね肉']
    expectedMenuIngredientQuantity = ['1枚（250g）', '300g']

    menuList = menuScrapingRepository.getMenu(menuIdList)

    for index, menuId in enumerate(menuIdList):
        assert menuList[index].title == expectedMenuTitle[index]
        assert menuList[index].Ingredient.item[0] == expectedMenuIngredientItem[index]
        assert menuList[index].Ingredient.content[0] == expectedMenuIngredientQuantity[index]


def test_menuScrapingController_menuBaseCsv():
    menuIdList = []
    spyStubMenuScrapingService = SpyStubMenuScrapingService([])

    menuBaseList_returnValue = [
        [1, 'menuTitleOne'],
        [2, 'menuTitleTwo'],
    ]
    spyStubMenuScrapingService.menuBaseList_returnValue = menuBaseList_returnValue

    menuScrapingController = MenuScrapingController(spyStubMenuScrapingService, menuIdList)

    menuScrapingController.saveMenu()

    with open(f'{os.getcwd()}/csvContainer/menuBase.csv', 'r') as csvMenuBase:
        actualMenuBase = csvMenuBase.read()

        assert len(actualMenuBase.splitlines()) == 3
        assert actualMenuBase.splitlines()[0].split(',') == ['id', 'title']
        assert actualMenuBase.splitlines()[1].split(',') == ['1', 'menuTitleOne']


def test_menuScrapingController_menuIngredientCsv():
    menuIdList = []
    spyStubMenuScrapingService = SpyStubMenuScrapingService(menuIdList)

    menuIngredientList_returnValue = [
        [1, 1, 'itemOneOne', 11, 'g'],
        [2, 1, 'itemOneTwo', 12, 'g'],
        [3, 2, 'itemTwoOne', 21, 'g'],
        [4, 2, 'itemTwoTwo', 22, 'g'],
        [5, 2, 'itemTwoThree', 23, 'g'],
    ]
    spyStubMenuScrapingService.menuIngredientList_returnValue = menuIngredientList_returnValue

    menuScrapingController = MenuScrapingController(spyStubMenuScrapingService, menuIdList)

    menuScrapingController.saveIngredient()

    with open(f'{os.getcwd()}/csvContainer/menuIngredient.csv', 'r') as csvMenuBase:
        actualMenuBase = csvMenuBase.read()

        assert len(actualMenuBase.splitlines()) == 6
        assert actualMenuBase.splitlines()[0].split(',') == ['ingredient_id', 'id', 'item', 'quantity', 'scale']
        assert actualMenuBase.splitlines()[1].split(',') == ['1', '1', 'itemOneOne', '11', 'g']
