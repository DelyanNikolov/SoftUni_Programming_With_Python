PUZZLE = 2.60
TALKING_DOLL = 3.00
TEDDY_BEAR = 4.10
MINION = 8.20
TRUCK = 2.00

vacation_prise = float(input())
puzzle_pcs = int(input())
talking_doll_pcs = int(input())
teddy_bear_pcs = int(input())
minions_pcs = int(input())
trucks_pcs = int(input())


toys_pcs = puzzle_pcs + talking_doll_pcs + teddy_bear_pcs + minions_pcs + trucks_pcs

discount = 0

if toys_pcs >= 50:
    discount = 0.25
income = puzzle_pcs * PUZZLE\
         + talking_doll_pcs * TALKING_DOLL\
         + teddy_bear_pcs * TEDDY_BEAR \
         + minions_pcs * MINION \
         + trucks_pcs * TRUCK
profit = income * (1 - discount)
rent = profit * 0.1
final_income = profit - rent

if final_income >= vacation_prise:
    print(f"Yes! {final_income - vacation_prise:.2f} lv left.")
else: print(f"Not enough money! {vacation_prise - final_income:.2f} lv needed.")