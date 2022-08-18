import re

from MenuClass import MenuStruct


class MaterialContent:
    def __init__(self, quantity, scale):
        self.quantity = quantity
        self.scale = scale


class MenuScrapingService:
    def __init__(self, menuScrapingRepository):
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
            quantity = 0
            scale = ''

            weight = re.findall(r"\d+", content)

            if '大さじ' in content:
                TABLE_SPOON_UNIT = 15
                if 'g' in content:
                    noGramWeight = weight[0:len(weight) - 1]
                    quantity = fractionCalculateQuantity(noGramWeight, TABLE_SPOON_UNIT)
                else:
                    quantity = fractionCalculateQuantity(weight, TABLE_SPOON_UNIT)
                scale = 'ml'

            if '小さじ' in content:
                TEA_SPOON_UNIT = 5
                if 'g' in content:
                    noGramWeight = weight[0:len(weight) - 1]
                    quantity = fractionCalculateQuantity(noGramWeight, TEA_SPOON_UNIT)
                else:
                    quantity = fractionCalculateQuantity(weight, TEA_SPOON_UNIT)
                scale = 'ml'

            if '適量' in content:
                quantity = 1
                scale = '適量'

            if '少々' in content:
                quantity = 1
                scale = '少々'

            if 'g' in content:
                if len(weight)==1:
                    quantity = int(weight[len(weight) - 1])
                    scale = 'g'

            if 'カップ' in content:
                CUP_UNIT = 200
                quantity = fractionCalculateQuantity(weight, CUP_UNIT)
                scale = 'ml'

            else:
                for uniqueScale in ['箱', '本', '個', '枚', '玉', '缶', '袋', 'かけ分', '株', 'cm']:
                    if uniqueScale in content:
                        UNIQUE_SCALE_UNIT = 1
                        if 'g' in content:
                            noGramWeight = weight[0:len(weight)-1]
                            quantity = fractionCalculateQuantity(noGramWeight, UNIQUE_SCALE_UNIT)
                        else:
                            quantity = fractionCalculateQuantity(weight, UNIQUE_SCALE_UNIT)
                        scale = uniqueScale

            return MaterialContent(quantity, scale)

        menuStruct = []

        menuList = self.menuScrapingRepository.getMenu(menuIdList)
        for menuIndex, menu in enumerate(menuList):
            ingredient = []
            seasoning = []

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
                    seasoning.append(
                        MenuStruct.Ingredient(
                            material,
                            materialContent.quantity,
                            materialContent.scale,
                        ).__dict__
                    )
                else:
                    ingredient.append(
                        MenuStruct.Ingredient(
                            material,
                            materialContent.quantity,
                            materialContent.scale,
                        ).__dict__
                    )

            menuStruct.append(
                MenuStruct(
                    MenuStruct.Menu(menu.title).__dict__,
                    ingredient,
                    seasoning,
                ).__dict__
            )

        return menuStruct
