from unittest import TestCase, main

from hash_table import HashTable


class TestHashTable(TestCase):
    def setUp(self) -> None:
        self.table = HashTable()

    def test_init(self):
        self.assertEqual(self.table._HashTable__keys, [None, None, None, None])
        self.assertEqual(self.table._HashTable__values, [None, None, None, None])
        self.assertEqual(self.table._HashTable__length, 4)

    def test_count_without_data(self):
        result = self.table.count
        self.assertEqual(result, 0)

    def test_count_with_data(self):
        self.table._HashTable__keys = [None, "name", None, None]
        self.table._HashTable__values = [None, "Delyan", None, None]

        result = self.table.count
        self.assertEqual(result, 1)

    def test_set_item_with_same_key_expected_replace_value(self):
        self.table._HashTable__keys = [None, "name", None, None]
        self.table._HashTable__values = [None, "Delyan", None, None]

        self.table["name"] = "Pesho"

        self.assertEqual(self.table._HashTable__keys, [None, "name", None, None])
        self.assertEqual(self.table._HashTable__values, [None, "Pesho", None, None])

    def test_set_item_with_non_existing_key_expected_add_key_and_value(self):
        self.table["name"] = "Pesho"

        self.assertEqual(self.table._HashTable__keys, [None, "name", None, None])
        self.assertEqual(self.table._HashTable__values, [None, "Pesho", None, None])

    def test_set_item_with_non_existing_key_and_items_in_dict_expected_add_key_and_value(self):
        self.table["name"] = "Pesho"
        self.table["city"] = "Plovdiv"

        self.assertEqual(self.table._HashTable__keys, [None, 'name', 'city', None])
        self.assertEqual(self.table._HashTable__values, [None, "Pesho", "Plovdiv", None])

    def test_set_item_with_non_existing_key_and_full_items_in_dict_expected_add_key_and_value_resize(self):
        self.table["name"] = "Pesho"
        self.table["city"] = "Plovdiv"
        self.table["email"] = "P@abv.bg"
        self.table["id"] = "123"
        self.table["car"] = "Skoda"

        self.assertEqual(self.table._HashTable__keys, ['email', 'name', 'city', 'id', None, None, 'car', None])
        self.assertEqual(self.table._HashTable__values,
                         ['P@abv.bg', 'Pesho', 'Plovdiv', '123', None, None, 'Skoda', None])

        self.assertEqual(self.table.count, 5)
        self.assertEqual(self.table.__len__(), 8)

    def test_get_item_with_existing_key_expect_return_value(self):
        self.table["name"] = "Pesho"

        result = self.table.__getitem__("name")
        self.assertEqual(result, "Pesho")

    def test_get_item_with_non_existing_key_expect_return_error_msg(self):
        error_msg = f"'Key does not exist!'"
        with self.assertRaises(KeyError) as ke:
            self.table.__getitem__("city")
        self.assertEqual(error_msg, str(ke.exception))

    def test_get_existing_key_expect_return_value(self):
        self.table["name"] = "Pesho"
        result = self.table.get("name")
        self.assertEqual("Pesho", result)

    def test_get_non_existing_key_expect_return_default_none(self):
        result = self.table.get("name")
        self.assertEqual(None, result)

    def test_get_non_existing_key_expect_return_user_select_answer(self):
        result = self.table.get("name", "Try again")
        self.assertEqual("Try again", result)

    def test_str_expect_success(self):
        self.table.add("name", "Pesho")
        self.table.add("car", "Skoda")
        self.table.add("email", "Pesho@abv.bg")
        self.table.add("city", "Plovdiv")
        self.table.add("id", 123)

        expected_msg = "{email: Pesho@abv.bg, name: Pesho, car: Skoda, city: Plovdiv, id: 123 }"

        self.assertEqual(expected_msg, self.table.__str__())

    def test_len(self):
        self.table.add("name", "Pesho")
        self.table.add("car", "Skoda")
        self.table.add("email", "Pesho@abv.bg")
        self.table.add("city", "Plovdiv")
        self.table.add("id", 123)
        self.assertEqual(8, len(self.table))


if __name__ == "__main__":
    main()
