import unittest

from MenuClass import MenuTmp
from MenuScrapingService import MenuScrapingService
from SpyStubMenuScrapingRepository import SpyStubMenuScrapingRepository


class TestMenuScrapingService(unittest.TestCase):
    def setUp(self):
        self.menuIdList = []
        self.spyStubMenuScrapingRepository = SpyStubMenuScrapingRepository()

    def test_seasoning_spoonScale(self):
        menuList = [
            MenuTmp(
                '',
                '',
                MenuTmp.Material(
                    ['itemOneOne', 'itemOneTwo', 'itemOneThree', 'itemOneFour'],
                    ['大さじ1', '小さじ2', '小さじ2（10g）', '大さじ1（15g）']
                ),
                MenuTmp.Make(
                    ['', '']
                )
            ),
            MenuTmp(
                '',
                '',
                MenuTmp.Material(
                    ['itemTwoOne', 'itemTwoTwo', 'itemTwoThree', 'itemTwoFour'],
                    ['大さじ1・1/2', '小さじ2・1/4', '大さじ1/2', '小さじ1/4']
                ),
                MenuTmp.Make(
                    ['', '']
                )
            )
        ]
        self.spyStubMenuScrapingRepository.menuList_returnValue = menuList

        menuScrapingService = MenuScrapingService(self.spyStubMenuScrapingRepository)

        actualMenuOutput = menuScrapingService.convertMenu(self.menuIdList)

        TABLE_SPOON_UNIT = 15
        TEA_SPOON_UNIT = 5

        expectedMenuStruct = [
            {
                'menuRecord': {
                    'title': '',
                    'image': '',
                },
                'ingredientRecord': [],
                'seasoningRecord': [
                    {
                        'item': 'itemOneOne',
                        'quantity': TABLE_SPOON_UNIT * 1,
                        'scale': 'ml'
                    },
                    {
                        'item': 'itemOneTwo',
                        'quantity': TEA_SPOON_UNIT * 2,
                        'scale': 'ml'
                    },
                    {
                        'item': 'itemOneThree',
                        'quantity': TEA_SPOON_UNIT * 2,
                        'scale': 'ml'
                    },
                    {
                        'item': 'itemOneFour',
                        'quantity': TABLE_SPOON_UNIT * 1,
                        'scale': 'ml'
                    }
                ],
                'makeRecord': [
                    {'content': '', },
                    {'content': '', },
                ],
            },
            {
                'menuRecord': {
                    'title': '',
                    'image': '',
                },
                'ingredientRecord': [],
                'seasoningRecord': [
                    {
                        'item': 'itemTwoOne',
                        'quantity': TABLE_SPOON_UNIT * 1.5,
                        'scale': 'ml'
                    },
                    {
                        'item': 'itemTwoTwo',
                        'quantity': TEA_SPOON_UNIT * 2.25,
                        'scale': 'ml'
                    },
                    {
                        'item': 'itemTwoThree',
                        'quantity': TABLE_SPOON_UNIT * 0.5,
                        'scale': 'ml'
                    },
                    {
                        'item': 'itemTwoFour',
                        'quantity': TEA_SPOON_UNIT * 0.25,
                        'scale': 'ml'
                    }
                ],
                'makeRecord': [
                    {'content': '', },
                    {'content': '', },
                ],
            }
        ]

        self.assertEqual(expectedMenuStruct, actualMenuOutput)

    def test_seasoning_cup(self):
        menuList = [
            MenuTmp(
                'menuTitleOne',
                'menuOneImage',
                MenuTmp.Material(
                    ['itemOneOne', 'itemOneTwo', 'itemOneThree'],
                    ['1カップ', '1/4カップ', '1カップ・1/2']
                ),
                MenuTmp.Make(
                    ['', '']
                ),
            ),
        ]
        self.spyStubMenuScrapingRepository.menuList_returnValue = menuList

        menuScrapingService = MenuScrapingService(self.spyStubMenuScrapingRepository)

        actualMenuOutput = menuScrapingService.convertMenu(self.menuIdList)

        CUP = 200

        expectedMenuStruct = [
            {
                'menuRecord': {
                    'title': 'menuTitleOne',
                    'image': 'menuOneImage',
                },
                'ingredientRecord': [],
                'seasoningRecord': [
                    {
                        'item': 'itemOneOne',
                        'quantity': CUP * 1,
                        'scale': 'ml'
                    },
                    {
                        'item': 'itemOneTwo',
                        'quantity': CUP * 0.25,
                        'scale': 'ml'
                    },
                    {
                        'item': 'itemOneThree',
                        'quantity': CUP * 1.5,
                        'scale': 'ml'
                    },
                ],
                'makeRecord': [
                    {'content': '', },
                    {'content': '', },
                ],
            },
        ]

        self.assertEqual(expectedMenuStruct, actualMenuOutput)

    def test_seasoning_amountOfYourChoice(self):
        menuList = [
            MenuTmp(
                'menuTitleOne',
                'menuOneImage',
                MenuTmp.Material(
                    ['itemOneOne', 'itemOneTwo'],
                    ['適量', '少々']
                ),
                MenuTmp.Make(
                    ['', '']
                ),
            ),
        ]
        self.spyStubMenuScrapingRepository.menuList_returnValue = menuList

        menuScrapingService = MenuScrapingService(self.spyStubMenuScrapingRepository)

        actualMenuOutput = menuScrapingService.convertMenu(self.menuIdList)

        expectedMenuStruct = [
            {
                'menuRecord': {
                    'title': 'menuTitleOne',
                    'image': 'menuOneImage',
                },
                'ingredientRecord': [],
                'seasoningRecord': [
                    {
                        'item': 'itemOneOne',
                        'quantity': 1,
                        'scale': '適量'
                    },
                    {
                        'item': 'itemOneTwo',
                        'quantity': 1,
                        'scale': '少々'
                    },
                ],
                'makeRecord': [
                    {'content': '', },
                    {'content': '', },
                ],
            },
        ]

        self.assertEqual(expectedMenuStruct, actualMenuOutput)

    def test_ingredient_gramDesignationOnly(self):
        menuList = [
            MenuTmp(
                'menuTitleOne',
                'menuOneImage',
                MenuTmp.Material(
                    ['itemOneOne', 'itemOneTwo'],
                    ['100g', '200g']
                ),
                MenuTmp.Make(
                    ['', '']
                ),
            ),
        ]
        self.spyStubMenuScrapingRepository.menuList_returnValue = menuList

        menuScrapingService = MenuScrapingService(self.spyStubMenuScrapingRepository)

        actualMenuOutput = menuScrapingService.convertMenu(self.menuIdList)

        expectedMenuStruct = [
            {
                'menuRecord': {
                    'title': 'menuTitleOne',
                    'image': 'menuOneImage',
                },
                'ingredientRecord': [
                    {
                        'item': 'itemOneOne',
                        'quantity': 100,
                        'scale': 'g'
                    },
                    {
                        'item': 'itemOneTwo',
                        'quantity': 200,
                        'scale': 'g'
                    },
                ],
                'seasoningRecord': [],
                'makeRecord': [
                    {'content': '', },
                    {'content': '', },
                ],
            },
        ]

        self.assertEqual(expectedMenuStruct, actualMenuOutput)

    def test_ingredient_uniqueScale(self):
        UNIQUE_SCALE_LIST = ['箱', '本', '個', '枚', '玉', '缶', '袋', 'かけ分', '株', 'cm']

        for uniqueScale in UNIQUE_SCALE_LIST:
            menuList = [
                MenuTmp(
                    'menuTitleOne',
                    'menuOneImage',
                    MenuTmp.Material(
                        ['itemOneOne', 'itemOneTwo', 'itemOneThree'],
                        ['1' + uniqueScale, '1/4' + uniqueScale, '1' + uniqueScale + '・1/2']
                    ),
                    MenuTmp.Make(
                        ['', '']
                    ),
                ),
                MenuTmp(
                    'menuTitleTwo',
                    'menuTwoImage',
                    MenuTmp.Material(
                        ['itemTwoOne', 'itemTwoTwo', 'itemTwoThree'],
                        ['1' + uniqueScale + '（100g）', '1/4' + uniqueScale + '（100g）',
                         '1' + uniqueScale + '・1/2' + '（100g）']
                    ),
                    MenuTmp.Make(
                        ['', '']
                    ),
                ),
            ]
            self.spyStubMenuScrapingRepository.menuList_returnValue = menuList

            menuScrapingService = MenuScrapingService(self.spyStubMenuScrapingRepository)

            actualMenuOutput = menuScrapingService.convertMenu(self.menuIdList)

            expectedMenuStruct = [
                {
                    'menuRecord': {
                        'title': 'menuTitleOne',
                        'image': 'menuOneImage',
                    },
                    'ingredientRecord': [
                        {
                            'item': 'itemOneOne',
                            'quantity': 1,
                            'scale': uniqueScale
                        },
                        {
                            'item': 'itemOneTwo',
                            'quantity': 0.25,
                            'scale': uniqueScale
                        },
                        {
                            'item': 'itemOneThree',
                            'quantity': 1.5,
                            'scale': uniqueScale
                        },
                    ],
                    'seasoningRecord': [],
                    'makeRecord': [
                        {'content': '', },
                        {'content': '', },
                    ],
                },
                {
                    'menuRecord': {
                        'title': 'menuTitleTwo',
                        'image': 'menuTwoImage',
                    },
                    'ingredientRecord': [
                        {
                            'item': 'itemTwoOne',
                            'quantity': 1,
                            'scale': uniqueScale
                        },
                        {
                            'item': 'itemTwoTwo',
                            'quantity': 0.25,
                            'scale': uniqueScale
                        },
                        {
                            'item': 'itemTwoThree',
                            'quantity': 1.5,
                            'scale': uniqueScale
                        },
                    ],
                    'seasoningRecord': [],
                    'makeRecord': [
                        {'content': '', },
                        {'content': '', },
                    ],
                },
            ]

            self.assertEqual(expectedMenuStruct, actualMenuOutput)

    def test_ingredientAndSeasoning_complex(self):
        menuList = [
            MenuTmp(
                'menuTitleOne',
                'menuOneImage',
                MenuTmp.Material(
                    ['itemOneOne', 'itemOneTwo', 'itemOneThree', 'itemOneFour'],
                    ['大さじ1', '小さじ2', '300g', '4箱']
                ),
                MenuTmp.Make(
                    ['', '']
                ),
            ),
            MenuTmp(
                'menuTitleTwo',
                'menuTwoImage',
                MenuTmp.Material(
                    ['itemTwoOne', 'itemTwoTwo', 'itemTwoThree', 'itemTwoFour'],
                    ['4株', '3かけ分', '2カップ', '適量']
                ),
                MenuTmp.Make(
                    ['', '']
                ),
            )
        ]
        self.spyStubMenuScrapingRepository.menuList_returnValue = menuList

        menuScrapingService = MenuScrapingService(self.spyStubMenuScrapingRepository)

        actualMenuOutput = menuScrapingService.convertMenu(self.menuIdList)

        TABLE_SPOON_UNIT = 15
        TEA_SPOON_UNIT = 5
        CUP = 200

        expectedMenuStruct = [
            {
                'menuRecord': {
                    'title': 'menuTitleOne',
                    'image': 'menuOneImage',
                },
                'ingredientRecord': [
                    {
                        'item': 'itemOneThree',
                        'quantity': 300,
                        'scale': 'g'
                    },
                    {
                        'item': 'itemOneFour',
                        'quantity': 4,
                        'scale': '箱'
                    },
                ],
                'seasoningRecord': [
                    {
                        'item': 'itemOneOne',
                        'quantity': TABLE_SPOON_UNIT * 1,
                        'scale': 'ml'
                    },
                    {
                        'item': 'itemOneTwo',
                        'quantity': TEA_SPOON_UNIT * 2,
                        'scale': 'ml'
                    },
                ],
                'makeRecord': [
                    {'content': '', },
                    {'content': '', },
                ],
            },
            {
                'menuRecord': {
                    'title': 'menuTitleTwo',
                    'image': 'menuTwoImage',
                },
                'ingredientRecord': [
                    {
                        'item': 'itemTwoOne',
                        'quantity': 4,
                        'scale': '株'
                    },
                    {
                        'item': 'itemTwoTwo',
                        'quantity': 3,
                        'scale': 'かけ分'
                    },
                ],
                'seasoningRecord': [
                    {
                        'item': 'itemTwoThree',
                        'quantity': CUP * 2,
                        'scale': 'ml'
                    },
                    {
                        'item': 'itemTwoFour',
                        'quantity': 1,
                        'scale': '適量'
                    },
                ],
                'makeRecord': [
                    {'content': '', },
                    {'content': '', },
                ],
            },
        ]

        self.assertEqual(expectedMenuStruct, actualMenuOutput)

    def test_make_nonInitialNumber(self):
        menuList = [
            MenuTmp(
                '',
                '',
                MenuTmp.Material([], []),
                MenuTmp.Make(
                    ['1\nmakeOneOne', '2\nmakeOneTwo'],
                ),
            ),
            MenuTmp(
                '',
                '',
                MenuTmp.Material([], []),
                MenuTmp.Make(
                    ['1\nmakeTwoOne', '2\nmakeTwoTwo'],
                ),
            )
        ]
        self.spyStubMenuScrapingRepository.menuList_returnValue = menuList

        menuScrapingService = MenuScrapingService(self.spyStubMenuScrapingRepository)

        actualMenuOutput = menuScrapingService.convertMenu(self.menuIdList)

        expectedMenuStruct = [
            {
                'menuRecord': {
                    'title': '',
                    'image': '',
                },
                'ingredientRecord': [],
                'seasoningRecord': [],
                'makeRecord': [
                    {'content': 'makeOneOne', },
                    {'content': 'makeOneTwo', },
                ],
            },
            {
                'menuRecord': {
                    'title': '',
                    'image': '',
                },
                'ingredientRecord': [],
                'seasoningRecord': [],
                'makeRecord': [
                    {'content': 'makeTwoOne', },
                    {'content': 'makeTwoTwo', },
                ],
            },
        ]

        self.assertEqual(expectedMenuStruct, actualMenuOutput)


if __name__ == '__main__':
    unittest.main()
