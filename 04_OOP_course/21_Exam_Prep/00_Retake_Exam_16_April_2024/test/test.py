from unittest import TestCase, main

from restaurant import Restaurant


class TestRestaurant(TestCase):
    def setUp(self) -> None:
        self.restaurant = Restaurant("Kavaka", 100)

    def test_init(self):
        self.assertEqual("Kavaka", self.restaurant.name)
        self.assertEqual(100, self.restaurant.capacity)
        self.assertEqual([], self.restaurant.waiters)

    def test_name_with_empty_name_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.new_rest = Restaurant("", 100)
        self.assertEqual("Invalid name!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.new_rest = Restaurant("      ", 100)
        self.assertEqual("Invalid name!", str(ve.exception))

    def test_capacity_with_negative_value_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.new_rest = Restaurant("BBQ", -1)
        self.assertEqual("Invalid capacity!", str(ve.exception))

    def test_capacity_with_negative_zero_expect_success(self):
        self.new_rest = Restaurant("BBQ", 0)
        self.assertEqual(0, self.new_rest.capacity)

    def test_get_waiters_happy_case_with_default_values(self):
        self.restaurant.waiters = [{'name': "Jimmy", "total_earnings": 123}, {'name': "Tommy", "total_earnings": 0}]
        result = self.restaurant.get_waiters()
        expected = [{'name': "Jimmy", "total_earnings": 123}, {'name': "Tommy", "total_earnings": 0}]
        self.assertEqual(expected, result)

    def test_get_waiters_happy_case_with_custom_values(self):
        self.restaurant.waiters = [{'name': "Jimmy", "total_earnings": 123}, {'name': "Tommy", "total_earnings": 0}]
        result = self.restaurant.get_waiters(10, 130)
        expected = [{'name': "Jimmy", "total_earnings": 123}]
        self.assertEqual(expected, result)

    def test_get_waiters_happy_case_with_one_custom_values(self):
        self.restaurant.waiters = [{'name': "Jimmy", "total_earnings": 123}, {'name': "Tommy", "total_earnings": 0}]
        result = self.restaurant.get_waiters(max_earnings=130)
        expected = [{'name': "Jimmy", "total_earnings": 123}, {'name': "Tommy", "total_earnings": 0}]
        self.assertEqual(expected, result)

        self.assertEqual(
            [{'name': "Jimmy", "total_earnings": 123}, {'name': "Tommy", "total_earnings": 0}], self.restaurant.waiters
        )

if __name__ == "__main__":
    main()
