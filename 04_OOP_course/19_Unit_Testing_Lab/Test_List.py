from unittest import TestCase, main

from Third_Task_List import IntegerList


class TestIntegerList(TestCase):

    def setUp(self) -> None:
        self.int_list = IntegerList(5.5, 1, 2, 3, "hello")

    def test_constructor(self):
        self.assertEqual([1, 2, 3], self.int_list.get_data())

    def test_add_non_integer_value_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.int_list.add(5.5)
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_integer_expected_to_add_to_list(self):
        expected_list = self.int_list.get_data() + [4]
        self.int_list.add(4)
        self.assertEqual(expected_list, self.int_list.get_data())

    def test_remove_element_by_non_valid_index_expect_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.remove_index(99999)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_element_with_valid_index_expect_to_remove_element(self):
        expected_list = [1, 3]
        self.int_list.remove_index(1)
        self.assertEqual(expected_list, self.int_list.get_data())

    def test_get_element_with_invalid_index_expect_error(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.get(99999)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_element_with_valid_index_and_return_element(self):
        element = self.int_list.get(1)
        self.assertEqual(2, element)

    def test_insert_valid_element_with_invalid_index_expect_error(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.insert(99999, 12)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_invalid_element_with_valid_index_expect_error(self):
        with self.assertRaises(ValueError) as ve:
            self.int_list.insert(1, "hello")
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_valid_element_with_valid_index(self):
        expected_list = self.int_list.get_data().copy()
        expected_list.insert(1, 10)
        self.int_list.insert(1, 10)
        self.assertEqual(expected_list, self.int_list.get_data())

    def test_get_biggest(self):
        biggest = self.int_list.get_biggest()
        self.assertEqual(3, biggest)

    def test_get_index(self):
        element_index = self.int_list.get_index(2)
        self.assertEqual(1, element_index)


if __name__ == "__main__":
    main()
