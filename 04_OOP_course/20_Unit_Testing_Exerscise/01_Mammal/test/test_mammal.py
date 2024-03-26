from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Brain", "Dolphin", "Eeek...eeek...")

    def test_correct_init(self):
        self.assertEqual("Brain", self.mammal.name)
        self.assertEqual("Dolphin", self.mammal.type)
        self.assertEqual("Eeek...eeek...", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_expected_str(self):
        sound = self.mammal.make_sound()
        self.assertEqual("Brain makes Eeek...eeek...", sound)

    def test_get_kingdom_expected_str_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_info_expected_str(self):
        self.assertEqual("Brain is of type Dolphin", self.mammal.info())


if __name__ == "__main__":
    main()
