seasonal_tire = {}

while True:
    command = input()
    if "Season end" in command:
        break
    if " -> " in command:
        line = command.split(" -> ")
        player = line[0]
        position = line[1]
        skill = int(line[2])
        if player not in seasonal_tire.keys():
            seasonal_tire[player] = {}
        if position not in seasonal_tire[player].keys() or seasonal_tire[player][position] < skill:
            seasonal_tire[player][position] = skill
    elif " vs " in command:
        line = command.split(" vs ")
        player_one = line[0]
        player_two = line[1]
        match = False
        if player_one in seasonal_tire and player_two in seasonal_tire:
            battle_score_player_one = 0
            battle_score_player_two = 0
            for position in seasonal_tire[player_one].keys():
                if position in seasonal_tire[player_two].keys():
                    battle_score_player_one += seasonal_tire[player_one][position]
                    battle_score_player_two += seasonal_tire[player_two][position]
            if battle_score_player_one > battle_score_player_two:
                del seasonal_tire[player_two]
            elif battle_score_player_one < battle_score_player_two:
                del seasonal_tire[player_one]
max_points = {player: sum(seasonal_tire[player].values()) for player in seasonal_tire.keys()}

for player, points in sorted(max_points.items(), key=lambda item: (-item[1], item[0])):
    print(f"{player}: {max_points[player]} skill")
    for position, skill in (sorted(seasonal_tire[player].items(), key=lambda item: (-item[1], item[0]))):
        print(f"- {position} <::> {skill}")
