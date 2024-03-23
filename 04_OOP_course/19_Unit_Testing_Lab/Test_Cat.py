from unittest import TestCase, main
# from Second_Cat import Cat


class TestCat(TestCase):
    def setUp(self) -> None:
        self.cat = Cat("Puhi")

    def test_correct_init(self):
        self.assertEqual("Puhi", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_eat_when_cat_is_fed(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_eat_when_cat_is_hungry_expect_cat_to_become_sleepy_and_size_increase(self):
        expected_size = self.cat.size + 1

        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(expected_size, self.cat.size)

    def test_sleep_if_cat_hungry_expect_exception(self):
        self.cat.fed = False

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_sleep_fed_cat_expect_to_not_be_sleepy(self):
        self.cat.fed = True
        self.cat.sleepy = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()
