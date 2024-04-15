class HashTable:
    def __init__(self):
        self.__keys = [None, None, None, None]
        self.__values = [None, None, None, None]
        self.__length = 4

    @property
    def count(self):
        return len([el for el in self.__keys if el is not None])

    def __setitem__(self, key, value):
        try:
            existing_value_key = self.__keys.index(key)
            self.__values[existing_value_key] = value
        except ValueError:
            if self.count == self.__length:
                self.__resize()
            index = self.__find_index(self.hash_func(key))
            self.__keys[index] = key
            self.__values[index] = value

    def __find_index(self, index):
        if index >= self.__length:
            index = 0
        if self.__keys[index] is None:
            return index
        return self.__find_index(index + 1)

    def hash_func(self, key: str) -> int:
        return sum([ord(char) for char in key]) % self.__length

    def __resize(self):
        self.__keys = self.__keys + [None] * self.__length
        self.__values = self.__values + [None] * self.__length
        self.__length *= 2

    def __getitem__(self, item):
        try:
            index = self.__keys.index(item)
            return self.__values[index]
        except ValueError:
            raise KeyError("Key does not exist!")

    def get(self, key, default_value=None):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            return default_value

    def add(self, key, value):
        self.__setitem__(key, value)

    def __len__(self):
        return self.__length

    def __str__(self):
        result = [f"{self.__keys[index]}: {self.__values[index]}"
                  for index in range(self.__length) if self.__keys[index] is not None]
        return "{" + ", ".join(result) + " }"


table = HashTable()
table["name"] = "Peter"
table["age"] = 25
table["street"] = "Skopie"
table["city"] = "Plovdiv"
table["nickname"] = "Alf"
print(table)
print(table.get("name"))
print(table["age"])
print(len(table))
print(table.count)
table.add("target", "Bol")
table.add("name", "Delyan")
print(table)
