# От конзолата се четат по два реда до въвеждане на команда "END":
# •	Име на играч – текст
# •	Брой вкарани голове  – цяло положително число в интервала [1 … 10000]
best_player_name = ""
best_goals = 0
command = input()
while command != "END":
    name_of_player = command
    current_goals = int(input())
    if current_goals > best_goals:
        best_player_name = command
        best_goals = current_goals
    if current_goals >= 10:
        break
    command = input()
print(f"{best_player_name} is the best player!")
if best_goals >= 3:
    print(f"He has scored {best_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_goals} goals.")
