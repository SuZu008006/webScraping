import pytest
from playwright.sync_api import Page

from MenuScrapingRepository import MenuScrapingRepository
from MenuScrapingController import MenuScrapingController
from MenuScrapingService import MenuScrapingService

@pytest.mark.skipif(True, reason="不用意なスクレイピングの防止のため")
def test_menuScraping(page: Page):
    menuIdList = [
        705651,
        708962,
        705645,
        707841,
        708846,
        # 702969,
        # 705346,
        # 700595,
        # 706594,
        # 800030,
    ]

    menuScrapingRepository = MenuScrapingRepository(page)

    menuScrapingService = MenuScrapingService(menuScrapingRepository)

    menuScrapingController = MenuScrapingController(menuScrapingService, menuIdList)
    menuScrapingController.saveMenu()
    menuScrapingController.saveIngredient()
    menuScrapingController.saveSeasoning()

@pytest.mark.skipif(True, reason="不用意なスクレイピングの防止のため")
def test_menuScrapingRepository(page: Page):
    menuScrapingRepository = MenuScrapingRepository(page)
    menuIdList = [705651, 708962]

    expectedMenuTitle = ['鶏のから揚げ', '鶏胸肉のうま酢煮']
    expectedMenuIngredientItem = ['鶏もも肉・または鶏ももから揚げ用肉', '鶏むね肉']
    expectedMenuIngredientQuantity = ['1枚（250g）', '300g']

    menuList = menuScrapingRepository.getMenu(menuIdList)

    for index, menuId in enumerate(menuIdList):
        assert menuList[index].title == expectedMenuTitle[index]
        assert menuList[index].Material.item[0] == expectedMenuIngredientItem[index]
        assert menuList[index].Material.content[0] == expectedMenuIngredientQuantity[index]
