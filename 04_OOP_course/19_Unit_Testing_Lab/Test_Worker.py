from unittest import TestCase, main

from First_Worker import Worker


class TestWorker(TestCase):

    def setUp(self) -> None:
        self.worker = Worker("Pesho", 25_000, 100)

    def test_correct_init(self):
        self.assertEqual("Pesho", self.worker.name)
        self.assertEqual(25_000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_with_zero_or_zero_energy_raise_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work_with_energy_expected_rise_money_decrease_energy(self):
        expected_money = self.worker.salary * 2
        expected_energy = self.worker.energy - 2

        self.worker.work()
        self.worker.work()

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_rest_expect_energy_rise(self):
        expected_energy = self.worker.energy + 1
        self.worker.rest()
        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info(self):
        self.assertEqual(f'Pesho has saved 0 money.', self.worker.get_info())


if __name__ == "__main__":
    main()
