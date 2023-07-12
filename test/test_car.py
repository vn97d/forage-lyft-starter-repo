import unittest
from datetime import date
from car import Car
from engine.model.car_factory import CarFactory
from engine.model.engine import CapuletEngine,WilloughbyEngine,SternmanEngine
from engine.model.Battery import SpindlerBattery,NubbinBattery


class EngineTestCase(unittest.TestCase):
    def setUp(self):
        self.capulet_engine = CapuletEngine(last_service_mileage=5000, current_mileage=7000)
        self.sternman_engine = SternmanEngine(warning_light_on=True)
        self.willoughby_engine = WilloughbyEngine(last_service_mileage=5000, current_mileage=7000)

    def test_needs_service(self):
        self.assertTrue(self.capulet_engine.needs_service())
        self.assertTrue(self.sternman_engine.needs_service())
        self.assertTrue(self.willoughby_engine.needs_service())

        self.capulet_engine.current_mileage = 5500
        self.assertFalse(self.capulet_engine.needs_service())

        self.sternman_engine.warning_light_on = False
        self.assertFalse(self.sternman_engine.needs_service())

        self.willoughby_engine.current_mileage = 5500
        self.assertFalse(self.willoughby_engine.needs_service())

    def test_invalid_engine(self):
        with self.assertRaises(AttributeError):
            engine = CapuletEngine(last_service_mileage=5000, current_mileage=7000)
            # Trying to access an invalid attribute
            engine.invalid_attribute


class BatteryTestCase(unittest.TestCase):
    def setUp(self):
        self.spindler_battery = SpindlerBattery(last_service_date=date(2022, 1, 1), current_date=date(2023, 1, 1))
        self.nubbin_battery = NubbinBattery(last_service_date=date(2022, 1, 1), current_date=date(2023, 1, 1))

    def test_needs_service(self):
        self.assertTrue(self.spindler_battery.needs_service())
        self.assertTrue(self.nubbin_battery.needs_service())

        self.spindler_battery.current_date = date(2023, 7, 1)
        self.assertFalse(self.spindler_battery.needs_service())

        self.nubbin_battery.current_date = date(2023, 7, 1)
        self.assertFalse(self.nubbin_battery.needs_service())

    def test_invalid_battery(self):
        with self.assertRaises(AttributeError):
            battery = SpindlerBattery(last_service_date=date(2022, 1, 1), current_date=date(2023, 1, 1))
            # Trying to access an invalid attribute
            battery.invalid_attribute


class CarTestCase(unittest.TestCase):
    def test_needs_service(self):
        car_needs_service = CarFactory.create_calliope(
            current_date=date.today(),
            last_service_date=date(2021, 1, 1),
            current_mileage=10000,
            last_service_mileage=8000
        )
        self.assertTrue(car_needs_service.needs_service())

        car_does_not_need_service = CarFactory.create_glissade(
            current_date=date.today(),
            last_service_date=date(2021, 1, 1),
            current_mileage=5500,
            last_service_mileage=5000
        )
        self.assertFalse(car_does_not_need_service.needs_service())


if __name__ == "__main__":
    unittest.main()