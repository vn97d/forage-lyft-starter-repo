from datetime import date
from serviceable import Serviceable


class Battery(Serviceable):
    def needs_service(self) -> bool:
        pass

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        pass

class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        pass

class UpgradedSpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        super().__init__(last_service_date, current_date)

    def needs_service(self) -> bool:
        service_interval = 3 * 365  # 3 years
        days_since_last_service = (self.current_date - self.last_service_date).days
        return days_since_last_service >= service_interval
