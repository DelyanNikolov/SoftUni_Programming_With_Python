class Integer:
    ROMAN_NUMS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):
        if not isinstance(float_value, float):
            return "value is not a float"

        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value: str):
        int_sum = 0

        for i in range(len(value)):
            if i != 0 and cls.ROMAN_NUMS[value[i]] > cls.ROMAN_NUMS[value[i - 1]]:
                int_sum += cls.ROMAN_NUMS[value[i]] - 2 * cls.ROMAN_NUMS[value[i - 1]]
            else:
                int_sum += cls.ROMAN_NUMS[value[i]]

        return cls(int_sum)

    @classmethod
    def from_string(cls, value: str):
        if not isinstance(value, str):
            return "wrong type"

        return cls(int(value))


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))