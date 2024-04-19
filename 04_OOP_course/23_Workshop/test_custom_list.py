from unittest import TestCase

from custom_list import CustomList


class TestCustomList(TestCase):
    def setUp(self) -> None:
        self.list = CustomList()

    def test_move(self):
        self.list._CustomList__values = [1, 2, 3, 4, 5]
        result = self.list.move(3)

        self.assertEqual([4, 5, 1, 2, 3], result)

    def test_sum_with_only_numbers(self):
        self.list._CustomList__values = [1, 2, 3, 4, 5]

        result = self.list.sum()
        self.assertEqual(15, result)

    def test_sum_with_mixed_type_values(self):
        self.list._CustomList__values = [1, 2, "asd", {"a": 1, "b": 2}]

        result = self.list.sum()

        self.assertEqual(8, result)