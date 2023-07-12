from datetime import date
from car import Car
from engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from Battery import SpindlerBattery, NubbinBattery
from engine.model import Battery
from engine.model.engine import Engine

class ConcreteCar(Car):
    def __init__(self, engine: Engine, battery: Battery):
        super().__init__(engine, battery)

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
    

class CarFactory:

    @staticmethod
    def create_car(engine: Engine, battery: Battery) -> ConcreteCar:
        return ConcreteCar(engine, battery)
    
    @staticmethod
    def create_calliope(
        current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int
    ) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return CarFactory.create_car(engine, battery)

    @staticmethod
    def create_glissade(
        current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int
    ) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return CarFactory.create_car(engine, battery)

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = NubbinBattery(last_service_date, current_date)
        return CarFactory.create_car(engine, battery)

    @staticmethod
    def create_rorschach(
        current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int
    ) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return CarFactory.create_car(engine, battery)

    @staticmethod
    def create_thovex(
        current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int
    ) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return CarFactory.create_car(engine, battery)