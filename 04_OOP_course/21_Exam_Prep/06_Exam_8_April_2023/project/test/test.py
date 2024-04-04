from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer("Grisho", 27, 100.25)
        self.other_player = TennisPlayer("Jokovich", 26, 200.13)

    def test_correct_innit(self):
        self.assertEqual("Grisho", self.player.name)
        self.assertEqual(27, self.player.age)
        self.assertEqual(100.25, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_short_name_with_2_chars(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "OP"
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_short_name_with_no_chars(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = ""
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_with_under_18(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_happy_case(self):
        self.player.add_new_win("Rolangaross")
        self.assertEqual(["Rolangaross"], self.player.wins)

    def test_add_new_win_with_existing_win_expect_error_msg(self):
        self.player.wins = ["Rolangaross"]
        result = self.player.add_new_win("Rolangaross")
        self.assertEqual(f"Rolangaross has been already added to the list of wins!", result)
        self.assertEqual(["Rolangaross"], self.player.wins)

    def test__lt__(self):
        msg = f'{self.other_player.name} is a top seeded player and he/she is better than {self.player.name}'
        self.assertEqual(msg, self.player < self.other_player)

    def test__lt__reverse(self):
        self.player.points = 300
        msg = f'{self.player.name} is a better player than {self.other_player.name}'
        self.assertEqual(msg, self.player < self.other_player)

    def test_check_str(self):
        message = f"Tennis Player: Grisho\n" \
                  f"Age: 27\n" \
                  f"Points: 100.2\n" \
                  f"Tournaments won: "

        result = self.player.__str__()
        self.assertEqual(message, result)

    def test_str_other_player(self):
        self.other_player.wins = ["Test1", "Test2", "Test3"]
        message = f"Tennis Player: Jokovich\n" \
                  f"Age: 26\n" \
                  f"Points: 200.1\n" \
                  f"Tournaments won: Test1, Test2, Test3"

        self.assertEqual(message, self.other_player.__str__())


if __name__ == "__main__":
    main()
