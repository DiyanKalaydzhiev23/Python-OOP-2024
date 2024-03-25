from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("Hero", 1, 100, 100)
        self.enemy = Hero("Enemy", 1, 50, 50)

    def test_correct__init__(self):
        self.assertEqual("Hero", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.damage)
        self.assertEqual(100, self.hero.health)

    def test_battle_hero_with_himself_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hero_with_zero_health_raises_value_error(self):
        self.hero.health = 0  # Arrange
        expected_string = "Your health is lower than or equal to 0. You need to rest"

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)  # Act

        self.assertEqual(expected_string, str(ve.exception))  # Assert

    def test_battle_enemy_with_zero_health_raises_value_error(self):
        self.enemy.health = 0  # Arrange
        expected_string = f"You cannot fight {self.enemy.username}. He needs to rest"

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)  # Act

        self.assertEqual(expected_string, str(ve.exception))  # Assert

    def test_fight_with_result_draw_returns_draw_and_decreases_health_on_both_players(self):
        self.hero.health = 50

        result = self.hero.battle(self.enemy)

        self.assertEqual("Draw", result)
        self.assertEqual(-50, self.enemy.health)
        self.assertEqual(0, self.hero.health)

    def test_fight_enemy_and_win_expect_stats_increase(self):
        expected_level = self.hero.level + 1
        expected_damage = self.hero.damage + 5
        expected_health = self.hero.health - self.enemy.damage + 5

        result = self.hero.battle(self.enemy)

        self.assertEqual("You win", result)
        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)

    def test_fight_enemy_and_lose_expect_enemy_stats_increase(self):
        self.hero, self.enemy = self.enemy, self.hero

        expected_level = self.enemy.level + 1
        expected_damage = self.enemy.damage + 5
        expected_health = self.enemy.health - self.hero.damage + 5

        result = self.hero.battle(self.enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(expected_level, self.enemy.level)
        self.assertEqual(expected_health, self.enemy.health)
        self.assertEqual(expected_damage, self.enemy.damage)

    def test_correct__str__(self):
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                          f"Health: {self.hero.health}\n" \
                          f"Damage: {self.hero.damage}\n"

        self.assertEqual(expected_result, str(self.hero))


if __name__ == "__main__":
    main()
