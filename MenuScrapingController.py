import csv
import os


class MenuScrapingController:
    def __init__(self, menuScrapingService, menuIdList):
        self.writePath = os.getcwd()
        self.menuStruct = menuScrapingService.convertMenu(menuIdList)

    def saveMenu(self):
        menuBase = self.menuStruct.menuBase
        with open(f'{self.writePath}/csvContainer/menuBase.csv', 'w') as csvMenuBase:
            writer = csv.writer(csvMenuBase)
            writer.writerow(["id", "title"])
            writer.writerows(menuBase)

    def saveIngredient(self):
        menuIngredient = self.menuStruct.menuIngredient
        with open(f'{self.writePath}/csvContainer/menuIngredient.csv', 'w') as csvMenuIngredient:
            writer = csv.writer(csvMenuIngredient)
            writer.writerow(['ingredient_id', 'id', 'item', 'quantity', 'scale'])
            writer.writerows(menuIngredient)

    def saveSeasoning(self):
        menuSeasoning = self.menuStruct.menuSeasoning
        with open(f'{self.writePath}/csvContainer/menuSeasoning.csv', 'w') as csvMenuSeasoning:
            writer = csv.writer(csvMenuSeasoning)
            writer.writerow(['seasoning_id', 'id', 'item', 'quantity', 'scale'])
            writer.writerows(menuSeasoning)

