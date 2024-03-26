from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.car = Vehicle(100, 50)

    def test_class_attribute(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_init(self):
        self.assertEqual(100, self.car.fuel)
        self.assertEqual(100, self.car.capacity)
        self.assertEqual(50, self.car.horse_power)
        self.assertEqual(self.car.DEFAULT_FUEL_CONSUMPTION, self.car.fuel_consumption)

    def test_drive_with_no_fuel_expected_error(self):
        self.car.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel_expect_fuel_decrease(self):
        self.car.drive(10)
        self.assertEqual(87.5, self.car.fuel)

    def test_refuel_with_more_fuel_than_capacity_expected_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(100)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_valid_fuel_expected_fuel_increase(self):
        self.car.fuel = 80
        self.car.refuel(10)
        self.assertEqual(90, self.car.fuel)

    def test_str_method(self):
        result = self.car.__str__()
        expected = f"The vehicle has 50 " \
                   f"horse power with 100 fuel left and 1.25 fuel consumption"

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
