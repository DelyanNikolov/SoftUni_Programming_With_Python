def forecast(*locations):
    result = []
    weather_data = {}

    for item in locations:
        location = item[0]
        weather = item[1]
        weather_data[location] = weather

    weather_order = {"Sunny": 0, "Cloudy": 1, "Rainy": 2}
    sorted_loc = sorted(weather_data.items(), key=lambda x: (weather_order[x[1]], x[0]))

    for city, condition in sorted_loc:
        result.append(f"{city} - {condition}")

    return '\n'.join(result)


print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
