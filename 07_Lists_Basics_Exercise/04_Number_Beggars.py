donations = input().split(", ")
beggars_count = int(input())
sum_of_donations_collected = []
for beggar in range(beggars_count):  # for every loop a beggar collects a sum of money
    beggar_money = 0  # setting zero for every beggar collection
    for index in range(beggar, len(donations), beggars_count):
        # index starts form position of the beggar in the que
        # (because they take turns)
        beggar_money += int(donations[index])

    sum_of_donations_collected.append(beggar_money)

print(sum_of_donations_collected)
