import unittest
from MenuScrapingController import MenuScrapingController


class MyTestCase(unittest.TestCase):
    @unittest.skip("classにしてplaywrightを使おうとしたができないので断念")
    def test_something(self):
        menuId = 708962
        menuScrapingController = MenuScrapingController(menuId)
        menuScrapingController.getMenuTitle()
        self.assertEqual('鶏胸肉のうま酢煮', menuScrapingController.menuTitle)


if __name__ == '__main__':
    unittest.main()
