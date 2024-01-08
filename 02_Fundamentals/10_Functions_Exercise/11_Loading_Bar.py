number = int(input())
percents_filled = number // 10

if number == 100:
    print("100% Complete!\n[%%%%%%%%%%]")
else:
    print(f"{number}% [{'%' * percents_filled}{'.' * (10 - percents_filled)}]\nStill loading...")
