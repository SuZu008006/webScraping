import os
import unittest

from MenuScrapingController import MenuScrapingController
from SpyStubMenuScrapingService import SpyStubMenuScrapingService


class TestMenuScrapingController(unittest.TestCase):
    def setUp(self):
        self.menuIdList = []
        self.spyStubMenuScrapingService = SpyStubMenuScrapingService([])

    def assertCsvContent(self, csvContent, rows, header, firstRow):
        self.assertEqual(rows, len(csvContent.splitlines()))
        self.assertEqual(header, csvContent.splitlines()[0].split(','))
        self.assertEqual(firstRow, csvContent.splitlines()[1].split(','))

    def test_menuBaseCsv(self):
        menuBaseList_returnValue = [
            [1, 'menuTitleOne'],
            [2, 'menuTitleTwo'],
        ]
        self.spyStubMenuScrapingService.menuBaseList_returnValue = menuBaseList_returnValue

        menuScrapingController = MenuScrapingController(
            self.spyStubMenuScrapingService,
            self.menuIdList
        )


        menuScrapingController.saveMenu()


        with open(f'{os.getcwd()}/csvContainer/menuBase.csv', 'r') as csvMenuBase:
            actualMenuBase = csvMenuBase.read()
            self.assertCsvContent(
                actualMenuBase,
                3,
                ['id', 'title'],
                ['1', 'menuTitleOne']
            )

    def test_menuIngredientCsv(self):
        menuIngredientList_returnValue = [
            [1, 1, 'itemOneOne', 11, 'g'],
            [2, 1, 'itemOneTwo', 12, 'g'],
            [3, 2, 'itemTwoOne', 21, 'g'],
            [4, 2, 'itemTwoTwo', 22, 'g'],
            [5, 2, 'itemTwoThree', 23, 'g'],
        ]
        self.spyStubMenuScrapingService.menuIngredientList_returnValue = menuIngredientList_returnValue

        menuScrapingController = MenuScrapingController(
            self.spyStubMenuScrapingService,
            self.menuIdList
        )


        menuScrapingController.saveIngredient()


        with open(f'{os.getcwd()}/csvContainer/menuIngredient.csv', 'r') as csvMenuIngredient:
            actualMenuIngredient = csvMenuIngredient.read()
            self.assertCsvContent(
                actualMenuIngredient,
                6,
                ['ingredient_id', 'id', 'item', 'quantity', 'scale'],
                ['1', '1', 'itemOneOne', '11', 'g']
            )

    def test_menuSeasoningCsv(self):
        menuSeasoningList_returnValue = [
            [1, 1, 'itemOneOne', 11, 'ml'],
            [2, 1, 'itemOneTwo', 12, 'ml'],
            [3, 2, 'itemTwoOne', 21, 'ml'],
            [4, 2, 'itemTwoTwo', 22, 'ml'],
            [5, 2, 'itemTwoThree', 23, 'ml'],
        ]
        self.spyStubMenuScrapingService.menuSeasoningList_returnValue = menuSeasoningList_returnValue

        menuScrapingController = MenuScrapingController(
            self.spyStubMenuScrapingService,
            self.menuIdList
        )


        menuScrapingController.saveSeasoning()


        with open(f'{os.getcwd()}/csvContainer/menuSeasoning.csv', 'r') as csvMenuSeasoning:
            actualMenuSeasoning = csvMenuSeasoning.read()
            self.assertCsvContent(
                actualMenuSeasoning,
                6,
                ['seasoning_id', 'id', 'item', 'quantity', 'scale'],
                ['1', '1', 'itemOneOne', '11', 'ml']
            )


if __name__ == '__main__':
    unittest.main()
