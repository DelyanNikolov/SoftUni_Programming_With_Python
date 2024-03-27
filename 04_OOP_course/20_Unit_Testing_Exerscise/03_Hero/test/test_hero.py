from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Pesho", 75, 100, 30)
        self.enemy_hero = Hero("Gosho", 70, 100, 20)

    def test_correct_init(self):
        self.assertEqual("Pesho", self.hero.username)
        self.assertEqual(75, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(30, self.hero.damage)

    def test_battle_with_same_hero_expected_error(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_zero_health_hero_expected_value_error_msg(self):
        expected_error_msg = "Your health is lower than or equal to 0. You need to rest"
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(expected_error_msg, str(ve.exception))

    def test_battle_with_zero_health_enemy_hero_expected_value_error_msg(self):
        expected_error_msg = f"You cannot fight Gosho. He needs to rest"
        self.enemy_hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(expected_error_msg, str(ve.exception))

    def test_battle_with_valid_heroes_draw_scenario_expected_both_heroes_health_decrease_below_zero(self):
        expected_msg = "Draw"
        battle_result = self.hero.battle(self.enemy_hero)

        self.assertEqual(expected_msg, battle_result)
        self.assertEqual(-1300, self.hero.health)
        self.assertEqual(-2150, self.enemy_hero.health)

    def test_battle_hero_wins_expected_increase_stats_win_msg(self):
        self.enemy_hero.damage = 1

        expected_msg = "You win"
        expected_level = self.hero.level + 1
        expected_health = self.hero.health - self.enemy_hero.damage * self.enemy_hero.level + 5
        expected_damage = self.hero.damage + 5

        battle_result = self.hero.battle(self.enemy_hero)
        self.assertEqual(expected_msg, battle_result)

        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)

    def test_battle_enemy_hero_wins_expected_increase_stats_win_msg(self):
        self.hero.damage = 1

        expected_msg = "You lose"
        expected_level = self.enemy_hero.level + 1
        expected_health = self.enemy_hero.health - self.hero.damage * self.hero.level + 5
        expected_damage = self.enemy_hero.damage + 5

        battle_result = self.hero.battle(self.enemy_hero)
        self.assertEqual(expected_msg, battle_result)

        self.assertEqual(expected_level, self.enemy_hero.level)
        self.assertEqual(expected_health, self.enemy_hero.health)
        self.assertEqual(expected_damage, self.enemy_hero.damage)

    def test_str_repr(self):
        expected_msg = f"Hero Pesho: 75 lvl\n" \
                       f"Health: 100\n" \
                       f"Damage: 30\n"

        self.assertEqual(expected_msg, self.hero.__str__())


if __name__ == "__main__":
    main()
