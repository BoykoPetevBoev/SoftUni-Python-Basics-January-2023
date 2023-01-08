chickenMenus = int(input())
fishMenu = int(input())
veganMenu = int(input())

chickenMenusPrice = chickenMenus * 10.35
fishMenuPrice = fishMenu * 12.4
veganMenuPrice = veganMenu * 8.15

totalMenusPrice = chickenMenusPrice + fishMenuPrice + veganMenuPrice
desertPrice = totalMenusPrice * 0.2

total = totalMenusPrice + desertPrice + 2.5

print(total)
