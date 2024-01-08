company_users = {}

command = input()
while command != "End":
    company_name, employee_id = command.split(" -> ")
    if company_name not in company_users.keys():
        company_users[company_name] = []
    if employee_id not in company_users[company_name]:
        company_users[company_name].append(employee_id)
    command = input()

for name, user in company_users.items():
    print(name)
    for i in user:
        print(f"-- {i}")
