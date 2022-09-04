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
        702969,
        705346,
        700595,
        706594,
        800030,
    ]

    menuScrapingRepository = MenuScrapingRepository(page)

    menuScrapingService = MenuScrapingService(menuScrapingRepository)

    menuScrapingController = MenuScrapingController(menuScrapingService, menuIdList)
    menuScrapingController.saveMenuStruct()

@pytest.mark.skipif(True, reason="不用意なスクレイピングの防止のため")
def test_menuScrapingRepository(page: Page):
    menuScrapingRepository = MenuScrapingRepository(page)
    menuIdList = [705651, 708962]

    expectedMenuTitle = ['鶏のから揚げ', '鶏胸肉のうま酢煮']
    expectedMenuImageUrl = [
        'https://park.ajinomoto.co.jp/wp-content/uploads/2018/03/705651.jpeg',
        'https://park.ajinomoto.co.jp/wp-content/uploads/2018/03/708962.jpeg'
    ]
    expectedMenuIngredientItem = ['鶏もも肉・または鶏ももから揚げ用肉', '鶏むね肉']
    expectedMenuIngredientQuantity = ['1枚（250g）', '300g']
    expectedMenuMake = [
        '1\n鶏肉はひと口大に切る。\nボウルに鶏肉、「丸鶏がらスープ」、Ａを入れ、汁気がなくなるまでもみ込む。',
        '1\n鶏肉は余分な脂を取り、ひと口大に切る。酒をもみ込み、しばらくおいて薄力粉をまぶす。'
    ]

    menuList = menuScrapingRepository.getMenu(menuIdList)

    for index, menuId in enumerate(menuIdList):
        assert menuList[index].title == expectedMenuTitle[index]
        assert menuList[index].image == expectedMenuImageUrl[index]
        assert menuList[index].material.item[0] == expectedMenuIngredientItem[index]
        assert menuList[index].material.content[0] == expectedMenuIngredientQuantity[index]
        assert menuList[index].make.content[0] == expectedMenuMake[index]
