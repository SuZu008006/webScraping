import csv
import os


class MenuScrapingController:
    def __init__(self, menuScrapingService):
        self.writePath = os.getcwd()
        self.menuScrapingService = menuScrapingService

    def saveMenu(self, menuIdList):
        menuStruct = self.menuScrapingService.convertMenu(menuIdList)
        menuBase = menuStruct.menuBase
        with open(f'{self.writePath}/csvContainer/menuBase.csv', 'w') as csvMenuBase:
            writer = csv.writer(csvMenuBase)
            writer.writerow(["id", "title"])
            writer.writerows(menuBase)

    def saveIngredient(self, menuIdList):
        menuStruct = self.menuScrapingService.convertMenu(menuIdList)
        menuIngredient = menuStruct.menuIngredient
        with open(f'{self.writePath}/csvContainer/menuIngredient.csv', 'w') as csvMenuIngredient:
            writer = csv.writer(csvMenuIngredient)
            writer.writerow(['ingredient_id', 'id', 'item', 'quantity'])
            writer.writerows(menuIngredient)
