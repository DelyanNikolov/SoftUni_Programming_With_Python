
facebook_fine = 150
instagram_fine = 100
reddit_fine = 50

open_tabs = int(input())
salary = float(input())


for tabs in range(1, open_tabs + 1):
    website = input()
    if website == "Facebook":
        salary -= facebook_fine
    elif website == "Instagram":
        salary -= instagram_fine
    elif website == "Reddit":
        salary -= reddit_fine
    if salary <= 0:
        break

if salary <= 0:
    print("You have lost your salary.")
else:
    print(int(salary))
