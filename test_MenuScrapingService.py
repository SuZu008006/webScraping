import unittest

from MenuClass import Menu, Ingredient
from MenuScrapingService import MenuScrapingService
from SpyStubMenuScrapingRepository import SpyStubMenuScrapingRepository


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.menuIdList = []
        self.spyStubMenuScrapingRepository = SpyStubMenuScrapingRepository()

    def test_menuScrapingService_spoonScale(self):
        menuList = [
            Menu(
                'menuTitleOne',
                Ingredient(
                    ['itemOneOne', 'itemOneTwo', 'itemOneThree', 'itemOneFour'],
                    ['大さじ1', '小さじ2', '小さじ2（10g）', '大さじ1（15g）']
                )
            ),
            Menu(
                'menuTitleTwo',
                Ingredient(
                    ['itemTwoOne', 'itemTwoTwo', 'itemTwoThree', 'itemTwoFour'],
                    ['大さじ1・1/2', '小さじ2・1/4', '大さじ1/2', '小さじ1/4']
                )
            )
        ]
        self.spyStubMenuScrapingRepository.menuList_returnValue = menuList

        menuScrapingService = MenuScrapingService(self.spyStubMenuScrapingRepository)

        actualMenuOutput = menuScrapingService.convertMenu(self.menuIdList)

        TABLE_SPOON_UNIT = 15
        TEA_SPOON_UNIT = 5

        expectedMenuBase = [
            [1, 'menuTitleOne'],
            [2, 'menuTitleTwo'],
        ]

        expectedMenuIngredient = [
            [1, 1, 'itemOneOne', TABLE_SPOON_UNIT * 1, 'ml'],
            [2, 1, 'itemOneTwo', TEA_SPOON_UNIT * 2, 'ml'],
            [3, 1, 'itemOneThree', TEA_SPOON_UNIT * 2, 'ml'],
            [4, 1, 'itemOneFour', TABLE_SPOON_UNIT * 1, 'ml'],
            [5, 2, 'itemTwoOne', TABLE_SPOON_UNIT * 1.5, 'ml'],
            [6, 2, 'itemTwoTwo', TEA_SPOON_UNIT * 2.25, 'ml'],
            [7, 2, 'itemTwoThree', TABLE_SPOON_UNIT * 0.5, 'ml'],
            [8, 2, 'itemTwoFour', TEA_SPOON_UNIT * 0.25, 'ml'],
        ]

        self.assertEqual(expectedMenuBase, actualMenuOutput.menuBase)
        self.assertEqual(expectedMenuIngredient, actualMenuOutput.menuIngredient)

    def test_menuScrapingService_amountOfYourChoice(self):
        menuList = [
            Menu(
                'menuTitleOne',
                Ingredient(
                    ['itemOneOne', 'itemOneTwo'],
                    ['適量', '少々']
                )
            ),
        ]
        self.spyStubMenuScrapingRepository.menuList_returnValue = menuList

        menuScrapingService = MenuScrapingService(self.spyStubMenuScrapingRepository)

        actualMenuOutput = menuScrapingService.convertMenu(self.menuIdList)

        expectedMenuBase = [
            [1, 'menuTitleOne'],
        ]

        expectedMenuIngredient = [
            [1, 1, 'itemOneOne', 1, '適量'],
            [2, 1, 'itemOneTwo', 1, '少々'],
        ]

        self.assertEqual(expectedMenuBase, actualMenuOutput.menuBase)
        self.assertEqual(expectedMenuIngredient, actualMenuOutput.menuIngredient)

    def test_menuScrapingService_gramDesignationOnly(self):
        menuList = [
            Menu(
                'menuTitleOne',
                Ingredient(
                    ['itemOneOne', 'itemOneTwo'],
                    ['100g', '200g']
                )
            ),
        ]
        self.spyStubMenuScrapingRepository.menuList_returnValue = menuList

        menuScrapingService = MenuScrapingService(self.spyStubMenuScrapingRepository)

        actualMenuOutput = menuScrapingService.convertMenu(self.menuIdList)

        expectedMenuBase = [
            [1, 'menuTitleOne'],
        ]

        expectedMenuIngredient = [
            [1, 1, 'itemOneOne', 100, 'g'],
            [2, 1, 'itemOneTwo', 200, 'g'],
        ]

        self.assertEqual(expectedMenuBase, actualMenuOutput.menuBase)
        self.assertEqual(expectedMenuIngredient, actualMenuOutput.menuIngredient)

    def test_menuScrapingService_cup(self):
        menuList = [
            Menu(
                'menuTitleOne',
                Ingredient(
                    ['itemOneOne', 'itemOneTwo', 'itemOneThree'],
                    ['1カップ', '1/4カップ', '1カップ・1/2']
                )
            ),
        ]
        self.spyStubMenuScrapingRepository.menuList_returnValue = menuList

        menuScrapingService = MenuScrapingService(self.spyStubMenuScrapingRepository)

        actualMenuOutput = menuScrapingService.convertMenu(self.menuIdList)

        expectedMenuBase = [
            [1, 'menuTitleOne'],
        ]

        expectedMenuIngredient = [
            [1, 1, 'itemOneOne', 200, 'ml'],
            [2, 1, 'itemOneTwo', 50, 'ml'],
            [3, 1, 'itemOneThree', 300, 'ml'],
        ]

        self.assertEqual(expectedMenuBase, actualMenuOutput.menuBase)
        self.assertEqual(expectedMenuIngredient, actualMenuOutput.menuIngredient)

    def test_menuScrapingService_uniqueScale(self):
        UNIQUE_SCALE_LIST = ['箱', '本', '個', '枚', '玉', '缶', '袋', 'かけ分', '株', 'cm']

        for uniqueScale in UNIQUE_SCALE_LIST:
            menuList = [
                Menu(
                    'menuTitleOne',
                    Ingredient(
                        ['itemOneOne', 'itemOneTwo', 'itemOneThree'],
                        ['1'+uniqueScale, '1/4'+uniqueScale, '1'+uniqueScale+'・1/2']
                    )
                ),
                Menu(
                    'menuTitleTwo',
                    Ingredient(
                        ['itemTwoOne', 'itemTwoTwo', 'itemTwoThree'],
                        ['1'+uniqueScale+'（100g）', '1/4'+uniqueScale+'（100g）', '1'+uniqueScale+'・1/2'+'（100g）']
                    )
                ),
            ]
            self.spyStubMenuScrapingRepository.menuList_returnValue = menuList

            menuScrapingService = MenuScrapingService(self.spyStubMenuScrapingRepository)

            actualMenuOutput = menuScrapingService.convertMenu(self.menuIdList)

            expectedMenuBase = [
                [1, 'menuTitleOne'],
                [2, 'menuTitleTwo'],
            ]

            expectedMenuIngredient = [
                [1, 1, 'itemOneOne', 1, uniqueScale],
                [2, 1, 'itemOneTwo', 0.25, uniqueScale],
                [3, 1, 'itemOneThree', 1.5, uniqueScale],
                [4, 2, 'itemTwoOne', 1, uniqueScale],
                [5, 2, 'itemTwoTwo', 0.25, uniqueScale],
                [6, 2, 'itemTwoThree', 1.5, uniqueScale],
            ]

            self.assertEqual(expectedMenuBase, actualMenuOutput.menuBase)
            self.assertEqual(expectedMenuIngredient, actualMenuOutput.menuIngredient)


if __name__ == '__main__':
    unittest.main()
