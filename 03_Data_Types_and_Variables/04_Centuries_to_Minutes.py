one_year_in_days = 365.2422

centuries = int(input())

years = int(centuries*100)
days = int(years*one_year_in_days)
hours = int(days * 24)
minutes = int(hours*60)
print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
