from collections import Sized
from collections.abc import Iterable

from custom_exeptions import EmptyListException


class CustomList:
    def __init__(self):
        self.__values = []

    def _check_index(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be of type integer!")
        if index < 0:
            raise ValueError("Index must be positive integer!")

        if index >= len(self.__values):
            raise ValueError("Index out of range!")

    def append(self, value):
        self.__values.append(value)
        return self.__values

    def remove(self, index):
        self._check_index(index)
        value = self.__values.pop(index)
        return value

    def get(self, index):
        self._check_index(index)
        value = self.__values[index]
        return value

    def extend(self, value):
        if not isinstance(value, Iterable):
            raise ValueError("Value is not iterable!")
        self.__values.extend(value)
        return self.__values

    def insert(self, index, value):
        self._check_index(index)
        self.__values.insert(index, value)
        return self.__values

    def pop(self):
        if not self.__values:
            raise EmptyListException("You can't pop out of an empty list!")
        return self.__values.pop()

    def clear(self):
        self.__values.clear()

    def index(self, value):
        if value not in self.__values:
            return None
        return self.__values.index(value)

    def count(self, value):
        return self.__values.count(value)

    def reverse(self):
        return self.__values[::-1]

    def copy(self):
        return self.__values[:]

    def size(self):
        return len(self.__values)

    def add_first(self, value):
        self.__values.insert(0, value)

    def dictionize(self):
        result = {}
        for idx in range(0, len(self.__values), 2):
            try:
                result[self.__values[idx]] = self.__values[idx + 1]
            except IndexError:
                result[self.__values[idx]] = " "
        return result

    def move(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Value is not a valid int")

        self.__values = self.__values[n:] + self.__values[:n]
        return self.__values

    def sum(self):
        total = 0
        for element in self.__values:
            if isinstance(element, Sized):
                total += len(element)
            else:
                total += element

        return total

    def overbound(self):
        max_value = float("-inf")
        max_value_index = None

        for index in range(0, len(self.__values)):
            current_element = self.__values[index]

            if isinstance(current_element, Sized):
                current_element = len(current_element)

            if max_value < current_element:
                max_value = current_element
                max_value_index = index

        return max_value_index

    def underbound(self):
        min_value = float("inf")
        min_value_index = None

        for index in range(0, len(self.__values)):
            current_element = self.__values[index]

            if isinstance(current_element, Sized):
                current_element = len(current_element)

            if min_value > current_element:
                min_value = current_element
                min_value_index = index

        return min_value_index
