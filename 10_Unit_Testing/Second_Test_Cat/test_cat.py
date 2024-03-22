from unittest import TestCase, main
from Second_Test_Cat.cat import Cat


class TestCat(TestCase):

    def setUp(self):
        self.cat = Cat("Pancho")

    def test_correct_init(self):
        self.assertEqual("Pancho", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_feed_cat_makes_cat_sleepy_and_not_hungry_expect_size_increase_by_1(self):
        expected_size = self.cat.size + 1

        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(expected_size, self.cat.size)

    def test_feed_cat_when_cat_is_already_fed_raise_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_sleepy_cat_sleeps_and_its_not_sleepy_after_that(self):
        self.cat.sleepy = True
        self.cat.fed = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)

    def test_make_hungry_cat_sleep_raises_exception(self):
        self.cat.fed = False

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))


if __name__ == "__main__":
    main()
