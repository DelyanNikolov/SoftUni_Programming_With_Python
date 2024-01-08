days_of_tournament = int(input())
total_charity_money = 0
won_games_total = 0
lost_games_total = 0
tournament_won = False
for _ in range(days_of_tournament):
    command = input()
    won_games_day = 0
    lost_games_day = 0
    daily_charity_money = 0
    while command != "Finish":
        sport = command
        result = input()
        if result == "win":
            daily_charity_money += 20
            won_games_day += 1
            won_games_total += 1
        elif result == "lose":
            lost_games_day += 1
            lost_games_total += 1
        command = input()

    if won_games_day > lost_games_day:
        daily_charity_money += daily_charity_money * 0.1
    total_charity_money += daily_charity_money

if won_games_total > lost_games_total:
    tournament_won = True
    total_charity_money += total_charity_money * 0.2
if tournament_won:
    print(f"You won the tournament! Total raised money: {total_charity_money :.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_charity_money :.2f}")
