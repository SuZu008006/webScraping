from playwright.sync_api import Page


class MenuScrapingController(Page):
    def __init__(self, menuId):
        self.menuTitle = ""
        self.menuId = menuId
        self.page = super()

    def getMenuTitle(self):
        self.page.goto(f"https://park.ajinomoto.co.jp/recipe/card/{self.menuId}/")

        recipeCardXpath = (
            "xpath="
            "html/body/"
            "div[@class='chFixed']/"
            "div[@class='searchView']/"
            "div[@id='content']/"
            "article[@id='recipeCard']/"
        )

        menuTitleLocator = self.page.locator(
            recipeCardXpath +
            "div[@class='recipeArea']/"
            "div[@class='recipeTitleAreaType02']/"
            "div[@class='wrap1160']/"
            "div[@class='in_table']/"
            "h1[@class='recipeTitle']/"
            "span"
        )
        menuTitle = menuTitleLocator.all_inner_texts()

        self.menuTitle = menuTitle
