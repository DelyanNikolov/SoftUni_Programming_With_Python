import re

text_with_stops = input()
regex = r"([=/])([A-Z][A-Za-z]{2,})(\1)"
all_valid_locations = re.findall(regex, text_with_stops)
travel_points = 0
locations = []
for location in all_valid_locations:
    name = location[1]
    travel_points += len(name)
    locations.append(name)
print(f"Destinations: {', '.join(locations)}")
print(f"Travel Points: {travel_points}")
