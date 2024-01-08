requirements = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"

}
collected_materials = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}

obtained = False
while True:
    materials = input().split()
    for i in range(0, len(materials), 2):
        resource_name = materials[i + 1].lower()
        resource_quantity = int(materials[i])
        if resource_name not in collected_materials.keys():
            collected_materials[resource_name] = resource_quantity
        else:
            collected_materials[resource_name] += resource_quantity
        if collected_materials[resource_name] >= 250:
            if resource_name in requirements.keys():
                print(f"{requirements[resource_name]} obtained!")
                collected_materials[resource_name] -= 250
                obtained = True
                for item, value in collected_materials.items():
                    print(f"{item}: {value}")
                break
    if obtained:
        break
