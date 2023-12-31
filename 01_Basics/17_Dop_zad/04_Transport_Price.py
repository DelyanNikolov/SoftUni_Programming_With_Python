# Студент трябва да пропътува n километра. Той има избор измежду три вида транспорт:
# •	Такси. Начална такса: 0.70 лв. Дневна тарифа: 0.79 лв. / км. Нощна тарифа: 0.90 лв. / км.
# •	Автобус. Дневна / нощна тарифа: 0.09 лв. / км. Може да се използва за разстояния минимум 20 км.
# •	Влак. Дневна / нощна тарифа: 0.06 лв. / км. Може да се използва за разстояния минимум 100 км.
# Напишете програма, която въвежда броя километри n и период от деня (ден или нощ) и изчислява цената
# на най-евтиния транспорт.
# Вход
# От конзолата се четат два реда:
# •	Първият ред съдържа числото n – брой километри – цяло число в интервала [1…5000]
# •	Вторият ред съдържа дума “day” или “night” – пътуване през деня или през нощта
n_kilometers = int(input())
time_of_day = input()

journey_cost = 0
taxi_cost = 0.70

if time_of_day == "night":
    taxi_cost += 0.9 * n_kilometers
else:
    taxi_cost += 0.79 * n_kilometers

bus_cost = 0.09 * n_kilometers
train_cost = 0.06 * n_kilometers
if n_kilometers < 20:
    journey_cost = taxi_cost
elif n_kilometers < 100:
    journey_cost = bus_cost
else:
    journey_cost = train_cost

print(f"{journey_cost:.2f}")
