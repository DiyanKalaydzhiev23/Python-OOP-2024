from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal(
            "some name",
            "some type",
            "some sound"
        )

    def test_correct_initializing(self):
        self.assertEqual("some name", self.mammal.name)
        self.assertEqual("some type", self.mammal.type)
        self.assertEqual("some sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_if_make_sound_returns_correct_message(self):
        result = self.mammal.make_sound()
        self.assertEqual("some name makes some sound", result)

    def test_if_get_kingdom_returns_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_if_info_returns_correct_message(self):
        result = self.mammal.info()
        self.assertEqual("some name is of type some type", result)


if __name__ == "__main__":
    main()
