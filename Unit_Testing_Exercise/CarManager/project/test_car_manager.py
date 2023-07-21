from unittest import TestCase, main
# from project.car_manager import Car


class TestCar(TestCase):

    def setUp(self):
        self.car = Car("Nissan", "GT-R", 15, 75)

    def test_correct_initialization(self):
        self.assertEqual("Nissan", self.car.make)
        self.assertEqual("GT-R", self.car.model)
        self.assertEqual(15, self.car.fuel_consumption)
        self.assertEqual(75, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_no_make_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_no_model_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_with_zero_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_with_negative_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_zero_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_negative_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_with_negative_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_withe_zero_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_not_full_tank(self):
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_car_more_than_capacity_expect_fill_to_capacity(self):
        self.car.refuel(100)
        self.assertEqual(75, self.car.fuel_amount)

    def test_drive_more_than_possible_raises_exception(self):
        self.car.fuel_amount = 20

        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_valid_distance_expect_fuel_amount_decrease(self):
        self.car.fuel_amount = 75
        self.car.drive(100)

        self.assertEqual(60, self.car.fuel_amount)


if __name__ == "__main__":
    main()
