from unittest import TestCase, main
from project.restaurant import Restaurant


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

    def test_get_waiters_with_no_results_expect_empty_list(self):
        self.restaurant.waiters = [{'name': "Jimmy", "total_earnings": 123}, {'name': "Tommy", "total_earnings": 100}]
        result = self.restaurant.get_waiters(max_earnings=80)
        expected = []
        self.assertEqual(expected, result)

        self.assertEqual(
            [{'name': "Jimmy", "total_earnings": 123}, {'name': "Tommy", "total_earnings": 100}],
            self.restaurant.waiters
        )

    def test_add_waiter_happy_case_expect_add_waiter(self):
        result = self.restaurant.add_waiter("Pesho")
        self.restaurant.add_waiter("Tommy")
        self.assertEqual("The waiter Pesho has been added.", result)

        self.assertIn({'name': "Pesho"}, self.restaurant.waiters)
        self.assertEqual([{'name': "Pesho"}, {'name': "Tommy"}], self.restaurant.waiters)

    def test_add_waiter_with_no_capacity_case_expect_error_msg(self):
        self.restaurant.capacity = 1
        self.restaurant.add_waiter("Pesho")
        result = self.restaurant.add_waiter("Tommy")
        self.assertEqual("No more places!", result)
        self.assertEqual([{'name': "Pesho"}], self.restaurant.waiters)

    def test_add_waiter_with_existing_waiter_expect_error_msg(self):
        self.restaurant.capacity = 5
        self.restaurant.add_waiter("Pesho")
        self.restaurant.add_waiter("Tommy")
        result = self.restaurant.add_waiter("Pesho")
        self.assertEqual("The waiter Pesho already exists!", result)
        self.assertEqual([{'name': "Pesho"}, {'name': "Tommy"}], self.restaurant.waiters)

    def test_remove_waiter_existing_waiter_expect_remove_waiter_and_msg(self):
        self.restaurant.add_waiter("Pesho")
        self.restaurant.add_waiter("Tommy")
        self.assertEqual([{'name': "Pesho"}, {'name': "Tommy"}], self.restaurant.waiters)
        result = self.restaurant.remove_waiter("Pesho")
        self.assertEqual(f"The waiter Pesho has been removed.", result)
        self.assertEqual([{'name': "Tommy"}], self.restaurant.waiters)

    def test_remove_waiter_no_existing_waiter_expect_remove_waiter_and_msg(self):
        self.restaurant.add_waiter("Pesho")
        self.restaurant.add_waiter("Tommy")
        self.assertEqual([{'name': "Pesho"}, {'name': "Tommy"}], self.restaurant.waiters)
        result = self.restaurant.remove_waiter("Dido")
        self.assertEqual("No waiter found with the name Dido.", result)
        self.assertEqual([{'name': "Pesho"}, {'name': "Tommy"}], self.restaurant.waiters)

    def test_get_total_earnings(self):
        self.restaurant.waiters = [{'name': "Jimmy", "total_earnings": 123}, {'name': "Tommy", "total_earnings": 100}]
        result = self.restaurant.get_total_earnings()
        self.assertEqual(223, result)

    def test_get_total_earnings_with_no_waiters(self):
        result = self.restaurant.get_total_earnings()
        self.assertEqual(0, result)


if __name__ == "__main__":
    main()
