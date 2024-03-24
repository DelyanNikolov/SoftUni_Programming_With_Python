from unittest import TestCase, main

from Forth_Task_Car_Manager import Car


class TestCar(TestCase):
    def setUp(self) -> None:
        self.car = Car("Opel", "Corsa", 8.0, 50)

    def test_constructor_innit(self):
        self.assertEqual("Opel", self.car.make)
        self.assertEqual("Corsa", self.car.model)
        self.assertEqual(8.0, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_with_empty_string_expected_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_with_empty_string_expected_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_with_negative_expected_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -15
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_zero_value_expected_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_negative_fuel_amount_expected_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -15
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_zero_expected_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-10)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_value_below_fuel_capacity_expected_tank_to_fill_with_fuel(self):
        self.car.refuel(15)
        self.assertEqual(15, self.car.fuel_amount)

    def test_refuel_with_more_than_fuel_capacity_expected_tank_to_be_filled_to_max_capacity(self):
        self.car.refuel(100)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_drive_with_not_enough_fuel_expected_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(999999999)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_with_possible_distance_expected_fuel_amount_to_decrease(self):
        self.car.refuel(100)
        self.car.drive(10)
        self.assertEqual(49.2, self.car.fuel_amount)


if __name__ == "__main__":
    main()
