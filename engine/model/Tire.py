from datetime import date
from serviceable import Serviceable


class Tire(Serviceable):
    def needs_service(self) -> bool:
        pass

class carrigan_tires(Tire):
    def __init__(self ,tire_wear_array):
        self.tire_wear_array = tire_wear_array
        

    def needs_service(self) -> bool:
        return any(wear >= 0.9 for wear in self.tire_wear_array)

class octoprime_tires(Tire):
    def __init__(self ,tire_wear_array):
         self.tire_wear_array = tire_wear_array

    def needs_service(self) -> bool:
        return sum(self.tire_wear_array) >= 3.0