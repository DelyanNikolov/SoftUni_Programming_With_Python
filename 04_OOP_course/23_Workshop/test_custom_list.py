from unittest import TestCase

from custom_exeptions import EmptyListException
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
        self.assertEqual([1, "Asd", 7, 100], self.list._CustomList__values)

    def test_remove_with_negative_index_expect_error(self):
        self.list._CustomList__values = [1, "Asd", 7, 100]
        with self.assertRaises(ValueError) as ve:
            self.list.remove(-1)
        self.assertEqual("Index must be positive integer!", str(ve.exception))
        self.assertEqual([1, "Asd", 7, 100], self.list._CustomList__values)

    def test_remove_with_over_length_index_expect_error(self):
        self.list._CustomList__values = [1, "Asd", 7, 100]
        with self.assertRaises(ValueError) as ve:
            self.list.remove(4)
        self.assertEqual("Index out of range!", str(ve.exception))
        self.assertEqual([1, "Asd", 7, 100], self.list._CustomList__values)

    def test_check_get_with_invalid_types_indexes_expect_error(self):
        self.list._CustomList__values = [1, "Asd", 7, 100]
        invalid_indexes = ["asd", [1, 2, 3], {"f": 1}, 2.25]
        for index in invalid_indexes:
            with self.assertRaises(TypeError) as te:
                self.list.get(index)
                self.assertEqual("Index must be of type integer!", str(te.exception))
        self.assertEqual([1, "Asd", 7, 100], self.list._CustomList__values)

    def test_check_get_with_negative_index_expect_error(self):
        self.list._CustomList__values = [1, "Asd", 7, 100]
        with self.assertRaises(ValueError) as ve:
            self.list.get(-1)
        self.assertEqual("Index must be positive integer!", str(ve.exception))
        self.assertEqual([1, "Asd", 7, 100], self.list._CustomList__values)

    def test_check_get_with_out_of_range_indexes_expect_error(self):
        self.list._CustomList__values = [1, "Asd", 7, 100]
        invalid_indexes = [4, 5]
        for index in invalid_indexes:
            with self.assertRaises(ValueError) as ve:
                self.list.get(index)
                self.assertEqual("Index out of range!", str(ve.exception))
        self.assertEqual([1, "Asd", 7, 100], self.list._CustomList__values)

    def test_check_get_with_valid_index_expect_error(self):
        self.list._CustomList__values = [1, "Asd", 7, 100]
        result = self.list.get(0)
        self.assertEqual(1, result)

        result = self.list.get(1)
        self.assertEqual("Asd", result)

    def test_extend_valid_iterable_argument_expect_add_arguments(self):
        self.list._CustomList__values = [1, "Asd", 7, 100]
        result = self.list.extend(["I", "am", "Batman"])
        self.assertEqual([1, "Asd", 7, 100, "I", "am", "Batman"], self.list._CustomList__values)
        self.assertEqual([1, "Asd", 7, 100, "I", "am", "Batman"], result)

    def test_extend_invalid_iterable_argument_expect_add_arguments(self):
        invalid_args = [1, 2.25, None]
        self.list._CustomList__values = [1, "Asd", 7, 100]
        for argument in invalid_args:
            with self.assertRaises(ValueError) as ve:
                self.list.extend(argument)
                self.assertEqual("Value is not iterable!", str(ve.exception))
        self.assertEqual([1, "Asd", 7, 100], self.list._CustomList__values)

    def test_insert_with_valid_indexes_expect_insert_value_correct_index_return_array(self):
        self.list._CustomList__values = [1, "Asd", 7, 100]
        result = self.list.insert(0, "test")
        self.assertEqual(["test", 1, "Asd", 7, 100], result)
        self.assertEqual(["test", 1, "Asd", 7, 100], self.list._CustomList__values)

        self.list._CustomList__values = [1, "Asd", 7, 100]
        result = self.list.insert(2, "test")
        self.assertEqual([1, "Asd", "test", 7, 100], result)
        self.assertEqual([1, "Asd", "test", 7, 100], self.list._CustomList__values)

        self.list._CustomList__values = [1, "Asd", 7, 100]
        result = self.list.insert(3, "test")
        self.assertEqual([1, "Asd", 7, "test", 100], result)
        self.assertEqual([1, "Asd", 7, "test", 100], self.list._CustomList__values)

    def test_insert_with_out_of_boundary_index_expect_insert_value_correct_index_return_array(self):
        self.list._CustomList__values = [1, "Asd", 7, 100]
        with self.assertRaises(ValueError) as ve:
            self.list.insert(4, "test")
        self.assertEqual("Index out of range!", str(ve.exception))
        self.assertEqual([1, "Asd", 7, 100], self.list._CustomList__values)

    def test_pop_with_values_expect_remove_last_value_returns_value(self):
        self.list._CustomList__values = [1, "Asd", 7, 100]
        result = self.list.pop()
        self.assertEqual(100, result)
        self.assertEqual([1, "Asd", 7], self.list._CustomList__values)

    def test_pop_with_empty_array_expect_error(self):
        with self.assertRaises(EmptyListException) as ex:
            self.list.pop()
        self.assertEqual("You can't pop out of an empty list!", str(ex.exception))

    def test_clear_expected_clears_array(self):
        self.list._CustomList__values = [1, "Asd", 7, 100]
        self.list.clear()
        self.assertEqual([], self.list._CustomList__values)

    def test_index_existing_value_expected_return_correct_index(self):
        self.list._CustomList__values = [1, "Asd", 7, 100]
        result = self.list.index(7)
        self.assertEqual(2, result)

    def test_index_non_existing_value_expected_return_correct_index(self):
        self.list._CustomList__values = [1, "Asd", 7, 100]
        result = self.list.index(20)
        self.assertEqual(None, result)

    def test_count_with_one_existing_value_expect_return_1(self):
        self.list._CustomList__values = [1, "Asd", 7, 100]
        result = self.list.count(7)
        self.assertEqual(1, result)

    def test_count_with_multiple_existing_values_expect_return_correct_count(self):
        self.list._CustomList__values = [7, 1, "Asd", 7, 7, 100, 7]
        result = self.list.count(7)
        self.assertEqual(4, result)

    def test_count_with_non_existing_values_expect_return_correct_count(self):
        self.list._CustomList__values = [7, 1, "Asd", 7, 7, 100, 7]
        result = self.list.count(20)
        self.assertEqual(0, result)

    def test_reverse_expected_return_reversed_array_in_new_array(self):
        self.list._CustomList__values = [1, "Asd", 7, 100]
        result = self.list.reverse()
        self.assertEqual([100, 7, "Asd", 1], result)
        self.assertEqual([1, "Asd", 7, 100], self.list._CustomList__values)
        self.assertIsNot(self.list._CustomList__values, result)

    def test_copy_expect_return_copy_of_list(self):
        self.list._CustomList__values = [1, "Asd", 7, 100]
        result = self.list.copy()
        self.assertEqual([1, "Asd", 7, 100], result)
        self.assertIsNot(self.list._CustomList__values, result)

    def test_size_with_non_empty_array_expect_correct_count(self):
        self.list._CustomList__values = [1, "Asd", 7, 100, {"b": 1, "c": 2}]
        result = self.list.size()
        self.assertEqual(5, result)

    def test_size_with_empty_array_expect_correct_count(self):
        result = self.list.size()
        self.assertEqual(0, result)

    def test_add_first_expected_add_on_index_0(self):
        self.list._CustomList__values = [1, "Asd", 7, 100]
        self.list.add_first(0)
        self.assertEqual([0, 1, "Asd", 7, 100], self.list._CustomList__values)
        self.assertEqual(0, self.list._CustomList__values[0])

    def test_add_first_with_empty_array_expected_add_on_index_0(self):
        self.list.add_first(0)
        self.assertEqual([0], self.list._CustomList__values)
        self.assertEqual(0, self.list._CustomList__values[0])

        self.list.add_first("asd")
        self.assertEqual(["asd", 0], self.list._CustomList__values)
        self.assertEqual("asd", self.list._CustomList__values[0])

    def test_dictionize_with_even_length(self):
        self.list._CustomList__values = ["one", 1, "two", 2, "tree", 3]
        result = self.list.dictionize()
        self.assertEqual({"one": 1, "two": 2, "tree": 3}, result)

    def test_dictionize_with_odd_length(self):
        self.list._CustomList__values = ["one", 1, "two", 2, "tree"]
        result = self.list.dictionize()
        self.assertEqual({"one": 1, "two": 2, "tree": " "}, result)

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

    def test_overbound_with_only_nums_expected_correct_result(self):
        self.list._CustomList__values = [1, 2, 2, 3, 5, 100]
        result = self.list.overbound()
        self.assertEqual(5, result)

    def test_overbound_with_mixed_types_values_expected_correct_result(self):
        self.list._CustomList__values = [1, 2, "asd", {"a": 1, "b": 2}]
        result = self.list.overbound()
        self.assertEqual(2, result)

    def test_underbound_with_empty_array_expected_None_result(self):
        result = self.list.underbound()
        self.assertIsNone(result)

    def test_underbound_with_only_nums_expected_correct_result(self):
        self.list._CustomList__values = [1, 2, 2, 3, 5, 100]
        result = self.list.underbound()
        self.assertEqual(0, result)

    def test_underbound_with_mixed_types_values_expected_correct_result(self):
        self.list._CustomList__values = [12, 2, "asd", 1, {"a": 1, "b": 2}]
        result = self.list.underbound()
        self.assertEqual(3, result)

    def test_underbound_with_mixed_types_values_with_two_equal_values_expected_correct_result(self):
        self.list._CustomList__values = [1, 2, "asd", 1, {"a": 1, "b": 2}]
        result = self.list.underbound()
        self.assertEqual(0, result)

    def test_overbound_with_empty_array_expected_None_result(self):
        result = self.list.overbound()
        self.assertIsNone(result)
