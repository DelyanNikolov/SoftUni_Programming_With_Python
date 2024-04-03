from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self) -> None:
        self.robot = Robot("C3PO", "Humanoids", 100, 5000)

        self.robot_with_upgrades = Robot("R2D2", "Entertainment", 200, 1000)
        self.robot_with_upgrades.hardware_upgrades = ["Hologram projector", "Stereo player"]
        self.robot_with_upgrades.software_updates = [1.01]

    def test_correct_init(self):
        self.assertEqual("C3PO", self.robot.robot_id)
        self.assertEqual("Humanoids", self.robot.category)
        self.assertEqual(100, self.robot.available_capacity)
        self.assertEqual(5000, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_category_setter_with_invalid_category_expected_value_error_msg(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Flying"
        self.assertEqual(f"Category should be one of '{Robot.ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_price_with_negative_value_expected_value_error_msg(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -100
        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_with_already_installed_component_expect_error_msg(self):
        expected_msg = f"Robot {self.robot_with_upgrades.robot_id} was not upgraded."
        result = self.robot_with_upgrades.upgrade("Hologram projector", 500)
        self.assertEqual(expected_msg, result)
        self.assertEqual(1000, self.robot_with_upgrades.price)

    def test_upgrade_robot_with_upgrades_happy_case_expect_add_component_price_increase_and_msg(self):
        expected_msg = f'Robot {self.robot_with_upgrades.robot_id} was upgraded with DVD.'
        result = self.robot_with_upgrades.upgrade("DVD", 500)
        expected_price = 1000 + (500 * Robot.PRICE_INCREMENT)
        self.assertEqual(expected_msg, result)

        self.assertEqual(["Hologram projector", "Stereo player", "DVD"], self.robot_with_upgrades.hardware_upgrades)
        self.assertEqual(expected_price, self.robot_with_upgrades.price)

    def test_update_with_no_updates_installed_and_available_capacity_expect_success_msg(self):
        expected_msg = f'Robot {self.robot.robot_id} was updated to version 1.01.'
        result = self.robot.update(1.01, 100)
        self.assertEqual(expected_msg, result)
        self.assertEqual(0, self.robot.available_capacity)

    def test_update_with_updates_installed_and_version_equal_to_and_available_capacity_expect_error_msg(self):
        expected_msg = f"Robot {self.robot_with_upgrades.robot_id} was not updated."
        result = self.robot_with_upgrades.update(1.01, 50)
        self.assertEqual(expected_msg, result)

    def test_update_with_updates_installed_and_version_equal_to_and_no_available_capacity_expect_error_msg(self):
        expected_msg = f"Robot {self.robot_with_upgrades.robot_id} was not updated."
        result = self.robot_with_upgrades.update(1.01, 201)
        self.assertEqual(expected_msg, result)

    def test_update_with_updates_installed_and_version_smaller_to_and_available_capacity_expect_error_msg(self):
        expected_msg = f"Robot {self.robot_with_upgrades.robot_id} was not updated."
        result = self.robot_with_upgrades.update(1.0, 50)
        self.assertEqual(expected_msg, result)

    def test_update_with_updates_installed_and_version_smaller_to_and_no_available_capacity_expect_error_msg(self):
        expected_msg = f"Robot {self.robot_with_upgrades.robot_id} was not updated."
        result = self.robot_with_upgrades.update(1.0, 201)
        self.assertEqual(expected_msg, result)

    def test_update_with_updates_installed_and_version_bigger_to_and_no_available_capacity_expect_error_msg(self):
        expected_msg = f"Robot {self.robot_with_upgrades.robot_id} was not updated."
        result = self.robot_with_upgrades.update(1.02, 201)
        self.assertEqual(expected_msg, result)

    def test_update_with_updates_installed_and_version_bigger_to_and_with_available_capacity_expect_error_msg(self):
        expected_msg = f'Robot {self.robot_with_upgrades.robot_id} was updated to version 1.02.'
        result = self.robot_with_upgrades.update(1.02, 200)
        self.assertEqual(expected_msg, result)

    def test_greater_than_method(self):
        expected_msg = f'Robot with ID {self.robot.robot_id} is more expensive than Robot with ID {self.robot_with_upgrades.robot_id}.'
        result = self.robot.__gt__(self.robot_with_upgrades)

        self.assertEqual(expected_msg, result)

    def test_greater_than_method_with_equal_prices(self):
        self.robot.price = 1000
        expected_msg = f'Robot with ID {self.robot.robot_id} costs equal to Robot with ID {self.robot_with_upgrades.robot_id}.'
        result = self.robot.__gt__(self.robot_with_upgrades)

        self.assertEqual(expected_msg, result)

    def test_greater_than_method_with_smaller_prices(self):
        self.robot.price = 999
        expected_msg = f'Robot with ID {self.robot.robot_id} is cheaper than Robot with ID {self.robot_with_upgrades.robot_id}.'
        result = self.robot.__gt__(self.robot_with_upgrades)

        self.assertEqual(expected_msg, result)
if __name__ == "__main__":
    main()
