import re

from MenuClass import MenuStruct


class IngredientContent:
    def __init__(self, quantity, scale):
        self.quantity = quantity
        self.scale = scale


class MenuScrapingService:
    def __init__(self, menuScrapingRepository):
        self.menuBase = []
        self.menuIngredient = []
        self.menuSeasoning = []
        self.ingredientIndex = 0
        self.seasoningIndex = 0
        self.menuScrapingRepository = menuScrapingRepository

    def convertMenu(self, menuIdList):
        def fractionCalculateQuantity(weight, SPOON_UNIT):
            if len(weight) == 3:
                return SPOON_UNIT * (int(weight[0]) + int(weight[1]) / int(weight[2]))
            elif len(weight) == 2:
                return SPOON_UNIT * (int(weight[0]) / int(weight[1]))
            else:
                return SPOON_UNIT * int(weight[0])

        def divideContentOnQuantityAndScale(content):
            ingredientQuantity = 0
            ingredientScale = ''

            weight = re.findall(r"\d+", content)

            if '大さじ' in content:
                TABLE_SPOON_UNIT = 15
                if 'g' in content:
                    noGramWeight = weight[0:len(weight) - 1]
                    ingredientQuantity = fractionCalculateQuantity(noGramWeight, TABLE_SPOON_UNIT)
                else:
                    ingredientQuantity = fractionCalculateQuantity(weight, TABLE_SPOON_UNIT)
                ingredientScale = 'ml'

            if '小さじ' in content:
                TEA_SPOON_UNIT = 5
                if 'g' in content:
                    noGramWeight = weight[0:len(weight) - 1]
                    ingredientQuantity = fractionCalculateQuantity(noGramWeight, TEA_SPOON_UNIT)
                else:
                    ingredientQuantity = fractionCalculateQuantity(weight, TEA_SPOON_UNIT)
                ingredientScale = 'ml'

            if '適量' in content:
                ingredientQuantity = 1
                ingredientScale = '適量'

            if '少々' in content:
                ingredientQuantity = 1
                ingredientScale = '少々'

            if 'g' in content:
                if len(weight)==1:
                    ingredientQuantity = int(weight[len(weight) - 1])
                    ingredientScale = 'g'

            if 'カップ' in content:
                CUP_UNIT = 200
                ingredientQuantity = fractionCalculateQuantity(weight, CUP_UNIT)
                ingredientScale = 'ml'

            else:
                for uniqueScale in ['箱', '本', '個', '枚', '玉', '缶', '袋', 'かけ分', '株', 'cm']:
                    if uniqueScale in content:
                        UNIQUE_SCALE_UNIT = 1
                        if 'g' in content:
                            noGramWeight = weight[0:len(weight)-1]
                            ingredientQuantity = fractionCalculateQuantity(noGramWeight, UNIQUE_SCALE_UNIT)
                        else:
                            ingredientQuantity = fractionCalculateQuantity(weight, UNIQUE_SCALE_UNIT)
                        ingredientScale = uniqueScale

            return IngredientContent(ingredientQuantity, ingredientScale)

        menuList = self.menuScrapingRepository.getMenu(menuIdList)
        for menuIndex, menu in enumerate(menuList):
            self.menuBase.append(
                [
                    menuIndex + 1,
                    menu.title,
                ]
            )
            for materialIndex, material in enumerate(menu.Material.item):
                materialContent = divideContentOnQuantityAndScale(
                    menu.Material.content[materialIndex]
                )

                seasoningPatternList = 'ml|適量|少々'
                isSeasoning = bool(
                    re
                    .compile(seasoningPatternList)
                    .search(materialContent.scale)
                )

                if isSeasoning:
                    self.menuSeasoning.append(
                        [
                            self.seasoningIndex + 1,
                            menuIndex + 1,
                            material,
                            materialContent.quantity,
                            materialContent.scale,
                        ]
                    )
                    self.seasoningIndex = self.seasoningIndex + 1
                else:
                    self.menuIngredient.append(
                        [
                            self.ingredientIndex + 1,
                            menuIndex + 1,
                            material,
                            materialContent.quantity,
                            materialContent.scale,
                        ]
                    )
                    self.ingredientIndex = self.ingredientIndex + 1

        return MenuStruct(
            self.menuBase,
            self.menuIngredient,
            self.menuSeasoning
        )

