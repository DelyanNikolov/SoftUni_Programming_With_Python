contests_data = {}
personal_statistics = {}
while True:
    command = input()
    if command == "no more time":
        break
    line = command.split(" -> ")
    username = line[0]
    contest = line[1]
    points = int(line[2])
    # collecting contest data
    if contest not in contests_data.keys():
        contests_data[contest] = {}
    if username not in contests_data[contest] or points > contests_data[contest][username]:
        contests_data[contest][username] = points

for contest in contests_data.keys():
    print(f"{contest}: {len(contests_data[contest].values())} participants")
    for n, (name, score) in enumerate(sorted(contests_data[contest].items(), key=lambda item: (-item[1], item[0])), 1):
        print(f"{n}. {name} <::> {score}")
        personal_statistics[name] = personal_statistics.get(name, 0) + score
print("Individual standings:")
for n, (name, score_data) in enumerate(sorted(personal_statistics.items(), key=lambda x: (-x[1], x[0])), 1):
    print(f"{n}. {name} -> {score_data}")
