import json
import os


class MenuScrapingController:
    def __init__(self, menuScrapingService, menuIdList):
        self.writePath = os.getcwd()
        self.menuStruct = menuScrapingService.convertMenu(menuIdList)

    def saveMenuStruct(self):
        print(self.menuStruct)
        with open(f'{os.getcwd()}/jsonContainer/menuStruct.json', 'w') as jsonMenuStruct:
            json.dump(self.menuStruct, jsonMenuStruct, ensure_ascii=False, indent=4)

