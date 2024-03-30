from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.store = ToyStore()

    def test_correct_init(self):
        for key in range(ord("A"), ord("G")):
            self.assertIsNone(self.store.toy_shelf[chr(key)])

    def test_add_toy_with_invalid_shelf_expected_error(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("H", "Pony")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_with_existing_toy_expect_error(self):
        self.store.toy_shelf["B"] = "Teddy Bear"
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("B", "Teddy Bear")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_with_taken_shelf_expected_error(self):
        self.store.toy_shelf["B"] = "Teddy Bear"
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("B", "Pony")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_with_valid_name_and_shelf_expected_toy_on_shelf_message(self):
        self.assertEqual(f"Toy:{'Teddy Bear'} placed successfully!", self.store.add_toy("B", "Teddy Bear"))
        self.assertEqual("Teddy Bear", self.store.toy_shelf["B"])

    def test_remove_toy_with_invalid_shelf_expected_error(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("H", "Teddy Bear")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_with_valid_shelf_invalid_toy_expect_error(self):
        self.store.toy_shelf["B"] = "Teddy Bear"
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("B", "Pony")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_with_valid_shelf_and_toy_expect_shelf_is_none_message(self):
        self.store.toy_shelf["B"] = "Teddy Bear"
        self.assertEqual(f"Remove toy:Teddy Bear successfully!", self.store.remove_toy("B", "Teddy Bear"))
        self.assertIsNone(self.store.toy_shelf["B"])


if __name__ == "__main__":
    main()
