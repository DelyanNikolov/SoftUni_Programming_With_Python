def start_spring(**kwargs):
    result = ""
    objects = {}
    for s_object, type_o in kwargs.items():
        if type_o not in objects:
            objects[type_o] = []
        objects[type_o].append(s_object)

    for types, names in sorted(objects.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f"{types}:\n"
        for name in sorted(names):
            result += f"-{name}\n"
    return result


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
