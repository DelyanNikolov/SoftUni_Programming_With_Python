from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self) -> None:
        self.station = RailwayStation("Plovdiv")

    def test_correct_init(self):
        self.assertEqual("Plovdiv", self.station.name)
        self.assertEqual(deque(), self.station.arrival_trains)
        self.assertEqual(deque(), self.station.departure_trains)

    def test_name_with_less_than_3_symbols_raise_value_error_msg(self):

        with self.assertRaises(ValueError) as ve:
            self.station.name = "Br"
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board_expected_appends_train(self):
        self.station.new_arrival_on_board("Fast train to Sofia")
        self.assertEqual(deque(["Fast train to Sofia"]), self.station.arrival_trains)

    def test_train_has_arrived_if_there_are_trains_before_train_info_expected_error_msg(self):
        expected_msg = f"There are other trains to arrive before Fast train to Sofia."
        self.station.new_arrival_on_board("Chaika express")
        self.station.new_arrival_on_board("Fast train to Sofia")
        result = self.station.train_has_arrived("Fast train to Sofia")
        self.assertEqual(expected_msg, result)

    def test_train_has_arrived_if_no_trains_before_our_train_expected_msg(self):
        expected_msg = f"Fast train to Sofia is on the platform and will leave in 5 minutes."
        self.station.new_arrival_on_board("Fast train to Sofia")
        result = self.station.train_has_arrived("Fast train to Sofia")
        self.assertEqual(expected_msg, result)

    def test_train_has_left_with_our_train_expected_True(self):
        self.station.new_arrival_on_board("Fast train to Sofia")
        self.station.train_has_arrived("Fast train to Sofia")
        result = self.station.train_has_left("Fast train to Sofia")
        self.assertTrue(result)

    def test_train_has_left_with_not_our_train_expected_False(self):
        self.station.new_arrival_on_board("Chaika express")
        self.station.train_has_arrived("Chaika express")
        result = self.station.train_has_left("Fast train to Sofia")
        self.assertFalse(result)

    def test_train_has_left_with_no_trains_on_board_expected_False(self):
        result = self.station.train_has_left("Fast train to Sofia")
        self.assertFalse(result)


if __name__ == "__main__":
    main()
