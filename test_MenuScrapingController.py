import os
import unittest

from MenuScrapingController import MenuScrapingController
from SpyStubMenuScrapingService import SpyStubMenuScrapingService


class TestMenuScrapingController(unittest.TestCase):
    def setUp(self):
        self.menuIdList = []
        self.spyStubMenuScrapingService = SpyStubMenuScrapingService([])

    def test_menuStructJson(self):
        menu_returnValue = ['menuTitleOne','menuImageOne']
        ingredient_returnValue = 11

        self.spyStubMenuScrapingService.menu_returnValue = menu_returnValue
        self.spyStubMenuScrapingService.ingredient_returnValue = ingredient_returnValue

        menuScrapingController = MenuScrapingController(
            self.spyStubMenuScrapingService,
            self.menuIdList
        )

        menuScrapingController.saveMenuStruct()

        with open(f'{os.getcwd()}/jsonContainer/menuStruct.json', 'r') as jsonMenuStruct:
            jsonMenuStruct.read()
            pass


if __name__ == '__main__':
    unittest.main()
