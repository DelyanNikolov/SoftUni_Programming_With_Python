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

if __name__ == "__main__":
    main()
