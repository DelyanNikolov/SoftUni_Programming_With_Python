population = [int(pop) for pop in input().split(", ")]
minimum_wealth = int(input())

for index in range(len(population)):
    if population[index] < minimum_wealth:
        max_pop = max(population)
        max_pop_index = population.index(max_pop)
        difference = minimum_wealth - population[index]
        # if population[max_pop_index] >= minimum_wealth + difference:
        population[max_pop_index] -= difference
        population[index] += difference

below_minimum_wealth = [stat for stat in population if stat < minimum_wealth]
if below_minimum_wealth:
    print("No equal distribution possible")
else:
    print(population)
