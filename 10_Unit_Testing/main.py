from unittest import TestCase, main


class MyCar:

    def __init__(self, model: str, hp: int):
        self.model = model
        self.hp = hp


# Test suite
class TestMyCar(TestCase):

    def test_correct_init(self):
        model, hp = "BMW", 100  # Arrange

        my_car = MyCar(model, hp)  # Act

        self.assertEqual(my_car.model, model)
        self.assertEqual(my_car.hp, hp)


if __name__ == "__main__":
    main()
