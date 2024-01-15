usernames_count = int(input())
usernames_data = set()
for _ in range(usernames_count):
    username = input()
    usernames_data.add(username)
for item in usernames_data:
    print(item)
