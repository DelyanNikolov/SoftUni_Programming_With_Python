# •	На първия ред е броят на закупените хризантеми – цяло число в интервала [0 ... 200]
# •	На втория ред е броят на закупените рози – цяло число в интервала [0 ... 200]
# •	На третия ред е броят на закупените лалета – цяло число в интервала [0 ... 200]
# •	На четвъртия ред е посочен сезона – [Spring, Summer, Аutumn, Winter]
# •	На петия ред е посочено дали денят е празник – [Y – да / N - не]
chrysanthemum_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()  # Spring, Summer, Аutumn, Winter
holiday = input()  # [Y – да / N - не]

chrysanthemum_price = 0
roses_price = 0
tulips_price = 0

bouquet_discount = 0
flower_quantity_discount = 0
bouquet_cost = 0
holiday_rise = 0
flowers_count = chrysanthemum_count + roses_count + tulips_count

if flowers_count > 20:
    flower_quantity_discount = 0.2

if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2
    roses_price = 4.1
    tulips_price = 2.5
    if tulips_count > 7 and season == "Spring":
        bouquet_discount = 0.05
elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15
    if roses_count >= 10 and season == "Winter":
        bouquet_discount = 0.1

if holiday == "Y":
    holiday_rise = 0.15

bouquet_cost = ((chrysanthemum_count * chrysanthemum_price
                + roses_count * roses_price
                + tulips_count * tulips_price)
                * (1 + holiday_rise))
bouquet_cost *= (1 - bouquet_discount)
bouquet_cost *= (1 - flower_quantity_discount)
bouquet_cost += 2
print(f"{bouquet_cost:.2f}")
