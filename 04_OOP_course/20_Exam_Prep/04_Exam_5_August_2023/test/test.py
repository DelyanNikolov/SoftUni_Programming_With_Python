from unittest import TestCase, main
from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar("Octavia", "liftback", 100_000, 4500.0)
        self.other_car = SecondHandCar("Vectra", "comby", 120000, 4200.0)

    def test_correct_init(self):
        self.assertEqual("Octavia", self.car.model)
        self.assertEqual("liftback", self.car.car_type)
        self.assertEqual(100000, self.car.mileage)
        self.assertEqual(4500.0, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_below_1_expected_value_error_msg(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0.9
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_mileage_with_mac_value_expected_value_error_msg(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_promotional_price_with_new_price_bigger_than_current_expect_value_error_msg(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(4500.50)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price_with_new_price_equal_than_current_expect_value_error_msg(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(4500.00)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price_with_new_price_lower_than_current_expect_value_error_msg(self):
        result = self.car.set_promotional_price(4000)
        self.assertEqual('The promotional price has been successfully set.', result)
        self.car.price = 4000

    def test_need_repair_with_repair_price_greater_than_half_self_price_expected_error_msg(self):
        result = self.car.need_repair(5000, "replace engine")
        self.assertEqual('Repair is impossible!', result)

    def test_need_repair_with_repair_price_equal_to_half_self_price_expected_error_msg(self):
        result = self.car.need_repair(2250, "replace engine")
        self.assertEqual(f'Price has been increased due to repair charges.', result)
        self.assertEqual(6750, self.car.price)
        self.assertEqual(["replace engine"], self.car.repairs)

    def test_compare_greater_than_with_different_car_types_expected_error_msg(self):
        expected_msg = 'Cars cannot be compared. Type mismatch!'
        self.assertEqual(expected_msg, self.car.__gt__(self.other_car))

    def test_compare_greater_than_with_matching_car_types_expected_error_msg(self):
        self.other_car.car_type = "liftback"
        self.assertEqual(True, self.car.__gt__(self.other_car))

    def test_correct_str(self):
        expected_str = f"""Model Octavia | Type liftback | Milage 100000km
Current price: 4500.00 | Number of Repairs: 0"""
        self.assertEqual(expected_str, self.car.__str__())


if __name__ == "__main__":
    main()
