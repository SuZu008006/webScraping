class SpyStubMenuScrapingRepository:
    def __init__(self):
        self.menuList_returnValue = []

    def getMenu(self, _):
        return self.menuList_returnValue
