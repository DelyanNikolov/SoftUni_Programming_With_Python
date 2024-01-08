annual_tax = int(input())
shoes_for_basketball = annual_tax - annual_tax * 0.4
uniform_for_basketball = shoes_for_basketball - shoes_for_basketball * 0.2
ball_for_basketball = uniform_for_basketball / 4
accessoaries_for_basketball = ball_for_basketball / 5

total_cost_for_basketball_training = annual_tax\
                                     + shoes_for_basketball\
                                     + uniform_for_basketball\
                                     + ball_for_basketball\
                                     + accessoaries_for_basketball
print(total_cost_for_basketball_training)