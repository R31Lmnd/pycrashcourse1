# Make a list of coffee types

coffee_make = ['drip', 'pourover', 'pressed', 'instant']
coffee_roast = ['light', 'medium', 'dark', 'extra dark']
coffee_bean = ['Arabica', 'Robusta', 'Liberica', 'Excelsa']
coffee_brew = ['hot', 'iced', 'cold brew', 'nitro']
drink_type = ['Americano', 'Cappuccino', 'Espresso', 'Latte', 'Macchiato', 'Mocha']


message = f"My favorite coffee drink is {coffee_brew[2], drink_type [2]}"
print(message)

message_2 = f"My least favorite coffee drink is {coffee_brew[3], drink_type[4]}"
print(message_2)
# Remove coffee options that you don't want
too_fatty = 'pressed'
coffee_make.remove(too_fatty)
print(coffee_make)
print(f"\nA {too_fatty.title()} coffee is too fatty for me")
too_bitter = 'Robusta'
coffee_bean.remove(too_bitter)
print(coffee_bean)
print(f"\nA {too_bitter.title()} bean is too bitter for me")
print("Here is the sorted list:")
print(sorted(drink_type))
# Use multiple lists for building coffee drinks
donut_shop = {}
donut_shop['roast'] = 'light'
donut_shop['bean'] = 'Arabica'
donut_shop['brew'] = 'hot'
print("Our Donut Shop cuppa is", donut_shop)