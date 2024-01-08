countries = input().split(", ")
cities = input().split(", ")

capitals = {country: city for country, city in zip(countries, cities)}

for item in capitals:
    country = item
    capital = capitals[item]
    print(f"{country} -> {capital}")
