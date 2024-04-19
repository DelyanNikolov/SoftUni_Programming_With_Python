from unittest import TestCase

from custom_list import CustomList


class TestCustomList(TestCase):
    def setUp(self) -> None:
        self.list = CustomList()

    def test_init_expect_success(self):
        self.assertEqual([], self.list._CustomList__values)

    def test_append_expect_success(self):
        self.list.append(1)
        self.assertEqual([1], self.list._CustomList__values)

        self.list.append("Asd")
        self.assertEqual([1, "Asd"], self.list._CustomList__values)

    def test_append_with_existing_values_expect_success_at_end(self):
        self.list._CustomList__values = [1, 2, 3, 4]
        self.list.append(5)
        self.assertEqual([1, 2, 3, 4, 5], self.list._CustomList__values)
        self.assertEqual(5, self.list._CustomList__values[-1])

    def test_remove_with_valid_index_expect_return_value(self):
        self.list._CustomList__values = [1, "Asd", 7, 100]
        result = self.list.remove(0)
        self.assertEqual(1, result)
        self.assertEqual(["Asd", 7, 100], self.list._CustomList__values)

    def test_remove_with_wrong_type_index_expect_error(self):
        self.list._CustomList__values = [1, "Asd", 7, 100]
        with self.assertRaises(TypeError) as te:
            self.list.remove("sss")
        self.assertEqual("Index must be of type integer!", str(te.exception))

    def test_remove_with_negative_index_expect_error(self):
        self.list._CustomList__values = [1, "Asd", 7, 100]
        with self.assertRaises(ValueError) as ve:
            self.list.remove(-1)
        self.assertEqual("Index must be positive integer!", str(ve.exception))

    def test_remove_with_over_length_index_expect_error(self):
        self.list._CustomList__values = [1, "Asd", 7, 100]
        with self.assertRaises(ValueError) as ve:
            self.list.remove(4)
        self.assertEqual("Index out of range!", str(ve.exception))

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
