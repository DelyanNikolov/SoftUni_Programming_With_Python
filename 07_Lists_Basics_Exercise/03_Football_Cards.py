team_a = []
team_b = []

is_game_terminated = False

for player in range(1, 12):
    team_a.append(f"A-{player}")
    team_b.append(f"B-{player}")

cards = input().split()

for card in cards:
    if card in team_a:
        team_a.remove(card)
    elif card in team_b:
        team_b.remove(card)
    if len(team_a) < 7 or len(team_b) < 7:
        is_game_terminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if is_game_terminated:
    print("Game was terminated")
