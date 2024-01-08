CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEGI_MENU = 8.15
DELIVERY = 2.50


chicken_menu_pcs = int(input())
fish_menu_pcs = int(input())
vegi_menu_pcs = int(input())

order_price = chicken_menu_pcs * CHICKEN_MENU + fish_menu_pcs * FISH_MENU + vegi_menu_pcs * VEGI_MENU
dessert = order_price * 0.2

print(order_price + dessert + DELIVERY)