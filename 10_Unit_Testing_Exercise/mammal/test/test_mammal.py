from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal(
            "some name",
            "some type",
            "some sound",
        )

    def test_correct_init_(self):
        self.assertEqual("some name", self.mammal.name)
        self.assertEqual("some type", self.mammal.type)
        self.assertEqual("some sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_get_sound_returns_correct_string(self):
        self.assertEqual(f"some name makes some sound", self.mammal.make_sound())

    def test_get_kingdom_returns_correct_string(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_get_info_returns_correct_string(self):
        self.assertEqual(f"some name is of type some type", self.mammal.info())


if __name__ == "__main__":
    main()
