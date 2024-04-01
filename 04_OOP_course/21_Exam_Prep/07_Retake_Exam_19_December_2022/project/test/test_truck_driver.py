from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):
    def setUp(self) -> None:
        self.truck_driver = TruckDriver("Dick", 1.40)

    def test_correct__init__(self):
        self.assertEqual("Dick", self.truck_driver.name)
        self.assertEqual(1.20, self.truck_driver.money_per_mile)
        self.assertEqual({}, self.truck_driver.available_cargos)
        self.assertEqual(0.0, self.truck_driver.earned_money)
        self.assertEqual(0, self.truck_driver.miles)

    def test_earned_money_with_negative_value_expected_value_error_msg(self):
        with self.assertRaises(ValueError) as ve:
            self.truck_driver.earned_money = -1
        self.assertEqual(f"{self.truck_driver.name} went bankrupt.", str(ve.exception))

    def test_add_cargo_offer_with_existing_offer_expect_exception_msg(self):
        self.truck_driver.available_cargos = {"Varna": 250}
        with self.assertRaises(Exception) as ex:
            self.truck_driver.add_cargo_offer("Varna", 400)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_with_non_existing_offer_expect_success(self):
        expected_msg = f"Cargo for 90 to Sofia was added as an offer."
        result = self.truck_driver.add_cargo_offer("Sofia", 90)
        self.assertEqual(expected_msg, result)
        self.assertEqual({"Sofia": 90}, self.truck_driver.available_cargos)

    def test_drive_best_cargo_offer_with_zero_offers_expect_error_msg(self):
        result = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_drive_best_cargo_offer_with_available_offer_expect_success(self):
        expected_msg = f"{self.truck_driver.name} is driving 400 to Varna."

        self.truck_driver.add_cargo_offer("Sofia", 90)
        self.truck_driver.add_cargo_offer("Varna", 400)

        result = self.truck_driver.drive_best_cargo_offer()

        self.assertEqual(expected_msg, result)
        self.assertEqual(400 * self.truck_driver.money_per_mile - 20, self.truck_driver.earned_money)
        self.assertEqual(400, self.truck_driver.miles)

    def test_check_for_activities(self):
        self.truck_driver.earned_money = 28000
        self.truck_driver.check_for_activities(20_000)
        expected_money = 28000 - (20_000//250 * 20) - (20_000//1000 * 45) - (20_000//1500 * 500) - (20_000//10000 * 7500)
        self.assertEqual(expected_money, self.truck_driver.earned_money)

    def test_repr(self):
        self.assertEqual(f"Dick has 0 miles behind his back.", self.truck_driver.__repr__())


if __name__ == "__main__":
    main()
