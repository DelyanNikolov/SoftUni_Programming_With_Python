
cat_breed = input()     #"British Shorthair", "Siamese", "Persian", "Ragdoll", "American Shorthair" или "Siberian"
cat_sex = input()       #'m' или 'f'
cat_years = 0
invalid_cat = False
if cat_sex == "m":
    if cat_breed == "British Shorthair":
        cat_years = 13
    elif cat_breed == "Siamese":
        cat_years = 15
    elif cat_breed == "Persian":
        cat_years = 14
    elif cat_breed == "Ragdoll":
        cat_years = 16
    elif cat_breed == "American Shorthair":
        cat_years = 12
    elif cat_breed == "Siberian":
        cat_years = 11
    else:
        invalid_cat = True
elif cat_sex == "f":
    if cat_breed == "British Shorthair":
        cat_years = 14
    elif cat_breed == "Siamese":
        cat_years = 16
    elif cat_breed == "Persian":
        cat_years = 15
    elif cat_breed == "Ragdoll":
        cat_years = 17
    elif cat_breed == "American Shorthair":
        cat_years = 13
    elif cat_breed == "Siberian":
        cat_years = 12
    else:
        invalid_cat = True
if not invalid_cat:
    cat_months = int((cat_years * 12) / 6)
    print(f"{cat_months} cat months")
else:
    print(f"{cat_breed} is invalid cat!")
